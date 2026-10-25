#!/usr/bin/env python3
"""
digit_rank.py -- kernel_ledger/PREREG.md Round K9 (T3-T5): does the low base-5 digit layer's rank mod 5 predict
singularity? M = 5A + B + 1, B = low digits. Run from kernel_ledger/:  python3 digit_rank.py   ASCII only.
"""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from four_in_five_core import det_bareiss, canon, local_certs, global_index, kernels
from eccentric import eccentric, load

HERE = os.path.dirname(os.path.abspath(__file__))

def rank_mod(A, p):
    A = [[x % p for x in r] for r in A]; r = 0
    for c in range(len(A[0])):
        piv = next((i for i in range(r, len(A)) if A[i][c]), None)
        if piv is None: continue
        A[r], A[piv] = A[piv], A[r]; inv = pow(A[r][c], p - 2, p)
        A[r] = [x * inv % p for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                f = A[i][c]; A[i] = [(x - f * y) % p for x, y in zip(A[i], A[r])]
        r += 1
    return r

old_paths = [os.path.join(HERE, "..", "binary_magic", "void_lens", "squares5_annealed.txt")] + \
            [os.path.join(HERE, f) for f in ("squares5_fresh.txt", "squares5_fresh2.txt", "squares5_fresh3.txt")]
old = {canon(M) for p in old_paths for M in load(p)}
fresh = {}
for M in load(os.path.join(HERE, "squares5_fresh4.txt")):
    k = canon(M)
    if k not in old: fresh.setdefault(k, M)

by_rank = Counter(); sing_rank = Counter(); t4_ok = True; share = {"concentric": [], "eccentric": [], "weighted": []}
for M in fresh.values():
    B = [[(x - 1) % 5 for x in r] for r in M]; rb = rank_mod(B, 5); by_rank[rb] += 1
    if det_bareiss(M) != 0: continue
    sing_rank[rb] += 1
    v = kernels(M)[0][0]
    if len({x % 5 for x in v}) > 1 and rb > 3: t4_ok = False
    kind = "concentric" if (local_certs(M) or (global_index(M, 26) or 0) >= 1) else ("eccentric" if eccentric(M) else "weighted")
    share[kind].append(rb <= 3)

n = len(fresh); s = sum(sing_rank.values()); base = s / n
print(f"fresh: {n} distinct new squares, {s} singular (base rate {100 * base:.3f}%)")
for r in sorted(by_rank):
    print(f"  rank_F5(B) = {r}: {by_rank[r]} squares, {sing_rank[r]} singular "
          f"({100 * sing_rank[r] / by_rank[r]:.2f}%, {sing_rank[r] / by_rank[r] / base:.1f}x base)")
for k, v in share.items():
    if v: print(f"  {k}: {len(v)} singular, share with rank_F5(B) <= 3: {100 * sum(v) / len(v):.0f}%")
def v5(x):
    x = abs(x); k = 0
    while x % 5 == 0: x //= 5; k += 1
    return k
q_non = [(det_bareiss(M) // 325, rank_mod([[(x - 1) % 5 for x in r] for r in M], 5)) for M in fresh.values()]
q_non = [(q, r) for q, r in q_non if q]
L, T = 48 * 5 ** 3, 30000
est6 = sum(1 for q, _ in q_non if abs(q) <= T and q % L == 0) / (2 * T / L)
nw = len(share["weighted"])
print(f"T6: lattice estimate with L = {L}: {est6:.2f} vs {nw} weighted zeros ({est6 / max(nw, 1):.2f}x)")
mv = {r: sum(v5(q) for q, rr in q_non if rr == r) / max(1, sum(1 for _, rr in q_non if rr == r)) for r in (2, 3, 4)}
print("T7: mean 5-adic valuation of det/325 by rank_F5(B):", {r: round(m, 3) for r, m in mv.items()})
res = {}
res["T6"] = None if nw < 6 else est6 >= 0.7 * nw
res["T7"] = mv[2] > mv[3] > mv[4]
res["T3"] = None if by_rank[2] < 100 else (sing_rank[2] / by_rank[2]) >= 10 * base
res["T4"] = t4_ok
w, c = share["weighted"], share["concentric"]
res["T5"] = None if len(w) < 6 else (sum(w) / len(w) > sum(c) / max(len(c), 1))
print("\nSCORE:", {k: ("UNSCORED" if v is None else "HELD" if v else "LOST") for k, v in res.items()})
