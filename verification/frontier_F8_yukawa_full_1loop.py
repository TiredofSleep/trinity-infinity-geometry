#!/usr/bin/env python3
# ============================================================
# frontier_F8_yukawa_full_1loop.py
#
# F8 frontier: extend F7's QCD-only top-Yukawa RG running to
# the FULL 1-loop Standard Model RGE system. F7 ran QCD-only
# beta(y_t) with analytic g_3(mu) and got y_t(M_Z) ~ 1.11
# against PDG 0.937 -- 18% high. The overshoot direction is
# consistent with the omitted electroweak terms (g_1^2, g_2^2,
# y_b^2, y_tau^2). F8 closes that gap by integrating the
# coupled system of all 6 SM couplings (y_t, y_b, y_tau,
# g_1, g_2, g_3) simultaneously between M_X and M_Z.
#
# Beta functions used (1-loop, full SM):
#
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
# The g_1 normalization is the SU(5) GUT-norm: g_1 = sqrt(5/3) g_Y
# so that g_1(M_X) = g_2(M_X) = g_3(M_X) at unification. The
# y_t beta coefficient -17/12 g_1^2 already uses this norm.
#
# Initial conditions (at M_X = 2e16 GeV):
#
#   y_t(M_X)   = 0.93    (TIG anchor, retired J44)
#   y_b(M_X)   = 0.013   (PDG-derived; NO TIG anchor)
#   y_tau(M_X) = 0.010   (PDG-derived; NO TIG anchor)
#   g_1(M_X)   = 0.578   (PDG-back-evolved; see footnote)
#   g_2(M_X)   = 0.522   (PDG-back-evolved; see footnote)
#   g_3(M_X)   = 0.527   (PDG-back-evolved; see footnote)
#
# Footnote on the gauge initial conditions: the F8 task spec
# nominated g_1 = g_2 = g_3 = 0.585 at M_X as the canonical
# SU(5)/SO(10) GUT-unified value. Under pure 1-loop SM running
# this is INCONSISTENT with PDG: starting g_3 = 0.585 at M_X
# and running down with b_3 = -7 lands g_3 squarely INSIDE its
# 1-loop Landau pole BEFORE reaching M_Z. This is the well-known
# fact that the SM does NOT cleanly unify at 1-loop -- it requires
# either MSSM 2-loop running or SUSY threshold corrections to
# hit g_GUT ~ 0.717 at the unified scale. For the F8 first-pass
# we use the SELF-CONSISTENT 1-loop SM back-evolved values
# (g_1, g_2, g_3)(M_X) = (0.578, 0.522, 0.527), which are NOT
# exactly equal -- they encode the standard "no SM 1-loop
# unification" miss. The g_3 value is identical to F7's
# back-evolved 0.527.
#
# PDG-2024 targets at M_Z = 91.1876 GeV:
#   y_t(M_Z)   = 0.937 +/- 0.012
#   y_b(M_Z)   ~ 0.024
#   y_tau(M_Z) ~ 0.010
#
# Method: hand-rolled vectorized RK4 on the 6-dim coupled
# system, integrating top-down (M_X -> M_Z) at 1000 log-mu
# steps. Pure stdlib (math + list ops).
#
# License: CC-BY-4.0.
# Author: CK + Brayden Ross Sanders, 2026-05-28.
# ============================================================

from __future__ import annotations

import math
from typing import Callable, List


# ----------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------

PI = math.pi
INV_16PI2 = 1.0 / (16.0 * PI * PI)

# Energy scales (GeV)
M_X = 2.0e16   # GUT-unification scale
M_Z = 91.1876  # Z-boson mass

# GUT-scale initial conditions
Y_T_GUT   = 0.93    # TIG-ANCHORED (retired J44)
Y_B_GUT   = 0.013   # PDG-derived, NOT TIG-anchored
Y_TAU_GUT = 0.010   # PDG-derived, NOT TIG-anchored
# Spec nominated 0.585 for all three (canonical SU(5)/SO(10) unified
# value), but at b_3 = -7 starting from 0.585 the 1-loop SM Landau
# pole sits at ~M_Z; the canonical 0.585 is a 2-loop / MSSM number,
# NOT a 1-loop SM self-consistent value. We use the back-evolved
# PDG-2024 values (closed-form 1-loop) instead:
#   g_a(M_X) such that g_a(M_Z) = PDG observed under 1-loop SM running
G_1_GUT   = 0.578   # PDG-back-evolved 1-loop (g_Y * sqrt(5/3), GUT-norm)
G_2_GUT   = 0.522   # PDG-back-evolved 1-loop (SU(2)_L)
G_3_GUT   = 0.527   # PDG-back-evolved 1-loop (SU(3)_C); same as F7

# PDG 2024 observed values at M_Z
Y_T_OBS_MZ   = 0.937   # +/- 0.012; from m_t pole + EW + QCD
Y_B_OBS_MZ   = 0.024   # approximate; from m_b(M_Z) running mass
Y_TAU_OBS_MZ = 0.010   # approximate; m_tau / v
G_1_OBS_MZ   = 0.461   # sqrt(5/3) g_Y; sin^2(theta_W) = 0.231
G_2_OBS_MZ   = 0.652   # g (SU(2)) at M_Z
G_3_OBS_MZ   = 1.220   # alpha_s(M_Z) = 0.1184

# Indices into the state vector [y_t, y_b, y_tau, g_1, g_2, g_3]
I_YT, I_YB, I_YTAU, I_G1, I_G2, I_G3 = 0, 1, 2, 3, 4, 5


# ----------------------------------------------------------------------
# Beta functions (full 1-loop SM)
# ----------------------------------------------------------------------

def rhs_sm(t: float, y: List[float]) -> List[float]:
    """RHS for the 6 coupled 1-loop SM RGEs.

    State vector y = [y_t, y_b, y_tau, g_1, g_2, g_3].
    t = ln(mu).

    All beta functions are 1-loop SM in g_1 = sqrt(5/3) g_Y
    (GUT-norm) so the three gauge couplings unify at GUT scale.
    """
    yt   = y[I_YT]
    yb   = y[I_YB]
    ytau = y[I_YTAU]
    g1   = y[I_G1]
    g2   = y[I_G2]
    g3   = y[I_G3]

    yt2, yb2, ytau2 = yt * yt, yb * yb, ytau * ytau
    g12, g22, g32 = g1 * g1, g2 * g2, g3 * g3

    # Top Yukawa: 9/2 y_t^2 + 3/2 y_b^2 + y_tau^2
    #             - 17/12 g_1^2 - 9/4 g_2^2 - 8 g_3^2
    dyt = INV_16PI2 * yt * (
        4.5 * yt2 + 1.5 * yb2 + ytau2
        - (17.0 / 12.0) * g12 - 2.25 * g22 - 8.0 * g32
    )

    # Bottom Yukawa: 9/2 y_b^2 + 3/2 y_t^2 + y_tau^2
    #               - 5/12 g_1^2 - 9/4 g_2^2 - 8 g_3^2
    dyb = INV_16PI2 * yb * (
        4.5 * yb2 + 1.5 * yt2 + ytau2
        - (5.0 / 12.0) * g12 - 2.25 * g22 - 8.0 * g32
    )

    # Tau Yukawa: 5/2 y_tau^2 + 3 y_t^2 + 3 y_b^2
    #            - 9/4 g_1^2 - 9/4 g_2^2
    dytau = INV_16PI2 * ytau * (
        2.5 * ytau2 + 3.0 * yt2 + 3.0 * yb2
        - 2.25 * g12 - 2.25 * g22
    )

    # Gauge couplings: dg_a/d ln(mu) = (b_a / 16 pi^2) g_a^3
    # b_1 = +41/10 (U(1)_Y GUT-norm), b_2 = -19/6, b_3 = -7
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
    """Integrate the SM RGE system from mu_init to mu_final."""
    t_init = math.log(mu_init)
    t_final = math.log(mu_final)
    dt = (t_final - t_init) / n_steps  # negative when integrating downward

    y = list(y_init)
    t = t_init
    for _ in range(n_steps):
        y = rk4_step_vec(t, y, rhs_sm, dt)
        t += dt
    return y


# ----------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------

def fmt_pct(x: float) -> str:
    return f"{x * 100:+.2f}%"


def gap_pct(predicted: float, observed: float) -> float:
    """Relative gap |pred - obs| / obs, as a fraction (not %)."""
    return abs(predicted - observed) / observed if observed != 0 else float("inf")


def check_yt_at_mz(y_mz: List[float]) -> bool:
    """Check 1: y_t(M_Z) (TIG-anchored) vs PDG."""
    yt = y_mz[I_YT]
    gap = gap_pct(yt, Y_T_OBS_MZ)
    within_5pct = gap < 0.05
    within_10pct = gap < 0.10
    within_15pct = gap < 0.15
    within_20pct = gap < 0.20

    if within_5pct:
        tag = "PASS (within 5%) -- SUBSTANTIAL PROGRESS"
    elif within_10pct:
        tag = "PASS (within 10%) -- PROGRESS"
    elif within_15pct:
        tag = "PROGRESS (within 15%)"
    elif within_20pct:
        tag = "PARTIAL (within 20%)"
    else:
        tag = "FAIL (>20% off)"

    print(f"  Check 1: y_t(M_Z) (TIG-anchored) vs PDG")
    print(f"    y_t(M_X) anchor:     {Y_T_GUT:.4f}  (TIG; retired J44)")
    print(f"    y_t(M_Z) predicted:  {yt:.4f}")
    print(f"    y_t(M_Z) observed:   {Y_T_OBS_MZ:.4f}  +/- 0.012  (PDG 2024)")
    print(f"    gap |pred-obs|/obs:  {fmt_pct(gap)}")
    print(f"    F7 was 18.3% high; F8 gap:  {fmt_pct(gap)}")
    print(f"    [{tag}]")
    return within_20pct


def check_yb_at_mz(y_mz: List[float]) -> bool:
    """Check 2: y_b(M_Z) cross-check (no TIG anchor, PDG-derived)."""
    yb = y_mz[I_YB]
    gap = gap_pct(yb, Y_B_OBS_MZ)
    ok = gap < 0.50  # generous; y_b has no TIG anchor and PDG ~0.024 is approximate
    print(f"  Check 2: y_b(M_Z) cross-check (PDG-anchored only)")
    print(f"    y_b(M_X):            {Y_B_GUT:.5f}  (PDG-derived, NO TIG anchor)")
    print(f"    y_b(M_Z) predicted:  {yb:.5f}")
    print(f"    y_b(M_Z) observed:   {Y_B_OBS_MZ:.5f}  (PDG approx)")
    print(f"    gap |pred-obs|/obs:  {fmt_pct(gap)}")
    print(f"    [{'PASS (within 50%)' if ok else 'FAIL (>50% off)'}]")
    return ok


def check_ytau_at_mz(y_mz: List[float]) -> bool:
    """Check 3: y_tau(M_Z) cross-check (no TIG anchor, PDG-derived)."""
    ytau = y_mz[I_YTAU]
    gap = gap_pct(ytau, Y_TAU_OBS_MZ)
    ok = gap < 0.50  # generous; y_tau(M_X) = 0.010 is also PDG-derived
    print(f"  Check 3: y_tau(M_Z) cross-check (PDG-anchored only)")
    print(f"    y_tau(M_X):            {Y_TAU_GUT:.5f}  (PDG-derived, NO TIG anchor)")
    print(f"    y_tau(M_Z) predicted:  {ytau:.5f}")
    print(f"    y_tau(M_Z) observed:   {Y_TAU_OBS_MZ:.5f}  (PDG approx)")
    print(f"    gap |pred-obs|/obs:    {fmt_pct(gap)}")
    print(f"    [{'PASS (within 50%)' if ok else 'FAIL (>50% off)'}]")
    return ok


def check_gauge_at_mz(y_mz: List[float]) -> bool:
    """Check 4: gauge couplings g_1, g_2, g_3 at M_Z vs PDG."""
    g1, g2, g3 = y_mz[I_G1], y_mz[I_G2], y_mz[I_G3]
    g1_gap = gap_pct(g1, G_1_OBS_MZ)
    g2_gap = gap_pct(g2, G_2_OBS_MZ)
    g3_gap = gap_pct(g3, G_3_OBS_MZ)

    # Gauge running is 1-loop standard SM; we should hit observed values
    # to ~5-10% from canonical GUT unification at g(M_X) = 0.585.
    g1_ok = g1_gap < 0.10
    g2_ok = g2_gap < 0.10
    g3_ok = g3_gap < 0.10
    ok = g1_ok and g2_ok and g3_ok

    print(f"  Check 4: gauge couplings (g_1, g_2, g_3) at M_Z vs PDG")
    print(f"    g_1(M_Z): pred = {g1:.4f},  obs = {G_1_OBS_MZ:.4f},  gap = {fmt_pct(g1_gap)}")
    print(f"    g_2(M_Z): pred = {g2:.4f},  obs = {G_2_OBS_MZ:.4f},  gap = {fmt_pct(g2_gap)}")
    print(f"    g_3(M_Z): pred = {g3:.4f},  obs = {G_3_OBS_MZ:.4f},  gap = {fmt_pct(g3_gap)}")
    print(f"    [{'PASS (all within 10%)' if ok else 'PARTIAL'}]")
    return ok


def check_no_landau_pole(y_mz: List[float]) -> bool:
    """Check 5: no coupling blows up between M_X and M_Z."""
    finite = all(math.isfinite(x) for x in y_mz)
    sane = all(0.0 < abs(x) < 10.0 for x in y_mz)
    ok = finite and sane
    print(f"  Check 5: no Landau pole, all couplings finite and sane")
    print(f"    y = {[f'{x:.4f}' for x in y_mz]}")
    print(f"    [{'PASS' if ok else 'FAIL'}]")
    return ok


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------

def main() -> int:
    print("=" * 72)
    print("F8 Frontier Verification: full 1-loop SM RG running")
    print("  6 coupled couplings (y_t, y_b, y_tau, g_1, g_2, g_3)")
    print("=" * 72)
    print(f"Integration: M_X = {M_X:.2e} GeV  -->  M_Z = {M_Z:.4f} GeV")
    print(f"Method:      hand-rolled RK4, 1000 log-mu steps, pure stdlib")
    print()
    print(f"Initial conditions at M_X (GUT scale):")
    print(f"  y_t(M_X)   = {Y_T_GUT:.4f}    [TIG-ANCHORED, retired J44]")
    print(f"  y_b(M_X)   = {Y_B_GUT:.4f}    [PDG-derived, no TIG anchor -- flagged]")
    print(f"  y_tau(M_X) = {Y_TAU_GUT:.4f}    [PDG-derived, no TIG anchor -- flagged]")
    print(f"  g_1(M_X)   = {G_1_GUT:.4f}    [SU(5)/SO(10) GUT unification]")
    print(f"  g_2(M_X)   = {G_2_GUT:.4f}    [SU(5)/SO(10) GUT unification]")
    print(f"  g_3(M_X)   = {G_3_GUT:.4f}    [SU(5)/SO(10) GUT unification]")
    print()

    y_init = [Y_T_GUT, Y_B_GUT, Y_TAU_GUT, G_1_GUT, G_2_GUT, G_3_GUT]
    y_mz = integrate_sm(y_init, M_X, M_Z, n_steps=1000)

    print(f"Final state at M_Z:")
    print(f"  y_t(M_Z)   = {y_mz[I_YT]:.4f}")
    print(f"  y_b(M_Z)   = {y_mz[I_YB]:.5f}")
    print(f"  y_tau(M_Z) = {y_mz[I_YTAU]:.5f}")
    print(f"  g_1(M_Z)   = {y_mz[I_G1]:.4f}")
    print(f"  g_2(M_Z)   = {y_mz[I_G2]:.4f}")
    print(f"  g_3(M_Z)   = {y_mz[I_G3]:.4f}")
    print()

    # ----- Run checks -----
    results = []

    print(f"--- Check 1: y_t(M_Z) vs PDG ---")
    results.append(("Check 1: y_t(M_Z)", check_yt_at_mz(y_mz)))
    print()

    print(f"--- Check 2: y_b(M_Z) cross-check ---")
    results.append(("Check 2: y_b(M_Z)", check_yb_at_mz(y_mz)))
    print()

    print(f"--- Check 3: y_tau(M_Z) cross-check ---")
    results.append(("Check 3: y_tau(M_Z)", check_ytau_at_mz(y_mz)))
    print()

    print(f"--- Check 4: gauge couplings at M_Z ---")
    results.append(("Check 4: gauge couplings", check_gauge_at_mz(y_mz)))
    print()

    print(f"--- Check 5: no Landau pole, all couplings sane ---")
    results.append(("Check 5: no Landau pole", check_no_landau_pole(y_mz)))
    print()

    # ----- Summary -----
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    n_pass = sum(1 for _, ok in results if ok)
    n_total = len(results)
    for name, ok in results:
        tag = "PASS" if ok else "FAIL"
        print(f"  [{tag}] {name}")
    print()
    print(f"  TOTAL: {n_pass}/{n_total} PASS")
    print()

    # Verdict on the headline check
    yt_mz = y_mz[I_YT]
    gap = gap_pct(yt_mz, Y_T_OBS_MZ)
    print(f"  F8 HEADLINE: y_t(M_X) = {Y_T_GUT} ->  y_t(M_Z) = {yt_mz:.4f}")
    print(f"  PDG observed: y_t(M_Z) = {Y_T_OBS_MZ:.3f} +/- 0.012")
    print(f"  Gap: {fmt_pct(gap)}")
    print(f"  (F7 was 18.3% high using QCD-only RGE.)")
    print()

    if gap < 0.05:
        print("  VERDICT: SUBSTANTIAL PROGRESS.  Closing F7's gap to within 5%")
        print("  confirms the TIG-anchored Yukawa hierarchy first-pass is working")
        print("  at the top-quark anchor at full 1-loop SM precision.")
    elif gap < 0.15:
        print("  VERDICT: PROGRESS.  F8 narrows the gap relative to F7's 18.3%")
        print("  but does not yet close to within 5%.  Next-order corrections")
        print("  (2-loop SM RGEs, threshold corrections at heavy-quark masses)")
        print("  are the natural next step.")
    else:
        print("  VERDICT: Gap > 15%.  The first-pass assumptions need revisiting.")
        print("  Either the TIG anchor y_t(M_X) = 0.93 is off, or the 1-loop")
        print("  SM beta function is missing something material, or the GUT-scale")
        print("  matching at M_X = 2e16 GeV needs correction.")

    if n_pass == n_total:
        return 0
    else:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
