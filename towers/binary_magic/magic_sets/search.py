"""
search.py — operator-first search for small genuine n-qubit magic sets (see PREREG.md).

1. grow a pool of Pauli operators along commuting XOR lines {a, b, a^b}
2. list every context in the pool: 3-5 pairwise-commuting operators that XOR to zero
3. integer program: the parity clash using the fewest observables (even degree everywhere, odd negatives)
4. shrink to a context-minimal clash; cut it; repeat
5. qubit count of each minimal clash = half the minimum magic Gram rank
"""
import itertools, json, os, sys, time, random
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
from ms_core import symp, product_sign, check_magic, min_magic_rank, rank_rows, gram_of, label

def grow_pool(n, k, rnd, seeds=None):
    full = (1 << n) - 1
    pool = []
    seen = set()
    def add(op):
        if op != (0, 0) and op not in seen: seen.add(op); pool.append(op)
    for _ in range(seeds or 2 * n):
        add((rnd.randrange(1 << n), rnd.randrange(1 << n)))
    tries = 0
    while len(pool) < k and tries < 200 * k:
        tries += 1
        a, b = rnd.sample(pool, 2)
        if symp(a, b) == 0: add((a[0] ^ b[0], a[1] ^ b[1]))
        elif rnd.random() < 0.15: add((rnd.randrange(1 << n), rnd.randrange(1 << n)))
    return pool

def contexts(pool, max_size=4, cap=20000):
    idx = {op: i for i, op in enumerate(pool)}
    comm = [[symp(a, b) == 0 for b in pool] for a in pool]
    out = set()
    N = len(pool)
    for a in range(N):
        for b in range(a + 1, N):
            if not comm[a][b]: continue
            c = idx.get((pool[a][0] ^ pool[b][0], pool[a][1] ^ pool[b][1]))
            if c is not None and c > b: out.add((a, b, c))
    if max_size >= 4:
        for a in range(N):
            for b in range(a + 1, N):
                if not comm[a][b]: continue
                for c in range(b + 1, N):
                    if not (comm[a][c] and comm[b][c]): continue
                    d = idx.get((pool[a][0] ^ pool[b][0] ^ pool[c][0], pool[a][1] ^ pool[b][1] ^ pool[c][1]))
                    if d is not None and d > c: out.add((a, b, c, d))
                    if len(out) > cap: return sorted(out)
    return sorted(out)

def solve(pool, ctxs, signs, cuts, must=None, restrict=None, minimize="vertices"):
    """MILP over context choices x_c. Returns the chosen contexts or None."""
    C, V = len(ctxs), len(pool)
    nvar = C + V + V + 1                                   # x_c, y_v, z_v, w
    ix = lambda c: c; iy = lambda v: C + v; iz = lambda v: C + V + v; iw = C + 2 * V
    rows, lo, hi = [], [], []
    A = lil_matrix((V + sum(len(c) for c in ctxs) + 1 + len(cuts) + 1, nvar))
    r = 0
    for v in range(V):                                     # sum_c A_vc x_c - 2 z_v = 0
        A[r, iz(v)] = -2; lo.append(0); hi.append(0); r += 1
    for ci, c in enumerate(ctxs):
        for v in c: A[v, ix(ci)] = 1
    for ci, c in enumerate(ctxs):                          # x_c <= y_v
        for v in c:
            A[r, ix(ci)] = 1; A[r, iy(v)] = -1; lo.append(-np.inf); hi.append(0); r += 1
    for ci, s in enumerate(signs):                         # sum_c s_c x_c - 2 w = 1
        if s == -1: A[r, ix(ci)] = 1
    A[r, iw] = -2; lo.append(1); hi.append(1); r += 1
    for S in cuts:                                         # exclude every superset of a found minimal clash
        for ci in S: A[r, ix(ci)] = 1
        lo.append(-np.inf); hi.append(len(S) - 1); r += 1
    A = A[:r]
    ub = np.full(nvar, 1.0); ub[C + V: C + 2 * V] = 4 * len(ctxs); ub[iw] = len(ctxs)
    lb = np.zeros(nvar)
    if restrict is not None:
        for ci in range(C):
            if ci not in restrict: ub[ix(ci)] = 0
    if must:
        for v in must: lb[iy(v)] = 1
    cost = np.zeros(nvar)
    if minimize == "vertices": cost[C:C + V] = 1; cost[:C] = 1e-3
    else: cost[:C] = 1
    integrality = np.ones(nvar)
    res = milp(cost, constraints=[LinearConstraint(A.tocsr(), lo, hi)], bounds=Bounds(lb, ub),
               integrality=integrality, options={"time_limit": 60})
    if res.x is None: return None
    return [ci for ci in range(C) if res.x[ix(ci)] > 0.5]

def minimal_clash(pool, ctxs, signs, S):
    """shrink S to a minimum-cardinality clash inside it (context-minimal by construction)"""
    T = solve(pool, ctxs, signs, [], restrict=set(S), minimize="contexts")
    return T

def run(n, pool_size, rounds, seconds, seed, out):
    rnd = random.Random(seed)
    t0 = time.time(); best = {}
    found = []
    while time.time() - t0 < seconds:
        pool = grow_pool(n, pool_size, rnd)
        ctxs = contexts(pool)
        if not ctxs: continue
        signs = [product_sign([pool[v] for v in c]) for c in ctxs]
        cuts = []
        for _ in range(rounds):
            S = solve(pool, ctxs, signs, cuts)
            if S is None: break
            T = minimal_clash(pool, ctxs, signs, S)
            cuts.append(T)
            verts = sorted({v for ci in T for v in ctxs[ci]})
            ops = [pool[v] for v in verts]
            own = rank_rows(gram_of(ops)) // 2
            if own < n: continue                           # its own operators live on fewer qubits
            remap = {v: k for k, v in enumerate(verts)}
            hg = [tuple(remap[v] for v in ctxs[ci]) for ci in T]
            r, d = min_magic_rank(len(verts), hg, limit_dim=22, stop_at=2 * n - 2)
            q = r // 2 if isinstance(r, int) else None
            rec = dict(n=n, observables=len(verts), contexts=len(T), gram_dim=d, min_rank=r,
                       labels=[label(o, n) for o in ops], ctx=hg)
            found.append(rec)
            if q == n:
                if n not in best or len(verts) < best[n]["observables"]:
                    best[n] = rec
                    print(f"  [{time.time()-t0:6.0f}s] genuine {n}-qubit minimal clash: {len(verts)} observables,"
                          f" {len(T)} contexts (Gram dim {d})", flush=True)
            elif r == "too big":
                print(f"  [{time.time()-t0:6.0f}s] candidate {len(verts)} obs / {len(T)} ctx: Gram space dim {d}"
                      f" too big to certify (own operators: {own} qubits)", flush=True)
    json.dump(dict(best=best, found=found), open(out, "w"))
    return best, found

if __name__ == "__main__":
    n, pool_size, rounds, seconds, seed = (int(a) for a in sys.argv[1:6])
    out = sys.argv[6] if len(sys.argv) > 6 else f"search_n{n}_s{seed}.json"
    best, found = run(n, pool_size, rounds, seconds, seed, out)
    sizes = sorted((f["observables"], f["min_rank"]) for f in found if isinstance(f["min_rank"], int))
    print(f"\nn={n}: {len(found)} minimal clashes with full own rank; best genuine: "
          f"{best[n]['observables'] if n in best else None}")
    from collections import Counter
    print("  (observables, min rank) counts:", sorted(Counter(sizes).items())[:20])
