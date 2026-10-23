"""
degree_explained.py — why the trefoil regions line up with Takemura's degree.

Takemura (arXiv:2601.06131) degree m1 = first m with APD_m != 0, where
APD_m = sum over permutations p of sgn(p) * f(p)^m and f(p) = sum_i A[i][p(i)].
Generating function: G(t) = sum_p sgn(p) e^{t f(p)} = det[e^{t A_ij}]  (entrywise exponential).

PROVED (by hand; checked here):
 P1  APD_3 = 24 det(A) / s for any 4x4 matrix with constant row sum s.  => degree 3 <=> A invertible.
 P2  If a row permutation r and column permutation c send every entry to its complement
     (A[r(i)][c(j)] = 15 - A[i][j]), then G(t) = sgn(r)sgn(c) e^{2st} G(-t).
     Even rearrangement => degree even (so not 3: singular).  Odd => degree odd.
 P3  If that rearrangement maps the main diagonal onto itself, the diagonal holds two complement
     pairs, so every bit appears twice on it: no carries (corner 000).
 P4  If the rows pair up as (i,j),(k,l) with A_j - A_i a nonzero multiple of Walsh vector h_a and
     A_l - A_k a nonzero multiple of h_b (a != b), then G == 0 (degree infinite) exactly when
     (A_i - A_k) . h_a*h_b = 0.  (Same with columns.)
VERIFIED BY EXHAUSTION (all 880): which Dudeney groups have which rearrangement, and where the
carry corners sit relative to them.
"""
import json, itertools
import numpy as np
import sympy as sp
from collections import Counter, defaultdict

S = 30
squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
perms = list(itertools.permutations(range(4)))
def sgn(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
def cvals(A):
    c = defaultdict(int)
    for p in perms:
        c[sum(A[i][p[i]] for i in range(4))] += sgn(p)
    return c
def degree(A):
    c = cvals(A)
    if all(v == 0 for v in c.values()):
        return "inf"
    m = 0
    while sum(x * v ** m for v, x in c.items()) == 0:
        m += 1
    return m
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]
    b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}
def geo(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); out += [A, tuple(r[::-1] for r in A)]
    return out
def pattern(M):
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in geo(M))
def comp_sym(M):
    A = np.array(M)
    out = []
    for r in perms:
        for c in perms:
            if (A[np.ix_(r, c)] == 15 - A).all():
                img = {(r[i], c[i]) for i in range(4)}
                where = ("diag->diag" if img == {(i, i) for i in range(4)} else
                         "diag->anti" if img == {(i, 3 - i) for i in range(4)} else "diag->other")
                out.append((sgn(r) * sgn(c), where))
    return out

deg = {M: degree(M) for M in squares}
det = {M: int(sp.Matrix(M).det()) for M in squares}

# P1
for M in squares:
    apd3 = sum(sgn(p) * sum(M[i][p[i]] for i in range(4)) ** 3 for p in perms)
    assert apd3 * S == 24 * det[M]
assert all((deg[M] == 3) == (det[M] != 0) for M in squares)
print("P1  APD_3 = 24 det/s on all 880; degree 3 <=> invertible "
      f"({sum(det[M] != 0 for M in squares)} invertible, {sum(det[M] == 0 for M in squares)} singular)")

# P2 / P3
sym = {M: comp_sym(M) for M in squares}
for M in squares:
    signs = {e for e, _ in sym[M]}
    if 1 in signs:
        assert deg[M] == "inf" or deg[M] % 2 == 0
    if -1 in signs:
        assert deg[M] == "inf" or deg[M] % 2 == 1
    if any(w == "diag->diag" for _, w in sym[M]):
        assert corner(M) == "000"
print("P2  even complement rearrangement => even degree; odd => odd degree: holds on all 880")
print("P3  rearrangement fixing the diagonal => corner 000: holds on all 880")

# P4
W = [np.array(h) for h in ((1, 1, -1, -1), (1, -1, 1, -1), (1, -1, -1, 1))]
def walsh_mult(d):
    for a, h in enumerate(W):
        lam = d[0] * h[0]
        if lam != 0 and (d == lam * h).all():
            return a
def p4(M):
    for A in (np.array(M), np.array(M).T):
        for (i, j), (k, l) in (((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))):
            a, b = walsh_mult(A[j] - A[i]), walsh_mult(A[l] - A[k])
            if a is not None and b is not None and a != b:
                hc = W[a] * W[b]
                if (A[i] - A[k]) @ hc == 0:
                    return True
    return False
assert all(p4(M) == (deg[M] == "inf") for M in squares)
print("P4  Walsh row/column pairing + cycle condition <=> degree infinite: holds on all 880 (16 squares)")

# exhaustion: Dudeney groups, rearrangement type, regions
groups = defaultdict(list)
for M in squares:
    groups[pattern(M)].append(M)
print("\nDudeney group | complement rearrangement | degrees | carry regions")
for key, g in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    kinds = Counter(("even" if e > 0 else "odd") + " " + w for M in g for e, w in sym[M][:1])
    kinds["none"] = sum(1 for M in g if not sym[M])
    kinds = {k: v for k, v in kinds.items() if v}
    print(f"  {len(g):3d} | {kinds} | {dict(Counter(deg[M] for M in g))} | "
          f"{dict(Counter(REGION[corner(M)] for M in g))}")
reg = defaultdict(Counter)
for M in squares:
    t = "none" if not sym[M] else ("even" if sym[M][0][0] > 0 else "odd")
    reg[REGION[corner(M)]][t] += 1
print("\nregion -> complement-rearrangement type:", {k: dict(v) for k, v in reg.items()})
