#!/usr/bin/env python3
"""
proof_first_g_event.py — verification script for Sprint 35 paper

"The First-G Event in the Coprimality Partition:
 Stability Windows, CRT Idempotent Count, and Prime-Indexed Phase
 Transitions"
B.R. Sanders, C.A. Luther, M. Gish (2026).
DOI: 10.5281/zenodo.18852047

Verifies Theorem 3.1 (First-G Event Localization) exhaustively for all
squarefree integers b in the range [2, 500]:
  (i)  |G_k(b)| = 0 for every k in {1, ..., p_1(b) - 1}
  (ii) G_{p_1(b)}(b) = {p_1(b)}, so |G_{p_1(b)}(b)| = 1.

The script prints a summary table and exits 0 iff there are no
counterexamples. All arithmetic is exact (Python integers + gcd).

Target: Integers: Electronic Journal of Combinatorial Number Theory.

Usage:
    python proof_first_g_event.py
"""

from math import gcd
from collections import Counter


def squarefree_kernel(n):
    """Return the largest squarefree divisor of n (radical of n)."""
    k = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            k *= p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        k *= n
    return k


def is_squarefree(n):
    """Return True iff n is squarefree (i.e., n == rad(n))."""
    if n < 2:
        return False
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return False
        else:
            p += 1
    return True


def smallest_prime_factor(n):
    """Return the smallest prime factor of n > 1."""
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n  # n is prime


def coprimality_partition(b, k):
    """Return (C, G) where C = coprimes in {1..k}, G = non-coprimes in {1..k}."""
    C, G = [], []
    for x in range(1, k + 1):
        if gcd(x, b) == 1:
            C.append(x)
        else:
            G.append(x)
    return C, G


def verify_first_g_event(b):
    """Check (i) and (ii) for a single b. Return (pass: bool, reason: str)."""
    p1 = smallest_prime_factor(b)

    # (i) |G_k(b)| = 0 for every k in {1, ..., p_1 - 1}
    for k in range(1, p1):
        _, G = coprimality_partition(b, k)
        if len(G) != 0:
            return False, f"Part (i) fail: b={b}, p1={p1}, k={k}, G={G}"

    # (ii) G_{p_1}(b) = {p_1}
    _, G_at_p1 = coprimality_partition(b, p1)
    if G_at_p1 != [p1]:
        return False, f"Part (ii) fail: b={b}, p1={p1}, G_{{p1}}={G_at_p1}"

    return True, "ok"


def main():
    B_MAX = 500
    squarefrees = [b for b in range(2, B_MAX + 1) if is_squarefree(b)]
    total_pairs = 0
    failures = []
    spf_distribution = Counter()

    print(f"Verifying First-G Event Localization for squarefree b in [2, {B_MAX}]...")
    print(f"  (Theorem 3.1 of Sanders-Luther-Gish 2026)\n")

    for b in squarefrees:
        p1 = smallest_prime_factor(b)
        spf_distribution[p1] += 1
        # total_pairs per b = (p1 - 1) pairs for Part (i) + 1 pair for Part (ii)
        total_pairs += p1

        ok, reason = verify_first_g_event(b)
        if not ok:
            failures.append((b, reason))

    # Summary
    print(f"  squarefree b tested:     {len(squarefrees):>6d}")
    print(f"  total (b, k) pairs:      {total_pairs:>6d}")
    print(f"  counterexamples (Part i):  {sum(1 for _, r in failures if 'Part (i)' in r):>6d}")
    print(f"  counterexamples (Part ii): {sum(1 for _, r in failures if 'Part (ii)' in r):>6d}")

    # Distribution by smallest prime factor
    print(f"\n  Distribution by smallest prime factor p_1:")
    print(f"    {'p_1':>6} {'# b':>8} {'window':>8}")
    for p1 in sorted(spf_distribution):
        print(f"    {p1:>6d} {spf_distribution[p1]:>8d} {p1-1:>8d}")
    print(f"    {'total':>6} {sum(spf_distribution.values()):>8d}")

    # Failure report
    if failures:
        print(f"\n  {len(failures)} FAILURE(S):")
        for b, r in failures[:10]:
            print(f"    b = {b}: {r}")
        if len(failures) > 10:
            print(f"    ... ({len(failures) - 10} more)")
        return 1
    else:
        print(f"\n  STATUS: PASS — zero counterexamples across all "
              f"{len(squarefrees)} squarefree b and {total_pairs} (b,k) pairs.")
        print(f"  QED (Theorem 3.1 verified on the specified range).")
        return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
