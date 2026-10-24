"""Direct search: does a k-qubit Pauli assignment exist for the hypergraph?
Every observable gets its own free 2k bits (identity and coincidences ALLOWED).
Constraints: per context vector-sum = 0 (product +-I), pairwise symplectic product 0 within a
context, and odd sign parity (parity = linear functional of commutation, validated in gram.py)."""
import sys, time, itertools
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from pysat.solvers import Cadical153
from gram import setup


class CNF:
    def __init__(self):
        self.nv = 0
        self.cl = []
    def new(self):
        self.nv += 1
        return self.nv
    def AND(self, a, b):
        t = self.new()
        self.cl += [[-t, a], [-t, b], [t, -a, -b]]
        return t
    def XOR2(self, a, b):
        y = self.new()
        self.cl += [[-y, a, b], [-y, -a, -b], [y, -a, b], [y, a, -b]]
        return y
    def xor_eq(self, lits, rhs):
        if not lits:
            if rhs: self.cl.append([])
            return
        acc = lits[0]
        for l in lits[1:]:
            acc = self.XOR2(acc, l)
        self.cl.append([acc] if rhs else [-acc])


def build(contexts, k, require_parity=True, extra=None):
    obs, C, N, pid, var, eqs, pvec = setup(contexts)
    f = CNF()
    X = [[f.new() for _ in range(k)] for _ in range(N)]
    Z = [[f.new() for _ in range(k)] for _ in range(N)]
    for c in C:
        for q in range(k):
            f.xor_eq([X[o][q] for o in c], 0)
            f.xor_eq([Z[o][q] for o in c], 0)
    share = set()
    for c in C:
        for a, b in itertools.combinations(sorted(c), 2):
            share.add((a, b))
    def sympl_terms(a, b):
        t = []
        for q in range(k):
            t.append(f.AND(X[a][q], Z[b][q]))
            t.append(f.AND(Z[a][q], X[b][q]))
        return t
    for (a, b) in share:
        f.xor_eq(sympl_terms(a, b), 0)
    if require_parity:
        terms = []
        for (a, b), kk in pid.items():
            if pvec >> kk & 1 and (a, b) not in share:
                terms += sympl_terms(a, b)
        f.xor_eq(terms, 1)
    return f, obs, X, Z


def solve(contexts, k, timeout=None, label=''):
    f, obs, X, Z = build(contexts, k)
    t0 = time.time()
    with Cadical153(bootstrap_with=f.cl) as s:
        res = s.solve()
        model = s.get_model() if res else None
    dt = time.time() - t0
    sol = None
    if res:
        mset = set(l for l in model if l > 0)
        sol = []
        for i, o in enumerate(obs):
            s_ = ''
            for q in range(k):
                x = X[i][q] in mset; z = Z[i][q] in mset
                s_ += {(0, 0): 'I', (1, 0): 'X', (1, 1): 'Y', (0, 1): 'Z'}[(x, z)]
            sol.append((o, s_))
    print(f'{label:12s} k={k}: {"SAT" if res else "UNSAT"}  vars={f.nv} clauses={len(f.cl)}  {dt:.2f}s')
    return res, sol


if __name__ == '__main__':
    import json
    from verify_sets import graph_star
    from core import mat
    import numpy as np
    square = [['XI', 'IX', 'XX'], ['IZ', 'ZI', 'ZZ'], ['XZ', 'ZX', 'YY'],
              ['XI', 'IZ', 'XZ'], ['IX', 'ZI', 'ZX'], ['XX', 'ZZ', 'YY']]
    pent = graph_star(3, [(0, 1), (1, 2), (0, 2)])
    solve(square, 1, label='square')
    solve(square, 2, label='square')
    solve(pent, 2, label='pentagram')
    solve(pent, 3, label='pentagram')
    sets = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')))
    which = sys.argv[1:] or ['C5 (n=5)']
    for name in which:
        ctx = sets[name]['contexts']
        n = sets[name]['qubits']
        res, sol = solve(ctx, n, label=name[:12])
        # check the SAT witness with explicit matrices: count negative contexts
        if res:
            m = dict(sol)
            neg = 0
            for c in ctx:
                P = np.eye(2 ** n, dtype=complex)
                for o in c: P = P @ mat(m[o])
                assert np.allclose(P, np.eye(2 ** n)) or np.allclose(P, -np.eye(2 ** n))
                neg += np.allclose(P, -np.eye(2 ** n))
            print('   witness re-checked with matrices: #negative contexts =', neg)
        solve(ctx, n - 1, label=name[:12])
