"""Builds the compact data table embedded in the atlas page (atlas.html)."""
import json, itertools
from collections import defaultdict
import sympy as sp

squares = [tuple(map(tuple, s["square"])) for s in json.load(open("squares_4x4.json"))]
perms = list(itertools.permutations(range(4)))
SG = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
def degree(M):
    c = defaultdict(int)
    for p, s in zip(perms, SG):
        c[sum(M[i][p[i]] for i in range(4))] += s
    if all(v == 0 for v in c.values()):
        return 0                                    # 0 encodes infinity
    m = 0
    while sum(x * v ** m for v, x in c.items()) == 0:
        m += 1
    return m
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]
    b = d[2] + 2 * d[3]
    sgn = next((x for x in (a, b, c) if x), 0)
    return ("1" if c else "0") + ("1" if b else "0") + ("1" if a else "0"), sgn
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
order = sorted(groups, key=lambda k: (-len(groups[k]), k))
gid = {}
for idx, k in enumerate(order):
    for M in groups[k]:
        gid[M] = idx
gsizes = [len(groups[k]) for k in order]
rows = []
for M in squares:
    S = [M[x >> 2][x & 3] for x in range(16)]
    tr = [(a, S[0] ^ S[a]) for a in range(1, 16) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16))]
    lr = next((b for a, b in tr if a == 0b0011), -1)
    tb = next((b for a, b in tr if a == 0b1100), -1)
    cn, sgn = corner(M)
    rows.append([[v for r in M for v in r], cn, sgn, degree(M), int(sp.Matrix(M).det() != 0),
                 gid[M], lr, tb, int(len(tr) == 15), int(any(b == 15 for a, b in tr))])
json.dump({"groups": gsizes, "rows": rows}, open("artifact/atlas_data.json", "w"), separators=(",", ":"))
print(len(rows), "rows; group sizes", gsizes)
