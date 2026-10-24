"""
gram_np.py: the minimum magic Gram rank (TLC Cor. 10), vectorized with numpy. Same Gram space as ms_core.py;
the walk over the magic coset is done in batches, with GF(2) ranks computed for a whole batch at once.
min_rank_np(V, ctxs, stop_at) returns (best rank found, Gram-space dimension, how):
  how = "none" (no magic Gram matrix), "found" (a point of rank <= stop_at was found, so the minimum is at most
  that), "exhaustive" (every magic point was checked, so best is the exact minimum), or "sampled" (the space was
  too big to exhaust and no low-rank point turned up).
"""
import numpy as np
from ms_core import gram_space, to_matrix_rows, pc


def batch_rank(R):
    """GF(2) rank of each matrix in a batch; R has shape (B, V), each row a bit mask (int64)"""
    R = R.copy()
    B, V = R.shape
    rank = np.zeros(B, dtype=np.int64)
    idx = np.arange(B)
    for bit in range(V - 1, -1, -1):
        has = (R >> bit) & 1
        anyb = has.any(axis=1)
        pivot = R[idx, has.argmax(axis=1)] * anyb
        R ^= has * pivot[:, None]                    # the pivot row clears itself, so it leaves the set
        rank += anyb
    return rank


def min_rank_np(V, ctxs, stop_at=None, exhaust_dim=26, samples=1 << 15, batch=1 << 14, seed=7):
    basis, var, f = gram_space(V, ctxs)
    d = len(basis)
    fv = [pc(b & f) & 1 for b in basis]
    if not any(fv):
        return None, d, "none"
    k0 = fv.index(1)
    base = basis[k0]
    others = [b ^ (base if fv[k] else 0) for k, b in enumerate(basis) if k != k0]
    m = len(others)
    base_rows = np.array(to_matrix_rows(base, var, V), dtype=np.int64)
    delta = np.array([to_matrix_rows(o, var, V) for o in others], dtype=np.int64).reshape(m, V)

    def ranks(g):
        R = np.tile(base_rows, (len(g), 1))
        for j in range(m):
            R ^= ((g >> j) & 1)[:, None] * delta[j][None, :]
        return batch_rank(R)

    best = V + 1
    rng = np.random.default_rng(seed)
    if m > 20:                                      # a quick random look first, when the space is large
        for _ in range(samples // batch):
            g = rng.integers(0, 1 << min(m, 62), size=batch, dtype=np.int64)
            best = min(best, int(ranks(g).min()))
            if stop_at is not None and best <= stop_at:
                return best, d, "found"
    if d > exhaust_dim:
        return best, d, "sampled"
    total = 1 << m
    for start in range(0, total, batch):
        g = np.arange(start, min(total, start + batch), dtype=np.int64)
        best = min(best, int(ranks(g).min()))
        if stop_at is not None and best <= stop_at:
            return best, d, "found"
    return best, d, "exhaustive"
