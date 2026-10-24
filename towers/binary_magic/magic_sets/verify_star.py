"""
verify_star.py — independent check that an X/Y star set needs all n qubits (no shared code with
gram_space / min_magic_rank / the Theorem 7 functional).

Any Pauli assignment of a star set is fixed by its single-qubit observables, since each M_S is the product of
the singles in its local context. Its Gram matrix G is alternating over F2 and its rank = 2 x (qubits used).
Steps: solve the linear commutation constraints for G; enumerate the whole solution space; realise every
solution as explicit Pauli operators; multiply out every context; count negatives.
Genuine n-qubit <=> no solution of rank < 2n has an odd number of negative contexts.
"""
import itertools, sys
import numpy as np
from ms_core import product_sign, verify_with_matrices, symp, label

def star_parts(n, F):
    singles = sorted({(("Y" if q in S else "X"), q) for S in F for q in range(n)}, key=lambda s: (s[1], s[0]))
    sid = {s: k for k, s in enumerate(singles)}
    local = [[sid[("Y" if q in S else "X", q)] for q in range(n)] for S in F]
    return singles, local

def solve_f2(rows, nvar):
    """all solutions of rows·x = 0 over F2: returns a basis (list of int masks)"""
    piv = {}
    for r in rows:
        for b, pr in piv.items():
            if r >> b & 1: r ^= pr
        if not r: continue
        b = r.bit_length() - 1
        for b2 in list(piv):
            if piv[b2] >> b & 1: piv[b2] ^= r
        piv[b] = r
    basis = []
    for f in (v for v in range(nvar) if v not in piv):
        x = 1 << f
        for b, pr in piv.items():
            if pr >> f & 1: x |= 1 << b
        basis.append(x)
    return basis

def f2rank(G):
    A = (G % 2).astype(np.uint8); r = 0
    for c in range(A.shape[1]):
        p = next((i for i in range(r, A.shape[0]) if A[i, c]), None)
        if p is None: continue
        A[[r, p]] = A[[p, r]]
        for i in range(A.shape[0]):
            if i != r and A[i, c]: A[i] ^= A[r]
        r += 1
    return r

def realise(G):
    m = G.shape[0]; B = lambda u, w: int(u @ G @ w) % 2
    pool = [np.eye(m, dtype=np.int64)[i] for i in range(m)]; pairs = []
    while True:
        hit = next(((u, w) for u in pool for w in pool if B(u, w)), None)
        if hit is None: break
        e, f = hit; pairs.append((e, f))
        pool = [v for v in ((u + B(u, f) * e + B(u, e) * f) % 2 for u in pool) if v.any()]
    ops = [(sum(B(np.eye(m, dtype=np.int64)[i], f) << a for a, (e, f) in enumerate(pairs)),
            sum(B(e, np.eye(m, dtype=np.int64)[i]) << a for a, (e, f) in enumerate(pairs))) for i in range(m)]
    assert all(symp(ops[i], ops[j]) == G[i, j] for i in range(m) for j in range(m))
    return len(pairs), ops

def verify(n, F, verbose=True):
    singles, local = star_parts(n, F)
    m = len(singles); L = len(F)
    ctxs = [tuple(range(m, m + L))] + [tuple(local[k]) + (m + k,) for k in range(L)]
    # actual operators: explicit matrices (feasible up to ~ 10 qubits)
    lab = lambda s: "".join(s[0] if r == s[1] else "I" for r in range(n))
    labels = [lab(s) for s in singles] + ["".join("Y" if q in S else "X" for q in range(n)) for S in F]
    if n <= 9:
        signs = verify_with_matrices(labels, ctxs)
        assert signs.count(-1) % 2 == 1
    deg = [sum(v in c for c in ctxs) for v in range(m + L)]
    assert all(d % 2 == 0 for d in deg) and len(set(labels)) == len(labels)
    # free Gram entries: single pairs never in a common local context
    co = {tuple(sorted(p)) for Lc in local for p in itertools.combinations(Lc, 2)}
    free = [(a, b) for a in range(m) for b in range(a + 1, m) if (a, b) not in co]
    fid = {p: k for k, p in enumerate(free)}
    rows = []
    for s, t in itertools.combinations(range(L), 2):             # M_s, M_t commute
        r = 0
        for a in local[s]:
            for b in local[t]:
                if a != b:
                    p = (min(a, b), max(a, b))
                    if p in fid: r ^= 1 << fid[p]
        if r: rows.append(r)
    basis = solve_f2(rows, len(free))
    tally = {}
    for coeffs in range(1 << len(basis)):
        x = 0
        for k, b in enumerate(basis):
            if coeffs >> k & 1: x ^= b
        G = np.zeros((m, m), dtype=np.int64)
        for k, (a, b) in enumerate(free):
            if x >> k & 1: G[a, b] = G[b, a] = 1
        r = f2rank(G); q, ops = realise(G); assert 2 * q == r
        allops = ops + [tuple(int(v) for v in np.bitwise_xor.reduce(np.array([ops[a] for a in Lc]), axis=0)) for Lc in local]
        neg = sum(product_sign([allops[v] for v in c]) == -1 for c in ctxs)
        tally.setdefault(r // 2, [0, 0])[neg % 2] += 1
    genuine = all(v[1] == 0 for qb, v in tally.items() if qb < n) and tally.get(n, [0, 0])[1] > 0
    if verbose:
        print(f"n={n}, |F|={L}: {m + L} observables, {L + 1} contexts; {len(free)} free Gram entries,"
              f" solution space 2^{len(basis)}; qubits -> [even, odd negatives]: {dict(sorted(tally.items()))}"
              f" -> {'GENUINE' if genuine else 'not genuine'} {n}-qubit")
    return genuine

if __name__ == "__main__":
    results = {}
    for n in (3, 5, 7, 9, 11, 13):
        F = [frozenset()] + [frozenset({q, (q + 1) % n}) for q in range(n)]
        results[f"C{n}"] = verify(n, F)
    for n in (6, 8, 10, 12):                                    # triangle + C_(n-2) sharing vertex 0
        E = [{0, 1}, {1, 2}, {0, 2}] + [{(0 if k == 0 else k + 2), (k + 3 if k + 3 < n else 0)} for k in range(n - 2)]
        E = [frozenset(e) for e in E]
        assert len(E) == n + 1 and all(sum(q in e for e in E) % 2 == 0 for q in range(n)) and len(set(E)) == len(E)
        results[f"tri+C{n-2}"] = verify(n, [frozenset()] + E)
    print(results)
    assert all(results.values())
