#!/usr/bin/env python3
"""
Verification script for "Joint Injectivity of Additive-Quotient and
Multiplicative-Orbit Partitions on Z/nZ" (Sanders, Gish, 2026).

Verifies, by direct enumeration on small cases:

  Examples 1, 2 (failure of the natural prime-action conjecture for
                 joint(A_d, orb_g) on Z/nZ):
    - (n, d, g) = (6, 3, 5): jointly injective, yet g = 5 satisfies
      g mod 2 = 1 (the condition "g_j != 1 mod p_j for every
      p_j | (n/d)" fails since n/d = 2).
    - (n, d, g) = (6, 2, 5): not jointly injective, yet g = 5
      satisfies g mod 3 = 2 != 1 (the condition holds; converse
      direction fails).

  Theorem 3.3 (Sufficient condition via order-equality, on units):
    If (i) g_j != 1 mod p_j for every p_j | (n/d) AND
       (ii) ord(g mod d) = ord(g mod n),
    then joint(A_d, orb_g) is injective on (Z/nZ)*.

  Theorem 4.1 (M+M classification on units):
    For squarefree n with omega(n) >= 2 and g, h in (Z/nZ)*:
    joint(orb_g, orb_h) is injective on (Z/nZ)*
    iff <g> intersect <h> = {1}.

  Theorem 5.1 (SPEC + DYN):
    For squarefree n with omega(n) >= 2 and g in (Z/nZ)*:
    joint(pi_SPEC, orb_g) is injective on Z/nZ
    iff -1 is not in <g mod p> for every odd prime p | n.

  Theorem 6.1 (no joint-injective pair for prime powers, non-identity g):
    For n = p^r with r >= 2, every g != 1 in (Z/p^r Z)*, every
    1 <= a < r: joint(A_{p^a}, orb_g) is NOT injective on Z/p^r Z.

Source bundle: J06 manuscript verification.

Copyright 2026 Brayden R. Sanders and M. Gish.
Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
DOI: 10.5281/zenodo.18852047
"""
from math import gcd
from itertools import product


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------
def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def is_squarefree(n):
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def prime_factors_sorted(n):
    pf = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            pf.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        pf.append(m)
    return sorted(pf)


def divisors(n):
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
        i += 1
    return sorted(out)


def units_mod(n):
    return [g for g in range(1, n) if gcd(g, n) == 1]


def cyclic_subgroup(g, n):
    out = set()
    h = 1 % n
    while True:
        if h in out:
            break
        out.add(h)
        h = (h * g) % n
    return out


def ord_mod(g, n):
    if n <= 1:
        return 1
    if gcd(g % n, n) != 1:
        return -1
    h = 1 % n
    for t in range(1, n + 1):
        h = (h * g) % n
        if h == 1:
            return t
    return -1


def orbit_partition(g, n):
    seen = set()
    blocks = []
    for x in range(n):
        if x in seen:
            continue
        orb = []
        y = x
        while y not in seen:
            seen.add(y)
            orb.append(y)
            y = (g * y) % n
        blocks.append(tuple(sorted(orb)))
    return blocks


def orbit_partition_units(g, n):
    units = units_mod(n)
    H = cyclic_subgroup(g, n)
    cosets = []
    seen = set()
    for x in units:
        if x in seen:
            continue
        coset = sorted(set((x * h) % n for h in H))
        cosets.append(tuple(coset))
        for y in coset:
            seen.add(y)
    return cosets


def additive_partition(d, n):
    blocks = [[] for _ in range(d)]
    for x in range(n):
        blocks[x % d].append(x)
    return [tuple(b) for b in blocks]


def additive_partition_units(d, n):
    units = units_mod(n)
    blocks_dict = {}
    for x in units:
        r = x % d
        blocks_dict.setdefault(r, []).append(x)
    return [tuple(b) for b in blocks_dict.values()]


def reflection_partition(n):
    seen = set()
    blocks = []
    for x in range(n):
        if x in seen:
            continue
        y = (-x) % n
        if x == y:
            blocks.append((x,))
            seen.add(x)
        else:
            blocks.append(tuple(sorted([x, y])))
            seen.add(x)
            seen.add(y)
    return blocks


def joint_discrete_on(part1, part2, support):
    L1, L2 = {}, {}
    for i, b in enumerate(part1):
        for x in b:
            L1[x] = i
    for i, b in enumerate(part2):
        for x in b:
            L2[x] = i
    seen = set()
    for x in support:
        if x not in L1 or x not in L2:
            continue
        k = (L1[x], L2[x])
        if k in seen:
            return False
        seen.add(k)
    return True


# ---------------------------------------------------------------------
# Examples 1, 2: confirm the natural prime-action conjecture fails in
# both directions on the full ring Z/nZ.
# ---------------------------------------------------------------------
def verify_examples_falsifying_natural_conjecture():
    print("=" * 60)
    print("Examples 1, 2: natural prime-action conjecture fails in")
    print("               both directions on Z/nZ")
    print("=" * 60)
    fails = 0

    # Example 1: (n, d, g) = (6, 3, 5).
    # n/d = 2; g mod 2 = 1 (condition fails); joint should be injective.
    n, d, g = 6, 3, 5
    ad = additive_partition(d, n)
    op = orbit_partition(g, n)
    pf_n_over_d = prime_factors_sorted(n // d)
    cond_c = all(g % p != 1 for p in pf_n_over_d)
    joint = joint_discrete_on(ad, op, range(n))
    expected_cond = False  # g mod 2 == 1
    expected_joint = True
    print(f"  Ex.1  (n,d,g)=({n},{d},{g}):  cond_c={cond_c} (want {expected_cond}),"
          f"  joint={joint} (want {expected_joint})")
    if cond_c != expected_cond or joint != expected_joint:
        fails += 1
        print(f"    FAIL: did not match expected falsifying behavior")

    # Example 2: (n, d, g) = (6, 2, 5).
    # n/d = 3; g mod 3 = 2 != 1 (condition holds); joint should NOT be
    # injective (orbit {1,5} lies inside A_2-fiber {1,3,5}).
    n, d, g = 6, 2, 5
    ad = additive_partition(d, n)
    op = orbit_partition(g, n)
    pf_n_over_d = prime_factors_sorted(n // d)
    cond_c = all(g % p != 1 for p in pf_n_over_d)
    joint = joint_discrete_on(ad, op, range(n))
    expected_cond = True   # g mod 3 != 1
    expected_joint = False
    print(f"  Ex.2  (n,d,g)=({n},{d},{g}):  cond_c={cond_c} (want {expected_cond}),"
          f"  joint={joint} (want {expected_joint})")
    if cond_c != expected_cond or joint != expected_joint:
        fails += 1
        print(f"    FAIL: did not match expected falsifying behavior")

    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 2: sufficient condition via order-equality (on units)
# ---------------------------------------------------------------------
def verify_theorem_2_sufficient():
    print("=" * 60)
    print("Theorem 2: sufficient condition (cond_c + ord-equality) on units")
    print("=" * 60)
    sf_ns = [n for n in range(6, 80) if is_squarefree(n)
             and len(prime_factors_sorted(n)) >= 2]
    fails = 0
    n_checks = 0
    for n in sf_ns:
        for d in divisors(n):
            if d == 1 or d == n:
                continue
            ad_u = additive_partition_units(d, n)
            n_over_d = n // d
            pf_n_over_d = prime_factors_sorted(n_over_d)
            for g in units_mod(n):
                cond_c = all(g % p != 1 for p in pf_n_over_d)
                if not cond_c:
                    continue
                ord_d = ord_mod(g, d)
                ord_n = ord_mod(g, n)
                if ord_d != ord_n:
                    continue
                # Both hypotheses hold; check sufficiency on units
                n_checks += 1
                ou = orbit_partition_units(g, n)
                joint_units = joint_discrete_on(ad_u, ou, units_mod(n))
                if not joint_units:
                    fails += 1
                    if fails < 3:
                        print(f"  FAIL n={n}, d={d}, g={g}: hypotheses hold, but joint on units fails")
    print(f"  total (n, d, g) cases where hypotheses hold: {n_checks}")
    print(f"  sufficiency violations: {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 3: M+M classification on units
# ---------------------------------------------------------------------
def verify_theorem_3_mm_units():
    print("=" * 60)
    print("Theorem 3: M+M classification on units")
    print("=" * 60)
    sf_ns = [n for n in range(6, 36) if is_squarefree(n)
             and len(prime_factors_sorted(n)) >= 2]
    fails = 0
    n_checks = 0
    for n in sf_ns:
        units = units_mod(n)
        for g, h in product(units, units):
            n_checks += 1
            inter = cyclic_subgroup(g, n) & cyclic_subgroup(h, n)
            cond = (inter == {1 % n})
            actual = joint_discrete_on(orbit_partition_units(g, n),
                                        orbit_partition_units(h, n),
                                        units)
            if cond != actual:
                fails += 1
                if fails < 3:
                    print(f"  FAIL n={n}, g={g}, h={h}: cond={cond}, actual={actual}")
    print(f"  squarefree n tested: {sf_ns}")
    print(f"  total (n, g, h) cases: {n_checks}")
    print(f"  counterexamples:       {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 4: SPEC + DYN
# ---------------------------------------------------------------------
def verify_theorem_4_specdyn():
    print("=" * 60)
    print("Theorem 4: SPEC + DYN classification on Z/nZ")
    print("=" * 60)
    sf_ns = [15, 21, 33, 35, 39, 51, 55, 57, 65, 69, 77]
    fails = 0
    n_checks = 0
    for n in sf_ns:
        if not is_squarefree(n):
            continue
        units = units_mod(n)
        odd_primes = [p for p in prime_factors_sorted(n) if p > 2]
        spec = reflection_partition(n)
        for g in units:
            n_checks += 1
            cond = all(((-1) % p) not in cyclic_subgroup(g % p, p) for p in odd_primes)
            actual = joint_discrete_on(spec, orbit_partition(g, n), range(n))
            if cond != actual:
                fails += 1
                if fails < 3:
                    print(f"  FAIL n={n}, g={g}: cond={cond}, actual={actual}")
    print(f"  squarefree n tested: {sf_ns}")
    print(f"  total (n, g) cases: {n_checks}")
    print(f"  counterexamples:    {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 5: prime-power obstruction (non-identity g)
# ---------------------------------------------------------------------
def verify_theorem_5_pkernel():
    print("=" * 60)
    print("Theorem 5: prime-power obstruction (non-identity g)")
    print("=" * 60)
    cases = [(2, 2), (2, 3), (3, 2), (5, 2), (3, 3),
             (2, 4), (5, 3), (7, 2)]
    surprise = 0
    n_checks = 0
    for p, r in cases:
        n = p ** r
        units = units_mod(n)
        for a in range(1, r):
            d = p ** a
            ad = additive_partition(d, n)
            for g in units:
                if g == 1:
                    continue  # exclude identity (degenerate)
                n_checks += 1
                ou = orbit_partition(g, n)
                if joint_discrete_on(ad, ou, range(n)):
                    surprise += 1
                    if surprise < 3:
                        print(f"  SURPRISE n={n}, d={d}, g={g}: jointly injective!")
    print(f"  prime-power n tested: {[p ** r for p, r in cases]}")
    print(f"  total (n, d, g) cases (g != 1): {n_checks}")
    print(f"  jointly-injective surprises: {surprise} (expected: 0)")
    print(f"  result: {'PASS' if surprise == 0 else 'FAIL'}")
    print()
    return surprise == 0


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print()
    print("=" * 72)
    print("  Verification: Joint Injectivity of Additive-Quotient and")
    print("                Multiplicative-Orbit Partitions on Z/nZ")
    print("                (Sanders, Gish, 2026)")
    print("=" * 72)
    print()

    results = [
        verify_examples_falsifying_natural_conjecture(),
        verify_theorem_2_sufficient(),
        verify_theorem_3_mm_units(),
        verify_theorem_4_specdyn(),
        verify_theorem_5_pkernel(),
    ]

    print("=" * 72)
    n_pass = sum(1 for r in results if r)
    print(f"  OVERALL: {n_pass} / {len(results)} verifications passed")
    print("=" * 72)
    print()
    if n_pass == len(results):
        print("  ALL ASSERTIONS PASSED.")
    else:
        print(f"  FAILURES: {len(results) - n_pass}")
    print()
