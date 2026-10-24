"""Exhaustive constructive search for k-qubit Pauli assignments, up to Clifford equivalence.

Clifford conjugation (= Sp(2k,2) on symplectic vectors) maps assignments to assignments and
preserves every context sign, so it suffices to enumerate one representative per orbit.
Observables are placed one at a time.  If an observable is the last unassigned member of some
context its vector is forced (sum of the others).  Otherwise we branch over orbit
representatives of the pointwise stabiliser of U = span(assigned vectors):
   * every vector in U (fixed points), and
   * one vector outside U for each functional f in U* that is realised outside U
     (Witt: v, v' outside U are in one orbit iff <u,v> = <u,v'> for all u in U).
Identity (zero) and coinciding images are allowed.  At each leaf the context products are
computed by explicit Pauli multiplication (table derived from numpy matrices), so the sign
parity does NOT use the inversion-count lemma."""
import sys, itertools, time
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from core import P1, observables_of

# single-qubit multiplication table from explicit matrices
LET = 'IXZY'  # index = x + 2z  (I=0, X=1, Z=2, Y=3)
TABLE = {}
for a in range(4):
    for b in range(4):
        M = P1[LET[a]] @ P1[LET[b]]
        c = a ^ b
        ph = None
        for cand in (1, -1, 1j, -1j):
            if np.allclose(M, cand * P1[LET[c]]):
                ph = cand
        TABLE[(a, b)] = (c, ph)


def letters(v, k):
    return [((v >> q) & 1) | (((v >> (k + q)) & 1) << 1) for q in range(k)]


def product_sign(vs, k):
    """Product of Hermitian Paulis W(v) (all with + sign); returns phase if identity else None."""
    cur = [0] * k
    ph = 1
    for v in vs:
        l = letters(v, k)
        for q in range(k):
            c, p = TABLE[(cur[q], l[q])]
            cur[q] = c
            ph *= p
    if any(cur):
        return None
    return ph


def sym(u, v, k):
    m = (1 << k) - 1
    return (bin((u & m) & (v >> k)).count('1') + bin((u >> k) & (v & m)).count('1')) & 1


def span_basis(vecs):
    piv = {}
    for r in vecs:
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h]
            else:
                piv[h] = r
                break
    return list(piv.values())


def in_span(basis, v):
    piv = {b.bit_length() - 1: b for b in basis}
    while v:
        h = v.bit_length() - 1
        if h in piv:
            v ^= piv[h]
        else:
            return False
    return True


def search(contexts, k, time_limit=3600, verbose=True):
    obs = observables_of(contexts)
    N = len(obs)
    oi = {o: i for i, o in enumerate(obs)}
    C = [[oi[o] for o in c] for c in contexts]
    nb = [set() for _ in range(N)]
    for c in C:
        for a in c:
            nb[a] |= set(c) - {a}
    allv = list(range(1 << (2 * k)))
    assign = [None] * N
    stats = {'nodes': 0, 'leaves': 0, 'magic': 0, 'parity_hist': {}}
    t0 = time.time()
    found = []

    def forced_value(i):
        for c in C:
            if i in c and all(assign[j] is not None for j in c if j != i):
                s = 0
                for j in c:
                    if j != i:
                        s ^= assign[j]
                return s
        return None

    def consistent(i, v):
        for j in nb[i]:
            if assign[j] is not None and sym(v, assign[j], k):
                return False
        # if this completes a context, its vector sum must vanish
        for c in C:
            if i in c and all(assign[j] is not None for j in c if j != i):
                s = v
                for j in c:
                    if j != i:
                        s ^= assign[j]
                if s:
                    return False
        return True

    def pick_next():
        # forced first
        for i in range(N):
            if assign[i] is None and forced_value(i) is not None:
                return i, True
        # else most constrained free observable
        best, bs = None, -1
        for i in range(N):
            if assign[i] is None:
                s = sum(1 for j in nb[i] if assign[j] is not None)
                if s > bs:
                    best, bs = i, s
        return best, False

    def candidates(i):
        assigned = [assign[j] for j in range(N) if assign[j] is not None]
        B = span_basis(assigned)
        # vectors in U
        U = [0]
        for b in B:
            U = U + [u ^ b for u in U]
        cands = list(U)
        seen_f = set()
        Uset = set(U)
        for v in allv:
            if v in Uset:
                continue
            f = tuple(sym(b, v, k) for b in B)
            if f not in seen_f:
                seen_f.add(f)
                cands.append(v)
        return cands

    def leaf():
        stats['leaves'] += 1
        neg = 0
        for c in C:
            ph = product_sign([assign[j] for j in c], k)
            if ph is None or ph not in (1, -1):
                raise RuntimeError('context product not +-I at leaf')
            neg += (ph == -1)
        stats['parity_hist'][neg % 2] = stats['parity_hist'].get(neg % 2, 0) + 1
        if neg % 2 == 1:
            stats['magic'] += 1
            if len(found) < 3:
                found.append(list(assign))

    def rec(depth):
        if time.time() - t0 > time_limit:
            raise TimeoutError
        stats['nodes'] += 1
        i, forced = pick_next()
        if i is None:
            leaf()
            return
        if forced:
            v = forced_value(i)
            if consistent(i, v):
                assign[i] = v
                rec(depth + 1)
                assign[i] = None
            return
        for v in candidates(i):
            if consistent(i, v):
                assign[i] = v
                rec(depth + 1)
                assign[i] = None

    try:
        rec(0)
        done = True
    except TimeoutError:
        done = False
    stats['complete'] = done
    stats['time'] = round(time.time() - t0, 2)
    return stats, found, obs


def to_str(v, k):
    return ''.join(LET[l] for l in letters(v, k))


if __name__ == '__main__':
    import json
    from verify_sets import graph_star
    square = [['XI', 'IX', 'XX'], ['IZ', 'ZI', 'ZZ'], ['XZ', 'ZX', 'YY'],
              ['XI', 'IZ', 'XZ'], ['IX', 'ZI', 'ZX'], ['XX', 'ZZ', 'YY']]
    pent = graph_star(3, [(0, 1), (1, 2), (0, 2)])
    for nm, ctx, ks in [('square', square, [1, 2]), ('pentagram', pent, [2, 3])]:
        for k in ks:
            st, fd, obs = search(ctx, k)
            print(nm, 'k=%d' % k, st)
    sets = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')))
    for name in sys.argv[1:]:
        ctx = sets[name]['contexts']
        n = sets[name]['qubits']
        for k in (n - 1,):
            st, fd, obs = search(ctx, k, time_limit=5000)
            print(name, 'k=%d' % k, st)
            for f in fd:
                print('   example magic assignment:', [to_str(v, k) for v in f])
