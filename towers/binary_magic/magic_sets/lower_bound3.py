"""
lower_bound3.py — the complete n = 5 search (Round 11, L3-full).
Cases forced by Lemmas 2-3: (C, V) in {(5, 14), (5, 15), (6, 15)}. Context sizes up to 9 (Lemma 4 with
dim R_c <= C - 2), then the exact Lemma-4 filter |c| <= V - C - 4 + dim R_c, then minimality, canonical
dedup, and the minimum magic Gram rank.
"""
import itertools, sys, time
from collections import Counter
from lower_bound2 import hypergraphs, build, canon, is_minimal
from ms_core import min_magic_rank

def dim_Rc(ctxs, V):
    C = len(ctxs)
    vec = [sum(1 << v for v in c) for c in ctxs]
    out = []
    for i, c in enumerate(ctxs):
        cm = vec[i]; sup = set()
        for T in range(1 << C):
            s = 0
            for j in range(C):
                if T >> j & 1: s ^= vec[j]
            if s & ~cm == 0: sup.add(s)
        out.append(len(sup).bit_length() - 1)              # |subspace| = 2^dim
    return out

n = 5
t0 = time.time(); tally = Counter(); seen = set(); hits = []; built = 0
for C, V in ((5, 14), (5, 15), (6, 15)):
    for highs, mg in hypergraphs(C, V, 9):
        built += 1
        if built % 200000 == 0:
            print(f"  ... {built:,} built, {len(seen):,} distinct survivors, {time.time() - t0:.0f}s", flush=True)
        _, ctxs = build(C, highs, mg)
        if len(set(map(frozenset, ctxs))) < C: tally["repeated context"] += 1; continue
        if not is_minimal(V, ctxs): tally["not minimal"] += 1; continue
        dR = dim_Rc(ctxs, V)
        if any(len(c) > V - C - 4 + k for c, k in zip(ctxs, dR)): tally["fails Lemma 4"] += 1; continue
        key = canon(C, ctxs, V)
        if key in seen: continue
        seen.add(key)
        q, d = min_magic_rank(V, ctxs, limit_dim=22, stop_at=2 * n - 2)
        if q is None: tally["no magic Pauli assignment"] += 1
        elif q == "too big": tally["unresolved"] += 1; hits.append(("?", C, V, ctxs))
        elif q >= 2 * n: tally["GENUINE 5-QUBIT"] += 1; hits.append((q // 2, C, V, ctxs))
        else: tally["fits on < 5 qubits"] += 1
    print(f"(C={C}, V={V}) done at {time.time() - t0:.0f}s: {dict(tally)}", flush=True)
print(f"\nL3-full: {built:,} hypergraphs built, {len(seen):,} distinct survivors tested; {dict(tally)}")
for h in hits: print("  hit:", h)
print("SCORE: L3-full", "HELD" if not hits else "LOST")
