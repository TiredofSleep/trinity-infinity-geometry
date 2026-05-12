"""
verify_J12.py
Copyright (c) 2026 B.R. Sanders and M. Gish.
Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
https://creativecommons.org/licenses/by/4.0/

Self-contained verification of J12:
  "Non-CRT Sufficient Pairs and the Minimum Viable Jump Number
   on Squarefree Z/nZ"

Each check is mapped one-to-one to a load-bearing claim in the manuscript.

  C1  Theorem 1.5 (n=30, family (a)):
        {pi_DYN(7), pi_DYN(11)} is sufficient on Z/30Z by direct enumeration
        of unresolved-pair intersections; the orbits of 1 under T_7 and T_11
        and the coordinate-wise orders match the values quoted at line 178-181.

  C2  Theorem 1.5 (n=30, family (b)):
        {pi_2, pi_15} is sufficient on Z/30Z.

  C3  Theorem 1.5 (n=30, family (c)):
        {pi_SPEC, pi_15} is sufficient on Z/30Z, via the modular argument
        2a == 15 (mod 30) has no solution (gcd(2,30) does not divide 15).

  C4  Theorem 1.4 mechanism (M3) example on Z/42:
        g = 11, h = 13 produces a sufficient orbit-pair on Z/42Z with
        supp(g) = {3, 7}, supp(h) = {7} (mixed mechanism).
        Coordinate-wise orders: ord_3(11)=2, ord_7(11)=3, ord_3(13)=1, ord_7(13)=2.

  C5  Theorem 1.4 smallest-five primes admitting (M2):
        primes p with p - 1 having >= 2 distinct prime factors,
        listed as 7, 11, 13, 19, 23 (then 29, 31, 37, ...), verified through p = 50.

  C6  Worked example on Z/10Z (Proposition 5.3):
        pi_SPEC <= pi_UG <= pi_2, with pi_5 incompatible with each, and
        pi_2 meet pi_5 = pi_disc. Verified by direct enumeration.

  C7  Theorem 7.4 (MVJN = 1, k=2 squarefree case):
        For every squarefree n = p*q with p < q both prime, the family
        {pi_p, pi_q} is a sufficient 2-family with one orthogonal jump.
        Verified for all such n <= 200.

Author lane: B.R. Sanders, M. Gish
License: CC-BY-4.0 (journal-bundled submission script)
Runtime: < 2 s on standard hardware. Dependencies: none (pure stdlib).
"""

import sys
from math import gcd


# ------------------------------------------------------------------ helpers


def title(s):
    print("=" * 70)
    print(s)
    print("=" * 70)


def order_mod(a, n):
    """Multiplicative order of a mod n, or 0 if gcd(a,n) != 1."""
    if gcd(a, n) != 1:
        return 0
    k = 1
    v = a % n
    while v != 1:
        v = (v * a) % n
        k += 1
    return k


def orbit(g, n, start=1):
    """Orbit of start under multiplication by g in Z/nZ."""
    seen = []
    v = start % n
    while v not in seen:
        seen.append(v)
        v = (v * g) % n
    return seen


def orbit_partition(g, n):
    """Partition pi_DYN(g) of Z/nZ into orbits of T_g."""
    seen = set()
    blocks = []
    for x in range(n):
        if x in seen:
            continue
        b = []
        v = x
        while v not in seen:
            b.append(v)
            seen.add(v)
            v = (v * g) % n
        blocks.append(frozenset(b))
    return blocks


def residue_partition(d, n):
    """Partition pi_d of Z/nZ into residue classes mod d (d | n)."""
    blocks = {}
    for x in range(n):
        blocks.setdefault(x % d, []).append(x)
    return [frozenset(b) for b in blocks.values()]


def spec_partition(n):
    """Reflection partition pi_SPEC of Z/nZ: blocks {x, n-x}."""
    seen = set()
    blocks = []
    for x in range(n):
        if x in seen:
            continue
        b = {x, (n - x) % n}
        blocks.append(frozenset(b))
        seen |= b
    return blocks


def block_of(P, x):
    """Block of partition P containing x."""
    for b in P:
        if x in b:
            return b
    raise ValueError(f"element {x} not in partition")


def is_sufficient(parts, n):
    """A partition family is sufficient iff its meet is discrete:
    no two distinct elements share a block in every partition."""
    for x in range(n):
        for y in range(x + 1, n):
            if all(y in block_of(P, x) for P in parts):
                return False
    return True


def incompatible(P1, P2):
    """Two partitions are incompatible iff neither refines the other."""
    def refines(A, B):
        for ba in A:
            if not any(ba <= bb for bb in B):
                return False
        return True
    return not refines(P1, P2) and not refines(P2, P1)


def is_prime(p):
    if p < 2:
        return False
    for q in range(2, int(p ** 0.5) + 1):
        if p % q == 0:
            return False
    return True


def distinct_prime_factors(m):
    primes = set()
    p = 2
    while p * p <= m:
        while m % p == 0:
            primes.add(p)
            m //= p
        p += 1
    if m > 1:
        primes.add(m)
    return primes


def gcd_class_partition_n10():
    """The pi_UG partition on Z/10Z: blocks indexed by gcd(x, 10)."""
    blocks = {}
    for x in range(10):
        blocks.setdefault(gcd(x, 10), []).append(x)
    return [frozenset(b) for b in blocks.values()]


# ------------------------------------------------------------------ checks


def check_C1():
    title("C1: Theorem 1.5(a) -- {pi_DYN(7), pi_DYN(11)} sufficient on Z/30Z")
    n = 30
    P7 = orbit_partition(7, n)
    P11 = orbit_partition(11, n)
    # orbits of 1
    o7 = orbit(7, n, 1)
    o11 = orbit(11, n, 1)
    assert sorted(o7) == [1, 7, 13, 19], f"orbit(7) wrong: {sorted(o7)}"
    assert sorted(o11) == [1, 11], f"orbit(11) wrong: {sorted(o11)}"
    print(f"  orbit of 1 under T_7  : {o7}  (expected [1, 7, 19, 13])")
    print(f"  orbit of 1 under T_11 : {o11}  (expected [1, 11])")
    # coordinate-wise orders
    expected_orders = {
        (7, 2): 1, (7, 3): 1, (7, 5): 4,
        (11, 2): 1, (11, 3): 2, (11, 5): 1,
    }
    for (g, p), want in expected_orders.items():
        got = order_mod(g, p)
        assert got == want, f"ord_{p}({g}) = {got}, expected {want}"
        print(f"  ord_{p}({g}) = {got}  (expected {want})")
    # coordinate-wise gcds of orders all equal 1 -> Theorem 1.3 -> sufficient
    for p in (2, 3, 5):
        g = gcd(order_mod(7, p), order_mod(11, p))
        assert g == 1
    # direct enumeration
    suff = is_sufficient([P7, P11], n)
    assert suff, "pair {pi_DYN(7), pi_DYN(11)} should be sufficient"
    print(f"  sufficient by direct enumeration: {suff}")
    # incompatible (orthogonal jump = 1)
    assert incompatible(P7, P11), "should be incompatible"
    print(f"  incompatible (one orthogonal jump): True")
    print("  PASS")


def check_C2():
    title("C2: Theorem 1.5(b) -- {pi_2, pi_15} sufficient on Z/30Z")
    n = 30
    P2 = residue_partition(2, n)
    P15 = residue_partition(15, n)
    suff = is_sufficient([P2, P15], n)
    assert suff
    incomp = incompatible(P2, P15)
    assert incomp
    print(f"  sufficient: {suff}")
    print(f"  incompatible: {incomp}")
    print("  PASS")


def check_C3():
    title("C3: Theorem 1.5(c) -- {pi_SPEC, pi_15} sufficient on Z/30Z")
    n = 30
    P_spec = spec_partition(n)
    P15 = residue_partition(15, n)
    suff = is_sufficient([P_spec, P15], n)
    assert suff
    incomp = incompatible(P_spec, P15)
    assert incomp
    # verify the modular argument: 2a == 15 (mod 30) has no solution
    # because gcd(2, 30) = 2 does not divide 15
    solns = [a for a in range(n) if (2 * a) % n == 15 % n]
    assert solns == [], f"unexpected solutions to 2a == 15 (mod 30): {solns}"
    print(f"  sufficient: {suff}")
    print(f"  incompatible: {incomp}")
    print(f"  2a == 15 (mod 30) has solutions: {solns}  (expected [])")
    print(f"  gcd(2, 30) = {gcd(2, 30)} does not divide 15: consistent")
    print("  PASS")


def check_C4():
    title("C4: Theorem 1.4 (M3) -- {pi_DYN(11), pi_DYN(13)} on Z/42")
    n = 42
    # orders at coordinate primes 3 and 7
    expected = {(11, 3): 2, (11, 7): 3, (13, 3): 1, (13, 7): 2}
    for (g, p), want in expected.items():
        got = order_mod(g, p)
        assert got == want, f"ord_{p}({g}) = {got}, expected {want}"
        print(f"  ord_{p}({g}) = {got}  (expected {want})")
    # gcds
    for p in (2, 3, 7):
        g = gcd(order_mod(11, p), order_mod(13, p))
        assert g == 1, f"gcd at p={p} should be 1, got {g}"
    P11 = orbit_partition(11, n)
    P13 = orbit_partition(13, n)
    suff = is_sufficient([P11, P13], n)
    assert suff
    print(f"  sufficient on Z/42: {suff}")
    # supports
    supp_11 = {p for p in (2, 3, 7) if (11 % p) != 1 % p}
    supp_13 = {p for p in (2, 3, 7) if (13 % p) != 1 % p}
    print(f"  supp(11) = {sorted(supp_11)}  (expected {{3, 7}})")
    print(f"  supp(13) = {sorted(supp_13)}  (expected {{7}})")
    assert supp_11 == {3, 7}
    assert supp_13 == {7}
    # mechanism is M3 (mixed: supports differ, both non-empty, supp(11) multi-element)
    print("  mechanism: M3 (mixed)")
    print("  PASS")


def check_C5():
    title("C5: Theorem 1.4 -- smallest primes admitting (M2)")
    lst = []
    for p in range(2, 51):
        if is_prime(p) and len(distinct_prime_factors(p - 1)) >= 2:
            lst.append(p)
    expected_first_5 = [7, 11, 13, 19, 23]
    expected_next = 29
    assert lst[:5] == expected_first_5, f"first five mismatch: {lst[:5]}"
    assert lst[5] == expected_next, f"sixth element mismatch: {lst[5]}"
    print(f"  smallest five (p <= 50): {lst[:5]}  (expected {expected_first_5})")
    print(f"  next: {lst[5]}  (expected {expected_next})")
    print(f"  full list through p = 50: {lst}")
    # note: 17 is correctly skipped (16 = 2^4, single prime factor)
    assert 17 not in lst
    print("  17 correctly skipped (16 = 2^4, single prime factor)")
    print("  PASS")


def check_C6():
    title("C6: Proposition 5.3 -- partition lattice on Z/10Z")
    n = 10
    P_dyn3 = orbit_partition(3, n)
    P_ug = gcd_class_partition_n10()
    P_spec = spec_partition(n)
    P_2 = residue_partition(2, n)
    P_5 = residue_partition(5, n)
    # Lemma 5.2: pi_DYN(3) == pi_UG
    assert set(P_dyn3) == set(P_ug), "pi_DYN(3) should equal pi_UG on Z/10Z"
    print("  Lemma 5.2: pi_DYN(3) = pi_UG  (verified)")

    # (a) refinement chain pi_SPEC <= pi_UG <= pi_2
    def refines(A, B):
        for ba in A:
            if not any(ba <= bb for bb in B):
                return False
        return True

    assert refines(P_spec, P_ug), "pi_SPEC should refine pi_UG"
    assert refines(P_ug, P_2), "pi_UG should refine pi_2"
    print("  (a) pi_SPEC <= pi_UG <= pi_2  (verified)")
    # (b) incompatibility of pi_5 with each
    for name, P in [("pi_2", P_2), ("pi_UG", P_ug), ("pi_SPEC", P_spec)]:
        assert incompatible(P_5, P), f"pi_5 should be incompatible with {name}"
        print(f"      pi_5 incompatible with {name}  (verified)")
    # (c) pi_2 meet pi_5 = pi_disc
    assert is_sufficient([P_2, P_5], n)
    print("  (c) pi_2 meet pi_5 = pi_disc  (verified)")
    print("  PASS")


def check_C7():
    title("C7: Theorem 7.4 -- MVJN = 1 for all squarefree n with k >= 2 primes")
    # check all squarefree n <= 200 with k = 2 distinct primes
    tested = 0
    for n in range(6, 201):
        primes = distinct_prime_factors(n)
        # squarefree iff product of distinct primes equals n
        prod = 1
        for p in primes:
            prod *= p
        if prod != n or len(primes) < 2:
            continue
        # construction: {pi_p1, pi_{n/p1}}
        plist = sorted(primes)
        p1 = plist[0]
        d = n // p1
        Pp1 = residue_partition(p1, n)
        Pd = residue_partition(d, n)
        # must be sufficient and incompatible
        assert is_sufficient([Pp1, Pd], n), f"family for n={n} not sufficient"
        assert incompatible(Pp1, Pd), f"family for n={n} not incompatible"
        tested += 1
    print(f"  verified MVJN(Z/n) = 1 construction for {tested} squarefree n <= 200")
    print("  (every such n: {pi_p1, pi_{n/p1}} is sufficient and incompatible)")
    print("  PASS")


def main():
    title("J12 verification: Non-CRT Sufficient Pairs and MVJN on Squarefree Z/nZ")
    print("Sanders & Gish, 2026. CC-BY-4.0.\n")
    checks = [check_C1, check_C2, check_C3, check_C4, check_C5, check_C6, check_C7]
    for c in checks:
        c()
        print()
    title("ALL 7 CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
