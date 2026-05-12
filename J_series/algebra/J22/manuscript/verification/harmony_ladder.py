#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder -- wrapper script that runs all five
verification snippets and prints a 5x3 (rung / expected / actual)
verification table.

The five rungs:
  - 73 (HARMONY count of full TSML T)
  - 71 (HARMONY count of TSML 9x9 sub-magma)
  - 71 (cell-disagreement count between TSML T and BHML B)
  - 70 (Yang-Mills 8x8 determinant)
  - disc(LMFDB 4.2.10224.1) = -40896 = -2^6 * 3^2 * 71  (71 prime in disc)

The TSML and BHML matrices below are the canonical tables exported by
Gen13/targets/foundations/lenses.py at integer precision.

Usage:
    PYTHONIOENCODING=utf-8 python harmony_ladder.py

Dependencies: numpy, sympy.
Wall-clock: under 3 seconds.
License: CC-BY-4.0.
"""

import math

import numpy as np
import sympy


# Canonical TSML composition table (Gen13/targets/foundations/lenses.py).
T = np.array([
    [0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 7, 3, 7, 7, 7, 7, 7, 7, 7],
    [0, 3, 7, 7, 4, 7, 7, 7, 7, 9],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 3],
    [0, 7, 4, 7, 7, 7, 7, 7, 8, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [0, 7, 7, 7, 8, 7, 7, 7, 7, 7],
    [0, 7, 9, 3, 7, 7, 7, 7, 7, 7],
])

# Canonical BHML companion table (Gen13/targets/foundations/lenses.py).
B = np.array([
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 2, 6, 6],
    [2, 3, 3, 4, 5, 6, 7, 3, 6, 6],
    [3, 4, 4, 4, 5, 6, 7, 4, 6, 6],
    [4, 5, 5, 5, 5, 6, 7, 5, 7, 7],
    [5, 6, 6, 6, 6, 6, 7, 6, 7, 7],
    [6, 7, 7, 7, 7, 7, 7, 7, 7, 7],
    [7, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [8, 6, 6, 6, 7, 7, 7, 9, 7, 8],
    [9, 6, 6, 6, 7, 7, 7, 0, 8, 0],
])


def rung_73():
    return int((T == 7).sum())


def rung_71_submagma():
    T9 = T[1:, 1:]
    return int((T9 == 7).sum())


def rung_71_disagreement():
    return int((T != B).sum())


def rung_70_ym_det():
    idx = [1, 2, 3, 4, 5, 6, 8, 9]
    B_YM = B[np.ix_(idx, idx)]
    return int(round(np.linalg.det(B_YM.astype(float))))


def rung_71_galois():
    """Compute the discriminant; return the integer 71 if it is the
    unique odd prime > 3 in the factorization, else return -1."""
    x = sympy.Symbol('x')
    f = x**4 + 4 * x**3 - x**2 + 2 * x - 2
    disc = sympy.discriminant(f, x)
    factor = sympy.factorint(abs(disc))
    odd_primes_above_3 = [p for p in factor if p > 3 and p % 2 == 1]
    if odd_primes_above_3 == [71]:
        return 71
    return -1


def main():
    rungs = [
        ("rung-A: HARM(T)             = 73", 73, rung_73()),
        ("rung-B-submagma: HARM(T_9)  = 71", 71, rung_71_submagma()),
        ("rung-B-lens: |T XOR B|      = 71", 71, rung_71_disagreement()),
        ("rung-B-galois: 71 in disc  = 71", 71, rung_71_galois()),
        ("rung-C: det(B_YM) = C(8,4) = 70", 70, rung_70_ym_det()),
    ]

    print("J22 / HARMONY ladder -- verification table (5 x 3)")
    print("=" * 60)
    n_pass = 0
    for label, expected, actual in rungs:
        mark = "[PASS]" if expected == actual else "[FAIL]"
        if expected == actual:
            n_pass += 1
        print(f"  {mark}  {label:<40s}  actual = {actual}")
    print("-" * 60)
    print(f"  {n_pass}/{len(rungs)} PASS at integer/machine precision.")

    # Print the discriminant + factorization explicitly:
    x = sympy.Symbol('x')
    f = x**4 + 4 * x**3 - x**2 + 2 * x - 2
    disc = sympy.discriminant(f, x)
    factor = sympy.factorint(abs(disc))
    print()
    print("Discriminant detail (rung-B-galois):")
    print(f"  f(x) = {f}")
    print(f"  disc(f) = {disc}")
    print(f"  |disc(f)| factor = {factor}")
    print(f"  -2^6 * 3^2 * 71 = {-2**6 * 3**2 * 71}  (correct)")
    print(f"  -2^7 * 3 * 7 * 19 = {-2**7 * 3 * 7 * 19}  (alternate, WRONG)")

    return 0 if n_pass == len(rungs) else 1


if __name__ == "__main__":
    raise SystemExit(main())
