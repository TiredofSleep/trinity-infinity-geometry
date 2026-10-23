"""
split_check.py — Where does the 48 / 64 / 192 split of Dudeney's 304 group come from?

Run after binary_magic.py (needs squares_4x4.json).
Tests, in order:
  1. Rebuild Dudeney's 12 groups (complement-pair patterns) and the balance split per group.
  2. Is "number of balanced bit planes" a true invariant of the symmetries that
     preserve ALL magic squares (32 grid moves x complement)?  If not, the split
     is a property of the binary labeling, not of the squares.
  3. Which bit plane is the balanced one in 1-balanced squares?
  4. Fully binary squares are closed under all 384 tesseract symmetries
     (bit permutations x bit flips) — forced, because every line count is 2 in every plane.
  5. The carry signatures of the 48 whole-only squares.
"""
import json, itertools
from collections import Counter, defaultdict

S = 30
data = json.load(open("squares_4x4.json"))
squares = [tuple(map(tuple, x["square"])) for x in data]

LINES = [[(i, j) for j in range(4)] for i in range(4)] + \
        [[(i, j) for i in range(4)] for j in range(4)] + \
        [[(i, i) for i in range(4)], [(i, 3 - i) for i in range(4)]]

def magic(M):
    return all(sum(M[i][j] for i, j in L) == S for L in LINES)

def geo(M):
    out, A = [], M
    for _ in range(4):
        A = tuple(zip(*A[::-1]))
        out += [A, tuple(r[::-1] for r in A)]
    return out

def canon(M):
    return min(geo(M))

def balanced_planes(M):
    return tuple(k for k in range(4)
                 if all(sum((M[i][j] >> k) & 1 for i, j in L) == 2 for L in LINES))

# ---------- 1. Dudeney groups ----------
def pair_pattern(M):
    pos = {M[i][j]: (i, j) for i in range(4) for j in range(4)}
    return frozenset(frozenset((pos[n], pos[15 - n])) for n in range(8))

def pattern_canon(M):
    return min(tuple(sorted(tuple(sorted(p)) for p in pair_pattern(G))) for G in geo(M))

groups = defaultdict(list)
for M in squares:
    groups[pattern_canon(M)].append(M)
sizes = sorted((len(v) for v in groups.values()), reverse=True)
assert sizes == [304, 96, 96, 56, 56, 56, 56, 48, 48, 48, 8, 8], sizes
print("1. Dudeney's 12 groups reproduced:", sizes)
for key, sq in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    print(f"   group of {len(sq):3d}: balanced-plane counts",
          dict(sorted(Counter(len(balanced_planes(M)) for M in sq).items())))
G304 = next(v for v in groups.values() if len(v) == 304)

# ---------- 2. invariance under the magic-preserving symmetries ----------
all7040 = sorted({G for M in squares for G in geo(M)})
assert len(all7040) == 7040
pos_maps = []
for s in itertools.permutations(range(4)):
    for t in itertools.permutations(range(4)):
        for tr in (False, True):
            def f(M, s=s, t=t, tr=tr):
                A = tuple(tuple(M[s[i]][t[j]] for j in range(4)) for i in range(4))
                return tuple(zip(*A)) if tr else A
            if all(magic(f(M)) for M in all7040):
                pos_maps.append(f)
assert len(pos_maps) == 32
comp = lambda M: tuple(tuple(15 - v for v in r) for r in M)
group64 = [f for f in pos_maps] + [lambda M, f=f: comp(f(M)) for f in pos_maps]

orbit_of, orbits = {}, []
for M in squares:
    c = canon(M)
    if c in orbit_of:
        continue
    orb, stack = {c}, [M]
    while stack:
        X = stack.pop()
        for g in group64:
            Y = canon(g(X))
            if Y not in orb:
                orb.add(Y); stack.append(g(X))
    for y in orb:
        orbit_of[y] = len(orbits)
    orbits.append(orb)
print(f"\n2. Orbits of the 880 under the 64 magic-preserving moves: {len(orbits)}, "
      f"sizes {dict(Counter(len(o) for o in orbits))}")
bal = {canon(M): len(balanced_planes(M)) for M in squares}
mixed = [o for o in orbits if len({bal[c] for c in o}) > 1]
print(f"   orbits that MIX balance levels: {len(mixed)} of {len(orbits)}")
grp_of = {canon(M): len(v) for v in groups.values() for M in v}
mixed_grp = [o for o in orbits if len({grp_of[c] for c in o}) > 1]
print(f"   orbits that MIX Dudeney groups:  {len(mixed_grp)} of {len(orbits)}")
for o in mixed[:6]:
    print("     e.g. orbit of", len(o), "balance levels", dict(Counter(bal[c] for c in o)),
          "groups", dict(Counter(grp_of[c] for c in o)))

# ---------- 3. which plane is balanced when only one is ----------
one = Counter(balanced_planes(M) for M in squares if len(balanced_planes(M)) == 1)
two = Counter(balanced_planes(M) for M in squares if len(balanced_planes(M)) == 2)
one304 = Counter(balanced_planes(M) for M in G304 if len(balanced_planes(M)) == 1)
print("\n3. single balanced plane, all 880 (bit 0 = 1s, bit 3 = 8s):", dict(one))
print("   single balanced plane, 304 group:", dict(one304))
print("   pairs of balanced planes (all 880):", dict(two))

# ---------- 4. fully binary squares are closed under the tesseract group ----------
tess = []
for perm in itertools.permutations(range(4)):
    for mask in range(16):
        table = [sum(((v >> perm[k]) & 1) << k for k in range(4)) ^ mask for v in range(16)]
        tess.append(table)
full = [M for M in squares if len(balanced_planes(M)) == 4]
closed = all(magic(tuple(tuple(t[v] for v in r) for r in M)) for M in full for t in tess)
broken = sum(1 for M in squares if len(balanced_planes(M)) < 4
             for t in tess if not magic(tuple(tuple(t[v] for v in r) for r in M)))
print(f"\n4. all 384 tesseract symmetries keep all {len(full)} fully-binary squares magic: {closed}")
assert closed
# orbits of the fully binary squares under (32 grid moves) x (384 tesseract symmetries)
seen, full_orbits = set(), []
for M in full:
    c = canon(M)
    if c in seen:
        continue
    orb, stack = {c}, [M]
    while stack:
        X = stack.pop()
        for f in pos_maps:
            Y0 = f(X)
            for t in tess:
                Y = tuple(tuple(t[v] for v in r) for r in Y0)
                cy = canon(Y)
                if cy not in orb:
                    orb.add(cy); stack.append(Y)
    seen |= orb; full_orbits.append(orb)
print(f"   fully-binary squares under grid x tesseract: {len(full_orbits)} orbit(s), "
      f"sizes {[len(o) for o in full_orbits]}")
for o in full_orbits:
    print("     orbit of", len(o), "spans Dudeney groups", dict(sorted(Counter(grp_of[c] for c in o).items())))

# ---------- 5. carry signatures of whole-only squares ----------
def line_counts(M):
    return tuple(tuple(sum((M[i][j] >> k) & 1 for i, j in L) for k in range(4)) for L in LINES)
sig = Counter()
for M in squares:
    if len(balanced_planes(M)) == 0:
        sig[tuple(sorted(Counter(line_counts(M)).items()))] += 1
print(f"\n5. whole-only squares: {sum(sig.values())}; distinct carry signatures: {len(sig)}")
for s, n in sig.most_common(4):
    print("   ", n, "squares; line types (c1s,c2s,c4s,c8s) x how many lines:", s)

# ---------- 6. the carry cube ----------
# On a line of 4 cells, plane k holds c_k ones (balanced = 2). Write d_k = c_k - 2.
# Line sum 30 means sum d_k 2^k = 0, so d is a sum of elementary carries:
#   carry0 = (-2,+1,0,0)  two 1s -> one 2
#   carry1 = (0,-2,+1,0)  two 2s -> one 4
#   carry2 = (0,0,-2,+1)  two 4s -> one 8
# Solve: a = -d0/2, b = d2 + 2*d3, c = d3; consistency d1 = a - 2b.
LINE_NAMES = [f"row{i}" for i in range(4)] + [f"col{j}" for j in range(4)] + ["diag", "anti"]
corner_count = Counter()
corner_vs_bal = defaultdict(Counter)
carry_lines = Counter()
for M in squares:
    U = set()
    for name, L in zip(LINE_NAMES, LINES):
        d = [sum((M[i][j] >> k) & 1 for i, j in L) - 2 for k in range(4)]
        a, c = -d[0] // 2, d[3]
        b = d[2] + 2 * d[3]
        assert d[0] % 2 == 0 and d[1] == a - 2 * b          # every line IS a sum of carries
        assert all(x in (-1, 0, 1) for x in (a, b, c))       # each carry used at most once
        for k, x in enumerate((a, b, c)):
            if x:
                U.add(k)
        if len(balanced_planes(M)) == 0 and (a, b, c) != (0, 0, 0):
            carry_lines[(name, (a, b, c))] += 1
    corner = "".join("1" if k in U else "0" for k in (2, 1, 0))   # bits: carry2 carry1 carry0
    corner_count[corner] += 1
    corner_vs_bal[corner][balanced_planes(M)] += 1
    # theorem: plane k balanced  <=>  carries k-1 and k both unused
    pred = tuple(k for k in range(4) if (k - 1) not in U and k not in U)
    assert pred == balanced_planes(M)
print("\n6. Carry cube (bits = carry 4->8, 2->4, 1->2 used anywhere in the square):")
for corner in [format(n, "03b") for n in range(8)]:
    print(f"   {corner}: {corner_count.get(corner, 0):4d} squares   balanced planes "
          f"{dict(corner_vs_bal[corner]) if corner in corner_vs_bal else '-'}")
print("   theorem 'plane k balanced iff carries k-1 and k unused' holds on all 880: True")
print("   by number of carries used:",
      {w: sum(n for c, n in corner_count.items() if c.count('1') == w) for w in range(4)})
print("   which lines carry in the 48 whole-only squares:", dict(carry_lines))

def corner_of(M):
    U = set()
    for L in LINES:
        d = [sum((M[i][j] >> k) & 1 for i, j in L) - 2 for k in range(4)]
        a, c = -d[0] // 2, d[3]
        b = d[2] + 2 * d[3]
        U |= {k for k, x in enumerate((a, b, c)) if x}
    return "".join("1" if k in U else "0" for k in (2, 1, 0))
print("   carry corners per Dudeney group:")
for key, sq in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    print(f"     {len(sq):3d}:", dict(sorted(Counter(corner_of(M) for M in sq).items())))

# ---------- 7. why corner 101 is empty, and what the corner really is ----------
# A line using carries 1->2 and 4->8 but not 2->4 has planes 0 and 2 constant on it,
# so its four DISTINCT values are the four numbers sharing those two bits. Their sums:
fixed = {}
for b0 in (0, 1):
    for b2 in (0, 1):
        vals = [v for v in range(16) if (v & 1) == b0 and ((v >> 2) & 1) == b2]
        fixed[(b0, b2)] = (vals, sum(vals))
print("\n7. corner 101 needs a line with bits 0 and 2 frozen; the only such 4-sets:",
      {k: v for k, v in fixed.items()})
assert all(s != 30 for _, s in fixed.values())
print("   none sums to 30 -> corner 101 is forced empty (distinctness), not luck")
# The carry corner equals the diagonal nim-sum (XOR) shifted down one bit.
from functools import reduce
ok = all(reduce(lambda x, y: x ^ y, (M[i][i] for i in range(4))) ==
         reduce(lambda x, y: x ^ y, (M[i][3 - i] for i in range(4))) == 2 * int(corner_of(M), 2)
         for M in squares)
rows_nim0 = all(reduce(lambda x, y: x ^ y, (M[i][j] for i, j in L)) == 0 for M in squares for L in LINES[:8])
print(f"   rows & columns nim-sum 0 in all 880 (Conway-Norton-Ryba 'Nimm0'): {rows_nim0}")
print(f"   both diagonals' nim-sum == 2 x carry corner, in all 880: {ok}")
assert ok and rows_nim0
