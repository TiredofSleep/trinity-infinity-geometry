#!/usr/bin/env python3
"""verify_eight_specimens.py -- the eight 14-law closures of an archived paper all have finite type specimens.

    python verify_eight_specimens.py            # about 35 seconds; needs numpy
    python verify_eight_specimens.py --order6   # + the six-element search for C3 (about 2 more minutes)

A type specimen of a closure C is a finite magma whose ETP profile (the set of the ETP's 4694 laws it
satisfies) is exactly C.  Rebuilds the ETP catalog from its definition (no download), checks it against
known ETP numbers, then checks every [FORCED] line of EIGHT_SPECIMENS.md: the eight closures, their
specimens (orders 3, 3, 32, 32, 6, 5, 6, 5), the product lemma, and the smallest orders.
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




def canon(tables):
    """a fixed code for the isomorphism class of each table"""
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


# ------------------------------------------------------------------ 1. the eight closures

def nf(t, node):
    return ("v", t) if isinstance(t, int) else node(nf(t[0], node), nf(t[1], node))


RULES = {   # each rewrite below is an instance of the anchor law, so it is valid in every model of it
    40: lambda a, b: ("c",) if a == b else ("m", a, b),                       # u*u = c (one constant)
    43: lambda a, b: ("m",) + tuple(sorted((a, b), key=repr)),                # u*v = v*u
    4295: lambda a, b: ("P",) + tuple(sorted((a, b[2]), key=repr)) if b[0] == "m" else ("m", a, b),
    4303: lambda a, b: ("Q",) + tuple(sorted((b[1], b[2]), key=repr)) if b[0] == "m" else ("m", a, b),
}
SPEC = {40: [[0, 0, 1], [1, 0, 2], [1, 1, 0]],
        43: [[0, 0, 1], [0, 2, 0], [1, 0, 0]],
        4295: [[0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2],
               [0, 0, 0, 0, 0, 2], [0, 3, 3, 0, 3, 4]],
        4303: [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 4, 0, 1], [0, 0, 0, 0, 1], [0, 0, 0, 0, 1]]}
NAME = {40: "C1", 43: "C2", 4295: "C5", 4303: "C6"}
CL = {}
print("\n1 -- C1, C2, C5, C6: what the anchor proves, and a model that satisfies nothing more")
for a, rule in RULES.items():
    derived = {1} | {i for i, (s, t) in enumerate(LAWS, 1) if nf(s, rule) == nf(t, rule)}
    T = np.array(SPEC[a])
    ok = len(derived) == 14 and profile(T) == derived and a in derived
    CL[NAME[a]] = derived
    check(f"{NAME[a]} = closure of #{a} ({show(a)}): 14 laws follow from it, and a {len(T)}-element model "
          f"satisfies exactly these 14", ok)
CL["C7"], CL["C8"] = mirror(CL["C5"]), mirror(CL["C6"])
check("C7 = mirror of C5 contains #4610, and the transpose of the C5 model has profile exactly C7",
      4610 in CL["C7"] and profile(np.array(SPEC[4295]).T) == CL["C7"])
check("C8 = mirror of C6 contains #4637, and the transpose of the C6 model has profile exactly C8",
      4637 in CL["C8"] and profile(np.array(SPEC[4303]).T) == CL["C8"])

print("\n2 -- C3 (#1312) and C4 (#2241): a 32-element product")


def gf8_mul(a, b):                       # GF(8) = GF(2)[t]/(t^3 + t^2 + 1), elements as 3-bit integers
    r = 0
    for i in range(3):
        if (b >> i) & 1:
            r ^= a << i
    for d in (4, 3):
        if (r >> d) & 1:
            r ^= 0b1101 << (d - 3)
    return r


G8 = np.array([[gf8_mul(2, x) ^ gf8_mul(3, y) for y in range(8)] for x in range(8)])   # x*y = t x + (1+t) y
M4 = np.array([[0, 1, 3, 2], [1, 0, 3, 2], [0, 1, 3, 2], [1, 0, 3, 2]])
pg, pm = profile(G8), profile(M4)
C3 = pg & pm
check(f"the GF(8) affine mean satisfies #1312 and breaks #16 x = y*(y*x); it satisfies {len(pg)} laws",
      1312 in pg and 16 not in pg)
check(f"a 4-element model of #1312 ({len(pm)} laws); the two share exactly 14 laws", 1312 in pm and len(C3) == 14)


def product(A, B):
    i = np.arange(len(A) * len(B))
    a, b = i // len(B), i % len(B)
    return A[a[:, None], a[None, :]] * len(B) + B[b[:, None], b[None, :]]


PR = product(G8, M4)
holds_all = all(np.array_equal(ev(LAWS[i - 1][0], PR, grid(32, NV[i - 1])), ev(LAWS[i - 1][1], PR, grid(32, NV[i - 1])))
                for i in C3)


def lifted_failure(i):
    s, t = LAWS[i - 1]
    k = NV[i - 1]
    for F, lift in ((G8, 4), (M4, 1)):
        env = grid(len(F), k)
        bad = np.flatnonzero(ev(s, F, env) != ev(t, F, env))
        if len(bad):
            e = np.array([[env[v][bad[0]] * lift] for v in range(k)])
            return ev(s, PR, e)[0] != ev(t, PR, e)[0]
    return False


check("on the 32-element product, those 14 hold at every assignment, and every other law fails "
      "(a failing assignment of a factor, lifted)", holds_all and all(lifted_failure(i) for i in range(1, N + 1) if i not in C3))
CL["C3"], CL["C4"] = C3, mirror(C3)
PRT = PR.T.copy()
check("C4 = mirror of C3 contains #2241, and the transposed product satisfies #2241",
      2241 in CL["C4"] and np.array_equal(ev(LAWS[2240][0], PRT, grid(32, NV[2240])), ev(LAWS[2240][1], PRT, grid(32, NV[2240]))))
print("  (that #1312 implies all 13 non-trivial laws of C3 is the ETP's result -- its Lean proofs --"
      " not re-proved here)")
LISTED = {"C1": [40, 3688, 3692, 3700], "C2": [43], "C3": [1312], "C4": [2241], "C5": [4295, 4345, 4371],
       "C6": [4303, 4328, 4376], "C7": [4610, 4660, 4686], "C8": [4637, 4659, 4678]}
check("all eight closures have 14 laws and contain the anchors the archived paper lists for them",
      all(len(CL[c]) == 14 and set(v) <= CL[c] for c, v in LISTED.items()))
check("the mirror: C1, C2 on the edge; C3|C4, C5|C7, C6|C8 the two sides",
      mirror(CL["C1"]) == CL["C1"] and mirror(CL["C2"]) == CL["C2"] and mirror(CL["C3"]) == CL["C4"]
      and mirror(CL["C5"]) == CL["C7"] and mirror(CL["C6"]) == CL["C8"])

print("\n3 -- the product lemma: a law holds in A x B exactly when it holds in A and in B")
rng = np.random.default_rng(5)
pairs = [(rng.integers(0, 2, (2, 2)), rng.integers(0, 3, (3, 3))) for _ in range(4)]
check("4 random pairs (orders 2 and 3): profile(A x B) = profile(A) & profile(B)",
      all(profile(product(A, B)) == profile(A) & profile(B) for A, B in pairs))

# ------------------------------------------------------------------ 4. smallest orders

print("\n4 -- smallest specimens")
two = np.array(list(itertools.product(range(2), repeat=4))).reshape(-1, 2, 2)
P2 = [set(np.flatnonzero(r) + 1) for r in profiles(two)]
check("order 2: no table has profile C1 or C2 (all 16 tables) -- so 3 is the smallest order for both",
      all(p not in (CL["C1"], CL["C2"]) for p in P2))


def brute(law, n):
    tabs = np.array(list(itertools.product(range(n), repeat=n * n)), dtype=np.int64).reshape(-1, n, n)
    s, t = LAWS[law - 1]
    env = grid(n, NV[law - 1])
    TF = tabs.reshape(len(tabs), -1)
    a, b = evb(s, TF, n, env), evb(t, TF, n, env)
    return {tuple(T.ravel()) for T in tabs[np.all(a == b, axis=1)]}


def classes(tabs):
    if len(tabs) == 0:
        return tabs
    tabs = np.asarray(tabs)
    _, first = np.unique(canon(tabs), return_index=True)
    return tabs[first]


def models_4303(n):
    """Structure theorem: z*(y*x) does not depend on z, so a column indexed by an element of the image S
    is constant, value h(p); the law is then h(x*y) = h(y*x).  S = exact image; other columns free."""
    out = []
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            rest = [q for q in range(n) if q not in S]
            for h in itertools.product(S, repeat=r):
                hm = dict(zip(S, h))
                for cols in itertools.product(itertools.product(S, repeat=n), repeat=len(rest)):
                    T = np.zeros((n, n), dtype=np.int64)
                    for p in S:
                        T[:, p] = hm[p]
                    for q, c in zip(rest, cols):
                        T[:, q] = c
                    if set(T.ravel().tolist()) != set(S):
                        continue
                    H = np.vectorize(hm.get)(T)
                    if np.array_equal(H, H.T):
                        out.append(T)
    return np.array(out)


def set_partitions(el):
    if not el:
        yield []
        return
    for part in set_partitions(el[1:]):
        for i in range(len(part)):
            yield part[:i] + [[el[0]] + part[i]] + part[i + 1:]
        yield [[el[0]]] + part


def models_4295(n, nonconstant_only=False):
    """Structure theorem: T is a model iff there are a partition pi (equal columns), a set I of classes
    with a class Z in I, K : pi -> I onto with K = Z on I, a symmetric E : I x I -> Z, and free columns
    c_p : M -> K(p) for p not in I, with T[x, s] = E[K(cls x), cls s] for s in a class of I and
    T[x, s] = c_p(x) otherwise.  Right-nested products u*(v*w) equal E[K(cls u), K(cls w)]."""
    seen = set()
    out = []
    for part in set_partitions(list(range(n))):
        k = len(part)
        cls = {x: ci for ci, b in enumerate(part) for x in b}
        for r in range(1, k + 1):
            for I in itertools.combinations(range(k), r):
                rest = [p for p in range(k) if p not in I]
                for Z in I:
                    if nonconstant_only and (r < 2 or len(part[Z]) < 2):
                        continue
                    pr = [(a, b) for ai, a in enumerate(I) for b in I[ai:]]
                    for Kr in itertools.product(I, repeat=len(rest)):
                        if set(Kr) | {Z} != set(I):
                            continue
                        K = dict(zip(rest, Kr))
                        K.update({p: Z for p in I})
                        for Ev in itertools.product(part[Z], repeat=len(pr)):
                            if nonconstant_only and len(set(Ev)) < 2:
                                continue
                            Em = {}
                            for (a, b), v in zip(pr, Ev):
                                Em[a, b] = Em[b, a] = v
                            base = np.zeros((n, n), dtype=np.int64)
                            for s in range(n):
                                if cls[s] in I:
                                    for x in range(n):
                                        base[x, s] = Em[K[cls[x]], cls[s]]
                            for pick in itertools.product(*[list(itertools.product(part[K[p]], repeat=n)) for p in rest]):
                                T = base.copy()
                                for p, f in zip(rest, pick):
                                    for s in part[p]:
                                        T[:, s] = f
                                key_ = T.tobytes()
                                if key_ not in seen:
                                    seen.add(key_)
                                    out.append(T)
    return np.array(out)


def models_1312(n):
    """Backtracking; in a finite model every row is a permutation (x = y*(...) makes left multiplication onto)."""
    T = [[-1] * n for _ in range(n)]
    used = [set() for _ in range(n)]
    out, trail = [], []

    def put(y, x, v):
        if T[y][x] >= 0:
            return T[y][x] == v
        if v in used[y]:
            return False
        T[y][x] = v
        used[y].add(v)
        trail.append((y, x))
        return True

    def prop():
        ch = True
        while ch:
            ch = False
            for y in range(n):
                for x in range(n):
                    a = T[y][x]
                    b = T[a][x] if a >= 0 else -1
                    c = T[b][x] if b >= 0 else -1
                    if c < 0:
                        continue
                    if T[y][c] >= 0:
                        if T[y][c] != x:
                            return False
                    elif not put(y, c, x):
                        return False
                    else:
                        ch = True
        return True

    def rec():
        cell = next(((y, x) for y in range(n) for x in range(n) if T[y][x] < 0), None)
        if cell is None:
            out.append(np.array(T))
            return
        y, x = cell
        for v in range(n):
            if v in used[y]:
                continue
            mark = len(trail)
            if put(y, x, v) and prop():
                rec()
            while len(trail) > mark:
                yy, xx = trail.pop()
                used[yy].discard(T[yy][xx])
                T[yy][xx] = -1

    rec()
    return out


for n in (2, 3):
    check(f"the three searches are complete at order {n} (they agree with brute force over all {n ** (n * n)} tables)",
          {tuple(T.ravel()) for T in models_4303(n)} == brute(4303, n)
          and {tuple(T.ravel()) for T in models_4295(n)} == brute(4295, n)
          and {tuple(np.array(T).ravel()) for T in models_1312(n)} == brute(1312, n))

low6 = []
for n in (2, 3, 4):
    reps = classes(models_4303(n))
    sz = profiles(reps).sum(axis=1)
    low6.append(int(sz.min()))
check(f"C6 (#4303): the smallest profile of a model of order 2, 3, 4 is {low6[0]}, {low6[1]}, {low6[2]} "
      "-- all above 14, so 5 is the smallest order (and for C8, by the mirror)", low6 == [1556, 122, 15])

rn_laws = [i for i, (s, t) in enumerate(LAWS, 1)
           if all(not isinstance(u, int) and isinstance(u[0], int) and not isinstance(u[1], int)
                  and all(isinstance(z, int) for z in u[1]) for u in (s, t))]
check(f"there are {len(rn_laws)} laws u*(v*w) = u'*(v'*w'); a model whose right-nested products are all equal "
      "satisfies every one of them, so its profile has at least 113 laws", len(rn_laws) == 112)
full4 = classes(models_4295(4))
nc = {n: classes(models_4295(n, nonconstant_only=True)) for n in (2, 3, 4, 5)}
check("C5 (#4295): 165 models of order 4 up to renaming; 3 of them have right-nested products not all equal "
      "(none at orders 2 and 3)", len(full4) == 165 and len(nc[4]) == 3 and len(nc[3]) == 0 and len(nc[2]) == 0)
lo = {n: int(profiles(nc[n]).sum(axis=1).min()) for n in (4, 5)}
check(f"C5: at order 5, 145 such models; the smallest profiles are {lo[4]} (order 4) and {lo[5]} (order 5) "
      "-- above 14, so 6 is the smallest order (and for C7)", len(nc[5]) == 145 and lo == {4: 76, 5: 16})
all16 = True
counts = []
for n in (2, 3, 4, 5):
    ms = models_1312(n)
    counts.append(len(classes(np.array(ms))))
    all16 &= all(np.array_equal(ev(LAWS[15][0], T, grid(n, 2)), ev(LAWS[15][1], T, grid(n, 2))) for T in ms)
check(f"C3 (#1312): models of order 2-5 up to renaming: {counts}; every one satisfies #16 x = y*(y*x), "
      "which is not in C3 -- so a C3 specimen has at least 6 elements (and at most 32)",
      all16 and counts == [3, 8, 54, 855])

if "--order6" in sys.argv:
    print("\n5 -- (--order6) C3 at six elements")

    def breakers_1312(n, w):
        """models of #1312 with 0*(0*w) != w (a model breaking #16 can be renamed so); least-number
        heuristic: cells in order of max(row, column), values up to (largest label used) + 1"""
        T = [[-1] * n for _ in range(n)]
        used = [set() for _ in range(n)]
        order = sorted(((y, x) for y in range(n) for x in range(n)), key=lambda c: (max(c), c))
        out, trail = [], []

        def put(y, x, v):
            if T[y][x] >= 0:
                return T[y][x] == v
            if v in used[y]:
                return False
            T[y][x] = v
            used[y].add(v)
            trail.append((y, x))
            return True

        def prop():
            ch = True
            while ch:
                ch = False
                for y in range(n):
                    for x in range(n):
                        a = T[y][x]
                        b = T[a][x] if a >= 0 else -1
                        c = T[b][x] if b >= 0 else -1
                        if c < 0:
                            continue
                        if T[y][c] >= 0:
                            if T[y][c] != x:
                                return False
                        elif not put(y, c, x):
                            return False
                        else:
                            ch = True
                for y in range(n):
                    if len(used[y]) == n - 1:
                        x = next(x for x in range(n) if T[y][x] < 0)
                        (v,) = set(range(n)) - used[y]
                        if not put(y, x, v):
                            return False
                        ch = True
            a = T[0][w]
            return not (a >= 0 and T[0][a] == w)

        def rec():
            cell = next((c for c in order if T[c[0]][c[1]] < 0), None)
            if cell is None:
                out.append(np.array(T))
                return
            y, x = cell
            m = max([w, y, x] + [max(yy, xx, T[yy][xx]) for yy, xx in trail])
            for v in range(min(n - 1, m + 1) + 1):
                if v in used[y]:
                    continue
                mark = len(trail)
                if put(y, x, v) and prop():
                    rec()
                while len(trail) > mark:
                    yy, xx = trail.pop()
                    used[yy].discard(T[yy][xx])
                    T[yy][xx] = -1

        if prop():
            rec()
        return out

    found = breakers_1312(6, 1) + breakers_1312(6, 0)
    reps6 = classes(np.array(found))
    sizes6 = sorted(profiles(reps6).sum(axis=1).tolist())
    check(f"order 6: {len(found)} tables ({len(reps6)} up to renaming) satisfy #1312 and break #16; their profiles "
          f"have {sizes6[0]} to {sizes6[-1]} laws -- none is a specimen, so a C3 specimen has at least 7 elements",
          len(reps6) == 10 and sizes6 == [29, 29, 29, 38, 38, 42, 53, 53, 91, 130]
          and all(np.array_equal(ev(LAWS[1311][0], T, grid(6, 2)), ev(LAWS[1311][1], T, grid(6, 2))) for T in reps6))

print(f"\n{'ALL CHECKS PASS' if not FAILS else str(len(FAILS)) + ' CHECK(S) FAILED'} ({time.time() - T0:.0f} s)")
sys.exit(1 if FAILS else 0)
