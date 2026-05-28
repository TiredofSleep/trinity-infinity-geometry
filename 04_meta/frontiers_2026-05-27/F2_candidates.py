#!/usr/bin/env python3
"""
F2 — Pauli-divisor bijection candidate tests.

Goal: find a NATURAL map of the 32 divisors of 2310 = 2*3*5*7*11 onto subshell
labels (s/p/d/f, l in 0..3) such that the count distribution = (2, 6, 10, 14).

This is the open negative from HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md §1.1.

The retired J47/pauli_divisor_bijection.py "bijection" used hand-picked
categories (kernel_base, strand_pair, weight_4, kernel_touching_pair, full,
strand_kernel_full, single_prime, kernel_missing_3) that are not canonically
forced — it's a hand-built 8-class partition matched onto the right counts.

We test new candidates rigorously here.
"""
from __future__ import annotations
from itertools import combinations, product
from math import prod, gcd
from collections import Counter
from fractions import Fraction
import random

PRIMES = [2, 3, 5, 7, 11]
N = 2310  # product
TARGET = (2, 6, 10, 14)  # Pauli n=4 subshell capacities


def divisors_of_2310():
    """Returns list of (d, prime-mask) pairs."""
    divs = []
    for k in range(6):
        for subset in combinations(PRIMES, k):
            d = prod(subset) if subset else 1
            mask = tuple(1 if p in subset else 0 for p in PRIMES)
            divs.append((d, mask))
    return sorted(divs)


def check_distribution(label_fn, name):
    """Apply label_fn(d, mask) -> l in {0,1,2,3} (or None to skip).
    Return (counts_tuple, match_bool)."""
    divs = divisors_of_2310()
    counts = Counter()
    skipped = 0
    for d, m in divs:
        l = label_fn(d, m)
        if l is None:
            skipped += 1
        else:
            counts[l] += 1
    if skipped > 0:
        print(f"[{name}] WARNING: {skipped} divisors unmapped")
    dist = tuple(counts.get(l, 0) for l in range(4))
    match = dist == TARGET
    print(f"[{name}] distribution = {dist}, target {TARGET}, match: {match}")
    return dist, match


# ============================================================
# Candidate 1: sigma-orbit class on Z/10Z lifted to divisors
# ============================================================
# sigma is a permutation on Z/10Z. The canonical TIG sigma cycle is
# (1 -> 3 -> 9 -> 7 -> 1)(2 -> 6 -> 8 -> 4 -> 2)(5)(0). Map d to d mod 10
# then to its orbit. Orbits partition Z/10Z into sizes 4, 4, 1, 1.
# We need 4 buckets summing to (2, 6, 10, 14).

SIGMA = {0: 0, 1: 3, 3: 9, 9: 7, 7: 1, 2: 6, 6: 8, 8: 4, 4: 2, 5: 5}


def sigma_orbits():
    seen = set()
    orbits = []
    for x in range(10):
        if x in seen:
            continue
        orbit = []
        cur = x
        while cur not in seen:
            seen.add(cur)
            orbit.append(cur)
            cur = SIGMA[cur]
        orbits.append(tuple(sorted(orbit)))
    return orbits


def candidate_1_sigma_orbit(d, m):
    orbits = sigma_orbits()  # [(1,3,7,9), (2,4,6,8), (0,), (5,)]
    r = d % 10
    for i, orb in enumerate(orbits):
        if r in orb:
            return i if i < 4 else None
    return None


# ============================================================
# Candidate 2: p-adic valuation triple Hamming weight + parity
# ============================================================
# Each divisor d has 5-bit mask (a, b, c, e, f) over (2, 3, 5, 7, 11).
# Try l = (Hamming_weight + max_prime_index*0) ... let's try several
# bit-pattern -> l functions.


def candidate_2_hw_mod4(d, m):
    """Just Hamming weight mod 4: gives (1+5=6, 10, 10, 5+1=6) -> no good."""
    return sum(m) % 4


def candidate_2b_hw_signed(d, m):
    """Map Hamming weight 0/5 -> 0, 1/4 -> 1, 2/3 -> 2,3 split somehow."""
    h = sum(m)
    if h in (0, 5):
        return 0
    if h in (1, 4):
        return 1
    # h in (2, 3): need 10 split between l=2 and l=3 with counts 10, 14
    # we have 10 + 10 = 20 elements at h in {2,3}, distribute 10 vs 10 -> not 10,14
    return 2  # gives (2, 10, 20, 0)


# ============================================================
# Candidate 3: CRT coordinate class — use (d mod 2, d mod 11) since 2 and 11
# are the "outer kernel" primes (2 is kernel, 11 is outermost strand)
# ============================================================


def candidate_3_crt_2_11(d, m):
    """(d mod 2, d mod 11). 4 classes => need counts (2,6,10,14)."""
    a = d % 2
    b = 1 if d % 11 != 0 else 0  # is 11 | d
    return 2 * a + b


def candidate_3b_crt_kernel_strand(d, m):
    """Number of kernel primes dividing d (in {0,1,2}) gives 3 classes;
    pad to 4 by parity of strand-prime count."""
    k = (1 if d % 2 == 0 else 0) + (1 if d % 5 == 0 else 0)
    s = (1 if d % 3 == 0 else 0) + (1 if d % 7 == 0 else 0) + (1 if d % 11 == 0 else 0)
    # k in {0,1,2}, s in {0,1,2,3}
    # 4-class scheme: (k=0, s_even), (k=0, s_odd), (k>=1, s_even), (k>=1, s_odd)
    return 2 * (1 if k >= 1 else 0) + (s % 2)


# ============================================================
# Candidate 4: Divisor-pair sum d + 2310/d mod something
# ============================================================


def candidate_4_pairsum_mod(d, m):
    """Compute d + N/d. Distribution of (d + N/d) mod 16 or some modulus."""
    s = d + N // d
    # Try mod 32, then label by s mod 32 // 8
    return (s % 32) // 8


# ============================================================
# Candidate 5: Multiplicative order in (Z/N)* — only defined for coprime d
# ============================================================


def mult_order(a, n):
    if gcd(a, n) != 1:
        return None
    o = 1
    cur = a % n
    while cur != 1:
        cur = (cur * a) % n
        o += 1
        if o > n:
            return None
    return o


def candidate_5_mult_order(d, m):
    """Only coprime divisors (i.e., d=1). So this only labels 1 element."""
    o = mult_order(d, N)
    if o is None:
        return None
    return 0


# ============================================================
# Candidate 6: Lens-pair (d mod 10, d mod 11) class — TSML lives at mod 10,
# BHML at mod 11; bivariate.
# ============================================================


def candidate_6_lens_pair(d, m):
    """Compute (d mod 10, d mod 11), then partition by some 4-class function."""
    r10 = d % 10
    r11 = d % 11
    # Classify by parity of r10 and whether r11 == 0
    a = r10 % 2
    b = 1 if r11 == 0 else 0
    return 2 * a + b


# ============================================================
# Candidate 7: max-prime descent — l = index of largest prime dividing d
# ============================================================


def candidate_7_max_prime_idx(d, m):
    """Index of largest prime dividing d, in {0..4}; map to l = min(idx, 3)."""
    if d == 1:
        return 0
    for i in range(4, -1, -1):
        if m[i] == 1:
            return min(i, 3)
    return None


# ============================================================
# Candidate 8: smallest prime dividing d (mirror of 7)
# ============================================================


def candidate_8_min_prime_idx(d, m):
    """Index of smallest prime dividing d."""
    if d == 1:
        return 0
    for i in range(5):
        if m[i] == 1:
            return min(i, 3)
    return None


# ============================================================
# Candidate 9: number of distinct prime factors mod 4
# ============================================================


def candidate_9_omega(d, m):
    return sum(m) % 4


# ============================================================
# Candidate 10: divisor index in sorted list mod 4
# ============================================================


def candidate_10_idx_mod4(d, m, divs_list):
    return divs_list.index(d) % 4


# ============================================================
# Candidate 11: log2 floor of d mod 4
# ============================================================


def candidate_11_log2_floor(d, m):
    import math
    if d == 1:
        return 0
    return int(math.log2(d)) % 4


# ============================================================
# Candidate 12: Triangle-number bin — exploits Pauli pattern
#   Pauli capacity 2(2l+1) -> 2, 6, 10, 14 are triangular differences
#   l=0: divisors d where d=1 or d=N
#   l=1: 3 even-half + 3 odd-half = strand-only-pair divisors
#   l=2: ...
# The retired "bijection" used kernel/strand within parity halves.
# Try a CLEAN canonical rule: hash by (mask popcount, mask[0] xor mask[1]).
# ============================================================


def candidate_12_popcount_xor(d, m):
    h = sum(m)
    k = (m[0] ^ m[1]) + (m[2] ^ m[3])  # gives 0,1,2
    return min(h * 2 + k, 3) % 4


# ============================================================
# Candidate 13: Z/2310 multiplicative-character lift — Legendre-like
# ============================================================


def candidate_13_legendre(d, m):
    """For each prime p in {2,3,5,7,11}, compute Legendre-symbol-like value.
    For d, sum of (d mod p == 1) over the 5 primes."""
    count = sum(1 for p in PRIMES if d % p == 1)
    return count if count <= 3 else 3


# ============================================================
# Candidate 14: kernel-fingerprint encoding
# Use the kernel/strand split with a sharper, more canonical rule:
# l = (kernel bits) * 2 + parity(strand bits)
# kernel = {2, 5}, strand = {3, 7, 11}
# ============================================================


def candidate_14_kernel_strand_canonical(d, m):
    """kernel bits = m[0]+m[2] in {0,1,2}, strand bits = m[1]+m[3]+m[4] in {0..3}."""
    k = m[0] + m[2]  # 2, 5 are kernel
    s = m[1] + m[3] + m[4]  # 3, 7, 11 are strand
    # Try l = k + (s // 2): k in 0,1,2; s//2 in 0,1 -> l in 0..3
    return k + (s // 2)


def candidate_14b_kernel_strand_xor(d, m):
    k = m[0] + m[2]
    s = m[1] + m[3] + m[4]
    return ((k + s) % 4)


# ============================================================
# Candidate 15: Pauli-state-style ordering — interpret d as bitstring,
# then group by structure mimicking (n_principal, l_angular, m_mag, s_spin)
# ============================================================


def candidate_15_pauli_ladder(d, m):
    """For each divisor d, compute principal-quantum-number-like value n,
    then split by parity to get spin, by angular position to get l."""
    # Use d's prime-exponent triple as a multi-quantum-number tuple
    # n_eff = total Hamming weight, l_eff = number of "outer" primes (7, 11)
    n = sum(m)
    l = m[3] + m[4]  # 7 and 11 only
    return min(l, 3)


# ============================================================
# Candidate 16: NEW IDEA — Mobius-style sign decomposition
# Mobius function mu(d) is (-1)^k for squarefree d with k primes.
# All 32 divisors of 2310 are squarefree. So mu(d) = (-1)^omega(d).
# 16 have mu = +1 (even omega), 16 have mu = -1 (odd omega).
# Within each, partition further.
# Could the natural partition be by SUM of digits, or by smallest prime factor?
# ============================================================


def candidate_16_mobius_then_smallest_prime(d, m):
    """mu(d) gives even/odd parity (16+16). Within each, partition by smallest
    prime factor of d (or d=1 special case)."""
    sign = sum(m) % 2  # 0 = mu=+1, 1 = mu=-1
    if d == 1:
        smallest = 0  # special bucket
    else:
        # smallest prime index
        for i, p in enumerate(PRIMES):
            if d % p == 0:
                smallest = i
                break
    # Need a 4-class map from (sign, smallest in 0..4) to l in 0..3.
    # 2 * 5 = 10 classes; we want 4 bins. Use:
    # l = (sign * 2 + (1 if smallest <= 1 else 0)) but check distribution
    return 2 * sign + (0 if smallest <= 1 else 1)


# ============================================================
# Candidate 17: total digit-sum mod 4 (base 10)
# ============================================================


def candidate_17_digit_sum_mod4(d, m):
    return sum(int(c) for c in str(d)) % 4


# ============================================================
# Candidate 18: prime-power class via Mobius + CRT
# Mobius-sign (Z/2) * (d mod 4 in {1, 3}) (Z/2): 4 classes
# ============================================================


def candidate_18_mobius_mod4(d, m):
    sign = sum(m) % 2
    r = d % 4  # for odd d, r in {1, 3}; for even d, r in {0, 2}
    if d % 2 == 0:
        sub = 0 if r == 0 else 1  # 0 or 2
    else:
        sub = 0 if r == 1 else 1
    return 2 * sign + sub


# ============================================================
# Candidate 19: max-prime + Hamming-weight parity (BHML-flavored)
# largest-prime index of d in {0..4} mod 4
# ============================================================


def candidate_19_max_prime_then_hw(d, m):
    if d == 1:
        return 0
    max_idx = 0
    for i in range(5):
        if m[i] == 1:
            max_idx = i
    hw = sum(m)
    # 4-class: 2 * (max_idx >= 3) + (hw % 2)
    return 2 * (1 if max_idx >= 3 else 0) + (hw % 2)


# ============================================================
# Candidate 20: BRUTE-FORCE — try all 5-bit-to-l maps and count matches
# Each of the 32 divisors has 5-bit mask m. A function f: {0,1}^5 -> {0,1,2,3}.
# That's 4^32 ~ 1.8e19 maps total -- too many.
# But functions of the FORM "compute scalar feature(m), then bin" we can
# enumerate over linear forms over GF(2)^5 mod 4, etc.
# ============================================================


def enumerate_linear_mod4():
    """Enumerate all maps m -> (sum_i a_i * m_i) mod 4 for a_i in {0,1,2,3}.
    That's 4^5 = 1024 maps. Plus 4 additive shifts = 4096."""
    divs = divisors_of_2310()
    masks = [m for _, m in divs]
    hits = []
    for a in product(range(4), repeat=5):
        for shift in range(4):
            labels = [(sum(ai * mi for ai, mi in zip(a, mask)) + shift) % 4 for mask in masks]
            dist = tuple(labels.count(l) for l in range(4))
            if dist == TARGET:
                hits.append((a, shift, dist))
    return hits


def enumerate_linear_mod4_general():
    """Enumerate maps m -> f(m) where f is linear mod-4 over a wider range."""
    divs = divisors_of_2310()
    masks = [m for _, m in divs]
    hits = []
    for a in product(range(8), repeat=5):
        labels = [(sum(ai * mi for ai, mi in zip(a, mask))) % 4 for mask in masks]
        dist = tuple(labels.count(l) for l in range(4))
        if dist == TARGET:
            hits.append((a, dist))
    return hits


def enumerate_threshold_maps():
    """Maps of the form m -> bin(threshold) where we threshold a linear functional
    of m into 4 buckets via 3 cut-points."""
    divs = divisors_of_2310()
    masks = [m for _, m in divs]
    hits = []
    # Linear weights in -3..3 for each prime
    weight_range = range(-3, 4)
    print("Brute-force threshold search...")
    count = 0
    for a in product(weight_range, repeat=5):
        scores = [sum(ai * mi for ai, mi in zip(a, mask)) for mask in masks]
        min_s, max_s = min(scores), max(scores)
        if max_s - min_s < 3:
            continue
        # Try all triples of cutpoints
        unique_s = sorted(set(scores))
        if len(unique_s) < 4:
            continue
        # Greedy: any 3 of unique_s -1 can be cutpoints
        for i in range(len(unique_s) - 1):
            for j in range(i + 1, len(unique_s) - 1):
                for k in range(j + 1, len(unique_s)):
                    c0, c1, c2 = unique_s[i], unique_s[j], unique_s[k] - 1
                    if c1 <= c0 or c2 < c1:
                        continue
                    labels = []
                    for s in scores:
                        if s <= c0:
                            labels.append(0)
                        elif s <= c1:
                            labels.append(1)
                        elif s <= c2:
                            labels.append(2)
                        else:
                            labels.append(3)
                    dist = tuple(labels.count(l) for l in range(4))
                    if dist == TARGET:
                        hits.append((a, (c0, c1, c2), dist))
                        count += 1
                        if count >= 20:
                            return hits
    return hits


# ============================================================
# RUN ALL CANDIDATES
# ============================================================


def run():
    divs = divisors_of_2310()
    print(f"Total divisors of 2310: {len(divs)}")
    print(f"Target subshell distribution: {TARGET}")
    print(f"Hamming weight distribution: 1, 5, 10, 10, 5, 1 = (C(5,k))_k")
    print()
    print("=" * 70)

    results = []

    results.append(("C1: sigma-orbit class on d mod 10", check_distribution(candidate_1_sigma_orbit, "C1")))
    results.append(("C2: Hamming weight mod 4", check_distribution(candidate_2_hw_mod4, "C2")))
    results.append(("C2b: Hamming weight signed bins", check_distribution(candidate_2b_hw_signed, "C2b")))
    results.append(("C3: CRT (d mod 2, d mod 11)", check_distribution(candidate_3_crt_2_11, "C3")))
    results.append(("C3b: kernel/strand canonical", check_distribution(candidate_3b_crt_kernel_strand, "C3b")))
    results.append(("C4: pairsum d + N/d mod 32 div 8", check_distribution(candidate_4_pairsum_mod, "C4")))
    results.append(("C7: max prime index", check_distribution(candidate_7_max_prime_idx, "C7")))
    results.append(("C8: min prime index", check_distribution(candidate_8_min_prime_idx, "C8")))
    results.append(("C9: omega mod 4", check_distribution(candidate_9_omega, "C9")))
    results.append(("C11: log2 floor mod 4", check_distribution(candidate_11_log2_floor, "C11")))
    results.append(("C12: popcount + xor", check_distribution(candidate_12_popcount_xor, "C12")))
    results.append(("C13: Legendre count", check_distribution(candidate_13_legendre, "C13")))
    results.append(("C14: kernel-strand canonical", check_distribution(candidate_14_kernel_strand_canonical, "C14")))
    results.append(("C14b: kernel-strand sum mod 4", check_distribution(candidate_14b_kernel_strand_xor, "C14b")))
    results.append(("C15: Pauli ladder l = #outer primes", check_distribution(candidate_15_pauli_ladder, "C15")))
    results.append(("C16: Mobius + smallest-prime", check_distribution(candidate_16_mobius_then_smallest_prime, "C16")))
    results.append(("C17: digit sum mod 4", check_distribution(candidate_17_digit_sum_mod4, "C17")))
    results.append(("C18: Mobius + d mod 4", check_distribution(candidate_18_mobius_mod4, "C18")))
    results.append(("C19: max-prime + hw parity", check_distribution(candidate_19_max_prime_then_hw, "C19")))
    results.append(("C6: Lens (mod10, mod11)", check_distribution(candidate_6_lens_pair, "C6")))

    print()
    print("=" * 70)
    print("BRUTE-FORCE LINEAR-MOD-4 ENUMERATION")
    print("=" * 70)
    hits = enumerate_linear_mod4()
    print(f"  Found {len(hits)} linear-mod-4 maps with sum_i a_i*m_i mod 4 in {{0,1,2,3}}^5")
    for h in hits[:5]:
        print(f"    weights={h[0]}, shift={h[1]}, dist={h[2]}")
    if len(hits) > 5:
        print(f"    ... and {len(hits) - 5} more")

    print()
    hits2 = enumerate_linear_mod4_general()
    print(f"  Found {len(hits2)} linear-mod-4 maps with sum_i a_i*m_i mod 4, a_i in {{0..7}}")
    for h in hits2[:5]:
        print(f"    weights={h[0]}, dist={h[1]}")

    print()
    print("=" * 70)
    print("BRUTE-FORCE LINEAR THRESHOLD MAPS")
    print("=" * 70)
    hits3 = enumerate_threshold_maps()
    print(f"  Found {len(hits3)} threshold maps")
    for h in hits3[:10]:
        print(f"    weights={h[0]}, cutpoints={h[1]}, dist={h[2]}")

    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    matches = [r for r in results if r[1][1]]
    print(f"  Hand-built candidates: {len(results)} tested, {len(matches)} match (2,6,10,14)")
    for name, (dist, m) in results:
        if m:
            print(f"    MATCH: {name} -> {dist}")
    if not matches and not hits and not hits3:
        print("  None of the natural hand-built candidates matched.")
        print("  This is evidence that (2,6,10,14) is a Pascal-type coincidence.")


if __name__ == "__main__":
    run()
