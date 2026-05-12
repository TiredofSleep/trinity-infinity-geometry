#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
J22 / HARMONY ladder — TSML HARMONY-count verification (73-rung).

Verifies Theorem 3.1 (manuscript §3): HARM(T) = 73, where T is the
canonical TSML composition table on Z/10Z.

Usage:
    PYTHONIOENCODING=utf-8 python tsml_harmony_count.py

Dependencies: numpy.
Wall-clock: under 1 second.
License: CC-BY-4.0.
"""

import numpy as np


# Canonical TSML composition table (CL forcing axioms; manuscript §2).
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
    harm_count = int((T == 7).sum())
    print(f"HARM(T) = {harm_count}")
    expected = 73
    if harm_count == expected:
        print(f"[PASS] HARM(T) == {expected}")
        return 0
    print(f"[FAIL] expected {expected}, got {harm_count}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
