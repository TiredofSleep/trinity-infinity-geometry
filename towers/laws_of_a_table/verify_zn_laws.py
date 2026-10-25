#!/usr/bin/env python3
"""verify_zn_laws.py -- what the ETP's 4694 laws can see of Z/n and of -(x+y) mod n.

    python verify_zn_laws.py        # about ten seconds; needs numpy

Rebuilds the catalog of the Equational Theories Project (ETP) from its definition (no download), checks it
against known ETP numbers, then checks every [FORCED] line of THE_LAWS_OF_ZN.md.
Exits with status 1 on any failure.  Output is ASCII only.
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


def mirror_t(t):
    return t if isinstance(t, int) else (mirror_t(t[1]), mirror_t(t[0]))


MIR = [0] + [ID[key(mirror_t(s), mirror_t(t))] for s, t in LAWS]


def mirror(S):
    return {MIR[i] for i in S}




import math
from collections import Counter

# ------------------------------------------------------------------ 1. the gap of a law


def counts(t, signed, depth=0, acc=None):
    """occurrences of each variable; signed: a leaf at depth d counts (-1)^d"""
    acc = Counter() if acc is None else acc
    if isinstance(t, int):
        acc[t] += (-1) ** depth if signed else 1
    else:
        counts(t[0], signed, depth + 1, acc)
        counts(t[1], signed, depth + 1, acc)
    return acc


def gap(i, signed):
    s, t = LAWS[i - 1]
    a, b = counts(s, signed), counts(t, signed)
    g = 0
    for v in set(a) | set(b):
        g = math.gcd(g, a[v] - b[v])
    return g


G = {i: gap(i, False) for i in range(1, N + 1)}
GS = {i: gap(i, True) for i in range(1, N + 1)}
print("\n1 -- the gap of a law")
check("Z/n (x*y = x+y): a term is the sum of its leaves; gaps 0, 1, 2, 3, 4 occur for 32, 4003, 547, 28, 84 laws",
      dict(Counter(G.values())) == {0: 32, 1: 4003, 2: 547, 3: 28, 4: 84})
check("-(x+y) mod n: a leaf at depth d counts (-1)^d; gaps 0, 1, 2, 3, 6 occur for 294, 3946, 366, 85, 3 laws",
      dict(Counter(GS.values())) == {0: 294, 1: 3946, 2: 366, 3: 85, 6: 3})
six = sorted(i for i, g in GS.items() if g == 6)
check("the three laws of gap 6 are #817, #2644, #3659: " + "; ".join(show(i) for i in six), six == [817, 2644, 3659])

print("\n2 -- a law holds mod n exactly when n divides its gap (direct evaluation, n = 1..8, 12)")
ZN = lambda n: np.add.outer(np.arange(n), np.arange(n)) % n
NG = lambda n: (-np.add.outer(np.arange(n), np.arange(n))) % n
sz, szn = [], []
for n in list(range(1, 9)) + [12]:
    pz, pn = profile(ZN(n)), profile(NG(n))
    check(f"n = {n}: Z/n has {len(pz)} laws, -(x+y) mod n has {len(pn)}; both exactly as the gaps predict",
          pz == {i for i, g in G.items() if g % n == 0} and pn == {i for i, g in GS.items() if g % n == 0})
    sz.append(len(pz))
    szn.append(len(pn))
check("sizes for n = 1..8: Z/n 4694, 663, 60, 116, 32, 32, 32, 32; -(x+y) 4694, 663, 382, 294, 294, 297, 294, 294",
      sz[:8] == [4694, 663, 60, 116, 32, 32, 32, 32] and szn[:8] == [4694, 663, 382, 294, 294, 297, 294, 294])
check("so for every n >= 5, Z/n satisfies the same 32 laws; for every n >= 4 except n = 6, -(x+y) mod n "
      "satisfies the same 294 (no gap is >= 5, resp. >= 7, and 6 is the only gap above 3)",
      max(G.values()) == 4 and sorted(set(GS.values())) == [0, 1, 2, 3, 6])

print("\n3 -- which varieties these are")
BAL = {i for i, g in G.items() if g == 0}
check("the 32 laws of gap 0 are the balanced ones (each variable equally often on both sides): sorting the "
      "leaves proves each in every commutative semigroup, and Z/5 (a commutative semigroup) fails the rest; "
      "so they are exactly the laws of commutative semigroups in the catalog",
      all(sorted(leaves(LAWS[i - 1][0])) == sorted(leaves(LAWS[i - 1][1])) for i in BAL) and len(BAL) == 32)


def tsq_nf(t):
    """totally symmetric quasigroups: u*v = v*u and u*(u*v) = v; every step is an instance of an axiom"""
    if isinstance(t, int):
        return ("v", t)
    a, b = tsq_nf(t[0]), tsq_nf(t[1])
    if b[0] == "m" and a in (b[1], b[2]):
        return b[2] if a == b[1] else b[1]
    if a[0] == "m" and b in (a[1], a[2]):
        return a[2] if b == a[1] else a[1]
    return ("m",) + tuple(sorted((a, b), key=repr))


TSQ = {i for i, (s, t) in enumerate(LAWS, 1) if tsq_nf(s) == tsq_nf(t)}
N4 = NG(4)
is_tsq = np.array_equal(N4, N4.T) and all(N4[x, N4[x, y]] == y for x in range(4) for y in range(4))
check("rewriting with u*v = v*u and u*(u*v) = v proves 294 laws in every totally symmetric quasigroup (TSQ); "
      "-(x+y) mod 4 is a TSQ and satisfies exactly these 294: they are the catalog laws of TSQs",
      len(TSQ) == 294 and is_tsq and profile(N4) == TSQ)
C2 = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}
S3 = profile(NG(3))
check("the 32 and the 294 share exactly the 14 laws of commutativity's closure; the 294 lie inside the 382 "
      "laws of the 3-element Steiner quasigroup -(x+y) mod 3", (BAL & TSQ) == C2 and TSQ <= S3 and len(S3) == 382)

print("\n4 -- three statements of the archived paper, corrected")
check("(2x + 2y) mod 3 = -(x+y) mod 3 has 382 laws, not 179", len(profile(NG(3))) == 382)
check("-(x+y) mod 6 has 297 laws, not 294: the archived conjecture '294 for every n >= 4' fails at n = 6", len(profile(NG(6))) == 297)
check("Z/n's 32 laws are not inside the 294 (associativity #4512 fails in -(x+y)); the archived '294 = 32 + 262' is false",
      4512 in BAL and 4512 not in TSQ)

print(f"\n{'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' CHECK(S) FAILED'} ({time.time() - T0:.0f} s)")
sys.exit(1 if FAILS else 0)
