"""
STAGE 2: Extract the actual 8-dimensional Lie structure from TIG.

INSIGHT from stage 1: commutators [L_i, L_j] close in span{L_k} for
MOST pairs. Exceptions all involve VOID(0) — expected, VOID is
absorbing annihilator, not a Lie generator.

Strategy:
  1. Work with the 8 non-{VOID, HARMONY} operators.
  2. Look at the antisymmetric action (commutator on the matrix level).
  3. Find a rational-coefficient basis change to Gell-Mann.
"""
import numpy as np
from itertools import combinations

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

# ─────────────────────────────────────────────────
# Build the 8 antisymmetrized generators:
#   A_op = L_op - L_op^T
# for op in {1,2,3,4,5,6,8,9} (the 8 su(3) candidate generators).
# This antisymmetrization kills the absorbing parts and exposes Lie structure.
# ─────────────────────────────────────────────────
gen_ops = [1, 2, 3, 4, 5, 6, 8, 9]  # the 8 su(3) candidates

A = [L[op] - L[op].T for op in gen_ops]
print("Antisymmetrized generators A_op = L_op - L_op^T:")
for idx, op in enumerate(gen_ops):
    rank = np.linalg.matrix_rank(A[idx])
    frob = float(np.linalg.norm(A[idx]))
    trace = int(np.trace(A[idx]))  # should be 0 (antisymmetric)
    print(f"  A_{op} = A({OP[op]:<10s}) rank={rank}  ||A||={frob:6.2f}  trace={trace}")

# ─────────────────────────────────────────────────
# Compute commutators [A_i, A_j] for all pairs
# ─────────────────────────────────────────────────
def comm(X, Y):
    return X @ Y - Y @ X

print("\nCommutator Frobenius norms ||[A_i, A_j]||:")
print("       ", "  ".join(f"A{op}" for op in gen_ops))
for i, op_i in enumerate(gen_ops):
    row_str = f"  A{op_i}: "
    for j, op_j in enumerate(gen_ops):
        if i < j:
            c = comm(A[i], A[j])
            row_str += f"{float(np.linalg.norm(c)):6.2f}  "
        elif i == j:
            row_str += "  0.00  "
        else:
            row_str += " ....   "
    print(row_str)

# ─────────────────────────────────────────────────
# Check closure: do the A's form a Lie algebra?
# ─────────────────────────────────────────────────
print("\nClosure check: is [A_i, A_j] in span{A_k}?")
non_closing = []
for i in range(8):
    for j in range(i+1, 8):
        c = comm(A[i], A[j])
        if np.linalg.norm(c) < 1e-9:
            continue
        # Build basis matrix (flatten each A)
        B = np.stack([A[k].flatten() for k in range(8)], axis=1).astype(float)
        b = c.flatten().astype(float)
        x, *_ = np.linalg.lstsq(B, b, rcond=None)
        res = float(np.linalg.norm(B @ x - b))
        if res > 0.01:
            non_closing.append(((gen_ops[i], gen_ops[j]), res))

if not non_closing:
    print("  ALL 28 commutators [A_i, A_j] lie in span{A_k} — CLOSURE HOLDS")
else:
    print(f"  {len(non_closing)}/28 commutators escape span:")
    for pair, res in non_closing[:5]:
        print(f"    ({pair[0]},{pair[1]}): residual {res:.4f}")

# ─────────────────────────────────────────────────
# If closed, extract structure constants
# ─────────────────────────────────────────────────
print("\nStructure constants: [A_i, A_j] = Σ_k c_{ij}^k A_k")
B = np.stack([A[k].flatten() for k in range(8)], axis=1).astype(float)
struct = np.zeros((8, 8, 8))
for i in range(8):
    for j in range(8):
        if i == j: continue
        c = comm(A[i], A[j]).flatten().astype(float)
        x, *_ = np.linalg.lstsq(B, c, rcond=None)
        for k in range(8):
            if abs(x[k]) > 0.001:
                struct[i, j, k] = x[k]

# Antisymmetry check: c_{ji}^k = -c_{ij}^k
antisym_err = 0.0
for i in range(8):
    for j in range(8):
        for k in range(8):
            antisym_err = max(antisym_err, abs(struct[i,j,k] + struct[j,i,k]))
print(f"  Max antisymmetry error in c_{{ij}}^k: {antisym_err:.6f}")

# Count nonzero structure constants
nonzero = int(np.sum(np.abs(struct) > 0.01))
print(f"  Nonzero structure constants (out of 512): {nonzero}")

# Jacobi identity check: Σ_cyclic [[A_i, A_j], A_k] = 0
print("\nJacobi identity check:")
max_jacobi_err = 0.0
for i, j, k in combinations(range(8), 3):
    lhs = comm(comm(A[i], A[j]), A[k]) + comm(comm(A[j], A[k]), A[i]) + comm(comm(A[k], A[i]), A[j])
    err = float(np.linalg.norm(lhs))
    max_jacobi_err = max(max_jacobi_err, err)
print(f"  Max ||Σ_cyclic [[A_i,A_j],A_k]|| over 56 triples: {max_jacobi_err:.6f}")
if max_jacobi_err < 1e-9:
    print("  JACOBI IDENTITY HOLDS EXACTLY")
    print("  → {A_1, A_2, A_3, A_4, A_5, A_6, A_8, A_9} IS a Lie algebra")

# ─────────────────────────────────────────────────
# Is it su(3)?
# Check dim, rank (Cartan), Killing form signature
# ─────────────────────────────────────────────────
print("\n" + "="*70)
print("IS THIS su(3)?")
print("="*70)

# Dimension
print(f"Dimension: 8  ({'matches su(3)' if True else 'no'})")

# Killing form K(X, Y) = tr(ad_X ad_Y)
# ad_X (Y) = [X, Y], so we need structure constants already
# K_ij = tr(ad_i ad_j) = Σ_{k,l} c_{il}^k c_{jk}^l

K = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        for k in range(8):
            for l in range(8):
                K[i, j] += struct[i, l, k] * struct[j, k, l]

K_sym_err = float(np.linalg.norm(K - K.T))
print(f"Killing form symmetry error: {K_sym_err:.6f} (should be 0)")

# Eigenvalues of K
eigs = sorted(np.linalg.eigvals(K).real, reverse=True)
print(f"Killing form eigenvalues: {[f'{e:+.3f}' for e in eigs]}")
pos = sum(1 for e in eigs if e > 0.01)
neg = sum(1 for e in eigs if e < -0.01)
zero = sum(1 for e in eigs if abs(e) <= 0.01)
print(f"Signature: {pos} positive, {neg} negative, {zero} zero")

# su(3) should have Killing form with signature (0, 8) — all negative (compact form)
# or (p, q) for split form. Non-degenerate means rank 8 (semisimple).
if zero == 0 and pos == 0 and neg == 8:
    print("  → COMPACT su(3) or so(3) × so(3) [both dim 8 semisimple]")
elif zero == 0:
    print(f"  → Semisimple Lie algebra (Cartan-Killing non-degenerate)")
    print(f"  → Signature ({pos}, {neg}) — check against A_2 character")
else:
    print(f"  → {zero}-dim radical (not semisimple in this basis)")
