"""Referee core: Pauli strings, matrices, symplectic vectors, F2 linear algebra.
Written from scratch; no code from the claimant's directory is used."""
import json
import itertools
import numpy as np

P1 = {
    'I': np.eye(2, dtype=complex),
    'X': np.array([[0, 1], [1, 0]], dtype=complex),
    'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
    'Z': np.array([[1, 0], [0, -1]], dtype=complex),
}
# symplectic bits (x, z)
XZ = {'I': (0, 0), 'X': (1, 0), 'Y': (1, 1), 'Z': (0, 1)}


def mat(s):
    m = np.array([[1]], dtype=complex)
    for ch in s:  # qubit 0 = leftmost tensor factor
        m = np.kron(m, P1[ch])
    return m


def vec(s):
    """Symplectic vector as python int: bits 0..n-1 = x, bits n..2n-1 = z."""
    n = len(s)
    v = 0
    for q, ch in enumerate(s):
        x, z = XZ[ch]
        v |= x << q
        v |= z << (n + q)
    return v


def symp(u, v, n):
    mask = (1 << n) - 1
    ux, uz = u & mask, u >> n
    vx, vz = v & mask, v >> n
    return (bin(ux & vz).count('1') + bin(uz & vx).count('1')) & 1


# ---------------- F2 linear algebra on python-int bit rows ----------------
def f2_rank(rows):
    piv = {}  # highest-bit pivot -> row
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h]
            else:
                piv[h] = r
                break
    return len(piv)


def f2_in_span(rows, target):
    piv = {}
    for r in rows:
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h]
            else:
                piv[h] = r
                break
    t = target
    while t:
        h = t.bit_length() - 1
        if h in piv:
            t ^= piv[h]
        else:
            return False
    return True


def f2_nullspace(rows, nvars):
    """rows: list of int bitmasks (equations sum_j a_j v_j = 0). Return basis of solution space."""
    # Gaussian elimination to RREF
    piv_rows = {}  # pivot col -> row
    for r in rows:
        for c, pr in piv_rows.items():
            if (r >> c) & 1:
                r ^= pr
        if r == 0:
            continue
        c = r.bit_length() - 1  # pivot = highest bit
        # eliminate this pivot from existing rows
        for c2 in list(piv_rows):
            if (piv_rows[c2] >> c) & 1:
                piv_rows[c2] ^= r
        piv_rows[c] = r
    free = [j for j in range(nvars) if j not in piv_rows]
    basis = []
    for f in free:
        v = 1 << f
        for c, pr in piv_rows.items():
            # row: x_c + sum_{other bits} = 0 -> x_c = sum of other bits present in v
            if (pr >> f) & 1:
                v |= 1 << c
        basis.append(v)
    return basis


def mat_rank_f2(M):
    """M: list of lists 0/1 -> rank over F2"""
    rows = []
    for row in M:
        r = 0
        for j, b in enumerate(row):
            if b & 1:
                r |= 1 << j
        rows.append(r)
    return f2_rank(rows)


def load_sets(path):
    with open(path) as f:
        return json.load(f)


def observables_of(contexts):
    obs = []
    seen = set()
    for c in contexts:
        for o in c:
            if o not in seen:
                seen.add(o)
                obs.append(o)
    return obs
