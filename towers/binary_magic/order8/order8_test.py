"""
order8_test.py — does the 4x4 structure survive at order 8 (values 0..63, 6 bit planes, lines of 8)?

Part A: 2,000 annealed 8x8 magic squares (no built-in binary structure).
  - rows/columns bit-balanced (4 ones per plane per line)?  [order-4: always, Conway-Norton-Ryba]
  - rows/columns XOR to 0?
  - carries per line: size and shape
  - folds: A(x xor a) = A(x) xor b for some nonzero position shift a?  [order-4: always]
  - singular?
Part B: exact count of affine, fully binary magic squares (value bits = XOR of position bits),
  checked against 432 at order 4.
"""
import itertools
import numpy as np
from collections import Counter

sq = [np.array(list(map(int, l.split()))).reshape(8, 8) for l in open("squares8_annealed.txt")]
assert all(sorted(A.flatten()) == list(range(64)) for A in sq)
LINES = [[(i, j) for j in range(8)] for i in range(8)] + [[(i, j) for i in range(8)] for j in range(8)] + \
        [[(i, i) for i in range(8)], [(i, 7 - i) for i in range(8)]]
assert all(sum(A[i][j] for i, j in L) == 252 for A in sq for L in LINES)

def carries(vals):
    d = [sum((v >> k) & 1 for v in vals) - 4 for k in range(6)]
    a = []
    prev = 0
    for k in range(5):                      # d_k = a_{k-1} - 2 a_k
        ak = (prev - d[k]) // 2
        assert (prev - d[k]) % 2 == 0
        a.append(ak); prev = ak
    assert d[5] == prev
    return a

rc_bal = rc_xor0 = 0; max_carry = Counter(); shape = Counter(); fold = Counter(); sing = 0
for A in sq:
    lines_rc = LINES[:16]
    if all(sum((A[i][j] >> k) & 1 for i, j in L) == 4 for L in lines_rc for k in range(6)):
        rc_bal += 1
    if all(np.bitwise_xor.reduce([A[i][j] for i, j in L]) == 0 for L in lines_rc):
        rc_xor0 += 1
    for L in LINES:
        a = carries([A[i][j] for i, j in L])
        max_carry[max(abs(x) for x in a)] += 1
        nz = [x for x in a if x]
        if nz:
            same_sign = all(x > 0 for x in nz) or all(x < 0 for x in nz)
            used = [k for k, x in enumerate(a) if x]
            contiguous = used == list(range(used[0], used[-1] + 1))
            shape[(same_sign, contiguous)] += 1
    S = [int(A[x >> 3][x & 7]) for x in range(64)]
    tr = [(a, S[0] ^ S[a]) for a in range(1, 64) if all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for x in range(64))]
    fold["has an XOR symmetry" if tr else "none"] += 1
    sing += abs(np.linalg.det(A)) < 0.5
n = len(sq)
print(f"A. {n} annealed 8x8 magic squares")
print(f"   rows+cols bit-balanced: {rc_bal}   rows+cols XOR to 0: {rc_xor0}")
print(f"   largest carry on a line (all 18 lines): {dict(sorted(max_carry.items()))}")
print(f"   carrying lines (same sign?, contiguous?): {dict(shape)}")
print(f"   folds: {dict(fold)}   singular: {sing}")

# Part B: affine fully binary magic squares. A plane = linear form w = (w_row, w_col) on position bits
# (plus a constant). Balanced on every row iff w_col != 0, every column iff w_row != 0,
# both diagonals iff w_row != w_col.  Square = 2m independent such forms + a constant.
def gf2_rank(vecs):
    rows = list(vecs); r = 0; nb = max(v.bit_length() for v in rows) if rows else 0
    for bit in reversed(range(nb)):
        piv = next((i for i in range(r, len(rows)) if (rows[i] >> bit) & 1), None)
        if piv is None: continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] >> bit) & 1: rows[i] ^= rows[r]
        r += 1
    return r
def affine_count(m):                         # order 2^m, 2m bits
    allowed = [(wr << m) | wc for wr in range(1, 2 ** m) for wc in range(1, 2 ** m) if wr != wc]
    nb = 2 * m
    # count ordered bases from 'allowed' by DFS over spans
    def count(chosen, span):
        if len(chosen) == nb: return 1
        tot = 0
        for v in allowed:
            if v not in span:
                newspan = span | {s ^ v for s in span}
                tot += count(chosen + [v], newspan)
        return tot
    bases = count([], {0})
    return bases * 2 ** nb // 8              # constants, then divide by the 8 rotations/reflections
c4 = affine_count(2)
print(f"\nB. affine fully binary magic squares: order 4 -> {c4} (expected 432)")
assert c4 == 432
