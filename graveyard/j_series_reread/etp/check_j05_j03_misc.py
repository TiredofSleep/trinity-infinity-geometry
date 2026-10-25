"""Remaining checkable claims of J05 / J03 / the database."""
import os, sys, time, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

C1 = {1, 40, 3659, 3662, 3665, 3677, 3684, 3688, 3692, 3700, 4270, 4341, 4590, 4622}
C2 = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}
t0 = time.time()

# ---- symmetric Latin squares of order 5 (commutative quasigroups)
def sym_latin(n):
    out = []
    L = -np.ones((n, n), dtype=np.int64)
    cells = [(i, j) for i in range(n) for j in range(i, n)]
    def rec(k):
        if k == len(cells):
            out.append(L.copy())
            return
        i, j = cells[k]
        for v in range(n):
            if v in L[i] or v in L[:, j] or v in L[j] or v in L[:, i]:
                continue
            L[i, j] = L[j, i] = v
            rec(k + 1)
            L[i, j] = L[j, i] = -1
    rec(0)
    return np.array(out)

for n in (3, 4, 5):
    S = sym_latin(n)
    M = E.profiles_batch(S)
    sizes = M.sum(axis=1)
    print(f"symmetric Latin squares of order {n}: {len(S)}; profile sizes {dict(sorted(Counter(sizes.tolist()).items()))}")
    if n == 5:
        p15 = [set(np.flatnonzero(r) + 1) for r in M if r.sum() == 15]
        extras = Counter(frozenset(p - C2) for p in p15)
        print("   profile-15 extras over C2:", {tuple(sorted(k)): v for k, v in extras.items()},
              [E.show(i) for k in extras for i in k])
        exact = sum(1 for r in M if set(np.flatnonzero(r) + 1) == C2)
        print("   exactly C2:", exact)

# ---- J03 section 6.3: order-3 satisfiers of the anchors, and their smallest profiles
tabs = np.array(list(itertools.product(range(3), repeat=9)), dtype=np.int64).reshape(-1, 3, 3)
TF = tabs.reshape(-1, 9)
for a, claim in ((1312, (28, 79)), (2241, (28, 79)), (4295, (None, None)), (4303, (45, 122)), (4610, (45, 122)), (4637, (45, 122))):
    ok = E.holds_batch(a, TF, 3)
    sat = tabs[ok]
    prof = [len(E.profile(T)) for T in sat]
    print(f"#{a}: {len(sat)} order-3 tables satisfy it; smallest profile {min(prof)}   (J03: {claim})")
T = np.array([[0, 1, 2], [0, 2, 1], [2, 1, 0]])
print("J03's C3 'minimum example' [[0,1,2],[0,2,1],[2,1,0]]: satisfies 1312:", E.holds(1312, T), " profile", len(E.profile(T)))

# ---- Lo Shu square mod 3 under the dihedral group (J03 section 3 / J29)
lo = np.array([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
orbit = set()
for k in range(4):
    R = np.rot90(lo, k)
    for X in (R, R.T):
        orbit.add(tuple((X % 3).ravel()))
for o in sorted(orbit):
    T = np.array(o).reshape(3, 3)
    print("Lo Shu mod 3 table", T.tolist(), "profile", len(E.profile(T)), "commutative", np.array_equal(T, T.T))

# ---- J03 verify check 5: random constant-diagonal magmas of order 5 realize C1
rng = np.random.default_rng(42)
hits = 0
for _ in range(30):
    T = rng.integers(0, 5, size=(5, 5))
    np.fill_diagonal(T, 0)
    hits += E.profile(T) == C1
print("random order-5 tables with constant diagonal whose profile is exactly C1:", hits, "of 30")

# ---- J61: random commutative magmas of order 10 realize C2
rng = np.random.default_rng(1)
cnt = 0
for _ in range(10):
    U = rng.integers(0, 10, size=(10, 10))
    T = np.triu(U) + np.triu(U, 1).T
    cnt += E.profile_big(T) == C2
print("random commutative tables of order 10 with profile exactly C2:", cnt, "of 10")

# ---- J05 3.3: is the Z/n profile (32 balanced laws) inside the negation-magma profile (294)?
Z5 = E.profile(np.add.outer(np.arange(5), np.arange(5)) % 5)
N5 = E.profile((-np.add.outer(np.arange(5), np.arange(5))) % 5)
print("Z/5 profile inside -(x+y) mod 5 profile:", Z5 <= N5, "; common laws:", len(Z5 & N5), "; associativity in 294-set:", 4512 in N5)
print("time %.1fs" % (time.time() - t0))
