"""Independent audit check for J29 (the Lo Shu's eight orientations mod 3).

Fresh code.  Checks every theorem of the note, the 'mod 3 is unique' sweep, the
kappa witness, the diagonal lemma (and its classical odd-order form), and the
equational-theory (ETP) profile sizes by re-enumerating the 4694 ETP laws.

Run:  python -I check_j29.py
"""
from itertools import product, permutations
import random
import sys
import time

import numpy as np

T0 = time.time()
FAIL = []


def check(label, ok):
    print(("  [ok]   " if ok else "  [FAIL] ") + label)
    if not ok:
        FAIL.append(label)


L = np.array([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
D = np.array([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]])


def orientations(M):
    out = []
    R = M.copy()
    for _ in range(4):
        out.append(R.copy())
        out.append(R.T.copy())
        R = np.rot90(R)
    return out


def is_comm(T):
    return bool((T == T.T).all())


def is_latin(T):
    n = T.shape[0]
    s = set(range(n))
    return all(set(r) == s for r in T.tolist()) and all(set(c) == s for c in T.T.tolist())


def kappa(M):
    M = M.astype(np.int64)
    return int(np.trace(M @ M) - np.trace(M) ** 2)


print("=" * 72)
print("1. The Lo Shu's orientations mod 3 (Theorems A-F)")
print("=" * 72)
O = orientations(L)
keys = {tuple(M.flatten()) for M in O}
check(f"8 distinct orientations: {len(keys)}", len(keys) == 8)
tabs = {}
for M in O:
    k = tuple((M % 3).flatten())
    tabs.setdefault(k, []).append(M)
check(f"4 distinct mod-3 tables, each from 2 orientations: {sorted(len(v) for v in tabs.values())}",
      len(tabs) == 4 and all(len(v) == 2 for v in tabs.values()))
x = np.arange(3)[:, None]
y = np.arange(3)[None, :]
forms = {"x+y": (x + y) % 3, "1-x-y": (1 - x - y) % 3, "x-y+2": (x - y + 2) % 3, "y-x+2": (y - x + 2) % 3}
found = {name: any((np.array(k).reshape(3, 3) == F).all() for k in tabs) for name, F in forms.items()}
check(f"the four tables are exactly x+y, 1-x-y, x-y+2, y-x+2 (mod 3): {found}", all(found.values()))
check("the Lo Shu itself reduces to x - y + 2 (mod 3)", ((L % 3) == forms["x-y+2"]).all())
T = [np.array(k).reshape(3, 3) for k in tabs]
check("all four are Latin squares (quasigroups)", all(is_latin(t) for t in T))
check("exactly two are commutative", sum(is_comm(t) for t in T) == 2)
nc = [t for t in T if not is_comm(t)]
check("the two non-commutative tables are each other's transposes (opposite magmas)",
      (nc[0] == nc[1].T).all())
# Why Latin: de la Hire -- L - 1 written in base 3 is two orthogonal Latin squares
hi, lo = (L - 1) // 3, (L - 1) % 3
check("de la Hire: digits of L-1 in base 3 are two orthogonal Latin squares, and L mod 3 = (low digit + 1) mod 3",
      is_latin(hi) and is_latin(lo) and len(set(zip(hi.flatten(), lo.flatten()))) == 9
      and ((L % 3) == (lo + 1) % 3).all())

print("=" * 72)
print("2. The 'cumulant' kappa = Tr(M^2) - Tr(M)^2 (Theorem E)")
print("=" * 72)
ks = [(kappa(M), is_comm(M % 3)) for M in O]
check(f"kappa = -48 on the 4 commutative orientations, +48 on the other 4: {sorted(set(ks))}",
      sorted(set(ks)) == [(-48, True), (48, False)])


def e2(M):
    return sum(int(M[i, i] * M[j, j] - M[i, j] * M[j, i]) for i in range(3) for j in range(i + 1, 3))


check("kappa = -2 * (sum of principal 2x2 minors): it is a characteristic-polynomial coefficient",
      all(kappa(M) == -2 * e2(M) for M in O))
ev_L = np.sort_complex(np.linalg.eigvals(L.astype(float)))
ev_R = np.sort_complex(np.linalg.eigvals(np.rot90(L).astype(float)))
check(f"eigenvalues: Lo Shu {np.round(ev_L, 4)} = 15, +-2 sqrt6; quarter-turn {np.round(ev_R, 4)} = 15, +-2 sqrt6 i",
      np.allclose(sorted(ev_L.real), [-2 * 6 ** .5, 2 * 6 ** .5, 15])
      and np.allclose(sorted(np.abs(ev_R.imag)), [0, 2 * 6 ** .5, 2 * 6 ** .5]))
simple = {(int((np.diag(M) ** 2).sum()), is_comm(M % 3)) for M in O}
check(f"any diagonal statistic separates the two cosets just as well, e.g. sum of squared diagonal: {sorted(simple)}",
      len(simple) == 2 and len({s[0] for s in simple}) == 2)

print("=" * 72)
print("3. Diagonal lemma, and its classical form (odd-order symmetric Latin squares)")
print("=" * 72)


def sym_latin(n):
    """All symmetric Latin squares of order n (backtracking over the upper triangle)."""
    cells = [(i, j) for i in range(n) for j in range(i, n)]
    G = [[-1] * n for _ in range(n)]
    rows = [set() for _ in range(n)]
    out = []

    def rec(k):
        if k == len(cells):
            out.append([r[:] for r in G])
            return
        i, j = cells[k]
        for s in range(n):
            if s in rows[i] or s in rows[j]:
                continue
            G[i][j] = G[j][i] = s
            rows[i].add(s)
            if i != j:
                rows[j].add(s)
            rec(k + 1)
            rows[i].discard(s)
            if i != j:
                rows[j].discard(s)
            G[i][j] = G[j][i] = -1
    rec(0)
    return out


for n in (3, 5):
    S = sym_latin(n)
    ok = all(sorted(G[i][i] for i in range(n)) == list(range(n)) for G in S)
    check(f"order {n}: all {len(S)} symmetric Latin squares have every symbol exactly once on the diagonal", ok)
random.seed(1)
ok7 = True
for _ in range(2000):                      # random isotopes P(x)+P(y) of Z/7 and Z/9-type squares
    for n in (7, 9):
        p = list(range(n))
        random.shuffle(p)
        q = list(range(n))
        random.shuffle(q)
        G = [[q[(p[i] + p[j]) % n] for j in range(n)] for i in range(n)]
        ok7 &= sorted(G[i][i] for i in range(n)) == list(range(n))
check("orders 7 and 9: 4000 random symmetric Latin squares, diagonal always a transversal", ok7)
K4 = [[i ^ j for j in range(4)] for i in range(4)]
Z4 = [[(i + j) % 4 for j in range(4)] for i in range(4)]
check("even order fails: Klein-group table diagonal = [0,0,0,0]; Z/4 diagonal = [0,2,0,2]",
      [K4[i][i] for i in range(4)] == [0] * 4 and [Z4[i][i] for i in range(4)] == [0, 2, 0, 2])
G5 = [[(i + 2 * j) % 5 for j in range(5)] for i in range(5)]
check("converse fails from order 5: x + 2y mod 5 has a transversal diagonal but is not symmetric",
      sorted(G5[i][i] for i in range(5)) == list(range(5)) and G5[0][1] != G5[1][0])
three = [np.array(t).reshape(3, 3) for t in product(range(3), repeat=9)]
lat3 = [t for t in three if is_latin(t)]
conv3 = all(is_comm(t) == (sorted(np.diag(t)) == [0, 1, 2]) for t in lat3)
check(f"order 3 only: among all {len(lat3)} Latin squares, symmetric <=> diagonal is a transversal", conv3)
dg = {(tuple(np.diag(M % 3)), is_comm(M % 3)) for M in O}
check(f"Lo Shu: orientations keeping the main diagonal 2,5,8 (= 2,2,2 mod 3) are non-commutative; "
      f"those with 6,5,4 (= 0,2,1) are commutative: {sorted(dg)}",
      all((len(set(d)) == 1) != c for d, c in dg))

print("=" * 72)
print("4. Theorem G (Durer) and the 'mod 3 is special' sweep")
print("=" * 72)
OD = orientations(D)
check(f"Durer: 8 distinct orientations", len({tuple(M.flatten()) for M in OD}) == 8)
td = {}
for M in OD:
    td.setdefault(tuple((M % 3).flatten()), []).append(M)
ncom = sum(is_comm(np.array(k).reshape(4, 4)) for k in td)
kd = sorted({(kappa(M), is_comm(M % 3)) for M in OD})
check(f"Durer mod 3: {len(td)} tables ({ncom} commutative), kappa by commutativity = {kd}",
      len(td) == 4 and ncom == 2 and kd == [(-128, True), (128, False)])


def pattern(M, m):
    c = [is_comm(Mi % m) for Mi in orientations(M)]
    return sum(c)


lo_mix = [m for m in range(2, 31) if 0 < pattern(L, m) < 8]
du_mix = [m for m in range(2, 31) if 0 < pattern(D, m) < 8]
print(f"  moduli 2..30 giving a mixed (some commutative, some not) orbit: Lo Shu {lo_mix}, Durer {du_mix}")
check("paper's tested moduli behave as stated (Lo Shu 2,4,5,7,9,10; Durer 2,4,5,6,8,10 not mixed)",
      all(m not in lo_mix for m in (2, 4, 5, 7, 9, 10)) and all(m not in du_mix for m in (2, 4, 5, 6, 8, 10)))
check("but the Lo Shu is ALSO mixed mod 6 (untested in the note): 'mod 3 is special' is only about "
      "the moduli tried", 6 in lo_mix)
check("mod 3 is the only modulus in 2..30 mixed for both squares", sorted(set(lo_mix) & set(du_mix)) == [3])

print("=" * 72)
print("5. ETP profile sizes (Sec. 7.4): re-enumerate the laws of order <= 4")
print("=" * 72)


def shapes(k):
    if k == 0:
        return ["v"]
    out = []
    for a in range(k):
        for l in shapes(a):
            for r in shapes(k - 1 - a):
                out.append(("o", l, r))
    return out


def leaves(s):
    return 1 if s == "v" else leaves(s[1]) + leaves(s[2])


def fill(s, it):
    if s == "v":
        return next(it)
    return ("o", fill(s[1], it), fill(s[2], it))


def rgs(m):
    """restricted growth strings of length m (set partitions of m leaves)."""
    def rec(pre, mx):
        if len(pre) == m:
            yield tuple(pre)
            return
        for v in range(mx + 2):
            yield from rec(pre + [v], max(mx, v))
    yield from rec([0], 0)


def flat(t):
    return [t] if isinstance(t, int) else flat(t[1]) + flat(t[2])


def relabel(t, mp):
    return mp.setdefault(t, len(mp)) if isinstance(t, int) else ("o", relabel(t[1], mp), relabel(t[2], mp))


def canon(l, r):
    best = None
    for a, b in ((l, r), (r, l)):
        mp = {}
        a2 = relabel(a, mp)
        b2 = relabel(b, mp)
        key = repr((a2, b2))
        if best is None or key < best[0]:
            best = (key, (a2, b2))
    return best


eqs = {}
for k1 in range(5):
    for k2 in range(5 - k1):
        for s1 in shapes(k1):
            for s2 in shapes(k2):
                m = leaves(s1) + leaves(s2)
                for lab in rgs(m):
                    it = iter(lab)
                    l = fill(s1, it)
                    r = fill(s2, it)
                    key, e = canon(l, r)
                    eqs[key] = e
triv = [k for k, (l, r) in eqs.items() if l == r]
laws = [e for k, e in eqs.items() if e[0] != e[1]] + [(0, 0)]
print(f"  distinct laws up to renaming and side-swap: {len(eqs)} ; trivial ones: {len(triv)}")
check(f"keeping one trivial law (x = x) gives {len(laws)} laws -- the ETP's 4694", len(laws) == 4694)


def nvars(e):
    return max(flat(e[0]) + flat(e[1])) + 1


def evaluate(t, Tab, A):
    if isinstance(t, int):
        return A[:, t]
    return Tab[evaluate(t[1], Tab, A), evaluate(t[2], Tab, A)]


assign = {v: np.array(list(product(range(3), repeat=v)), dtype=np.int64) for v in range(1, 7)}


def profile(Tab):
    S = set()
    for idx, e in enumerate(laws):
        A = assign[nvars(e)]
        if (evaluate(e[0], Tab, A) == evaluate(e[1], Tab, A)).all():
            S.add(idx)
    return S


T1 = forms["x-y+2"]
T2 = forms["x+y"]
T3 = forms["y-x+2"]
T4 = forms["1-x-y"]
P = {name: profile(t) for name, t in (("T1", T1), ("T2", T2), ("T3", T3), ("T4", T4))}
sizes = {k: len(v) for k, v in P.items()}
print("  profile sizes:", sizes, "; |T1&T4| =", len(P["T1"] & P["T4"]), "; |T2&T4| =", len(P["T2"] & P["T4"]))
check("paper: |T1| = |T3| = 179, |T2| = 60, |T4| = 313",
      sizes == {"T1": 179, "T2": 60, "T3": 179, "T4": 313})
check("paper: |T1 & T4| = 63", len(P["T1"] & P["T4"]) == 63)
check("paper: |T2 & T4| = 14", len(P["T2"] & P["T4"]) == 14)
check("opposite magmas satisfy the same number of laws (T1 vs T3)", len(P["T1"]) == len(P["T3"]))


def comm_norm(t):
    if isinstance(t, int):
        return repr(t)
    a, b = sorted([comm_norm(t[1]), comm_norm(t[2])])
    return "(" + a + "*" + b + ")"


forced = {i for i, e in enumerate(laws) if comm_norm(e[0]) == comm_norm(e[1])}
check(f"the laws true in EVERY commutative magma (equal up to swapping arguments) number {len(forced)}, "
      f"and T2 & T4 is exactly that set: {P['T2'] & P['T4'] == forced}",
      P["T2"] & P["T4"] == forced)

print("=" * 72)
print(f"elapsed {time.time() - T0:.1f} s ; failures: {len(FAIL)}")
for f_ in FAIL:
    print("  FAILED:", f_)
sys.exit(1 if FAIL else 0)
