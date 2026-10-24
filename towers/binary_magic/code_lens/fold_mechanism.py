"""
fold_mechanism.py — Round 3 of PREREG.md: does "every shuffle of 4 is affine" explain the fold?
Order 4: every plane is bi-affine (R1); folds are kernel conditions on the planes' Q matrices (R2);
the two diagonals form one Walsh pattern (R3). Order 8: restore bi-affinity by hand with bilinear
shears, then see whether the fold comes back (R4, R5).
"""
import itertools, json, os, random
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
squares = [s["square"] for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
pc = lambda x: bin(x).count("1")
dot = lambda a, b: pc(a & b) & 1

def biaffine(f, m):
    """f: dict (i,j)->bit on m-bit rows/cols. Returns (Q as list of row masks, ok) where Q[a] has bit b = Q_ab."""
    E = [1 << a for a in range(m)]
    c = f[0, 0]
    u = [f[e, 0] ^ c for e in E]; w = [f[0, e] ^ c for e in E]
    Q = [sum((f[E[a], E[b]] ^ f[E[a], 0] ^ f[0, E[b]] ^ c) << b for b in range(m)) for a in range(m)]
    ok = all(f[i, j] == (sum(((i >> a) & 1) & dot(Q[a], j) for a in range(m)) & 1)
             ^ dot(sum(u[a] << a for a in range(m)), i) ^ dot(sum(w[b] << b for b in range(m)), j) ^ c
             for i in range(2 ** m) for j in range(2 ** m))
    return Q, ok
def Qc(Q, c):  return sum(dot(Q[a], c) << a for a in range(len(Q)))             # Q·c
def QTr(Q, r): return sum((sum(((r >> a) & 1) & ((Q[a] >> b) & 1) for a in range(len(Q))) & 1) << b
                          for b in range(len(Q)))                               # Qᵀ·r
def folds(A, m):
    n = 2 ** m
    return {(r, c) for r in range(n) for c in range(n) if (r, c) != (0, 0)
            and len({A[i ^ r][j ^ c] ^ A[i][j] for i in range(n) for j in range(n)}) == 1}
res = {}

# ---------------------------------------------------------------- order 4
r1 = r2 = True
for M in squares:
    planes = [{(i, j): (M[i][j] >> k) & 1 for i in range(4) for j in range(4)} for k in range(4)]
    Qs = []
    for f in planes:
        Q, ok = biaffine(f, 2); r1 &= ok; Qs.append(Q)
    pred = {(r, c) for r in range(4) for c in range(4) if (r, c) != (0, 0)
            and all(Qc(Q, c) == 0 and QTr(Q, r) == 0 for Q in Qs)}
    r2 &= pred == folds(M, 2)
res["R1"], res["R2"] = r1, r2
print("R1  every plane of all 880 squares is bi-affine:", r1)
print("R2  fold by shift (r,c)  <=>  Q_k c = 0 and Q_k^T r = 0 for all planes (880 x 15):", r2)

chi = lambda r, c, i, j: (-1) ** (dot(r, i) ^ dot(c, j))
D4 = {(i, j): int(i == j or j == i ^ 3) for i in range(4) for j in range(4)}
ok4 = all(D4[i, j] == (1 + chi(3, 3, i, j)) // 2 for i in range(4) for j in range(4))
D8 = {(i, j): int(i == j or j == i ^ 7) for i in range(8) for j in range(8)}
ok8 = not any(all(D8[i, j] == (1 + s * chi(r, c, i, j)) // 2 for i in range(8) for j in range(8))
              for r in range(8) for c in range(8) for s in (1, -1))
res["R3"] = ok4 and ok8
print("R3  order 4: diagonals = (1 + chi11 x chi11)/2:", ok4, "| order 8: diagonals are no single Walsh pattern:", ok8)

# ---------------------------------------------------------------- order 8: bilinear shears
rnd = random.Random(23)
def matvec(Mrows, v): return sum(dot(Mrows[a], v) << a for a in range(3))
def inv3(Mrows):
    return len({matvec(Mrows, v) for v in range(8)}) == 8
def madd(A, B): return [a ^ b for a, b in zip(A, B)]
I3 = [1, 2, 4]
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
def affine8(A):
    S = [A[x >> 3][x & 7] for x in range(64)]
    return all(len({S[x ^ a] ^ S[x] for x in range(64)}) == 1 for a in range(1, 64))

# Exact list of shear structures: triples (M1, M2, M3) of 3x3 matrices with I + M(i) invertible for all i.
# (A first version sampled triples at random: 1 square in 400,000 draws, too few to score. Replaced
#  before scoring R4/R5; the predictions are unchanged.) Folds depend only on the shear, not on L or c,
#  so the sample takes at most one magic square per shear structure.
code = lambda R: R[0] | (R[1] << 3) | (R[2] << 6)
rows = lambda m: [(m >> (3 * a)) & 7 for a in range(3)]
INVI = [inv3(madd(I3, rows(m))) for m in range(512)]
valid = []
for m1 in range(512):
    if not INVI[m1]: continue
    for m2 in range(512):
        if not (INVI[m2] and INVI[m1 ^ m2]): continue
        for m3 in range(512):
            if INVI[m3] and INVI[m1 ^ m3] and INVI[m2 ^ m3] and INVI[m1 ^ m2 ^ m3] and (m1 or m2 or m3):
                valid.append((m1, m2, m3))
print(f"\norder 8: {len(valid):,} shear structures (nonzero triples with I + M(i) invertible for every i)")
found, tries = {}, 0
order_ = list(range(len(valid))); rnd.shuffle(order_)
for t in order_:
    if len(found) >= 600: break
    tries += 1
    Ms = [rows(m) for m in valid[t]]
    Mof = lambda i: [(Ms[0][a] if i & 1 else 0) ^ (Ms[1][a] if i & 2 else 0) ^ (Ms[2][a] if i & 4 else 0)
                     for a in range(3)]                     # M(i) = i0*M1 + i1*M2 + i2*M3 (row masks)
    orient = rnd.randrange(2)                       # 0: shear the columns by the row, 1: the transpose
    Phi = {}
    for i in range(8):
        for j in range(8):
            if orient == 0: Phi[i, j] = i | (matvec(madd(I3, Mof(i)), j) << 3)
            else:           Phi[i, j] = matvec(madd(I3, Mof(j)), i) | (j << 3)
    good = [l for l in range(1, 64)
            if all(sum(dot(l, Phi[i, j]) for j in range(8)) == 4 for i in range(8))
            and all(sum(dot(l, Phi[i, j]) for i in range(8)) == 4 for j in range(8))]
    if len(good) < 6: continue
    done = False
    for _ in range(40):
        L = rnd.sample(good, 6)
        if rank6(L) < 6: continue
        base = [[sum(dot(L[k], Phi[i, j]) << k for k in range(6)) for j in range(8)] for i in range(8)]
        for c in range(64):
            if sum(base[i][i] ^ c for i in range(8)) == 252 and sum(base[i][7 - i] ^ c for i in range(8)) == 252:
                A = [[v ^ c for v in row] for row in base]
                assert sorted(v for r in A for v in r) == list(range(64))
                assert all(sum(r) == 252 for r in A) and all(sum(col) == 252 for col in zip(*A))
                found[tuple(map(tuple, A))] = (valid[t], orient); done = True
                break
        if done: break

print(f"   {len(found)} bi-affine magic squares, one per shear structure, from {tries:,} structures tried")
sq8 = [list(map(list, k)) for k in found]
nonaff = [A for A in sq8 if not affine8(A)]
print(f"   non-affine: {len(nonaff)}")
stats = Counter()
crit_ok = True
for A in nonaff:
    F = folds(A, 3)
    planes = [{(i, j): (A[i][j] >> k) & 1 for i in range(8) for j in range(8)} for k in range(6)]
    Qs = []
    for f in planes:
        Q, ok = biaffine(f, 3); assert ok; Qs.append(Q)
    pred = {(r, c) for r in range(8) for c in range(8) if (r, c) != (0, 0)
            and all(Qc(Q, c) == 0 and QTr(Q, r) == 0 for Q in Qs)}
    crit_ok &= pred == F
    mirror = (0, 7) in F or (7, 0) in F
    stats["mirror fold"] += mirror; stats["any fold"] += bool(F); stats["no fold"] += not F
print("   the Q-kernel criterion predicts every order-8 fold exactly too:", crit_ok)
print("  ", dict(stats))
n = len(nonaff)
res["R4"] = n > 0 and stats["mirror fold"] < n / 2
res["R5"] = n > 0 and stats["no fold"] > n / 2
print(f"R4  share with a left-right or top-bottom mirror fold: {stats['mirror fold']}/{n} (predicted under half)")
print(f"R5  share with no fold at all: {stats['no fold']}/{n} (predicted over half)")
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert res["R1"] and res["R2"] and res["R3"] and crit_ok, "a translation check failed"
json.dump(sq8, open(os.path.join(HERE, "squares8_biaffine.json"), "w"))

# ---------- POST HOC (after scoring): does the magic condition pick out folded shears?
def shear_folds(trip, orient):
    """fold shifts of the shear itself, from the derivation: (r,c) folds iff M(r) = 0 and M_k c = 0 for all k
    (orientation 0); orientation 1 swaps the roles of r and c."""
    Ms = [rows(m) for m in trip]
    Mr = lambda r: (trip[0] if r & 1 else 0) ^ (trip[1] if r & 2 else 0) ^ (trip[2] if r & 4 else 0)
    K = {c for c in range(8) if all(matvec(M, c) == 0 for M in Ms)}
    F = {(r, c) for r in range(8) for c in K if Mr(r) == 0 and (r, c) != (0, 0)}
    return F if orient == 0 else {(c, r) for r, c in F}
for A, (trip, orient) in found.items():                     # the derivation matches the direct computation
    assert shear_folds(trip, orient) == folds([list(r) for r in A], 3)
base = Counter()
for trip in valid:
    F = shear_folds(trip, 0)
    base["mirror"] += (0, 7) in F or (7, 0) in F; base["any"] += bool(F)
N = len(valid)
print(f"\npost hoc: all {N:,} shear structures: mirror fold {base['mirror'] / N:.1%}, any fold {base['any'] / N:.1%},"
      f" no fold {1 - base['any'] / N:.1%}")
print(f"          the {n} that carry a magic square: mirror fold {stats['mirror fold'] / n:.1%},"
      f" any fold {stats['any fold'] / n:.1%}, no fold {stats['no fold'] / n:.1%}")
