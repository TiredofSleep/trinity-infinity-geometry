"""
ms_core.py — toolkit for Pauli magic sets (Trandafir–Lisoněk–Cabello, arXiv:2202.13141).

Pauli operator on n qubits = (x, z) bit masks; Hermitian representative i^{|x&z|} X^x Z^z.
A context is a list of operator indices; a magic set is (ops, contexts) with every operator in an even
number of contexts and an odd number of negative contexts.
Qubit count: half the minimum binary rank over magic Gram matrices in the valid Gram space (their Cor. 10).
"""
import itertools
import numpy as np

pc = lambda x: bin(x).count("1")
def symp(a, b):  return (pc(a[0] & b[1]) + pc(a[1] & b[0])) & 1
def label(op, n):
    x, z = op
    return "".join("IXZY"[((x >> q) & 1) | (((z >> q) & 1) << 1)] for q in range(n))
def parse(s):
    x = z = 0
    for q, ch in enumerate(s):
        if ch in "XY": x |= 1 << q
        if ch in "ZY": z |= 1 << q
    return (x, z)

def product_sign(ops):
    """sign of the product of the Hermitian representatives, in the given order (must be +-I)"""
    p, x, z = 0, 0, 0
    for (x2, z2) in ops:
        p2 = pc(x2 & z2)
        p = (p + p2 + 2 * pc(z & x2)) % 4
        x ^= x2; z ^= z2
    assert x == 0 and z == 0 and p in (0, 2), "context does not multiply to +-I"
    return 1 if p == 0 else -1

def check_magic(ops, ctxs):
    """returns (is_parity_clash, negatives, degrees)"""
    for c in ctxs:
        assert all(symp(ops[a], ops[b]) == 0 for a, b in itertools.combinations(c, 2)), "non-commuting context"
    deg = [0] * len(ops)
    for c in ctxs:
        for v in c: deg[v] += 1
    neg = [i for i, c in enumerate(ctxs) if product_sign([ops[v] for v in c]) == -1]
    return all(d % 2 == 0 for d in deg) and len(neg) % 2 == 1, neg, deg

def noncontextual_bound(nv, ctxs, negs):
    """b = |E| - 2 * w_min, w_min = fewest contexts any +-1 assignment must violate (brute force, nv <= 26)"""
    A = np.zeros((len(ctxs), nv), dtype=np.uint8)
    for e, c in enumerate(ctxs): A[e, list(c)] = 1
    s = np.zeros(len(ctxs), dtype=np.uint8); s[list(negs)] = 1
    best = len(ctxs)
    chunk = 1 << min(nv, 20)
    for start in range(0, 1 << nv, chunk):
        xs = (np.arange(start, start + chunk)[:, None] >> np.arange(nv)[None, :]) & 1
        viol = ((xs.astype(np.uint8) @ A.T) + s) % 2
        best = min(best, int(viol.sum(1).min()))
    return len(ctxs) - 2 * best

# ---------------------------------------------------------------- F2 linear algebra on Python ints
def nullspace(rows, nvar):
    """basis of {x : r·x = 0 for all rows}; rows and returned vectors are int bit masks over nvar bits"""
    piv = {}
    for r in rows:
        for b, pr in piv.items():
            if r >> b & 1: r ^= pr
        if r == 0: continue
        b = r.bit_length() - 1
        for b2 in list(piv):
            if piv[b2] >> b & 1: piv[b2] ^= r
        piv[b] = r
    free = [v for v in range(nvar) if v not in piv]
    basis = []
    for f in free:
        x = 1 << f
        for b, pr in piv.items():
            if pr >> f & 1: x |= 1 << b
        basis.append(x)
    return basis
def rank_rows(rows):
    rows = [r for r in rows if r]; rank = 0
    while rows:
        p = max(rows); hb = p.bit_length() - 1
        rows = [r ^ p if r >> hb & 1 else r for r in rows if r != p]
        rows = [r for r in rows if r]; rank += 1
    return rank

def gram_space(nv, ctxs):
    """valid Gram space as a basis of variable vectors, the variable list (pairs), and the magic functional"""
    share = set()
    for c in ctxs:
        for a, b in itertools.combinations(sorted(c), 2): share.add((a, b))
    var = [(i, j) for i in range(nv) for j in range(i + 1, nv) if (i, j) not in share]
    vid = {p: k for k, p in enumerate(var)}
    rows = []
    for c in ctxs:
        cs = set(c)
        for j in range(nv):
            if j in cs: continue
            r = 0
            for i in c:
                p = (min(i, j), max(i, j))
                if p in vid: r ^= 1 << vid[p]
            if r: rows.append(r)
    basis = nullspace(rows, len(var))
    seq = [v for c in ctxs for v in c]                       # Theorem 7: concatenated entries
    f = 0
    for p in range(len(seq)):
        for q in range(p + 1, len(seq)):
            a, b = seq[p], seq[q]
            if a > b:
                key = (b, a)
                if key in vid: f ^= 1 << vid[key]
    return basis, var, f

def to_matrix_rows(x, var, nv):
    R = [0] * nv
    for k, (i, j) in enumerate(var):
        if x >> k & 1: R[i] ^= 1 << j; R[j] ^= 1 << i
    return R

def min_magic_rank(nv, ctxs, limit_dim=26, stop_at=None):
    """minimum binary rank over magic Gram matrices (exhaustive over the affine space). Returns (rank, dim)."""
    basis, var, f = gram_space(nv, ctxs)
    d = len(basis)
    fv = [pc(b & f) & 1 for b in basis]
    if not any(fv): return None, d                            # no magic Gram matrix at all
    if d > limit_dim: return "too big", d
    k0 = fv.index(1)                                          # a magic base point; the rest: an even-f subspace
    base = basis[k0]
    others = [b ^ (base if fv[k] else 0) for k, b in enumerate(basis) if k != k0]
    best = nv
    # Gray-code walk over the 2^(d-1) magic matrices, rank of each
    x = base; best = rank_rows(to_matrix_rows(x, var, nv))
    for g in range(1, 1 << len(others)):
        bit = (g & -g).bit_length() - 1
        x ^= others[bit]
        r = rank_rows(to_matrix_rows(x, var, nv))
        if r < best:
            best = r
            if stop_at is not None and best <= stop_at: break
    return best, d

def gram_of(ops):
    return [sum(symp(a, b) << j for j, b in enumerate(ops)) for a in ops]

# ---------------------------------------------------------------- explicit matrices (independent check)
P1 = {"I": np.eye(2), "X": np.array([[0, 1], [1, 0]]), "Z": np.diag([1, -1]), "Y": np.array([[0, -1j], [1j, 0]])}
def matrix(lbl):
    M = np.array([[1]])
    for ch in lbl: M = np.kron(M, P1[ch])
    return M
def verify_with_matrices(labels, ctxs):
    """commutation, products = +-I and signs, computed with explicit complex matrices"""
    Ms = [matrix(l) for l in labels]; dim = Ms[0].shape[0]
    signs = []
    for c in ctxs:
        for a, b in itertools.combinations(c, 2):
            assert np.allclose(Ms[a] @ Ms[b], Ms[b] @ Ms[a])
        P = np.eye(dim)
        for v in c: P = P @ Ms[v]
        if np.allclose(P, np.eye(dim)): signs.append(1)
        elif np.allclose(P, -np.eye(dim)): signs.append(-1)
        else: raise AssertionError("context product is not +-I")
    return signs
