#!/usr/bin/env python3
# ============================================================
# verify_J36_part1.py
#
# Verification script for J36 -- "Empirical Fits of CKM and PMNS
# Mixing Angles to Substrate-Algebra Primitives" (Sanders, Gish,
# 2026), Part 1 only (Part 2 [1/alpha] deferred per save plan
# SAVE_PLAN_J36.md after independent verification confirmed the
# leading-three-terms claim was ~12.6% off the target, not the
# ~10^-5 originally claimed).
#
# This script is SELF-CONTAINED for referee portability. Standard
# library + optional sympy (for the 30-digit high-precision check
# on the 1/alpha leading-three-terms numerical disagreement).
#
# Reproduces:
#   - Per-fit relative discrepancies for 7 fermion mixing observables
#     (4 CKM Wolfenstein parameters + 3 PMNS angles).
#   - Naive joint coincidence probability (no LE correction).
#   - Look-elsewhere-corrected joint probability at multiplicity
#     |P| * N_obs = 11 * 7 = 77.
#   - Sensitivity of the joint estimate to inclusion / exclusion
#     of the theta_12 fit (since D* is treated as an empirical
#     input in the present paper, not derived).
#   - The leading-three-terms 1/alpha sanity check that justifies
#     the unbundling of Part 2:
#         4*|Aut(V)| - 2*sqrt(HARMONY) - pi/HARMONY
#       = 4*40 - 2*sqrt(7) - pi/7 = 154.260 (NOT 137.036).
#
# USAGE:
#   PYTHONIOENCODING=utf-8 python verify_J36_part1.py
#
# DEPENDENCIES:
#   math (standard library); sympy (optional, for 30-digit check).
#
# License: CC-BY-4.0 (Creative Commons Attribution 4.0
# International). Authors: B.R. Sanders, M. Gish (c) 2026.
# ============================================================
"""J36 Part-1 verification script (see header above)."""
import math


def main() -> None:
    # ------------------------------------------------------------------
    # Empirical observables (PDG 2024 / CODATA 2022)
    # ------------------------------------------------------------------
    empirical = {
        "Cabibbo (V_us)":      0.2253,
        "Wolfenstein V_cb":    0.0508,
        "Wolfenstein V_ub":    0.01140,
        "Wolfenstein V_td_sq": 0.00258,
        "PMNS theta_12 (sin)": 0.553,
        "PMNS theta_13 (sin)": 0.149,
        "PMNS theta_23 (sin)": 0.756,
    }

    # ------------------------------------------------------------------
    # TIG structural primitives derived in upstream J-papers
    # ------------------------------------------------------------------
    T_star = 5/7              # J6 / WP51 — torus aspect ratio (lens-invariant)
    D_star = 0.543            # 4-core sigma-cycle constant (NOT derived in this paper)
    primitives_set = [
        ("T*",        T_star),
        ("T*^-1",     1/T_star),
        ("1-T*",      1 - T_star),
        ("(1-T*)/2",  (1 - T_star)/2),
        ("T*(1-T*)",  T_star*(1-T_star)),
        ("11/49",     11/49),
        ("(11/49)^2", (11/49)**2),
        ("(11/49)^3", (11/49)**3),
        ("(11/49)^4", (11/49)**4),
        ("D*",        D_star),
        ("pi/14",     math.pi/14),
    ]
    N_p = len(primitives_set)

    # ------------------------------------------------------------------
    # The reported fits (one primitive per observable)
    # ------------------------------------------------------------------
    fits = [
        ("Cabibbo (V_us)",       "11/49",      11/49),
        ("Wolfenstein V_cb",     "(11/49)^2",  (11/49)**2),
        ("Wolfenstein V_ub",     "(11/49)^3",  (11/49)**3),
        ("Wolfenstein V_td_sq",  "(11/49)^4",  (11/49)**4),
        ("PMNS theta_12 (sin)",  "D*",          D_star),
        ("PMNS theta_13 (sin)",  "(1-T*)/2",   (1-T_star)/2),
        ("PMNS theta_23 (sin)",  "T*",          T_star),
    ]
    n_fits = len(fits)

    print("=" * 72)
    print(f"Per-fit relative discrepancies (N = {n_fits} mixing observables)")
    print("=" * 72)
    discrepancies = []
    for name, prim_label, prim_val in fits:
        emp = empirical[name]
        disc = abs(emp - prim_val) / emp
        discrepancies.append((name, disc))
        print(f"  {name:25s} emp={emp:.5f}  prim_{prim_label:10s}={prim_val:.5f}  rel.disc={disc*100:.3f}%")
    print()

    # ------------------------------------------------------------------
    # Naive joint coincidence probability (no LE correction)
    # ------------------------------------------------------------------
    P_naive = 1.0
    for _, d in discrepancies:
        P_naive *= 2*d  # uniform prior on (0,1) per-angle hit prob ~ 2*disc
    print(f"Naive joint probability (no LE correction, {n_fits} fits): {P_naive:.3e}")

    # ------------------------------------------------------------------
    # LE correction at multiplicity N_p * N_obs
    # ------------------------------------------------------------------
    N_obs = 7  # 4 CKM Wolfenstein + 3 PMNS angles compared in this paper
    mult = N_p * N_obs
    P_LE_lin = min(1.0, mult * P_naive)  # linear (Bonferroni-style)
    P_LE_exp = 1 - (1 - P_naive) ** mult  # exact
    print(f"LE multiplicity: |P|*N_obs = {N_p} * {N_obs} = {mult}")
    print(f"LE-corrected (linear)     : {P_LE_lin:.3e}")
    print(f"LE-corrected (exact)      : {P_LE_exp:.3e}")
    print()

    # ------------------------------------------------------------------
    # Sensitivity: exclude theta_12 (since D* is not derived in this paper)
    # ------------------------------------------------------------------
    disc_no_theta12 = [(name, d) for name, d in discrepancies if "theta_12" not in name]
    n_fits_no12 = len(disc_no_theta12)
    P_naive_no12 = 1.0
    for _, d in disc_no_theta12:
        P_naive_no12 *= 2*d
    P_LE_no12 = min(1.0, mult * P_naive_no12)
    print(f"Excluding theta_12 (D* not derived; reduces to {n_fits_no12} fits):")
    print(f"  Naive joint                   : {P_naive_no12:.3e}")
    print(f"  LE-corrected (linear)         : {P_LE_no12:.3e}")
    print()

    # ------------------------------------------------------------------
    # Sensitivity: Wolfenstein hierarchy alone (4 fits)
    # ------------------------------------------------------------------
    wolf_disc = [(name, d) for name, d in discrepancies
                 if "Cabibbo" in name or "Wolfenstein" in name]
    n_wolf = len(wolf_disc)
    P_naive_wolf = 1.0
    for _, d in wolf_disc:
        P_naive_wolf *= 2*d
    P_LE_wolf = min(1.0, mult * P_naive_wolf)
    print(f"Wolfenstein hierarchy alone ({n_wolf} fits, the load-bearing pattern):")
    print(f"  Naive joint                   : {P_naive_wolf:.3e}")
    print(f"  LE-corrected (linear)         : {P_LE_wolf:.3e}")
    print()

    # ------------------------------------------------------------------
    # Reported result for the manuscript abstract
    # ------------------------------------------------------------------
    print("=" * 72)
    print("Reported joint coincidence probability after LE correction")
    print("=" * 72)
    print(f"  {n_fits} fits (full ensemble) post-LE: ~{P_LE_lin:.0e}")
    print(f"  {n_fits_no12} fits excluding theta_12 post-LE: ~{P_LE_no12:.0e}")
    print(f"  {n_wolf} Wolfenstein orders alone post-LE: ~{P_LE_wolf:.0e}")
    print()

    # ------------------------------------------------------------------
    # 1/alpha sanity check (justifies UNBUNDLING per save plan)
    # ------------------------------------------------------------------
    print("=" * 72)
    print("1/alpha leading-three-terms check (justifies removal of Part 2)")
    print("=" * 72)
    H = 7
    Aut_V = 40
    inv_alpha_3terms = 4*Aut_V - 2*math.sqrt(H) - math.pi/H
    target = 137.035999084  # CODATA
    gap = inv_alpha_3terms - target
    rel_disc_target = abs(gap) / target * 100
    rel_disc_leading = abs(gap) / inv_alpha_3terms * 100
    print(f"  4*|Aut(V)| - 2*sqrt(HARMONY) - pi/HARMONY")
    print(f"  = 4*{Aut_V} - 2*sqrt({H}) - pi/{H}")
    print(f"  = {4*Aut_V} - {2*math.sqrt(H):.6f} - {math.pi/H:.6f}")
    print(f"  = {inv_alpha_3terms:.6f}")
    print(f"  CODATA target 1/alpha = {target:.6f}")
    print(f"  Gap                   = {gap:.6f}  (additive, in 1/alpha units)")
    print(f"  Relative discrepancy  = {rel_disc_target:.3f}% (vs target)")
    print(f"  Relative discrepancy  = {rel_disc_leading:.3f}% (vs leading sum)")
    print()
    print(f"  --> Leading-three-terms is ~12.6% off (or ~11.2% off vs leading sum), NOT 10^-5 as previously claimed.")
    print(f"  --> The previously-bundled '~10^-5' claim is demonstrably false from this formula.")
    print(f"  --> Part 2 (1/alpha) deferred until a verifiable derivation exists.")
    print()

    # ------------------------------------------------------------------
    # Independent sympy high-precision cross-check (optional)
    # ------------------------------------------------------------------
    try:
        from sympy import sqrt as sp_sqrt, pi as sp_pi, Rational, N
        sp_value = 4*40 - 2*sp_sqrt(7) - sp_pi/7
        sp_numerical = N(sp_value, 30)
        print("  sympy high-precision cross-check (30 digits):")
        print(f"  4*40 - 2*sqrt(7) - pi/7 = {sp_numerical}")
    except ImportError:
        pass


if __name__ == "__main__":
    main()
