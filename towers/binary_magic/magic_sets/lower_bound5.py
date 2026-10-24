"""
lower_bound5.py: the n-qubit lower bound with a sharper regime B. Written in Claude Code, 2026-10-24.

Regime A is lower_bound4.py's: every context within the Lemma-4 cap V - C + 2 - n for dim R_c = 1.
Regime B: some context is bigger. Relabel a LARGEST context as context 0, of exact size s0, so every other
context has at most s0 observables. Put S = {T subset of {1..C-1} : the contexts in T sum to a vector inside c_0}.
The contexts 1..C-1 are independent (Lemma 2), so S is a subspace of F2^(C-1), it contains the all-ones set,
and dim S = dim R_{c_0} >= s0 - (V - C + 1 - n) =: k (Lemma 4). An observable outside c_0 has an even T-degree
for every T in S, so its pattern (the contexts containing it) lies in the orthogonal complement S^perp. An
observable inside c_0 has a pattern {0} + D with |D| odd. So it suffices to take, for each s0, one k-dimensional
S containing the all-ones set from each orbit under relabelling 1..C-1, and to build the multisets of s0 inside
patterns and V - s0 outside patterns. The outside multiset is taken once per orbit of the stabilizer of S.
Every hypergraph is then filtered exactly as in lower_bound4.py.

Calibration: (5, 14) and (5, 15) at n = 5 must give lower_bound4's 216 and 2,327 distinct survivors.
Usage: python lower_bound5.py C V [processes] [n]
"""
import itertools, sys, time
from collections import Counter
from multiprocessing import Pool
from lower_bound2 import is_minimal
from lower_bound4 import jobs, generate, multigraphs, build, dim_Rc, canon_fast, be_gentle
from ms_core import min_magic_rank


def bits(x, m):
    return frozenset(i + 1 for i in range(m) if x >> i & 1)


def span(gens):
    out = {0}
    for g in gens:
        out |= {x ^ g for x in out}
    return out


def subspaces(m, k):
    """one k-dim subspace of F2^m containing the all-ones vector from each orbit under permuting coordinates,
    each with its stabilizer (as permutations of 0..m-1)"""
    ones = (1 << m) - 1
    perms = list(itertools.permutations(range(m)))
    def act(p, x):
        return sum(1 << p[i] for i in range(m) if x >> i & 1)
    seen, reps = set(), []
    for gens in itertools.combinations(range(1, ones), k - 1):
        S = frozenset(span(list(gens) + [ones]))
        if len(S) != 1 << k or S in seen:
            continue
        orbit = {frozenset(act(p, x) for x in S) for p in perms}
        seen |= orbit
        stab = [p for p in perms if frozenset(act(p, x) for x in S) == S]
        reps.append((S, stab))
    return reps


def regime_b_jobs(C, V, n):
    small = V - C + 2 - n
    big = V - n - 1                                   # V - C + 1 - n + (C - 2)
    m = C - 1
    out = []
    for s0 in range(small + 1, big + 1):
        k = max(2, s0 - (V - C + 1 - n))
        for S, stab in subspaces(m, k):
            perp = [x for x in range(1, 1 << m) if all(bin(x & t).count("1") % 2 == 0 for t in S)]
            inside = [x for x in range(1 << m) if bin(x).count("1") % 2 == 1]
            out.append((s0, k, S, stab, perp, inside))
    return out


def outside_multisets(C, V, job):
    """canonical outside multisets (one per orbit of the stabilizer), as tuples of patterns"""
    s0, k, S, stab, perp, inside = job
    m = C - 1
    def act(p, x):
        return sum(1 << p[i] for i in range(m) if x >> i & 1)
    for ms in itertools.combinations_with_replacement(perp, V - s0):
        deg = Counter(i for x in ms for i in range(m) if x >> i & 1)
        if any(d > s0 for d in deg.values()):
            continue
        if ms == min(tuple(sorted(act(p, x) for x in ms)) for p in stab):
            yield ms


def work(args):
    C, V, n, ji, worker, P = args
    if ji == "A":
        job = jobs(C, V, n)[0]
        hyper = ((highs, mg) for idx, (H, highs, cap, need, E) in enumerate(generate(C, V, job))
                 if idx % P == worker for mg in multigraphs(C, E, cap, need, job[2]))
        label = "A"
    else:
        job = regime_b_jobs(C, V, n)[ji]
        label = f"B s0={job[0]} k={job[1]}"
    tally, seen, hits, built = Counter(), {}, [], 0
    def handle(ctxs):
        nonlocal built
        built += 1
        if len(set(map(frozenset, ctxs))) < C:
            tally["repeated context"] += 1; return
        if not is_minimal(V, ctxs):
            tally["not minimal"] += 1; return
        if ji != "A":
            dR = dim_Rc(ctxs)
            if any(len(c) > V - C + 1 - n + kk for c, kk in zip(ctxs, dR)):
                tally["fails Lemma 4"] += 1; return
        key = canon_fast(C, ctxs, V)
        if key in seen:
            return
        q, d = min_magic_rank(V, ctxs, limit_dim=22, stop_at=2 * n - 2)
        res = ("none" if q is None else "unresolved" if q == "too big" else
               "GENUINE" if q >= 2 * n else "fewer qubits")
        seen[key] = res
        if res in ("GENUINE", "unresolved"):
            hits.append((res, q, ctxs))
    if ji == "A":
        for highs, mg in hyper:
            handle(build(C, highs, mg)[1])
    else:
        s0, k, S, stab, perp, inside = job
        m = C - 1
        for oi, out_ms in enumerate(outside_multisets(C, V, job)):
            if oi % P != worker:
                continue
            odeg = [0] * C
            for x in out_ms:
                for i in range(m):
                    if x >> i & 1:
                        odeg[i + 1] += 1
            for in_ms in itertools.combinations_with_replacement(inside, s0):
                deg = odeg[:]
                for x in in_ms:
                    for i in range(m):
                        if x >> i & 1:
                            deg[i + 1] += 1
                if any(not 3 <= deg[i] <= s0 for i in range(1, C)):
                    continue
                ctxs = [[] for _ in range(C)]
                v = 0
                for x in in_ms:
                    ctxs[0].append(v)
                    for i in range(m):
                        if x >> i & 1:
                            ctxs[i + 1].append(v)
                    v += 1
                for x in out_ms:
                    for i in range(m):
                        if x >> i & 1:
                            ctxs[i + 1].append(v)
                    v += 1
                handle([tuple(c) for c in ctxs])
    return label, built, tally, seen, hits


if __name__ == "__main__":
    be_gentle()
    C, V = int(sys.argv[1]), int(sys.argv[2])
    P = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    t0 = time.time()
    bjobs = regime_b_jobs(C, V, n)
    print(f"(C, V) = ({C}, {V}), n = {n}: regime A plus {len(bjobs)} regime-B jobs "
          f"{[(j[0], j[1], len(j[4])) for j in bjobs]} (s0, k, outside patterns)", flush=True)
    tasks = [(C, V, n, "A", w, P) for w in range(P)] + [(C, V, n, j, w, P) for j in range(len(bjobs)) for w in range(P)]
    built, tally, seen, hits = Counter(), Counter(), {}, []
    with Pool(P) as pool:
        for label, b, t, s, h in pool.imap_unordered(work, tasks):
            built[label] += b; tally.update(t); hits += h
            for key, res in s.items():
                seen[key] = res
    outcome = Counter(seen.values())
    print(f"done in {time.time() - t0:.0f}s with {P} processes")
    print("  built per job:", {k: f"{v:,}" for k, v in sorted(built.items())})
    print("  filtered:", dict(tally))
    print(f"  distinct survivors: {len(seen):,}  ->  {dict(outcome)}")
    for h in hits:
        print("  HIT:", h)
    print("RESULT:", f"no genuine {n}-qubit set in this case" if not hits else "SEE HITS")
