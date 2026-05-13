# SPDX-License-Identifier: CC-BY-4.0
# Copyright (c) 2026 Brayden Ross Sanders / 7Site LLC
#
# verify_J52.py — Verification script for J52 (TSML Lens Family, Math Intelligencer).
#
# Verifies the two computational claims displayed in the manuscript body:
#   (A) Exercise 7.1 — non-associative triple counts in the three TSML lenses.
#       TSML_RAW: 126   TSML_SYM: 128   TSML_LOWERTRI: 122
#   (B) Exercise 7.2 — wobble localization at prime 11 in the characteristic
#       polynomial of TSML_RAW (descending-power convention).
#       c_2(RAW) = 33 = 3 * 11   c_2(SYM) = 17   (the 11 disappears under SYM)
#       c_8(RAW) divisible by 11; c_8(SYM) not divisible by 11.
#
# All checks are EXACT (integer-only or sympy symbolic).

import numpy as np
import sympy as sp


# -------- §1.1 / §1.2: the displayed CL_TSML matrices --------
# Each string is one row of the 10x10 RAW matrix (per the §1 display).
CL_TSML_RAW_ROWS = (
    "0000000700",
    "0737777777",
    "0377477779",
    "0777777773",
    "0747777787",
    "0777777777",
    "0777777777",
    "7777777777",
    "0777877777",
    "0797377777",
)
RAW = np.array([[int(c) for c in r] for r in CL_TSML_RAW_ROWS], dtype=int)

# Upper-triangular-authoritative symmetrization (manuscript §1.1).
SYM = RAW.copy()
for i in range(10):
    for j in range(i + 1, 10):
        SYM[j, i] = RAW[i, j]

# Lower-triangular-authoritative symmetrization.
LOW = RAW.copy()
for i in range(10):
    for j in range(i + 1, 10):
        LOW[i, j] = RAW[j, i]


def n_nonassoc(M):
    """Count (x,y,z) with M(M(x,y),z) != M(x,M(y,z))."""
    n = 0
    for x in range(10):
        for y in range(10):
            for z in range(10):
                if M[M[x, y], z] != M[x, M[y, z]]:
                    n += 1
    return n


def harmony_count(M):
    """Count entries equal to 7 in the table."""
    return int(np.sum(M == 7))


def four_core_closed(M):
    """Check that {0,7,8,9} x {0,7,8,9} is closed under M."""
    core = {0, 7, 8, 9}
    for a in core:
        for b in core:
            if int(M[a, b]) not in core:
                return False
    return True


def char_poly_coeffs(M):
    """Return descending-power coefficients (c_1, c_2, ..., c_10) of det(lambda I - M)
       as exact sympy integers, using the manuscript indexing
           det(lambda*I - M) = lambda^10 + c_1*lambda^9 + ... + c_10.
    """
    Msym = sp.Matrix(M.tolist())
    lam = sp.symbols("lam")
    poly = sp.Poly(Msym.charpoly(lam).as_expr(), lam)
    # all_coeffs returns highest degree first: [1, c_1, c_2, ..., c_10].
    coeffs = poly.all_coeffs()
    assert coeffs[0] == 1, "characteristic polynomial should be monic"
    return [sp.Integer(c) for c in coeffs[1:]]


# -------- Exercise 7.1 — non-associative triple counts --------
counts = {
    "RAW": n_nonassoc(RAW),
    "SYM": n_nonassoc(SYM),
    "LOW": n_nonassoc(LOW),
}
assert counts["RAW"] == 126, f"RAW: expected 126, got {counts['RAW']}"
assert counts["SYM"] == 128, f"SYM: expected 128, got {counts['SYM']}"
assert counts["LOW"] == 122, f"LOW: expected 122, got {counts['LOW']}"

# -------- §1.1 structural facts: HARMONY counts and 4-core closure --------
assert harmony_count(RAW) == 73, f"RAW HARMONY count expected 73, got {harmony_count(RAW)}"
assert harmony_count(SYM) == 73, f"SYM HARMONY count expected 73, got {harmony_count(SYM)}"
assert four_core_closed(RAW), "4-core {0,7,8,9} must be closed under RAW"
assert four_core_closed(SYM), "4-core {0,7,8,9} must be closed under SYM"

# -------- Exercise 7.2 — wobble localization (prime 11) --------
raw_coeffs = char_poly_coeffs(RAW)
sym_coeffs = char_poly_coeffs(SYM)

c2_raw = int(raw_coeffs[1])  # coefficient of lambda^8
c2_sym = int(sym_coeffs[1])
c8_raw = int(raw_coeffs[7])  # coefficient of lambda^2
c8_sym = int(sym_coeffs[7])

assert c2_raw == 33, f"c_2(RAW) expected 33, got {c2_raw}"
assert c2_sym == 17, f"c_2(SYM) expected 17, got {c2_sym}"
assert c2_raw % 11 == 0 and c2_raw // 11 == 3, "c_2(RAW) must factor as 3 * 11"
assert c2_sym % 11 != 0, "c_2(SYM) must NOT be divisible by 11"
assert c8_raw % 11 == 0, "c_8(RAW) must be divisible by 11"
assert c8_sym % 11 != 0, "c_8(SYM) must NOT be divisible by 11 (wobble erased)"

# Final report.
print("=" * 68)
print("J52 verification — TSML Lens Family (Sanders + Gish, Math Intelligencer)")
print("=" * 68)
print(f"Exercise 7.1 non-assoc triples:  RAW={counts['RAW']}  "
      f"SYM={counts['SYM']}  LOW={counts['LOW']}     [PASS]")
print(f"HARMONY counts (both 73):        RAW=73  SYM=73                     [PASS]")
print(f"4-core {{0,7,8,9}} closure:       RAW closed, SYM closed             [PASS]")
print(f"Exercise 7.2 wobble at prime 11: c_2(RAW)={c2_raw}=3*11   "
      f"c_2(SYM)={c2_sym}    [PASS]")
print(f"                                 c_8(RAW)%11=0   c_8(SYM)%11={c8_sym % 11}     [PASS]")
print("=" * 68)
print("All J52 verification checks PASS at exact arithmetic.")
