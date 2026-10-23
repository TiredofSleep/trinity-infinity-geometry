"""
fold_proof_check.py — checks every step of the hand proof that every 4x4 magic square folds.

Notation. Rows/columns indexed 0..3 = 2-bit strings. Walsh characters chi_r(i) = (-1)^(r.i),
r in {01, 10, 11}. For a bit plane B (0/1), D = 1 - 2B (+-1), spectrum M(r,c) = sum D(i,j) chi_r(i) chi_c(j).
Assumption N (Conway-Norton-Ryba 'Nimm0'): every bit plane has exactly two 1s in every row and column.

Step 1  Under N, each row of D is +-chi_a for some a (its 'row type'), each column is +-chi_r.
        Spectrum is either TYPE I: one entry +-16, or TYPE II: a full 2x2 block of +-8 on
        rows {r : r.p = 1} x columns {a, b}.  Row types = spectrum columns; column types = spectrum rows.
Step 2  Distinct values => any two bit planes are orthogonal (sum D_k D_l = 0) => their spectra have
        zero inner product (Parseval).
Step 3  Corners + center hold half the total (diag + anti-diag = 2s) => sum_k 2^k n_k = 0 with
        n_k = M_k(11,11)/8 in {0, +-1, +-2}. A +-2 is a lone spike, which cannot be orthogonal to another
        plane that is nonzero at (11,11); with all |n_k| <= 1 the top term dominates. So every n_k = 0.
Step 4  Left-right mirror (j -> 3-j) multiplies chi_a by -1 for a in {01,10} and +1 for a = 11. A plane is
        symmetric or antisymmetric under it unless its spectrum columns mix 11 with 01/10 ('alpha' plane).
        Same for top-bottom with spectrum rows ('beta' plane).
Step 5  With Step 3, alpha = rows {01,10} x cols {11,x}; beta = rows {11,y} x cols {01,10}. Their supports
        meet in exactly one cell (y, x), where both are +-8 => not orthogonal => never in the same square.
Conclusion: no alpha plane (left-right fold) or no beta plane (top-bottom fold). Mask bit b_k = 1 iff
plane k is antisymmetric under that fold.
"""
import json
import numpy as np
from collections import Counter

squares = [np.array(s["square"]) for s in json.load(open("squares_4x4.json"))]
H = np.array([[(-1) ** bin(r & i).count("1") for i in range(4)] for r in range(4)])
R = {1: "01", 2: "10", 3: "11"}

def spectrum(D):
    return (H @ D @ H.T)[1:, 1:]          # 3x3 block, index 0,1,2 <-> r = 01, 10, 11

cnt = Counter(); s1 = s2 = s3 = s5 = fold_ok = True
for A in squares:
    planes = [1 - 2 * ((A >> k) & 1) for k in range(4)]
    specs = [spectrum(D) for D in planes]
    full = [H @ D @ H.T for D in planes]
    # assumption N
    assert all((((A >> k) & 1).sum(axis=0) == 2).all() and (((A >> k) & 1).sum(axis=1) == 2).all() for k in range(4))
    # step 1: type I / type II shapes
    for D, M in zip(planes, specs):
        nz = np.argwhere(M != 0)
        vals = sorted(set(np.abs(M[M != 0])))
        if len(nz) == 1:
            s1 &= vals == [16]; cnt["type I"] += 1
        else:
            rows, cols = set(nz[:, 0]), set(nz[:, 1])
            p_ok = any(rows == {r - 1 for r in (1, 2, 3) if bin(r & p).count("1") % 2} for p in (1, 2, 3))
            s1 &= len(nz) == 4 and len(rows) == 2 and len(cols) == 2 and vals == [8] and p_ok
            cnt["type II"] += 1
        s1 &= not full[0][0, 1:].any() and not full[0][1:, 0].any()
    # step 2: pairwise orthogonality, in space and in spectrum
    for k in range(4):
        for l in range(k + 1, 4):
            s2 &= (planes[k] * planes[l]).sum() == 0 and (specs[k] * specs[l]).sum() == 0
    # step 3: every plane is zero at (11,11)
    s3 &= all(M[2, 2] == 0 for M in specs)
    # step 4/5: classify planes, check alpha and beta never coexist, derive the fold
    def mixed(idx):
        return 2 in idx and len(idx & {0, 1}) > 0
    alpha = [mixed(set(np.argwhere(M != 0)[:, 1])) for M in specs]   # spectrum columns = row types
    beta = [mixed(set(np.argwhere(M != 0)[:, 0])) for M in specs]    # spectrum rows = column types
    s5 &= not (any(alpha) and any(beta))
    S = [int(A[x >> 2][x & 3]) for x in range(16)]
    for a, blocked in ((0b0011, any(alpha)), (0b1100, any(beta))):
        if not blocked:
            b = S[0] ^ S[a]
            fold_ok &= all(S[x ^ a] ^ S[x] == b for x in range(16))   # the predicted fold really holds
            # predicted mask: bit k flips iff plane k's types are all in {01,10} on the folded side
            for k, M in enumerate(specs):
                side = set(np.argwhere(M != 0)[:, 1 if a == 0b0011 else 0])
                fold_ok &= ((b >> k) & 1) == (1 if side <= {0, 1} else 0)
print("plane shapes:", dict(cnt))
print("step 1 (spectrum is a lone +-16 spike or a full +-8 2x2 block; axes empty):", s1)
print("step 2 (bit planes pairwise orthogonal):", s2)
print("step 3 (every plane zero at (11,11)):", s3)
print("step 5 (alpha and beta planes never coexist):", s5)
print("conclusion (predicted fold and mask hold exactly):", fold_ok)
assert s1 and s2 and s3 and s5 and fold_ok
