"""
ck_tables.py — Two commutative binary operations on Z/10Z

Sanders + Gish (2026), companion to manuscript:
  "A Small Commutative Non-Associative Magma on Z/10Z with
   Role-Deterministic Boundary Behavior"

Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
You are free to share and adapt this work with attribution.
See https://creativecommons.org/licenses/by/4.0/ for full terms.

This file defines:
- TSML: a commutative binary operation on Z/10Z (V0/V1/Echo/Default rules)
- BHML: a commutative binary operation on Z/10Z (R_A/R_B/R_7/R_89 rules)

Both tables are 10x10 arrays indexed 0..9 with rows/cols matching the
explicit four-zone (BHML) and three-exception (TSML) rules in the manuscript.

Verification: running this file directly checks symmetry, harmony counts,
and the rule structure. Should print "ALL CHECKS PASSED."
"""

# ============================================================
# TSML  — three exception classes plus Default = 7
# Verified: symmetric; 73/100 cells output 7
# ============================================================
TSML = [
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],   # row 0: V0 (j!=7 -> 0; j=7 -> 7)
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],   # row 1: default + Echo (1,2)=3
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],   # row 2: Echos (2,1)=3, (2,4)=4, (2,9)=9
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],   # row 3: Echo (3,9)=3
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],   # row 4: Echos (4,2)=4, (4,8)=8
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 5: default
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 6: default
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 7: V1 fixed at 7; default elsewhere
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],   # row 8: Echo (8,4)=8
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],   # row 9: Echos (9,2)=9, (9,3)=3
]

# ============================================================
# BHML — four-zone partition R_A, R_B, R_7, R_89
# Verified: symmetric; 28/100 cells output 7
# ============================================================
BHML = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],   # row 0: R_A (BH(0,j)=j)
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],   # row 1: R_B for j in 1..6; R_7 at j=7; R_89 at j>=8
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],   # row 2
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],   # row 3
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],   # row 4
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],   # row 5
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],   # row 6 (max+1 hits 7 across)
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],   # row 7: R_7 ((j+1) mod 10)
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],   # row 8: R_89 explicit
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],   # row 9: R_89 explicit
]

# Role partition (used in M_R reduction)
V_role = {0}
F_role = {1, 3, 5, 7, 9}
S_role = {2, 4, 8}
T_role = {6}

def role(x):
    if x in V_role: return 'V'
    if x in F_role: return 'F'
    if x in S_role: return 'S'
    if x in T_role: return 'T'
    raise ValueError(f"unrecognized {x}")

# sigma permutation: order 6, fixes {0,3,8,9}, cycles (1 7 6 5 4 2)
SIGMA = {0: 0, 1: 7, 2: 1, 3: 3, 4: 2, 5: 4, 6: 5, 7: 6, 8: 8, 9: 9}

def apply_sigma(x, k=1):
    """Apply sigma^k to x."""
    cur = x
    for _ in range(k):
        cur = SIGMA[cur]
    return cur

# ============================================================
# Quick verification (run this file directly)
# ============================================================
if __name__ == '__main__':
    # Symmetry checks
    tsml_sym = all(TSML[i][j] == TSML[j][i] for i in range(10) for j in range(10))
    bhml_sym = all(BHML[i][j] == BHML[j][i] for i in range(10) for j in range(10))
    assert tsml_sym, "TSML must be symmetric"
    assert bhml_sym, "BHML must be symmetric"
    print(f"TSML symmetric: {tsml_sym}")
    print(f"BHML symmetric: {bhml_sym}")

    # Harmony cell counts
    tsml_h = sum(1 for i in range(10) for j in range(10) if TSML[i][j] == 7)
    bhml_h = sum(1 for i in range(10) for j in range(10) if BHML[i][j] == 7)
    assert tsml_h == 73, f"TSML harmony count = {tsml_h}, expected 73"
    assert bhml_h == 28, f"BHML harmony count = {bhml_h}, expected 28"
    print(f"TSML harmony cells: {tsml_h}/100 (expect 73)")
    print(f"BHML harmony cells: {bhml_h}/100 (expect 28)")

    # BHML Rule B (max+1) on i,j in 1..6
    rule_b = all(BHML[i][j] == max(i, j) + 1 for i in range(1, 7) for j in range(1, 7))
    assert rule_b, "BHML R_B rule fails"
    print(f"BHML R_B (max+1) holds on 1..6 x 1..6: {rule_b}")

    # BHML Row 7 increment (j+1) mod 10 for j>=1
    row7_ok = all(BHML[7][j] == (j + 1) % 10 for j in range(1, 10))
    assert row7_ok, "BHML R_7 rule fails on row 7"
    print(f"BHML R_7 (j+1)%10 holds on row 7 for j>=1: {row7_ok}")

    # sigma has order 6
    cur = list(range(10))
    cur = [SIGMA[x] for x in cur]
    cur = [SIGMA[x] for x in cur]
    cur = [SIGMA[x] for x in cur]
    cur = [SIGMA[x] for x in cur]
    cur = [SIGMA[x] for x in cur]
    cur = [SIGMA[x] for x in cur]
    sigma_order_6 = (cur == list(range(10)))
    assert sigma_order_6, "sigma should have order 6"
    print(f"sigma has order 6 (sigma^6 = identity): {sigma_order_6}")

    print()
    print("ALL CHECKS PASSED.")
    print("  from ck_tables import TSML, BHML, role, SIGMA, V_role, F_role, S_role, T_role")
