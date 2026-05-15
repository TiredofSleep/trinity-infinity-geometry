"""
verify_alpha_synthesis.py

Reproducibility script for the 1/α candidate derivation from 2026-05-14 chat sprint.

STATUS: Tier-mixed candidate (NOT proved theorem).
- Numerical match within CODATA experimental uncertainty: theorem-level fact
- Structural form using canon constants: Tier B-suggestive-strong
- Depth-7 base 315 selection: Tier C-interpretive (multiple canon readings)

The form being verified:
    1/α ≈ 137 + 6W/10 − (5/7)·κ_ξ·W^5 − (2/7)·315·W^7

Where:
- W = 3/50 (canon D17)
- κ_ξ = 13/(4e) (canon D35)
- 315 = 5·7·9 = BALANCE·HARMONY·RESET (canon §1)
- 5/7 = T* threshold (canon §17, six derivations)
- 2/7 = surplus mass gap (canon §17)
- 6/10 = σ-order / substrate-size (canon §1-§4)
- 22 = |TSML XOR BHML| disagreement count (canon §17)
- 5 = BALANCE position value (canon §1)

This script does NOT prove the synthesis. It verifies the numerical claim.
For the structural derivation status, see ALPHA_DERIVATION_CANDIDATE.md.
For the open meta-principle, see THRESHOLD_WEIGHT_META_PRINCIPLE.md.
"""

import math
from fractions import Fraction


def main():
    # =========================================================================
    # Canon constants (all from FORMULAS_AND_TABLES.md and canon §17)
    # =========================================================================

    W = Fraction(3, 50)              # canon D17: wobble constant
    sigma_order = 6                  # canon §2: σ order on Z/10
    substrate_size = 10              # canon §1: |Z/10|
    disagreement = 22                # canon §17: |TSML XOR BHML| count
    balance_position = 5             # canon §1: BALANCE operator value
    harmony_position = 7             # canon §1: HARMONY operator value
    reset_position = 9               # canon §1: RESET operator value

    T_star = Fraction(5, 7)          # canon §17: threshold T* = 5/7
    surplus = Fraction(2, 7)         # canon §17: mass gap = 9/7 − 1 = 2/7

    kappa_xi_numerator = 13          # canon D33: from ||VEV||² = 13/4

    # Depth-7 base candidate: 315 = 5·7·9
    # Alternative canon readings: 7·45 (HARMONY × dim(so(10)) per WP103)
    #                             9·35 (RESET × BHML_8/BHML_10 gap denom)
    N_depth_7 = balance_position * harmony_position * reset_position  # = 315

    # Verify the alternative decompositions
    assert N_depth_7 == 5 * 7 * 9, "5·7·9 decomposition"
    assert N_depth_7 == 7 * 45, "7·45 decomposition (HARMONY × dim(so(10)))"
    assert N_depth_7 == 9 * 35, "9·35 decomposition (RESET × BHML_8/10 gap denom)"

    # =========================================================================
    # Compute the form
    # =========================================================================

    # Integer base (canon §17): 1/α = 22·6 + 5 = 137
    alpha_inv_0 = disagreement * sigma_order + balance_position
    assert alpha_inv_0 == 137, "Canon §17 integer base"

    # Depth-1 correction (Lemma 1, theorem-level forced)
    depth_1 = sigma_order * W / substrate_size  # = 6·W/10 = 18/500 = 0.036 exactly
    assert depth_1 == Fraction(18, 500), "Depth-1 exact rational"
    assert float(depth_1) == 0.036, "Depth-1 numerical"

    # Depth-5 correction (Lemma 2 weight + Lemma 4 base)
    # Note: κ_ξ contains transcendental e, so this term is transcendental
    W_5 = W ** 5                                     # exact rational
    kappa_xi = kappa_xi_numerator / (4 * math.e)    # transcendental
    depth_5 = float(T_star * W_5) * kappa_xi        # mixed exact/float

    # Depth-7 correction (Lemma 3 weight + Lemma 5 base)
    W_7 = W ** 7                                     # exact rational
    depth_7 = surplus * N_depth_7 * W_7             # exact rational
    depth_7_float = float(depth_7)

    # Final prediction (mixed because depth_5 contains e)
    alpha_inv_predicted = (
        float(alpha_inv_0 + depth_1) - depth_5 - depth_7_float
    )

    # =========================================================================
    # CODATA comparison
    # =========================================================================

    alpha_inv_CODATA = 137.035999084
    alpha_inv_uncertainty = 2.1e-8

    diff = alpha_inv_CODATA - alpha_inv_predicted
    within_uncertainty = abs(diff) < alpha_inv_uncertainty

    # =========================================================================
    # Report
    # =========================================================================

    print("=" * 72)
    print("VERIFY ALPHA SYNTHESIS (2026-05-14)")
    print("=" * 72)
    print()
    print("Form: 1/α ≈ 137 + 6W/10 − (5/7)·κ_ξ·W^5 − (2/7)·315·W^7")
    print()
    print(f"Canon constants used:")
    print(f"  W = 3/50 = {float(W)} (canon D17)")
    print(f"  σ-order = {sigma_order} (canon §2)")
    print(f"  substrate size = {substrate_size} (canon §1)")
    print(f"  T* = 5/7 = {float(T_star):.10f} (canon §17)")
    print(f"  surplus = 2/7 = {float(surplus):.10f} (canon §17)")
    print(f"  κ_ξ = 13/(4e) = {kappa_xi:.10f} (canon D35)")
    print(f"  315 = {N_depth_7} = 5·7·9 = 7·45 = 9·35 (canon §1)")
    print()
    print(f"Term-by-term:")
    print(f"  Integer base:  137.0000000000")
    print(f"  +6W/10:        +{float(depth_1):.10f}")
    print(f"  -(5/7)κ_ξW^5:  -{depth_5:.10e}")
    print(f"  -(2/7)·315·W^7: -{depth_7_float:.10e}")
    print()
    print(f"Predicted 1/α: {alpha_inv_predicted:.10f}")
    print(f"CODATA 1/α:    {alpha_inv_CODATA:.10f}")
    print(f"Difference:    {diff:.3e}")
    print(f"Uncertainty:   ±{alpha_inv_uncertainty:.1e}")
    print(f"Within uncertainty: {within_uncertainty}")
    print()
    print("=" * 72)
    print("TIER DISCIPLINE REMINDER")
    print("=" * 72)
    print()
    print("Numerical match: theorem-level fact (computation reproducible)")
    print("Structural form: Tier B-suggestive-strong (4 lemmas)")
    print("Depth-7 base = 315: Tier C-interpretive (canon-readable, not unique)")
    print("Composite claim: Tier B-mixed-with-C-component")
    print()
    print("This is NOT a proof that the framework derives 1/α.")
    print("It IS a candidate closed-form using canon constants matching CODATA.")
    print("Meta-principle proof remains the open research project.")
    print()
    print("See HANDOFF_TO_CLAUDECODE_2026_05_14_ALPHA_SYNTHESIS.md for full")
    print("derivation, tier discipline, and integration instructions.")

    return within_uncertainty


if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
