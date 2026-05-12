#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder — TSML 9x9 sub-magma HARMONY-count
verification (71-rung sub-magma form).

Verifies Theorem 5.1 (manuscript §4): HARM(T_{1..9}) = 71, where
T_{1..9} is the restriction of the canonical TSML composition table
to the index set {1, 2, ..., 9} (VOID-stripped 9x9 sub-magma).

Usage:
    PYTHONIOENCODING=utf-8 python tsml_submagma_9x9.py

Dependencies: numpy.
Wall-clock: under 1 second.
License: CC-BY-4.0.
"""

import numpy as np


# Canonical TSML composition table.
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


def main():
    T9 = T[1:, 1:]  # rows 1..9, cols 1..9
    harm_count = int((T9 == 7).sum())
    expected = 71
    print(f"HARM(T_{{1..9}}) = {harm_count}")
    if harm_count == expected:
        print(f"[PASS] HARM(T_{{1..9}}) == {expected}")
        return 0
    print(f"[FAIL] expected {expected}, got {harm_count}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
