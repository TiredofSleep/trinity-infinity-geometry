"""Independent genuineness test via the full valid Gram space over ALL observables.

Any Pauli assignment o -> +-W(v_o) on k qubits preserving the context relations gives an
alternating F2 matrix G[o,p] = <v_o, v_p> with
  (C1) G[o,p] = 0 whenever o,p share a context        (commutation)
  (C2) sum_{o in c} G[o,w] = 0 for every context c, w  (product +-I  =>  sum_{o in c} v_o = 0)
Conversely any such G is realised by vectors in F2^{rank G} with the relations exact
(the relation vectors lie in rad G, so G descends to the quotient; a symplectic basis of the
non-degenerate part does the rest).  Hence min qubits = min rank(G)/2 over magic G.

Sign parity: multiply all context products together.  The word contains each letter an even
number of times; bubble-sorting it costs (-1)^{G[a,b]} per inverted pair, after which it is I.
So  prod_c s_c = (-1)^{ sum_{inverted pairs (a,b)} G[a,b] }  -- a LINEAR functional of G.
This lemma is validated numerically below before use."""
import sys, itertools, random
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from core import mat, vec, symp, load_sets, observables_of, f2_nullspace, f2_rank

PATH = __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')


def pair_index(N):
    idx = {}
    for i in range(N):
        for j in range(i + 1, N):
            idx[(i, j)] = len(idx)
    return idx


def setup(contexts):
    obs = observables_of(contexts)
    oi = {o: i for i, o in enumerate(obs)}
    C = [[oi[o] for o in c] for c in contexts]
    N = len(obs)
    pid = pair_index(N)
    def var(a, b):
        return pid[(a, b) if a < b else (b, a)]
    eqs = []
    for c in C:
        for a, b in itertools.combinations(c, 2):
            eqs.append(1 << var(a, b))
        for w in range(N):
            r = 0
            for o in c:
                if o != w:
                    r ^= 1 << var(o, w)
            if r:
                eqs.append(r)
    # parity functional from the concatenated word
    word = [o for c in C for o in c]
    pvec = 0
    for i in range(len(word)):
        for j in range(i + 1, len(word)):
            a, b = word[i], word[j]
            if a > b:
                pvec ^= 1 << var(a, b)
    return obs, C, N, pid, var, eqs, pvec


def G_from_solution(sol, N, pid):
    G = [[0] * N for _ in range(N)]
    for (a, b), k in pid.items():
        if sol >> k & 1:
            G[a][b] = G[b][a] = 1
    return G


def rank_of(G):
    rows = [sum(b << j for j, b in enumerate(r)) for r in G]
    return f2_rank(rows), rows


def validate_parity_lemma(trials=3000, seed=7):
    rng = random.Random(seed)
    letters = 'IXYZ'
    for t in range(trials):
        n = rng.randint(1, 3)
        m = rng.randint(1, 6)
        ops = [''.join(rng.choice(letters) for _ in range(n)) for _ in range(m)]
        word = []
        for i in range(m):
            word += [i] * (2 * rng.randint(0, 3))
        rng.shuffle(word)
        P = np.eye(2 ** n, dtype=complex)
        for i in word:
            P = P @ mat(ops[i])
        actual = 1 if np.allclose(P, np.eye(2 ** n)) else (-1 if np.allclose(P, -np.eye(2 ** n)) else None)
        assert actual is not None
        e = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                a, b = word[i], word[j]
                if a > b:
                    e ^= symp(vec(ops[a]), vec(ops[b]), n)
        assert actual == (-1) ** e, (ops, word)
    return trials


def analyse(name, contexts, n_actual=None, verbose=True, enum_limit=22):
    obs, C, N, pid, var, eqs, pvec = setup(contexts)
    basis = f2_nullspace(eqs, len(pid))
    d = len(basis)
    out = {'name': name, 'N': N, 'unknowns': len(pid), 'dim': d}
    # check the actual realisation is in the space and has odd parity
    if n_actual is not None:
        n = n_actual
        vs = [vec(o) for o in obs]
        sol = 0
        for (a, b), k in pid.items():
            if symp(vs[a], vs[b], n):
                sol |= 1 << k
        ok = all(bin(e & sol).count('1') % 2 == 0 for e in eqs)
        out['actual_in_space'] = ok
        out['actual_parity'] = bin(pvec & sol).count('1') % 2
    # parity on basis
    pb = [bin(pvec & b).count('1') % 2 for b in basis]
    out['parity_on_basis'] = pb
    if d > enum_limit:
        out['note'] = 'space too large to enumerate'
        return out
    results = []
    for mask in range(1 << d):
        sol = 0
        for i in range(d):
            if mask >> i & 1:
                sol ^= basis[i]
        par = bin(pvec & sol).count('1') % 2
        G = G_from_solution(sol, N, pid)
        r, rows = rank_of(G)
        zero_rows = sum(1 for x in rows if x == 0)
        rep_rows = len(rows) - len(set(rows))
        results.append((par, r, zero_rows, rep_rows))
    odd = [x for x in results if x[0] == 1]
    out['n_solutions'] = len(results)
    out['n_magic'] = len(odd)
    out['magic_ranks'] = sorted(set(x[1] for x in odd))
    out['min_qubits'] = (min(x[1] for x in odd) // 2) if odd else None
    out['magic_with_zero_or_repeated_rows'] = sum(1 for x in odd if x[2] or x[3])
    out['nonmagic_ranks'] = sorted(set(x[1] for x in results if x[0] == 0))
    return out


if __name__ == '__main__':
    print('parity lemma validated on', validate_parity_lemma(), 'random words')
    sets = load_sets(PATH)
    for name, dd in sets.items():
        print(analyse(name, dd['contexts'], n_actual=dd['qubits']))
