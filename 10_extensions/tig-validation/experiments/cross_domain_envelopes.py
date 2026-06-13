"""
cross_domain_envelopes.py — three processes, three envelope behaviors.

============================================================================
WHAT THIS DEMONSTRATES
============================================================================

The framework's lens says: when you see a straight-line summary in data,
look at the envelope of the residual.

This script shows the lens in action across three different processes:

  (A) Random walk Sn = X1 + ... + Xn with i.i.d. +/- 1 steps.
      The envelope is sqrt(n) by the Central Limit Theorem (THEOREM, 1733-1812).

  (B) Prime staircase psi(x) = sum_{p^k <= x} log(p).
      The envelope is conjectured to be sqrt(x) * log^2(x) under RH.
      Verified empirically to x ~ 10^13 via zero computations.

  (C) Levy walk Sn = X1 + ... + Xn with i.i.d. steps from a heavy-tailed
      stable distribution (alpha = 1.5).
      The envelope is n^(1/alpha) = n^(2/3), NOT sqrt(n).
      This is by the Generalized Central Limit Theorem.

============================================================================
WHY ALL THREE
============================================================================

(A) and (B) both have parabolic envelopes -- but for DIFFERENT REASONS:
  - (A) by CLT, which requires finite variance of steps.
  - (B) by the explicit formula for zeros, conditional on RH.

This is a fact about envelopes, NOT a unified mechanism. The framework's
lens helps notice that both have sqrt-shape envelopes, but it does NOT
claim that one process explains the other.

(C) breaks the parabolic pattern entirely. Heavy-tailed step distributions
produce envelopes that grow faster than sqrt(n). This is exactly the kind
of case the framework's discipline insists on checking: if you see a
parabolic envelope, that is INFORMATION about the underlying process
(finite variance, CLT-like, etc.). It is NOT a universal default.

============================================================================
WHAT THIS SCRIPT IS NOT
============================================================================

It is not a unification of (A), (B), (C) under a single theory.
It is not a claim that the framework derives any of them.
It is not a substitute for the domain-specific theorems (CLT, GCLT, RH).

It IS a clean cross-domain illustration of the framework's visual
vocabulary: same residual-envelope question, three different answers.
"""

import math
import random
from pathlib import Path
from typing import List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# Use the prime sieve / psi from the existing staircase module
import sys
sys.path.insert(0, str(Path(__file__).parent))
from staircase_envelope import sieve, psi_sampled


# ----------------------------------------------------------------------------
# Random walk with +/- 1 steps (finite variance, CLT applies)
# ----------------------------------------------------------------------------

def random_walk(n_steps: int, seed: int = 42) -> np.ndarray:
    """Simple +/-1 random walk; returns the cumulative path S_0, S_1, ..., S_n."""
    rng = np.random.default_rng(seed)
    steps = rng.choice([-1, 1], size=n_steps)
    return np.concatenate(([0], np.cumsum(steps)))


# ----------------------------------------------------------------------------
# Levy walk with heavy-tailed steps (variance infinite, GCLT applies)
# ----------------------------------------------------------------------------

def levy_walk(n_steps: int, alpha: float = 1.5, seed: int = 42) -> np.ndarray:
    """
    Random walk where each step is drawn from a symmetric stable distribution
    with stability parameter alpha (1 < alpha < 2 gives heavy tails but finite
    mean). For alpha < 2, variance is INFINITE; the envelope of S_n grows
    as n^{1/alpha}, not as sqrt(n).
    """
    rng = np.random.default_rng(seed)
    # symmetric stable variates via Chambers-Mallows-Stuck algorithm
    U = rng.uniform(-math.pi / 2, math.pi / 2, size=n_steps)
    W = rng.exponential(1.0, size=n_steps)
    steps = (np.sin(alpha * U) / (np.cos(U) ** (1 / alpha))
             * (np.cos(U - alpha * U) / W) ** ((1 - alpha) / alpha))
    return np.concatenate(([0], np.cumsum(steps)))


# ----------------------------------------------------------------------------
# Make the three-panel figure
# ----------------------------------------------------------------------------

def make_figure(output_path: Path,
                walk_n: int = 5000,
                psi_xmax: int = 5000,
                k_clt: float = 3.0,
                k_rh: float = 3.0,
                levy_alpha: float = 1.5,
                k_levy: float = 3.0,
                seed: int = 42) -> Path:
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # ---- (A) Random walk with sqrt(n) envelope (CLT) ----
    ax = axes[0]
    rw = random_walk(walk_n, seed=seed)
    ns = np.arange(len(rw))
    ax.plot(ns, rw, color="#1f77b4", linewidth=0.7, label="S_n  (random walk)")
    ax.axhline(0, color="black", linewidth=1.0, linestyle="--", label="mean = 0")
    sqrt_env_upper = k_clt * np.sqrt(np.maximum(ns, 1))
    sqrt_env_lower = -sqrt_env_upper
    ax.plot(ns, sqrt_env_upper, color="#d62728", linewidth=1.5,
            label=f"y = +/- {k_clt}*sqrt(n)  (CLT envelope, THEOREM)")
    ax.plot(ns, sqrt_env_lower, color="#d62728", linewidth=1.5)
    ax.fill_between(ns, sqrt_env_lower, sqrt_env_upper, color="#d62728", alpha=0.08)
    ax.set_xlabel("n")
    ax.set_ylabel("S_n")
    ax.set_title("(A) Random walk: parabolic envelope by CLT\n"
                 f"n = {walk_n} i.i.d. +/-1 steps; envelope is sqrt(n) (theorem)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    # ---- (B) Prime staircase residual with sqrt(x) envelope (RH conjectural) ----
    ax = axes[1]
    n_sample = 600
    xs = np.linspace(1, psi_xmax, n_sample)
    psi_vals = np.array(psi_sampled(list(xs), psi_xmax))
    residual = psi_vals - xs
    ax.plot(xs, residual, color="#1f77b4", linewidth=0.8,
            label="psi(x) - x  (prime residual)")
    ax.axhline(0, color="black", linewidth=1.0, linestyle="--", label="mean = 0")
    sqrt_env_upper = k_rh * np.sqrt(xs)
    sqrt_env_lower = -sqrt_env_upper
    ax.plot(xs, sqrt_env_upper, color="#d62728", linewidth=1.5,
            label=f"y = +/- {k_rh}*sqrt(x)  (RH envelope, CONJECTURE)")
    ax.plot(xs, sqrt_env_lower, color="#d62728", linewidth=1.5)
    ax.fill_between(xs, sqrt_env_lower, sqrt_env_upper, color="#d62728", alpha=0.08)
    ax.set_xlabel("x")
    ax.set_ylabel("psi(x) - x")
    ax.set_title("(B) Primes: parabolic envelope under RH\n"
                 f"x up to {psi_xmax}; envelope is sqrt(x) (conjectural)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    # ---- (C) Levy walk: SUPER-parabolic envelope (GCLT) ----
    ax = axes[2]
    lw = levy_walk(walk_n, alpha=levy_alpha, seed=seed)
    ns = np.arange(len(lw))
    ax.plot(ns, lw, color="#1f77b4", linewidth=0.7, label="S_n  (Levy walk)")
    ax.axhline(0, color="black", linewidth=1.0, linestyle="--", label="mean = 0")
    # The true envelope for alpha-stable walks scales as n^{1/alpha}; the
    # k_levy constant absorbs scale + scale-of-distribution factors.
    levy_exp = 1 / levy_alpha
    ns_safe = np.maximum(ns, 1)
    levy_env_upper = k_levy * (ns_safe ** levy_exp)
    levy_env_lower = -levy_env_upper
    ax.plot(ns, levy_env_upper, color="#d62728", linewidth=1.5,
            label=f"y = +/- {k_levy}*n^(1/{levy_alpha}) (GCLT envelope, THEOREM)")
    ax.plot(ns, levy_env_lower, color="#d62728", linewidth=1.5)
    # Also overlay sqrt envelope for COMPARISON to show it doesn't contain the walk
    sqrt_env_upper_C = k_levy * np.sqrt(ns_safe)
    sqrt_env_lower_C = -sqrt_env_upper_C
    ax.plot(ns, sqrt_env_upper_C, color="#2ca02c", linewidth=1.0, linestyle=":",
            label=f"y = +/- {k_levy}*sqrt(n)  (NAIVE sqrt envelope, INSUFFICIENT)")
    ax.plot(ns, sqrt_env_lower_C, color="#2ca02c", linewidth=1.0, linestyle=":")
    ax.fill_between(ns, levy_env_lower, levy_env_upper, color="#d62728", alpha=0.06)
    ax.set_xlabel("n")
    ax.set_ylabel("S_n")
    ax.set_title(f"(C) Levy walk (alpha={levy_alpha}): SUPER-parabolic envelope\n"
                 "heavy tails -> envelope ~ n^(1/alpha) > sqrt(n); the parabolic\n"
                 "lens FAILS here (green dotted line cannot contain the walk)",
                 fontsize=11)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)

    fig.suptitle(
        "Three processes, three envelope behaviors.\n"
        "Same VISUAL VOCABULARY (line + envelope), DIFFERENT mechanisms "
        "(CLT theorem, RH conjecture, GCLT theorem).\n"
        "The framework's lens makes the comparison precise; it does NOT unify the mechanisms.",
        fontsize=12, fontweight="bold"
    )
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    out = Path(__file__).parent.parent / "plots" / "cross_domain_envelopes.png"
    saved = make_figure(output_path=out)
    print(f"Saved figure to: {saved}")


if __name__ == "__main__":
    main()
