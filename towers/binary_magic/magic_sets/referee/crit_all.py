import sys, networkx as nx
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from verify_sets import graph_star
from critical import id_sets, proof_exists
from core import observables_of
from gram import analyse
for G in nx.graph_atlas_g():
    n = G.number_of_nodes()
    if n < 2 or not nx.is_connected(G): continue
    if any(d % 2 for _, d in G.degree()) or G.number_of_edges() % 2 == 0: continue
    E = sorted(tuple(sorted(e)) for e in G.edges())
    ctx = graph_star(n, E); obs = observables_of(ctx); N = len(obs)
    allid, minimal, signs = id_sets(obs, n)
    given = {tuple(sorted(obs.index(o) for o in c)) for c in ctx}
    extra = [c for c in minimal if c not in given]
    dele = [o for o in range(N) if proof_exists([j for j in range(N) if j != o], minimal, signs, N)]
    # smallest sub-proof found greedily: delete deletable observables one by one
    keep = list(range(N))
    changed = True
    while changed:
        changed = False
        for o in list(keep):
            rest = [j for j in keep if j != o]
            if proof_exists(rest, minimal, signs, N):
                keep = rest; changed = True; break
    # min qubits of the greedy sub-proof (contexts = minimal ID sets inside keep forming the proof)
    is_cycle = all(d == 2 for _, d in G.degree())
    print(f'n={n} |E|={len(E)} cycle={is_cycle} #obs={N} extraIDsets={len(extra)} deletable={len(dele)} greedy-min-subproof-size={len(keep)}')
