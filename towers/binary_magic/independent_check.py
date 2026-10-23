"""
independent_check.py: a second implementation of the headline claims in binary_magic/.

It was written from the claims alone, not from the original scripts. It enumerates every square
from scratch, using a different method (row and column partitions rather than cell-by-cell search),
and recomputes every count. Pass a path to the original squares_4x4.json to diff the two
enumerations. Pure Python, standard library only. About a minute.
"""
import itertools, sys, json
from collections import Counter, defaultdict
from fractions import Fraction

FAILS = []
def check(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'} {name}")
    if not cond:
        FAILS.append(name)

def frenicle(A):
    """Frenicle standard form: smallest corner at top left, then A[0][1] < A[1][0]."""
    imgs, B = [], A
    for _ in range(4):
        B = tuple(zip(*B[::-1]))                     # quarter turn
        imgs += [B, tuple(zip(*B))]                  # and its transpose
    best = [M for M in imgs if M[0][0] == min(M[0][0], M[0][3], M[3][0], M[3][3]) and M[0][1] < M[1][0]]
    assert len(best) == 1
    return best[0]

def dihedral(A):
    imgs, B = [], A
    for _ in range(4):
        B = tuple(zip(*B[::-1]))
        imgs += [B, tuple(zip(*B))]
    return imgs

# ---------------------------------------------------------------- 1. the 880, from partitions
print("1. Enumeration (row-set and column-set partitions)")
subs = [frozenset(c) for c in itertools.combinations(range(16), 4) if sum(c) == 30]
parts = []
def rec(rem, chosen):
    if not rem:
        parts.append(tuple(chosen)); return
    m = min(rem)
    for s in subs:
        if m in s and s <= rem:
            rec(rem - s, chosen + [s])
rec(frozenset(range(16)), [])
all_sq = set()
for R in parts:
    for C in parts:
        if all(len(r & c) == 1 for r in R for c in C):
            cell = [[next(iter(r & c)) for c in C] for r in R]
            for rp in itertools.permutations(range(4)):
                for cp in itertools.permutations(range(4)):
                    A = tuple(tuple(cell[rp[i]][cp[j]] for j in range(4)) for i in range(4))
                    if sum(A[i][i] for i in range(4)) == 30 and sum(A[i][3 - i] for i in range(4)) == 30:
                        all_sq.add(A)
check(f"86 four-number sets sum to 30 ({len(subs)}); {len(parts)} partitions of 0..15 into them", len(subs) == 86)
check(f"7,040 magic squares in all ({len(all_sq)})", len(all_sq) == 7040)
SQ = sorted({frenicle(A) for A in all_sq})
check(f"880 up to rotation and reflection ({len(SQ)})", len(SQ) == 880)
if len(sys.argv) > 1:
    theirs = {tuple(map(tuple, s["square"])) for s in json.load(open(sys.argv[1]))}
    check("the same 880 squares as the original enumeration (squares_4x4.json)", theirs == set(SQ))

# ---------------------------------------------------------------- 2. bit planes and carries
print("2. Bit planes and carries")
def lines(A):
    rows = [A[i] for i in range(4)]
    cols = [tuple(A[i][j] for i in range(4)) for j in range(4)]
    return rows, cols, tuple(A[i][i] for i in range(4)), tuple(A[i][3 - i] for i in range(4))
def counts(vals):
    return [sum((v >> k) & 1 for v in vals) for k in range(4)]
def carry_vector(vals):
    """Write (count - 2) per plane as t0*(2,-1,0,0) + t1*(0,2,-1,0) + t2*(0,0,2,-1)."""
    e = [c - 2 for c in counts(vals)]
    t2 = -e[3]; t1 = 2 * t2 - e[2]; t0 = 2 * t1 - e[1]
    assert e[0] == 2 * t0
    return (t0, t1, t2)
nimm0 = all(counts(l) == [2, 2, 2, 2] for A in SQ for L in lines(A)[:2] for l in L)
check("Nimm0: every bit plane has exactly two 1s in every row and column, all 880", nimm0)
corner, sign = {}, {}
ok_size = ok_contig = ok_sign = ok_opp = True
for A in SQ:
    _, _, d1, d2 = lines(A)
    t, u = carry_vector(d1), carry_vector(d2)
    ok_opp &= all(x == -y for x, y in zip(t, u))
    ok_size &= all(x in (-1, 0, 1) for x in t)
    used = [k for k in range(3) if t[k]]
    ok_contig &= used == list(range(used[0], used[0] + len(used))) if used else True
    ok_sign &= len({t[k] for k in used}) <= 1
    corner[A] = "".join("1" if t[k] else "0" for k in (2, 1, 0))      # (4->8, 2->4, 1->2)
    sign[A] = t[used[0]] if used else 0
check("the two diagonals carry equal and opposite amounts", ok_opp)
check("every carry has size 1", ok_size)
check("the carries used are contiguous (1->2 with 4->8 alone never occurs)", ok_contig)
check("all carries on a diagonal have the same sign", ok_sign)
cc = Counter(corner.values())
print("     carry corners:", dict(sorted(cc.items())))
check("528 / 64 / 64 / 64 / 56 / 0 / 56 / 48", [cc.get(k, 0) for k in
      ("000", "001", "010", "100", "011", "101", "110", "111")] == [528, 64, 64, 64, 56, 0, 56, 48])
# corner 101 by line arithmetic: bits 0 and 2 frozen leaves {0,2,8,10}+offset, sums 20/24/36/40
sums = sorted({sum(v + b0 + 4 * b2 for v in (0, 2, 8, 10)) for b0 in (0, 1) for b2 in (0, 1)})
check(f"a line with bits 1s and 4s frozen sums to {sums}, never 30", 30 not in sums)
whole = [A for A in SQ if corner[A] == "111"]
sig = Counter((tuple(counts(lines(A)[2])), tuple(counts(lines(A)[3]))) for A in whole)
check("the 48 whole-only squares: one diagonal (0,1,1,3), the other (4,3,3,1)",
      all(set(k) == {(0, 1, 1, 3), (4, 3, 3, 1)} for k in sig))
check("handedness 24 / 24 among the whole-only squares", Counter(sign[A] for A in whole) == Counter({1: 24, -1: 24}))
diag8 = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 3), (1, 2), (2, 1), (3, 0)]
check("every plane has exactly four 1s on the eight diagonal cells, all 880",
      all(sum((A[i][j] >> k) & 1 for i, j in diag8) == 4 for A in SQ for k in range(4)))

# ---------------------------------------------------------------- 3. folds and affine squares
print("3. Folds (XOR symmetries) and affine squares")
def flat(A):
    return [A[x >> 2][x & 3] for x in range(16)]
def xor_syms(A):
    S = flat(A)
    return [(a, S[0] ^ S[a]) for a in range(1, 16) if all(S[x ^ a] == S[x] ^ S[0] ^ S[a] for x in range(16))]
LR, TB = 0b0011, 0b1100
syms = {A: xor_syms(A) for A in SQ}
check("every square has a left-right or top-bottom mirror fold (the fold theorem), all 880",
      all(any(a in (LR, TB) for a, b in syms[A]) for A in SQ))
# affine squares by brute force over GL(4,2) x constants
def parity(x):
    return bin(x).count("1") & 1
aff = set()
for rows_ in itertools.permutations(range(1, 16), 4):
    span = {0}
    for r in rows_:
        if r in span:
            break
        span |= {s ^ r for s in span}
    else:
        for c in range(16):
            v = [sum(parity(rows_[k] & x) << k for k in range(4)) ^ c for x in range(16)]
            A = tuple(tuple(v[4 * i + j] for j in range(4)) for i in range(4))
            if all(sum(l) == 30 for L in lines(A)[:2] for l in L) and sum(lines(A)[2]) == 30 and sum(lines(A)[3]) == 30:
                aff.add(frenicle(A))
check(f"432 affine squares over GF(2), by brute force over all 322,560 affine maps ({len(aff)})", len(aff) == 432)
check("the affine squares are exactly the squares with all 15 XOR symmetries", aff == {A for A in SQ if len(syms[A]) == 15})
check("every affine square is fully binary (carry corner 000)", all(corner[A] == "000" for A in aff))

# ---------------------------------------------------------------- 4. determinant and Takemura degree
print("4. Determinant and Takemura degree")
def det(M):
    M = [[Fraction(x) for x in r] for r in M]
    n, d = len(M), Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return 0
        if p != c:
            M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [M[r][k] - f * M[c][k] for k in range(n)]
    return d
P4 = list(itertools.permutations(range(4)))
SGN = {p: (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) for p in P4}
def degree(A):
    cv = Counter()
    for p in P4:
        cv[sum(A[i][p[i]] for i in range(4))] += SGN[p]
    cv = {v: c for v, c in cv.items() if c}
    if not cv:
        return "inf"
    m = 0
    while sum(c * v ** m for v, c in cv.items()) == 0:
        m += 1
    return m
D = {A: det(A) for A in SQ}
deg = {A: degree(A) for A in SQ}
check(f"640 singular, 240 invertible ({sum(D[A] == 0 for A in SQ)} / {sum(D[A] != 0 for A in SQ)})",
      sum(D[A] == 0 for A in SQ) == 640)
dc = Counter(str(d) for d in deg.values())
check(f"Takemura degree 3 / 4 / never: 240 / 624 / 16 ({dict(dc)})", dc == Counter({"3": 240, "4": 624, "inf": 16}))
check("degree 3 exactly when invertible", all((deg[A] == 3) == (D[A] != 0) for A in SQ))
def apd(A, m):
    return sum(SGN[p] * sum(A[i][p[i]] for i in range(4)) ** m for p in P4)
check("APD3 = 24 det / s on all 880 and on 200 random constant-row-sum integer matrices",
      all(apd(A, 3) == 24 * D[A] / 30 for A in SQ))
import random
random.seed(1)
okr = True
for _ in range(200):
    s = random.randint(1, 40)
    M = []
    for i in range(4):
        r = [random.randint(-9, 9) for _ in range(3)]
        M.append(tuple(r + [s - sum(r)]))
    okr &= apd(M, 3) == 24 * det(M) / s
check("  (the identity APD3 = 24 det/s is general, not special to magic squares)", okr)

# ---------------------------------------------------------------- 5. the triad and the fold rules
print("5. The triad: regions, folds, signs")
REGION = {"000": "center", "111": "center", "001": "petal", "010": "petal", "100": "petal",
          "011": "crossing", "110": "crossing", "101": "crossing"}
reg = {A: REGION[corner[A]] for A in SQ}
check("center 576, petals 192, crossings 112", Counter(reg.values()) == Counter({"center": 576, "petal": 192, "crossing": 112}))
comp = {A: any(b == 15 for a, b in syms[A]) for A in SQ}
check("singular exactly when there is a complement fold (some XOR symmetry with mask 1111)",
      all(comp[A] == (D[A] == 0) for A in SQ))
check("every invertible square has a fold flipping exactly 3 bits",
      all(any(bin(b).count("1") == 3 for a, b in syms[A]) for A in SQ if D[A] != 0))
check("every center square has a complement fold; no petal square has one",
      all(comp[A] for A in SQ if reg[A] == "center") and not any(comp[A] for A in SQ if reg[A] == "petal"))
# Lemma (easy): if the shift a keeps the main diagonal in place (row part = column part), the fold maps
# that diagonal onto itself with every value complemented, so each plane has 2 of its 4 ones there: no carry.
check("a complement fold whose shift keeps the main diagonal in place forces carry corner 000",
      all(corner[A] == "000" for A in SQ for a, b in syms[A] if b == 15 and a >> 2 == a & 3))
byreg = {r: Counter(str(deg[A]) for A in SQ if reg[A] == r) for r in ("center", "petal", "crossing")}
check(f"degree by region: center all 4, petals all 3, crossings 48/48/16 ({byreg})",
      byreg == {"center": Counter({"4": 576}), "petal": Counter({"3": 192}),
                "crossing": Counter({"3": 48, "4": 48, "inf": 16})})

# Dudeney's groups: the pattern of complement pairs (n, 15 - n), up to rotation and reflection
def pattern(A):
    def pp(G):
        pos = {G[i][j]: (i, j) for i in range(4) for j in range(4)}
        return tuple(sorted(tuple(sorted((pos[v], pos[15 - v]))) for v in range(8)))
    return min(pp(G) for G in dihedral(A))
grp = Counter(pattern(A) for A in SQ)
check(f"Dudeney's 12 groups: sizes {sorted(grp.values(), reverse=True)}",
      sorted(grp.values(), reverse=True) == [304, 96, 96, 56, 56, 56, 56, 48, 48, 48, 8, 8])
gs = {A: grp[pattern(A)] for A in SQ}
check("the 432 affine squares are both 96-groups, all three 48-groups, and 96 of the 304-group",
      Counter(gs[A] for A in aff) == Counter({96: 192, 48: 144, 304: 96}))
pand = [A for A in SQ if all(sum(A[i][(i + k) % 4] for i in range(4)) == 30 and
                             sum(A[i][(k - i) % 4] for i in range(4)) == 30 for k in range(4))]
asso = [A for A in SQ if all(A[i][j] + A[3 - i][3 - j] == 15 for i in range(4) for j in range(4))]
check(f"48 pandiagonal and 48 associative squares, disjoint, all fully binary ({len(pand)}, {len(asso)})",
      len(pand) == 48 and len(asso) == 48 and not set(pand) & set(asso)
      and all(corner[A] == "000" for A in pand + asso))
check("Durer's 1514 square is among the associative ones",
      frenicle(((16, 3, 2, 13), (5, 10, 11, 8), (9, 6, 7, 12), (4, 15, 14, 1))) in
      {frenicle(tuple(tuple(v + 1 for v in r) for r in A)) for A in asso})

# ---------------------------------------------------------------- 6. level 3: the cube's corners
print("6. The cube's corners 0..7")
rects = {frozenset([frozenset(r), frozenset(set(range(8)) - set(r))]) for r in itertools.combinations(range(8), 4)
         if sum(r) == 14 and all((n in r) != (7 - n in r) for n in range(8))}
check("one 2x4 magic rectangle on 0..7 up to order: rows {0,3,5,6} and {1,2,4,7}, columns (n, 7-n)",
      rects == {frozenset([frozenset({0, 3, 5, 6}), frozenset({1, 2, 4, 7})])})
check("{0,3,5,6} are the corners with an even number of 1-bits (one tetrahedron)",
      {n for n in range(8) if bin(n).count("1") % 2 == 0} == {0, 3, 5, 6})

# ---------------------------------------------------------------- 7. qubits and qutrits
print("7. Commuting grids of two-qubit and two-qutrit operators (symplectic vectors)")
def grids(p):
    """3x3 grids of distinct non-identity vectors in GF(p)^4 whose rows and columns are
    commuting triples x, y, z with x + y + z = 0 (lines that multiply to the identity)."""
    V = [v for v in itertools.product(range(p), repeat=4) if any(v)]
    om = lambda u, v: (u[0] * v[2] + u[1] * v[3] - u[2] * v[0] - u[3] * v[1]) % p
    add = lambda u, v: tuple((a + b) % p for a, b in zip(u, v))
    neg = lambda u: tuple((-a) % p for a in u)
    third = lambda u, v: neg(add(u, v))
    found = set()
    for g00 in V:
        for g01 in V:
            if g01 == g00 or om(g00, g01):
                continue
            g02 = third(g00, g01)
            for g10 in V:
                if om(g00, g10):
                    continue
                for g11 in V:
                    if om(g10, g11) or om(g01, g11):
                        continue
                    g12, g20, g21 = third(g10, g11), third(g00, g10), third(g01, g11)
                    g22 = third(g20, g21)
                    cells = [g00, g01, g02, g10, g11, g12, g20, g21, g22]
                    if any(not any(c) for c in cells) or len(set(cells)) < 9:
                        continue
                    if om(g20, g21) or om(g02, g12) or g22 != third(g02, g12):
                        continue
                    found.add(frozenset(cells))
    return found
q2 = grids(2)
check(f"two qubits: 10 grids (as sets of 9 operators) ({len(q2)})", len(q2) == 10)
q3 = grids(3)
check(f"two qutrits: no grid at all ({len(q3)})", len(q3) == 0)

# signs for the qubit grids, with real Pauli matrices (complex 4x4, pure Python)
I2 = [[1, 0], [0, 1]]; X = [[0, 1], [1, 0]]; Z = [[1, 0], [0, -1]]; Y = [[0, -1j], [1j, 0]]
def kron(a, b):
    return [[a[i // 2][j // 2] * b[i % 2][j % 2] for j in range(4)] for i in range(4)]
def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
PAULI = {(0, 0): I2, (1, 0): X, (0, 1): Z, (1, 1): Y}          # (x, z) bits
def op(v):                                                       # v = (x1, x2, z1, z2)
    return kron(PAULI[(v[0], v[2])], PAULI[(v[1], v[3])])
def line_sign(vs):
    m = mul(mul(op(vs[0]), op(vs[1])), op(vs[2]))
    s = m[0][0]
    assert all(abs(m[i][j] - (s if i == j else 0)) < 1e-9 for i in range(4) for j in range(4))
    return round(s.real if isinstance(s, complex) else s)
def mermin_odd(cells):
    """True if some 3x3 arrangement's six line signs multiply to -1 (no classical +-1 assignment)."""
    cells = list(cells)
    for g00, g01, g10, g11 in itertools.permutations(cells, 4):
        add2 = lambda u, v: tuple((a + b) % 2 for a, b in zip(u, v))
        rows = [(g00, g01, add2(g00, g01)), (g10, g11, add2(g10, g11))]
        rows.append(tuple(add2(rows[0][j], rows[1][j]) for j in range(3)))
        if {c for r in rows for c in r} == set(cells):
            cols = [tuple(rows[i][j] for i in range(3)) for j in range(3)]
            prod = 1
            for l in rows + cols:
                prod *= line_sign(l)
            return prod == -1
    return None
check("every two-qubit grid is a Mermin-Peres square (line signs multiply to -1)",
      all(mermin_odd(g) for g in q2))

# the magic Mermin square: over all 28 symplectic forms on GF(2)^4 ("qubit labelings")
def forms():
    out = []
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    for bits in range(64):
        W = [[0] * 4 for _ in range(4)]
        for t, (i, j) in enumerate(pairs):
            if (bits >> t) & 1:
                W[i][j] = W[j][i] = 1
        if det(W) % 2:
            out.append(W)
    return out
FORMS = forms()
check(f"28 symplectic forms on GF(2)^4 ({len(FORMS)})", len(FORMS) == 28)
def wform(W, a, b):
    return sum(W[i][j] * ((a >> i) & 1) * ((b >> j) & 1) for i in range(4) for j in range(4)) % 2
xor_magic = []                                  # 3x3 magic squares (sum 30) whose lines XOR to 0
for g00, g01, g10, g11 in itertools.permutations(range(1, 16), 4):
    G = [[g00, g01, g00 ^ g01], [g10, g11, g10 ^ g11]]
    G.append([G[0][j] ^ G[1][j] for j in range(3)])
    flatg = [v for r in G for v in r]
    if 0 in flatg or len(set(flatg)) < 9:
        continue
    L = G + [[G[i][j] for i in range(3)] for j in range(3)]
    if all(sum(l) == 30 for l in L) and G[0][0] + G[1][1] + G[2][2] == 30 and G[0][2] + G[1][1] + G[2][0] == 30:
        xor_magic.append((tuple(map(tuple, G)), L))
magic_mermin, labelings = set(), Counter()
for G, L in xor_magic:
    for t, W in enumerate(FORMS):
        if not any(wform(W, l[0], l[1]) for l in L):
            magic_mermin.add(min(dihedral(G)))
            labelings[t] += 1
print(f"     {len(xor_magic)} arrangements are magic with every line XOR 0; "
      f"{len({min(dihedral(G)) for G, L in xor_magic})} up to symmetry")
check(f"exactly one 3x3 square, up to rotation and reflection, is magic (sum 30) with commuting "
      f"rows and columns under some qubit labeling ({sorted(magic_mermin)})", len(magic_mermin) == 1)
check(f"  under exactly one of the 28 labelings ({len(labelings)})", len(labelings) == 1)
target = ((11, 13, 6), (5, 10, 15), (14, 7, 9))
check("  and it is 11 13 6 / 5 10 15 / 14 7 9", magic_mermin == {min(dihedral(target))})
G = target
hi = [[v // 4 for v in r] for r in G]; lo = [[v % 4 for v in r] for r in G]
latin = lambda M: all(sorted(r) == [1, 2, 3] for r in M) and all(sorted(c) == [1, 2, 3] for c in zip(*M))
check("in base 4 it is two orthogonal Latin squares on {1, 2, 3}",
      latin(hi) and latin(lo) and len({(hi[i][j], lo[i][j]) for i in range(3) for j in range(3)}) == 9)
vec = lambda n: ((n >> 3) & 1, (n >> 1) & 1, (n >> 2) & 1, n & 1)   # digit d = 2x + z per qubit
rows3 = [tuple(vec(v) for v in r) for r in G]
cols3 = [tuple(vec(G[i][j]) for i in range(3)) for j in range(3)]
signs = [line_sign(l) for l in rows3 + cols3]
check(f"read 1 = Z, 2 = X, 3 = Y it is XY YZ ZX / ZZ XX YY / YX ZY XZ; line signs {signs}, product -1",
      signs == [-1, -1, -1, 1, 1, 1])
lo_shu = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
check("Lo Shu: the centre 5 is the edge of n -> 10 - n (every complement pair is mirrored through the centre)",
      all(lo_shu[i][j] + lo_shu[2 - i][2 - j] == 10 for i in range(3) for j in range(3)) and lo_shu[1][1] == 5)

# ---------------------------------------------------------------- 8. order 8: affine count
print("8. Order 8: affine fully binary squares (count by subspace recursion)")
def rref(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
    # reduce fully
    basis.sort(reverse=True)
    changed = True
    while changed:
        changed = False
        for i in range(len(basis)):
            for j in range(len(basis)):
                if i != j and basis[j] ^ basis[i] < basis[j] and (basis[j] >> (basis[i].bit_length() - 1)) & 1:
                    basis[j] ^= basis[i]; changed = True
        basis.sort(reverse=True)
    return tuple(basis)
def count_bases(m):
    n = 2 * m
    allowed = [(r << m) | c for r in range(1, 2 ** m) for c in range(1, 2 ** m) if r != c]
    memo = {}
    def f(B):
        if len(B) == n:
            return 1
        if B in memo:
            return memo[B]
        span = {0}
        for b in B:
            span |= {s ^ b for s in span}
        tot = sum(f(rref(list(B) + [v])) for v in allowed if v not in span)
        memo[B] = tot
        return tot
    return f(()), len(allowed)
b4, n4 = count_bases(2)
check(f"order 4: {n4} allowed patterns, {b4} ordered bases -> {b4 * 16 // 8} squares (432)", b4 * 16 // 8 == 432)
b8, n8 = count_bases(3)
check(f"order 8: {n8} allowed patterns, {b8:,} ordered bases -> {b8 * 64 // 8:,} squares (12,631,127,040)",
      b8 * 64 // 8 == 12631127040)

print()
print("ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
