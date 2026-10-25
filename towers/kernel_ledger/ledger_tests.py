#!/usr/bin/env python3
"""
ledger_tests.py -- kernel_ledger/PREREG.md, tests K1-K5: does the observed kernel equal the forced count
(Levels 0-2 of THEORY.md) plus a value-forced residue (Level 3), in four domains?
Run from kernel_ledger/:  python3 ledger_tests.py        Prints ASCII only.
Exact integer ranks except K3 (DFT minors: floating determinants; the gap between zero and the smallest
nonzero |minor| is printed so the threshold can be judged).
"""
import itertools, math, os, random, sys
from collections import Counter
import numpy as np
import networkx as nx
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(1024)
res = {}

# ------------------------------------------------------------- exact integer linear algebra
def rank_exact(A):
    A = [list(r) for r in A]
    if not A: return 0
    m, n = len(A), len(A[0]); r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None: continue
        A[r], A[p] = A[p], A[r]
        for i in range(m):
            if i != r and A[i][c]:
                f, g = A[r][c], A[i][c]
                A[i] = [f * x - g * y for x, y in zip(A[i], A[r])]
                gg = 0
                for x in A[i]: gg = math.gcd(gg, x)
                if gg > 1: A[i] = [x // gg for x in A[i]]
        r += 1
        if r == m: break
    return r

def det_bareiss(A):
    A = [list(r) for r in A]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((r for r in range(k + 1, n) if A[r][k]), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def matching_deficiency(G):
    nu = len(nx.max_weight_matching(G, maxcardinality=True))
    return G.number_of_nodes() - 2 * nu

def adjacency(G, weights=None):
    idx = {v: i for i, v in enumerate(G.nodes())}; n = len(idx)
    A = [[0] * n for _ in range(n)]
    for u, v in G.edges():
        w = 1 if weights is None else weights[(u, v)]
        A[idx[u]][idx[v]] = A[idx[v]][idx[u]] = w
    return A

# ------------------------------------------------------------- K1: random benzenoids
def flake(hexes):
    verts, edges = {}, set()
    def vid(x, y):
        return verts.setdefault((round(x, 4) + 0.0, round(y, 4) + 0.0), len(verts))
    for q, r in hexes:
        cx, cy = math.sqrt(3) * (q + r / 2), 1.5 * r
        vs = [vid(cx + math.cos(math.radians(60 * k + 30)), cy + math.sin(math.radians(60 * k + 30))) for k in range(6)]
        for k in range(6): edges.add(tuple(sorted((vs[k], vs[(k + 1) % 6]))))
    G = nx.Graph(); G.add_edges_from(edges); return G

NB = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
k1_ok = True; k1n = 0; k1_null = Counter()
while k1n < 300:
    h = rng.randint(4, 12); cl = {(0, 0)}
    while len(cl) < h:
        q, r = rng.choice(sorted(cl)); dq, dr = rng.choice(NB); cl.add((q + dq, r + dr))
    G = flake(cl)
    if G.number_of_nodes() - G.number_of_edges() + len(cl) != 1: continue        # holes: not a benzenoid
    k1n += 1
    nul = G.number_of_nodes() - rank_exact(adjacency(G)); d = matching_deficiency(G)
    k1_null[nul] += 1
    if nul != d: k1_ok = False
print(f"K1 benzenoids: {k1n} samples, nullity == n - 2nu in all: {k1_ok}; nullity counts {dict(sorted(k1_null.items()))}")
res["K1"] = k1_ok

# ------------------------------------------------------------- K2: site-diluted square lattice
k2 = Counter(); k2b_ok = True; done = 0
while done < 300:
    L = 8; keep = {(i, j) for i in range(L) for j in range(L) if rng.random() < 0.75}
    G = nx.Graph(); G.add_nodes_from(keep)
    for (i, j) in keep:
        for d in ((1, 0), (0, 1)):
            if (i + d[0], j + d[1]) in keep: G.add_edge((i, j), (i + d[0], j + d[1]))
    comp = max(nx.connected_components(G), key=len)
    if len(comp) < 12: continue
    H = G.subgraph(comp).copy(); done += 1
    d = matching_deficiency(H)
    nul = H.number_of_nodes() - rank_exact(adjacency(H))
    W = {}
    for u, v in H.edges(): W[(u, v)] = W[(v, u)] = rng.randint(1, 10 ** 6)
    nulw = H.number_of_nodes() - rank_exact(adjacency(H, W))
    k2["excess" if nul > d else "exact"] += 1
    if nulw != d: k2b_ok = False
print(f"K2 diluted square lattice: {done} clusters; unweighted excess over n - 2nu in {k2['excess']} "
      f"({100 * k2['excess'] / done:.1f}%); random weights exact in all: {k2b_ok}")
res["K2a"] = k2["excess"] / done >= 0.05
res["K2b"] = k2b_ok

# ------------------------------------------------------------- K3: DFT minors and coset certificates
def subgroups(n):          # H = dZ_n for proper divisors d (H nontrivial and proper): order n/d
    return [d for d in range(2, n) if n % d == 0]

def certified(n, R, C, w):
    """Single-subgroup coset certificate for det F[R, C] = 0 (rows = times R, columns = frequencies C)."""
    for d in subgroups(n):
        H = set(range(0, n, d)); Hperp = set(range(0, n, n // d))   # H = dZ_n (order n/d), Hperp order d
        reps, seen = [], set()
        for f in sorted(C):
            if f in seen: continue
            cos = {(f + h) % n for h in H}
            if cos <= set(C): reps.append(f); seen |= cos
        if not reps: continue
        T = [t for t in R if t in Hperp]
        if not T: return True
        Q = np.array([[w ** (t * f) for f in reps] for t in T])
        if np.linalg.matrix_rank(Q, tol=1e-9) < len(reps): return True
    return False

def k3(n):
    w = np.exp(2j * np.pi / n); F = w ** np.outer(range(n), range(n))
    sing = unc = 0; minnz = 1e9; bad_ex = None
    for k in range(1, n + 1):
        for R in itertools.combinations(range(n), k):
            for C in itertools.combinations(range(n), k):
                dv = abs(np.linalg.det(F[np.ix_(R, C)]))
                if dv < 1e-7:
                    sing += 1
                    if not (certified(n, R, C, w) or certified(n, C, R, w)):
                        unc += 1; bad_ex = bad_ex or (R, C)
                else:
                    minnz = min(minnz, dv)
    # soundness: every certificate must point at a numerically singular minor (spot check)
    return sing, unc, minnz, bad_ex

k3r = {}
for n in (6, 8, 9, 10):
    k3r[n] = k3(n)
    s, u, mn, ex = k3r[n]
    print(f"K3 DFT_{n}: singular minors {s}, uncertified {u}, smallest nonzero |minor| {mn:.2e}" + (f", e.g. rows {ex[0]} cols {ex[1]}" if ex else ""))
# soundness spot check of the certificate itself
for n in (6, 9, 10):
    w = np.exp(2j * np.pi / n); F = w ** np.outer(range(n), range(n))
    for _ in range(3000):
        k = rng.randint(1, n); R = tuple(sorted(rng.sample(range(n), k))); C = tuple(sorted(rng.sample(range(n), k)))
        if certified(n, R, C, w): assert abs(np.linalg.det(F[np.ix_(R, C)])) < 1e-7, (n, R, C)
res["K3a"] = k3r[9][1] == 0
res["K3b"] = k3r[8][1] == 0
res["K3c"] = k3r[6][1] > 0 or k3r[10][1] > 0

# ------------------------------------------------------------- K4: mirror-symmetric frameworks
def rigidity(P, bars):
    Rm = []
    for i, j in bars:
        row = [0] * (2 * len(P)); dx, dy = P[i][0] - P[j][0], P[i][1] - P[j][1]
        row[2 * i], row[2 * i + 1], row[2 * j], row[2 * j + 1] = dx, dy, -dx, -dy
        Rm.append(row)
    return Rm

def sectors(Rm, m):
    """dims of (antisymmetric, symmetric) parts of the velocity kernel; joints 0..m-1 = L_i, m..2m-1 = R_i."""
    K = sp.Matrix(Rm).nullspace()
    def part(v, s):
        out = [0] * (4 * m)
        for i in range(2 * m):
            k = (i + m) % (2 * m)
            out[2 * k] += -s * v[2 * i]; out[2 * k + 1] += s * v[2 * i + 1]
        return [sp.Rational(1, 2) * (a + b) for a, b in zip(v, out)]
    anti = sp.Matrix([part(list(k), -1) for k in K]).rank() if K else 0
    sym = sp.Matrix([part(list(k), 1) for k in K]).rank() if K else 0
    return anti, sym

k4a_ok = True; gen = exact = 0; k4n = 0; tally = Counter()
while k4n < 300:
    m = rng.choice([3, 4, 5]); j = 2 * m; b = 2 * j - 3
    bs = rng.choice([x for x in (1, 3, 5) if x <= m])
    cross = rng.sample(range(m), bs)
    orbits = [("LL", i, k) for i in range(m) for k in range(i + 1, m)] + [("LR", i, k) for i in range(m) for k in range(i + 1, m)]
    need = (b - bs) // 2
    if need > len(orbits): continue
    chosen = rng.sample(orbits, need)
    bars = [(i, i + m) for i in cross]
    for t, i, k in chosen:
        if t == "LL": bars += [(i, k), (i + m, k + m)]
        else: bars += [(i, k + m), (k, i + m)]
    Lp = [(-rng.randint(1, 40), rng.randint(-40, 40)) for _ in range(m)]
    P = Lp + [(-x, y) for x, y in Lp]
    if len(set(P)) < j: continue
    k4n += 1
    rk = rank_exact(rigidity(P, bars)); mech = 2 * j - 3 - rk
    anti, sym = sectors(rigidity(P, bars), m)
    anti_mech, sym_mech = anti - 2, sym - 1                      # remove x-translation + rotation, y-translation
    forced = (bs - 1) // 2
    if anti_mech < forced: k4a_ok = False
    Pg = [(rng.randint(-40, 40), rng.randint(-40, 40)) for _ in range(j)]
    if rank_exact(rigidity(Pg, bars)) == 2 * j - 3:
        gen += 1; exact += mech == forced
    tally[(bs, mech)] += 1
print(f"K4 frameworks: {k4n} samples; antisymmetric mechanisms >= (b_sigma-1)/2 always: {k4a_ok}; "
      f"generically rigid graphs {gen}, exactly the forced count in {exact} ({100 * exact / max(gen, 1):.1f}%)")
print("   (b_sigma, mechanisms) counts:", dict(sorted(tally.items())))
res["K4a"] = k4a_ok
res["K4b"] = gen > 0 and exact / gen >= 0.90

# ------------------------------------------------------------- K5: order-6 magic squares
def local_certs(M):
    n = len(M); out = []
    for lines in ([list(c) for c in zip(*M)], [list(r) for r in M]):
        for k in range(2, n - 1):
            for S in itertools.combinations(range(n), k):
                v = [sum(lines[j][i] for j in S) for i in range(n)]
                if len(set(v)) == 1: out.append((S, v[0]))
    return out

def global_index(M, c):
    n = len(M); pos = {M[i][j]: (i, j) for i in range(n) for j in range(n)}
    mp = {(i, j): pos.get(c - M[i][j]) for i in range(n) for j in range(n)}
    if any(v is None for v in mp.values()): return None
    P = [mp[(i, 0)][0] for i in range(n)]; Q = [mp[(0, j)][1] for j in range(n)]
    if not all(mp[(i, j)] == (P[i], Q[j]) for i in range(n) for j in range(n)): return None
    return abs((sum(i == x for i, x in enumerate(P)) + sum(j == x for j, x in enumerate(Q))) / 2 - 1)

raw = [list(map(int, l.split())) for l in open(os.path.join(HERE, "squares6_annealed.txt"))]
sq = {}
for r in raw:
    M = [r[6 * i:6 * i + 6] for i in range(6)]
    assert sorted(r) == list(range(1, 37))
    L = [sum(x) for x in M] + [sum(x) for x in zip(*M)] + [sum(M[i][i] for i in range(6)), sum(M[i][5 - i] for i in range(6))]
    assert set(L) == {111}
    sq[tuple(r)] = M
sing = [M for M in sq.values() if det_bareiss(M) == 0]
acc = [M for M in sing if not local_certs(M) and not ((global_index(M, 37) or 0) >= 1)]
rate = len(sing) / len(sq)
print(f"K5 order 6: {len(sq)} distinct squares, {len(sing)} singular ({100 * rate:.3f}%), with no void certificate {len(acc)}")
res["K5a"] = rate < 0.0019
res["K5b"] = None if len(sing) < 5 else (len(acc) / len(sing) > 5 / 19)

print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})
