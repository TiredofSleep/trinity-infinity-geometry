"""
fourier_check.py — "go Fourier with it."

Three Fourier transforms of a 4x4 magic square on 0..15:
  (1) wave Fourier: 2D DFT over the grid (what a metasurface / wave sees)
  (2) binary Fourier on positions: Walsh-Hadamard over (row bits, column bits)
  (3) full binary Fourier: positions AND values. The square is a bijection from 4 position bits
      to 4 value bits -- a 4-bit S-box -- and its full Walsh table is the cryptographers'
      Linear Approximation Table (LAT).
Plus (4): Takemura's degree as the first nonzero moment of a signed spectrum.
"""
import json, itertools
import numpy as np
from collections import Counter, defaultdict

squares = [np.array(s["square"]) for s in json.load(open("squares_4x4.json"))]
H4 = np.array([[(-1) ** bin(r & i).count("1") for i in range(4)] for r in range(4)])
def corner(M):
    d = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a, c = -d[0] // 2, d[3]
    b = d[2] + 2 * d[3]
    return "".join("1" if x else "0" for x in (c, b, a))
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}

# (1) wave Fourier
ax = 0.0
for A in squares:
    F = np.fft.fft2(A - A.mean())
    ax = max(ax, np.abs(F[0, :]).max(), np.abs(F[:, 0]).max())
print(f"(1) 2D DFT: every square is silent on both frequency axes (max |F| there = {ax:.1e})")

# (2) Walsh on positions: W = H A H^T. DC = 4s; axes = 0; the 3x3 block M carries everything.
for A in squares:
    W = H4 @ A @ H4.T
    M = W[1:, 1:]
    assert W[0, 0] == 120 and not W[0, 1:].any() and not W[1:, 0].any()
    assert M[2, 2] == 0 and M[0, 0] == -M[1, 1]                         # the two diagonal sums
    assert round(np.linalg.det(A)) * 64 == round(30 * np.linalg.det(M))  # det A = s det M / 64
    for k in range(4):                                                   # carries = traces of bit-plane blocks
        Mk = (H4 @ (1 - 2 * ((A >> k) & 1)) @ H4.T)[1:, 1:]
        dk = sum((A[i][i] >> k) & 1 for i in range(4)) - 2
        assert Mk[0, 0] + Mk[1, 1] + Mk[2, 2] == -8 * dk
print("(2) Walsh: DC = 4s, axes = 0, M33 = 0, M11 = -M22, det A = s*det(M)/64, "
      "each bit plane's carry = -trace/8 : all hold on 880")

# (3) full binary Fourier: LAT of the square as a 4-bit S-box
def lat(A):
    S = [int(A[x >> 2][x & 3]) for x in range(16)]          # position bits (i1 i0 j1 j0)
    L = np.zeros((16, 16), int)
    for u in range(16):
        for v in range(16):
            L[u, v] = sum((-1) ** (bin(u & x).count("1") ^ bin(v & S[x]).count("1")) for x in range(16))
    return L, S
def ddt_max(S):
    return max(sum(1 for x in range(16) if S[x] ^ S[x ^ a] == b) for a in range(1, 16) for b in range(16))
lin = Counter(); du = Counter(); affine_by = defaultdict(Counter); nl_by = defaultdict(Counter)
for A in squares:
    L, S = lat(A)
    m = int(np.abs(L[1:, 1:]).max())          # linearity: biggest correlation with a linear rule
    lin[m] += 1
    du[ddt_max(S)] += 1
    nl_by[REGION[corner(A)]][m] += 1
print("(3) magic squares as 4-bit S-boxes (position bits -> value bits):")
print("    linearity max|LAT| :", dict(sorted(lin.items())), " (16 = affine map, 8 = cryptographically optimal)")
print("    differential max   :", dict(sorted(du.items())), " (16 = affine, 4 = optimal)")
print("    linearity by trefoil region:", {k: dict(sorted(v.items())) for k, v in nl_by.items()})

# (4) signed spectrum of permutation sums
perms = list(itertools.permutations(range(4)))
sg = [(-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in perms]
def signed_spectrum(A):
    c = defaultdict(int)
    for p, s in zip(perms, sg):
        c[sum(int(A[i][p[i]]) for i in range(4))] += s
    return {v: x for v, x in sorted(c.items()) if x}
print("(4) Takemura's degree = first nonzero moment of the signed spectrum c_v; G(t) = sum c_v e^{tv}.")
for want in ("petal", "center", "crossing"):
    for A in squares:
        if REGION[corner(A)] == want:
            print(f"    {want:8s} example: c_v = {signed_spectrum(A)}")
            break

# (5) the fold: every square has a mirror that XORs every value by one fixed mask
print("(5) XOR symmetries  A(x xor a) = A(x) xor b  (a = position shift in row/column bits):")
def S_of(A):
    return [int(A[x >> 2][x & 3]) for x in range(16)]
def translations(S):
    return [(a, S[0] ^ S[a]) for a in range(1, 16) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(16))]
MIRRORS = {0b0011: "left-right", 0b1100: "top-bottom"}     # j -> 3-j  and  i -> 3-i
n_affine = 0; carry_ok = True; half_zero = True
for A in squares:
    S = S_of(A)
    tr = translations(S)
    if len(tr) == 15:
        n_affine += 1
    mir = [(a, b) for a, b in tr if a in MIRRORS]
    assert mir, "a square with no mirror XOR symmetry"
    # proof check: a diagonal-swapping mirror must flip every carrying bit plane
    for a, b in mir:
        for k in range(4):
            dk = sum((A[i][i] >> k) & 1 for i in range(4)) - 2
            if dk != 0 and not (b >> k) & 1:
                carry_ok = False
    # Fourier consequence: LAT[u, v] = 0 whenever u.a != v.b
    L, _ = lat(A)
    for a, b in tr:
        for u in range(16):
            for v in range(16):
                if (bin(u & a).count("1") + bin(v & b).count("1")) % 2 and L[u, v] != 0:
                    half_zero = False
print(f"    every one of the 880 squares folds left-right or top-bottom with a fixed XOR mask: True")
print(f"    a diagonal-swapping fold always flips every carrying bit plane: {carry_ok}")
print(f"    each symmetry zeroes every LAT entry with u.a != v.b (at least half the spectrum): {half_zero}")
print(f"    affine squares (A(x) = Lx xor c over GF(2); spectrum = 15 single spikes): {n_affine}")
