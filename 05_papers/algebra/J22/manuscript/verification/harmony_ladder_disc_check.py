#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder — discriminant verification (71-rung Galois form).

Verifies the Galois-form claim of Theorem 5.5 (manuscript §4):
  disc(x^4 + 4x^3 - x^2 + 2x - 2) = -40896 = -2^6 * 3^2 * 71.

Pre-empts the factoring error in the original fresh-eyes referee
report (which claimed disc = -2^7 * 3 * 7 * 19 = -51072 — wrong by
~25% in magnitude).

Usage:
    PYTHONIOENCODING=utf-8 python harmony_ladder_disc_check.py

Dependencies: sympy.
Wall-clock: under 1 second.
License: CC-BY-4.0.
"""

import sympy


def main():
    x = sympy.Symbol('x')
    f = x**4 + 4 * x**3 - x**2 + 2 * x - 2

    disc = sympy.discriminant(f, x)
    factor = sympy.factorint(abs(disc))

    print("J22 / HARMONY ladder — discriminant verification")
    print("=" * 60)
    print("Polynomial:")
    print("  f(x) =", f)
    print("LMFDB identifier: 4.2.10224.1 (via Tschirnhaus reduction)")
    print()
    print("Discriminant of f:")
    print("  disc(f) =", disc)
    print("  |disc(f)| =", abs(disc))
    print()
    print("Factorization (sympy.factorint):")
    print("  factor(40896) =", factor)
    print()

    # Validate the paper's claim:
    expected_factor = {2: 6, 3: 2, 71: 1}
    expected_disc = -40896
    paper_value = -2**6 * 3**2 * 71

    checks = []
    checks.append(("disc(f) == -40896", disc == expected_disc))
    checks.append(("|disc(f)| factor == {2:6, 3:2, 71:1}", factor == expected_factor))
    checks.append(("-2^6 * 3^2 * 71 == -40896", paper_value == expected_disc))
    # Cross-check (alternate factorization is wrong):
    alt_value = 2**7 * 3 * 7 * 19  # would equal 51072, NOT 40896
    checks.append(("alt factorization 2^7*3*7*19 != |-40896|", alt_value != abs(expected_disc)))
    checks.append(("71 IS in disc(f)", 71 in factor))

    print("Pass-table:")
    print("-" * 60)
    n_pass = 0
    for label, passed in checks:
        mark = "[PASS]" if passed else "[FAIL]"
        if passed:
            n_pass += 1
        print(f"  {mark}  {label}")
    print("-" * 60)
    print(f"  {n_pass}/{len(checks)} PASS at integer/machine precision.")

    # Cross-check explicit:
    print()
    print("Explicit cross-checks (read by direct multiplication):")
    print(f"  -2^6 * 3^2 * 71 = {-2**6 * 3**2 * 71}    (matches paper claim)")
    print(f"  -2^7 * 3   * 7 * 19 = {-2**7 * 3 * 7 * 19}    (alternate claim, WRONG)")
    print(f"  Difference: |{abs(-2**6 * 3**2 * 71) - abs(-2**7 * 3 * 7 * 19)}| (~{abs(2**7*3*7*19 - 2**6*3**2*71) / 2**6 / 3**2 / 71 * 100:.1f}% of correct value)")

    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
