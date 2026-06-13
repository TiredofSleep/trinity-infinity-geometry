"""
envelope_analyzer_demo.py — applies the analyzer to the three cross-domain cases.

Demonstrates that the analyzer correctly identifies:

  - Random walk:    envelope ~ sqrt(n)   (alpha ~ 0.5)
  - Prime staircase: envelope ~ sqrt(x)  (alpha ~ 0.5 under RH)
  - Levy walk:      envelope ~ n^(1/1.5) = n^(2/3)  (alpha ~ 0.67)

If the analyzer cannot distinguish these, it isn't a useful tool. This
script is the discriminative test.
"""

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).parent))

from envelope_analyzer import analyze, report
from cross_domain_envelopes import random_walk, levy_walk
from staircase_envelope import psi_sampled


def main() -> None:
    rng_seed = 42

    # --- (A) Random walk ENSEMBLE ---
    # A single random walk has high realization-to-realization variance, so
    # the empirical envelope is noisy. Averaging over an ensemble gives a
    # cleaner estimate. We stack K walks into one (n, |S_n|) dataset.
    K = 30
    N = 10_000
    all_ns = []
    all_Sn = []
    for k in range(K):
        walk = random_walk(n_steps=N, seed=rng_seed + k)
        all_ns.append(np.arange(1, len(walk)))
        all_Sn.append(walk[1:])
    ns_rw = np.concatenate(all_ns)
    Sn_rw = np.concatenate(all_Sn)
    analysis = analyze(ns_rw, Sn_rw, skip_line_fit=True, n_bins=30)
    print(report(analysis,
                 header=f"(A) RANDOM WALK  (ensemble of {K} walks, N={N}; expect alpha ~ 0.5)"))
    print()

    # --- (B) Prime staircase residual ---
    # This is one realization (only one set of primes), but has rich oscillation
    # structure from many zeta zeros, so the empirical envelope is clean.
    psi_xmax = 50_000
    xs = np.linspace(10, psi_xmax, 1500)
    psi_vals = np.array(psi_sampled(list(xs), psi_xmax))
    residual = psi_vals - xs
    analysis = analyze(xs, residual, skip_line_fit=True, n_bins=30)
    print(report(analysis,
                 header=f"(B) PRIME STAIRCASE  psi(x) - x for x up to {psi_xmax}, expect alpha ~ 0.5"))
    print()

    # --- (C) Levy walk ENSEMBLE ---
    all_ns = []
    all_Sn = []
    for k in range(K):
        walk = levy_walk(n_steps=N, alpha=1.5, seed=rng_seed + k)
        all_ns.append(np.arange(1, len(walk)))
        all_Sn.append(walk[1:])
    ns_lv = np.concatenate(all_ns)
    Sn_lv = np.concatenate(all_Sn)
    analysis = analyze(ns_lv, Sn_lv, skip_line_fit=True, n_bins=30)
    print(report(analysis,
                 header=f"(C) LEVY WALK  (ensemble of {K} walks, alpha=1.5; expect alpha ~ 0.667)"))


if __name__ == "__main__":
    main()
