"""
nimm0_coupling.py — Round 6b of PREREG.md: how much coupling between bit planes forces Nimm0?
Plane systems (P0..P3): each Pk a 4x4 0/1 matrix with eight 1s, all 10 magic line sums = 30
(sum_k 2^k * count_k(line) = 30), plus a coupling level: none / pairwise / triple-wise / full.
"""
import itertools
from collections import Counter
import numpy as np

LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
LM = [sum(1 << (4 * i + j) for i, j in L) for L in LINES]
masks = np.array([sum(1 << c for c in cs) for cs in itertools.combinations(range(16), 8)], dtype=np.int64)
pcnt = lambda a: np.array([bin(int(x)).count("1") for x in np.atleast_1d(a)])
POP = np.array([bin(x).count("1") for x in range(1 << 16)], dtype=np.int8)
C = np.stack([POP[masks & lm] for lm in LM], axis=1).astype(np.int64)        # 12870 x 10 line counts
by_counts = {}
for m, c in zip(masks.tolist(), map(tuple, C.tolist())): by_counts.setdefault(c, []).append(m)

def search(level, keep=None):
    """level 2 = pairwise, 3 = triple-wise, 4 = full. Returns (#systems, #carrying); appends systems to keep."""
    n = carry = 0
    i0 = np.flatnonzero((C % 2 == 0).all(1))
    for a in i0:
        P0, c0 = int(masks[a]), C[a]
        ok1 = ((c0 + 2 * C) % 4 == 2).all(1)
        if level >= 2: ok1 &= POP[masks & P0] == 4
        for b in np.flatnonzero(ok1):
            P1, c1 = int(masks[b]), C[b]
            ok2 = ((c0 + 2 * c1 + 4 * C) % 8 == 6).all(1)
            if level >= 2: ok2 &= (POP[masks & P0] == 4) & (POP[masks & P1] == 4)
            if level >= 3: ok2 &= POP[masks & (P0 & P1)] == 2
            for c in np.flatnonzero(ok2):
                P2, c2 = int(masks[c]), C[c]
                rem = 30 - c0 - 2 * c1 - 4 * c2
                if (rem % 8).any() or (rem < 0).any(): continue
                for P3 in by_counts.get(tuple((rem // 8).tolist()), []):
                    if level >= 2 and not all(POP[P3 & P] == 4 for P in (P0, P1, P2)): continue
                    if level >= 3 and not all(POP[P3 & x & y] == 2 for x, y in ((P0, P1), (P0, P2), (P1, P2))): continue
                    if level >= 3 and POP[P0 & P1 & P2] != 2: continue
                    if level >= 4 and POP[P0 & P1 & P2 & P3] != 1: continue
                    n += 1
                    if keep is not None: keep.append((P0, P1, P2, P3))
                    cs = [c0, c1, c2, rem // 8]
                    carry += any(v[l] != 2 for v in cs for l in range(8))
    return n, carry

res = {}
pairwise_systems = []
for level, name in ((2, "pairwise"), (3, "triple-wise"), (4, "full")):
    n, k = search(level, pairwise_systems if level == 2 else None)
    print(f"{name:12s}: {n:9,} plane systems with magic line sums, of which carry in a row or column: {k:,}")
    if level == 2: res["H8"] = k > 0
    if level == 3: res["H9"] = k > 0
    if level == 4: res["H10"] = n == 7040 and k == 0
# H11: every pairwise system folds plane-wise under a left-right or top-bottom mirror
LR = [4 * i + (3 - j) for i in range(4) for j in range(4)]; TB = [4 * (3 - i) + j for i in range(4) for j in range(4)]
bits = lambda P: [(P >> c) & 1 for c in range(16)]
def plane_mirror(P, perm):
    b = bits(P); flips = {b[perm[c]] ^ b[c] for c in range(16)}
    return len(flips) == 1                       # symmetric (all 0) or antisymmetric (all 1)
fold_ok = [any(all(plane_mirror(P, perm) for P in sysm) for perm in (LR, TB)) for sysm in pairwise_systems]
res["H11"] = all(fold_ok)
print(f"H11 pairwise systems with a plane-wise mirror fold: {sum(fold_ok):,} of {len(pairwise_systems):,}")
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert res["H10"] and res["H11"], "a translation check failed"
