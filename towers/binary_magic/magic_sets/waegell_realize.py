"""
waegell_realize.py: an explicit few-qubit realization of each Waegell-Aravind Star, checked with matrices.
Find a magic Gram matrix of low rank (exhaustively when the Gram space is small, by random search when it
is not), factor it symplectically into Pauli strings on rank/2 qubits, then verify those strings directly:
commutation, products +-I and an odd number of negative contexts, using explicit matrices.
This does not rely on the Gram-rank theory: the realization is checked as a magic set on its own.
Prints ASCII only.
"""
import random, sys
from ms_core import gram_space, to_matrix_rows, rank_rows, pc, check_magic, verify_with_matrices, label
from waegell_stars import odd_kernel, even_kernel, star


def magic_points(V, ctxs, samples, seed=1):
    basis, var, f = gram_space(V, ctxs)
    fv = [pc(b & f) & 1 for b in basis]
    k0 = fv.index(1); base = basis[k0]
    others = [b ^ (base if fv[k] else 0) for k, b in enumerate(basis) if k != k0]
    rng = random.Random(seed)
    if len(others) <= 20:                                   # exhaustive
        x = base
        yield x, var
        for g in range(1, 1 << len(others)):
            x ^= others[(g & -g).bit_length() - 1]
            yield x, var
    else:
        for _ in range(samples):
            x = base
            for b in others:
                if rng.random() < 0.5:
                    x ^= b
            yield x, var


def factor(rows, V):
    """alternating F2 matrix (rows as bit masks) -> per-observable (x, z) masks on rank/2 qubits"""
    B = [[(rows[i] >> j) & 1 for j in range(V)] for i in range(V)]
    xs, zs, q = [0] * V, [0] * V, 0
    while True:
        piv = next(((a, b) for a in range(V) for b in range(V) if B[a][b]), None)
        if piv is None:
            return xs, zs, q
        a, b = piv
        col_b = [B[j][b] for j in range(V)]                 # x-coordinate of qubit q
        col_a = [B[a][j] for j in range(V)]                 # z-coordinate of qubit q
        for j in range(V):
            xs[j] |= col_b[j] << q; zs[j] |= col_a[j] << q
        for i in range(V):
            for j in range(V):
                B[i][j] ^= (col_b[i] & col_a[j]) ^ (col_a[i] & col_b[j])
        q += 1


def realize(name, obs, ctxs, samples=300000):
    V = len(obs)
    best = None
    for x, var in magic_points(V, ctxs, samples):
        rows = to_matrix_rows(x, var, V)
        r = rank_rows(rows)
        if best is None or r < best[0]:
            best = (r, rows)
            if r <= 4:
                break
    r, rows = best
    xs, zs, q = factor(rows, V)
    ops = list(zip(xs, zs))
    labels = [label(op, q) for op in ops]
    clash, neg, deg = check_magic(ops, ctxs)
    signs = verify_with_matrices(labels, ctxs)
    distinct = len(set(labels)) == V and all(set(l) != {"I"} for l in labels)
    print(f"{name}: lowest magic Gram rank found {r} -> {q} qubits; explicit {2**q}x{2**q} check:"
          f" parity clash = {clash and signs.count(-1) % 2 == 1}, negatives {signs.count(-1)} of {len(ctxs)},"
          f" all {V} observables distinct and non-identity = {distinct}")
    print("   ", " ".join(labels))
    return q, clash, distinct


if __name__ == "__main__":
    for N in [int(a) for a in sys.argv[1:]] or [4, 5, 6, 7]:
        sets = ([(f"odd Star N={N}", star(odd_kernel(N)))] if N % 2 else
                [(f"even Star N={N} (grouped, as in the thesis)", star(even_kernel(N), True)),
                 (f"even Star N={N} (all single-qubit factors)", star(even_kernel(N), False))])
        for name, (obs, ctxs) in sets:
            q, clash, distinct = realize(name, obs, ctxs)
            assert clash and q < N                              # a magic set on fewer than N qubits
    print("PASS: each Star is realized, and matrix-checked, on fewer than N qubits")
