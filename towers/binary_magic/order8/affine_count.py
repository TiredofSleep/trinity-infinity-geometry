"""
affine_count.py — exact count of affine, fully binary magic squares of order 2^m.

A square on 0..4^m-1 is affine if each value bit is an XOR of position bits (plus a constant).
Each value bit is a linear form w = (w_row, w_col) on the 2m position bits. It is balanced on
every row iff w_col != 0, on every column iff w_row != 0, and on both diagonals iff w_row != w_col.
So the fully binary affine squares = (ordered bases of GF(2)^{2m} drawn from the allowed forms)
x (2^{2m} constants), divided by the 8 rotations/reflections.
Counting ordered bases: dynamic programming over subspaces (memoized on the span).
"""
from functools import lru_cache

def count_affine(m):
    nb = 2 * m
    allowed = [(wr << m) | wc for wr in range(1, 2 ** m) for wc in range(1, 2 ** m) if wr != wc]
    def reduce_basis(basis):
        basis = sorted(basis, reverse=True)
        out = []
        for v in basis:
            for b in out:
                v = min(v, v ^ b)
            if v:
                out.append(v)
                out = sorted(out, reverse=True)
        # canonical: reduced echelon
        out = sorted(out, reverse=True)
        for i in range(len(out)):
            for j in range(len(out)):
                if i != j and (out[j] ^ out[i]) < out[j] and out[i].bit_length() <= out[j].bit_length():
                    hb = 1 << (out[i].bit_length() - 1)
                    if out[j] & hb:
                        out[j] ^= out[i]
        return tuple(sorted(out, reverse=True))
    def span(basis):
        s = {0}
        for b in basis:
            s |= {x ^ b for x in s}
        return frozenset(s)
    @lru_cache(maxsize=None)
    def f(sp):
        if len(sp) == 2 ** nb:
            return 1
        tot = 0
        for v in allowed:
            if v not in sp:
                tot += f(frozenset(sp | {x ^ v for x in sp}))
        return tot
    bases = f(frozenset({0}))
    return bases, bases * 2 ** nb // 8, len(allowed)

for m in (2, 3):
    bases, squares, nallowed = count_affine(m)
    print(f"order {2**m}: {nallowed} allowed value-bit patterns, {bases:,} ordered bases -> "
          f"{squares:,} affine fully binary magic squares (up to rotation/reflection)")
