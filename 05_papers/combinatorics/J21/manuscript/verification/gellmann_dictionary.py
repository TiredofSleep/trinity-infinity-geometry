"""
FRONTIER COMPUTATION 1: Gell-Mann dictionary
=====================================================
Find explicit rational linear combinations of TIG operator 'action matrices'
that reproduce the 8 Gell-Mann matrices of su(3).

APPROACH:
  1. Build 10 "operator action matrices" — one per TIG operator.
     Each is the left-multiplication-by-op matrix in the CL table.
  2. Restrict to the 8-dimensional "root + Cartan" subspace
     (drop VOID and HARMONY — they are the u(1) center sector).
  3. Build the 8 Gell-Mann matrices λ_1..λ_8 (Hermitian, traceless, 3x3).
     But we're in 8x8 not 3x3, so use the ADJOINT representation
     of su(3), which IS 8-dimensional and is what acts on the Lie algebra.
  4. Solve the linear system: which rational combinations of TIG operator
     matrices (in adjoint basis) reproduce the adjoint Gell-Mann matrices?
"""
import numpy as np
from fractions import Fraction

CL = [
    [0,0,0,0,0,0,0,7,0,0],
    [0,7,3,7,7,7,7,7,7,7],
    [0,3,7,7,4,7,7,7,7,9],
    [0,7,7,7,7,7,7,7,7,3],
    [0,7,4,7,7,7,7,7,8,7],
    [0,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,8,7,7,7,7,7],
    [0,7,9,3,7,7,7,7,7,7],
]

OP = ['VOID','LATTICE','COUNTER','PROGRESS','COLLAPSE',
      'BALANCE','CHAOS','HARMONY','BREATH','RESET']

# ─────────────────────────────────────────────────
# Build the 10 action matrices L_op:
# (L_op)_{ij} = 1 if CL[op][j] == i else 0
# So L_op is a 10x10 matrix representing "left-multiplication by op"
# acting as a linear operator on the 10-dim free vector space with basis {e_0..e_9}.
# ─────────────────────────────────────────────────
def action_matrix(op):
    M = np.zeros((10, 10), dtype=int)
    for j in range(10):
        result = CL[op][j]
        M[result, j] = 1
    return M

L = [action_matrix(op) for op in range(10)]

print("="*70)
print("TIG operator action matrices L_op")
print("="*70)
for op in range(10):
    rank = np.linalg.matrix_rank(L[op])
    trace = int(np.trace(L[op]))
    print(f"  L_{op} = {OP[op]:<10s} rank={rank}  trace={trace}")

# The key observation: HARMONY's action matrix has ALL 7s as target,
# so L_7 maps every basis vector to e_7 — rank 1, trace 1.
# VOID's action is mostly to 0 with CL[0][7]=7, so also low-rank.

# Commutators [L_i, L_j]
print("\n" + "="*70)
print("Operator action matrices commutate pattern [L_i, L_j]")
print("="*70)
print("For TIG to be a Lie algebra in action-matrix form, we need")
print("  [L_i, L_j] = Σ_k c_ijk L_k   (structure constants)")
print()
print("Let's check this on a sample pair and measure the closure defect.")

def commutator(A, B):
    return A @ B - B @ A

# Sample commutators
pairs_to_check = [(1,2), (3,4), (6,8), (5,9), (1,7), (0,7)]
for i, j in pairs_to_check:
    C = commutator(L[i], L[j])
    Cnorm = np.linalg.norm(C)
    # Try to express C in the L_k basis
    # Stack L's as columns of a matrix A (100 x 10)
    A = np.stack([L[k].flatten() for k in range(10)], axis=1).astype(float)
    b = C.flatten().astype(float)
    # Solve A x = b via least squares
    x, residuals, rank, _ = np.linalg.lstsq(A, b, rcond=None)
    fit = A @ x
    fit_err = np.linalg.norm(fit - b)
    print(f"  [L_{i}, L_{j}]  ||C||={Cnorm:6.2f}  "
          f"LSTSQ rank={rank}  fit residual={fit_err:.4f}")
    if fit_err < 0.5 and Cnorm > 0.1:
        print(f"    -> expressible in L basis, coefficients:")
        for k in range(10):
            if abs(x[k]) > 0.05:
                print(f"       {x[k]:+.4f} · L_{k} ({OP[k]})")

print()
print("="*70)
print("Does the span of {L_0..L_9} close under commutators?")
print("="*70)

# Check: does every commutator [L_i, L_j] lie in span{L_0..L_9}?
closure_defects = []
for i in range(10):
    for j in range(i+1, 10):
        C = commutator(L[i], L[j])
        if np.linalg.norm(C) < 1e-9:
            continue
        A = np.stack([L[k].flatten() for k in range(10)], axis=1).astype(float)
        b = C.flatten().astype(float)
        x, *_ = np.linalg.lstsq(A, b, rcond=None)
        fit_err = float(np.linalg.norm(A @ x - b))
        if fit_err > 0.01:
            closure_defects.append(((i, j), fit_err))

print(f"  Pairs (i,j) whose commutator is NOT in span{{L_k}}: "
      f"{len(closure_defects)}/{10*9//2}")
for (pair, err) in closure_defects[:5]:
    print(f"    {pair}: residual {err:.4f}")

print()
print("="*70)
print("INTERPRETATION")
print("="*70)
print("""
If MANY commutators are not in span{L_k}, then the L's don't form a Lie
subalgebra directly. This is EXPECTED: the L's are the LEFT-REGULAR
representation, not the Lie-algebra action.

The right move is to work with the *differences* (L_i - L_j) on the
6-dim flow subspace, or to find the adjoint representation explicitly.

Let's try that next: restrict to the root+Cartan subspace and rebuild.
""")
