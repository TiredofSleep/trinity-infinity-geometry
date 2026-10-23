"""
takemura_cross.py — cross the carry cube with an independent classification.

Takemura (arXiv:2601.06131, Jan 2026) classifies the 880 squares by the first m where
APD_m = sum over permutations s of sgn(s) * (sum_i A[i][s(i)])^m is nonzero: 240 / 624 / 16
(16 = 'complete alternating', APD_m = 0 for every m). No binary, no carries in that paper.
This script reproduces his counts and crosses them with the carry corners and Dudeney's groups.
"""
import json, itertools
from collections import Counter, defaultdict

squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
perms = list(itertools.permutations(range(4)))
def sgn(p):
    return (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
def first_degree(M, shift=1):            # Takemura numbers 1..16
    c = defaultdict(int)
    for p in perms:
        c[sum(M[i][p[i]] + shift for i in range(4))] += sgn(p)
    if all(v == 0 for v in c.values()):
        return "inf"
    m = 0
    while sum(cv * v ** m for v, cv in c.items()) == 0:
        m += 1
    return m
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]
    b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))
def geo(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); out += [A, tuple(r[::-1] for r in A)]
    return out
def group_size(M, sizes={}):
    return sizes[M]
def pattern(M):
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in geo(M))

groups = defaultdict(list)
for M in squares:
    groups[pattern(M)].append(M)
gsize = {M: len(v) for v in groups.values() for M in v}
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}

deg = {M: first_degree(M) for M in squares}
assert Counter(deg.values()) == Counter({4: 624, 3: 240, "inf": 16})
print("Takemura's counts reproduced: m1 = 3: 240, 4: 624, inf: 16")
tab = defaultdict(Counter)
for M in squares:
    tab[deg[M]][(REGION[corner(M)], corner(M))] += 1
for k in (3, 4, "inf"):
    print(f"  m1 = {k}:", dict(sorted(tab[k].items())))
print("crossing squares by Dudeney group and m1:")
cx = Counter((gsize[M], deg[M]) for M in squares if REGION[corner(M)] == "crossing")
print("  ", dict(sorted(cx.items(), key=str)))
assert all(deg[M] == 4 for M in squares if REGION[corner(M)] == "center")
assert all(deg[M] == 3 for M in squares if REGION[corner(M)] == "petal")
assert all(REGION[corner(M)] == "crossing" for M in squares if deg[M] == "inf")
print("center -> always 4; petals -> always 3; all 16 complete-alternating squares sit on crossings")
