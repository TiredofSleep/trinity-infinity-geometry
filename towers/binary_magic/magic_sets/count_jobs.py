"""count_jobs.py: exact hypergraph counts for lower_bound4.py's jobs, with one shared cache (fast), plus the
counts for a symmetry-broken regime B: context 0 is a LARGEST context, of exact size s0, and no other context
is bigger. Every regime-B hypergraph has a largest context, of size > the regime-A cap, which needs its own
split T (Lemma 4), so relabelling it as context 0 loses nothing.
Usage: python count_jobs.py C V [n]"""
import itertools, sys
from functools import lru_cache
from lower_bound4 import jobs, generate

PAIRS = {}


@lru_cache(maxsize=None)
def count_mg(C, E, cap, need, allowed):
    pairs = [p for p in itertools.combinations(range(C), 2) if p in allowed]

    @lru_cache(maxsize=None)
    def rec(t, left, deg):
        if left == 0:
            return int(all(d >= n for d, n in zip(deg, need)))
        if t == len(pairs) or sum(c - d for c, d in zip(cap, deg)) < 2 * left:
            return 0
        i, j = pairs[t]
        total, m = 0, 0
        while m <= left and deg[i] + m <= cap[i] and deg[j] + m <= cap[j]:
            dd = list(deg); dd[i] += m; dd[j] += m
            total += rec(t + 1, left - m, tuple(dd))
            m += 1
        return total
    return rec(0, E, tuple([0] * C))


def count(C, V, job):
    tot = nh = 0
    for H, highs, cap, need, E in generate(C, V, job):
        nh += 1
        tot += count_mg(C, E, tuple(cap), tuple(need), frozenset(job[2]))
    return nh, tot


if __name__ == "__main__":
    C, V = int(sys.argv[1]), int(sys.argv[2])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    grand = 0
    for job in jobs(C, V, n):
        nh, tot = count(C, V, job); grand += tot
        print(f"  as written, job {job[0]:7s}: {nh:,} high-degree choices, {tot:,} hypergraphs", flush=True)
    print(f"(C, V) = ({C}, {V}), n = {n}, as written: {grand:,} hypergraphs", flush=True)
    small = V - C + 2 - n; big = V - n - 1
    sym = 0
    for job in jobs(C, V, n)[1:]:
        label, hp, pairs, caps, mins = job
        for s0 in range(small + 1, big + 1):
            j2 = (f"{label},s0={s0}", hp, pairs, [s0] * C, [s0] + mins[1:])
            nh, tot = count(C, V, j2); sym += tot
            print(f"  symmetry-broken {j2[0]:14s}: {nh:,} high-degree choices, {tot:,} hypergraphs", flush=True)
    print(f"regime B symmetry-broken: {sym:,} hypergraphs")
