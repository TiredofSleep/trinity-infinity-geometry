"""
order8_lens.py — Round 2 of PREREG.md: the code lens on fresh order-8 data.
Values 0..63 (6 bits), magic sum 252. A line is a "flat" if its 8 values form an affine 3-space.
"""
import os, itertools
import numpy as np
from functools import reduce

HERE = os.path.dirname(os.path.abspath(__file__))
O8 = os.path.join(HERE, "..", "order8")
def load(name):
    return [np.array(list(map(int, l.split()))).reshape(8, 8) for l in open(os.path.join(O8, name)) if l.strip()]
annealed, bitbal = load("squares8_annealed.txt"), load("squares8_bitbalanced.txt")
for M in annealed + bitbal:
    assert sorted(M.flatten()) == list(range(64))
    assert all(M.sum(0) == 252) and all(M.sum(1) == 252) and np.trace(M) == 252 and np.trace(M[:, ::-1]) == 252
print(f"loaded {len(annealed)} annealed and {len(bitbal)} bit-balanced order-8 magic squares (all verified magic)")

lines = lambda M: [M[i] for i in range(8)] + [M[:, j] for j in range(8)] + [np.diag(M), np.diag(M[:, ::-1])]
X = lambda L: reduce(lambda a, b: a ^ b, map(int, L), 0)
def is_flat(L):
    L = list(map(int, L)); U = {v ^ L[0] for v in L}
    return len(U) == 8 and all((a ^ b) in U for a in U for b in U)
res = {}

all_lines = [L for M in annealed + bitbal for L in lines(M)]
res["O1"] = all(X(L) & 1 == 0 for L in all_lines)
print(f"O1  bit 0 of the XOR is 0 on all {len(all_lines)} lines:", res["O1"])

ann = [L for M in annealed for L in lines(M)]
rate = sum(X(L) == 0 for L in ann) / len(ann)
res["O2"] = 0.026 <= rate <= 0.036
print(f"O2  annealed lines that XOR to 0: {rate:.2%} of {len(ann)} (predicted 3.1% ± 0.5%)")

bb = [L for M in bitbal for L in lines(M)]
res["O3"] = all(X(L) == 0 for L in bb)
fl = sum(is_flat(L) for L in bb) / len(bb)
res["O4"] = fl < 0.05
print(f"O3  bit-balanced lines that XOR to 0: {sum(X(L) == 0 for L in bb)}/{len(bb)}")
print(f"O4  bit-balanced lines that are flats: {fl:.2%} (predicted under 5%);"
      f" annealed lines that are flats: {sum(is_flat(L) for L in ann)}/{len(ann)}")

# O5: non-affine squares with parallel flat rows and columns, by shuffling an affine square
rng = np.random.default_rng(8)
def dotb(w, v): return bin(w & v).count("1") & 1
allowed = [(wr << 3) | wc for wr in range(1, 8) for wc in range(1, 8) if wr != wc]
while True:                                     # random basis of GF(2)^6 from the allowed forms
    W = list(rng.choice(allowed, 6, replace=False))
    if len({reduce(lambda a, b: a ^ b, [W[k] for k in range(6) if (s >> k) & 1], 0) for s in range(64)}) == 64: break
A = np.array([[sum(dotb(W[k], (r << 3) | c) << k for k in range(6)) for c in range(8)] for r in range(8)])
assert sorted(A.flatten()) == list(range(64)) and all(A.sum(0) == 252) and all(A.sum(1) == 252)
assert np.trace(A) == 252 and np.trace(A[:, ::-1]) == 252
def affine(M):
    S = [int(M[x >> 3][x & 7]) for x in range(64)]
    return all(len({S[x ^ a] ^ S[x] for x in range(64)}) == 1 for a in range(1, 64))
assert affine(A)
def parallel_flats(M):
    R = [M[i] for i in range(8)]; C = [M[:, j] for j in range(8)]
    dirs = lambda Ls: {frozenset(int(v) ^ int(L[0]) for v in L) for L in Ls}
    return all(map(is_flat, R + C)) and len(dirs(R)) == 1 and len(dirs(C)) == 1
assert parallel_flats(A)
T = 200_000
P = np.array([rng.permutation(8) for _ in range(T)]); S = np.array([rng.permutation(8) for _ in range(T)])
idx = np.arange(8)
d1 = A[P, S].sum(1); d2 = A[P, S[:, ::-1]].sum(1)
hits = np.flatnonzero((d1 == 252) & (d2 == 252))
found = []
for h in hits:
    M = A[P[h]][:, S[h]]
    assert all(M.sum(0) == 252) and all(M.sum(1) == 252) and np.trace(M) == 252 and np.trace(M[:, ::-1]) == 252
    if parallel_flats(M) and not affine(M): found.append(M)
res["O5"] = len(found) > 0
print(f"O5  {T:,} shuffles of an affine square: {len(hits)} keep both diagonals at 252;"
      f" non-affine with parallel flat rows and columns: {len(found)}")
if found:
    print("    example:"); [print("     ", " ".join(f"{v:2d}" for v in r)) for r in found[0]]
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert res["O1"], "a translation check failed"

# ---------- POST HOC (after scoring)
print("\n--- post hoc")
rc = [L for M in bitbal for L in lines(M)[:16]]; dg = [L for M in bitbal for L in lines(M)[16:]]
assert all(X(L) == 0 for L in rc)
print(f"O3 diagnosis: rows and columns {sum(X(L) == 0 for L in rc)}/{len(rc)} XOR to 0; diagonals {sum(X(L) == 0 for L in dg)}/{len(dg)}.")
print("    The samples are bit-balanced in rows and columns only (anneal8_binary.c), so the derivation covers")
print("    16 lines per square, not 18. The failure is in my registered scope, not in the code.")
# O2 null model: random 8-subsets of 0..63 conditioned on sum 252
keep = []
for _ in range(10):                                         # 10 chunks of 300k draws keeps memory small
    draws = np.argsort(rng.random((300_000, 64)), axis=1)[:, :8]
    keep += list(draws[draws.sum(1) == 252])
null = np.mean([X(L) == 0 for L in keep])
se = np.sqrt(null * (1 - null) / len(keep))
print(f"O2 diagnosis: random 8-subsets with sum 252 XOR to 0 at {null:.2%} ± {se:.2%} ({len(keep):,} draws);"
      f" annealed lines {rate:.2%}.")
print("    The sum pins the low bits' parities toward 0 (sum = 0 mod 4 ties bit 1 to the count of odd values),")
print("    so 1/32 was the wrong chance model.")
