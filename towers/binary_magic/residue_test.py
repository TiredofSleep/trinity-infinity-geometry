"""
residue_test.py — "randomness is abundant, but only balanced-sign structures leave measurable residue."

Sandbox test with the numbers 0..15 in a 4x4 grid. Two kinds of residue:
  (a) line residue: XOR each line (= which Dirac element the line multiplies to, up to sign)
  (b) alternating-sum residue: lowest degree m where sum_p sgn(p) f(p)^m != 0 (Takemura's degree)
Compare 100,000 random arrangements with the 880 magic squares.
"""
import json, itertools, math, random
from functools import reduce
from collections import Counter, defaultdict
import numpy as np

random.seed(1)
LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
perms = list(itertools.permutations(range(4)))
SG = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
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
def entropy(cnt):
    n = sum(cnt.values())
    return -sum(v / n * math.log2(v / n) for v in cnt.values() if v)

def profile(squares):
    rc, dg, deg = Counter(), Counter(), Counter()
    for M in squares:
        for k, L in enumerate(LINES):
            x = reduce(lambda a, b: a ^ b, (M[i][j] for i, j in L))
            (rc if k < 8 else dg)[x] += 1
        deg[degree(M)] += 1
    return rc, dg, deg

magic = [s["square"] for s in json.load(open("squares_4x4.json"))]
rand = []
for _ in range(100_000):
    v = list(range(16)); random.shuffle(v)
    rand.append([v[4 * i:4 * i + 4] for i in range(4)])

for name, sq in (("random", rand), ("magic", magic)):
    rc, dg, deg = profile(sq)
    print(f"{name:7s} rows/cols residue: {len(rc):2d} distinct values, entropy {entropy(rc):.2f} bits"
          f" | diagonals: {len(dg):2d} values, entropy {entropy(dg):.2f} bits"
          f" | degree: {dict(sorted(Counter({str(k): v for k, v in deg.items()}).items()))}")
