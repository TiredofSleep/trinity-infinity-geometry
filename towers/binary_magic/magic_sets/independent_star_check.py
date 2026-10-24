"""
star_independent.py: a second, independent check of the graph-star magic sets (magic_sets/THEOREM.md).

Written from the theorem statement alone, with no code from magic_sets/ or its referee. Paulis are
(x, z, phase) words; products track the phase exactly; F2 linear algebra decides clashes; and the
qubit count is decided by solving for the whole space of commutation patterns ("Gram matrices") that
the context structure allows, then taking ranks.

For a graph G: one qubit per vertex; observables X_v, Y_v and M_S (Y on S, X elsewhere) for
S in F = {empty} + E; contexts: the GHZ context {M_S} and a local context per S.
"""
import itertools, sys
from collections import Counter

FAILS = []
def check(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'} {name}")
    if not cond:
        FAILS.append(name)

# ---- Paulis: (x, z, k) means i^k X^x Z^z, with x, z bit masks over the qubits
def pmul(a, b):
    x1, z1, k1 = a; x2, z2, k2 = b
    sign = bin(z1 & x2).count("1") & 1                      # Z^z1 X^x2 = (-1)^(z1.x2) X^x2 Z^z1
    return (x1 ^ x2, z1 ^ z2, (k1 + k2 + 2 * sign) % 4)
def commute(a, b):
    return (bin(a[0] & b[1]).count("1") + bin(a[1] & b[0]).count("1")) % 2 == 0
def single(kind, v):
    return {"X": (1 << v, 0, 0), "Y": (1 << v, 1 << v, 1)}[kind]          # Y = i X Z
def M(S, n):
    zs = sum(1 << v for v in S)
    return ((1 << n) - 1, zs, len(S) % 4)                                  # i^|S| X^all Z^S

def star(n, edges):
    F = [frozenset()] + [frozenset(e) for e in edges]
    obs = {("X", v): single("X", v) for v in range(n)}
    obs.update({("Y", v): single("Y", v) for v in range(n)})
    obs.update({("M", S): M(S, n) for S in F})
    ctx = [[("M", S) for S in F]]
    for S in F:
        ctx.append([("Y", v) if v in S else ("X", v) for v in range(n)] + [("M", S)])
    return obs, ctx

def product(ops):
    p = (0, 0, 0)
    for o in ops:
        p = pmul(p, o)
    return p

def rank_f2(rows):
    rows, r = [x for x in rows if x], 0
    piv = []
    for x in rows:
        for b in piv:
            x = min(x, x ^ b)
        if x:
            piv.append(x)
    return len(piv)

def solvable(A_rows, s_bits):
    """Is A y = s solvable over F2? (A as row bit masks over the observables; s as bits.)"""
    aug = [(row << 1) | b for row, b in zip(A_rows, s_bits)]
    return rank_f2(aug) == rank_f2([r << 1 for r in A_rows])

def analyse(name, n, edges, expect_critical):
    print(f"\n{name}: n = {n}, |E| = {len(edges)}")
    obs, ctx = star(n, edges)
    keys = list(obs)
    idx = {k: i for i, k in enumerate(keys)}
    V = len(keys)
    check(f"{V} observables, all distinct and not the identity (2n + |E| + 1 = {2 * n + len(edges) + 1})",
          V == 2 * n + len(edges) + 1 and len({o[:2] for o in obs.values()}) == V and all(o[:2] != (0, 0) for o in obs.values()))
    signs = []
    ok = True
    for c in ctx:
        ops = [obs[k] for k in c]
        ok &= all(commute(a, b) for a, b in itertools.combinations(ops, 2))
        p = product(ops)
        ok &= p[0] == 0 and p[1] == 0 and p[2] in (0, 2)
        signs.append(1 if p[2] == 2 else 0)
    check(f"{len(ctx)} contexts, each of commuting observables multiplying to +-I", ok)
    check(f"exactly one negative context, the GHZ one (signs {signs})", signs == [1] + [0] * (len(ctx) - 1))
    deg = Counter(k for c in ctx for k in c)
    check("every observable lies in an even number of contexts", all(d % 2 == 0 for d in deg.values()))
    A = [sum(1 << idx[k] for k in c) for c in ctx]
    check("it is a clash: no +-1 assignment satisfies every context", not solvable(A, signs))
    minimal = True
    for r in range(1, len(ctx)):
        for sub in itertools.combinations(range(len(ctx)), r):
            even = all(sum((A[i] >> j) & 1 for i in sub) % 2 == 0 for j in range(V))
            if even and sum(signs[i] for i in sub) % 2 == 1:
                minimal = False
    check("minimal: no proper set of contexts is a clash", minimal)

    # criticality: every commuting subset with product +-I counts as a context
    vals = [obs[k] for k in keys]
    comm = [[commute(a, b) for b in vals] for a in vals]
    cands = []
    def grow(start, chosen, prod):
        if len(chosen) >= 2 and prod[0] == 0 and prod[1] == 0:
            cands.append((tuple(chosen), 1 if prod[2] == 2 else 0))
        for j in range(start, V):
            if all(comm[i][j] for i in chosen):
                grow(j + 1, chosen + [j], pmul(prod, vals[j]))
    grow(0, [], (0, 0, 0))
    given = {tuple(sorted(idx[k] for k in c)) for c in ctx}
    extra = [c for c, s in cands if c not in given]
    Arows = [sum(1 << i for i in c) for c, s in cands]
    sv = [s for c, s in cands]
    clash_after = []
    for o in range(V):
        keep = [(r, s) for r, s in zip(Arows, sv) if not (r >> o) & 1]
        clash_after.append(not solvable([r for r, s in keep], [s for r, s in keep]))
    critical = not any(clash_after)
    print(f"     {len(cands)} commuting +-I subsets in all; {len(extra)} beyond the given contexts")
    check(f"critical (no clash survives deleting any one observable): {critical}, expected {expect_critical}",
          critical == expect_critical)

    # genuineness: the space of Gram matrices on the 2n single-qubit observables that the contexts allow
    singles = [("X", v) for v in range(n)] + [("Y", v) for v in range(n)]
    sidx = {k: i for i, k in enumerate(singles)}
    pairs = list(itertools.combinations(range(2 * n), 2))
    pidx = {p: i for i, p in enumerate(pairs)}
    def vec_of(k):                                          # an observable's image as a set of singles
        if k[0] in "XY":
            return {sidx[k]}
        S = k[1]
        return {sidx[("Y", v)] if v in S else sidx[("X", v)] for v in range(n)}
    def omega(a, b):                                        # the symplectic product, linear in the Gram entries
        out = 0
        for i in a:
            for j in b:
                if i != j:
                    out ^= 1 << pidx[(min(i, j), max(i, j))]
        return out
    eqs = []
    for c in ctx:
        for a, b in itertools.combinations(c, 2):
            e = omega(vec_of(a), vec_of(b))
            if e:
                eqs.append(e)
    # the solution space of eqs (each eq: XOR of chosen Gram entries = 0)
    m = len(pairs)
    basis, pivcols = [], []
    rows = []
    for e in eqs:
        for (pc, r) in rows:
            if (e >> pc) & 1:
                e ^= r
        if e:
            pc = e.bit_length() - 1
            rows = [(p, r ^ e if (r >> pc) & 1 else r) for p, r in rows]
            rows.append((pc, e))
    pivots = {p for p, r in rows}
    free = [c for c in range(m) if c not in pivots]
    sols = []
    for bits in range(1 << len(free)):
        g = 0
        for t, c in enumerate(free):
            if (bits >> t) & 1:
                g |= 1 << c
        for p, r in rows:
            if bin(r & g & ~(1 << p)).count("1") % 2:
                g |= 1 << p
        sols.append(g)
    def gram(g):
        G = [[0] * (2 * n) for _ in range(2 * n)]
        for (i, j), t in pidx.items():
            G[i][j] = G[j][i] = (g >> t) & 1
        return G
    def ghz_sign(g):                                        # local contexts set to +I; then the GHZ product's sign
        G = gram(g)
        seq = []
        for S in [k[1] for k in ctx[0]]:
            seq += sorted(vec_of(("M", S)))
        inv = 0
        for a in range(len(seq)):                           # bubble the singles together; count anticommuting swaps
            for b in range(a + 1, len(seq)):
                if seq[a] > seq[b]:
                    inv ^= G[seq[a]][seq[b]]
        return inv
    def rank_gram(g):
        return rank_f2([sum(G_row[j] << j for j in range(2 * n)) for G_row in gram(g)])
    magic = [(rank_gram(g), g) for g in sols if all(gram(g)[i][j] == gram(g)[j][i] for i in range(2*n) for j in range(2*n)) and ghz_sign(g) == 1]
    print(f"     Gram space: dimension {len(free)}, {len(sols)} patterns; ranks of the magic ones: "
          f"{sorted(Counter(r for r, g in magic).items())}")
    check(f"genuine {n}-qubit: every magic pattern has rank >= 2n = {2 * n}", magic and min(r for r, g in magic) >= 2 * n)
    return V

analyse("C5 star (the 16-observable record)", 5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], True)
analyse("C7 star", 7, [(i, (i + 1) % 7) for i in range(7)], True)
analyse("C3 star (the Mermin pentagram)", 3, [(0, 1), (1, 2), (2, 0)], True)
analyse("triangle + C4 sharing a vertex (n = 6)", 6, [(0, 1), (1, 2), (2, 0), (0, 3), (3, 4), (4, 5), (5, 0)], False)

print()
print("ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
