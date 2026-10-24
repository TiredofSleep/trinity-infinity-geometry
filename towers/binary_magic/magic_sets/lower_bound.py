"""
lower_bound.py — Round 11 of PREREG.md.

LEMMA. Let a magic set have V observables, contexts with incidence matrix A (V x C) of rank r over F2, and
suppose it is genuine n-qubit. Take any magic Pauli assignment with vectors v_1..v_V in F2^(2k). Each context
multiplies to +-I, so its vectors sum to 0: the r independent columns of A are r independent linear relations
among the v_i. Hence dim span(v) <= V - r. The symplectic Gram matrix has rank <= dim span. Genuineness
forces that rank to be >= 2n (Corollary 10 of Trandafir-Lisonek-Cabello). So V >= 2n + r.

SEARCH. Hypergraphs are described by observable "membership patterns": each observable lies in an
even-size set of contexts. Enumerate pattern multiplicities with up to C_max contexts of size in [3, s_max]
and V <= V_max. Dedupe up to permutations of contexts. Filter by V - r >= 2n. Test with min_magic_rank.
"""
import itertools, sys, time
from collections import Counter
from ms_core import min_magic_rank, rank_rows

def incidence_rank(ctxs, V):
    rows = []
    for c in ctxs:
        m = 0
        for v in c: m |= 1 << v
        rows.append(m)
    return rank_rows(rows)

def enumerate_hypergraphs(C, smin, smax, Vmax):
    pats = [frozenset(s) for k in range(2, C + 1, 2) for s in itertools.combinations(range(C), k)]
    perms = list(itertools.permutations(range(C)))
    seen = set()
    def canon(mult):
        best = None
        for p in perms:
            key = tuple(sorted((tuple(sorted(p[i] for i in pat)), m) for pat, m in mult.items() if m))
            if best is None or key < best: best = key
        return best
    sizes = [0] * C
    mult = {}
    def rec(k, V):
        if k == len(pats):
            if V == 0 or any(s < smin for s in sizes): return
            if any(s == 0 for s in sizes): return
            key = canon(mult)
            if key in seen: return
            seen.add(key)
            yield dict(mult)
            return
        pat = pats[k]
        m = 0
        while True:
            if V + m > Vmax or any(sizes[i] > smax for i in pat): break
            mult[pat] = m
            yield from rec(k + 1, V + m)
            for i in pat: sizes[i] += 1
            m += 1
        for i in pat: sizes[i] -= m
        mult.pop(pat, None)
    yield from rec(0, 0)

def build(mult, C):
    ctxs = [[] for _ in range(C)]; V = 0
    for pat, m in mult.items():
        for _ in range(m):
            for i in pat: ctxs[i].append(V)
            V += 1
    return V, [tuple(c) for c in ctxs]

def run(n, Cmax, smax, Vmax, label):
    t0 = time.time(); found = []; tally = Counter()
    for C in range(3, Cmax + 1):
        for mult in enumerate_hypergraphs(C, 3, smax, Vmax):
            V, ctxs = build(mult, C)
            if len(set(ctxs)) < C: tally["repeated context"] += 1; continue
            r = incidence_rank(ctxs, V)
            if V - r < 2 * n: tally["V - r < 2n"] += 1; continue
            q, d = min_magic_rank(V, ctxs, limit_dim=22, stop_at=2 * n - 2)
            if q is None: tally["no magic assignment"] += 1; continue
            if q == "too big": tally["unresolved (Gram space too big)"] += 1; found.append(("?", V, C, ctxs)); continue
            if q >= 2 * n:
                tally["genuine"] += 1; found.append((q // 2, V, C, ctxs))
            else: tally[f"realisable on <{n} qubits"] += 1
    best = min((f[1] for f in found if f[0] != "?"), default=None)
    print(f"{label}: tested in {time.time() - t0:.0f}s; outcomes {dict(tally)}; smallest genuine: {best}", flush=True)
    return found, tally, best

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "cal"
    res = {}
    if which in ("cal", "all"):
        f2, t2, b2 = run(2, 6, 3, 9, "L1 n=2 (<=6 contexts, size 3, V<=9)")
        res["L1"] = b2 == 9
        f3, t3, b3 = run(3, 6, 4, 10, "L2 n=3 (<=6 contexts, size 3-4, V<=10)")
        res["L2"] = b3 == 10
    if which in ("n4", "all"):
        f4, t4, b4 = run(4, 6, 5, 30, "L4 n=4 (<=6 contexts, size 3-5)")
        res["L4"] = b4 is None and t4.get("unresolved (Gram space too big)", 0) == 0
    if which in ("n5", "all"):
        f5, t5, b5 = run(5, 6, 6, 15, "L3 n=5 (<=6 contexts, size 3-6, V<=15)")
        res["L3"] = b5 is None and t5.get("unresolved (Gram space too big)", 0) == 0
    print("SCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
