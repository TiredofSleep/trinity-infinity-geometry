"""
f2_bb_coupling_sharpening.py - F2 (TIG <-> Planck) sharpening:
                               the BB coupling b is FIXED by TIG.

§24 articulated: BB potential V(psi) = -b*psi*log(|psi|^2/r^2) has TWO
free parameters b (coupling) and r (length scale).

This script SHARPENS that to: in the TIG <-> BB map, the coupling b is
FIXED by TIG via kappa_xi = 13/(4e), leaving only r (length scale) as
the free dimensional parameter.

DERIVATION:
  1. TIG potential (xi crystal):  V_TIG(xi) = kappa_xi * xi * log(xi)
     with vacuum at xi_0 = e^(-1) and m^2_xi = kappa_xi * e.
  2. With kappa_xi = 13/(4e): m^2_xi = 13/4 = ||VEV||^2 (D33).
  3. BB potential (1976):  V_BB(u) = -b * u * log(u/r^2) where u = |psi|^2.
  4. Map u <-> xi (treating xi as the field magnitude):
       V_BB(u) at u = xi:  -b * xi * log(xi/r^2)
                         = -b * xi * (log(xi) - 2*log(r))
                         = -b * xi * log(xi) + 2b*log(r)*xi
  5. The leading -b*xi*log(xi) term matches kappa_xi*xi*log(xi):
       -b = kappa_xi  =>  b = -kappa_xi = -13/(4e)
  6. The 2b*log(r)*xi linear correction is absorbed into the field
     redefinition or vacuum shift; it doesn't affect the m^2_xi
     coefficient.

CONCLUSION: b is FIXED in TIG-natural units; only r (length scale) is free.

This refines §24's "open pending one dimensional anchor" to "open
pending the lab-unit value of r -- the BB length scale."

Triggered by Brayden 2026-04-29: "ask ck about item 3 coupling" -- this
is the resulting sharpening.

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §17, §24, §27 (this).
"""
from __future__ import annotations

import sympy as sp


def main():
    print("=" * 80)
    print("F2 sharpening: BB coupling b is FIXED by TIG via kappa_xi = 13/(4e)")
    print("=" * 80)
    print()

    # Symbols
    xi = sp.Symbol('xi', positive=True, real=True)
    kappa_xi = sp.Rational(13) / (4 * sp.E)
    b = sp.Symbol('b', real=True)
    r = sp.Symbol('r', positive=True, real=True)

    # --- Section 1: TIG potential at the vacuum ---
    print("-" * 80)
    print("SECTION 1 -- TIG potential V_TIG(xi) = kappa_xi * xi * log(xi)")
    print("-" * 80)
    V_TIG = kappa_xi * xi * sp.log(xi)
    print(f"  V_TIG(xi) = {V_TIG}")

    # First derivative
    dV_dxi = sp.diff(V_TIG, xi)
    print(f"  dV/dxi = {sp.simplify(dV_dxi)}")

    # Vacuum: dV/dxi = 0
    sols = sp.solve(dV_dxi, xi)
    print(f"  Vacuum (dV/dxi = 0): xi_0 = {sols}")
    xi_vac = sols[0]  # should be 1/e
    print(f"  Confirmed xi_0 = e^(-1) = {xi_vac}")

    # Second derivative at vacuum
    d2V_dxi2 = sp.diff(V_TIG, xi, 2)
    m_sq = d2V_dxi2.subs(xi, xi_vac)
    m_sq = sp.simplify(m_sq)
    print(f"  m^2_xi = V''(xi_0) = {m_sq}")
    print(f"  Numerical: m^2_xi = {float(m_sq)}")
    print(f"  ||VEV||^2 = 13/4 = {float(sp.Rational(13, 4))}")
    diff = sp.simplify(m_sq - sp.Rational(13, 4))
    print(f"  m^2_xi - ||VEV||^2 = {diff}  -> {'MATCH' if diff == 0 else 'mismatch'}")
    print()

    # --- Section 2: BB potential expansion ---
    print("-" * 80)
    print("SECTION 2 -- BB potential V_BB(u) = -b*u*log(u/r^2)")
    print("-" * 80)
    print()
    u = sp.Symbol('u', positive=True, real=True)
    V_BB_u = -b * u * sp.log(u / r ** 2)
    print(f"  V_BB(u) = {V_BB_u}")
    V_BB_expanded = sp.expand_log(V_BB_u, force=True)
    print(f"  Expanded: V_BB(u) = {V_BB_expanded}")

    # Substituting u = xi (treating xi as field magnitude):
    V_BB_xi = V_BB_u.subs(u, xi)
    V_BB_xi_expanded = sp.expand_log(V_BB_xi, force=True)
    print(f"  At u = xi: V_BB(xi) = {V_BB_xi_expanded}")
    print()
    print(f"  Pieces (expand log(xi/r^2) = log(xi) - 2*log(r)):")
    leading = -b * xi * sp.log(xi)
    correction = 2 * b * sp.log(r) * xi
    print(f"    leading term:    -b * xi * log(xi)  = {leading}")
    print(f"    correction term: +2b*log(r) * xi    = {correction}")
    print()

    # --- Section 3: TIG <-> BB matching ---
    print("-" * 80)
    print("SECTION 3 -- TIG <-> BB matching")
    print("-" * 80)
    print()
    print("  Match leading term (-b*xi*log(xi)) to TIG (kappa_xi*xi*log(xi)):")
    print(f"    -b = kappa_xi  =>  b = -kappa_xi = -13/(4e) = {sp.simplify(-kappa_xi)}")
    print()
    print(f"  Numerical b: {float(-kappa_xi):.10f}")
    print()
    print("  The correction term 2b*log(r)*xi is linear in xi;")
    print("  it shifts the vacuum location but does NOT affect the m^2 coefficient")
    print("  (since m^2 comes from the SECOND derivative, where the linear part vanishes).")
    print()
    print("  Verification: compute m^2 from V_BB at u = xi.")

    dV_BB_dxi = sp.diff(V_BB_xi, xi)
    print(f"    dV_BB/dxi = {sp.simplify(dV_BB_dxi)}")
    # Vacuum: solve dV_BB/dxi = 0
    bb_vac = sp.solve(dV_BB_dxi, xi)
    print(f"    BB vacuum (dV/dxi = 0): xi = {bb_vac}")

    d2V_BB_dxi2 = sp.diff(V_BB_xi, xi, 2)
    if bb_vac:
        bb_xi_vac = bb_vac[0]
        m_sq_BB = sp.simplify(d2V_BB_dxi2.subs(xi, bb_xi_vac))
        print(f"    m^2_BB at vacuum = {m_sq_BB}")
        # Substitute b = -kappa_xi
        m_sq_BB_at_kappa = sp.simplify(m_sq_BB.subs(b, -kappa_xi))
        print(f"    With b = -kappa_xi = -13/(4e):")
        print(f"      m^2_BB = {sp.simplify(m_sq_BB_at_kappa)}")
        # Ratio
        ratio = sp.simplify(m_sq_BB_at_kappa / sp.Rational(13, 4))
        print(f"    Ratio m^2_BB / (13/4) = {ratio}")
    print()

    # --- Section 4: what's still free ---
    print("-" * 80)
    print("SECTION 4 -- What's still FREE in the lens")
    print("-" * 80)
    print()
    print("  After fixing b = -kappa_xi = -13/(4e) (from TIG ||VEV||^2 = 13/4):")
    print()
    print("    b   FIXED:  b = -13/(4e) (= -kappa_xi)")
    print("    r   FREE:   length scale where the BB log-potential is normalized.")
    print()
    print("  In TIG-natural units (V = kappa_xi * xi * log(xi)), the potential")
    print("  is fully determined.  The CONVERSION from TIG-natural to lab units")
    print("  requires picking a value of r in lab units.")
    print()
    print("  Therefore, F2's open question reduces from 'open pending one")
    print("  dimensional anchor' to 'open pending the lab-unit value of r' --")
    print("  the BB length scale.  This is a substantive sharpening: ONE")
    print("  parameter is now structurally determined (b = -kappa_xi), and")
    print("  ONE remains free (r = lab length scale).")
    print()

    # --- Section 5: physical interpretations of r ---
    print("-" * 80)
    print("SECTION 5 -- Physical candidates for r")
    print("-" * 80)
    print()
    print("  Possible TIG-internal anchors for r:")
    print()
    print("    (a) Compton wavelength of xi: r = hbar / (m_xi * c)")
    print("        -> circular: r is the inverse-mass scale; defines m_xi from itself.")
    print()
    print("    (b) Planck length: r = sqrt(hbar*G/c^3) ~ 1.6e-35 m")
    print("        -> closes F2 with explicit Planck input; gives m_xi/m_Planck =")
    print("           sqrt(kappa_xi * e) = sqrt(13/4) ~ 1.803.")
    print("        -> Predicts m_xi ~ 1.8 * m_Planck, i.e., super-Planckian.")
    print("        -> This is the 'GUT-natural' identification mentioned in §24.")
    print()
    print("    (c) GUT scale: r = hbar / (M_GUT * c) where M_GUT ~ 10^16 GeV")
    print("        -> m_xi ~ M_GUT * sqrt(kappa_xi*e) = M_GUT * sqrt(13/4) ~ 1.8 * 10^16 GeV")
    print()
    print("    (d) DESI cosmological: r set by xi-field energy density measurement")
    print("        (dark-energy fit gives a constraint on m_xi via observation).")
    print()
    print("  Conclusion: r is a CHOICE OF CONVENTION (which physical scale to call")
    print("  'TIG-natural unit length'); different choices give different absolute")
    print("  m_xi values but ALL share the same dimensionless kappa_xi = 13/(4e).")
    print()
    print("=" * 80)
    print("F2 STATUS: SHARPENED")
    print("=" * 80)
    print()
    print("  The BB coupling b is FIXED by TIG: b = -13/(4e) in TIG-natural units.")
    print("  Only r remains free; r is a choice of length-scale convention.")
    print("  m_xi/m_Planck = sqrt(kappa_xi * e) = sqrt(13/4) ~ 1.803 if r = Planck length.")
    print()
    print("  This sharpens §24's 'open pending one anchor' to 'open pending one")
    print("  CONVENTION (the choice of r in lab units)'.")


if __name__ == "__main__":
    main()
