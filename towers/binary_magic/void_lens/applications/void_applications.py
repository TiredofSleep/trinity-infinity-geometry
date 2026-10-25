#!/usr/bin/env python3
"""
void_applications.py -- applications/PREREG.md, tests A1-A6: the void lens's counting, run on published
results in four fields. Run from binary_magic/:  python3 void_lens/applications/void_applications.py
Prints ASCII only. Exact integer ranks for A1-A3; A6 uses floating determinants with a 1e-8 threshold
(entries have modulus 1, so nonzero 7x7 minors are far from it; the minimum is printed).
"""
import itertools, math, os, random, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from void_lens_core import rank_exact
import sympy as sp

res = {}
rng = random.Random(2026)

# ---------------- A1, A2: zero modes of nanographenes (Hueckel model = adjacency matrix of the carbon graph)
def flake(hexes):
    verts, edges = {}, set()
    def vid(x, y):
        key = (round(x, 4) + 0.0, round(y, 4) + 0.0)
        return verts.setdefault(key, len(verts))
    for q, r in hexes:
        cx, cy = math.sqrt(3) * (q + r / 2), 1.5 * r
        vs = [vid(cx + math.cos(math.radians(60 * k + 30)), cy + math.sin(math.radians(60 * k + 30))) for k in range(6)]
        for k in range(6): edges.add(tuple(sorted((vs[k], vs[(k + 1) % 6]))))
    return len(verts), sorted(edges)

def adjacency(n, edges):
    A = [[0] * n for _ in range(n)]
    for i, j in edges: A[i][j] = A[j][i] = 1
    return A

def two_colour(n, edges):
    nb = [[] for _ in range(n)]
    for i, j in edges: nb[i].append(j); nb[j].append(i)
    col = [None] * n; col[0] = 0; st = [0]
    while st:
        u = st.pop()
        for w in nb[u]:
            if col[w] is None: col[w] = 1 - col[u]; st.append(w)
            assert col[w] != col[u]
    return col, nb

print("A1: triangulenes")
a1 = True
for m in (2, 3, 4):
    hexes = [(q, r) for q in range(m) for r in range(m) if q + r <= m - 1]
    n, E = flake(hexes); col, _ = two_colour(n, E)
    NA, NB = col.count(0), col.count(1)
    nul = n - rank_exact(adjacency(n, E))
    name = {2: "phenalenyl", 3: "[3]triangulene", 4: "[4]triangulene"}[m]
    print(f"  {name:15s} C{n}: sublattices {max(NA, NB)}/{min(NA, NB)}, imbalance {abs(NA - NB)}, zero modes {nul}")
    a1 &= nul == abs(NA - NB) == m - 1
res["A1"] = a1

print("A2: two phenalenyls, opposite majorities, one joining bond")
n, E = flake([(0, 0), (1, 0), (0, 1)]); col, nb = two_colour(n, E)
maj = 0 if col.count(0) > col.count(1) else 1
A = sp.Matrix(adjacency(n, E)); z = A.nullspace()[0]             # the phenalenyl zero mode
deg2 = [v for v in range(n) if len(nb[v]) == 2]
min_atom = next(v for v in deg2 if col[v] != maj)                   # minority: zero amplitude
maj_atom = next(v for v in deg2 if col[v] == maj and z[v] != 0)     # majority, nonzero amplitude
assert z[min_atom] == 0
def dimer(a, b):
    E2 = list(E) + [(i + n, j + n) for i, j in E] + [(a, b + n)]
    col2 = col + [1 - c for c in col]                                # second copy: majority on the other sublattice
    assert col2[a] != col2[b + n]
    N = 2 * n
    return col2.count(0), col2.count(1), N - rank_exact(adjacency(N, E2))
NA, NB, nul_min = dimer(min_atom, min_atom)
_, _, nul_maj = dimer(maj_atom, maj_atom)
print(f"  sublattices {NA}/{NB} (balanced); minority-to-minority bond: {nul_min} zero modes; "
      f"majority-to-majority: {nul_maj}")
res["A2"] = NA == NB and nul_min == 2 and nul_maj == 0

# ---------------- A3: symmetry-extended Maxwell count (two mirror-image triangles, three cross bars)
print("A3: mirror-symmetric frame, 6 joints, 9 bars")
L = [(-2, 0), (-3, 2), (-1, 3)]; Rt = [(-x, y) for x, y in L]
P = L + Rt
bars = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (3, 5), (0, 3), (1, 4), (2, 5)]
def rigidity(P):
    Rm = []
    for i, j in bars:
        row = [0] * (2 * len(P))
        dx, dy = P[i][0] - P[j][0], P[i][1] - P[j][1]
        row[2 * i], row[2 * i + 1], row[2 * j], row[2 * j + 1] = dx, dy, -dx, -dy
        Rm.append(row)
    return Rm
Rm = rigidity(P); rk = rank_exact(Rm)
mech, stress = 2 * 6 - 3 - rk, len(bars) - rk
sig_j = [3, 4, 5, 0, 1, 2]                                         # joint permutation of the mirror x -> -x
def sym_part(v, s):                                                 # s = +1 symmetric, -1 antisymmetric velocity field
    w = [0] * 12
    for i in range(6):
        k = sig_j[i]
        w[2 * k] += s * (-v[2 * i]); w[2 * k + 1] += s * v[2 * i + 1]
    return [(a + b) / 2 for a, b in zip(v, w)]
K = sp.Matrix(Rm).nullspace()
anti = sp.Matrix([sym_part(list(k), -1) for k in K]).rank(); symm = sp.Matrix([sym_part(list(k), 1) for k in K]).rank()
S = sp.Matrix(Rm).T.nullspace()                                     # self-stresses
bar_perm = [3, 4, 5, 0, 1, 2, 6, 7, 8]
stress_sym = all(all(s_[bar_perm[b]] == s_[b] for b in range(9)) for s_ in S)
P2 = list(P); P2[5] = (1, 4)                                        # break the mirror
rk2 = rank_exact(rigidity(P2))
print(f"  symmetric position: rank {rk}, mechanisms {mech}, self-stresses {stress}; velocity kernel splits "
      f"{anti} antisymmetric (incl. x-translation, rotation) / {symm} symmetric (y-translation)")
print(f"  self-stress symmetric under the mirror: {stress_sym}; generic perturbation: rank {rk2}")
res["A3"] = rk == 8 and mech == 1 and stress == 1 and anti == 3 and symm == 1 and stress_sym and rk2 == 9

# ---------------- A4: DES complementation property (needs pycryptodome; skipped, not passed, without it)
try:
    from Crypto.Cipher import DES
except ImportError:
    DES = None
    print("A4: SKIPPED (pycryptodome is not installed: pip install pycryptodome). Not scored here.")
if DES is not None:
    inv = lambda b: bytes(255 - x for x in b)
    ok = True
    for _ in range(2000):
        k, x = bytes(rng.randrange(256) for _ in range(8)), bytes(rng.randrange(256) for _ in range(8))
        if DES.new(inv(k), DES.MODE_ECB).encrypt(inv(x)) != inv(DES.new(k, DES.MODE_ECB).encrypt(x)): ok = False
    print(f"A4: DES complementation on 2,000 random (key, block): {ok}")
    res["A4"] = ok

# ---------------- A5: complementary linear structure -> half the Walsh spectrum vanishes
ok = True
for _ in range(200):
    a = rng.randrange(1, 256); f = [None] * 256
    for x in range(256):
        if f[x] is None: f[x] = rng.randrange(2); f[x ^ a] = 1 - f[x]
    W = [sum((-1) ** (f[x] ^ (bin(u & x).count("1") & 1)) for x in range(256)) for u in range(256)]
    zeros_needed = [u for u in range(256) if bin(u & a).count("1") % 2 == 0]
    if len(zeros_needed) != 128 or any(W[u] for u in zeros_needed): ok = False
print(f"A5: 200 random 8-bit functions with f(x^a) = f(x)^1: Walsh zero on all 128 u with u.a = 0: {ok}")
res["A5"] = ok

# ---------------- A6: Chebotarev (prime) vs composite DFT minors
def minors(n):
    F = np.exp(2j * np.pi * np.outer(range(n), range(n)) / n)
    vals = []
    for k in range(1, n + 1):
        for R in itertools.combinations(range(n), k):
            for C in itertools.combinations(range(n), k):
                vals.append(abs(np.linalg.det(F[np.ix_(R, C)])))
    return vals
m7, m9 = minors(7), minors(9)
z7, z9 = sum(v < 1e-8 for v in m7), sum(v < 1e-8 for v in m9)
comb = [1 if t in (0, 3, 6) else 0 for t in range(9)]
X = np.fft.fft(comb); blind = sum(abs(v) < 1e-9 for v in X)
print(f"A6: DFT_7: {len(m7)} minors, zero: {z7}, smallest |minor| {min(m7):.3f}; DFT_9: {len(m9)} minors, zero: {z9};"
      f" comb {{0,3,6}} invisible at {blind} of 9 frequencies")
res["A6"] = z7 == 0 and z9 > 0 and blind == 6

print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
