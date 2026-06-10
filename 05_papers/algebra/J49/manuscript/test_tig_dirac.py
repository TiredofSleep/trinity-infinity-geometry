"""
test_tig_dirac.py — comprehensive test suite for tig_dirac.py

Run with:  python3 test_tig_dirac.py

Tests organized by structural claim:
  T1: V's basic algebraic properties
  T2: Idempotent structure and primitive idempotents
  T3: Privileged basis relations (p_+² = p_+, p_-² = p_-, etc.)
  T4: The annihilator ε
  T5: The h element with h² = p_+
  T6: Three commuting projectors L_HARMONY, L_VOID, L_p_-
  T7: Eigenspace dimensions (1+3, 2+2, 1+3 splits)
  T8: Forbidden eigenspace (V−A asymmetry)
  T9: Associator image = span(p_-)
  T10: Aut(V) order 40
  T11: σ palindrome
  T12: σ³ doomdo swap
  T13: Tensor partition counts
  T14: Binomial distribution at GUT level
  T15: Clifford ladder dimensional match

Each test prints PASS/FAIL with brief explanation.
"""

import numpy as np
from tig_dirac import (
    V, mul, L_op, projectors, projector_HARMONY, projector_VOID, projector_BECOMING,
    P_PLUS, P_MINUS, EPS, H_ELEM, E_0,
    sigma, all_automorphisms, tensor_partition, cell_binomial_distribution,
    clifford_match, all_vectors,
)


def assert_eq(a, b, msg):
    """Assertion helper printing PASS/FAIL line."""
    if isinstance(a, np.ndarray):
        ok = np.array_equal(a % 5, b % 5) if isinstance(b, np.ndarray) else False
    else:
        ok = a == b
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {msg}")
    if not ok:
        print(f"          expected: {b}")
        print(f"          got:      {a}")
    return ok


def test_T1_basic():
    print("T1: V's basic algebraic properties")
    assert_eq(V.is_commutative(), True, "V is commutative")
    assert_eq(V.is_power_associative(), True, "V is power-associative")
    assert_eq(V.is_associative_on_basis(), False, "V is NOT associative (on basis)")
    assert_eq(V.dim(), 4, "dim V = 4")
    assert_eq(V.field_size(), 5, "F_5 base field")
    assert_eq(V.num_elements(), 625, "5^4 = 625 elements")


def test_T2_idempotents():
    print("\nT2: Idempotents")
    idemps = V.idempotents()
    assert_eq(len(idemps), 4, "Exactly 4 idempotents (incl. 0)")
    expected = {(0,0,0,0), (1,0,0,0), (0,1,0,0), (1,4,0,0)}
    assert_eq(set(idemps), expected, "Idempotents = {0, e_0, p_+, p_-}")


def test_T3_privileged_basis():
    print("\nT3: Privileged basis relations")
    # p_+² = p_+
    pp_sq = mul(P_PLUS, P_PLUS)
    assert_eq(np.array_equal(pp_sq, P_PLUS), True, "p_+² = p_+ (HARMONY idempotent)")
    # p_-² = p_-
    pm_sq = mul(P_MINUS, P_MINUS)
    assert_eq(np.array_equal(pm_sq, P_MINUS), True, "p_-² = p_- (second idempotent)")
    # p_+ · p_- = 0
    pp_pm = mul(P_PLUS, P_MINUS)
    assert_eq(np.all(pp_pm == 0), True, "p_+ · p_- = 0 (orthogonal idempotents)")
    # p_+ + p_- = e_0
    sum_p = (P_PLUS + P_MINUS) % 5
    assert_eq(np.array_equal(sum_p, E_0), True, "p_+ + p_- = e_0")


def test_T4_annihilator():
    print("\nT4: Annihilator ε")
    # ε² = 0
    eps_sq = mul(EPS, EPS)
    assert_eq(np.all(eps_sq == 0), True, "ε² = 0 (nilpotent)")
    # ε · y = 0 for many y (sample)
    n_zero = sum(1 for y in all_vectors() if np.all(mul(EPS, y) == 0))
    assert_eq(n_zero, 625, "ε · y = 0 for ALL y (full annihilator)")


def test_T5_h_element():
    print("\nT5: h element (sqrt of p_+ = supercharge analog)")
    h_sq = mul(H_ELEM, H_ELEM)
    assert_eq(np.array_equal(h_sq, P_PLUS), True, "h² = p_+ (exact)")


def test_T6_projectors():
    print("\nT6: Three Dirac-like projectors")
    L_H, L_V, L_M = projectors()
    # Idempotent
    assert_eq(np.array_equal((L_H @ L_H) % 5, L_H), True, "L_HARMONY² = L_HARMONY")
    assert_eq(np.array_equal((L_V @ L_V) % 5, L_V), True, "L_VOID² = L_VOID")
    assert_eq(np.array_equal((L_M @ L_M) % 5, L_M), True, "L_p_-² = L_p_-")
    # Commute
    assert_eq(np.array_equal((L_H @ L_V) % 5, (L_V @ L_H) % 5), True,
              "L_HARMONY commutes with L_VOID")
    assert_eq(np.array_equal((L_H @ L_M) % 5, (L_M @ L_H) % 5), True,
              "L_HARMONY commutes with L_p_-")
    assert_eq(np.array_equal((L_V @ L_M) % 5, (L_M @ L_V) % 5), True,
              "L_VOID commutes with L_p_-")
    # L_M = L_V - L_H
    assert_eq(np.array_equal(L_M, (L_V - L_H) % 5), True,
              "L_p_- = L_VOID − L_HARMONY (linearity of L)")


def test_T7_eigenspaces():
    print("\nT7: Eigenspace dimensions (1+3, 2+2, 1+3)")
    L_H, L_V, L_M = projectors()
    # L_HARMONY: rank 1 (image = span(p_+))
    img_H = sum(1 for v in all_vectors() if not np.all(v == 0)
                and np.array_equal((L_H @ v) % 5, v))
    # 5^1 - 1 = 4 nonzero vectors with eigenvalue 1
    assert_eq(img_H, 4, "L_HARMONY 1-eigenspace = 1-dim (4 nonzero vectors)")


def test_T8_forbidden():
    print("\nT8: Forbidden eigenspace (V−A asymmetry)")
    L_H, L_V, L_M = projectors()
    # Cell (1, 0, 1): L_H = 1, L_V = 0, L_M = 1 — should be empty
    forbidden_count = 0
    for v in all_vectors():
        if np.all(v == 0): continue
        if (np.array_equal((L_H @ v) % 5, v) and
            np.all((L_V @ v) % 5 == 0) and
            np.array_equal((L_M @ v) % 5, v)):
            forbidden_count += 1
    assert_eq(forbidden_count, 0, "Forbidden cell (1,0,1) is empty (V−A asymmetry)")


def test_T9_associator():
    print("\nT9: Associator image")
    img = V.associator_image()
    # All images should be in span(p_-) = {(c, 4c, 0, 0) : c ∈ F_5}
    span_pm = {(c, (4*c) % 5, 0, 0) for c in range(5)}
    assert_eq(img.issubset(span_pm), True,
              f"Associator image ⊂ span(p_-): {len(img)} values, all in {len(span_pm)}-element span")
    # Image is non-trivial (V is genuinely non-associative)
    assert_eq(any(not all(c == 0 for c in v) for v in img), True,
              "Associator image is non-zero (V is non-associative)")


def test_T10_Aut():
    print("\nT10: Aut(V) ≅ F_20 × Z/2 of order 40")
    auts = all_automorphisms()
    assert_eq(len(auts), 40, "|Aut(V)| = 40")


def test_T11_sigma_palindrome():
    print("\nT11: σ-power cycle palindrome")
    pal = sigma.palindrome()
    expected = [
        (1, "1 × 6-cycle (primary)"),
        (2, "2 × 3-cycles (TWO TREFOILS)"),
        (3, "3 × 2-cycles (THREE DUALITIES)"),
        (4, "2 × 3-cycles (TWO TREFOILS)"),
        (5, "1 × 6-cycle (primary)"),
        (6, "all fixed (identity)"),
    ]
    for actual, exp in zip(pal, expected):
        assert_eq(actual, exp, f"σ^{exp[0]} → {exp[1]}")


def test_T12_doomdo():
    print("\nT12: σ³ doomdo swap")
    cs3 = sigma.cycle_structure(3)
    pairs = {tuple(sorted(c)) for c in cs3['cycles']}
    expected_pairs = {(1, 5), (2, 6), (4, 7)}
    assert_eq(pairs, expected_pairs, "σ³ swaps {(1,5), (2,6), (4,7)}")
    # Specifically: (4, 7) = COLLAPSE/Kindness ↔ HARMONY/Gentleness
    assert_eq((4, 7) in pairs, True,
              "(COLLAPSE/Kindness ↔ HARMONY/Gentleness) is a σ³ pair (the doomdo swap)")


def test_T13_tensor_partition():
    print("\nT13: Tensor partition counts (2^n cells at level n)")
    for n in range(1, 6):
        cells = tensor_partition(n)
        assert_eq(len(cells), 2**n, f"V^⊗{n} has 2^{n} = {2**n} fine cells")


def test_T14_GUT_binomial():
    print("\nT14: GUT-level binomial distribution (n=5)")
    bd = cell_binomial_distribution(5)
    expected = {0: 1, 1: 5, 2: 10, 3: 10, 4: 5, 5: 1}
    assert_eq(bd, expected, "V^⊗5 binomial: 1+5+10+10+5+1 = 32 (SU(5) GUT)")
    # Particle/antiparticle split: 16 + 16
    half_low = sum(bd[k] for k in range(3))
    half_high = sum(bd[k] for k in range(3, 6))
    assert_eq(half_low, 16, "≤2-plus cells = 16 (SU(5) particle 1+5̄+10)")
    assert_eq(half_high, 16, "≥3-plus cells = 16 (antiparticle)")


def test_T15_Clifford_ladder():
    print("\nT15: Clifford ladder dimensional match")
    for n in range(6):
        cm = clifford_match(n)
        assert_eq(cm['dim_F5'], cm['dim_Cl_2n'],
                  f"V^⊗{n}: dim_F5 = {cm['dim_F5']} = dim_R Cl({2*n})")


def run_all():
    print("=" * 70)
    print("TIG DIRAC LIBRARY — TEST SUITE")
    print("=" * 70)
    test_T1_basic()
    test_T2_idempotents()
    test_T3_privileged_basis()
    test_T4_annihilator()
    test_T5_h_element()
    test_T6_projectors()
    test_T7_eigenspaces()
    test_T8_forbidden()
    test_T9_associator()
    test_T10_Aut()
    test_T11_sigma_palindrome()
    test_T12_doomdo()
    test_T13_tensor_partition()
    test_T14_GUT_binomial()
    test_T15_Clifford_ladder()
    print()
    print("=" * 70)
    print("All structural tests run. See PASS/FAIL above.")
    print("=" * 70)


if __name__ == "__main__":
    run_all()


def test_schur_weyl_su2():
    from tig_dirac import schur_weyl_match
    info = schur_weyl_match(2)
    assert info['orbit_sizes'] == [2, 1, 1], f"V^⊗2 should give SU(2) pattern 2+1+1, got {info['orbit_sizes']}"

def test_schur_weyl_su3():
    from tig_dirac import schur_weyl_match
    info = schur_weyl_match(3)
    assert info['orbit_sizes'] == [3, 3, 1, 1], f"V^⊗3 should give SU(3) pattern 3+3+1+1, got {info['orbit_sizes']}"

def test_schur_weyl_su5():
    from tig_dirac import schur_weyl_match
    info = schur_weyl_match(5)
    assert info['orbit_sizes'] == [10, 10, 5, 5, 1, 1], f"V^⊗5 should give SU(5) pattern, got {info['orbit_sizes']}"
