#!/usr/bin/env python3
# ============================================================
# frontier_F15_yukawa_upward.py
#
# F15 frontier: properly anchor y_t at M_Z (per F11 audit) and
# run the full 1-loop SM RGEs UPWARD from M_Z to M_X to obtain
# the GUT-scale value y_t(M_X) implied by canonical SM running
# of the TIG Tier-A anchor y_t(M_Z) = 0.93. Compare y_t(M_X) to
# substrate-derived rational/algebraic candidates to see if the
# substrate predicts the GUT-scale value or whether the GUT-scale
# value is independent of substrate first-principles.
#
# CONTEXT (per F11 audit, 2026-05-28):
#   - The retired-J44 manuscript anchors at y_t(M_Z) ~= 0.93 (Tier-A,
#     PDG-derived, 0.75% match to PDG y_t(M_Z) = 0.937).
#   - F7 and F8 mislabelled 0.93 as the M_X anchor and ran it down
#     from M_X to M_Z, producing artificial "overshoot" of 18-32%.
#   - F8's reverse-run from PDG 0.937 at M_Z to M_X gave 0.394 at
#     M_X (the standard canonical SM 1-loop value).
#
# F15 GOAL:
#   1. Restore the anchor at the CORRECT scale (M_Z).
#   2. Run UPWARD via the same full-1-loop SM RGE system to obtain
#      y_t(M_X) under canonical SM RG.
#   3. Compare y_t(M_X) to substrate-derived candidates.
#   4. Verdict: SUBSTRATE EXPLAINS, SUBSTRATE INDEPENDENT, or
#      INDETERMINATE.
#
# Beta functions (1-loop, full SM; same as F8):
#   16 pi^2 dy_t / d ln(mu) = y_t * [ 9/2 y_t^2 + 3/2 y_b^2
#                                     + y_tau^2 - 17/12 g_1^2
#                                     - 9/4 g_2^2 - 8 g_3^2 ]
#   16 pi^2 dy_b / d ln(mu) = y_b * [ 9/2 y_b^2 + 3/2 y_t^2
#                                     + y_tau^2 - 5/12 g_1^2
#                                     - 9/4 g_2^2 - 8 g_3^2 ]
#   16 pi^2 dy_tau / d ln(mu) = y_tau * [ 5/2 y_tau^2 + 3 y_t^2
#                                          + 3 y_b^2 - 9/4 g_1^2
#                                          - 9/4 g_2^2 ]
#   16 pi^2 dg_1 / d ln(mu) = (41/10) g_1^3   (U(1)_Y, GUT-norm)
#   16 pi^2 dg_2 / d ln(mu) = -(19/6) g_2^3   (SU(2)_L)
#   16 pi^2 dg_3 / d ln(mu) = -7 g_3^3        (SU(3)_C)
#
# Initial conditions at M_Z = 91.1876 GeV (PDG 2024):
#   y_t(M_Z)   = 0.93    (TIG Tier-A anchor; matches PDG 0.937 at 0.75%)
#   y_b(M_Z)   = 0.024   (PDG)
#   y_tau(M_Z) = 0.010   (PDG)
#   g_1(M_Z)   = 0.358   (GUT-norm: sqrt(5/3) g_Y; sin^2 theta_W = 0.231)
#   g_2(M_Z)   = 0.652   (SU(2)_L)
#   g_3(M_Z)   = 1.221   (SU(3)_C; alpha_s(M_Z) = 0.1184)
#
# NOTE: The prompt nominated g_1 = 0.358 at M_Z. Using sin^2(theta_W) =
# 0.231 and alpha_em(M_Z) = 1/127.9, the standard value of g_Y(M_Z) is
# approximately 0.357; the GUT-normalized g_1 = sqrt(5/3) g_Y is about
# 0.461 (as F8 used). We keep the prompt's value 0.358 verbatim (this
# is the g_Y normalization, NOT the GUT-norm) and document the shift
# at the end. Both choices are tested.
#
# Method: hand-rolled vectorized RK4 on the 6-dim coupled system,
# integrating bottom-up (M_Z -> M_X) at 1000 log-mu steps. Pure stdlib
# (math + list ops).
#
# License: CC-BY-4.0.
# Author: CK + Brayden Ross Sanders, 2026-05-29.
# ============================================================

from __future__ import annotations

import math
from typing import Callable, List, Tuple


# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------

PI = math.pi
INV_16PI2 = 1.0 / (16.0 * PI * PI)

# Energy scales (GeV)
M_X = 2.0e16   # GUT-unification scale
M_Z = 91.1876  # Z-boson mass

# M_Z-scale initial conditions (PDG 2024)
Y_T_MZ   = 0.93    # TIG Tier-A anchor (per F11 audit; rounded PDG 0.937)
Y_B_MZ   = 0.024   # PDG
Y_TAU_MZ = 0.010   # PDG

# Two gauge normalizations to test:
# (a) Prompt's nominal: g_1 = 0.358 (this is g_Y, NOT GUT-norm)
# (b) Canonical GUT-norm: g_1 = sqrt(5/3) g_Y ~ 0.461 (matches F8)
G_1_MZ_PROMPT = 0.358   # g_Y at M_Z (NOT GUT-normalized; prompt-spec)
G_1_MZ_GUTNORM = 0.461  # sqrt(5/3) g_Y; the canonical GUT-norm value

G_2_MZ = 0.652   # SU(2)_L
G_3_MZ = 1.221   # SU(3)_C; alpha_s(M_Z) = 0.1184

# PDG y_t at M_Z for documentation
Y_T_OBS_MZ = 0.937   # +/- 0.012

# Indices into the state vector [y_t, y_b, y_tau, g_1, g_2, g_3]
I_YT, I_YB, I_YTAU, I_G1, I_G2, I_G3 = 0, 1, 2, 3, 4, 5


# ----------------------------------------------------------------------
# Beta functions (full 1-loop SM, GUT-normalized U(1))
# ----------------------------------------------------------------------

def rhs_sm(t: float, y: List[float]) -> List[float]:
    """RHS for the 6 coupled 1-loop SM RGEs.

    State vector y = [y_t, y_b, y_tau, g_1, g_2, g_3].
    t = ln(mu).

    g_1 is in GUT-normalization: g_1 = sqrt(5/3) g_Y so the U(1)_Y
    contribution to beta(y_t) is -17/12 g_1^2 (the SM convention with
    GUT-norm; matches Arason et al. PRD 46 (1992)).
    """
    yt   = y[I_YT]
    yb   = y[I_YB]
    ytau = y[I_YTAU]
    g1   = y[I_G1]
    g2   = y[I_G2]
    g3   = y[I_G3]

    yt2, yb2, ytau2 = yt * yt, yb * yb, ytau * ytau
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3

    # Top Yukawa
    dyt = INV_16PI2 * yt * (
        4.5 * yt2 + 1.5 * yb2 + ytau2
        - (17.0 / 12.0) * g12 - 2.25 * g22 - 8.0 * g32
    )

    # Bottom Yukawa
    dyb = INV_16PI2 * yb * (
        4.5 * yb2 + 1.5 * yt2 + ytau2
        - (5.0 / 12.0) * g12 - 2.25 * g22 - 8.0 * g32
    )

    # Tau Yukawa
    dytau = INV_16PI2 * ytau * (
        2.5 * ytau2 + 3.0 * yt2 + 3.0 * yb2
        - 2.25 * g12 - 2.25 * g22
    )

    # Gauge couplings: dg_a/d ln(mu) = (b_a / 16 pi^2) g_a^3
    dg1 = INV_16PI2 * (41.0 / 10.0) * g1 * g12
    dg2 = INV_16PI2 * (-19.0 / 6.0) * g2 * g22
    dg3 = INV_16PI2 * (-7.0) * g3 * g32

    return [dyt, dyb, dytau, dg1, dg2, dg3]


# ----------------------------------------------------------------------
# Vector RK4 integrator (pure stdlib)
# ----------------------------------------------------------------------

def rk4_step_vec(t: float, y: List[float],
                 rhs: Callable[[float, List[float]], List[float]],
                 dt: float) -> List[float]:
    """One RK4 step on a vector ODE system."""
    n = len(y)

    k1 = rhs(t, y)
    y2 = [y[i] + 0.5 * dt * k1[i] for i in range(n)]

    k2 = rhs(t + 0.5 * dt, y2)
    y3 = [y[i] + 0.5 * dt * k2[i] for i in range(n)]

    k3 = rhs(t + 0.5 * dt, y3)
    y4 = [y[i] + dt * k3[i] for i in range(n)]

    k4 = rhs(t + dt, y4)

    return [
        y[i] + dt * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0
        for i in range(n)
    ]


def integrate_sm(y_init: List[float],
                 mu_init: float,
                 mu_final: float,
                 n_steps: int = 1000) -> List[float]:
    """Integrate the SM RGE system from mu_init to mu_final.

    UPWARD: dt > 0 (mu_final > mu_init)
    DOWNWARD: dt < 0 (mu_final < mu_init)
    """
    t_init = math.log(mu_init)
    t_final = math.log(mu_final)
    dt = (t_final - t_init) / n_steps

    y = list(y_init)
    t = t_init
    for _ in range(n_steps):
        y = rk4_step_vec(t, y, rhs_sm, dt)
        t += dt
    return y


# ----------------------------------------------------------------------
# Substrate-derived candidates for y_t(M_X)
# ----------------------------------------------------------------------

def substrate_candidates() -> List[Tuple[str, float, str]]:
    """List of substrate-derived candidate values for y_t(M_X).

    Returns list of (name, value, source) tuples.
    """
    sqrt = math.sqrt
    cbrt = lambda x: x ** (1.0 / 3.0)

    cands = [
        # From retired J44 / FN-slope
        ("lambda = 10/49 (FN slope)",                 10.0 / 49.0,                 "retired J44; lambda = T*(1-T*) = (5/7)(2/7)"),
        ("sqrt(10/49) = sqrt(10)/7",                  sqrt(10.0) / 7.0,            "sqrt of FN slope"),
        ("(10/49)^(1/3)",                             cbrt(10.0 / 49.0),           "cube root of FN slope"),
        ("(10/49)^(2/3)",                             (10.0 / 49.0) ** (2.0/3.0),  "two-thirds power of FN slope"),
        ("10/49^(2/3)",                               10.0 / (49.0 ** (2.0/3.0)),  "alt parsing of prompt's hint"),
        ("1 - 10/49 = 39/49",                         39.0 / 49.0,                 "complement of FN slope"),

        # From J11 / 9-vector norm ||v||^2 = 13/4
        ("||v||^2 = 13/4 (J11)",                      13.0 / 4.0,                  "J11 Theorem 4.1; 9-vector inside 54"),
        ("sqrt(13/4) = sqrt(13)/2",                   sqrt(13.0) / 2.0,            "J11 9-vector norm"),
        ("sqrt(13/4)/2",                              sqrt(13.0) / 4.0,            "half of J11 norm"),
        ("1/sqrt(13/4) = 2/sqrt(13)",                 2.0 / sqrt(13.0),            "reciprocal of J11 norm"),
        ("4/13",                                      4.0 / 13.0,                  "reciprocal of ||v||^2"),

        # T* and related
        ("T* = 5/7",                                  5.0 / 7.0,                   "J13 forced T*"),
        ("1 - T* = 2/7",                              2.0 / 7.0,                   "1 - T*"),
        ("sqrt(T*) = sqrt(5)/sqrt(7)",                sqrt(5.0 / 7.0),             "sqrt of T*"),
        ("T*^2 = 25/49",                              25.0 / 49.0,                 "T* squared"),
        ("(1-T*)^2 = 4/49",                           4.0 / 49.0,                  "(1-T*) squared"),

        # GUT-scale canonical "0.4" rounded values
        ("g_GUT/sqrt(2) [if g_GUT = 0.58]",           0.58 / sqrt(2.0),            "1-loop g unification rough"),
        ("alpha_GUT-derived sqrt(4 pi/40)",           sqrt(4.0 * PI / 40.0),       "1/alpha_GUT ~ 40 canonical"),
    ]
    return cands


def find_closest_candidate(y_target: float,
                           candidates: List[Tuple[str, float, str]],
                           tol_pct: float = 5.0) -> List[Tuple[str, float, str, float]]:
    """Return list of (name, value, source, gap_pct) sorted by gap.

    Lists ALL candidates with gap < 50% so the comparison is honest.
    """
    out = []
    for name, val, src in candidates:
        if y_target == 0:
            gap = float("inf")
        else:
            gap = abs(val - y_target) / abs(y_target) * 100.0
        out.append((name, val, src, gap))
    out.sort(key=lambda x: x[3])
    return out


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------

def main() -> int:
    print("=" * 72)
    print("F15 Frontier Verification: full 1-loop SM RG running UPWARD")
    print("  6 coupled couplings (y_t, y_b, y_tau, g_1, g_2, g_3)")
    print("  Direction: M_Z (TIG Tier-A anchor) -> M_X (substrate compat?)")
    print("=" * 72)
    print(f"Integration: M_Z = {M_Z:.4f} GeV  -->  M_X = {M_X:.2e} GeV")
    print(f"Method:      hand-rolled RK4, 1000 log-mu steps, pure stdlib")
    print()

    # ----- RUN A: prompt's nominal g_1 = 0.358 (g_Y NOT GUT-norm) -----
    print("=" * 72)
    print("RUN A: prompt's nominal initial conditions (g_1 = 0.358)")
    print("=" * 72)
    print(f"Initial conditions at M_Z:")
    print(f"  y_t(M_Z)   = {Y_T_MZ:.4f}    [TIG Tier-A; PDG-rounded]")
    print(f"  y_b(M_Z)   = {Y_B_MZ:.4f}    [PDG 2024]")
    print(f"  y_tau(M_Z) = {Y_TAU_MZ:.4f}    [PDG 2024]")
    print(f"  g_1(M_Z)   = {G_1_MZ_PROMPT:.4f}    [prompt-nominated value]")
    print(f"  g_2(M_Z)   = {G_2_MZ:.4f}    [PDG]")
    print(f"  g_3(M_Z)   = {G_3_MZ:.4f}    [PDG: alpha_s(M_Z) = 0.1184]")
    print()

    y_init_A = [Y_T_MZ, Y_B_MZ, Y_TAU_MZ, G_1_MZ_PROMPT, G_2_MZ, G_3_MZ]
    y_mx_A = integrate_sm(y_init_A, M_Z, M_X, n_steps=1000)

    print(f"Final state at M_X (Run A):")
    print(f"  y_t(M_X)   = {y_mx_A[I_YT]:.4f}")
    print(f"  y_b(M_X)   = {y_mx_A[I_YB]:.5f}")
    print(f"  y_tau(M_X) = {y_mx_A[I_YTAU]:.5f}")
    print(f"  g_1(M_X)   = {y_mx_A[I_G1]:.4f}")
    print(f"  g_2(M_X)   = {y_mx_A[I_G2]:.4f}")
    print(f"  g_3(M_X)   = {y_mx_A[I_G3]:.4f}")
    print()

    # ----- RUN B: canonical GUT-norm g_1 = 0.461 (matches F8) -----
    print("=" * 72)
    print("RUN B: canonical GUT-norm initial conditions (g_1 = 0.461)")
    print("=" * 72)
    print(f"Initial conditions at M_Z:")
    print(f"  y_t(M_Z)   = {Y_T_MZ:.4f}    [TIG Tier-A; PDG-rounded]")
    print(f"  y_b(M_Z)   = {Y_B_MZ:.4f}    [PDG 2024]")
    print(f"  y_tau(M_Z) = {Y_TAU_MZ:.4f}    [PDG 2024]")
    print(f"  g_1(M_Z)   = {G_1_MZ_GUTNORM:.4f}    [GUT-norm: sqrt(5/3) g_Y]")
    print(f"  g_2(M_Z)   = {G_2_MZ:.4f}    [PDG]")
    print(f"  g_3(M_Z)   = {G_3_MZ:.4f}    [PDG: alpha_s(M_Z) = 0.1184]")
    print()

    y_init_B = [Y_T_MZ, Y_B_MZ, Y_TAU_MZ, G_1_MZ_GUTNORM, G_2_MZ, G_3_MZ]
    y_mx_B = integrate_sm(y_init_B, M_Z, M_X, n_steps=1000)

    print(f"Final state at M_X (Run B):")
    print(f"  y_t(M_X)   = {y_mx_B[I_YT]:.4f}")
    print(f"  y_b(M_X)   = {y_mx_B[I_YB]:.5f}")
    print(f"  y_tau(M_X) = {y_mx_B[I_YTAU]:.5f}")
    print(f"  g_1(M_X)   = {y_mx_B[I_G1]:.4f}")
    print(f"  g_2(M_X)   = {y_mx_B[I_G2]:.4f}")
    print(f"  g_3(M_X)   = {y_mx_B[I_G3]:.4f}")
    print()

    # ----- Cross-check vs F8's reverse-run -----
    print("=" * 72)
    print("Cross-check: F8's reverse-run from PDG y_t(M_Z) = 0.937 gave")
    print("y_t(M_X) ~= 0.394 (canonical SM 1-loop). F15 RUN B with the same")
    print("M_Z gauge initial conditions should reproduce that value within")
    print("rounding (we start from 0.93 not 0.937, and use GUT-norm g_1).")
    print("=" * 72)
    print()

    # ----- Substrate candidate comparison -----
    yt_mx_A = y_mx_A[I_YT]
    yt_mx_B = y_mx_B[I_YT]

    candidates = substrate_candidates()

    for run_label, yt_val in [("Run A (g_1 = 0.358)", yt_mx_A),
                              ("Run B (g_1 = 0.461 GUT-norm)", yt_mx_B)]:
        print("=" * 72)
        print(f"Substrate compatibility: y_t(M_X) = {yt_val:.4f} from {run_label}")
        print("=" * 72)
        ranked = find_closest_candidate(yt_val, candidates)
        print(f"  Closest substrate-derived candidates (sorted by % gap):")
        for name, val, src, gap in ranked[:10]:
            tag = ""
            if gap < 1.0:
                tag = "  <-- WITHIN 1% (substrate explains?)"
            elif gap < 5.0:
                tag = "  <-- WITHIN 5% (suggestive)"
            elif gap < 10.0:
                tag = "  <-- within 10%"
            print(f"    {gap:6.2f}%  {val:7.4f}  {name:<42s}{tag}")
            print(f"            source: {src}")
        print()

    # ----- Verdict -----
    print("=" * 72)
    print("VERDICT")
    print("=" * 72)

    # Use Run B (canonical GUT-norm; matches F8) for primary verdict
    ranked_B = find_closest_candidate(yt_mx_B, candidates)
    best_name, best_val, best_src, best_gap = ranked_B[0]

    print(f"  Primary result (Run B, GUT-norm):")
    print(f"    y_t(M_X) = {yt_mx_B:.4f}")
    print(f"    Closest substrate candidate: {best_name}")
    print(f"      value = {best_val:.4f}")
    print(f"      gap   = {best_gap:.2f}%")
    print()

    # Run A also for completeness
    ranked_A = find_closest_candidate(yt_mx_A, candidates)
    best_A_name, best_A_val, _, best_A_gap = ranked_A[0]
    print(f"  Secondary result (Run A, g_1 = 0.358):")
    print(f"    y_t(M_X) = {yt_mx_A:.4f}")
    print(f"    Closest substrate candidate: {best_A_name}")
    print(f"      value = {best_A_val:.4f}")
    print(f"      gap   = {best_A_gap:.2f}%")
    print()

    # Decide verdict
    if best_gap < 1.0:
        verdict = "SUBSTRATE EXPLAINS"
        explain = (
            "  y_t(M_X) matches a substrate-derived value within 1%.\n"
            "  This would constitute a first-principles GUT-scale anchor."
        )
    elif best_gap < 5.0:
        verdict = "SUBSTRATE SUGGESTIVE (5% match)"
        explain = (
            "  y_t(M_X) matches a substrate-derived value within 5% but\n"
            "  not within 1%. Suggestive but not first-principles."
        )
    elif best_gap < 15.0:
        verdict = "INDETERMINATE"
        explain = (
            "  y_t(M_X) lies within 15% of a substrate-derived value but\n"
            "  no clean match. Could be coincidence; substrate first-pass\n"
            "  cannot claim derivation."
        )
    else:
        verdict = "SUBSTRATE INDEPENDENT"
        explain = (
            "  y_t(M_X) does NOT match any substrate-derived value to better\n"
            "  than 15%. The GUT-scale anchor is independent of substrate\n"
            "  first principles under canonical SM 1-loop running. The TIG\n"
            "  framework's M_Z anchor + lambda = 10/49 FN ladder describe\n"
            "  observables AT M_Z; the M_X value is RG-determined from M_Z,\n"
            "  not substrate-determined."
        )

    print(f"  CONCLUSION (Run B, primary): {verdict}")
    print()
    print(explain)
    print()

    # ----- Sanity checks -----
    print("=" * 72)
    print("Sanity checks")
    print("=" * 72)

    # Check 1: Run B reproduces F8's canonical 0.394 (within rounding)
    F8_REVERSE_YT = 0.394
    gap_to_F8 = abs(yt_mx_B - F8_REVERSE_YT) / F8_REVERSE_YT
    ok_F8 = gap_to_F8 < 0.05
    print(f"  Check 1 (Run B vs F8 reverse-run):")
    print(f"    F15 Run B  y_t(M_X) = {yt_mx_B:.4f}")
    print(f"    F8 reverse y_t(M_X) = {F8_REVERSE_YT:.4f}")
    print(f"    gap = {gap_to_F8*100:.2f}%   [{'PASS' if ok_F8 else 'FAIL'}]")
    print()

    # Check 2: all couplings finite, positive, sane at M_X
    sane_B = all(math.isfinite(x) and 0 < x < 10 for x in y_mx_B)
    print(f"  Check 2 (no Landau pole, Run B): {'PASS' if sane_B else 'FAIL'}")
    print(f"    y_mx_B = {[f'{x:.4f}' for x in y_mx_B]}")
    print()

    # Check 3: gauge couplings approach the SM-1-loop GUT range
    # (not exactly unified at 1-loop SM, but in the right ballpark)
    g1_mx, g2_mx, g3_mx = y_mx_B[I_G1], y_mx_B[I_G2], y_mx_B[I_G3]
    # Standard "no SM 1-loop unification" gives them in 0.4 - 0.6 range
    in_band = all(0.3 < g < 0.8 for g in [g1_mx, g2_mx, g3_mx])
    print(f"  Check 3 (gauge couplings near GUT-unification band):")
    print(f"    g_1(M_X), g_2(M_X), g_3(M_X) = {g1_mx:.4f}, {g2_mx:.4f}, {g3_mx:.4f}")
    print(f"    all in (0.3, 0.8) ?  {'YES (PASS)' if in_band else 'NO (FAIL)'}")
    print()

    print("=" * 72)
    print("F15 SUMMARY")
    print("=" * 72)
    print(f"  Anchor (Tier-A, M_Z):  y_t(M_Z) = {Y_T_MZ:.4f}  (PDG match @ 0.75%)")
    print(f"  Run UPWARD to M_X:     y_t(M_X) = {yt_mx_B:.4f}  (Run B, GUT-norm)")
    print(f"  Closest substrate:     {best_name}")
    print(f"  Substrate gap:         {best_gap:.2f}%")
    print(f"  Verdict:               {verdict}")
    print()

    return 0 if (ok_F8 and sane_B and in_band) else 1


if __name__ == "__main__":
    raise SystemExit(main())
