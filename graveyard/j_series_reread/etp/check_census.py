"""Order-2 and order-3 census: the ETP profile of every magma table, recomputed."""
import os, sys, json, time, itertools
from collections import Counter
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

if len(sys.argv) < 2:
    sys.exit("usage: python check_census.py <archive>/etp_database   (<archive>: a checkout of the tag archive-2026-09-24; see ../README.md)")
ARCH = sys.argv[1]
FAMC = {1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}
t0 = time.time()


def all_tables(n):
    vals = np.array(list(itertools.product(range(n), repeat=n * n)), dtype=np.int64)
    return vals.reshape(-1, n, n)


out = {}
for n in (2, 3):
    tabs = all_tables(n)
    M = E.profiles_batch(tabs)
    sizes = M.sum(axis=1)
    profs = [frozenset(np.flatnonzero(row) + 1) for row in M]
    comm = np.array([np.array_equal(T, T.T) for T in tabs])
    latin = np.array([all(len(set(r)) == n for r in T) and all(len(set(c)) == n for c in T.T) for T in tabs])
    dist = Counter(sizes.tolist())
    distinct_sets = set(profs)
    mirror = lambda P: frozenset(E.MIRROR[i] for i in P)
    selfmirror_sets = sum(1 for P in distinct_sets if mirror(P) == P)
    # sanity: profile of the transpose is the mirror of the profile
    idx = {tuple(T.ravel()): k for k, T in enumerate(tabs)}
    transpose_ok = all(profs[idx[tuple(T.T.ravel())]] == mirror(profs[k]) for k, T in enumerate(tabs))
    print(f"order {n}: {len(tabs)} tables, {len(dist)} distinct profile sizes, {len(distinct_sets)} distinct profiles")
    print(f"   smallest size {min(dist)} ({dist[min(dist)]} tables), largest {max(dist)} ({dist[max(dist)]} tables)")
    print(f"   transpose -> mirror holds for every table: {transpose_ok};  self-mirror profiles: {selfmirror_sets}")
    cd = Counter(sizes[comm].tolist())
    print(f"   commutative tables: {comm.sum()}, min size {min(cd)}; with profile == C2: {sum(1 for k in np.flatnonzero(comm) if profs[k] == FAMC)}")
    ld = Counter(sizes[latin].tolist())
    print(f"   Latin squares: {latin.sum()}, sizes {dict(sorted(ld.items()))}")
    out[n] = dict(dist=dist, profs=profs, comm=comm, latin=latin, sizes=sizes, tabs=tabs)

# compare with the archived order-3 census
arch = json.load(open(os.path.join(ARCH, "data", "order3_profile_distribution.json"), encoding="utf-8"))
d3 = out[3]["dist"]
same_counts = {int(k): v for k, v in arch["profile_counts"].items()} == dict(d3)
print("archived order-3 profile_counts identical:", same_counts)
c3 = Counter(out[3]["sizes"][out[3]["comm"]].tolist())
same_comm = {int(k): v for k, v in arch["profile_counts_commutative"].items() if v} == dict(c3)
print("archived commutative counts identical:", same_comm)
q3 = Counter(out[3]["sizes"][out[3]["latin"]].tolist())
same_q = {int(k): v for k, v in arch["profile_counts_quasigroup"].items() if v} == dict(q3)
print("archived quasigroup counts identical:", same_q)
per = Counter()
for P in set(out[3]["profs"]):
    per[len(P)] += 1
same_fam = {int(k): v for k, v in arch["distinct_families_per_profile"].items()} == dict(per)
print("archived distinct-sets-per-size identical:", same_fam, " total distinct sets:", sum(per.values()))

# profile-14 sets at order 3: anchors (lowest non-trivial law) and number of variables in it
p14 = sorted({P for P in out[3]["profs"] if len(P) == 14}, key=lambda P: sorted(P))
anchors = Counter()
two_var = 0
for P in p14:
    a = min(i for i in P if i > 1)
    anchors[a] += 1
    two_var += E.NV[a - 1] >= 2
print(f"order 3: {len(p14)} distinct 14-law profiles; anchors with >=2 variables: {two_var}")
print("   anchor histogram:", dict(sorted(anchors.items())))
# which are closures of their own anchor?  (unknown without the ETP graph) -- skip
lawfree = [k for k, P in enumerate(out[3]["profs"]) if P == {1}]
print("order 3: tables satisfying no law but x = x:", len(lawfree), " example:", out[3]["tabs"][lawfree[0]].tolist())
lf2 = [k for k, P in enumerate(out[2]["profs"]) if P == {1}]
print("order 2: tables satisfying no law but x = x:", len(lf2))
# the archived smallest Family C realizer
T = np.array([[1, 2, 0], [2, 0, 0], [0, 0, 0]])
print("archived 'smallest Family C realizer' [[1,2,0],[2,0,0],[0,0,0]] has profile C2:", E.profile(T) == FAMC)
print("time %.1fs" % (time.time() - t0))
