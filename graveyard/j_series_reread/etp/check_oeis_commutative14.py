"""OEIS draft 'A_commutative_profile14_at_order_n': number of commutative magmas on n labeled
elements whose ETP profile is exactly C2 (the closure of commutativity).  Exact a(4) via
isomorphism classes; a(5) bounded below (the draft's a(5) = 480 counts only quasigroups)."""
import os, sys, time, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

C2 = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}
OTHER = [i for i in range(1, E.NLAWS + 1) if i not in C2]
t0 = time.time()


def commutative_tables(n):
    cells = [(i, j) for i in range(n) for j in range(i, n)]
    vals = np.array(list(itertools.product(range(n), repeat=len(cells))), dtype=np.int64)
    T = np.zeros((len(vals), n, n), dtype=np.int64)
    for c, (i, j) in enumerate(cells):
        T[:, i, j] = vals[:, c]
        T[:, j, i] = vals[:, c]
    return T


def count_exact_c2(n, chunk=4000):
    T = commutative_tables(n)
    codes = np.concatenate([E.canon_codes(T[i:i + 50000]) for i in range(0, len(T), 50000)])
    uniq, first, counts = np.unique(codes, return_index=True, return_counts=True)
    reps = T[first]
    exact = np.zeros(len(reps), dtype=bool)
    min_sizes = []
    for s in range(0, len(reps), chunk):
        M = E.profiles_batch(reps[s:s + chunk], laws=OTHER)
        extra = M.sum(axis=1)
        exact[s:s + chunk] = extra == 0
        min_sizes.append(int(extra.min()))
    raw = int(counts[exact].sum())
    return len(T), len(reps), int(exact.sum()), raw


for n in (2, 3, 4):
    t1 = time.time()
    tot, ncls, nex, raw = count_exact_c2(n)
    print(f"order {n}: {tot} commutative tables, {ncls} up to isomorphism; profile exactly C2: "
          f"{nex} classes, {raw} labeled tables   ({time.time() - t1:.1f}s)")

# order 5: the draft's 480 counts symmetric Latin squares only.  Random commutative tables:
rng = np.random.default_rng(2026)
n = 5
B = 400
U = rng.integers(0, n, size=(B, n, n))
T = np.triu(U) + np.triu(U, 1).transpose(0, 2, 1)
M = E.profiles_batch(T, laws=OTHER)
exact = M.sum(axis=1) == 0
quasi = np.array([all(len(set(r)) == n for r in X) for X in T])
print(f"order 5: {exact.sum()} of {B} random commutative tables have profile exactly C2;"
      f" of those, quasigroups: {int((exact & quasi).sum())}")
ex = T[np.flatnonzero(exact & ~quasi)[0]]
print("   example (not a quasigroup):", ex.tolist(), " profile == C2:", E.profile(ex) == C2)
print(f"   => a(5) is about {exact.mean():.3f} * 5^15 = {exact.mean() * 5 ** 15:.3e}, not 480")
print("time %.1fs" % (time.time() - t0))
