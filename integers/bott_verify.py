#!/usr/bin/env python3
"""bott_verify.py -- reproduces every FORCED claim in bott_periodicity.md.

    python bott_verify.py     # all four blocks must print PASS

Verifies: (1) the quaternion relations Cl(0,2) ~ H; (2) the pseudoscalar signature sign
I^2 = (-1)^{n(n-1)/2} has period 4; (3) the three corrected sub-claims; (4) H (x) H ~ R(4):
left and right multiplication by quaternions span all 16 dimensions of the real 4x4 matrices --
the fact that makes the Clifford types return after 4 + 4 = 8 steps.
Nothing here is a new derivation of Bott periodicity -- it is standard mathematics, checked.
"""
import numpy as np
from itertools import combinations

# (1) quaternion relations: Cl(0,2) ~ H  --  i^2=j^2=k^2=-1, ij=k, jk=i, ki=j, ijk=-1
I = np.array([[1j, 0], [0, -1j]]); J = np.array([[0, 1], [-1, 0]]); K = np.array([[0, 1j], [1j, 0]])
assert np.allclose(I @ I, -np.eye(2)) and np.allclose(J @ J, -np.eye(2)) and np.allclose(K @ K, -np.eye(2))
assert np.allclose(I @ J, K) and np.allclose(J @ K, I) and np.allclose(K @ I, J)
assert np.allclose(I @ J @ K, -np.eye(2))
assert np.allclose(J @ I, -K)                      # anticommute -> 3D rotation is non-abelian
print("BLOCK 1  quaternion relations Cl(0,2)~H: PASS  (i^2=j^2=k^2=-1, ij=k, ijk=-1, ji=-k)")

# (2) pseudoscalar signature sign, period 4
signs = [(-1) ** (n * (n - 1) // 2) for n in range(17)]
seq = ''.join('+' if s > 0 else '-' for s in signs)
assert seq[:8] == '++--++--' and seq[8:16] == seq[0:8]
print(f"BLOCK 2  pseudoscalar sign period 4: PASS  (n=0..15: {seq[:16]})")

# (3) corrected sub-claims
assert len(list(combinations(range(4), 2))) == 6      # tetrahedron: 6 edges
assert len(list(combinations(range(3), 2))) == 3      # triangle: 3
assert signs[3] == -1 and signs[4] == +1              # sign flips + at dim 4, still - at dim 3
print("BLOCK 3  corrections: PASS  (tet=6 edges, tri=3; sign flips + at dim 4, not dim 3)")


# (4) H (x) H ~ R(4): quaternion left/right multiplications on R^4 span all real 4x4 matrices
def qmul(p, q):
    a1, b1, c1, d1 = p
    a2, b2, c2, d2 = q
    return np.array([a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2, a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
                     a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2, a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2])


basis = np.eye(4)
L = [np.array([qmul(a, e) for e in basis]).T for a in basis]     # x -> a x
R = [np.array([qmul(e, b) for e in basis]).T for b in basis]     # x -> x b
span = np.array([(Li @ Rj).ravel() for Li in L for Rj in R])
assert np.linalg.matrix_rank(span) == 16
print("BLOCK 4  H (x) H ~ R(4): PASS  (the 16 maps x -> a x b span all real 4x4 matrices)")

print("\nAll FORCED claims in bott_periodicity.md verified.")
