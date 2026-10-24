import sys, itertools, random
import numpy as np
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from core import mat, vec, symp, load_sets, observables_of

PATH = __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')


def graph_star(n, edges):
    """Rebuild from THEOREM.md text: F = {emptyset} u E; M_S has Y on S, X elsewhere."""
    F = [frozenset()] + [frozenset(e) for e in edges]
    def M(S):
        return ''.join('Y' if v in S else 'X' for v in range(n))
    def single(v, ch):
        return ''.join(ch if u == v else 'I' for u in range(n))
    C0 = [M(S) for S in F]
    ctx = [C0]
    for S in F:
        ctx.append([single(v, 'Y' if v in S else 'X') for v in range(n)] + [M(S)])
    return ctx


def edges_from_M(contexts, n):
    E = []
    for s in contexts[0]:
        S = tuple(i for i, ch in enumerate(s) if ch == 'Y')
        if S:
            E.append(S)
    return E


def check(name, d, rng):
    ctxs = d['contexts']
    n = d['qubits']
    print(f'=== {name}: n={n}, {len(ctxs)} contexts')
    assert all(len(s) == n and set(s) <= set('IXYZ') for c in ctxs for s in c)
    obs = observables_of(ctxs)
    print('  #observables (distinct strings):', len(obs), ' claimed:', d['observables'])
    assert all(len(set(c)) == len(c) for c in ctxs), 'repeated obs in a context'
    assert all(o != 'I' * n for o in obs), 'identity observable'
    vs = [vec(o) for o in obs]
    assert len(set(vs)) == len(vs), 'two observables equal up to phase'
    assert len(set(map(lambda c: frozenset(c), ctxs))) == len(ctxs), 'repeated context'
    Mt = {o: mat(o) for o in obs}
    dim = 2 ** n
    I = np.eye(dim)
    signs = []
    for ci, c in enumerate(ctxs):
        for a, b in itertools.combinations(c, 2):
            A, B = Mt[a], Mt[b]
            assert np.allclose(A @ B, B @ A), f'context {ci}: {a},{b} do not commute'
            assert symp(vec(a), vec(b), n) == 0
        # product in listed order and several random orders
        prods = []
        for trial in range(4):
            order = list(c) if trial == 0 else rng.sample(list(c), len(c))
            P = I.astype(complex)
            for o in order:
                P = P @ Mt[o]
            if np.allclose(P, I):
                prods.append(+1)
            elif np.allclose(P, -I):
                prods.append(-1)
            else:
                raise AssertionError(f'context {ci} product not +-I')
        assert len(set(prods)) == 1
        signs.append(prods[0])
        # Hermiticity
    for o in obs:
        assert np.allclose(Mt[o], Mt[o].conj().T)
    neg = [i for i, s in enumerate(signs) if s < 0]
    print('  signs:', signs, ' negative contexts:', neg, ' claimed negative index:', d.get('negative_context'))
    deg = {o: sum(o in c for c in ctxs) for o in obs}
    print('  degree multiset:', sorted(set(deg.values())), ' all even:', all(v % 2 == 0 for v in deg.values()))
    print('  (ii) #neg odd:', len(neg) % 2 == 1)
    # (iii) brute-force all proper nonempty subcollections
    m = len(ctxs)
    bad = []
    for mask in range(1, (1 << m) - 1):
        sub = [i for i in range(m) if mask >> i & 1]
        cnt = {}
        for i in sub:
            for o in ctxs[i]:
                cnt[o] = cnt.get(o, 0) + 1
        if all(v % 2 == 0 for v in cnt.values()) and sum(signs[i] < 0 for i in sub) % 2 == 1:
            bad.append(sub)
    print(f'  (iii) proper sub-collections satisfying (i)+(ii): {len(bad)} (of {2**m-2} checked)')
    # are the contexts minimal ID sets (no proper nonempty subset multiplying to +-I)?
    nonmin = []
    for ci, c in enumerate(ctxs):
        cv = [vec(o) for o in c]
        for r in range(1, len(c)):
            for sub in itertools.combinations(range(len(c)), r):
                x = 0
                for j in sub:
                    x ^= cv[j]
                if x == 0:
                    nonmin.append((ci, [c[j] for j in sub]))
    if nonmin:
        print('  contexts containing a proper ID subset (vector sum 0):')
        seen = set()
        for ci, sub in nonmin:
            key = (ci, frozenset(sub))
            if key in seen: continue
            seen.add(key)
            P = np.eye(dim, dtype=complex)
            for o in sub: P = P @ Mt[o]
            sg = '+I' if np.allclose(P, I) else '-I'
            print(f'    ctx {ci}: {sub} -> {sg}')
    else:
        print('  every context is a minimal ID set (no proper subset multiplies to +-I)')
    # compare with rebuild from THEOREM.md
    E = edges_from_M(ctxs, n)
    rebuilt = graph_star(n, E)
    same = set(map(frozenset, rebuilt)) == set(map(frozenset, ctxs))
    print('  edges read off M_S:', E, ' JSON == rebuild from THEOREM construction:', same)
    print('  2|V|+|E|+1 =', 2 * n + len(E) + 1, ' |E|+2 =', len(E) + 2)
    return signs


if __name__ == '__main__':
    rng = random.Random(1)
    sets = load_sets(PATH)
    for name, d in sets.items():
        check(name, d, rng)
