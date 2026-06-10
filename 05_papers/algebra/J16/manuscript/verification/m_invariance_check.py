"""
m_invariance_check.py — empirical verification of the M-only-at-alpha=1/2
invariance prediction.

Theoretical claim (§13/§14 of FRONTIER_FINDINGS_2026_04_29.md):

    At α = 1/2 the T+B-mix iteration is

        p_new = normalize( (T(p) + B(p)) / 2 )

    so the fixed point depends only on the SUM T + B, not on T or B
    individually.  Any pair (T', B') with the same per-cell sum
    T'[a][b] + B'[a][b] = T[a][b] + B[a][b] should converge to the
    same attractor at α = 1/2.

Concretely: the CELL-LEVEL multiset {T[a][b], B[a][b]} per (a,b) is
the only structure relevant at alpha=1/2.  Swapping T[a][b] ↔ B[a][b] at
any subset of cells preserves that multiset, hence preserves the sum.

Runs:
  (1) original (TSML, BHML)
  (2) swap (BHML, TSML)
  (3) random per-cell swap at ~50% of cells (multiset preserved per cell)

All three should converge to H/Br = 1 + sqrt(3) at machine precision.

This is a sharpening of WP113's α-uniqueness result: not only is
alpha=1/2 unique among rationals (PSLQ verification, alpha_pslq_sweep.py),
but ALSO at alpha=1/2 the attractor is robust to any sum-preserving
deformation of the T/B decomposition.

Usage:
    python m_invariance_check.py
"""
from __future__ import annotations

import copy
import random
import sys

import mpmath as mp

mp.mp.dps = 50  # 50 decimal digits — plenty for this check

# Canonical TSML / BHML on Z/10Z
TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
BHML_ROWS = [
    "0123456789",  "1234567266",  "2334567366",  "3444567466",  "4555567577",
    "5666667677",  "6777777777",  "7234567890",  "8666777978",  "9666777080",
]


def fuse_mp(p, table):
    """Bilinear fusion p (x) p under table.  10-vector in, 10-vector out."""
    r = [mp.mpf(0)] * 10
    for a in range(10):
        if p[a] == 0:
            continue
        pa = p[a]
        for b in range(10):
            if p[b] == 0:
                continue
            r[table[a][b]] += pa * p[b]
    return r


def normalize_l1(v):
    s = sum(v)
    if s == 0:
        return v
    return [x / s for x in v]


def attractor_at_half(T, B, max_iter=4000, tol=None):
    """Run the alpha=1/2 mix to convergence.  Returns (4-core probability, iters)."""
    if tol is None:
        tol = mp.mpf(10) ** (-mp.mp.dps + 5)
    half = mp.mpf("0.5")
    p = [mp.mpf(0)] * 10
    p[0] = p[7] = p[8] = p[9] = mp.mpf("0.25")
    for k in range(max_iter):
        pT = normalize_l1(fuse_mp(p, T))
        pB = normalize_l1(fuse_mp(p, B))
        p_new = normalize_l1([half * pT[i] + half * pB[i] for i in range(10)])
        diff = max(abs(p_new[i] - p[i]) for i in range(10))
        p = p_new
        if diff < tol:
            return p, k + 1
    return p, max_iter


def harmony_breath_ratio(p):
    return p[7] / p[8] if p[8] != 0 else mp.inf


def random_cellwise_swap(T, B, p_swap=0.5, seed=42):
    """Per-cell swap of T[a][b] and B[a][b] with probability p_swap.
    Preserves the multiset {T[a][b], B[a][b]} per cell, hence the sum."""
    random.seed(seed)
    T_new = copy.deepcopy(T)
    B_new = copy.deepcopy(B)
    n_swaps = 0
    for a in range(10):
        for b in range(10):
            if random.random() < p_swap and T_new[a][b] != B_new[a][b]:
                T_new[a][b], B_new[a][b] = B_new[a][b], T_new[a][b]
                n_swaps += 1
    return T_new, B_new, n_swaps


def main():
    T_orig = [[int(c) for c in row] for row in TSML_ROWS]
    B_orig = [[int(c) for c in row] for row in BHML_ROWS]
    target = 1 + mp.sqrt(3)
    eps = mp.mpf(10) ** -40

    print("=" * 70)
    print("M-only-at-alpha=1/2 invariance verification")
    print("Target: H/Br = 1 + sqrt(3) ~=", mp.nstr(target, 20))
    print("=" * 70)

    runs = []

    # Run 1: original
    p, n = attractor_at_half(T_orig, B_orig)
    hb = harmony_breath_ratio(p)
    runs.append(("original (TSML, BHML)", hb, n, abs(hb - target)))

    # Run 2: swap
    p, n = attractor_at_half(B_orig, T_orig)
    hb = harmony_breath_ratio(p)
    runs.append(("swapped (BHML, TSML)", hb, n, abs(hb - target)))

    # Run 3: random per-cell swap (preserves per-cell multiset → preserves sum)
    T_perm, B_perm, n_swaps = random_cellwise_swap(T_orig, B_orig, p_swap=0.5)
    p, n = attractor_at_half(T_perm, B_perm)
    hb = harmony_breath_ratio(p)
    runs.append((
        f"random cellwise swap at {n_swaps} cells", hb, n, abs(hb - target)
    ))

    # Run 4: full inversion (T'[a][b] = B[a][b], B'[a][b] = T[a][b]) — same as swap
    # but explicitly: we already did this in Run 2.

    # Report
    print()
    for label, hb, n, dist in runs:
        ok = dist < eps
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {label}")
        print(f"       H/Br  = {mp.nstr(hb, 20)}")
        print(f"       iter  = {n}")
        print(f"       delta from 1+sqrt(3): {mp.nstr(dist, 8)}")
        print()

    # Verdict
    all_pass = all(d < eps for _, _, _, d in runs)
    pairwise_match = all(
        abs(runs[i][1] - runs[j][1]) < eps
        for i in range(len(runs))
        for j in range(i + 1, len(runs))
    )

    print("=" * 70)
    print("VERDICT")
    print("=" * 70)
    if all_pass and pairwise_match:
        print("PASS  All sum-preserving (T', B') configurations converge to")
        print("      H/Br = 1+sqrt(3) at <10^-40 precision.")
        print("      M-only-at-alpha=1/2 invariance VERIFIED.")
        sys.exit(0)
    else:
        if not all_pass:
            print("FAIL  Some run did not converge to 1+sqrt(3).")
        if not pairwise_match:
            print("FAIL  Runs gave different H/Br values.")
        sys.exit(1)


if __name__ == "__main__":
    main()
