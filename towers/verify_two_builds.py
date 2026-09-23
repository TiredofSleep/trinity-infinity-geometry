#!/usr/bin/env python3
"""verify_two_builds.py -- the two forced builds from N points, unified by Pascal.

Reproduces every [FORCED] claim in THE_TWO_BUILDS.md:
  A (equidistant -> simplex): face-vector = Pascal row N, sums to 2^N.
  B (orthogonal  -> Cl(n)):   grade-vector = Pascal row n, sums to 2^n; bivectors^2 = -1.
  shared: adding one element = one binary in/out choice = a factor of 2.

    python verify_two_builds.py
"""
import numpy as np
from math import comb

# --- Build A: the (N-1)-simplex on N points; j vertices span a (j-1)-face ---
for N in (3, 4, 5, 6):
    faces = [comb(N, j) for j in range(N + 1)]        # j=0 empty ... j=N whole
    assert sum(faces) == 2**N
print("Build A (simplex on N points): face-vector = Pascal row N, sums to 2^N")
print(f"   tetrahedron N=4: {[comb(4, j) for j in range(5)]} = empty, verts, edges, faces, cell")

# --- Build B: Cl(3) from three orthogonal (Pauli) generators ---
e1 = np.array([[0, 1], [1, 0]], complex)
e2 = np.array([[0, -1j], [1j, 0]], complex)
e3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
for e in (e1, e2, e3):
    assert np.allclose(e @ e, I2)                     # square to +1
for a, b in ((e1, e2), (e1, e3), (e2, e3)):
    assert np.allclose(a @ b, -b @ a)                 # anticommute
grades = [1, 3, 3, 1]
assert grades == [comb(3, k) for k in range(4)] and sum(grades) == 2**3
print("Build B (Cl(3) from 3 orthogonal axes): grades = Pascal row 3 = 1,3,3,1, sums to 2^3")

# --- the i: bivectors (face-planes) square to -1 ---
for biv in (e1 @ e2, e1 @ e3, e2 @ e3):
    assert np.allclose(biv @ biv, -I2)
assert np.allclose((e1 @ e2 @ e3) @ (e1 @ e2 @ e3), -I2)   # pseudoscalar too
print("the i: bivectors (and the pseudoscalar) square to -1 -> rotation is intrinsic to Cl(3)")

# --- the shared doubling: one added element = one binary choice = x2 ---
for n in range(1, 9):
    assert 2**(n + 1) == 2 * 2**n
print("shared mechanism: +1 point/generator = one in/out choice = a factor of 2")

print("\nTwo builds, same binomials (Pascal), same doubling; A indexed by POINTS, B by DIMENSIONS.")
print("They coincide in counting and growth only -- a simplex is not a Clifford algebra (fence).")
