"""
graph_star.py — the graph-star theorem (THEOREM.md) and its test (Round 8c of PREREG.md).
"""
import itertools, random, sys
from ms_core import parse, check_magic, min_magic_rank, product_sign, gram_space

def graph_star(n, E):
    F = [frozenset()] + [frozenset(e) for e in E]
    labels, idx = [], {}
    def op(l):
        if l not in idx: idx[l] = len(labels); labels.append(l)
        return idx[l]
    ghz = [op("".join("Y" if q in S else "X" for q in range(n))) for S in F]
    local = [tuple(op("I" * q + ("Y" if q in S else "X") + "I" * (n - q - 1)) for q in range(n)) + (ghz[k],)
             for k, S in enumerate(F)]
    return labels, [tuple(ghz)] + local

def random_graph(rnd, n, want_odd):
    """random connected simple graph with all degrees even and the requested edge-count parity"""
    pairs = list(itertools.combinations(range(n), 2))
    for _ in range(20000):
        E = {p for p in pairs if rnd.random() < rnd.choice((0.3, 0.5, 0.7))}
        deg = [sum(v in e for e in E) for v in range(n)]
        if any(d % 2 or d == 0 for d in deg) or (len(E) % 2 == 1) != want_odd: continue
        seen, stack = {0}, [0]                                  # connected?
        while stack:
            v = stack.pop()
            for a, b in E:
                for x, y in ((a, b), (b, a)):
                    if x == v and y not in seen: seen.add(y); stack.append(y)
        if len(seen) == n: return sorted(E)
    return None

if __name__ == "__main__":
    rnd = random.Random(8)
    ok1 = ok3 = True; done = 0; sizes = {}
    while done < 300:
        n = rnd.randint(5, 9)
        E = random_graph(rnd, n, True)
        if E is None: continue
        labels, ctxs = graph_star(n, E)
        ops = [parse(l) for l in labels]
        magic, neg, deg = check_magic(ops, ctxs)
        basis, var, f = gram_space(len(ops), ctxs)
        r, d = min_magic_rank(len(ops), ctxs)
        minimal = neg == [0]                                     # only the GHZ context negative => minimal
        ok1 &= magic and minimal and d == 1 and r == 2 * n and len(ops) == 2 * n + len(E) + 1
        # TH3: GHZ sign by explicit multiplication vs the degree formula vs |E|
        sgn = product_sign([ops[v] for v in ctxs[0]])
        pred = (-1) ** sum(dg * (dg - 1) // 2 for dg in (sum(v in e for e in E) for v in range(n)))
        ok3 &= (sgn == pred == -1) and sum(dg * (dg - 1) // 2 for dg in (sum(v in e for e in E) for v in range(n))) % 2 == len(E) % 2
        done += 1; sizes[n] = sizes.get(n, 0) + 1
    print(f"TH1 300 random graphs (vertices: {dict(sorted(sizes.items()))}): all magic, minimal, rigid, genuine: {ok1}")
    print(f"TH3 GHZ product = (-1)^(sum C(deg,2)) = -1 on all of them: {ok3}")
    ok2 = True; done = 0
    while done < 200:
        n = rnd.randint(4, 9)
        E = random_graph(rnd, n, False)
        if E is None: continue
        labels, ctxs = graph_star(n, E)
        try:
            magic, neg, deg = check_magic([parse(l) for l in labels], ctxs)
        except AssertionError:                                   # |F| odd: the GHZ "context" isn't +-I at all
            magic = False
        ok2 &= not magic; done += 1
    print(f"TH2 200 random graphs with an even number of edges: none magic: {ok2}")
    res = {"TH1": ok1, "TH2": ok2, "TH3": ok3}
    print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
    assert all(res.values())
