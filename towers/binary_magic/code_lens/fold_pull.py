"""
fold_pull.py — Round 5 of PREREG.md: does the magic condition pull bi-affine 8x8 squares toward folding?
Fresh family: two-sided shears  Psi(i,j) = ((I + N(j)) i, (I + M(i)) j).
Baseline: structures that can carry a semi-magic square (every row and column balanced in every bit plane).
Comparison: those that also carry a magic square (diagonals 252) vs those that don't, same search budget.
"""
import random
from collections import Counter
import numpy as np
from scipy.stats import fisher_exact

pc = lambda x: bin(x).count("1")
dot = lambda a, b: pc(a & b) & 1
rows = lambda m: [(m >> (3 * a)) & 7 for a in range(3)]
MV = [[sum(dot(R, v) << a for a, R in enumerate(rows(m))) for v in range(8)] for m in range(512)]   # M·v
ID = 1 | (2 << 3) | (4 << 6)
INVI = [len(set(MV[m ^ ID])) == 8 for m in range(512)]                   # is I + M invertible?
valid = [(a, b, c) for a in range(512) if INVI[a] for b in range(512) if INVI[b] and INVI[a ^ b]
         for c in range(512) if INVI[c] and INVI[a ^ c] and INVI[b ^ c] and INVI[a ^ b ^ c] and (a or b or c)]
assert len(valid) == 109_823
mcode = lambda T, i: (T[0] if i & 1 else 0) ^ (T[1] if i & 2 else 0) ^ (T[2] if i & 4 else 0)     # code of M(i)

def two_sided(M, N):
    return [[MV[mcode(N, j) ^ ID][i] | (MV[mcode(M, i) ^ ID][j] << 3) for j in range(8)] for i in range(8)]
def one_sided(M, orient):
    if orient == 0: return [[i | (MV[mcode(M, i) ^ ID][j] << 3) for j in range(8)] for i in range(8)]
    return [[MV[mcode(M, j) ^ ID][i] | (j << 3) for j in range(8)] for i in range(8)]
def folds(V):
    return {(r, c) for r in range(8) for c in range(8) if (r, c) != (0, 0)
            and len({V[i ^ r][j ^ c] ^ V[i][j] for i in range(8) for j in range(8)}) == 1}
def biaffine_planes(V):
    for k in range(6):
        f = lambda i, j: (V[i][j] >> k) & 1
        for i in range(8):                       # affine along each row and each column: f(x^y^z) = f(x)^f(y)^f(z)
            for a, b, c in [(1, 2, 3), (1, 4, 5), (2, 4, 6), (1, 6, 7), (3, 4, 7), (2, 5, 7), (3, 5, 6)]:
                if f(i, 0) ^ f(i, a) ^ f(i, b) ^ f(i, c) or f(0, i) ^ f(a, i) ^ f(b, i) ^ f(c, i): return False
    return True
def rank6(vs):
    vs = list(vs); r = 0
    for bit in range(6):
        p = next((k for k in range(r, len(vs)) if vs[k] >> bit & 1), None)
        if p is None: continue
        vs[r], vs[p] = vs[p], vs[r]
        for k in range(len(vs)):
            if k != r and vs[k] >> bit & 1: vs[k] ^= vs[r]
        r += 1
    return r
DIAG = [(i, i) for i in range(8)] + [(i, 7 - i) for i in range(8)]
CS = np.arange(64)
def classify(V, rnd, budget=40):
    """returns (semi-magic capable, carries a magic square)"""
    good = [l for l in range(1, 64)
            if all(sum(dot(l, V[i][j]) for j in range(8)) == 4 for i in range(8))
            and all(sum(dot(l, V[i][j]) for i in range(8)) == 4 for j in range(8))]
    if rank6(good) < 6: return False, False
    for _ in range(budget):
        L = rnd.sample(good, 6)
        if rank6(L) < 6: continue
        d = np.array([sum(dot(L[k], V[i][j]) << k for k in range(6)) for i, j in DIAG])
        s1 = (d[:8, None] ^ CS[None, :]).sum(0); s2 = (d[8:, None] ^ CS[None, :]).sum(0)
        hit = np.flatnonzero((s1 == 252) & (s2 == 252))
        if len(hit):
            c = int(hit[0])
            A = [[sum(dot(L[k], V[i][j]) << k for k in range(6)) ^ c for j in range(8)] for i in range(8)]
            assert sorted(v for r in A for v in r) == list(range(64))
            assert all(sum(r) == 252 for r in A) and all(sum(col) == 252 for col in zip(*A))
            assert sum(A[i][i] for i in range(8)) == 252 and sum(A[i][7 - i] for i in range(8)) == 252
            assert folds(A) == folds(V)            # an output map and a constant never change the folds
            return True, True
    return True, False

def compare(structs, label, rnd):
    rec = []
    for V in structs:
        semi, magic = classify(V, rnd)
        F = folds(V)
        rec.append(dict(semi=semi, magic=magic, nofold=not F, mirror=(0, 7) in F or (7, 0) in F))
    S = [r for r in rec if r["semi"]]
    g1 = [r for r in S if r["magic"]]; g0 = [r for r in S if not r["magic"]]
    out = {}
    print(f"\n{label}: {len(rec)} structures, {len(S)} semi-magic capable, {len(g1)} carry a magic square")
    for key, want in (("nofold", "smaller"), ("mirror", "larger")):
        a, b = sum(r[key] for r in g1), sum(r[key] for r in g0)
        share1, share0 = a / max(len(g1), 1), b / max(len(g0), 1)
        p = fisher_exact([[a, len(g1) - a], [b, len(g0) - b]])[1] if g1 and g0 else 1.0
        direction = share1 < share0 if want == "smaller" else share1 > share0
        print(f"   {key:7s}: magic-carrying {a}/{len(g1)} = {share1:.1%}   vs  semi-magic only {b}/{len(g0)} = {share0:.1%}"
              f"   (Fisher p = {p:.2g}; predicted {want})")
        out[key] = dict(ok=direction and p < 0.01, informative=(a + b) > 0, p=p, s1=share1, s0=share0)
    allF = sum(r["nofold"] for r in rec) / len(rec); allM = sum(r["mirror"] for r in rec) / len(rec)
    print(f"   all structures: no fold {allF:.1%}, mirror fold {allM:.1%}")
    return out

rnd = random.Random(55)
# ---------------- the fresh family
two, draws, t1 = [], 0, True
while len(two) < 2500 and draws < 2_000_000:
    draws += 1
    M, N = rnd.choice(valid), rnd.choice(valid)
    V = two_sided(M, N)
    if len({v for r in V for v in r}) != 64: continue
    pred = {(r, c) for r in range(8) for c in range(8) if (r, c) != (0, 0)
            and mcode(M, r) == 0 and mcode(N, c) == 0
            and all(MV[n][r] == 0 for n in N) and all(MV[m][c] == 0 for m in M)}
    t1 &= biaffine_planes(V) and pred == folds(V)
    two.append(V)
dirs = lambda vals: frozenset(v ^ vals[0] for v in vals)
par = Counter((len({dirs(r) for r in V}) == 1, len({dirs([V[a][b] for a in range(8)]) for b in range(8)}) == 1) for V in two)
print(f"two-sided shears: {len(two)} bijections from {draws:,} draws; (rows parallel, cols parallel): {dict(par)}")
print("T1  bi-affine planes and the derived fold criterion, all structures:", t1)
res = {"T1": t1}
o = compare(two, "F1/F2  two-sided shears (fresh)", rnd)
res["F1"] = o["nofold"]["ok"]
res["F2"] = o["mirror"]["ok"] if o["mirror"]["informative"] else None

# ---------------- Round 3's family, re-analysed with the semi-magic baseline
one = [one_sided(rnd.choice(valid), rnd.randrange(2)) for _ in range(3000)]
o3 = compare(one, "F3  one-sided shears (Round 3's family, new baseline)", rnd)
res["F3"] = o3["nofold"]["ok"] and o3["mirror"]["ok"]

print("\nSCORE:", {k: ("HELD" if v else "UNINFORMATIVE" if v is None else "LOST") for k, v in res.items()})
assert res["T1"], "a translation check failed"

# ---------- POST HOC (after scoring): why mirror folds? A left-right mirror fold with mask b gives
# A(i, 7-i) = A(i, i) XOR b, so the second diagonal is the first one re-coloured: once one diagonal hits 252,
# the other usually does too. Test: P(second diagonal hits | first hits), mirror-folded vs not.
def conditional_hit(V, rnd, draws=150):
    good = [l for l in range(1, 64)
            if all(sum(dot(l, V[i][j]) for j in range(8)) == 4 for i in range(8))
            and all(sum(dot(l, V[i][j]) for i in range(8)) == 4 for j in range(8))]
    first = both = 0
    for _ in range(draws):
        L = rnd.sample(good, 6)
        if rank6(L) < 6: continue
        d = np.array([sum(dot(L[k], V[i][j]) << k for k in range(6)) for i, j in DIAG])
        s1 = (d[:8, None] ^ CS[None, :]).sum(0) == 252; s2 = (d[8:, None] ^ CS[None, :]).sum(0) == 252
        first += s1.sum(); both += (s1 & s2).sum()
    return first, both
groups = {"mirror fold": [], "no mirror fold": []}
for V in two:
    F = folds(V)
    key = "mirror fold" if ((0, 7) in F or (7, 0) in F) else "no mirror fold"
    if len(groups[key]) < 150 and rank6([l for l in range(1, 64)
            if all(sum(dot(l, V[i][j]) for j in range(8)) == 4 for i in range(8))
            and all(sum(dot(l, V[i][j]) for i in range(8)) == 4 for j in range(8))]) == 6:
        groups[key].append(V)
print("\n--- post hoc: P(second diagonal = 252 | first diagonal = 252), two-sided shears")
cond = {}
for key, Vs in groups.items():
    f = b = 0
    for V in Vs:
        x, y = conditional_hit(V, rnd); f += x; b += y
    cond[key] = b / f
    print(f"   {key:15s} ({len(Vs)} structures): {b}/{f} = {b / f:.1%}")
assert cond["mirror fold"] > 2 * cond["no mirror fold"]
print("   A mirror fold ties the two diagonals together, so a magic square costs one diagonal condition, not two.")
