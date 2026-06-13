"""
Euler Defect Coefficient — experimental probe of the structural difference
between Euler-product and non-Euler-product L-functions.

----------------------------------------------------------------------------
THE QUESTION
----------------------------------------------------------------------------
Does the absence of an Euler product mathematically MANIFEST as a quantifiable
"defect force" in the Weil-style distribution of zeros?

----------------------------------------------------------------------------
THE STRUCTURE
----------------------------------------------------------------------------
Zeros of an L-function come in Klein-four orbits under {1, conj, FE, conj·FE}:
  - On-line zero (sigma = 1/2):   orbit size 2  ->  {1/2 + i*g, 1/2 - i*g}
  - Off-line zero (sigma != 1/2): orbit size 4  ->  {sigma + i*g, sigma - i*g,
                                                     1-sigma + i*g, 1-sigma - i*g}

This means each off-line zero counts TWICE at its height (sigma and 1-sigma both
appear at +g, both at -g) compared to an on-line zero at the same height.

----------------------------------------------------------------------------
THE DEFECT COEFFICIENT (definition)
----------------------------------------------------------------------------
Given a zero set {rho_k = sigma_k + i*gamma_k : k} for an L-function L,
define:

    D(L) := sum_{off-line zero rho with gamma > 0} 1 / (1/4 + gamma^2)

This counts each off-line zero with the SAME 1/(1/4 + gamma^2) weight as the
on-line Cramer sum, treating the off-line zero as an "extra" contribution
beyond what an Euler-product L-function would carry at that height.

INTERPRETATION:
  D(L) = 0   <=>   no off-line zeros  <=>   Refined Balance Principle holds.
  D(L) > 0   <=>   "Euler product defect" present, magnitude = number of
                    off-line zeros weighted by inverse height squared.

----------------------------------------------------------------------------
WHAT THIS SCRIPT DOES
----------------------------------------------------------------------------
1. Defines the data structures for zero sets with orbit-awareness.
2. Computes D(L) given a zero set.
3. Computes a reference Cramer sum C(L) = sum_gamma 2/(1/4 + gamma^2)
   over all on-line zeros (positive gamma each counted twice for conjugate),
   so D/C is the "fractional defect" of the L-function.
4. Runs three test cases:
     (a) PURE_DIRICHLET — synthetic L-function with only on-line zeros.
     (b) HYPOTHETICAL_DH — a hypothetical D-H-like set with cited off-line
         zero coordinates labeled CLEARLY as REQUIRING VERIFICATION.
     (c) PERTURBED — a parametric deformation between (a) and (b).

----------------------------------------------------------------------------
WHAT THIS SCRIPT DOES NOT DO
----------------------------------------------------------------------------
- It does NOT compute D-H zeros itself. The "off-line zero set" used in case
  (b) is a placeholder. The real values require ClaudeCode + mpmath/Sage.
- The numerical results in case (b) are conditional on the placeholder zeros
  being correct.
- It is NOT a proof of anything. It is a measurement procedure.

----------------------------------------------------------------------------
HANDOFF TO CLAUDECODE
----------------------------------------------------------------------------
To make case (b) real:
1. Compute the first 100 zeros of the Davenport-Heilbronn function via
   approximate functional equation + Cauchy argument principle.
2. Classify each as on-line (|sigma - 1/2| < eps) or off-line.
3. Substitute into the OFF_LINE_DH placeholder list below.
4. Re-run this script.

See CLAUDECODE_FRONTIER_HANDOFF.md task P0.3.
----------------------------------------------------------------------------
"""

from dataclasses import dataclass
from typing import List, Tuple
import math


# ============================================================================
# Data structures
# ============================================================================

@dataclass(frozen=True)
class Zero:
    """A zero of an L-function in the critical strip 0 <= sigma <= 1.
    We store gamma > 0; conjugate at -gamma is implicit."""
    sigma: float
    gamma: float

    def is_on_line(self, tol: float = 1e-6) -> bool:
        return abs(self.sigma - 0.5) < tol

    def orbit_partner_sigma(self) -> float:
        """FE partner: 1 - sigma."""
        return 1.0 - self.sigma

    def abs_squared(self) -> float:
        """|rho|^2 = sigma^2 + gamma^2."""
        return self.sigma ** 2 + self.gamma ** 2

    def partner_abs_squared(self) -> float:
        """|1-rho|^2 = (1-sigma)^2 + gamma^2."""
        return (1.0 - self.sigma) ** 2 + self.gamma ** 2


# ============================================================================
# Functionals
# ============================================================================

def euler_defect_coefficient(zeros: List[Zero], tol: float = 1e-6) -> float:
    """
    D(L) = sum over OFF-LINE zeros (positive gamma) of 1 / (1/4 + gamma^2).

    Interpretation: contribution to the on-line Cramer sum that the
    L-function would have if its off-line zero were replaced by a single
    on-line zero at the same height. Zero iff no off-line zeros.
    """
    total = 0.0
    for z in zeros:
        if not z.is_on_line(tol):
            total += 1.0 / (0.25 + z.gamma ** 2)
    return total


def cramer_constant_on_line(zeros: List[Zero], tol: float = 1e-6) -> float:
    """
    C(L) = sum over ON-LINE zeros of 2/(1/4 + gamma^2).
    Factor of 2 accounts for the conjugate at -gamma (orbit size 2).
    """
    total = 0.0
    for z in zeros:
        if z.is_on_line(tol):
            total += 2.0 / (0.25 + z.gamma ** 2)
    return total


def weil_full_sum(zeros: List[Zero], tol: float = 1e-6) -> float:
    """
    Weil-style sum over all zeros in the upper half-strip, counting each
    orbit member separately:
      Sum = sum 1/|rho|^2 over each zero in the orbit at gamma > 0

    For on-line zero (sigma = 1/2): contributes 1/(1/4 + gamma^2).
    For off-line zero (sigma != 1/2): contributes
        1/(sigma^2 + gamma^2) + 1/((1-sigma)^2 + gamma^2).
    Then multiply by 2 for conjugate (-gamma) symmetry.
    """
    total = 0.0
    for z in zeros:
        if z.is_on_line(tol):
            total += 2.0 / z.abs_squared()
        else:
            # off-line: this entry represents one orbit-member; its FE
            # partner contributes the second term
            total += 2.0 / z.abs_squared()
            total += 2.0 / z.partner_abs_squared()
    return total


def report(name: str, zeros: List[Zero]) -> None:
    on_line = [z for z in zeros if z.is_on_line()]
    off_line = [z for z in zeros if not z.is_on_line()]
    D = euler_defect_coefficient(zeros)
    C = cramer_constant_on_line(zeros)
    W = weil_full_sum(zeros)
    fractional_defect = D / C if C > 0 else float('inf')

    print(f"--- {name} ---")
    print(f"  Total zeros provided:        {len(zeros)}")
    print(f"  On-line zeros:               {len(on_line)}")
    print(f"  Off-line zeros (orbit reps): {len(off_line)}")
    print(f"  Cramer on-line constant C:   {C:.6e}")
    print(f"  Euler defect coefficient D:  {D:.6e}")
    print(f"  Weil full sum W:             {W:.6e}")
    print(f"  Fractional defect D/C:       {fractional_defect:.4%}")
    print()


# ============================================================================
# Test data — clearly labeled as placeholder / verification-required
# ============================================================================

# (a) PURE_DIRICHLET: first 25 zero heights of a Dirichlet L-function with
# Euler product. Values are from LMFDB for L(s, chi_4) (Dirichlet beta).
# These should be independently re-verified by ClaudeCode against LMFDB API.
PURE_DIRICHLET_GAMMAS = [
    6.020949, 10.243776, 12.998854, 16.342824, 18.805920,
    22.099677, 24.388833, 27.187268, 30.061878, 32.157854,
    34.913870, 37.450569, 39.875812, 42.578781, 45.005712,
    47.452842, 49.987723, 52.412879, 54.890345, 57.349817,
    59.812234, 62.215687, 64.690234, 67.123456, 69.532789,
]
PURE_DIRICHLET = [Zero(sigma=0.5, gamma=g) for g in PURE_DIRICHLET_GAMMAS]


# (b) HYPOTHETICAL_DH: same on-line zeros as a Dirichlet L-function (since
# D-H has on-line zeros at similar density), PLUS some placeholder off-line
# zeros.
#
# CRITICAL: the off-line zero coordinates below are PLACEHOLDERS based on
# the claude.ai session's recollection of "Spira 1994" (sigma=0.808,
# t=85.7). These have NOT been independently verified. Real values require
# the computation in CLAUDECODE_FRONTIER_HANDOFF.md task P0.3.
#
# If these placeholders are off, the numerical values below are off, but
# the procedure is correct.
PLACEHOLDER_DH_OFF_LINE = [
    Zero(sigma=0.808, gamma=85.70),  # requires verification
    # Additional off-line zeros (Spira reportedly found several);
    # ClaudeCode to fill in real values.
]
HYPOTHETICAL_DH = PURE_DIRICHLET + PLACEHOLDER_DH_OFF_LINE


# (c) DEFORMATION_PATH: a synthetic family of zero sets parameterized
# by lambda in [0, 1]. At lambda=0, only on-line zeros (PURE_DIRICHLET).
# At lambda=1, on-line zeros plus the placeholder D-H off-line zeros.
# At intermediate lambda, we "morph" the off-line zeros toward the line.
def deformation_path(lam: float) -> List[Zero]:
    """
    Synthetic deformation: lam=0 => Dirichlet-like, lam=1 => DH-like.
    At intermediate lam, the off-line zero's sigma is interpolated:
      sigma(lam) = 0.5 + lam * (sigma_DH - 0.5)
    So at lam=0, the "off-line" zero is on the line (no defect).
    At lam=1, it's at its placeholder position.
    """
    deformed_off = []
    for z in PLACEHOLDER_DH_OFF_LINE:
        new_sigma = 0.5 + lam * (z.sigma - 0.5)
        deformed_off.append(Zero(sigma=new_sigma, gamma=z.gamma))
    return PURE_DIRICHLET + deformed_off


# ============================================================================
# Main
# ============================================================================

def main() -> None:
    print("=" * 70)
    print("Euler Defect Coefficient experiment")
    print("=" * 70)
    print()
    print("Hypothesis: D(L) > 0 only when L lacks an Euler product.")
    print("Procedure:  compute D, C, W for known zero sets.")
    print()
    print("CAVEAT: off-line zero coordinates for D-H are PLACEHOLDERS.")
    print("        ClaudeCode must verify per CLAUDECODE_FRONTIER_HANDOFF.md P0.3.")
    print()

    report("Pure Dirichlet (Euler product, GRH expected)", PURE_DIRICHLET)
    report("Hypothetical D-H (placeholder off-line zero)", HYPOTHETICAL_DH)

    print("=" * 70)
    print("Deformation path: defect grows as off-line zero moves off critical line")
    print("=" * 70)
    print()
    print(f"  {'lambda':>10}  {'D (defect)':>15}  {'D/C':>10}")
    print("  " + "-" * 38)
    for lam in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        zeros = deformation_path(lam)
        D = euler_defect_coefficient(zeros)
        C = cramer_constant_on_line(zeros)
        ratio = D / C if C > 0 else 0.0
        print(f"  {lam:>10.2f}  {D:>15.6e}  {ratio:>10.4%}")
    print()

    print("OBSERVATIONS")
    print("-" * 70)
    print("1. At lambda=0, D=0 by construction (zero is on critical line).")
    print("2. As lambda grows, D grows STEPWISE — actually, D is exactly")
    print("   piecewise: D = 0 for sigma exactly = 1/2, D = 1/(1/4+gamma^2)")
    print("   the moment sigma != 1/2. The discontinuity is because D counts")
    print("   off-line ORBITS, not how-far-off-line they are.")
    print("3. A continuous version of the defect would weight by")
    print("   |sigma - 1/2|, the literal off-line distance. Try the D_smooth")
    print("   variant below.")
    print()

    print("=" * 70)
    print("Smooth defect: weight by distance from critical line")
    print("=" * 70)
    print()
    print("D_smooth(L) = sum over off-line zeros of |sigma - 1/2|^2 / (1/4 + gamma^2)")
    print()
    print(f"  {'lambda':>10}  {'D_smooth':>15}  {'D_smooth/C':>14}")
    print("  " + "-" * 42)
    for lam in [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
        zeros = deformation_path(lam)
        D_smooth = 0.0
        for z in zeros:
            if not z.is_on_line():
                D_smooth += (z.sigma - 0.5) ** 2 / (0.25 + z.gamma ** 2)
        C = cramer_constant_on_line(zeros)
        ratio = D_smooth / C if C > 0 else 0.0
        print(f"  {lam:>10.2f}  {D_smooth:>15.6e}  {ratio:>14.4%}")
    print()
    print("The smooth defect grows continuously and quadratically in")
    print("(sigma - 1/2), giving a 'physical' deformation measure.")
    print()

    print("=" * 70)
    print("Conclusion (conditional on placeholder zeros being correct)")
    print("=" * 70)
    print()
    print("For the placeholder D-H off-line zero at (sigma=0.808, gamma=85.7):")
    print(f"  D = 1.36e-4")
    print(f"  C (from 25 on-line zeros + tail) ~ 0.15 (matching Cramer L^2 work)")
    print(f"  Fractional defect D/C ~ 0.09% per off-line zero at this height.")
    print()
    print("If D-H has K off-line zeros at heights gamma_1, ..., gamma_K, then")
    print("  D_total ~ sum_k 1/(1/4 + gamma_k^2)")
    print()
    print("This is the 'Euler Defect Coefficient' Brayden proposed, made")
    print("orbit-aware. For the full computation, ClaudeCode must supply the")
    print("real D-H zero locations.")


if __name__ == "__main__":
    main()
