#!/usr/bin/env python3
"""
F2 extended — additional natural candidates motivated by TIG substrate structure.

We've shown no natural low-complexity bit-function f: {0,1}^5 -> {0,1,2,3}
matches the (2, 6, 10, 14) target. This file tests SUBSTRATE-MOTIVATED maps
that use d itself (not just its mask), invoking the TIG vocabulary.
"""
from __future__ import annotations
from itertools import combinations, product
from math import prod, gcd
from collections import Counter

PRIMES = [2, 3, 5, 7, 11]
N = 2310
TARGET = (2, 6, 10, 14)


def divisors_with_masks():
    divs = []
    for k in range(6):
        for subset in combinations(PRIMES, k):
            d = prod(subset) if subset else 1
            mask = tuple(1 if p in subset else 0 for p in PRIMES)
            divs.append((d, mask))
    return sorted(divs)


def check(label_fn, name):
    divs = divisors_with_masks()
    skipped = 0
    counts = Counter()
    for d, m in divs:
        l = label_fn(d, m)
        if l is None or l < 0 or l > 3:
            skipped += 1
        else:
            counts[l] += 1
    dist = tuple(counts.get(l, 0) for l in range(4))
    match = dist == TARGET and skipped == 0
    print(f"[{name}] {dist}, skipped {skipped}, match: {match}")
    return dist, match


# Candidate 21: # of distinct prime factors in d that are <= 5
def c21(d, m):
    """omega_inner = number of inner primes (<=5) dividing d. In {0,1,2,3}."""
    return sum(1 for p in [2, 3, 5] if d % p == 0)


# Candidate 22: # of distinct prime factors in d that are >= 7
def c22(d, m):
    """omega_outer = number of outer primes (>=7) dividing d. In {0,1,2}.
    Pad to 4 by parity of d."""
    outer = sum(1 for p in [7, 11] if d % p == 0)
    return min(outer * 2 + (d % 2 == 0), 3)


# Candidate 23: Floor of (log_2 d / log_2 N) scaled to 4 bins
def c23(d, m):
    import math
    if d == 1:
        return 0
    ratio = math.log(d) / math.log(N)
    return min(int(ratio * 4), 3)


# Candidate 24: Map d to (d-1) mod 11 // 3 (only valid for d coprime to 11;
# i.e., d not divisible by 11). Try a partial map and see distribution.
def c24(d, m):
    if d % 11 == 0:
        return None
    return ((d - 1) % 11) // 3


# Candidate 25: Quadratic residue class mod 7 (squarefree d, exclude d=7,14,21,...)
def c25(d, m):
    if d % 7 == 0:
        return None
    sq = pow(d, 3, 7)  # by Euler, this is +-1
    return 0 if sq == 1 else 1


# Candidate 26: d mod 16 // 4  (4 buckets)
def c26(d, m):
    return (d % 16) // 4


# Candidate 27: ord_2(N/d) when defined — i.e., 2-adic valuation
def c27(d, m):
    """N/d. v_2(N/d): in {0, 1}. Repeat for v_3(N/d)... combine into 4 bins."""
    q = N // d
    a = (1 if q % 2 == 0 else 0)
    b = (1 if q % 3 == 0 else 0)
    return 2 * a + b


# Candidate 28: K12 lattice depth — distance from 1 in divisor lattice (= Hamming weight)
# but classify in 4 bins
def c28(d, m):
    h = sum(m)
    # 4-bin map: 0 -> 0, 1 -> 1, 2-3 -> 2, 4-5 -> 3
    if h == 0:
        return 0
    if h == 1:
        return 1
    if h <= 3:
        return 2
    return 3


# Candidate 29: divisor lattice meet/join — meets every other divisor and counts
def c29(d, m):
    """Number of OTHER divisors that divide d (or d divides them) and the difference is exactly one prime."""
    # This is just (sum of m) + (5 - sum of m) = 5 for all d. Useless.
    return None


# Candidate 30: Strand-prime parity & kernel-prime parity
# (kernel = {2,5}, strand = {3,7,11})
def c30(d, m):
    k = m[0] + m[2]  # kernel
    s = m[1] + m[3] + m[4]  # strand
    return 2 * (k % 2) + (s % 2)


# Candidate 31: outer-prime weighted sum
def c31(d, m):
    # weights: prime - 1
    score = sum((p - 1) * mi for p, mi in zip(PRIMES, m))
    # min=0 (d=1), max=1+2+4+6+10=23 (d=N). 4 bins by quartile cutpoints
    cuts = [3, 8, 15]
    for i, c in enumerate(cuts):
        if score <= c:
            return i
    return 3


# Candidate 32: Pauli-style direct via Jacobi-symbol-like aggregator
def c32(d, m):
    """Use d mod 11 (since 11 is the largest substrate prime).
    Map (d mod 11) into 4 bins by orbit class."""
    r = d % 11
    if r == 0:
        return 0
    # quad residues mod 11: {1,3,4,5,9} -> bin 1; non-residues {2,6,7,8,10} -> bin 2
    # Plus residue r=1 -> bin 0
    if r == 1:
        return 0
    qr11 = {1, 3, 4, 5, 9}
    if r in qr11:
        return 1
    return 2
    # Bins 0,1,2 only; need 4. Doesn't work as 4-bin.


# Candidate 33: σ-orbit class on Z/11Z lifted to divisor
# In Z/11Z, multiplicative group is cyclic of order 10. σ acts as multiplication
# by a primitive root, e.g., 2. Orbits under <2>: just one orbit of size 10 (plus 0).
# Less useful.

# Candidate 34: divisor d's image in (Z/2Z) x (Z/5Z) under CRT (Z/10Z dual)
def c34(d, m):
    a = d % 2
    b = d % 5
    # 2 * 5 = 10 classes; map to 4 by:
    return min(a * 2 + (b // 2), 3)


# Candidate 35: count of primes p such that d^2 = 1 (mod p) for substrate primes
def c35(d, m):
    """Count substrate primes p where d^2 mod p == 1 (i.e., d == ±1 mod p)."""
    count = 0
    for p in PRIMES:
        if d % p == 0:
            continue
        if (d * d) % p == 1:
            count += 1
    return min(count, 3)


# Candidate 36: lift to canonical TSML cell — TIG uses tau = (1,0)(2,3)(4,5)(6,7)(8,9)
# on Z/10Z; assign d -> cell color.
# Define: tau orbits = {0}, {1}, {2,3}, {4,5}, {6,7}, {8,9}
def c36(d, m):
    r = d % 10
    if r in (0,):
        return 0
    if r in (1,):
        return 0
    if r in (2, 3):
        return 1
    if r in (4, 5):
        return 2
    return 3  # 6, 7, 8, 9


# Candidate 37: Mertens-function-style — (-1)^omega * 1_squarefree
def c37(d, m):
    # All divisors of 2310 are squarefree. mu = (-1)^omega.
    sign = sum(m) % 2  # 0 or 1
    # And further split by some d-mod feature
    extra = d % 3  # 0, 1, or 2
    return min(2 * sign + (0 if extra == 0 else 1), 3)


# Candidate 38: divisor d's index in lexicographic order
def c38(d, m):
    divs = divisors_with_masks()
    idx = sorted(divs).index((d, m))
    return idx // 8


# Candidate 39: Generalized Pauli — interpret (d mod 11, d mod 7, d mod 5, d mod 3, d mod 2)
# as a five-fold quantum number. Specifically, l = number of components equal to 1.
def c39(d, m):
    """Count number of substrate primes for which d mod p == 1."""
    return min(sum(1 for p in PRIMES if d % p == 1), 3)


# Candidate 40: (d mod 3) gives a Z/3 quantum number; combine with v_2(d) parity
def c40(d, m):
    r3 = d % 3
    v2 = m[0]  # 0 if d odd, 1 if d even
    # 3 * 2 = 6 classes; bin to 4
    raw = 2 * v2 + (r3 % 2)
    return min(raw + (r3 // 2), 3)


if __name__ == "__main__":
    print("=" * 70)
    print("EXTENDED SUBSTRATE-MOTIVATED CANDIDATES")
    print("=" * 70)
    print(f"Target: {TARGET}")
    print()

    matches = []
    for fn, name in [
        (c21, "C21: #inner-primes (<=5)"),
        (c22, "C22: outer-primes + parity"),
        (c23, "C23: log(d)/log(N) quartile"),
        (c24, "C24: (d-1) mod 11 // 3 (partial)"),
        (c25, "C25: QR mod 7 (partial)"),
        (c26, "C26: d mod 16 // 4"),
        (c27, "C27: v_2(N/d), v_3(N/d)"),
        (c28, "C28: Hamming weight 4-bin"),
        (c30, "C30: kernel|strand parities"),
        (c31, "C31: weighted (p-1) score"),
        (c34, "C34: CRT (mod 2, mod 5) 4-bin"),
        (c35, "C35: #primes where d^2 == 1 mod p"),
        (c36, "C36: tau-orbit class on Z/10"),
        (c37, "C37: mu(d) + d mod 3"),
        (c38, "C38: lex index // 8"),
        (c39, "C39: #primes where d == 1 mod p"),
        (c40, "C40: d mod 3 + v_2"),
    ]:
        dist, m = check(fn, name)
        if m:
            matches.append(name)

    print()
    print("=" * 70)
    if matches:
        print(f"FRONTIER POSITIVE: {len(matches)} matches found.")
        for name in matches:
            print(f"  {name}")
    else:
        print("No additional natural candidates match the target distribution.")
        print("Combined with F2_candidates.py (20 hand-built) and F2_coincidence_bound.py")
        print("(0/4096 linear-mod-4, 0/24576 perm-linear, 0/4096 symmetric,")
        print("0 2-bit and 3-bit dictators, 0 quadratic+linear), the verdict is:")
        print()
        print("  CONCLUSION: The 32 = 32 equality has NO natural bijection.")
        print("  It is a Pascal-type coincidence (binomial C(5,k) sum = 32,")
        print("  Pauli triangular 2*(2l+1) sum = 32).")
