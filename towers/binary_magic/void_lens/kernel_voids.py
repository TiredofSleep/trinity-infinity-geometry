#!/usr/bin/env python3
"""
kernel_voids.py -- Round 8c (void_lens/PREREG.md): does every kernel have a void certificate?
  (a) local:  a proper set S of rows or columns summing to a constant vector t*1  -> kernel s*1_S - t*1
  (b) global: the complement map (where c - x sits) factorises as (P(i), Q(j)) with void index >= 1
Run from binary_magic/:  python3 void_lens/kernel_voids.py      Prints ASCII only.
"""
import itertools, json, os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from void_lens_core import det_bareiss, rank_exact

HERE = os.path.dirname(os.path.abspath(__file__))

def local_certs(M):
    n = len(M); out = []
    for name, lines in (("cols", [list(c) for c in zip(*M)]), ("rows", [list(r) for r in M])):
        for k in range(2, n - 1):
            for S in itertools.combinations(range(n), k):
                v = [sum(lines[j][i] for j in S) for i in range(n)]
                if len(set(v)) == 1: out.append((name, S, v[0]))
    return out

def global_cert(M, c):
    n = len(M); pos = {M[i][j]: (i, j) for i in range(n) for j in range(n)}
    m = {(i, j): pos.get(c - M[i][j]) for i in range(n) for j in range(n)}
    if any(v is None for v in m.values()): return None
    P = [m[(i, 0)][0] for i in range(n)]; Q = [m[(0, j)][1] for j in range(n)]
    if not all(m[(i, j)] == (P[i], Q[j]) for i in range(n) for j in range(n)): return None
    fP = sum(i == x for i, x in enumerate(P)); fQ = sum(j == x for j, x in enumerate(Q))
    return abs((fP + fQ) / 2 - 1)

def canon(M):
    n = len(M); G = [list(r) for r in M]; out = []
    for _ in range(4):
        G = [list(r) for r in zip(*G[::-1])]
        out += [tuple(v for r in G for v in r), tuple(v for r in G for v in r[::-1])]
    return min(out)

res = {}
# ---- H1 on the 880
sq4 = [s["square"] for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
typ = Counter()
for M in sq4:
    pos = {M[i][j]: (i, j) for i in range(4) for j in range(4)}
    m = {(i, j): pos[15 - M[i][j]] for i in range(4) for j in range(4)}
    P = [m[(i, 0)][0] for i in range(4)]; Q = [m[(0, j)][1] for j in range(4)]
    fact = all(m[(i, j)] == (P[i], Q[j]) for i in range(4) for j in range(4))
    t = (sum(i == x for i, x in enumerate(P)), sum(j == x for j, x in enumerate(Q))) if fact else None
    typ[(t, bool(local_certs(M)), det_bareiss(M) == 0)] += 1
for k, v in sorted(typ.items(), key=str): print("  880:", "type", k[0], "local cert", k[1], "singular", k[2], "->", v)
forced = all(k[1] for k in typ if k[0] in ((4, 0), (0, 4)))
res["H1"] = forced and not any(k[1] for k in typ if k[0] == (0, 0))

# ---- H2, H3 on annealed 5x5
raw = [list(map(int, l.split())) for l in open(os.path.join(HERE, "squares5_annealed.txt"))]
uniq = {}
for r in raw:
    M = [r[5 * i:5 * i + 5] for i in range(5)]
    assert sorted(r) == list(range(1, 26))
    L = [sum(x) for x in M] + [sum(x) for x in zip(*M)] + [sum(M[i][i] for i in range(5)), sum(M[i][4 - i] for i in range(5))]
    assert set(L) == {65}
    uniq.setdefault(canon(M), M)
sing = [M for M in uniq.values() if det_bareiss(M) == 0]
print(f"\n  5x5: {len(raw)} annealed, {len(uniq)} distinct up to symmetry, {len(sing)} singular "
      f"({100 * len(sing) / len(uniq):.2f}%)")
unexplained = []; tvals = Counter(); kinds = Counter(); ranks = Counter()
for M in sing:
    lc = local_certs(M); g = global_cert(M, 26)
    ranks[rank_exact(M)] += 1
    for name, S, t in lc:
        if len(S) == 2: tvals[t] += 1
    kinds[("local" if lc else "") + ("+global" if g else "")] += 1
    if not lc and not (g and g >= 1): unexplained.append(M)
print("  certificate kinds among singular:", dict(kinds), " ranks:", dict(ranks))
print("  pair sums t of 2-line certificates:", dict(tvals))
nonsing_local = sum(1 for M in uniq.values() if det_bareiss(M) != 0 and local_certs(M))
print("  (consistency: nonsingular squares with a local certificate:", nonsing_local, ")")
if unexplained: print("  first unexplained singular square:", unexplained[0])
res["H2"] = not unexplained
res["H3"] = set(tvals) <= {26}
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
