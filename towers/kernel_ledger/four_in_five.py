#!/usr/bin/env python3
"""
four_in_five.py -- kernel_ledger/PREREG.md Round K6 ("4 seen as 5"): do singular magic squares collapse to
fewer lines, with two lines entering merged (repeated kernel entry) or one dropping out (zero entry)?
Run from kernel_ledger/:  python3 four_in_five.py        Prints ASCII only. Exact arithmetic for kernels.
"""
import itertools, json, math, os, random, sys
from fractions import Fraction
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
rng = random.Random(4545)
res = {}

def det_bareiss(A):
    A = [list(r) for r in A]; n = len(A); sign = 1; prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((r for r in range(k + 1, n) if A[r][k]), None)
            if p is None: return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]

def primitive(v):
    den = 1
    for x in v: den = den * x.denominator // math.gcd(den, x.denominator)
    w = [int(x * den) for x in v]; g = 0
    for x in w: g = math.gcd(g, x)
    return [x // g for x in w]

def kernels(M):
    A = sp.Matrix(M)
    r = [primitive([Fraction(int(x.p), int(x.q)) for x in k]) for k in A.nullspace()]
    l = [primitive([Fraction(int(x.p), int(x.q)) for x in k]) for k in A.T.nullspace()]
    return r, l

def merge_or_drop(v, signed=False):
    if any(x == 0 for x in v): return "drop"
    vals = [abs(x) for x in v] if signed else v
    return "merge" if len(set(vals)) < len(vals) else None

def canon(M):
    n = len(M); G = [list(r) for r in M]; out = []
    for _ in range(4):
        G = [list(r) for r in zip(*G[::-1])]
        out += [tuple(v for r in G for v in r), tuple(v for r in G for v in r[::-1])]
    return min(out)

def local_certs(M):
    n = len(M); out = []
    for lines in ([list(c) for c in zip(*M)], [list(r) for r in M]):
        for k in range(2, n - 1):
            for S in itertools.combinations(range(n), k):
                v = [sum(lines[j][i] for j in S) for i in range(n)]
                if len(set(v)) == 1: out.append(S)
    return out

def global_index(M, c):
    n = len(M); pos = {M[i][j]: (i, j) for i in range(n) for j in range(n)}
    mp = {(i, j): pos.get(c - M[i][j]) for i in range(n) for j in range(n)}
    if any(v is None for v in mp.values()): return None
    P = [mp[(i, 0)][0] for i in range(n)]; Q = [mp[(0, j)][1] for j in range(n)]
    if not all(mp[(i, j)] == (P[i], Q[j]) for i in range(n) for j in range(n)): return None
    return abs((sum(i == x for i, x in enumerate(P)) + sum(j == x for j, x in enumerate(Q))) / 2 - 1)

def chance(v, trials=20000):
    """P(a random zero-sum integer vector with entries in [-K, K] has a repeat or a zero), K = max|v_i|."""
    n = len(v); K = max(abs(x) for x in v); hit = got = 0
    while got < trials:
        w = [rng.randint(-K, K) for _ in range(n - 1)]; last = -sum(w)
        if abs(last) > K: continue
        w.append(last)
        if not any(w): continue
        got += 1
        hit += merge_or_drop(w) is not None
    return hit / trials

# ---------------- M0: order 4
sq4 = [s["square"] for s in json.load(open(os.path.join(HERE, "..", "binary_magic", "squares_4x4.json")))]
m0 = True; n_sing4 = 0
for M in sq4:
    if det_bareiss(M) != 0: continue
    n_sing4 += 1
    r, l = kernels(M)
    if not any(merge_or_drop(v, signed=True) for v in r + l): m0 = False
print(f"M0 order 4: {n_sing4} singular squares; all have a kernel vector with |v_a| = |v_b| or a zero: {m0}")
res["M0"] = m0

# ---------------- M1-M3: fresh order-5 sample
seen = set()
for l in open(os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt")):
    r = list(map(int, l.split())); seen.add(canon([r[5 * i:5 * i + 5] for i in range(5)]))
fresh = {}
for l in open(os.path.join(HERE, "squares5_fresh.txt")):
    r = list(map(int, l.split())); M = [r[5 * i:5 * i + 5] for i in range(5)]
    assert sorted(r) == list(range(1, 26))
    L = [sum(x) for x in M] + [sum(x) for x in zip(*M)] + [sum(M[i][i] for i in range(5)), sum(M[i][4 - i] for i in range(5))]
    assert set(L) == {65}
    key = canon(M)
    if key not in seen: fresh.setdefault(key, M)
sing = [M for M in fresh.values() if det_bareiss(M) == 0]
print(f"\nfresh order-5 sample: {len(fresh)} distinct new squares, {len(sing)} singular")
rows = []; base = []
for M in sing:
    r, l = kernels(M)
    kind_r = [merge_or_drop(v) for v in r]; kind_l = [merge_or_drop(v) for v in l]
    has = any(kind_r) or any(kind_l)
    acc = not local_certs(M) and not ((global_index(M, 26) or 0) >= 1)
    pr = 1 - (1 - chance(r[0])) * (1 - chance(l[0])) if len(r) == 1 and len(l) == 1 else 1.0
    base.append(pr)
    rows.append((has, acc, r, l, kind_r, kind_l, pr))
    print(f"  {'accidental' if acc else 'forced    '}  right {r[0] if len(r) == 1 else r}  left {l[0] if len(l) == 1 else l}"
          f"  -> {'/'.join(k for k in kind_r + kind_l if k) or 'NONE'}   chance {pr:.3f}")
obs = sum(h for h, *_ in rows) / max(len(rows), 1); exp_rate = sum(base) / max(len(base), 1)
acc_rows = [x for x in rows if x[1]]
print(f"\nobserved merge/drop rate {obs:.2f}; chance baseline {exp_rate:.3f}; ratio {obs / max(exp_rate, 1e-9):.1f}x")
print(f"accidental: {len(acc_rows)}, with merge/drop: {sum(x[0] for x in acc_rows)}")
res["M1"] = None if len(rows) < 10 else all(h for h, *_ in rows)
res["M2"] = None if len(rows) < 10 else obs >= 3 * exp_rate
res["M3"] = None if len(acc_rows) < 3 else all(x[0] for x in acc_rows)
print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})
