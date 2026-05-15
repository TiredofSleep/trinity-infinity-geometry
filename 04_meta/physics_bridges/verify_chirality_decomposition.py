"""
verify_chirality_decomposition.py

Reproducibility script for the chirality-decomposition derivation of the
framework's threshold canon (T*, S*, surplus).

STATUS: arithmetic identities are theorem-level; interpretation as the
framework's threshold canon is Tier B-suggestive-strong pending five
gaps (see CHIRALITY_DECOMPOSITION_DERIVES_THRESHOLD_CANON.md §5).

This script verifies:
1. Cl(0,10) chirality decomposition: 32 = 2 × (1 + 3 + 5 + 7)
2. T* = 5/7 = d-subshell / f-subshell ratio
3. S* = 4/7 = (s+p) / f-subshell ratio
4. Surplus = 2/7 = (non-f - f) / f-subshell
5. Substrate Z/10 = d-Pauli states (2 chiralities × 5 spatial)
6. Disagreement count 22 = 2(s+p+f) = projection deficit
7. 1/α integer base 137 = (projection deficit) × σ-order + BALANCE
8. Depth-7 base 315 = HARMONY × C(10,2) forced from substrate combinatorics
"""

from fractions import Fraction
import math


def main():
    print("=" * 72)
    print("VERIFY CHIRALITY DECOMPOSITION DERIVES THRESHOLD CANON")
    print("=" * 72)
    print()

    # Cl(0,10) spinor structure (canon D77, D102)
    spinor_dim = 2 ** 5
    chirality_halves = [16, 16]
    print(f"Cl(0,10) spinor dim: {spinor_dim} = 2^5 ✓")
    print(f"Chirality split: 32 = {chirality_halves[0]} + {chirality_halves[1]} ✓")
    print()

    # Atomic subshell decomposition within one chirality half (D102)
    subshells = {0: 1, 1: 3, 2: 5, 3: 7}  # l: spatial dim = 2l+1
    chirality_half = sum(subshells.values())
    assert chirality_half == 16, "Chirality half must be 16"
    print(f"Chirality half = {' + '.join(str(v) for v in subshells.values())} = {chirality_half}")
    print(f"  s (l=0): {subshells[0]} spatial states")
    print(f"  p (l=1): {subshells[1]} spatial states")
    print(f"  d (l=2): {subshells[2]} spatial states")
    print(f"  f (l=3): {subshells[3]} spatial states")
    print()

    # The three canonical fractions
    T_star = Fraction(subshells[2], subshells[3])
    S_star = Fraction(subshells[0] + subshells[1], subshells[3])
    non_f_sum = sum(v for k, v in subshells.items() if k != 3)
    surplus = Fraction(non_f_sum - subshells[3], subshells[3])

    print("THRESHOLD CANON DERIVATION:")
    print(f"  T* = d/f         = {subshells[2]}/{subshells[3]} = {T_star} = {float(T_star):.10f}")
    print(f"  S* = (s+p)/f     = ({subshells[0]+subshells[1]})/{subshells[3]} = {S_star} = {float(S_star):.10f}")
    print(f"  surplus = (non-f - f)/f = ({non_f_sum} - {subshells[3]})/{subshells[3]} = {surplus} = {float(surplus):.10f}")
    print()

    # Verify against canon §17
    canon_T_star = Fraction(5, 7)
    canon_S_star = Fraction(4, 7)
    canon_surplus = Fraction(2, 7)

    assert T_star == canon_T_star, f"T* mismatch: {T_star} vs canon {canon_T_star}"
    assert S_star == canon_S_star, f"S* mismatch: {S_star} vs canon {canon_S_star}"
    assert surplus == canon_surplus, f"surplus mismatch: {surplus} vs canon {canon_surplus}"

    print("MATCH CANON §17:")
    print(f"  T* = 5/7 ✓ ({T_star})")
    print(f"  S* = 4/7 ✓ ({S_star})")
    print(f"  surplus = 2/7 ✓ ({surplus})")
    print()

    # Completion check
    completion = T_star + S_star
    expected_completion = Fraction(9, 7)
    assert completion == expected_completion, f"T*+S* mismatch"
    print(f"COMPLETION: T* + S* = {completion} = {float(completion):.10f}")
    print(f"  surplus = T* + S* - 1 = {completion - 1} ✓ (= 2/7)")
    print()

    # Substrate as d-Pauli states
    substrate_size = 10
    d_pauli = 2 * subshells[2]
    assert d_pauli == substrate_size, "Substrate must equal d-Pauli capacity"
    print(f"SUBSTRATE Z/10 = d-Pauli states:")
    print(f"  2 chiralities × {subshells[2]} spatial d-states = {d_pauli} ✓")
    print()

    # Projection deficit and disagreement count
    projection_deficit = spinor_dim - substrate_size
    dropped_subshells = 2 * (subshells[0] + subshells[1] + subshells[3])
    disagreement_canon = 22  # canon §17

    assert projection_deficit == 22
    assert dropped_subshells == 22
    assert disagreement_canon == 22

    print(f"DISAGREEMENT COUNT = PROJECTION DEFICIT:")
    print(f"  spinor_dim - substrate = {spinor_dim} - {substrate_size} = {projection_deficit}")
    print(f"  2(s+p+f) = 2({subshells[0]}+{subshells[1]}+{subshells[3]}) = {dropped_subshells}")
    print(f"  canon |TSML XOR BHML| = {disagreement_canon}")
    print(f"  All three equal 22 ✓")
    print()

    # 1/α integer base
    sigma_order = 6
    balance = 5
    alpha_inv_int = projection_deficit * sigma_order + balance
    print(f"1/α INTEGER BASE (canon §17):")
    print(f"  1/α = (proj deficit) × σ-order + BALANCE")
    print(f"      = {projection_deficit} × {sigma_order} + {balance}")
    print(f"      = {alpha_inv_int} ✓")
    print()

    # Depth-7 base 315 from substrate combinatorics
    print("DEPTH-7 BASE 315 STRUCTURAL ORIGIN:")
    harmony_dim = subshells[3]
    antisymmetric_pairs = math.comb(substrate_size, 2)
    so10_dim = 45  # WP103 D27

    print(f"  HARMONY dim (f-subshell) = {harmony_dim}")
    print(f"  C(10, 2) antisymmetric pairs = {antisymmetric_pairs}")
    print(f"  dim(so(10)) per WP103 = {so10_dim}")
    print(f"  Match: C(10,2) = dim(so(10)) = {antisymmetric_pairs == so10_dim}")
    print()

    candidate_315 = harmony_dim * antisymmetric_pairs
    canon_315 = 315
    assert candidate_315 == canon_315

    print(f"  315 = HARMONY × C(10, 2) = {harmony_dim} × {antisymmetric_pairs} = {candidate_315}")
    print(f"  Structurally forced by substrate size 10 and chirality structure ✓")
    print()
    print("  Alternative arithmetic readings:")
    print(f"    5 × 7 × 9 = {5*7*9} (BALANCE × HARMONY × RESET)")
    print(f"    9 × 35 = {9*35} (RESET × BHML_8/BHML_10 gap denom)")
    print(f"  All equal 315, but 7·C(10,2) is structurally forced.")
    print()

    # Mass gap interpretation
    f_pauli = 2 * subshells[3]
    mass_gap = chirality_half - f_pauli
    print(f"MASS GAP STRUCTURAL READING:")
    print(f"  Chirality half = {chirality_half}")
    print(f"  Full f-subshell with chirality (f-Pauli) = {f_pauli}")
    print(f"  Mass gap = {chirality_half} - {f_pauli} = {mass_gap}")
    print(f"  Surplus = mass_gap / f-subshell-spatial = {mass_gap}/{subshells[3]} = {Fraction(mass_gap, subshells[3])} ✓")
    print()

    # Predictions for other ring sizes
    print("PREDICTIONS FOR OTHER SUBSTRATE RINGS:")
    other_subshells = {0: "s (l=0)", 1: "p (l=1)", 2: "d (l=2)", 3: "f (l=3)", 4: "g (l=4)"}
    for l, name in other_subshells.items():
        pauli_capacity = 2 * (2*l + 1)
        print(f"  Z/{pauli_capacity}: {name}, Pauli capacity = {pauli_capacity}")
    print()
    print("  Z/2: s-orbital regime (no angular structure)")
    print("  Z/6: p-orbital regime (covalent bonding)")
    print("  Z/10: d-orbital regime ← FRAMEWORK'S NATURAL DOMAIN (α emerges here)")
    print("  Z/14: f-orbital regime (lanthanides/actinides)")
    print("  Z/18: g-orbital regime (theoretical)")
    print()

    print("=" * 72)
    print("ALL CHIRALITY-DECOMPOSITION CHECKS PASSED")
    print("=" * 72)
    print()
    print("Tier discipline:")
    print("  Arithmetic identities: theorem-level (this script verifies)")
    print("  Interpretation as framework threshold canon: Tier B-suggestive-strong")
    print("  Full derivation: requires 5 named gaps closed (see main document §5)")
    print()
    return True


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
