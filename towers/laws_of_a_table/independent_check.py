#!/usr/bin/env python3
"""independent_check.py -- the headline counts of this folder, recomputed by a second implementation.

    python independent_check.py      # about two minutes; needs numpy

The verify scripts here share one catalog engine. This file shares nothing with it: its catalog
enumeration is the one written for the archived J29's audit (graveyard/j_series_reread/check_j29.py),
by a different author, and its law-evaluation and mirror code are new. It recomputes:
  * the catalog size, 4694, and its split by number of operations (OEIS A376640: 2, 5, 39, 364, 4284);
  * the laws satisfied by x + y mod n and by -(x + y) mod n, for small n;
  * the laws satisfied by the Steiner quasigroups of the Fano plane and of AG(2, 3);
  * the number of laws that are their own mirror, 84.
Exits with status 1 on any failure. Output is ASCII only.
"""
import ctypes
import sys
import time
from itertools import product

import numpy as np

try:                                   # below-normal priority on Windows (the machine is shared)
    ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
except Exception:
    pass

T0 = time.time()
FAIL = []


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAIL.append(label)


# ---- the catalog: every law with at most four operations, up to renaming and swapping sides ----
def shapes(k):
    if k == 0:
        return ["v"]
    return [("o", l, r) for a in range(k) for l in shapes(a) for r in shapes(k - 1 - a)]


def leaves(s):
    return 1 if s == "v" else leaves(s[1]) + leaves(s[2])


def fill(s, it):
    return next(it) if s == "v" else ("o", fill(s[1], it), fill(s[2], it))


def rgs(m):
    def rec(pre, mx):
        if len(pre) == m:
            yield tuple(pre)
            return
        for v in range(mx + 2):
            yield from rec(pre + [v], max(mx, v))
    yield from rec([0], 0)


def relabel(t, mp):
    return mp.setdefault(t, len(mp)) if isinstance(t, int) else ("o", relabel(t[1], mp), relabel(t[2], mp))


def canon(l, r):
    best = None
    for a, b in ((l, r), (r, l)):
        mp = {}
        a2, b2 = relabel(a, mp), relabel(b, mp)
        key = repr((a2, b2))
        if best is None or key < best[0]:
            best = (key, (a2, b2))
    return best


def ops(t):
    return 0 if isinstance(t, int) else 1 + ops(t[1]) + ops(t[2])


eqs = {}
for k1 in range(5):
    for k2 in range(5 - k1):
        for s1 in shapes(k1):
            for s2 in shapes(k2):
                for lab in rgs(leaves(s1) + leaves(s2)):
                    it = iter(lab)
                    l, r = fill(s1, it), fill(s2, it)
                    key, e = canon(l, r)
                    eqs[key] = e
laws = [e for e in eqs.values() if e[0] != e[1]] + [(0, 0)]          # keep one trivial law, x = x
by_ops = [sum(1 for e in laws if ops(e[0]) + ops(e[1]) == k) for k in range(5)]
check(f"the catalog has {len(laws)} laws, split by operations as {by_ops} (OEIS A376640: 2, 5, 39, 364, 4284)",
      len(laws) == 4694 and by_ops == [2, 5, 39, 364, 4284])


def flat(t):
    return [t] if isinstance(t, int) else flat(t[1]) + flat(t[2])


NV = [max(flat(e[0]) + flat(e[1])) + 1 for e in laws]


def evaluate(t, tab, A):
    return A[:, t] if isinstance(t, int) else tab[evaluate(t[1], tab, A), evaluate(t[2], tab, A)]


def profile_size(tab):
    n = tab.shape[0]
    assign = {v: np.array(list(product(range(n), repeat=v)), dtype=np.int64) for v in set(NV)}
    return sum(1 for e, v in zip(laws, NV)
               if np.array_equal(evaluate(e[0], tab, assign[v]), evaluate(e[1], tab, assign[v])))


def table(f, n):
    return np.array([[f(x, y) % n for y in range(n)] for x in range(n)], dtype=np.int64)


# ---- Z/n under addition, and under negation ----
add = {n: profile_size(table(lambda x, y: x + y, n)) for n in range(1, 7)}
check(f"x + y mod n, n = 1..6: {[add[n] for n in range(1, 7)]} laws (expected 4694, 663, 60, 116, 32, 32)",
      [add[n] for n in range(1, 7)] == [4694, 663, 60, 116, 32, 32])
neg = {n: profile_size(table(lambda x, y: -(x + y), n)) for n in range(1, 8)}
check(f"-(x + y) mod n, n = 1..7: {[neg[n] for n in range(1, 8)]} laws (expected 4694, 663, 382, 294, 294, 297, 294)",
      [neg[n] for n in range(1, 8)] == [4694, 663, 382, 294, 294, 297, 294])


# ---- Steiner quasigroups: x*x = x, and x*y = the third point on the line through x and y ----
def steiner(n, lines):
    tab = np.zeros((n, n), dtype=np.int64)
    for x in range(n):
        tab[x, x] = x
    for a, b, c in lines:
        for x, y, z in ((a, b, c), (b, c, a), (c, a, b)):
            tab[x, y] = tab[y, x] = z
    return tab


# The Fano plane on the nonzero 3-bit strings 1..7, as in planes_and_mirrors: its lines are {a, b, a XOR b},
# so for a != b the Steiner product is a XOR b -- the octonions' rule e_a e_b = +-e_(a XOR b), signs forgotten.
# (Point p here is the string p + 1.)
fano = sorted({tuple(sorted((a - 1, b - 1, (a ^ b) - 1))) for a in range(1, 8) for b in range(1, 8) if a != b})
ag23 = []
pts = [(i, j) for i in range(3) for j in range(3)]
for p in range(9):
    for q in range(p + 1, 9):
        r = pts.index(tuple((-pts[p][k] - pts[q][k]) % 3 for k in range(2)))
        line = tuple(sorted((p, q, r)))
        if line not in ag23:
            ag23.append(line)
fano_tab, ag_tab = steiner(7, fano), steiner(9, ag23)
ok = all(len(set(fano_tab[x])) == 7 for x in range(7)) and len(fano) == 7 and len(ag23) == 12
ok &= all(fano_tab[a - 1, b - 1] == (a ^ b) - 1 for a in range(1, 8) for b in range(1, 8) if a != b)
ok &= all(len(set(ag_tab[x])) == 9 for x in range(9))
pf, pa = profile_size(fano_tab), profile_size(ag_tab)
check(f"the Fano plane's Steiner quasigroup satisfies {pf} laws and AG(2,3)'s {pa} "
      "(expected 382 each, the same as -(x + y) mod 3)", ok and pf == 382 and pa == 382)


# ---- the mirror: reverse every product, and compare canonical forms ----
def mirror(t):
    return t if isinstance(t, int) else ("o", mirror(t[2]), mirror(t[1]))


keys = {canon(e[0], e[1])[0] for e in laws}
selfm = sum(1 for e in laws if canon(mirror(e[0]), mirror(e[1]))[0] == canon(e[0], e[1])[0])
closed = all(canon(mirror(e[0]), mirror(e[1]))[0] in keys for e in laws)
check(f"{selfm} laws are their own mirror, and the other {len(laws) - selfm} form {(len(laws) - selfm) // 2} pairs "
      "(expected 84 and 2305)", closed and selfm == 84 and (len(laws) - selfm) == 2 * 2305)

print(f"elapsed {time.time() - T0:.1f} s")
if FAIL:
    print(f"{len(FAIL)} check(s) FAILED")
    sys.exit(1)
print("all checks passed")
