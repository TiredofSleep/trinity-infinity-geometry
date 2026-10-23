"""
triad_atlas.py — internal organization of the triad (center / petals / crossings),
read through three lenses:
  BITS      carry corner (which of the 3 carries the diagonals use)
  FOLDS     XOR symmetries A(x xor a) = A(x) xor b ; the masks b
  SIGNS     determinant / Takemura degree / binary spectrum
Prints the 3 x 3 organization and checks the fold-mask rules.
"""
import json, itertools
import numpy as np
import sympy as sp
from collections import Counter, defaultdict

squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
perms = list(itertools.permutations(range(4)))
SG = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]
    b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}
def balanced(M):
    return {k for k in range(4) if sum((M[i][i] >> k) & 1 for i in range(4)) == 2}
def folds(M):
    S = [M[x >> 2][x & 3] for x in range(16)]
    return [(a, S[0] ^ S[a]) for a in range(1, 16) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16))]
def degree(M):
    c = defaultdict(int)
    for p, s in zip(perms, SG):
        c[sum(M[i][p[i]] for i in range(4))] += s
    if all(v == 0 for v in c.values()):
        return "inf"
    m = 0
    while sum(x * v ** m for v, x in c.items()) == 0:
        m += 1
    return m
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
groups = defaultdict(list)
for M in squares:
    groups[pattern(M)].append(M)
gsize = {M: len(v) for v in groups.values() for M in v}

rows = []
for M in squares:
    f = folds(M)
    masks = {b for a, b in f}
    rows.append(dict(M=M, region=REGION[corner(M)], corner=corner(M), affine=len(f) == 15,
                     comp=15 in masks, masks=masks, deg=degree(M), inv=sp.Matrix(M).det() != 0,
                     group=gsize[M], bal=balanced(M)))

# rule checks
assert all(r["comp"] == (not r["inv"]) for r in rows)                       # complement fold <=> singular
for r in rows:
    if r["inv"]:
        w3 = [b for b in r["masks"] if bin(b).count("1") == 3]
        assert w3                                                            # invertible => a weight-3 fold
        for b in w3:
            missing = ({0, 1, 2, 3} - {k for k in range(4) if (b >> k) & 1}).pop()
            assert missing in r["bal"]                                       # the unflipped plane is balanced
print("rules: complement fold <=> singular;  invertible => a fold flipping 3 bits, and the bit it")
print("       skips is always a balanced plane  (all 880)")

print("\nTHE TRIAD, three lenses")
for reg in ("center", "petal", "crossing"):
    R = [r for r in rows if r["region"] == reg]
    print(f"\n{reg.upper()}  ({len(R)} squares)")
    print("  BITS  :", dict(sorted(Counter(r["corner"] for r in R).items())))
    kinds = Counter(("affine (all 15 folds)" if r["affine"] else
                     "complement fold" if r["comp"] else "3-bit fold only") for r in R)
    print("  FOLDS :", dict(kinds))
    print("  SIGNS :", "degree", dict(sorted(Counter(str(r["deg"]) for r in R).items())),
          "| invertible", sum(r["inv"] for r in R))
    print("  Dudeney groups:", dict(sorted(Counter(r["group"] for r in R).items(), reverse=True)))
    sub = Counter((r["corner"], "affine" if r["affine"] else "comp" if r["comp"] else "3-bit", str(r["deg"]))
                  for r in R)
    print("  cells (corner, fold, degree):", dict(sorted(sub.items())))
