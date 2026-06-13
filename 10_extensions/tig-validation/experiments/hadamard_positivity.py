"""
hadamard_positivity.py — Hadamard-quantity profiler at a fixed sigma.

============================================================================
SCOPE OF THIS SCRIPT  (read before drawing any conclusions)
============================================================================

This script PROFILES the Hadamard quantity

    H_L(sigma, t) := 3 log|L(sigma)| + 4 log|L(sigma + it)| + log|L(sigma + 2it)|

for several L-functions along a single vertical line in the s-plane,
sigma = (user choice, default 1.05), as t varies over a user-defined interval.

What it does:
    - Evaluates the true Dirichlet series for zeta(s), L(s, chi_3),
      Davenport-Heilbronn f(s), and the products zeta*L(chi_3) and zeta*f.
    - At sigma = 1.05 the raw Dirichlet sum converges far too slowly to be
      useful directly, so we use the standard Euler-Maclaurin acceleration
      of the Dirichlet series (NOT analytic continuation): the sum
      sum_{n=0}^inf (n+a)^{-s} is rearranged as
        sum_{n=0}^{N-1}(n+a)^{-s}  +  (N+a)^{1-s}/(s-1)  +  (N+a)^{-s}/2
                                   +  Bernoulli corrections.
      This is the same convergent Dirichlet series, evaluated efficiently;
      it stays strictly within the convergent region Re(s) > 1.
    - Reports the EXACT empirical minimum, maximum, mean, and locations
      of extrema for H_L over the requested t-interval.
    - Reports a count of t-values where H_L < 0, with no claim of statistical
      or theoretical significance attached to that count.

What it does NOT do:
    - It does NOT claim that negative values of H_DH localize off-line
      zeros of the Davenport-Heilbronn function. The classical Hadamard
      argument runs from positivity to zero-free regions; the converse
      (from positivity failure to zero existence) is NOT an established
      theorem and we do not assert it.
    - It does NOT claim any specific magnitude of "Euler defect" is
      structurally significant. The lower bounds reported below are
      exploratory profiling metrics only.
    - It does NOT touch analytic continuation, the critical strip, or
      any zero-finding. All evaluations are strictly in Re(s) > 1.

Why the script is still useful:
    - For zeta and zeta*L(chi_3), classical theory guarantees H >= 0
      (Hadamard 1893 + the standard product-trick extension). Checking
      this numerically is a sanity test on the Dirichlet-series evaluator.
    - For Davenport-Heilbronn there is no known positive-log-coefficient
      product companion. We profile H to see what numerical lower bounds
      arise empirically. Whatever number comes out is what comes out; we
      attach no theorem to it.

============================================================================
USAGE
============================================================================

    python experiments/hadamard_positivity.py
    python experiments/hadamard_positivity.py --sigma 1.05 --t-min 0 --t-max 50
    python experiments/hadamard_positivity.py --sigma 1.5 --n-points 2000

============================================================================
"""

import argparse
import math
from dataclasses import dataclass
from typing import Callable, List, Tuple


# ----------------------------------------------------------------------------
# Hurwitz zeta via Euler-Maclaurin acceleration of the Dirichlet series
# ----------------------------------------------------------------------------
#
# We need to evaluate sum_{n=0}^inf (n+a)^{-s} for complex s with Re(s) > 1
# and 0 < a <= 1. Direct summation converges as N^{1-sigma}, which at
# sigma = 1.05 needs ~ 10^15 terms for 1% accuracy. Euler-Maclaurin
# rearranges the series into a small head sum plus an explicit asymptotic
# tail using Bernoulli numbers, giving ~ 10^-12 accuracy with N = 20.
#
# This is NOT analytic continuation. It is a strictly-equivalent rewriting
# of the Dirichlet sum valid for Re(s) > 1.

# Bernoulli numbers B_2, B_4, ..., B_14 divided by their factorials:
#   B_{2k} / (2k)!
_BERNOULLI_OVER_FACTORIAL = [
    1 / 12,           # k=1:  B_2  / 2!  =  (1/6)   / 2
    -1 / 720,         # k=2:  B_4  / 4!  =  (-1/30) / 24
    1 / 30_240,       # k=3:  B_6  / 6!  =  (1/42)  / 720
    -1 / 1_209_600,   # k=4:  B_8  / 8!  =  (-1/30) / 40320
    1 / 47_900_160,   # k=5:  B_10 / 10! =  (5/66)  / 3628800
    -691 / 1_307_674_368_000,  # k=6
    1 / 74_724_249_600,        # k=7
]


def hurwitz_zeta(s: complex, a: float, n_head: int = 20) -> complex:
    """
    Hurwitz zeta function zeta(s, a) = sum_{n=0}^inf (n + a)^{-s}
    for Re(s) > 1, 0 < a <= 1, computed by Euler-Maclaurin acceleration.

    With n_head = 20 and seven Bernoulli corrections, the relative error
    is below 1e-12 for sigma >= 1.05 and |t| <= 100.
    """
    # head sum
    total = sum((n + a) ** (-s) for n in range(n_head))

    # Euler-Maclaurin tail at the point a + n_head
    base = n_head + a
    # leading integral approximation
    total += base ** (1 - s) / (s - 1)
    # half-correction at endpoint
    total += 0.5 * base ** (-s)

    # Bernoulli corrections
    # k-th term: B_{2k}/(2k)!  *  s(s+1)...(s+2k-2)  *  base^{-s - 2k + 1}
    pochhammer = 1.0 + 0j
    for k, coef in enumerate(_BERNOULLI_OVER_FACTORIAL, start=1):
        # build pochhammer (s)(s+1)...(s + 2k-2)  incrementally
        # at k=1 this is just s
        # going from k to k+1 multiplies by (s + 2k-1)(s + 2k)
        if k == 1:
            pochhammer = s
        else:
            pochhammer *= (s + 2 * k - 3) * (s + 2 * k - 2)
        total += coef * pochhammer * base ** (-s - 2 * k + 1)

    return total


# ----------------------------------------------------------------------------
# L-functions, all built from Hurwitz zeta to ensure consistent precision
# ----------------------------------------------------------------------------

def zeta(s: complex) -> complex:
    """Riemann zeta function via Hurwitz: zeta(s) = zeta(s, 1)."""
    return hurwitz_zeta(s, 1.0)


def L_chi3(s: complex) -> complex:
    """L(s, chi_3) for chi_3 the non-principal Dirichlet character mod 3.
    chi_3(1) = 1, chi_3(2) = -1, chi_3(3) = 0.
    L(s, chi_3) = 3^{-s} * [zeta(s, 1/3) - zeta(s, 2/3)]."""
    return (3 ** (-s)) * (hurwitz_zeta(s, 1 / 3) - hurwitz_zeta(s, 2 / 3))


# The Davenport-Heilbronn parameter (their 1936 choice, giving the
# functional equation that mimics zeta's).
ALPHA_DH = (math.sqrt(10) - 2 * math.sqrt(5)) / 2


def L_chi5_complex(s: complex) -> complex:
    """L(s, chi) for the non-real Dirichlet character mod 5 with chi(2) = i.
    chi(1)=1, chi(2)=i, chi(3)=-i, chi(4)=-1, chi(5)=0.
    L(s, chi) = 5^{-s} * sum_{a=1..4} chi(a) * zeta(s, a/5)."""
    coeffs = [1, 1j, -1j, -1]  # chi(1), chi(2), chi(3), chi(4)
    return (5 ** (-s)) * sum(
        c * hurwitz_zeta(s, a / 5)
        for c, a in zip(coeffs, [1, 2, 3, 4])
    )


def L_chi5_bar(s: complex) -> complex:
    """L(s, chi-bar): complex conjugate character."""
    coeffs = [1, -1j, 1j, -1]
    return (5 ** (-s)) * sum(
        c * hurwitz_zeta(s, a / 5)
        for c, a in zip(coeffs, [1, 2, 3, 4])
    )


def davenport_heilbronn(s: complex) -> complex:
    """The Davenport-Heilbronn function:
        f(s) = ((1 - alpha)/2) * L(s, chi) + ((1 + alpha)/2) * L(s, chi-bar)
    with alpha chosen so f satisfies a functional equation symmetric about
    Re(s) = 1/2. The function has NO Euler product because it is a
    non-trivial linear combination of distinct L-functions."""
    return ((1 - ALPHA_DH) * L_chi5_complex(s)
            + (1 + ALPHA_DH) * L_chi5_bar(s)) / 2


# ----------------------------------------------------------------------------
# The Hadamard quantity
# ----------------------------------------------------------------------------

def hadamard_quantity(L: Callable[[complex], complex],
                      sigma: float, t: float) -> float:
    """H_L(sigma, t) = 3 log|L(sigma)| + 4 log|L(sigma + it)| + log|L(sigma + 2it)|.
    Returns NaN if any value vanishes."""
    v1 = L(complex(sigma, 0))
    v2 = L(complex(sigma, t))
    v3 = L(complex(sigma, 2 * t))
    if abs(v1) == 0 or abs(v2) == 0 or abs(v3) == 0:
        return float("nan")
    return (3 * math.log(abs(v1))
            + 4 * math.log(abs(v2))
            +     math.log(abs(v3)))


# ----------------------------------------------------------------------------
# Profile: evaluate H at evenly-spaced t over a user-defined interval
# ----------------------------------------------------------------------------

@dataclass
class Profile:
    name: str
    sigma: float
    t_min: float
    t_max: float
    n_points: int
    min_H: float
    max_H: float
    mean_H: float
    t_at_min: float
    t_at_max: float
    n_negative: int


def profile(L: Callable[[complex], complex], name: str,
            sigma: float, t_min: float, t_max: float,
            n_points: int) -> Profile:
    """Compute H_L(sigma, t) at n_points evenly-spaced t in [t_min, t_max].
    Report empirical extrema and locations -- no interpretation attached."""
    if n_points < 2:
        raise ValueError("n_points must be >= 2")

    t_values = [
        t_min + (t_max - t_min) * i / (n_points - 1)
        for i in range(n_points)
    ]
    H_values: List[float] = []
    for t in t_values:
        h = hadamard_quantity(L, sigma, t)
        if not math.isnan(h):
            H_values.append(h)

    if not H_values:
        raise RuntimeError(
            f"All {n_points} evaluations of H_{name} returned NaN. "
            f"Check that the Dirichlet series implementation is correct."
        )

    min_H = min(H_values)
    max_H = max(H_values)
    mean_H = sum(H_values) / len(H_values)
    i_min = H_values.index(min_H)
    i_max = H_values.index(max_H)
    n_negative = sum(1 for h in H_values if h < 0)

    return Profile(
        name=name, sigma=sigma, t_min=t_min, t_max=t_max, n_points=n_points,
        min_H=min_H, max_H=max_H, mean_H=mean_H,
        t_at_min=t_values[i_min], t_at_max=t_values[i_max],
        n_negative=n_negative,
    )


def print_profile(p: Profile) -> None:
    """Print a profile result. No 'verdict' string; just the numbers."""
    print(f"  {p.name}")
    print(f"    sigma = {p.sigma:.4f},  t in [{p.t_min:.4f}, {p.t_max:.4f}],  "
          f"{p.n_points} evaluation points")
    print(f"    min  H = {p.min_H:+.6f}   at t = {p.t_at_min:.6f}")
    print(f"    max  H = {p.max_H:+.6f}   at t = {p.t_at_max:.6f}")
    print(f"    mean H = {p.mean_H:+.6f}")
    print(f"    #points with H < 0 :  {p.n_negative} / {p.n_points}")
    print()


# ----------------------------------------------------------------------------
# CLI driver
# ----------------------------------------------------------------------------

# L-functions we profile, paired with a short label:
PROFILED_FUNCTIONS: List[Tuple[Callable[[complex], complex], str]] = [
    (zeta,                                "zeta(s)"),
    (L_chi3,                              "L(s, chi_3)"),
    (lambda s: zeta(s) * L_chi3(s),       "zeta(s) * L(s, chi_3)"),
    (davenport_heilbronn,                 "Davenport-Heilbronn f(s)"),
    (lambda s: zeta(s) * davenport_heilbronn(s), "zeta(s) * f(s)"),
]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Profile the Hadamard quantity H_L(sigma, t) for "
                    "several L-functions along a fixed-sigma line."
    )
    parser.add_argument("--sigma", type=float, default=1.05,
                        help="Real part sigma (default: 1.05). "
                             "Must satisfy sigma > 1.")
    parser.add_argument("--t-min", type=float, default=0.0,
                        help="Minimum t (default: 0.0).")
    parser.add_argument("--t-max", type=float, default=50.0,
                        help="Maximum t (default: 50.0).")
    parser.add_argument("--n-points", type=int, default=500,
                        help="Number of evaluation points (default: 500).")
    args = parser.parse_args()

    if args.sigma <= 1.0:
        parser.error("sigma must be > 1.0 (convergent region only).")

    print("=" * 72)
    print("Hadamard-quantity profile")
    print("=" * 72)
    print()
    print("Profiling H_L(sigma, t) along the line sigma = "
          f"{args.sigma} for t in "
          f"[{args.t_min}, {args.t_max}], {args.n_points} evenly-spaced points.")
    print()
    print("Reminder: this is an EXPLORATORY profiling metric. Negative values")
    print("of H for non-Euler-product L-functions are structurally consistent")
    print("with the absence of a positive-log-coefficient companion, but they")
    print("are NOT a localization tool for off-line zeros. No claim of zero")
    print("existence or location is attached to the numbers below.")
    print()

    for L, name in PROFILED_FUNCTIONS:
        p = profile(L, name, args.sigma, args.t_min, args.t_max, args.n_points)
        print_profile(p)


if __name__ == "__main__":
    main()
