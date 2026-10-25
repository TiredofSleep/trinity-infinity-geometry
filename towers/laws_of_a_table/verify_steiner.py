#!/usr/bin/env python3
"""verify_steiner.py -- every Steiner triple system satisfies the same 382 laws of the ETP catalog.

    python verify_steiner.py       # about six seconds; needs numpy

Rebuilds the catalog of the Equational Theories Project (ETP) from its definition (no download), checks it
against known ETP numbers, then checks every [FORCED] line of STEINER_SYSTEMS.md.
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




# ------------------------------------------------------------------ Steiner quasigroups


def sq_nf(t):
    """squags: u*u = u, u*v = v*u, u*(u*v) = v; every rewrite step is an instance of an axiom"""
    if isinstance(t, int):
        return ("v", t)
    a, b = sq_nf(t[0]), sq_nf(t[1])
    if a == b:
        return a
    if b[0] == "m" and a in (b[1], b[2]):
        return b[2] if a == b[1] else b[1]
    if a[0] == "m" and b in (a[1], a[2]):
        return a[2] if b == a[1] else a[1]
    return ("m",) + tuple(sorted((a, b), key=repr))


def from_blocks(v, blocks):
    T = -np.ones((v, v), dtype=np.int64)
    np.fill_diagonal(T, np.arange(v))
    for b in blocks:
        for i in range(3):
            for j in range(3):
                if i != j:
                    T[b[i], b[j]] = b[3 - i - j]
    return T


def cyclic(v, base, short=None):
    bl = {tuple(sorted((x + s) % v for x in bb)) for bb in base for s in range(v)}
    if short:
        bl |= {tuple(sorted((x + s) % v for x in short)) for s in range(v // 3)}
    return from_blocks(v, sorted(bl))


def affine3(m):                       # AG(m,3): x*y = -(x+y) coordinatewise mod 3
    pts = list(itertools.product(range(3), repeat=m))
    ix = {p: i for i, p in enumerate(pts)}
    return np.array([[ix[tuple((-a - b) % 3 for a, b in zip(p, q))] for q in pts] for p in pts])


def projective2(m):                   # PG(m-1,2): nonzero vectors of GF(2)^m, x*y = x+y, x*x = x
    v = 2 ** m - 1
    T = np.array([[(x + 1) ^ (y + 1) for y in range(v)] for x in range(v)]) - 1
    np.fill_diagonal(T, np.arange(v))
    return T


def is_squag(T):
    v = len(T)
    return (np.array_equal(np.diag(T), np.arange(v)) and np.array_equal(T, T.T)
            and all(T[x, T[x, y]] == y for x in range(v) for y in range(v)))


print("\n1 -- the 3-point line and what every squag proves")
S3 = affine3(1)
P3 = profile(S3)
PROVED = {i for i, (s, t) in enumerate(LAWS, 1) if sq_nf(s) == sq_nf(t)}
check("STS(3), the 3-element squag x*y = -(x+y) mod 3, satisfies 382 laws", is_squag(S3) and len(P3) == 382)
check("rewriting with the squag axioms proves exactly these 382 laws in every squag (and nothing that fails in STS(3))",
      PROVED == P3)
check("in any squag, two elements a != b generate {a, b, a*b}, a copy of STS(3); a law true in a magma is true "
      "in each of its submagmas -- so a squag with >= 3 elements satisfies at most these 382; hence exactly these",
      True)

print("\n2 -- direct check on Steiner triple systems")
SYSTEMS = [("STS(7)  Fano plane PG(2,2)", projective2(3)), ("STS(9)  affine plane AG(2,3)", affine3(2)),
           ("STS(13) cyclic, base blocks {0,1,4} {0,2,7}", cyclic(13, [(0, 1, 4), (0, 2, 7)])),
           ("STS(15) PG(3,2)", projective2(4)),
           ("STS(15) cyclic, {0,1,4} {0,2,8} + short orbit {0,5,10}", cyclic(15, [(0, 1, 4), (0, 2, 8)], (0, 5, 10))),
           ("STS(19) cyclic, {0,1,4} {0,2,9} {0,5,11}", cyclic(19, [(0, 1, 4), (0, 2, 9), (0, 5, 11)])),
           ("STS(27) AG(3,3)", affine3(3)), ("STS(31) PG(4,2)", projective2(5))]
rng = np.random.default_rng(11)
for name, T in SYSTEMS:
    v = len(T)
    sub = True
    for a in range(v):
        for b in range(a + 1, v):
            S = [a, b, int(T[a, b])]
            sub &= len(set(S)) == 3 and all(int(T[p, q]) in S for p in S for q in S)
    if v <= 13:
        ok = profile(T) == P3                         # every law, every assignment
        how = "exhaustive"
    else:                                             # the 382 hold by the theorem; refute all others
        ok = True
        for i in range(1, N + 1):
            if i in P3:
                continue
            s, t = LAWS[i - 1]
            env = rng.integers(0, v, size=(NV[i - 1], 4000))
            if np.array_equal(ev(s, T, env), ev(t, T, env)):
                env = rng.integers(0, v, size=(NV[i - 1], 400000))
                if np.array_equal(ev(s, T, env), ev(t, T, env)):
                    print("    law", i, "not refuted by sampling")
                    ok = False
                    break
        how = "every other law refuted by an explicit assignment"
    check(f"{name}: a squag, with STS(3) inside; its profile is the same 382 laws ({how})", is_squag(T) and sub and ok)

print("\n3 -- the archive's '40 small-order coincidences'")
FORTY = [313, 315, 362, 365, 3272, 3278, 3414, 3417, 3472, 3484, 3588, 3601, 3668, 3678, 3685, 3687, 3871, 3878, 3994,
         4007, 4068, 4091, 4135, 4162, 4273, 4275, 4305, 4307, 4332, 4383, 4386, 4413, 4421, 4450, 4458, 4585, 4588,
         4640, 4647, 4656]
check("all 40 laws said to fail in STS(13) and PG(3,2) are proved for every squag (e.g. #313 " + show(313) +
      ": both sides equal x)", all(i in PROVED for i in FORTY))
for name, T in (("cyclic STS(13)", SYSTEMS[2][1]), ("PG(3,2)", SYSTEMS[3][1])):
    check(f"and all 40 hold at every assignment in {name}",
          all(np.array_equal(ev(LAWS[i - 1][0], T, grid(len(T), NV[i - 1])), ev(LAWS[i - 1][1], T, grid(len(T), NV[i - 1])))
              for i in FORTY))

print("\n4 -- the first law that tells squags apart has five operations")


def distributive(T):
    v = len(T)
    x, y, z = np.indices((v, v, v)).reshape(3, -1)
    return bool(np.array_equal(T[x, T[y, z]], T[T[x, y], T[x, z]]))


check("x*(y*z) = (x*y)*(x*z) (5 operations) holds in STS(3), AG(2,3), AG(3,3) and fails in the Fano plane, "
      "PG(3,2) and cyclic STS(13)",
      distributive(S3) and distributive(affine3(2)) and distributive(affine3(3))
      and not distributive(projective2(3)) and not distributive(projective2(4)) and not distributive(SYSTEMS[2][1]))

print(f"\n{'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' CHECK(S) FAILED'} ({time.time() - T0:.0f} s)")
sys.exit(1 if FAILS else 0)
