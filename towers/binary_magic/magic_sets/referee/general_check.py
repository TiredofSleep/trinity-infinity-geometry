import sys, itertools, random
import numpy as np
import networkx as nx
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from core import mat, vec, symp, observables_of
from verify_sets import graph_star
from gram import analyse


def check_graph(n, E, use_matrices=True):
    ctx = graph_star(n, E)
    obs = observables_of(ctx)
    assert len(obs) == 2 * n + len(E) + 1
    assert len({vec(o) for o in obs}) == len(obs)
    deg = {o: sum(o in c for c in ctx) for o in obs}
    assert all(v % 2 == 0 for v in deg.values())
    signs = []
    if use_matrices:
        I = np.eye(2 ** n)
        for c in ctx:
            for a, b in itertools.combinations(c, 2):
                assert symp(vec(a), vec(b), n) == 0
            P = np.eye(2 ** n, dtype=complex)
            for o in c:
                P = P @ mat(o)
            if np.allclose(P, I): signs.append(1)
            elif np.allclose(P, -I): signs.append(-1)
            else: raise AssertionError('not +-I')
    neg = sum(s < 0 for s in signs)
    # minimality (iii): brute force over sub-collections
    m = len(ctx)
    minimal = True
    if m <= 14:
        for mask in range(1, (1 << m) - 1):
            sub = [i for i in range(m) if mask >> i & 1]
            if sum(signs[i] < 0 for i in sub) % 2 == 0:
                continue
            cnt = {}
            for i in sub:
                for o in ctx[i]:
                    cnt[o] = cnt.get(o, 0) + 1
            if all(v % 2 == 0 for v in cnt.values()):
                minimal = False
                break
    g = analyse('g', ctx, n_actual=n)
    return neg, minimal, g


if __name__ == '__main__':
    tested = 0
    fails = []
    for G in nx.graph_atlas_g():
        n = G.number_of_nodes()
        if n < 2 or not nx.is_connected(G):
            continue
        if any(d % 2 for _, d in G.degree()) or G.number_of_edges() % 2 == 0:
            continue
        E = sorted(tuple(sorted(e)) for e in G.edges())
        neg, minimal, g = check_graph(n, E)
        tested += 1
        ok = (neg == 1 and minimal and g['min_qubits'] == n and g['dim'] == 1
              and g['magic_with_zero_or_repeated_rows'] == 0)
        print(f'n={n} |E|={len(E)} #obs={2*n+len(E)+1} neg={neg} minimal={minimal} '
              f'gramdim={g["dim"]} minq={g["min_qubits"]} nondegenerate={g["magic_with_zero_or_repeated_rows"]==0} {"OK" if ok else "FAIL"}  E={E}')
        if not ok:
            fails.append((n, E))
    print('atlas graphs tested:', tested, 'failures:', fails)
    # random larger even graphs: union of random cycles, keep connected/simple/odd |E|
    rng = random.Random(3)
    cnt = 0
    while cnt < 12:
        n = rng.randint(8, 9)
        Gm = nx.Graph()
        Gm.add_nodes_from(range(n))
        for _ in range(rng.randint(2, 4)):
            L = rng.randint(3, n)
            cyc = rng.sample(range(n), L)
            for i in range(L):
                e = tuple(sorted((cyc[i], cyc[(i + 1) % L])))
                if Gm.has_edge(*e): Gm.remove_edge(*e)
                else: Gm.add_edge(*e)
        Gm.remove_nodes_from([v for v in list(Gm) if Gm.degree(v) == 0])
        if Gm.number_of_nodes() < 3 or not nx.is_connected(Gm): continue
        if any(d % 2 for _, d in Gm.degree()) or Gm.number_of_edges() % 2 == 0: continue
        Gm = nx.convert_node_labels_to_integers(Gm)
        n = Gm.number_of_nodes()
        E = sorted(tuple(sorted(e)) for e in Gm.edges())
        neg, minimal, g = check_graph(n, E)
        print(f'[rand] n={n} |E|={len(E)} neg={neg} minimal={minimal} gramdim={g["dim"]} minq={g["min_qubits"]}')
        cnt += 1
