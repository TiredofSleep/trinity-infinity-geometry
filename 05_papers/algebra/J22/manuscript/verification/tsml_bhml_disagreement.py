#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder -- TSML vs BHML cell-disagreement verification
(71-rung lens form).

Verifies Theorem 5.3 (manuscript Sec. 4): |T XOR B| = 71, where T is
the canonical TSML composition table and B is the canonical BHML
companion table on Z/10Z; "XOR" is taken as the count of cells
(i, j) in {0, ..., 9}^2 with T(i, j) != B(i, j).

The two matrices below are the canonical tables exported by
Gen13/targets/foundations/lenses.py at integer precision; both are
the result of the CL forcing axioms A1--A9.

Usage:
    PYTHONIOENCODING=utf-8 python tsml_bhml_disagreement.py

Dependencies: numpy.
Wall-clock: under 1 second.
License: CC-BY-4.0.
"""

import numpy as np


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


def main():
    diff_count = int((T != B).sum())
    expected = 71
    print(f"|T XOR B| (cell disagreement count) = {diff_count}")
    if diff_count == expected:
        print(f"[PASS] cell-disagreement == {expected}")
        return 0
    print(f"[FAIL] expected {expected}, got {diff_count}.")
    print("       (The canonical tables are exported by")
    print("        Gen13/targets/foundations/lenses.py.)")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
