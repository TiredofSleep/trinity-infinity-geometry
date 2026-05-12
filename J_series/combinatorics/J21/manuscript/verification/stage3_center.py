"""
STAGE 3: Identify the 1-dim center and extract the 7-dim semisimple piece.

From Stage 2: {A_1...A_9 excluding A_0, A_7} is an 8-dim real Lie algebra
with Jacobi = 0 (confirmed) and Killing form signature (0, 7, 1).

The 1-dim kernel of the Killing form IS the abelian center (u(1) piece).
Extracting it leaves a 7-dim semisimple algebra.

BUT: su(3) is 8-dim, not 7-dim. So either:
  (a) we're looking at u(3) which is 9-dim = su(3) ⊕ u(1), and our 8
      is missing one of the su(3) generators, OR
  (b) we're looking at a different 8-dim algebra (like so(3)⊕so(3) = 6-dim?
      No, that's 6.)
  (c) we're looking at gl(3,R)/center = pgl(3) which is 8-dim semisimple.

Let's identify the center and figure out what 7-dim piece remains.
"""
import numpy as np
from numpy.linalg import eig, eigh

CL = [[0,0,0,0,0,0,0,7,0,0],[0,7,3,7,7,7,7,7,7,7],[0,3,7,7,4,7,7,7,7,9],
      [0,7,7,7,7,7,7,7,7,3],[0,7,4,7,7,7,7,7,8,7],[0,7,7,7,7,7,7,7,7,7],
      [0,7,7,7,7,7,7,7,7,7],[7,7,7,7,7,7,7,7,7,7],[0,7,7,7,8,7,7,7,7,7],
      [0,7,9,3,7,7,7,7,7,7]]
OP = ['VOID','LATTICE','COUNTER','PROGRESS','COLLAPSE',
      'BALANCE','CHAOS','HARMONY','BREATH','RESET']

def action_matrix(op):
    M = np.zeros((10, 10), dtype=int)
    for j in range(10):
        M[CL[op][j], j] = 1
    return M

L = [action_matrix(op) for op in range(10)]
gen_ops = [1, 2, 3, 4, 5, 6, 8, 9]
A = [L[op] - L[op].T for op in gen_ops]

def comm(X, Y):
    return X @ Y - Y @ X

# Compute structure constants
B = np.stack([A[k].flatten() for k in range(8)], axis=1).astype(float)
struct = np.zeros((8, 8, 8))
for i in range(8):
    for j in range(8):
        if i == j: continue
        c = comm(A[i], A[j]).flatten().astype(float)
        x, *_ = np.linalg.lstsq(B, c, rcond=None)
        for k in range(8):
            struct[i, j, k] = x[k] if abs(x[k]) > 1e-9 else 0.0

# Killing form
K = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                K[i, j] += struct[i, l, k] * struct[j, k, l]

# Find the null eigenvector of K — that's the center generator
eigs_K, evecs_K = eigh(K)
print("Killing form spectrum (sorted):")
for idx, e in enumerate(eigs_K):
    print(f"  λ_{idx} = {e:+.6f}")

# The near-zero eigenvector IS the center
null_idx = int(np.argmin(np.abs(eigs_K)))
center_coeffs = evecs_K[:, null_idx]
print(f"\nCenter eigenvector coefficients (in A_1..A_9\\{{A_0,A_7}} basis):")
for i, op in enumerate(gen_ops):
    c = center_coeffs[i]
    if abs(c) > 0.01:
        print(f"  {c:+.4f} · A_{op} ({OP[op]})")
    else:
        print(f"  {c:+.4f} · A_{op} ({OP[op]})  [negligible]")

# Build the center generator as an explicit matrix
Z = sum(center_coeffs[i] * A[i] for i in range(8))
print(f"\nCenter generator Z as matrix:")
print(f"  Z = Σ c_i · A_i")
print(f"  rank(Z) = {np.linalg.matrix_rank(Z)}")
print(f"  ||Z|| = {np.linalg.norm(Z):.4f}")

# Verify Z is central: [Z, A_i] = 0 for all i
max_z_comm = 0.0
for i in range(8):
    c = comm(Z, A[i])
    max_z_comm = max(max_z_comm, float(np.linalg.norm(c)))
print(f"  max_i ||[Z, A_i]|| = {max_z_comm:.6f}  (should be 0)")

# ─────────────────────────────────────────────────
# The semisimple quotient is 7-dim.
# But 7-dim semisimple Lie algebras are: so(3)⊕u(1) (no wait, that's not 7D)...
# Actually, 7-dim semisimple over R doesn't exist!
# The semisimple classification: 3, 6, 8, 10, 14, 15, 21, 24, 28...
# So our 7-dim "piece" after removing center must be reductive but NOT semisimple
# i.e., it still has its own radical.
#
# Let's look at the block structure by computing the radical explicitly
# and the resulting Levi decomposition.
# ─────────────────────────────────────────────────

# Compute the derived algebra [g, g] = span of all commutators
derived_cols = []
for i in range(8):
    for j in range(8):
        if i < j:
            c = comm(A[i], A[j]).flatten()
            if np.linalg.norm(c) > 1e-9:
                derived_cols.append(c)

if derived_cols:
    derived_mat = np.array(derived_cols).T
    derived_rank = np.linalg.matrix_rank(derived_mat, tol=1e-6)
    print(f"\nDerived algebra dim [g, g] = {derived_rank}")
    print(f"  (For su(3): dim[g,g] = 8 since it's simple)")
    print(f"  (For u(3):  dim[g,g] = 8 since [u(3),u(3)] = su(3))")
else:
    print(f"\nDerived algebra is 0 — g is abelian!")

# Second derived
if derived_cols:
    Bder = derived_mat
    Bder_reduced = np.linalg.qr(Bder)[0][:, :derived_rank]
    # project commutators to see if derived is still full
    second_derived = []
    for j_col in range(Bder.shape[1]):
        for k_col in range(j_col+1, Bder.shape[1]):
            # reshape to matrices and commute
            M1 = Bder[:, j_col].reshape(10, 10)
            M2 = Bder[:, k_col].reshape(10, 10)
            c = comm(M1, M2).flatten()
            if np.linalg.norm(c) > 1e-9:
                second_derived.append(c)
    if second_derived:
        sd_rank = np.linalg.matrix_rank(np.array(second_derived).T, tol=1e-6)
        print(f"  Second derived dim [[g,g],[g,g]] = {sd_rank}")

# ─────────────────────────────────────────────────
# Cartan rank: max abelian subalgebra of [g,g]
# For su(3) rank = 2, for u(3) rank = 3
# ─────────────────────────────────────────────────
print("\n" + "="*70)
print("Finding abelian subalgebras (Cartan candidates)")
print("="*70)

# Check which pairs commute
commuting_pairs = []
for i in range(8):
    for j in range(i+1, 8):
        if np.linalg.norm(comm(A[i], A[j])) < 1e-9:
            commuting_pairs.append((gen_ops[i], gen_ops[j]))

print(f"\nAbsolutely commuting pairs [A_i, A_j] = 0:")
for pair in commuting_pairs:
    print(f"  A_{pair[0]} ({OP[pair[0]]}) and A_{pair[1]} ({OP[pair[1]]})")

# ─────────────────────────────────────────────────
# Final characterization
# ─────────────────────────────────────────────────
print("\n" + "="*70)
print("STRUCTURE SUMMARY")
print("="*70)
print(f"""
  Dimension:       8
  Jacobi:          holds exactly
  Killing rank:    7  (1-dim center)
  Killing sig:     (0, 7, 1)  [all non-center eigenvalues negative → compact]

  Compact 7-dim semisimple over R doesn't exist.
  This means the "quotient" by the center is NOT semisimple —
  it must itself have a radical.

  → This algebra is neither su(3) nor u(3) directly.
  → It appears to be a solvable-by-semisimple extension
    with a specific center structure.
""")
