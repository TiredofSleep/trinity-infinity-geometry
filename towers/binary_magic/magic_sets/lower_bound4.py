"""
lower_bound4.py: the 5-qubit lower bound (Round 11, L3-full), with a generator that builds only what
Lemma 4 allows instead of filtering afterwards. Written in Claude Code, 2026-10-24.

The question: is there a genuine 5-qubit minimal magic set with C contexts and V <= 15 observables?
Lemmas 2-3 leave (C, V) in {(5, 14), (5, 15), (6, 15)}. Lemma 4: every context has |c| <= V - C - 4 + dim R_c.

Two regimes, together complete:
  A. every context has at most V - C - 3 observables (the cap when dim R_c = 1): lower_bound2's generator
     with that cap;
  B. some context c is bigger. Then dim R_c >= 2: some proper, nonempty set T of the other contexts has a sum
     supported inside c, so every observable outside c meets T an even number of times. Relabel so that c is
     context 0 and |T| <= (C-1)/2 (T and its complement both work). Then observables outside c may only be
     degree-2 pairs inside T or inside its complement, or high-degree patterns meeting T evenly.
Every hypergraph is then filtered exactly as in lower_bound3.py (repeated contexts, minimality, the exact
Lemma 4, canonical dedup) and tested by the paper's own criterion (min_magic_rank from ms_core.py).

Calibration: the two finished cases, (5, 14) and (5, 15), must give the same distinct survivors as
lower_bound3.py did (216 and 2,543 cumulative).

General n (added for L4): Lemma 4 reads |c| <= V - C + 1 - n + dim R_c, so the regime-A cap is V - C + 2 - n,
and a class cap smax on context size can be imposed on top (L4: n = 4, contexts of 3-5). A regime-B job is
only needed when smax exceeds the regime-A cap.
Usage: python lower_bound4.py C V [processes] [n] [smax] [dump.json]   (defaults: 6, 5, no cap)
"""
import itertools, json, sys, time
from collections import Counter
from multiprocessing import Pool
from lower_bound2 import build, canon, is_minimal
from ms_core import min_magic_rank

def dim_Rc(ctxs):
    C = len(ctxs)
    vec = [sum(1 << v for v in c) for c in ctxs]
    out = []
    for i in range(C):
        sup = set()
        for T in range(1 << C):
            s = 0
            for j in range(C):
                if T >> j & 1:
                    s ^= vec[j]
            if s & ~vec[i] == 0:
                sup.add(s)
        out.append(len(sup).bit_length() - 1)
    return out


def canon_fast(C, ctxs, V):
    """A canonical form under relabelling the contexts. Contexts are first sorted by an invariant (size,
    the degrees of their observables, their overlaps with the others); only ties are permuted. Isomorphic
    hypergraphs get the same key, and the key determines the hypergraph up to relabelling."""
    sets = [set(c) for c in ctxs]
    pats = Counter(tuple(i for i in range(C) if v in sets[i]) for v in range(V))
    deg = {v: sum(v in s for s in sets) for v in range(V)}
    inv = [(len(sets[i]), tuple(sorted(deg[v] for v in sets[i])),
            tuple(sorted(len(sets[i] & sets[j]) for j in range(C) if j != i))) for i in range(C)]
    order = sorted(range(C), key=lambda i: inv[i])
    groups, cur = [], [order[0]]
    for i in order[1:]:
        if inv[i] == inv[cur[-1]]:
            cur.append(i)
        else:
            groups.append(cur); cur = [i]
    groups.append(cur)
    best = None
    for choice in itertools.product(*[itertools.permutations(g) for g in groups]):
        seq = [i for g in choice for i in g]
        pos = {ctx: k for k, ctx in enumerate(seq)}
        key = tuple(sorted((tuple(sorted(pos[i] for i in pat)), m) for pat, m in pats.items()))
        if best is None or key < best:
            best = key
    return best


def multigraphs(C, E, cap, need, allowed):
    """multisets of E edges on C nodes, using only the allowed pairs; returns full-length multiplicity tuples"""
    pairs = list(itertools.combinations(range(C), 2))
    use = [k for k, p in enumerate(pairs) if p in allowed]
    deg = [0] * C; mult = [0] * len(pairs)
    def rec(t, left):
        if left == 0:
            if all(deg[i] >= need[i] for i in range(C)):
                yield tuple(mult)
            return
        if t == len(use):
            return
        if sum(cap[i] - deg[i] for i in range(C)) < 2 * left:
            return
        k = use[t]; i, j = pairs[k]; m = 0
        while m <= left and deg[i] + m <= cap[i] and deg[j] + m <= cap[j]:
            mult[k] = m; deg[i] += m; deg[j] += m
            yield from rec(t + 1, left - m)
            deg[i] -= m; deg[j] -= m
            m += 1
        mult[k] = 0
    yield from rec(0, E)


def jobs(C, V, n=5, smax=None):
    """the generation tasks: (regime label, allowed high patterns, allowed pairs, per-context size caps, mins)"""
    small = V - C + 2 - n                                   # the Lemma-4 cap when dim R_c = 1
    big = V - C + 1 - n + (C - 2)                           # the absolute cap (dim R_c <= C - 2)
    if smax is not None:
        small, big = min(small, smax), min(big, smax)
    allpairs = set(itertools.combinations(range(C), 2))
    hp_all = [frozenset(s) for k in range(4, C + 1, 2) for s in itertools.combinations(range(C), k)]
    out = [("A", hp_all, allpairs, [small] * C, [3] * C)]
    if big <= small:                                        # the class cap leaves no room for regime B
        return out
    U = list(range(1, C))
    for t in range(1, (C - 1) // 2 + 1):                    # T = {1..t}, |T| <= (C-1)/2
        T = set(U[:t]); Tc = set(U[t:])
        pairs = {(0, x) for x in U} | {p for p in allpairs if 0 not in p and (set(p) <= T or set(p) <= Tc)}
        hps = [D for D in hp_all if 0 in D or len(D & T) % 2 == 0]
        out.append((f"B|T|={t}", hps, pairs, [big] * C, [small + 1] + [3] * (C - 1)))
    return out


def generate(C, V, job):
    label, hp, pairs, caps, mins = job
    for a in range(0, V + 1):
        if 4 * a > sum(caps):
            break
        for H in itertools.combinations_with_replacement(range(len(hp)), a):
            h = [0] * C
            for t in H:
                for i in hp[t]:
                    h[i] += 1
            if any(x > cap for x, cap in zip(h, caps)):
                continue
            cap = [cp - x for cp, x in zip(caps, h)]
            need = [max(0, mn - x) for mn, x in zip(mins, h)]
            E = V - a
            if 2 * E > sum(cap) or 2 * E < sum(need):
                continue
            yield H, [hp[t] for t in H], cap, need, E


def work(args):
    C, V, job_index, worker, P, n, smax = args
    job = jobs(C, V, n, smax)[job_index]
    tally, seen, hits, built = Counter(), {}, [], 0
    idx = 0
    for H, highs, cap, need, E in generate(C, V, job):
        idx += 1
        if idx % P != worker:
            continue
        for mg in multigraphs(C, E, cap, need, job[2]):
            built += 1
            _, ctxs = build(C, highs, mg)
            if len(set(map(frozenset, ctxs))) < C:
                tally["repeated context"] += 1; continue
            if not is_minimal(V, ctxs):
                tally["not minimal"] += 1; continue
            if job[0] != "A":                               # in regime A every context is within the cap
                dR = dim_Rc(ctxs)
                if any(len(c) > V - C + 1 - n + k for c, k in zip(ctxs, dR)):
                    tally["fails Lemma 4"] += 1; continue
            key = canon_fast(C, ctxs, V)
            if key in seen:
                continue
            q, d = min_magic_rank(V, ctxs, limit_dim=22, stop_at=2 * n - 2)
            res = ("none" if q is None else "unresolved" if q == "too big" else
                   "GENUINE" if q >= 2 * n else "fewer qubits")
            seen[key] = res
            if res in ("GENUINE", "unresolved"):
                hits.append((res, q, ctxs))
    return job[0], built, tally, seen, hits


def be_gentle():
    """below-normal priority on Windows; pool workers started afterwards inherit it"""
    if sys.platform == "win32":
        import ctypes
        k = ctypes.windll.kernel32
        k.SetPriorityClass(k.GetCurrentProcess(), 0x00004000)


if __name__ == "__main__":
    be_gentle()
    C, V = int(sys.argv[1]), int(sys.argv[2])
    P = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    n = int(sys.argv[4]) if len(sys.argv) > 4 else 5
    smax = int(sys.argv[5]) if len(sys.argv) > 5 and sys.argv[5] != "-" else None
    dump = sys.argv[6] if len(sys.argv) > 6 else None
    t0 = time.time()
    tasks = [(C, V, j, w, P, n, smax) for j in range(len(jobs(C, V, n, smax))) for w in range(P)]
    with Pool(P) as pool:
        results = pool.map(work, tasks, chunksize=1)
    built, tally, seen, hits = Counter(), Counter(), {}, []
    for label, b, t, s, h in results:
        built[label] += b; tally.update(t); seen.update(s); hits += h
    outcome = Counter(seen.values())
    print(f"(C, V) = ({C}, {V}), n = {n}, context sizes 3-{smax or 'Lemma 4'}:"
          f" {time.time() - t0:.0f}s with {P} processes")
    print("  built per regime:", {k: f"{v:,}" for k, v in sorted(built.items())})
    print("  filtered:", dict(tally))
    print(f"  distinct survivors: {len(seen):,}  ->  {dict(outcome)}")
    for h in hits:
        print("  HIT:", h)
    if dump:
        with open(dump, "w", encoding="utf-8", newline="") as fh:
            json.dump([[list(map(list, k)), v] for k, v in seen.items()], fh)
    print("RESULT:", f"no genuine {n}-qubit set in this case" if not hits else "SEE HITS")
