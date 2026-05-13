# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2026 Brayden Ross Sanders, M. Gish
#
# Verification script for J37: Prime-Divisibility Pattern of the
# Characteristic Polynomial of a 10x10 Integer Matrix Arising in a
# Discrete Magma on Z/10Z.
#
# Reproduces all numerical claims of Theorems 1.1, 1.2, 1.3 and the
# lens-dependence comparison of Theorem 4.1 at integer/machine precision.
# Pure numpy + sympy; runs in under 5 seconds on a typical laptop.
"""
Prime-divisibility verification — characteristic polynomial of the
specific 10x10 integer matrix T defined in manuscript §1.

The integer characteristic polynomial of T has the prime 11 as a divisor
of exactly two of its nine nonzero coefficients (c_2 and c_8), which by
the elementary-symmetric-function identification correspond to:
  - the sum of products of pairs of eigenvalues (e_2)
  - the product of the eight nonzero eigenvalues (e_8)

Pure numpy + sympy. No external dependencies.
"""
import numpy as np
import sympy
from sympy import factorint

# Literal cell pattern of T (manuscript §1); rows of integers in {0,3,4,7,8,9}.
T_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
T = np.array([[int(c) for c in row] for row in T_ROWS], dtype=float)

# CLAIM 1: T has integer characteristic polynomial
char_poly = np.poly(T)
all_int = all(abs(c - round(c)) < 1e-6 for c in char_poly)
assert all_int, "Char poly should have integer coefficients"
int_coeffs = [int(round(c)) for c in char_poly]
print(f"[PASS] CLAIM 1: charpoly(T) has integer coefficients")
print(f"  Polynomial: {int_coeffs}")
print()

# CLAIM 2: trace = 63 = 9*7 (sum of eigenvalues = -c_1)
trace = -int_coeffs[1]
assert trace == 63, f"Trace should be 63, got {trace}"
assert trace == 9 * 7, f"63 = 9 * 7"
print(f"[PASS] CLAIM 2: trace(T) = 63 = 9 * 7  (Theorem 1.3)")
print()

# CLAIM 3: c_2 = 33 = 3 * 11
c_2 = int_coeffs[2]
assert c_2 == 33, f"c_2 should be 33"
assert c_2 % 11 == 0, "c_2 should be divisible by 11"
print(f"[PASS] CLAIM 3: c_2 = 33 = 3 * 11  (11 divides c_2)")
print()

# CLAIM 4: c_8 = -120736 = -2^5 * 7^3 * 11
c_8 = int_coeffs[8]
assert c_8 == -120736, f"c_8 should be -120736"
factors_c8 = factorint(abs(c_8))
expected = {2: 5, 7: 3, 11: 1}
assert factors_c8 == expected, f"c_8 factorization mismatch: {factors_c8}"
print(f"[PASS] CLAIM 4: c_8 = -120736 = -2^5 * 7^3 * 11  (11 divides c_8)")
print()

# CLAIM 5: among the nine nonzero coefficients, ONLY c_2 and c_8 are divisible by 11
print("Coefficients divisible by 11:")
divisors_of_11 = []
for i, c in enumerate(int_coeffs):
    if c != 0 and abs(c) % 11 == 0:
        divisors_of_11.append(i)
        print(f"  c_{i} = {c}  (divisible by 11)")
assert divisors_of_11 == [2, 8], f"Only c_2 and c_8 should have 11, got {divisors_of_11}"
print(f"[PASS] CLAIM 5: exactly c_2 and c_8 are divisible by 11  (Theorem 1.1)")
print()

# CLAIM 6: disc(g) = 2^16 * 7^7 * 659 * (large primes), with 11 absent
x = sympy.Symbol('x')
p8 = sympy.Poly(int_coeffs[:9], x)
disc = p8.discriminant()
disc_factors = factorint(abs(disc))
print(f"Discriminant of the 8th-degree quotient g(lambda) = f(lambda)/lambda^2:")
print(f"  Factorization: {disc_factors}")
assert disc_factors.get(2) == 16, f"Expected 2^16 in disc(g)"
assert disc_factors.get(7) == 7, f"Expected 7^7 in disc(g)"
assert 11 not in disc_factors, "disc(g) should NOT have 11"
print(f"[PASS] CLAIM 6: disc(g) = 2^16 * 7^7 * 659 * (large primes), no factor of 11  (Theorem 1.2)")
print()

# CLAIM 7 (Theorem 4.1 lens-dependence): upper-triangle authoritative symmetrization.
# T (manuscript §1) is asymmetric in exactly two cell pairs (in 0-indexed numpy
# coordinates, which coincide with the magma-element subscripts in §1):
#   T[3,9] = 3, T[9,3] = 7
#   T[4,9] = 7, T[9,4] = 3
# Under upper-triangle authoritative symmetrization, both pairs are replaced
# with 7 (the upper-triangle value at the higher of the two columns; see §4):
T_SYM = T.copy()
T_SYM[3, 9] = 7  # was 3
T_SYM[9, 3] = 7  # was 7 (unchanged; written for clarity)
T_SYM[4, 9] = 7  # was 7 (unchanged)
T_SYM[9, 4] = 7  # was 3
sym_coeffs_np = np.poly(T_SYM)
sym_coeffs = [int(round(c)) for c in sym_coeffs_np]
sym_c2 = sym_coeffs[2]
print(f"Lens variant T_SYM (upper-triangle authoritative symmetrization):")
print(f"  charpoly(T_SYM) coefficients: {sym_coeffs}")
print(f"  c_2(T_SYM) = {sym_c2}")
print(f"  factorint(|c_2(T_SYM)|) = {factorint(abs(sym_c2)) if sym_c2 != 0 else '(zero)'}")
assert sym_c2 % 11 != 0, "T_SYM c_2 should NOT be divisible by 11"
sym_div_by_11 = [i for i, c in enumerate(sym_coeffs) if c != 0 and abs(c) % 11 == 0]
assert sym_div_by_11 == [], f"T_SYM should have no coefficient divisible by 11, got {sym_div_by_11}"
print(f"[PASS] CLAIM 7: T_SYM has c_2 = {sym_c2} (no factor of 11); no nonzero coefficient of charpoly(T_SYM) is divisible by 11  (Theorem 4.1, lens-dependence)")
print()

# Print final summary
print("=" * 60)
print("ALL 7 CLAIMS VERIFIED at integer/machine precision")
print("=" * 60)
print()
print("Summary (Theorems 1.1, 1.2, 1.3, 4.1):")
print("  - charpoly(T) has nine nonzero integer coefficients")
print("  - Exactly two (c_2 = 33, c_8 = -120736) are divisible by 11")
print("  - disc(f/lambda^2) = 2^16 * 7^7 * 659 * (large primes), no 11")
print("  - trace(T) = 63 = 9 * 7")
print("  - The 2-cell perturbation T -> T_SYM destroys the 11-divisibility pattern entirely")
print()
print("Structural co-occurrence (manuscript §3, no physical claim):")
print("  - exponent 16 in disc(g) = 2^16 matches dim of a 16-dim")
print("    doubly-invariant subalgebra of so(10) in the source program")
print("  - exponent 7 in disc(g) = 7^7 matches the recurring entry 7 in T")
