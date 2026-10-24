#!/usr/bin/env python3
"""
void_fold_check.py -- a second, independent check of Round 7 / 7b (code_lens/PREREG.md) and of the atlas
statements made live on 2026-10-24 (version 5). Written in Claude Code; it shares no code with void_fold.py
or atlas_data.py: determinants by exact Bareiss elimination, carries solved from the diagonal's bit counts,
symmetries tested cell by cell.

Run from binary_magic/:  python code_lens/void_fold_check.py        Prints ASCII only.
"""
import json, os, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SQ = [[list(r) for r in s["square"]] for s in json.load(open(os.path.join(HERE, "..", "squares_4x4.json")))]
assert len(SQ) == 880


def det(A):
    """exact integer determinant (Bareiss fraction-free elimination)"""
    A = [r[:] for r in A]; n = len(A); sign, prev = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            p = next((i for i in range(k + 1, n) if A[i][k]), None)
            if p is None:
                return 0
            A[k], A[p] = A[p], A[k]; sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
        prev = A[k][k]
    return sign * A[n - 1][n - 1]


def cell(M, x):                      # cell address x = 4-bit (row bits, column bits)
    return M[x >> 2][x & 3]


def xor_symmetries(M):
    """{shift a: mask b} for every nonzero cell shift a with M[x ^ a] = M[x] ^ b for all cells x"""
    out = {}
    for a in range(1, 16):
        b = cell(M, 0) ^ cell(M, a)
        if all(cell(M, x ^ a) == cell(M, x) ^ b for x in range(16)):
            out[a] = b
    return out


def carries(M):
    """carry flags (plane 2->3, 1->2, 0->1) on the main diagonal: its bit-count deviations e_k = count_k - 2
    satisfy sum 2^k e_k = 0, and e = a(-2,1,0,0) + b(0,-2,1,0) + c(0,0,-2,1) has a unique solution"""
    e = [sum((M[i][i] >> k) & 1 for i in range(4)) - 2 for k in range(4)]
    a = -e[0] / 2; b = (e[1] - a) / -2; c = e[3]
    assert a == int(a) and b == int(b) and e[2] == b - 2 * c, e
    return "".join("1" if v else "0" for v in (c, b, a))


def region(cr):
    return "center" if cr in ("000", "111") else "petal" if cr.count("1") == 1 else "crossing"


MIRRORS, HALF_TURN = {0b0011: "left-right", 0b1100: "top-bottom"}, 0b1111
checks = []
def check(name, ok):
    checks.append((name, ok)); print(("  ok   " if ok else "  FAIL ") + name)

# 1. every mask is a reflection about 7.5 shifted by +-2^(q-1) per kept bit q; only b = 1111 is about 7.5 itself
ok = True
for b in range(1, 16):
    for n in range(16):
        centre = ((n ^ b) + n) / 2
        shift = sum((2 ** q if (n >> q) & 1 else 0) - 2 ** (q - 1) for q in range(4) if not (b >> q) & 1)
        ok &= centre == 7.5 + shift
    ok &= (b == 15) == all((n ^ b) + n == 15 for n in range(16))
print("1. n XOR b = c - n with c/2 = 7.5 +- 2^(q-1) for each kept bit q; only b = 1111 is about 7.5:")
check("all 15 masks, all 16 values", ok)

rows = []
for M in SQ:
    sy = xor_symmetries(M)
    comp = {a for a, b in sy.items() if b == 15}
    mirror_masks = {a: b for a, b in sy.items() if a in MIRRORS}
    cr = carries(M)
    rows.append(dict(D=det(M), comp=comp, mirror=mirror_masks, cr=cr, reg=region(cr),
                     affine=len(sy) == 15,
                     assoc=all(M[i][j] + M[3 - i][3 - j] == 15 for i in range(4) for j in range(4))))

print("2. regions and carries (Fitting 1931's split):")
check("528 / 64 / 64 / 64 / 56 / 56 / 0 / 48 by carry corner 000/001/010/100/011/110/101/111",
      Counter(r["cr"] for r in rows) == {"000": 528, "001": 64, "010": 64, "100": 64, "011": 56, "110": 56, "111": 48})
check("center 576, petals 192, crossings 112", Counter(r["reg"] for r in rows) == {"center": 576, "petal": 192, "crossing": 112})

print("3. singular exactly when some cell shift complements the square (all 15 shifts):")
sing = [r for r in rows if r["D"] == 0]
check("640 singular, 240 invertible", len(sing) == 640)
check("singular <=> a complement symmetry exists, on all 880", all((r["D"] == 0) == bool(r["comp"]) for r in rows))
mirror_c = [r for r in sing if r["comp"] & set(MIRRORS)]
half = [r for r in sing if not r["comp"] & set(MIRRORS) and HALF_TURN in r["comp"]]
swap = [r for r in sing if not r["comp"] & set(MIRRORS) and HALF_TURN not in r["comp"]]
check("split 304 by a mirror / 288 by another shift (row or column swaps) / 48 by the half-turn only",
      (len(mirror_c), len(swap), len(half)) == (304, 288, 48))
check("the 48 half-turn-only squares are exactly the 48 associative squares",
      len([r for r in rows if r["assoc"]]) == 48 and all(r["assoc"] for r in half)
      and all(not r["assoc"] for r in rows if r not in half))
sw_shifts = Counter(a for r in swap for a in r["comp"])
check("the 288 use no mirror and no half-turn: only shifts that swap rows and/or columns",
      all(a not in MIRRORS and a != HALF_TURN for a in sw_shifts))

print("4. the atlas's region rows (version 5):")
cen = [r for r in rows if r["reg"] == "center"]
check("every center square is singular", all(r["D"] == 0 for r in cen))
check("center: a complement mirror in 240, only a swap or the half-turn in 336",
      sum(bool(r["comp"] & set(MIRRORS)) for r in cen) == 240
      and sum(bool(r["comp"]) and not r["comp"] & set(MIRRORS) for r in cen) == 336)
check("all 432 affine squares lie in the center", sum(r["affine"] for r in rows) == 432
      and all(r["reg"] == "center" for r in rows if r["affine"]))
pet = [r for r in rows if r["reg"] == "petal"]
check("petals: invertible, no complement symmetry, every mirror fold flips 3 bits",
      all(r["D"] != 0 and not r["comp"] and r["mirror"] and all(bin(b).count("1") == 3 for b in r["mirror"].values())
          for r in pet))
cro = [r for r in rows if r["reg"] == "crossing"]
check("crossings: 64 with a complement mirror (singular), 48 with 3-bit mirror folds only (invertible)",
      sum(bool(r["comp"] & set(MIRRORS)) and r["D"] == 0 for r in cro) == 64
      and sum(not r["comp"] and r["D"] != 0 for r in cro) == 48)

print("5. mirror folds by weight:")
w = Counter(bin(b).count("1") for r in rows for b in r["mirror"].values())
check("over all mirror folds: weight 2 in 480, weight 3 in 624, weight 4 in 304", w == {2: 480, 3: 624, 4: 304})
check("every weight-2 mirror fold sits on a singular square",
      all(r["D"] == 0 for r in rows for b in r["mirror"].values() if bin(b).count("1") == 2))
check("on an invertible square every mirror fold flips 3 bits",
      all(bin(b).count("1") == 3 for r in rows if r["D"] for b in r["mirror"].values()))
check("288 singular squares also have a 3-bit mirror fold",
      sum(any(bin(b).count("1") == 3 for b in r["mirror"].values()) for r in sing) == 288)
inv_w = Counter(bin(b).count("1") for r in rows if r["D"]
                for a, b in xor_symmetries(SQ[rows.index(r)]).items())
check("invertible squares' XOR symmetries under all shifts: weight 3 x240, 2 x128, 1 x128 (V10 lost)",
      inv_w == {3: 240, 2: 128, 1: 128})

print("6. the literature's classes (Dudeney 1917; Trigg 1948; Staab et al., arXiv:1007.3239):")
def geo(M):                          # the 8 rotations and reflections of the square
    out, A = [], [r[:] for r in M]
    for _ in range(4):
        A = [list(r) for r in zip(*A[::-1])]; out += [A, [r[::-1] for r in A]]
    return out
def pair_pattern(M):                 # where the complementary pairs v, 15 - v sit, up to rotation and reflection
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in geo(M))
groups = {}
for M, r in zip(SQ, rows):
    groups.setdefault(pair_pattern(M), []).append(r)
check("Dudeney's 12 complement-pair groups, sizes 304, 96 x2, 56 x4, 48 x3, 8 x2",
      sorted(len(g) for g in groups.values()) == sorted([304, 96, 96, 56, 56, 56, 56, 48, 48, 48, 8, 8]))
NAME = {0: "-", 1: "K", 2: "L", 3: "J"}       # K: swap 0<->1, 2<->3; L: swap 0<->2, 1<->3; J: reverse
def side(a):
    return NAME[a >> 2], NAME[a & 3]
kinds = {}
for g in groups.values():
    sh = Counter(tuple(sorted(side(a) for a in r["comp"])) for r in g)
    kinds[len(g), tuple(sorted(sh))] = kinds.get((len(g), tuple(sorted(sh))), 0) + 1
want = {(304, ((("-", "J"),), (("J", "-"),))): 1,                       # VI: B_J, a mirror
        (96, ((("-", "K"),), (("K", "-"),))): 1, (96, ((("-", "L"),), (("L", "-"),))): 1,   # IV, V
        (48, ((("K", "K"),),)): 1, (48, ((("L", "L"),),)): 1, (48, ((("J", "J"),),)): 1,   # I, II, III
        (56, ((),)): 4, (8, ((),)): 2}                                   # VII-XII: none
check("each singular square has exactly one complement shift, and the groups are Staab et al.'s types:"
      " B_J (304), B_K and B_L (96 each), A_K, A_L, A_J (48 each); the 240 in VII-XII have none",
      kinds == want and all(len(r["comp"]) == (1 if r["D"] == 0 else 0) for r in rows))
check("each Dudeney group is wholly singular or wholly invertible: types I-VI (640) singular, VII-XII (240) not",
      all(len({r["D"] == 0 for r in g}) == 1 for g in groups.values())
      and sum(len(g) for g in groups.values() if g[0]["D"] == 0) == 640)
check("the 336 squares complemented by a swap or the half-turn (types I-V) are all affine;"
      " the 48 under the half-turn are the associative squares",
      all(r["affine"] for r in rows if r["comp"] and not r["comp"] & set(MIRRORS))
      and sum(1 for r in rows if r["comp"] and not r["comp"] & set(MIRRORS)) == 336)

bad = [n for n, ok in checks if not ok]
print(f"\n{len(checks) - len(bad)} of {len(checks)} checks pass")
sys.exit(1 if bad else 0)
