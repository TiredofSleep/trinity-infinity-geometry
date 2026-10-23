"""
dirac_tower.py — "the Dirac matrices, same rules, many more."

1. Build n mutually anticommuting matrices (gamma_a gamma_b + gamma_b gamma_a = 2 delta_ab)
   for n = 1..12 by stacking Pauli matrices (Brauer-Weyl / Jordan-Wigner). Size 2^floor(n/2).
2. The full algebra has 2^n elements, one per n-bit string. Product rule:
   e_A e_B = sign(A,B) * e_(A XOR B)   -- binary XOR, plus a sign from counting swaps.
3. n = 4 is the Dirac algebra: 16 elements = the numbers 0..15. Put them in a 4x4 magic square
   and multiply along each line.
4. The 3-fold version (Sylvester's clock and shift): same idea with a cube root of unity.
"""
import json, itertools
import numpy as np
from functools import reduce
from collections import Counter

I2 = np.eye(2); X = np.array([[0, 1], [1, 0]]); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1])
def kron(*ms):
    return reduce(np.kron, ms, np.eye(1))

def gammas(n):
    k = (n + 1) // 2 if n % 2 else n // 2
    k = max(k, 1)
    g = []
    for j in range(n // 2):
        g.append(kron(*([Z] * j + [X] + [I2] * (k - j - 1))))
        g.append(kron(*([Z] * j + [Y] + [I2] * (k - j - 1))))
    if n % 2:
        g.append(kron(*([Z] * k)) if n > 1 else Z)
    return g[:n] if n > 1 else [Z]

print("1. n anticommuting matrices, each squaring to 1:")
for n in range(1, 13):
    g = gammas(n)
    ok = all(np.allclose(g[a] @ g[b] + g[b] @ g[a], 2 * (a == b) * np.eye(len(g[0])))
             for a in range(n) for b in range(n))
    print(f"   n = {n:2d}: {len(g[0]):3d} x {len(g[0]):<3d} matrices, rule holds: {ok}, algebra size 2^{n} = {2**n}")
    assert ok

# 2. blades and the XOR rule (Euclidean signature, n = 4)
n = 4
g = gammas(n)
def blade(A):                     # A = bit string as int; product of gammas whose bits are set, in order
    M = np.eye(len(g[0]), dtype=complex)
    for k in range(n):
        if (A >> k) & 1:
            M = M @ g[k]
    return M
def sign(A, B):                   # swaps needed to sort the concatenated generator list
    s = 0
    for i in range(n):
        if (A >> i) & 1:
            s += bin(B & ((1 << i) - 1)).count("1")
    return (-1) ** s
E = [blade(A) for A in range(16)]
assert all(np.allclose(E[A] @ E[B], sign(A, B) * E[A ^ B]) for A in range(16) for B in range(16))
print("\n2. all 256 products obey e_A e_B = sign * e_(A xor B)  [n = 4, the Dirac algebra's 16 elements]")

# 3. magic squares as Dirac products
squares = [s["square"] for s in json.load(open("squares_4x4.json"))]
LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
line_kind = Counter(); diag_blade = Counter(); row_signs = Counter()
for M in squares:
    rs = []
    for idx, L in enumerate(LINES):
        P = reduce(lambda a, b: a @ b, (E[M[i][j]] for i, j in L))
        x = reduce(lambda a, b: a ^ b, (M[i][j] for i, j in L))
        s = None
        for sg in (1, -1):
            if np.allclose(P, sg * E[x]):
                s = sg
        assert s is not None
        if idx < 8:
            assert x == 0                    # rows and columns: product is +-1 (a pure number)
            rs.append(s)
        else:
            diag_blade[x] += 1
    row_signs[(rs[:4].count(-1), rs[4:].count(-1))] += 1
print("3. every row and column of every square multiplies to +1 or -1 (all 880 x 8 lines)")
print("   diagonal products land on blade e_x with x in", dict(sorted(Counter({k: v // 1 for k, v in diag_blade.items()}).items())))
print("   (# of -1 rows, # of -1 columns) per square:", dict(sorted(row_signs.items())))

# 4. the 3-fold version: clock C and shift S, C^3 = S^3 = 1, C S = w S C
w = np.exp(2j * np.pi / 3)
C = np.diag([1, w, w * w]); S = np.roll(np.eye(3), 1, axis=0)
assert np.allclose(np.linalg.matrix_power(C, 3), np.eye(3)) and np.allclose(np.linalg.matrix_power(S, 3), np.eye(3))
assert np.allclose(C @ S, w * S @ C)
print("\n4. 3-fold version: C^3 = S^3 = 1 and C S = w S C (w = cube root of 1): holds."
      "\n   9 elements C^a S^b; product rule: add exponents mod 3, times a power of w.")

# 5. the 3-fold version on the 3x3 magic square (Lo Shu, numbers 0..8 = two trits each)
lo = [[3, 8, 1], [2, 4, 6], [7, 0, 5]]                 # Lo Shu minus 1
assert all(sum(r) == 12 for r in lo) and all(sum(c) == 12 for c in zip(*lo))
assert sum(lo[i][i] for i in range(3)) == 12 and sum(lo[i][2 - i] for i in range(3)) == 12
L3 = [[(i, j) for j in range(3)] for i in range(3)] + [[(i, j) for i in range(3)] for j in range(3)] + \
     [[(i, i) for i in range(3)], [(i, 2 - i) for i in range(3)]]
print("\n5. Lo Shu (0..8) in base 3, each line, each trit: digits are")
for L in L3:
    vals = [lo[i][j] for i, j in L]
    hi = [v // 3 for v in vals]; lo_t = [v % 3 for v in vals]
    kind = lambda t: "all different" if len(set(t)) == 3 else "all the same" if len(set(t)) == 1 else "MIXED"
    print(f"   {vals}: high trit {kind(hi)}, low trit {kind(lo_t)}")
    assert "MIXED" not in (kind(hi), kind(lo_t))
# as clock-and-shift products: v = 3a + b  ->  C^a S^b ; every line multiplies to a power of w times 1
E3 = {v: np.linalg.matrix_power(C, v // 3) @ np.linalg.matrix_power(S, v % 3) for v in range(9)}
for L in L3:
    P = reduce(lambda x, y: x @ y, (E3[lo[i][j]] for i, j in L))
    assert any(np.allclose(P, w ** k * np.eye(3)) for k in range(3))
print("   every line of the Lo Shu, read as clock-and-shift matrices, multiplies to a pure number (power of w)")
