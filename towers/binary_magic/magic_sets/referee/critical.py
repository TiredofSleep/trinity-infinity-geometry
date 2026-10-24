"""Strong minimality ('criticality'): using ANY ID sets (pairwise-commuting subsets of the given
observables whose product is +-I), is there a parity proof on a proper subset of observables?
A proof on O' exists iff the sign vector s is NOT in the F2 row space of the incidence matrix
(observables in O' x ID-sets inside O').  Non-minimal ID sets split into disjoint minimal ones
with multiplicative signs, so minimal ID sets suffice."""
import sys, json, itertools
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from core import vec, symp, observables_of, f2_rank, f2_in_span
from canon_search import product_sign


def id_sets(obs, n):
    vs = [vec(o) for o in obs]
    N = len(obs)
    comm = [[symp(vs[a], vs[b], n) == 0 for b in range(N)] for a in range(N)]
    out = []
    def rec(start, chosen, s):
        if chosen and s == 0 and len(chosen) >= 3:
            out.append(tuple(chosen))
        for j in range(start, N):
            if all(comm[j][c] for c in chosen):
                chosen.append(j)
                rec(j + 1, chosen, s ^ vs[j])
                chosen.pop()
    rec(0, [], 0)
    minimal = [c for c in out if f2_rank([vs[j] for j in c]) == len(c) - 1]
    signs = {}
    for c in minimal:
        ph = product_sign([vs[j] for j in c], n)
        assert ph in (1, -1)
        signs[c] = ph
    return out, minimal, signs


def proof_exists(subset, minimal, signs, N):
    sub = set(subset)
    ids = [c for c in minimal if set(c) <= sub]
    if not ids:
        return False
    rows = []
    for o in subset:
        r = 0
        for k, c in enumerate(ids):
            if o in c:
                r |= 1 << k
        rows.append(r)
    s = 0
    for k, c in enumerate(ids):
        if signs[c] == -1:
            s |= 1 << k
    return not f2_in_span(rows, s)


if __name__ == '__main__':
    sets = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')))
    for name, d in sets.items():
        ctx = d['contexts']; n = d['qubits']
        obs = observables_of(ctx)
        N = len(obs)
        allid, minimal, signs = id_sets(obs, n)
        given = {tuple(sorted(obs.index(o) for o in c)) for c in ctx}
        sizes = {}
        for c in minimal:
            sizes[len(c)] = sizes.get(len(c), 0) + 1
        print(f'=== {name}: {N} observables; ID sets: {len(allid)} total, {len(minimal)} minimal; '
              f'minimal sizes {dict(sorted(sizes.items()))}; negative minimal: {sum(1 for c in minimal if signs[c]==-1)}')
        extra = [c for c in minimal if c not in given]
        print('   minimal ID sets not among the given contexts:', len(extra))
        for c in extra[:12]:
            print('     ', [obs[j] for j in c], signs[c])
        print('   proof on full set:', proof_exists(range(N), minimal, signs, N))
        removable = [obs[o] for o in range(N) if proof_exists([j for j in range(N) if j != o], minimal, signs, N)]
        print('   observables whose deletion still leaves a parity proof:', removable)
        if N <= 20:
            # all minimal observable subsets supporting a proof (monotone property)
            good = {}
            mins = []
            for size in range(1, N + 1):
                for S in itertools.combinations(range(N), size):
                    # skip supersets of an already-found minimal set
                    if any(set(m) <= set(S) for m in mins):
                        continue
                    if proof_exists(S, minimal, signs, N):
                        mins.append(S)
                if size >= 16 and N == 20 and mins:
                    pass
            print('   minimal observable subsets supporting a parity proof:')
            for m in mins:
                print('     size', len(m), [obs[j] for j in m])
