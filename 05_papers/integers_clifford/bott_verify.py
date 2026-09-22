#!/usr/bin/env python3
"""bott_verify.py -- reproduces every FORCED claim in bott_periodicity_2x3.md.

    python bott_verify.py     # all three blocks must print PASS

Verifies: (1) the quaternion relations Cl(0,2) ~ H (the book's tower rung, and the
'trinity' member H); (2) the pseudoscalar signature sign I^2 = (-1)^{n(n-1)/2} has
period 4 (the '+' + - -' duality); (3) the three corrected sub-claims.
Nothing here is a TIG derivation of Bott periodicity -- it is standard mathematics,
recorded so the fenced [READING] rests on checked facts.
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
print("         Bott period 8 = 4 (sign duality) x 2 (real/complex character; R,C,H by Frobenius)")

# (3) corrected sub-claims
assert len(list(combinations(range(4), 2))) == 6      # tetrahedron: 6 edge-tensors
assert len(list(combinations(range(3), 2))) == 3      # triangle: 3
assert signs[3] == -1 and signs[4] == +1              # sign flips + at dim 4, still - at dim 3
print("BLOCK 3  corrections: PASS  (tet=6 edges, tri=3; sign flips + at dim 4, not dim 3)")

print("\nAll FORCED claims in bott_periodicity_2x3.md verified. The [READING] (duality x")
print("trinity) is tagged, not asserted; the [FENCE] (framework-8 dimension != Bott-8")
print("period) stands.")
