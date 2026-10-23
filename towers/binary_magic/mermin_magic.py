"""
mermin_magic.py — a 3x3 square that is both a magic square (sum 30) and a Mermin-Peres square.

Search over all 28 qubit labelings found exactly one such square up to rotation/reflection:
    11 13  6
     5 10 15
    14  7  9
Write each number in base 4: two digits from {1,2,3}. Read digit 1 = Z, 2 = X, 3 = Y, the high digit
on qubit 1 and the low digit on qubit 2. Each number is then a two-qubit operator with no identity factor.
"""
import numpy as np
from functools import reduce

G = [[11, 13, 6], [5, 10, 15], [14, 7, 9]]
s = 30
L = [[(i, j) for j in range(3)] for i in range(3)] + [[(i, j) for i in range(3)] for j in range(3)]
D = [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
assert all(sum(G[i][j] for i, j in l) == s for l in L + D)
print("magic: every row, column and diagonal sums to 30")

hi = [[v // 4 for v in r] for r in G]; lo = [[v % 4 for v in r] for r in G]
latin = lambda M: all(sorted(r) == [1, 2, 3] for r in M) and all(sorted(c) == [1, 2, 3] for c in zip(*M))
assert latin(hi) and latin(lo) and len({(hi[i][j], lo[i][j]) for i in range(3) for j in range(3)}) == 9
print("base 4: high digits", hi, "and low digits", lo, "are orthogonal Latin squares on {1,2,3}")
for name, l in (("main diagonal", D[0]), ("anti-diagonal", D[1])):
    print(f"  {name}: high digits {[hi[i][j] for i, j in l]}, low digits {[lo[i][j] for i, j in l]}")

# Lo Shu for comparison: base 3, digits {0,1,2}
LS = [[3, 8, 1], [2, 4, 6], [7, 0, 5]]
print("Lo Shu (0..8) in base 3: high", [[v // 3 for v in r] for r in LS], "low", [[v % 3 for v in r] for r in LS])

# as quantum operators
X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
op = {1: Z, 2: X, 3: Y}; name = {1: "Z", 2: "X", 3: "Y"}
Q = [[np.kron(op[v // 4], op[v % 4]) for v in r] for r in G]
print("\nas two-qubit operators:")
for r in G:
    print("   ", "  ".join(name[v // 4] + name[v % 4] for v in r))
comm = lambda A, B: np.allclose(A @ B, B @ A)
signs = []
for l in L:
    ops = [Q[i][j] for i, j in l]
    assert all(comm(a, b) for a in ops for b in ops)
    prod = reduce(lambda a, b: a @ b, ops)
    sg = prod[0, 0].real; assert np.allclose(prod, sg * np.eye(4)); signs.append(int(round(sg)))
diag_ok = [all(comm(Q[a][b], Q[c][d]) for (a, b) in l for (c, d) in l) for l in D]
print("rows commute and multiply to", signs[:3], "; columns to", signs[3:])
print("product of all six signs:", int(np.prod(signs)), "-> no +-1 assignment can satisfy every line")
print("diagonals are measurement contexts?", diag_ok)
