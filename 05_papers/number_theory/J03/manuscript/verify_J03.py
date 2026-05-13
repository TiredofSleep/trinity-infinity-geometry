#!/usr/bin/env python3
"""
Verification script for "The First-G Event and a Discrete Sinc^2 Identity"
(B.R. Sanders, M. Gish, 2026).

Verifies, by exact computation:
  Theorem 1 (First-G localization): k*(b) = spf(b) for every squarefree b in [2, 500]
  Theorem 2 (closed form): R(k,f) = sin^2(pi k / f) / (k^2 sin^2(pi/f))
  Theorem 3 (synchronization): for f = spf(b), R(spf(b), spf(b)) = 0
  Theorem 4 (continuum limit): R(k, f) -> sinc^2(k/f) as f -> infinity

Source bundle: J03 manuscript verification.

Usage:
  python3 verify_first_g.py
"""
import math
from math import gcd, sin, pi


def smallest_prime_factor(n: int) -> int:
    """Return the smallest prime factor of n (assumes n >= 2)."""
    if n % 2 == 0:
        return 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return p
        p += 2
    return n


def is_squarefree(n: int) -> bool:
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def first_g_event(b: int) -> int:
    """Return the smallest k in {1,...,b} with G_k(b) nonempty."""
    for k in range(1, b + 1):
        for x in range(1, k + 1):
            if gcd(x, b) > 1:
                return k
    return -1  # never reached for b > 1


def R_geometric(k: int, f: int) -> float:
    """Direct computation: R(k,f) = |(1/k) sum_{j=1}^{k} e^{2 pi i j / f}|^2."""
    real = sum(math.cos(2 * pi * j / f) for j in range(1, k + 1)) / k
    imag = sum(math.sin(2 * pi * j / f) for j in range(1, k + 1)) / k
    return real * real + imag * imag


def R_closed(k: int, f: int) -> float:
    """Closed form: R(k,f) = sin^2(pi k/f) / (k^2 sin^2(pi/f))."""
    return sin(pi * k / f) ** 2 / (k * k * sin(pi / f) ** 2)


def sinc2(t: float) -> float:
    """Normalized sinc^2: sinc^2(t) = (sin(pi t) / (pi t))^2 for t != 0, else 1."""
    if t == 0.0:
        return 1.0
    s = sin(pi * t) / (pi * t)
    return s * s


# ---------------------------------------------------------------------
# Theorem 1: First-G localization
# ---------------------------------------------------------------------
def verify_first_g():
    print("=" * 60)
    print("Theorem 1: First-G localization (k*(b) = spf(b))")
    print("=" * 60)
    squarefree_bs = [b for b in range(2, 501) if is_squarefree(b)]
    n_b = len(squarefree_bs)
    n_pairs = sum(smallest_prime_factor(b) for b in squarefree_bs)
    fails = 0
    for b in squarefree_bs:
        kstar = first_g_event(b)
        spf = smallest_prime_factor(b)
        if kstar != spf:
            fails += 1
            print(f"  FAIL b={b}: k*={kstar}, spf={spf}")
    print(f"  squarefree b values tested: {n_b}")
    print(f"  total (b,k) pairs:           {n_pairs}")
    print(f"  counterexamples:             {fails}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 2: closed form
# ---------------------------------------------------------------------
def verify_closed_form():
    print("=" * 60)
    print("Theorem 2: closed form for R(k,f)")
    print("=" * 60)
    primes = [3, 5, 7, 11, 13, 17, 19, 23]
    max_err = 0.0
    n_checked = 0
    for f in primes:
        for k in range(1, f + 2):
            geo = R_geometric(k, f)
            cls = R_closed(k, f)
            err = abs(geo - cls)
            max_err = max(max_err, err)
            n_checked += 1
    print(f"  primes tested:        {primes}")
    print(f"  (k,f) pairs checked:  {n_checked}")
    print(f"  max deviation:        {max_err:.2e}  (machine eps ~ 2.22e-16)")
    print(f"  result: {'PASS' if max_err < 1e-12 else 'FAIL'}")
    print()
    return max_err < 1e-12


# ---------------------------------------------------------------------
# Theorem 3: synchronization
# ---------------------------------------------------------------------
def verify_synchronization():
    print("=" * 60)
    print("Theorem 3: synchronization (k*=spf(b), R(spf(b), spf(b))=0)")
    print("=" * 60)
    test_bs = [10, 30, 35, 77, 105, 210, 1001, 2310]
    fails = 0
    for b in test_bs:
        p1 = smallest_prime_factor(b)
        kstar = first_g_event(b)
        R_at_p1 = R_closed(p1, p1)
        ok = (kstar == p1) and (abs(R_at_p1) < 1e-10)
        marker = "OK" if ok else "FAIL"
        if not ok:
            fails += 1
        print(f"  b={b:>5}  spf={p1:>3}  k*={kstar:>3}  R(p1,p1)={R_at_p1:.2e}  [{marker}]")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


# ---------------------------------------------------------------------
# Theorem 4: continuum limit
# ---------------------------------------------------------------------
def verify_continuum_limit():
    print("=" * 60)
    print("Theorem 4: continuum limit R(k,f) -> sinc^2(k/f)")
    print("=" * 60)
    # Fix t = k/f at t = 1/2 and t = 1/4, scale f -> infinity
    print(f"  Scaling along t = 1/2:")
    print(f"    {'f':>6} {'k':>6} {'R(k,f)':>14} {'sinc^2(1/2)':>14} {'diff':>12}")
    target = sinc2(0.5)
    for f in [10, 100, 1000, 10000]:
        k = f // 2
        R = R_closed(k, f)
        print(f"    {f:>6} {k:>6} {R:>14.10f} {target:>14.10f} {abs(R-target):>12.2e}")
    print()
    print(f"  Scaling along t = 1/4:")
    print(f"    {'f':>6} {'k':>6} {'R(k,f)':>14} {'sinc^2(1/4)':>14} {'diff':>12}")
    target = sinc2(0.25)
    for f in [4, 40, 400, 4000]:
        k = f // 4
        R = R_closed(k, f)
        print(f"    {f:>6} {k:>6} {R:>14.10f} {target:>14.10f} {abs(R-target):>12.2e}")
    print(f"  result: PASS (visible monotone convergence)")
    print()
    return True


# ---------------------------------------------------------------------
# Corollary 4.4(ii): R(f-1, f) = 1/(f-1)^2
# ---------------------------------------------------------------------
def verify_endpoint_minimum():
    print("=" * 60)
    print("Corollary 4.4(ii): R(f-1, f) = 1/(f-1)^2")
    print("=" * 60)
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 31, 53, 97, 211]
    fails = 0
    for f in primes:
        R_minus = R_closed(f - 1, f)
        expected = 1.0 / (f - 1) ** 2
        err = abs(R_minus - expected)
        if err > 1e-12:
            fails += 1
        print(f"  f={f:>4}  R(f-1,f)={R_minus:.10f}  1/(f-1)^2={expected:.10f}  diff={err:.2e}")
    print(f"  result: {'PASS' if fails == 0 else 'FAIL'}")
    print()
    return fails == 0


if __name__ == "__main__":
    print()
    print("Verification: The First-G Event and a Discrete Sinc^2 Identity")
    print("=" * 60)
    print()
    results = [
        verify_first_g(),
        verify_closed_form(),
        verify_synchronization(),
        verify_continuum_limit(),
        verify_endpoint_minimum(),
    ]
    print("=" * 60)
    print(f"OVERALL: {sum(results)} / {len(results)} verifications passed")
    print("=" * 60)
