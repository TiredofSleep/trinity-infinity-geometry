#!/usr/bin/env python3
"""verify_mirror.py -- the mirror of a magma table is a coin on the ETP's 4694 laws.

    python verify_mirror.py        # about 30 seconds; needs numpy

Rebuilds the catalog of the Equational Theories Project (ETP) from its definition (no download),
checks the rebuild against laws whose ETP numbers are known, and then checks every
[FORCED] line of THE_MIRROR.md.  Exits with status 1 on any failure.  Output is ASCII only.
"""
import itertools
import sys
import time

import numpy as np

T0 = time.time()
FAILS = []


def check(name, cond):
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    if not cond:
        FAILS.append(name)


# ------------------------------------------------------------------ the catalog, rebuilt
# Laws s = t with at most 4 operations, up to renaming variables and swapping sides; t = t dropped
# except x = x.  Order: total operations; operations on the smaller (left) side; left shape; right
# shape (shapes listed by size of the left subtree); variable pattern as a restricted-growth string.

def shapes(k):
    if k == 0:
        return [0]
    return [(a, b) for i in range(k) for a in shapes(i) for b in shapes(k - 1 - i)]


def nleaves(s):
    return 1 if s == 0 else nleaves(s[0]) + nleaves(s[1])


def rgs(m):
    out = [(0,)]
    for _ in range(m - 1):
        out = [p + (v,) for p in out for v in range(max(p) + 2)]
    return out


def plant(s, lab, i=0):
    if s == 0:
        return lab[i], i + 1
    a, i = plant(s[0], lab, i)
    b, i = plant(s[1], lab, i)
    return (a, b), i


def leaves(t):
    return [t] if isinstance(t, int) else leaves(t[0]) + leaves(t[1])


def nops(t):
    return 0 if isinstance(t, int) else 1 + nops(t[0]) + nops(t[1])


def rename(t, m):
    return m[t] if isinstance(t, int) else (rename(t[0], m), rename(t[1], m))


def key(s, t):
    def norm(a, b):
        m = {}
        for v in leaves(a) + leaves(b):
            m.setdefault(v, len(m))
        return repr((rename(a, m), rename(b, m)))
    return min(norm(s, t), norm(t, s))


LAWS, SEEN = [], set()
for total in range(5):
    for small in range(total // 2 + 1):
        for sl in shapes(small):
            for sr in shapes(total - small):
                for g in rgs(nleaves(sl) + nleaves(sr)):
                    s, i = plant(sl, g)
                    t, _ = plant(sr, g, i)
                    if total and s == t:
                        continue
                    k = key(s, t)
                    if k not in SEEN:
                        SEEN.add(k)
                        LAWS.append((s, t))
N = len(LAWS)
NV = [max(leaves(s) + leaves(t)) + 1 for s, t in LAWS]
ID = {key(s, t): i for i, (s, t) in enumerate(LAWS, 1)}


def show_t(t, top=True):
    if isinstance(t, int):
        return "xyzwuv"[t]
    s = show_t(t[0], False) + " * " + show_t(t[1], False)
    return s if top else "(" + s + ")"


def show(i):
    return show_t(LAWS[i - 1][0]) + " = " + show_t(LAWS[i - 1][1])


print("0 -- the ETP catalog, rebuilt from its definition")
check("4694 laws", N == 4694)
check("laws per number of operations 2, 5, 39, 364, 4284 (OEIS A376640)",
      [sum(1 for s, t in LAWS if nops(s) + nops(t) == k) for k in range(5)] == [2, 5, 39, 364, 4284])
KNOWN = {1: "x = x", 2: "x = y", 3: "x = x * x", 4: "x = x * y", 5: "x = y * x", 8: "x = x * (x * x)",
         14: "x = y * (x * y)", 16: "x = y * (y * x)", 23: "x = (x * x) * x", 40: "x * x = y * y",
         43: "x * y = y * x", 46: "x * y = z * w", 168: "x = (y * x) * (x * z)",
         4512: "x * (y * z) = (x * y) * z", 4694: "(x * y) * z = (w * u) * v"}
check("ETP numbers of 15 known laws (e.g. #43 commutativity, #168 central groupoid, #4512 associativity)",
      all(show(i) == s for i, s in KNOWN.items()))

# ------------------------------------------------------------------ evaluation


def ev(t, T, env):
    return env[t] if isinstance(t, int) else T[ev(t[0], T, env), ev(t[1], T, env)]


def evb(t, TF, n, env):
    """batch: TF is (B, n*n); returns (B, N) or (N,) for a bare variable"""
    if isinstance(t, int):
        return env[t]
    a, b = evb(t[0], TF, n, env), evb(t[1], TF, n, env)
    idx = a * n + b
    return TF[:, idx] if idx.ndim == 1 else np.take_along_axis(TF, idx, axis=1)


GRID = {}


def grid(n, k):
    if (n, k) not in GRID:
        GRID[n, k] = np.indices((n,) * k).reshape(k, -1)
    return GRID[n, k]


def profiles(tables):
    """(B, N) boolean matrix: which laws hold in each table (exhaustive; a few random assignments
    are tried first, which only discards laws that already fail)"""
    tables = np.asarray(tables, dtype=np.int64)
    B, n, _ = tables.shape
    TF = tables.reshape(B, n * n)
    res = np.zeros((B, N), dtype=bool)
    rng = np.random.default_rng(1)
    for col, (s, t) in enumerate(LAWS):
        k = NV[col]
        alive = np.arange(B)
        if n ** k > 32:
            env = rng.integers(0, n, size=(k, 8))
            a, b = evb(s, TF, n, env), evb(t, TF, n, env)
            a = np.broadcast_to(a, (B, 8)) if a.ndim == 1 else a
            b = np.broadcast_to(b, (B, 8)) if b.ndim == 1 else b
            alive = np.flatnonzero(np.all(a == b, axis=1))
            if not len(alive):
                continue
        env = grid(n, k)
        sub = TF[alive]
        a, b = evb(s, sub, n, env), evb(t, sub, n, env)
        a = np.broadcast_to(a, (len(alive), a.shape[-1])) if a.ndim == 1 else a
        b = np.broadcast_to(b, (len(alive), b.shape[-1])) if b.ndim == 1 else b
        res[alive[np.all(a == b, axis=1)], col] = True
    return res


def profile(T):
    return set(np.flatnonzero(profiles([T])[0]) + 1)


# ------------------------------------------------------------------ 1. the mirror on laws

def mirror_t(t):
    return t if isinstance(t, int) else (mirror_t(t[1]), mirror_t(t[0]))


MIR = [0] + [ID[key(mirror_t(s), mirror_t(t))] for s, t in LAWS]


def mirror(S):
    return {MIR[i] for i in S}


print("\n1 -- the mirror on the 4694 laws")
check("mirroring twice changes nothing (it is a flip)", all(MIR[MIR[i]] == i for i in range(1, N + 1)))
edge = [i for i in range(1, N + 1) if MIR[i] == i]
check("edge: 84 laws are their own mirror image; sides: the other 4610 form 2305 pairs",
      len(edge) == 84 and (N - 84) % 2 == 0 and (N - 84) // 2 == 2305)
byop = [sum(1 for i in edge if nops(LAWS[i - 1][0]) + nops(LAWS[i - 1][1]) == k) for k in range(5)]
check("the 84 by number of operations: 2, 3, 5, 12, 62", byop == [2, 3, 5, 12, 62])
check("commutativity #43, associativity #4512 and #40 x*x = y*y are on the edge", {40, 43, 4512} <= set(edge))
# agreement with the ETP's own list of duals (data/dual_equations.md) and its paper (arXiv:2512.07087)
pairs = [(4, 5), (8, 23), (9, 28), (10, 25), (38, 39), (42, 45), (47, 255), (327, 395), (677, 2910)]
check("dual pairs named by the ETP: 4|5, 8|23, 9|28, 10|25, 38|39, 42|45, 47|255, 327|395, 677|2910",
      all(MIR[a] == b for a, b in pairs))
check("laws the ETP's dual list omits as self-dual: 3, 6, 7, 40, 41, 44, 46, 151, 159, 168, 202",
      all(MIR[i] == i for i in (3, 6, 7, 40, 41, 44, 46, 151, 159, 168, 202)))

# ------------------------------------------------------------------ 2. the mirror on tables and profiles

print("\n2 -- the opposite magma: profile(transpose of T) = mirror(profile(T))")
rng = np.random.default_rng(7)
rand = [rng.integers(0, n, size=(n, n)) for n in (2, 3, 4, 5) for _ in range(3)]
check("12 random magmas of orders 2-5", all(profile(T.T) == mirror(profile(T)) for T in rand))


def canon(tables):
    tables = np.asarray(tables)
    B, n, _ = tables.shape
    w = (n ** np.arange(n * n - 1, -1, -1)).astype(np.int64)
    best = None
    for p in itertools.permutations(range(n)):
        p = np.array(p)
        inv = np.argsort(p)
        c = (p[tables[:, inv[:, None], inv[None, :]]].reshape(B, -1).astype(np.int64)) @ w
        best = c if best is None else np.minimum(best, c)
    return best


for n in (2, 3):
    alltabs = np.array(list(itertools.product(range(n), repeat=n * n)), dtype=np.int64).reshape(-1, n, n)
    codes = canon(alltabs)
    _, first = np.unique(codes, return_index=True)
    reps = alltabs[first]                         # one table per isomorphism class
    P = profiles(reps)
    PT = profiles(reps.transpose(0, 2, 1))
    sets = [frozenset(np.flatnonzero(r) + 1) for r in P]
    setsT = [frozenset(np.flatnonzero(r) + 1) for r in PT]
    check(f"order {n}: all {len(alltabs)} tables ({len(reps)} up to renaming): transpose -> mirror",
          all(b == frozenset(mirror(a)) for a, b in zip(sets, setsT)))
    comm = np.array([np.array_equal(T, T.T) for T in reps])
    perms = [np.array(p) for p in itertools.permutations(range(n))]
    selfop = np.array([any(np.array_equal(p[T[np.argsort(p)][:, np.argsort(p)]], T.T) for p in perms) for T in reps])
    distinct = set(sets)
    sm = {S for S in distinct if frozenset(mirror(S)) == S}
    by = {}
    for S, c, so in zip(sets, comm, selfop):
        a, b = by.get(S, (False, False))
        by[S] = (a or c, b or so)
    kinds = (sum(1 for S in sm if by[S][0]), sum(1 for S in sm if not by[S][0] and by[S][1]),
             sum(1 for S in sm if not by[S][1]))
    if n == 2:
        check("order 2: 10 distinct profiles, 4 of them their own mirror", len(distinct) == 10 and len(sm) == 4)
    else:
        nfix = 3 ** 6
        check("order 3: the transpose fixes the 729 commutative tables and pairs the other 18954 (9477 pairs)",
              nfix == 729 and (19683 - nfix) // 2 == 9477)
        check("order 3: 2639 distinct profiles; 101 are their own mirror (the edge of the induced flip)",
              len(distinct) == 2639 and len(sm) == 101)
        check("order 3: of the 101: 78 have a commutative table, 6 more a table isomorphic to its transpose, "
              "17 neither (the profile cannot see that flip)", kinds == (78, 6, 17))
        ex = np.array([[0, 0, 0], [0, 1, 2], [2, 1, 2]])
        pe = profile(ex)
        check("example of the 17: [[0,0,0],[0,1,2],[2,1,2]] -- profile of 62 laws, its own mirror, "
              "yet the table is not isomorphic to its transpose",
              len(pe) == 62 and mirror(pe) == pe and not any(
                  np.array_equal(p[ex[np.argsort(p)][:, np.argsort(p)]], ex.T) for p in perms))

# ------------------------------------------------------------------ 3. closures and the mirror

print("\n3 -- closures follow the mirror: the eight closures of size 14")


def nf(t, node):
    return ("v", t) if isinstance(t, int) else node(nf(t[0], node), nf(t[1], node))


RULES = {
    40: lambda a, b: ("c",) if a == b else ("m", a, b),                       # all squares equal
    43: lambda a, b: ("m",) + tuple(sorted((a, b), key=repr)),                # factors commute
    4295: lambda a, b: ("P",) + tuple(sorted((a, b[2]), key=repr)) if b[0] == "m" else ("m", a, b),
    4303: lambda a, b: ("Q",) + tuple(sorted((b[1], b[2]), key=repr)) if b[0] == "m" else ("m", a, b),
}
SPEC = {40: [[0, 0, 1], [1, 0, 2], [1, 1, 0]], 43: [[0, 0, 1], [0, 2, 0], [1, 0, 0]],
        4295: [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2],
               [0, 3, 3, 0, 3, 4]],
        4303: [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 4, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]}
CL = {}
for a, rule in RULES.items():
    derived = {1} | {i for i, (s, t) in enumerate(LAWS, 1) if nf(s, rule) == nf(t, rule)}
    T = np.array(SPEC[a])
    CL[a] = derived
    check(f"#{a} {show(a)}: 14 laws follow by rewriting, and a {len(T)}-element model satisfies exactly them",
          len(derived) == 14 and profile(T) == derived)
check("C1 (#40) and C2 (#43) are their own mirror: on the edge", mirror(CL[40]) == CL[40] and mirror(CL[43]) == CL[43])
check("C5 (#4295) mirrors to C7, which contains #4610; C6 (#4303) mirrors to C8, which contains #4637",
      4610 in mirror(CL[4295]) and 4637 in mirror(CL[4303]) and mirror(CL[4295]) != CL[4295])
for a, b in ((4295, 4610), (4303, 4637)):
    T = np.array(SPEC[a]).T
    check(f"the transpose of the #{a} specimen satisfies #{b} and has profile exactly mirror(C)",
          profile(T) == mirror(CL[a]))
check("#1312 and #2241 are mirror images (C3 and C4)", MIR[1312] == 2241)

print(f"\n{'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' CHECK(S) FAILED'} ({time.time() - T0:.0f} s)")
sys.exit(1 if FAILS else 0)
