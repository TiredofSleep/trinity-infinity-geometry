"""
order8_bitbalanced_test.py — 8x8 magic squares whose rows and columns are bit-balanced
(the order-8 analog of what every 4x4 square has). Do folds, diagonal cancellation, and the carry
rules come back once that property is forced in?
"""
import numpy as np
from collections import Counter

sq = [np.array(list(map(int, l.split()))).reshape(8, 8) for l in open("squares8_bitbalanced.txt")]
LINES = [[(i, j) for j in range(8)] for i in range(8)] + [[(i, j) for i in range(8)] for j in range(8)] + \
        [[(i, i) for i in range(8)], [(i, 7 - i) for i in range(8)]]
assert all(sorted(A.flatten()) == list(range(64)) for A in sq)
assert all(sum(A[i][j] for i, j in L) == 252 for A in sq for L in LINES)
assert all(sum((A[i][j] >> k) & 1 for i, j in L) == 4 for A in sq for L in LINES[:16] for k in range(6))

def carries(vals):
    d = [sum((v >> k) & 1 for v in vals) - 4 for k in range(6)]
    a, prev = [], 0
    for k in range(5):
        ak = (prev - d[k]) // 2; a.append(ak); prev = ak
    return tuple(a)
fold = Counter(); mirror = Counter(); cancel = Counter(); shapes = Counter(); affine = 0; sing = 0
for A in sq:
    S = [int(A[x >> 3][x & 7]) for x in range(64)]
    tr = [(a, S[0] ^ S[a]) for a in range(1, 64) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(64))]
    fold[len(tr)] += 1
    mirror[any(a in (0b000111, 0b111000) for a, b in tr)] += 1
    affine += len(tr) == 63
    dD, dA = carries([A[i][i] for i in range(8)]), carries([A[i][7 - i] for i in range(8)])
    cancel[dA == tuple(-x for x in dD)] += 1
    nz = [x for x in dD if x]
    if nz:
        used = [k for k, x in enumerate(dD) if x]
        shapes[(all(x > 0 for x in nz) or all(x < 0 for x in nz), used == list(range(used[0], used[-1] + 1)),
                max(abs(x) for x in nz))] += 1
    else:
        shapes["no carry"] += 1
    sing += abs(np.linalg.det(A)) < 0.5
print(f"{len(sq)} bit-balanced 8x8 magic squares (annealed)")
print("  number of XOR symmetries per square:", dict(sorted(fold.items())))
print("  has a left-right or top-bottom fold:", dict(mirror))
print("  affine:", affine, "  singular:", sing)
print("  diagonals carry equal and opposite:", dict(cancel))
print("  main-diagonal carries (same sign?, contiguous?, biggest):", dict(shapes))
