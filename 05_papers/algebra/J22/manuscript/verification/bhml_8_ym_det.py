#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder -- Yang--Mills 8x8 determinant verification
(70-rung).

Verifies Theorem 6.1 (manuscript Sec. 5): det(B_YM) = 70 = C(8, 4),
where B_YM is the canonical BHML companion table restricted to the
index set {1, 2, 3, 4, 5, 6, 8, 9} (i.e., B with the VOID and
HARMONY rows/columns dropped).

The BHML matrix below is the canonical table exported by
Gen13/targets/foundations/lenses.py at integer precision; it is
the result of the CL forcing axioms A1--A9.

Usage:
    PYTHONIOENCODING=utf-8 python bhml_8_ym_det.py

Dependencies: numpy.
Wall-clock: under 1 second.
License: CC-BY-4.0.
"""

import math

import numpy as np


# Canonical BHML composition table (Gen13/targets/foundations/lenses.py).
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


def main():
    idx = [1, 2, 3, 4, 5, 6, 8, 9]
    B_YM = B[np.ix_(idx, idx)]
    det = int(round(np.linalg.det(B_YM.astype(float))))
    c84 = math.comb(8, 4)
    print(f"det(B_YM) = {det}")
    print(f"C(8, 4)   = {c84}")
    if det == c84 == 70:
        print("[PASS] det(B_YM) == C(8, 4) == 70")
        return 0
    print(f"[FAIL] expected det(B_YM) == 70; got {det}.")
    print("       (The canonical BHML is exported by")
    print("        Gen13/targets/foundations/lenses.py.)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
