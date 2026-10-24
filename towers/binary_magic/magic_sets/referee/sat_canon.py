"""SAT search with justified symmetry breaking (Witt): the images x_v of X_v pairwise commute
(all lie in C_empty), so up to Sp(2k,2) they are pure-X vectors whose x-parts are in reduced
echelon form (each is a new unit vector or a combination of earlier unit vectors).  For each such
pattern, SAT-solve for the 2k bits of each y_v.  M_S := sum of its local context (forced by
product +-I).  Constraints: all within-context commutations, odd sign parity (linear functional
of the commutation matrix, lemma validated in gram.py)."""
import sys, json, itertools, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from pysat.solvers import Cadical153
from sat_search import CNF
from gram import setup


def patterns(n, k):
    """Yield tuples of x-part ints (k bits) in reduced echelon pattern."""
    def rec(i, r, cur):
        if i == n:
            yield tuple(cur)
            return
        # combination of existing unit vectors e_0..e_{r-1} (including 0)
        for m in range(1 << r):
            cur.append(m)
            yield from rec(i + 1, r, cur)
            cur.pop()
        if r < k:
            cur.append(1 << r)
            yield from rec(i + 1, r + 1, cur)
            cur.pop()
    yield from rec(0, 0, [])


def run(n, E, contexts, k, label):
    obs, C, N, pid, var, eqs, pvec = setup(contexts)
    oi = {o: i for i, o in enumerate(obs)}
    Xs = [''.join('X' if u == v else 'I' for u in range(n)) for v in range(n)]
    Ys = [''.join('Y' if u == v else 'I' for u in range(n)) for v in range(n)]
    F = [frozenset()] + [frozenset(e) for e in E]
    Ms = [''.join('Y' if v in S else 'X' for v in range(n)) for S in F]
    share = set()
    for c in C:
        for a, b in itertools.combinations(sorted(c), 2):
            share.add((a, b))
    par_pairs = [(a, b) for (a, b), kk in pid.items() if pvec >> kk & 1 and (a, b) not in share]
    t0 = time.time()
    count = 0
    sat_count = 0
    for pat in patterns(n, k):
        count += 1
        f = CNF()
        TRUE = f.new(); f.cl.append([TRUE])
        # y bits
        Yx = [[f.new() for _ in range(k)] for _ in range(n)]
        Yz = [[f.new() for _ in range(k)] for _ in range(n)]
        # representation of each observable's bits as lists of (literal or const)
        # x_v: x-part = pat[v] (consts), z-part = 0
        def const(b):
            return TRUE if b else -TRUE
        rep = {}
        for v in range(n):
            rep[oi[Xs[v]]] = ([const(pat[v] >> q & 1) for q in range(k)], [const(0)] * k)
            rep[oi[Ys[v]]] = (Yx[v], Yz[v])
        for S, Mstr in zip(F, Ms):
            xb, zb = [], []
            for q in range(k):
                lx = [Yx[v][q] for v in S]
                lz = [Yz[v][q] for v in S]
                cx = 0
                for v in range(n):
                    if v not in S:
                        cx ^= pat[v] >> q & 1
                # xor of literals and constant
                def xor_lits(lits, c0):
                    if not lits:
                        return const(c0)
                    acc = lits[0]
                    for l in lits[1:]:
                        acc = f.XOR2(acc, l)
                    return -acc if c0 else acc
                xb.append(xor_lits(lx, cx))
                zb.append(xor_lits(lz, 0))
            rep[oi[Mstr]] = (xb, zb)
        def sympl_terms(a, b):
            (ax, az), (bx, bz) = rep[a], rep[b]
            return [f.AND(ax[q], bz[q]) for q in range(k)] + [f.AND(az[q], bx[q]) for q in range(k)]
        for (a, b) in share:
            f.xor_eq(sympl_terms(a, b), 0)
        terms = []
        for (a, b) in par_pairs:
            terms += sympl_terms(a, b)
        f.xor_eq(terms, 1)
        with Cadical153(bootstrap_with=f.cl) as s:
            if s.solve():
                sat_count += 1
    print(f'{label}: k={k}: {count} canonical X-patterns, SAT in {sat_count}  ({time.time()-t0:.1f}s)', flush=True)
    return sat_count


if __name__ == '__main__':
    from verify_sets import graph_star
    run(3, [(0, 1), (1, 2), (0, 2)], graph_star(3, [(0, 1), (1, 2), (0, 2)]), 2, 'pentagram')
    run(3, [(0, 1), (1, 2), (0, 2)], graph_star(3, [(0, 1), (1, 2), (0, 2)]), 3, 'pentagram')
    sets = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')))
    for name in sys.argv[1:]:
        d = sets[name]; n = d['qubits']
        E = [tuple(i for i, ch in enumerate(s) if ch == 'Y') for s in d['contexts'][0]]
        E = [e for e in E if e]
        for k in (n, n - 1):
            run(n, E, d['contexts'], k, name)
