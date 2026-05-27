"""verify_J62.py -- Independent verification of Theorems 1, 2 of J62.

Runs in <0.1 seconds. Dependencies: NumPy only.
Imports the canonical TSML table from ck_tables.py at the repo root.
"""
import sys
from pathlib import Path
# Locate repo root from this script's path
REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))

import numpy as np
from ck_tables import TSML


def main():
    T8 = np.array(TSML)[np.ix_([1, 2, 3, 4, 5, 6, 8, 9],
                                [1, 2, 3, 4, 5, 6, 8, 9])]
    print("=== J62 — TSML 8x8 Null Verification ===\n")
    print("TSML_8 matrix (basis: BEING, DOING, BECOMING, COLLAPSE, CREATE,")
    print("                       ASCEND, BREATH, RESET):")
    print(T8)
    print()

    # Theorem 1: rank, nullity, null eigenvector
    rank = np.linalg.matrix_rank(T8)
    print(f"[Theorem 1] rank(TSML_8) = {rank}      (expected 7)")
    assert rank == 7, "rank mismatch"

    v0 = np.array([0, 0, 0, 0, 1, -1, 0, 0]) / np.sqrt(2)
    null_check = T8 @ v0
    print(f"           TSML_8 @ v0 = {null_check}  (expected ~0)")
    assert np.allclose(null_check, np.zeros(8)), "null eigenvector mismatch"
    print("           PASS\n")

    # Theorem 2: eigenvalue spectrum
    eigs = sorted(np.linalg.eigvals(T8).real, key=abs)
    print(f"[Theorem 2] eigenvalues (sorted by magnitude):")
    for ev in eigs:
        print(f"           {ev:>10.4f}")
    # Smallest in magnitude should be near zero
    assert abs(eigs[0]) < 1e-10, "smallest eigenvalue not ~0"
    # Largest should be ~54.077
    assert abs(eigs[-1] - 54.0767) < 0.001, "largest eigenvalue mismatch"
    print("           PASS\n")

    # Additional check: structural — rows 5 (CREATE) and 6 (ASCEND) identical
    # Indices in T8 are 0..7 for the original {1, 2, 3, 4, 5, 6, 8, 9}.
    # CREATE = index 5 in original = T8 row 4 (0-indexed)
    # ASCEND = index 6 in original = T8 row 5 (0-indexed)
    create_row = T8[4]
    ascend_row = T8[5]
    print(f"[Boundary-stripped resonance check]")
    print(f"           CREATE row (T8[4]): {create_row}")
    print(f"           ASCEND row (T8[5]): {ascend_row}")
    assert np.array_equal(create_row, ascend_row), "CREATE-ASCEND not identical"
    print("           CREATE row == ASCEND row: PASS")
    print()
    print("=== All checks PASS ===")


if __name__ == "__main__":
    main()
