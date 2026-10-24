"""
fold_needs.py — Round 6 of PREREG.md: what the 4x4 fold actually needs, and what forces Nimm0.
Enumerates every 4x4 semi-magic square on 0..15 (rows and columns sum to 30), then runs the relaxation
in which bit planes are independent 0/1 matrices tied together only by line sums.
"""
import itertools, json, os
from collections import Counter
from functools import reduce

HERE = os.path.dirname(os.path.abspath(__file__))
xor = lambda S: reduce(lambda a, b: a ^ b, S, 0)

# ---------------------------------------------------------------- enumerate semi-magic squares
quads = [q for q in itertools.combinations(range(16), 4) if sum(q) == 30]
def partitions(rem):
    if not rem: yield []; return
    m = min(rem)
    for q in quads:
        if q[0] == m and set(q) <= rem:
            for rest in partitions(rem - set(q)): yield [q] + rest
parts = list(partitions(set(range(16))))
base = []                                   # row order fixed (as listed), column order fixed by row 1 sorted
for P in parts:
    r1 = P[0]
    for p2 in itertools.permutations(P[1]):
        for p3 in itertools.permutations(P[2]):
            r4 = [30 - a - b - c for a, b, c in zip(r1, p2, p3)]
            if sorted(r4) == list(P[3]):
                base.append((tuple(r1), p2, p3, tuple(r4)))
total = len(base) * 24 * 24
print(f"semi-magic: {len(quads)} row-sets, {len(parts)} partitions, {len(base)} base squares -> {total:,} arrangements")
res = {"H1": total == 549_504}

def nimm0(B):                               # rows and columns all XOR to 0 (same as: no carries)
    return all(xor(r) == 0 for r in B) and all(xor(c) == 0 for c in zip(*B))
def mirror(A):
    lr = len({A[i][3 - j] ^ A[i][j] for i in range(4) for j in range(4)}) == 1
    tb = len({A[3 - i][j] ^ A[i][j] for i in range(4) for j in range(4)}) == 1
    return lr or tb
P4 = list(itertools.permutations(range(4)))
CHI = [[(-1) ** bin(r & i).count("1") for i in range(4)] for r in range(4)]
def Fhat(A, r, c):                          # Walsh coefficient of F = 15 - 2A
    return sum(CHI[r][i] * CHI[c][j] * (15 - 2 * A[i][j]) for i in range(4) for j in range(4))
spectral_ok = True
st = Counter()
magic_set = set()
for B in base:
    n0 = nimm0(B)
    st["base nimm0"] += n0
    for rp in P4:
        R = [B[k] for k in rp]
        for cp in P4:
            A = [[r[k] for k in cp] for r in R]
            d1 = sum(A[i][i] for i in range(4)); d2 = sum(A[i][3 - i] for i in range(4))
            m = mirror(A)
            spectral_ok &= (d1 == 30 and d2 == 30) == (Fhat(A, 3, 3) == 0 and Fhat(A, 1, 1) + Fhat(A, 2, 2) == 0)
            if d1 == 30 and d2 == 30:
                st["magic"] += 1; st["magic nimm0"] += n0; st["magic mirror"] += m
                magic_set.add(tuple(map(tuple, A)))
            if d1 + d2 == 60:
                st["diag60"] += 1
                st[("diag60", "nimm0" if n0 else "carry", "mirror" if m else "no mirror")] += 1
            st["all"] += 1; st["all nimm0"] += n0
print(f"H1  {total:,} arrangements (OEIS A271103: 68,688 x 8 = 549,504): {res['H1']}")
res["H2"] = st["magic"] == 7040 and st["magic nimm0"] == 7040 and st["magic mirror"] == 7040
known = json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))
def d4(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1])); out += [A, tuple(r[::-1] for r in A)]
    return out
known_all = {tuple(map(tuple, G)) for s in known for G in d4(tuple(map(tuple, s["square"])))}
res["H2"] &= magic_set == known_all
assert spectral_ok
print("    both diagonals = 30  <=>  F^(11,11) = 0 and F^(01,01) + F^(10,10) = 0  (F = 15 - 2A; all 549,504)")
print(f"H2  magic: {st['magic']} (all Nimm0: {st['magic nimm0']}, all mirror-folded: {st['magic mirror']});"
      f" identical to the 880 x 8 from binary_magic.py: {magic_set == known_all}")

a = st[("diag60", "nimm0", "mirror")]; b = st[("diag60", "nimm0", "no mirror")]
c = st[("diag60", "carry", "mirror")]; d = st[("diag60", "carry", "no mirror")]
print(f"\nsquares whose 8 diagonal cells sum to 60: {st['diag60']:,}")
print(f"   Nimm0:    {a:7,} mirror-folded, {b:7,} not")
print(f"   carries:  {c:7,} mirror-folded, {d:7,} not")
res["H3"] = b == 0
res["H4"] = d > 0
res["H5"] = st["all nimm0"] < st["all"] / 2
res["H6"] = (c + d) > 0
print(f"H3  Nimm0 + diagonals sum to 60  =>  mirror fold: {b == 0}  ({a:,} squares, no exceptions)" if b == 0 else
      f"H3  counterexamples: {b}")
print(f"H4  without Nimm0 it fails: {d:,} carrying squares with diagonals at 60 and no mirror fold")
print(f"H5  semi-magic squares violating Nimm0: {1 - st['all nimm0'] / st['all']:.1%}"
      f"  ({len(base) - st['base nimm0']} of {len(base)} base squares)")
print(f"H6  diagonals summing to 60 without Nimm0: {c + d:,} squares")

# ---------------------------------------------------------------- the relaxation (H7)
LINES = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
S = set()
for ones in itertools.combinations(range(16), 8):
    on = set(ones)
    S.add(tuple(sum((4 * i + j) in on for i, j in L) for L in LINES))
print(f"\nrelaxation: {len(S):,} possible line-count patterns for one plane with eight 1s")
def relax(nlines):
    """all (v0..v3) with sum_k 2^k v_k[line] = 30 on the first nlines lines (10 = magic, 8 = semi-magic)"""
    proj = {}
    for v in S: proj.setdefault(v[:nlines], []).append(v)
    keys = list(proj)
    even = [k for k in keys if all(x % 2 == 0 for x in k)]
    sols, carry = 0, Counter()
    keyset = set(keys)
    for v0 in even:
        for v1 in keys:
            if any((x + 2 * y - 30) % 4 for x, y in zip(v0, v1)): continue
            for v2 in keys:
                rem = [30 - x - 2 * y - 4 * z for x, y, z in zip(v0, v1, v2)]
                if any(r % 8 or not 0 <= r // 8 <= 4 for r in rem): continue
                v3 = tuple(r // 8 for r in rem)
                if v3 not in keyset: continue
                sols += 1
                if any(v[l] != 2 for v in (v0, v1, v2, v3) for l in range(8)):
                    carry["carry in a row or column"] += 1
    return sols, carry
s10, c10 = relax(10)
s8, c8 = relax(8)
print(f"   magic (10 lines):      {s10:,} count patterns, of which carry in a row or column: {c10['carry in a row or column']:,}")
print(f"   semi-magic (8 lines):  {s8:,} count patterns, of which carry in a row or column: {c8['carry in a row or column']:,}")
res["H7"] = c10["carry in a row or column"] > 0
print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})
assert res["H1"] and res["H2"], "a translation check failed"
