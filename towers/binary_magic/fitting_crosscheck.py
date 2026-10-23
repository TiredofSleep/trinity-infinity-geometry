"""
fitting_crosscheck.py: what F. Fitting (1931) already had, checked against the 880 squares.

F. Fitting, "Rein mathematische Behandlung des Problems der magischen Quadrate von 16 und von 64
Feldern", Jahresbericht der DMV 40 (1931) 177-199. Free scan and OCR at the Goettingen digital library
(GDZ, PPN37721857X_0040). Fitting credits the key idea, splitting a square into its four binary
"components", to his son, then a student in Goettingen: Hans Fitting, the algebraist.

Each check below states a result in Fitting's language and tests it on all 880 squares (read from
squares_4x4.json, whose path is the first argument).
"""
import itertools, json, sys
from collections import Counter

SQ = [tuple(map(tuple, s["square"])) for s in json.load(open(sys.argv[1]))]
FAILS = []
def check(name, cond):
    print(f"  {'ok  ' if cond else 'FAIL'} {name}")
    if not cond:
        FAILS.append(name)

def plane(A, k):
    return tuple(tuple((v >> k) & 1 for v in r) for r in A)
def diag_counts(P):
    return sum(P[i][i] for i in range(4)), sum(P[i][3 - i] for i in range(4))
def lines_ok(P):                                  # two 1s in every row, column and both diagonals
    return all(sum(r) == 2 for r in P) and all(sum(c) == 2 for c in zip(*P)) and diag_counts(P) == (2, 2)

# Fitting's "regular" forms: two 1s in every row and column (Section II); Section III proves that
# no other components occur. That is Nimm0, proved in 1931.
check("Section III: every component is regular (two 1s in each row and column), all 880",
      all(all(sum(r) == 2 for r in P) and all(sum(c) == 2 for c in zip(*P))
          for A in SQ for P in (plane(A, k) for k in range(4))))

# Satz 3: each regular component has two 1s on each of four 4-cell sets: the corners, the centre,
# and the two sets of middle edge cells. Folgerung: a ones on one diagonal means 4 - a on the other.
SETS = {"corners": [(0, 0), (0, 3), (3, 0), (3, 3)], "centre": [(1, 1), (1, 2), (2, 1), (2, 2)],
        "top/bottom middles": [(0, 1), (0, 2), (3, 1), (3, 2)], "left/right middles": [(1, 0), (2, 0), (1, 3), (2, 3)]}
check("Satz 3: every component has two 1s on each of the four sets (corners, centre, edge middles)",
      all(sum(P[i][j] for i, j in S) == 2 for A in SQ for P in (plane(A, k) for k in range(4)) for S in SETS.values()))
check("Folgerung: a 1s on one diagonal, 4 - a on the other (the diagonals cancel plane by plane)",
      all(sum(diag_counts(plane(A, k))) == 4 for A in SQ for k in range(4)))

# A-, B-, C-forms by the diagonal: 2/2, 3/1, 4/0
def form(P):
    a, b = diag_counts(P)
    return {2: "A", 3: "B", 1: "B", 4: "C", 0: "C"}[a]
kinds = Counter()
for A in SQ:
    f = [form(plane(A, k)) for k in range(4)]
    kinds[(f.count("B"), f.count("C"))] += 1
print("     (B-forms, C-forms):", dict(sorted(kinds.items())))
check("Satz 4 and 5: a square with non-magic components has exactly one C-form", all(c == 1 for b, c in kinds if b))
check("Sections I and II a-c: 528 squares with four A-forms, 192 with one B-form, 112 with two, 48 with three",
      kinds == Counter({(0, 0): 528, (1, 1): 192, (2, 1): 112, (3, 1): 48}))

# In the carry language of binary_magic/: the number of B-forms is the number of carries used, and
# the one C-form is the plane at the bottom of the carry chain (Fitting's diagonal equations 2a = b,
# 2a = b - c, 2a = b - c - d are the carry equations; his "2a = b + c is unsolvable" is the empty corner).
def carries(A):
    e = [c - 2 for c in diag_counts_planes(A)]
    t2 = -e[3]; t1 = 2 * t2 - e[2]; t0 = 2 * t1 - e[1]
    return [t0, t1, t2]
def diag_counts_planes(A):
    return [sum((A[i][i] >> k) & 1 for i in range(4)) for k in range(4)]
ok = True
for A in SQ:
    t = carries(A)
    used = [k for k in range(3) if t[k]]
    f = [form(plane(A, k)) for k in range(4)]
    ok &= f.count("B") == len(used)
    if used:
        ok &= f[used[0]] == "C" and all(f[k + 1] == "B" for k in used)
check("number of B-forms = number of carries; the C-form is the lowest plane of the carry chain", ok)

# Section I: the eight magic forms (up to swapping 0 and 1) and the eleven quadruples they make
forms = set()
for ones in itertools.combinations(range(16), 8):
    P = tuple(tuple(1 if 4 * i + j in ones else 0 for j in range(4)) for i in range(4))
    if lines_ok(P):
        forms.add(min(P, tuple(tuple(1 - x for x in r) for r in P)))
check(f"Section I: 16 magic forms, 8 up to swapping 0 and 1 ({len(forms)})", len(forms) == 8)
def affine_form(P):
    S = [P[x >> 2][x & 3] for x in range(16)]
    return all(S[x ^ a] ^ S[x] == S[0] ^ S[a] for a in range(16) for x in range(16))
aff_forms = {P for P in forms if affine_form(P)}
check(f"  6 of the 8 are affine over GF(2) (an XOR of position bits); the other 2 are not ({len(aff_forms)})",
      len(aff_forms) == 6)
def fit(Ps):                                       # every 0/1 combination equally often (Satz 2a-2c)
    combos = Counter(tuple(P[i][j] for P in Ps) for i in range(4) for j in range(4))
    return len(combos) == 2 ** len(Ps) and len(set(combos.values())) == 1
quads = [q for q in itertools.combinations(sorted(forms), 4) if fit(q)]
check(f"  they make 11 fitting quadruples ({len(quads)}); 11 x 4! x 2^4 / 8 = 528", len(quads) == 11 and 11 * 24 * 16 // 8 == 528)
aq = [q for q in quads if all(P in aff_forms for P in q)]
check(f"  9 of the 11 quadruples are all-affine: 9 x 48 = 432, the affine squares ({len(aq)})", len(aq) == 9)

print()
print("ALL CHECKS PASSED" if not FAILS else f"{len(FAILS)} FAILED: {FAILS}")
sys.exit(1 if FAILS else 0)
