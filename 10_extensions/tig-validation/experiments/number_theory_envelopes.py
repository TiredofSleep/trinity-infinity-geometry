"""
number_theory_envelopes.py -- the lens applied within math, testing
DIFFERENT conjectured exponents.

============================================================================
WHY THIS EXISTS
============================================================================

The cross-domain figure shows the lens across processes with the same
expected exponent (sqrt) but different mechanisms (CLT vs RH).

This experiment shows the lens WITHIN number theory, across functions
with DIFFERENT expected exponents:

  (1) psi(x) - x           prime staircase residual
                           expected envelope: sqrt(x) * log^2(x), alpha ~ 0.5
                           (under RH; this is the von Mangoldt summatory)

  (2) Delta(x) = D(x) - main_terms     Dirichlet divisor problem residual
                           where D(x) = sum_{n<=x} d(n), d(n) = number of
                           divisors of n, and the main terms are
                           x log(x) + (2*gamma - 1) * x.
                           Conjectured envelope: x^(1/4 + epsilon), alpha ~ 0.25
                           Best unconditional: x^0.314 (Bourgain-Watt 2017)
                           Original Voronoi bound: x^(1/3)

  (3) M(x) = sum_{n<=x} mu(n)           Mertens function
                           expected envelope: sqrt(x), alpha ~ 0.5
                           (under RH, mu being the Mobius function)

If the envelope analyzer is doing real work, it should report
DISTINCTLY DIFFERENT alphas for (2) versus (1, 3).

If it reports the same alpha for all three, it's not actually
discriminating -- and we've learned something about the tool's
limitations at this scale.

============================================================================
SOURCES
============================================================================

* Tenenbaum, "Introduction to Analytic and Probabilistic Number Theory" (Ch I.6).
* Iwaniec & Kowalski, "Analytic Number Theory", Theorem 13.5 (divisor sums).
* Titchmarsh, "Theory of the Riemann Zeta-Function", Ch XII (omega bounds).
* Bourgain & Watt, "Mean square of zeta function...", 2017 (alpha = 0.31490).

This script does not cite any of these in its output -- they are the
background literature. The point is the empirical measurement.
"""

import math
import sys
from pathlib import Path
from typing import Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent))
from envelope_analyzer import analyze, report

# Use the existing prime sieve to compute psi(x) - x cleanly
from staircase_envelope import sieve, psi_sampled


# Euler-Mascheroni constant (high precision)
EULER_GAMMA = 0.5772156649015328606065120900824024310421


# ----------------------------------------------------------------------------
# Divisor function d(n) and the divisor problem residual
# ----------------------------------------------------------------------------

def divisor_count_sieve(N: int) -> np.ndarray:
    """Return d[0..N] where d[n] = number of divisors of n.
    Algorithm: for each k in 1..N, every multiple of k has k as a divisor.
    Cost: O(N log N)."""
    d = np.zeros(N + 1, dtype=np.int64)
    for k in range(1, N + 1):
        d[k::k] += 1
    return d


def divisor_summatory(N: int) -> np.ndarray:
    """D[n] = sum_{m<=n} d(m) for n = 0..N."""
    d = divisor_count_sieve(N)
    return np.cumsum(d)


def divisor_residual(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """Compute Delta(x) = D(x) - x log(x) - (2 gamma - 1) x for x = 1..N.
    The leading main terms are the Dirichlet asymptotic.

    Note: there's a controversy in some references about whether the
    constant 1/4 should be included as an additional main term
    (Voronoi's original formula). We use the canonical two-term version
    which is standard in Iwaniec-Kowalski."""
    D = divisor_summatory(N)
    xs = np.arange(N + 1, dtype=float)
    xs[0] = 1e-30  # avoid log(0)
    main = xs * np.log(xs) + (2 * EULER_GAMMA - 1) * xs
    delta = D - main
    return xs[1:], delta[1:]  # drop n=0


# ----------------------------------------------------------------------------
# Mobius function mu(n) and the Mertens function M(x)
# ----------------------------------------------------------------------------

def mobius_sieve(N: int) -> np.ndarray:
    """Return mu[0..N] using the smallest-prime-factor sieve.
    mu(1) = 1; mu(n) = 0 if n has a squared prime factor; otherwise
    mu(n) = (-1)^k where k = number of distinct prime factors."""
    spf = np.zeros(N + 1, dtype=np.int32)  # smallest prime factor
    for i in range(2, N + 1):
        if spf[i] == 0:  # i is prime
            for j in range(i, N + 1, i):
                if spf[j] == 0:
                    spf[j] = i

    mu = np.zeros(N + 1, dtype=np.int8)
    mu[1] = 1
    for n in range(2, N + 1):
        p = int(spf[n])
        m = n // p
        if m % p == 0:
            mu[n] = 0
        else:
            mu[n] = -mu[m]
    return mu


def mertens(N: int) -> np.ndarray:
    """M[n] = sum_{k<=n} mu(k) for n = 0..N."""
    mu = mobius_sieve(N)
    return np.cumsum(mu.astype(np.int64))


# ----------------------------------------------------------------------------
# Run the three analyses
# ----------------------------------------------------------------------------

def main() -> None:
    N = 200_000  # large enough to get clean envelope behavior

    print(f"Computing all three functions up to N = {N}...")
    print()

    # (1) psi(x) - x
    print("--- Computing prime staircase residual ---")
    n_sample = 2000
    xs_psi = np.linspace(10, N, n_sample)
    psi_vals = np.array(psi_sampled(list(xs_psi), N))
    psi_residual = psi_vals - xs_psi
    a_psi = analyze(xs_psi, psi_residual, skip_line_fit=True, n_bins=30)
    print(report(a_psi, header="(1) PSI(x) - x   prime staircase residual, expect alpha ~ 0.5"))
    print()

    # (2) Dirichlet divisor problem residual
    print("--- Computing Dirichlet divisor residual (may take a moment) ---")
    xs_div, delta = divisor_residual(N)
    # subsample for speed (analyzer doesn't need every integer)
    step = max(1, len(xs_div) // 5000)
    xs_div_sub = xs_div[::step]
    delta_sub = delta[::step]
    a_div = analyze(xs_div_sub, delta_sub, skip_line_fit=True, n_bins=30)
    print(report(a_div, header="(2) Delta(x) = D(x) - main_terms   divisor problem, expect alpha ~ 0.25"))
    print()

    # (3) Mertens function
    print("--- Computing Mertens function (Mobius sieve) ---")
    M = mertens(N)
    ns_m = np.arange(1, N + 1, dtype=float)
    M_vals = M[1:].astype(float)
    step = max(1, len(ns_m) // 5000)
    ns_m_sub = ns_m[::step]
    M_sub = M_vals[::step]
    a_m = analyze(ns_m_sub, M_sub, skip_line_fit=True, n_bins=30)
    print(report(a_m, header="(3) M(x) = Mertens function, expect alpha ~ 0.5 under RH"))
    print()

    # Summary
    print("=" * 72)
    print("CROSS-FUNCTION SUMMARY")
    print("=" * 72)
    print(f"  (1) psi(x) - x:       measured alpha = {a_psi.power_law.alpha:.4f}  (expect ~0.5)")
    print(f"  (2) Delta(x) divisor: measured alpha = {a_div.power_law.alpha:.4f}  (expect ~0.25)")
    print(f"  (3) M(x) Mertens:     measured alpha = {a_m.power_law.alpha:.4f}  (expect ~0.5)")
    print()
    print("Discriminative test: is alpha(2) clearly smaller than alpha(1) and alpha(3)?")
    smaller_than_psi = a_div.power_law.alpha < a_psi.power_law.alpha - 0.10
    smaller_than_m = a_div.power_law.alpha < a_m.power_law.alpha - 0.10
    if smaller_than_psi and smaller_than_m:
        print("  YES: the divisor residual has a distinctly smaller envelope exponent,")
        print("  consistent with the conjectured x^(1/4+eps) bound being tighter than")
        print("  the sqrt(x) bound that applies to psi and M.")
    else:
        print("  NOT CLEARLY: at this scale (N = " + str(N) + ") the three exponents are")
        print("  not yet clearly separated. Larger N or refined main-term subtraction")
        print("  may sharpen the discrimination.")

    # Build the three-panel figure
    make_figure(xs_psi, psi_residual,
                xs_div_sub, delta_sub,
                ns_m_sub, M_sub,
                a_psi, a_div, a_m,
                output_path=Path(__file__).parent.parent / "plots" / "number_theory_envelopes.png")


def make_figure(xs_psi, psi_res,
                xs_div, delta,
                ns_m, M,
                a_psi, a_div, a_m,
                output_path: Path) -> Path:
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # ---- (1) psi(x) - x ----
    ax = axes[0]
    ax.plot(xs_psi, psi_res, color="#1f77b4", linewidth=0.7,
            label="psi(x) - x")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    k = 3.0
    ax.plot(xs_psi, k * np.sqrt(xs_psi), color="#d62728", linewidth=1.3,
            label=f"+/- {k}*sqrt(x) reference")
    ax.plot(xs_psi, -k * np.sqrt(xs_psi), color="#d62728", linewidth=1.3)
    ax.set_xlabel("x")
    ax.set_ylabel("psi(x) - x")
    ax.set_title(f"(1) Prime staircase residual\n"
                 f"measured alpha = {a_psi.power_law.alpha:.3f}  (expect ~0.5 under RH)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    # ---- (2) Dirichlet divisor residual ----
    ax = axes[1]
    ax.plot(xs_div, delta, color="#1f77b4", linewidth=0.7,
            label="Delta(x) = D(x) - x*log x - (2gamma-1)*x")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    # The conjectured envelope is x^(1/4); for comparison overlay both
    # x^(1/4) and sqrt(x) so the reader can see which one fits.
    k2 = 1.5
    ax.plot(xs_div, k2 * np.power(xs_div, 0.25), color="#d62728", linewidth=1.3,
            label=f"+/- {k2}*x^(1/4) conjectured envelope")
    ax.plot(xs_div, -k2 * np.power(xs_div, 0.25), color="#d62728", linewidth=1.3)
    ax.plot(xs_div, np.sqrt(xs_div), color="#2ca02c", linewidth=1.0, linestyle=":",
            label="+/- sqrt(x) (looser bound)")
    ax.plot(xs_div, -np.sqrt(xs_div), color="#2ca02c", linewidth=1.0, linestyle=":")
    ax.set_xlabel("x")
    ax.set_ylabel("Delta(x)")
    ax.set_title(f"(2) Dirichlet divisor residual\n"
                 f"measured alpha = {a_div.power_law.alpha:.3f}  (expect ~0.25 conjectured)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    # ---- (3) Mertens function ----
    ax = axes[2]
    ax.plot(ns_m, M, color="#1f77b4", linewidth=0.7, label="M(x) = Mertens")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.plot(ns_m, 2 * np.sqrt(ns_m), color="#d62728", linewidth=1.3,
            label="+/- 2*sqrt(x) reference (under RH)")
    ax.plot(ns_m, -2 * np.sqrt(ns_m), color="#d62728", linewidth=1.3)
    ax.set_xlabel("x")
    ax.set_ylabel("M(x)")
    ax.set_title(f"(3) Mertens function\n"
                 f"measured alpha = {a_m.power_law.alpha:.3f}  (expect ~0.5 under RH)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle(
        "Three number-theoretic residuals, three conjectured envelope exponents.\n"
        "Same lens (line + envelope), DIFFERENT predicted alphas (0.5 / 0.25 / 0.5).\n"
        "The envelope analyzer's measurements either confirm or contradict the predictions.",
        fontsize=12, fontweight="bold"
    )
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"Saved figure to: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
