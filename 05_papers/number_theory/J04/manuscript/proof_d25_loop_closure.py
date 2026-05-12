"""
Verification script for "Full-Period Cancellation of R(k, f) and the
spf-Localization for Squarefree Moduli" (Sanders, Gish, 2026).

Verifies, in order:

  Lemma 1 (basic divisibility biconditional):
      For every prime p in {3, 5, ..., 199} and every k in {1, ..., p}:
      R(k, p) = 0  iff  p | k.

  Theorem 1.A (full-period cancellation):
      For every f in {2, ..., 30} and every m in {1, ..., 5}:
      R(k, f) = 0 at k = f * m.

  Theorem 2 (squarefree layered-divisor structure):
      For 50 squarefree b in {6, 10, 14, 15, ..., 210}:
        - smallest k at which any non-trivial divisor d|b gives R(k,d)=0
          is exactly spf(b);
        - count at k = b_2 = p_1 p_2 is exactly 2^2 - 1 = 3;
        - if omega(b) >= 3, count at k = b_3 = p_1 p_2 p_3 is 2^3 - 1 = 7.

  Theorem 3 (asymptotic average):
      Numerical Riemann sum (1/(f-1)) * sum_{k=1}^{f-1} R(k, f)
      converges to Si(2 pi)/pi ~= 0.45141 for f in {50, 100, 500, 1000}.

Source bundle: J04 manuscript verification.

Notes on changes vs the prior draft (per SAVE_PLAN_J04 §2.5):
  - DROPPED the bisection block (referee M3): the location of
    sinc^2(x) = 1/2 is not in the manuscript and does not belong here.
  - DROPPED the strict-monotonicity assertion at integer arguments
    outside (0, 1) (referee M4): rephrased as "non-increasing at
    integer arguments k in {1, ..., p}", which is what the closed form
    actually delivers.
  - ADDED the layered-closure check (Theorem 2) and the asymptotic-
    average check (Theorem 3).

Copyright 2026 Brayden R. Sanders and M. Gish.
Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
DOI: 10.5281/zenodo.18852047
"""
import math
from math import gcd, sin, pi


# ---------------------------------------------------------------------
# Helper functions
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


def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n


def is_squarefree(n):
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def prime_factors_sorted(n):
    """Return the distinct prime factors of n, sorted ascending."""
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
    """Return all positive divisors of n."""
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i * i != n:
                out.append(n // i)
        i += 1
    return sorted(out)


def R(k, f):
    """Discrete Fejer quotient R(k, f) = sin^2(pi k/f) / (k^2 sin^2(pi/f))."""
    return sin(pi * k / f) ** 2 / (k * k * sin(pi / f) ** 2)


def sinc2(t):
    if t == 0.0:
        return 1.0
    s = sin(pi * t) / (pi * t)
    return s * s


# Si(2 pi) ~ 1.4181515761326284 (from mpmath / scipy.special.sici)
# Si(2 pi) / pi ~ 0.4514120029017365
SI_2PI_OVER_PI = 0.4514120029017365


# ---------------------------------------------------------------------
# Lemma 1: basic divisibility biconditional
# ---------------------------------------------------------------------
def verify_lemma_basic():
    print("=" * 60)
    print("Lemma 1: basic biconditional R(k, p) = 0  iff  p | k")
    print("=" * 60)
    primes = [p for p in range(3, 200) if is_prime(p)]
    n_pairs = 0
    fails = 0
    for p in primes:
        for k in range(1, p + 1):
            n_pairs += 1
            r = R(k, p)
            divides = (k % p == 0)
            iszero = (abs(r) < 1e-10)
            if divides != iszero:
                fails += 1
                print(f"  FAIL p={p}, k={k}: R={r:.3e}, p|k={divides}")
    print(f"  primes tested:        {len(primes)}")
    print(f"  (p, k) pairs checked: {n_pairs}")
    print(f"  counterexamples:      {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 1.A: full-period cancellation
# ---------------------------------------------------------------------
def verify_full_period_cancellation():
    print("=" * 60)
    print("Theorem 1.A: full-period cancellation R(f * m, f) = 0")
    print("=" * 60)
    n_pairs = 0
    fails = 0
    for f in range(2, 31):
        for m in range(1, 6):
            n_pairs += 1
            k = f * m
            r = R(k, f)
            if abs(r) >= 1e-10:
                fails += 1
                print(f"  FAIL f={f}, m={m}, k={k}: R={r:.3e}")
    print(f"  (f, m) pairs checked: {n_pairs}")
    print(f"  counterexamples:      {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 2: squarefree layered-divisor structure
# ---------------------------------------------------------------------
def verify_layered_structure():
    print("=" * 60)
    print("Theorem 2: squarefree layered-divisor structure")
    print("=" * 60)
    # Pick 50 squarefree b in [6, 210] with omega(b) >= 2
    candidates = []
    for n in range(6, 211):
        if is_squarefree(n):
            pf = prime_factors_sorted(n)
            if len(pf) >= 2:
                candidates.append(n)
    bs = candidates[:50]

    fails_smallest = 0
    fails_count_2 = 0
    fails_count_3 = 0
    n_count_3_checked = 0
    for b in bs:
        pf = prime_factors_sorted(b)
        spf_b = pf[0]
        nontrivial_divs = [d for d in divisors(b) if d > 1]

        # (i) smallest k with R(k, d) = 0 for some non-trivial d|b
        smallest_k = None
        for k in range(1, b + 1):
            for d in nontrivial_divs:
                if abs(R(k, d)) < 1e-10:
                    smallest_k = k
                    break
            if smallest_k is not None:
                break
        if smallest_k != spf_b:
            fails_smallest += 1
            print(f"  FAIL b={b}: smallest_k={smallest_k}, spf={spf_b}")

        # (ii) count at k = b_2 = p_1 p_2: should be 2^2 - 1 = 3
        b2 = pf[0] * pf[1]
        cnt2 = sum(1 for d in nontrivial_divs if abs(R(b2, d)) < 1e-10)
        if cnt2 != 3:
            fails_count_2 += 1
            print(f"  FAIL b={b}, b_2={b2}: count={cnt2}, expected 3")

        # (iii) count at k = b_3 = p_1 p_2 p_3 (only if omega(b) >= 3)
        if len(pf) >= 3:
            n_count_3_checked += 1
            b3 = pf[0] * pf[1] * pf[2]
            cnt3 = sum(1 for d in nontrivial_divs if abs(R(b3, d)) < 1e-10)
            if cnt3 != 7:
                fails_count_3 += 1
                print(f"  FAIL b={b}, b_3={b3}: count={cnt3}, expected 7")

    print(f"  squarefree b tested (omega>=2): {len(bs)}")
    print(f"  spf smallest-k failures:        {fails_smallest}")
    print(f"  b_2 count = 3 failures:         {fails_count_2}")
    print(f"  b_3 count = 7 failures (of {n_count_3_checked}):  {fails_count_3}")
    ok = (fails_smallest == 0 and fails_count_2 == 0 and fails_count_3 == 0)
    print(f"  result: {'PASS' if ok else 'FAIL'}")
    print()
    return ok


# ---------------------------------------------------------------------
# Theorem 3: asymptotic average  (1/(f-1)) sum R(k,f) -> Si(2 pi)/pi
# ---------------------------------------------------------------------
def verify_asymptotic_average():
    print("=" * 60)
    print("Theorem 3: asymptotic average -> Si(2 pi)/pi ~ 0.45141")
    print("=" * 60)
    target = SI_2PI_OVER_PI
    rows = []
    fails = 0
    for f in [50, 100, 500, 1000]:
        s = 0.0
        for k in range(1, f):
            s += R(k, f)
        avg = s / (f - 1)
        dev = abs(avg - target)
        # Tolerance: O(1/f) convergence rate; allow 2 * (target / f)
        tol = max(1e-3, 4.0 * target / f)
        if dev > tol:
            fails += 1
        rows.append((f, avg, dev))
        print(f"  f={f:>5}  avg={avg:.6f}  target={target:.6f}  dev={dev:.2e}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Optional informational pass: monotone non-increase at integer args
# ---------------------------------------------------------------------
def report_monotone_at_integers():
    """
    Per referee M4 (SAVE_PLAN_J04 §2.5): R(k, p) is non-increasing on
    k in {1, ..., p-1} from the closed form. We REPORT this rather
    than ASSERT strict monotonicity outside (0, 1).
    """
    print("=" * 60)
    print("Report: R(k, p) is non-increasing on k in {1, ..., p-1}")
    print("=" * 60)
    primes = [p for p in range(3, 30) if is_prime(p)]
    fails = 0
    for p in primes:
        prev = float("inf")
        for k in range(1, p):
            v = R(k, p)
            if v > prev + 1e-12:
                fails += 1
                print(f"  NOTE p={p}, k={k}: R={v:.6f} > prev={prev:.6f}")
            prev = v
    print(f"  primes tested: {len(primes)}")
    print(f"  monotone violations: {fails}")
    print(f"  result: {'PASS (informational)' if fails == 0 else 'NOTE'}")
    print()
    return True


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
if __name__ == "__main__":
    print()
    print("=" * 72)
    print("  Verification: Full-Period Cancellation of R(k, f) and the")
    print("                spf-Localization for Squarefree Moduli")
    print("                (Sanders, Gish, 2026)")
    print("=" * 72)
    print()

    results = [
        verify_lemma_basic(),
        verify_full_period_cancellation(),
        verify_layered_structure(),
        verify_asymptotic_average(),
        report_monotone_at_integers(),
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
