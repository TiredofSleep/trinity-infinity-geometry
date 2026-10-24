"""
lower_bound2.py — Round 11 of PREREG.md, the fast enumerator.

Lemma 1: V >= 2n + r.  Lemma 2: minimal => r = C - 1.  So V >= 2n + C - 1, i.e. C <= V_max - 2n + 1.
Hypergraph = C contexts; each observable lies in an even number (2, 4 or 6) of contexts.
Build: choose the observables of degree >= 4 (as context subsets), then a multigraph of degree-2 observables
with node capacities (context size <= s_max). Canonical form under context permutations. Then:
r == C - 1 (needed for minimality), min magic Gram rank (genuineness), and minimality of any genuine hit.
"""
import itertools, sys, time
from collections import Counter
from ms_core import min_magic_rank, rank_rows

def multigraphs(C, E, cap, need):
    """all multisets of E edges on C nodes with node degree <= cap[i]; final sizes checked by caller"""
    pairs = list(itertools.combinations(range(C), 2))
    deg = [0] * C; mult = [0] * len(pairs)
    def rec(k, left):
        if left == 0:
            if all(deg[i] >= need[i] for i in range(C)): yield tuple(mult)
            return
        if k == len(pairs): return
        # remaining capacity check
        room = sum(cap[i] - deg[i] for i in range(C))
        if room < 2 * left: return
        i, j = pairs[k]; m = 0
        while m <= left and deg[i] + m <= cap[i] and deg[j] + m <= cap[j]:
            mult[k] = m; deg[i] += m; deg[j] += m
            yield from rec(k + 1, left - m)
            deg[i] -= m; deg[j] -= m
            m += 1
        mult[k] = 0
    yield from rec(0, E)

def hypergraphs(C, V, smax):
    hp = [frozenset(s) for k in range(4, C + 1, 2) for s in itertools.combinations(range(C), k)]
    for a in range(0, V + 1):
        for H in itertools.combinations_with_replacement(range(len(hp)), a):
            h = [0] * C
            for t in H:
                for i in hp[t]: h[i] += 1
            if any(x > smax for x in h): continue
            cap = [smax - x for x in h]; need = [max(0, 3 - x) for x in h]
            E = V - a
            if 2 * E > sum(cap) or 2 * E < sum(need): continue
            for mg in multigraphs(C, E, cap, need):
                yield [hp[t] for t in H], mg
        if 4 * a > C * smax: break

def build(C, highs, mg):
    pairs = list(itertools.combinations(range(C), 2))
    ctxs = [[] for _ in range(C)]; V = 0
    for pat in highs:
        for i in pat: ctxs[i].append(V)
        V += 1
    for k, m in enumerate(mg):
        for _ in range(m):
            for i in pairs[k]: ctxs[i].append(V)
            V += 1
    return V, [tuple(c) for c in ctxs]

def canon(C, ctxs, V):
    pats = Counter()
    for v in range(V):
        pats[tuple(i for i in range(C) if v in ctxs[i])] += 1
    best = None
    for p in itertools.permutations(range(C)):
        key = tuple(sorted((tuple(sorted(p[i] for i in pat)), m) for pat, m in pats.items()))
        if best is None or key < best: best = key
    return best

def is_minimal(V, ctxs):
    """no proper nonempty sub-collection with all degrees even (and then odd negatives) — Lemma 2 check by rank"""
    rows = []
    for c in ctxs:
        m = 0
        for v in c: m |= 1 << v
        rows.append(m)
    return rank_rows(rows) == len(ctxs) - 1

def run(n, Vmax, smax, label, Cmax_cap=6):
    t0 = time.time(); tally = Counter(); hits = []; seen = set()
    Cmax = min(Vmax - 2 * n + 1, Cmax_cap)
    for C in range(3, Cmax + 1):
        for V in range(2 * n + C - 1, Vmax + 1):
            for highs, mg in hypergraphs(C, V, smax):
                Vv, ctxs = build(C, highs, mg)
                assert Vv == V
                if len(set(map(frozenset, ctxs))) < C: tally["repeated context"] += 1; continue
                if not is_minimal(V, ctxs): tally["not minimal (r < C-1)"] += 1; continue
                key = canon(C, ctxs, V)
                if key in seen: continue
                seen.add(key)
                q, d = min_magic_rank(V, ctxs, limit_dim=22, stop_at=2 * n - 2)
                if q is None: tally["no magic Pauli assignment"] += 1
                elif q == "too big": tally["unresolved"] += 1; hits.append(("?", V, C, ctxs))
                elif q >= 2 * n: tally["genuine"] += 1; hits.append((q // 2, V, C, ctxs))
                else: tally[f"fits on < {n} qubits"] += 1
    best = min((h[1] for h in hits if h[0] != "?"), default=None)
    print(f"{label}: {len(seen)} distinct minimal-candidate hypergraphs in {time.time() - t0:.0f}s;"
          f" {dict(tally)}; smallest genuine: {best}", flush=True)
    return hits, tally, best

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "cal"
    res = {}
    if which in ("cal", "all"):
        h, t, b = run(2, 9, 3, "L1 n=2 (V<=9, sizes 3)"); res["L1"] = b == 9
        h, t, b = run(3, 10, 4, "L2 n=3 (V<=10, sizes 3-4)"); res["L2"] = b == 10 and t.get("unresolved", 0) == 0
    if which in ("n5", "all"):
        h, t, b = run(5, 15, 6, "L3 n=5 (V<=15, C<=6 forced, sizes 3-6)")
        res["L3"] = b is None and t.get("unresolved", 0) == 0
        for x in h: print("   hit:", x)
    if which in ("n4", "all"):
        h, t, b = run(4, 15, 5, "L4 n=4 (C<=6, sizes 3-5)")
        res["L4"] = b is None and t.get("unresolved", 0) == 0
        for x in h[:5]: print("   hit:", x)
    print("SCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
