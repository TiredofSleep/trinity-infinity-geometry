"""
Baseline test: compute Catalan's constant G = beta(2) via convergent Dirichlet series.

This is the framework's most basic computational sanity check:
- The Dirichlet beta function beta(s) = sum_{n=0}^inf (-1)^n / (2n+1)^s converges for Re(s) > 0
- At s=2, this equals Catalan's constant G = 0.9159655941772190150546...
- We compute this directly from the series and check against the known value

No fabrication possible: this is straightforward floating-point arithmetic
on a convergent series. If this test fails, something is fundamentally broken.
"""

import math
from typing import Tuple


CATALAN_KNOWN = 0.9159655941772190150546  # OEIS A006752, more than enough digits


def dirichlet_beta(s: float, max_terms: int = 100_000) -> float:
    """
    Compute beta(s) = sum_{n=0}^inf (-1)^n / (2n+1)^s by direct summation.

    Convergence is fast for s >= 2 (each term ~ 1/n^s).
    """
    if s <= 0:
        raise ValueError(f"beta(s) requires Re(s) > 0; got s={s}")

    total = 0.0
    for n in range(max_terms):
        term = ((-1) ** n) / ((2 * n + 1) ** s)
        total += term
        # convergence check for s >= 2
        if abs(term) < 1e-15 and n > 100:
            break
    return total


def catalan_constant(max_terms: int = 1_000_000) -> float:
    """Catalan's constant G = beta(2) via direct summation. Slow but reliable."""
    return dirichlet_beta(2.0, max_terms=max_terms)


def verify_catalan(tolerance: float = 1e-6) -> Tuple[bool, float, float, float]:
    """
    Compute G = beta(2) and verify it matches the known value.

    Returns:
        (passed, computed, known, error)
    """
    computed = catalan_constant(max_terms=1_000_000)
    error = abs(computed - CATALAN_KNOWN)
    passed = error < tolerance
    return passed, computed, CATALAN_KNOWN, error


if __name__ == "__main__":
    print("Catalan constant baseline test")
    print("-" * 50)
    passed, computed, known, error = verify_catalan()
    print(f"  Computed G = beta(2): {computed:.12f}")
    print(f"  Known value:           {known:.12f}")
    print(f"  Absolute error:        {error:.2e}")
    print(f"  Status: {'PASS' if passed else 'FAIL'}")
