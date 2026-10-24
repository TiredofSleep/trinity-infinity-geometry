"""
stars2.py — Round 8b of PREREG.md.
  (a) graph families: F = {∅} ∪ E(G) for an Eulerian graph G with an odd number of edges (odd cycles, etc.)
  (b) N6: every X/Y family at n = 6 with |F| = 8 (WLOG ∅ ∈ F, by the X<->Y relabelling symmetry)
  (c) NZ: three-letter families at n = 4 (operators in {X,Y,Z}^n, pairwise even distance), |F| <= 8
"""
import itertools, sys, time
from collections import Counter
from ms_core import parse, check_magic, min_magic_rank, noncontextual_bound

def build(words):
    """words: list of strings over XYZ of length n. GHZ context + one local context per word."""
    n = len(words[0]); ops, idx = [], {}
    def op(l):
        if l not in idx: idx[l] = len(ops); ops.append(l)
        return idx[l]
    ghz = [op(w) for w in words]
    local = [tuple(op("I" * q + w[q] + "I" * (n - q - 1)) for q in range(n)) + (op(w),) for w in words]
    return ops, [tuple(ghz)] + local

def analyse(words, limit_dim=24):
    labels, ctxs = build(words)
    ops = [parse(l) for l in labels]
    ok, neg, deg = check_magic(ops, ctxs)
    if not ok: return None
    r, d = min_magic_rank(len(ops), ctxs, limit_dim=limit_dim)
    return dict(words=words, observables=len(ops), contexts=len(ctxs), min_rank=r, gram_dim=d,
                qubits=r // 2 if isinstance(r, int) else r, labels=labels, ctxs=ctxs, neg=neg)

xy = lambda n, S: "".join("Y" if q in S else "X" for q in range(n))
part = sys.argv[1] if len(sys.argv) > 1 else "all"
res = {}

if part in ("all", "a"):
    print("(a) graph families: F = {empty} + edges of G")
    for n in (3, 5, 7, 9, 11):
        E = [frozenset({q, (q + 1) % n}) for q in range(n)]
        a = analyse([xy(n, S) for S in [frozenset()] + E], limit_dim=24)
        b = noncontextual_bound(a["observables"], a["ctxs"], a["neg"]) if a["observables"] <= 24 else None
        print(f"   odd cycle C{n}: {a['observables']} observables, {a['contexts']} contexts, Gram dim {a['gram_dim']},"
              f" min rank {a['min_rank']} -> {a['qubits']} qubits" + (f", bound {b}/{a['contexts']}" if b is not None else ""))
        res[f"C{n}"] = a["qubits"]
    tri_c4 = [frozenset(e) for e in ({0, 1}, {1, 2}, {0, 2}, {2, 3}, {3, 4}, {4, 5}, {2, 5})]
    a = analyse([xy(6, S) for S in [frozenset()] + tri_c4])
    print(f"   triangle + 4-cycle sharing a vertex (n = 6): {a['observables']} observables, {a['qubits']} qubits")
    res["tri+C4"] = a["qubits"]
    bow = [frozenset(e) for e in ({0, 1}, {1, 2}, {0, 2}, {2, 3}, {3, 4}, {2, 4}, {0, 3})]  # deg check below
    for name, n, E in (("C3+C5 sharing a vertex", 7, [{0,1},{1,2},{0,2},{2,3},{3,4},{4,5},{5,6},{2,6}]),
                       ("C5 + C3 disjoint", 8, [{0,1},{1,2},{2,3},{3,4},{0,4},{5,6},{6,7},{5,7}])):
        E = [frozenset(e) for e in E]
        if any(sum(q in e for e in E) % 2 for q in range(n)) or len(E) % 2 == 0:
            print(f"   {name}: not an Eulerian graph with an odd number of edges, skipped"); continue
        a = analyse([xy(n, S) for S in [frozenset()] + E])
        print(f"   {name} (n = {n}): {a['observables']} observables, {a['qubits']} qubits")

if part in ("all", "b"):
    print("\n(b) N6: all X/Y families at n = 6 with |F| = 8 and the empty set in F")
    n = 6
    ev = [frozenset(S) for k in (2, 4, 6) for S in itertools.combinations(range(n), k)]
    vec = {S: sum(1 << q for q in S) for S in ev}
    back = {v: S for S, v in vec.items()}
    t0 = time.time(); tally = Counter(); best = None; seen = set()
    for six in itertools.combinations(ev, 6):
        x = 0
        for S in six: x ^= vec[S]
        if x == 0 or x not in back: continue
        last = back[x]
        if last in six or vec[last] < max(vec[S] for S in six): continue        # each 7-set once
        F = [frozenset()] + list(six) + [last]
        a = analyse([xy(n, S) for S in F])
        if a is None: tally["not magic"] += 1; continue
        tally[a["qubits"]] += 1
        if a["qubits"] == 6 and (best is None or a["observables"] < best["observables"]): best = a
    print(f"   outcomes (qubits -> count): {dict(tally)}  ({time.time() - t0:.0f}s)")
    if best: print(f"   smallest genuine 6-qubit: {best['observables']} observables, words {best['words']}")
    res["N6"] = (tally.get(6, 0) == 0)

if part in ("all", "c"):
    print("\n(c) NZ: three-letter families at n = 4 (first word XXXX), |F| <= 8")
    n = 4
    W = ["".join(w) for w in itertools.product("XYZ", repeat=n)]
    dist = lambda a, b: sum(x != y for x, y in zip(a, b))
    first = "X" * n
    cand = [w for w in W if w != first and dist(w, first) % 2 == 0]
    t0 = time.time(); tally = Counter(); best = None
    def grow(F, start):
        global best
        if len(F) % 2 == 0 and len(F) >= 2:
            cnt = Counter((q, w[q]) for w in F for q in range(n))
            if all(v % 2 == 0 for v in cnt.values()):
                a = analyse(F)
                if a is None: tally["not magic"] += 1
                else:
                    tally[a["qubits"]] += 1
                    if a["qubits"] == 4 and (best is None or a["observables"] < best["observables"]): best = a
        if len(F) == 8: return
        for k in range(start, len(cand)):
            w = cand[k]
            if all(dist(w, u) % 2 == 0 for u in F): grow(F + [w], k + 1)
    grow([first], 0)
    print(f"   outcomes (qubits -> count): {dict(tally)}  ({time.time() - t0:.0f}s)")
    if best: print(f"   smallest genuine 4-qubit: {best['observables']} observables, words {best['words']}")
    res["NZ"] = best is not None and best["observables"] <= 20
print("\nresults:", res)
