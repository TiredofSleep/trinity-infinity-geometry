"""
order8_families.py: which 8x8 squares fold? Three families, tested.

1. Affine fully binary squares (12,631,127,040 up to symmetry): all 63 XOR symmetries, by construction.
2. Fitting's 1931 construction (Jahresbericht DMV 40, Part 2, Satz II and Fig. 22-25): every quadrant
   holds the same fully binary 4x4 square (the 1s, 2s, 4s and 8s components), and the 16s and 32s
   components are built from halves, one half the inverse of the other. Fitting counts
   11 * 1296^2 * 6! * 2^6 / 8 = 106,420,469,760 such squares up to rotation and reflection.
   Claim tested: every one is fully binary and has an XOR symmetry (a half-shift), and almost none is
   affine.
3. Annealed fully binary squares (fullbinary8_samples.txt, from anneal8_fullbinary.js): every bit plane
   balanced on every line, the strongest order-8 analog of the 4x4 law. Claim tested: full balance does
   NOT force an XOR symmetry at order 8. The file holds 17 squares: the first came from an earlier
   version of the sampler (seed 7, a slower random generator), and the other 16 from
   `node anneal8_fullbinary.js 2 SEED` for SEED = 101, 202, ..., 808. The checks below re-verify every
   square, so where a square came from does not matter to the result.
Usage: python order8_families.py squares_4x4.json fullbinary8_samples.txt
"""
import itertools, json, random, sys
from collections import Counter

FAILS = []
def check(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'} {name}")
    if not cond:
        FAILS.append(name)

LINES = [[(i, j) for j in range(8)] for i in range(8)] + [[(i, j) for i in range(8)] for j in range(8)] + \
        [[(i, i) for i in range(8)], [(i, 7 - i) for i in range(8)]]
def fully_binary(A):
    return all(sum((A[i][j] >> k) & 1 for i, j in L) == 4 for L in LINES for k in range(6))
def magic(A):
    return sorted(v for r in A for v in r) == list(range(64)) and all(sum(A[i][j] for i, j in L) == 252 for L in LINES)
def xor_syms(A):
    S = [A[x >> 3][x & 7] for x in range(64)]
    return [(a, S[0] ^ S[a]) for a in range(1, 64) if all(S[x ^ a] == S[x] ^ S[0] ^ S[a] for x in range(64))]
MIRRORS = (0b000111, 0b111000)                      # left-right (j -> 7 - j) and top-bottom

# ---- 2. Fitting's construction
sq4 = [tuple(map(tuple, s["square"])) for s in json.load(open(sys.argv[1]))]
def orientations(A):
    out, B = [], A
    for _ in range(4):
        B = tuple(zip(*B[::-1])); out += [B, tuple(zip(*B))]
    return out
def fb4(A):
    L4 = [[(i, j) for j in range(4)] for i in range(4)] + [[(i, j) for i in range(4)] for j in range(4)] + \
         [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]
    return all(sum((A[i][j] >> k) & 1 for i, j in L) == 2 for L in L4 for k in range(4))
base = [B for A in sq4 if fb4(A) for B in orientations(A)]
check(f"the base: the 528 fully binary 4x4 squares in all 8 orientations ({len(base)})", len(base) == 528 * 8)
cols2 = [c for c in itertools.product((0, 1), repeat=4) if sum(c) == 2]          # 6 balanced columns
check("1296 = 6^4 ways to put two 1s in each of four columns", len(cols2) ** 4 == 1296)
def fitting_square(rng):
    B = rng.choice(base)
    f = [rng.choice(cols2) for _ in range(4)]          # f[c][r]: two 1s in each column of the quadrant
    g = [rng.choice(cols2) for _ in range(4)]          # g[r][c]: two 1s in each row of the quadrant
    A = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            r, c = i % 4, j % 4
            b16 = f[c][r] ^ (j >= 4)                   # right half the inverse of the left; top = bottom
            b32 = g[r][c] ^ (i >= 4)                   # bottom half the inverse of the top; left = right
            A[i][j] = B[r][c] + 16 * b16 + 32 * b32
    return A
rng = random.Random(1931)
fam = [fitting_square(rng) for _ in range(2000)]
check("2,000 random squares from Fitting's construction are all magic and fully binary",
      all(magic(A) and fully_binary(A) for A in fam))
fs = [xor_syms(A) for A in fam]
check("every one has XOR symmetries: the half-shifts flip the 32s and 16s components",
      all({(0b100000, 32), (0b000100, 16)} <= set(s) for s in fs))
naff = sum(len(s) == 63 for s in fs)
nmir = sum(any(a in MIRRORS for a, b in s) for s in fs)
print(f"     affine (all 63 symmetries): {naff} of 2000;  with a mirror fold: {nmir} of 2000")
print("     symmetries per square:", dict(sorted(Counter(len(s) for s in fs).items())))
check("almost none is affine: the family is not 'affine or close to it'", naff < 20)

# ---- 3. annealed fully binary squares
if len(sys.argv) > 2:
    samp = [list(map(int, l.split())) for l in open(sys.argv[2]) if l.strip()]
    samp = [[S[8 * i:8 * i + 8] for i in range(8)] for S in samp]
    check(f"{len(samp)} annealed squares: all magic and fully binary", all(magic(A) and fully_binary(A) for A in samp))
    ss = [xor_syms(A) for A in samp]
    none = sum(not s for s in ss)
    print("     XOR symmetries per square:", dict(sorted(Counter(len(s) for s in ss).items())))
    check(f"full binary balance does not force an XOR symmetry: {none} of {len(samp)} have none", none > 0)
    print("     first such square:")
    A = next(A for A, s in zip(samp, ss) if not s)
    for r in A:
        print("      ", " ".join(f"{v:2d}" for v in r))

print()
print("ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
