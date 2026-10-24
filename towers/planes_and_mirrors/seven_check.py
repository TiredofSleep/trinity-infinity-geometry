"""
seven_check.py — what 7 dimensions actually contain.
Octonions by Cayley-Dickson doubling (R -> C -> H -> O), basis e_0..e_7 labelled by 3-bit strings.
Checks: e_a e_b = +- e_(a xor b); the 7 Fano lines (triples that XOR to 0) are each a copy of the
quaternions; a cross product with |x cross y|^2 = |x|^2|y|^2 - (x.y)^2 exists in 7D; octonions are not
associative; and one more doubling (sedenions) breaks division.
"""
import itertools
from collections import Counter
import numpy as np

def conj(x):
    y = -x.copy(); y[0] = x[0]; return y
def mult(x, y):                       # Cayley-Dickson: (a,b)(c,d) = (ac - d* b, d a + b c*)
    n = len(x)
    if n == 1:
        return x * y
    h = n // 2
    a, b, c, d = x[:h], x[h:], y[:h], y[h:]
    return np.concatenate([mult(a, c) - mult(conj(d), b), mult(d, a) + mult(b, conj(c))])
def e(k, n=8):
    v = np.zeros(n); v[k] = 1; return v

rule = all(np.count_nonzero(mult(e(a), e(b))) == 1 and abs(mult(e(a), e(b))[a ^ b]) == 1
           for a in range(8) for b in range(8))
print("e_a e_b = +-e_(a xor b) for all 64 pairs:", rule)
lines = [t for t in itertools.combinations(range(1, 8), 3) if t[0] ^ t[1] ^ t[2] == 0]
print("Fano lines (nonzero 3-bit triples that XOR to 0):", lines)
quat = all(np.allclose(mult(e(i), e(i)), -e(0)) and np.allclose(mult(e(i), e(j)), -mult(e(j), e(i)))
           for t in lines for i in t for j in t if i != j)
print("each line behaves like i, j, k of the quaternions (squares to -1, pairs anticommute):", quat)

rng = np.random.default_rng(0)
def cross7(x, y):                     # imaginary part of the octonion product
    X = np.concatenate([[0], x]); Y = np.concatenate([[0], y])
    return mult(X, Y)[1:]
ok = True
for _ in range(1000):
    x, y = rng.normal(size=7), rng.normal(size=7)
    c = cross7(x, y)
    ok &= np.isclose(c @ c, (x @ x) * (y @ y) - (x @ y) ** 2) and np.isclose(c @ x, 0) and np.isclose(c @ y, 0)
print("7D cross product: perpendicular to both, length^2 = |x|^2|y|^2 - (x.y)^2 (1000 random pairs):", ok)

x, y, z = (rng.normal(size=8) for _ in range(3))
print("octonions associative? (xy)z == x(yz):", np.allclose(mult(mult(x, y), z), mult(x, mult(y, z))))
s = e(3, 16) + e(10, 16); t = e(6, 16) - e(15, 16)
print("sedenions (one more doubling): a nonzero pair whose product is 0 ->", np.allclose(mult(s, t), 0) and
      np.any(s) and np.any(t), "(division breaks)" )

# ---------------------------------------------------------------------------------------------
# Part 2: is it a fractal? The XOR skeleton nests forever; the signs that make it a number system stop.
print("\n--- the skeleton: projective spaces over F2 (points = nonzero bit strings, lines = XOR-to-0 triples)")
for n in range(2, 6):
    pts = range(1, 2 ** n)
    lines_n = [t for t in itertools.combinations(pts, 3) if t[0] ^ t[1] ^ t[2] == 0]
    per_pt = Counter(p for t in lines_n for p in t)
    # Fano planes = 3-bit subspaces: count them by closing triples of independent points
    planes = set()
    if n >= 3:
        for a, b, c in itertools.combinations(pts, 3):
            if a ^ b != c and (a ^ b) ^ c != 0:
                span = frozenset({a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
                if len(span) == 7: planes.add(span)
    print(f"  {n} bits: {2**n-1:2d} points, {len(lines_n):3d} lines, each point on {set(per_pt.values())} lines,"
          f" {len(planes):3d} copies of the 7-point Fano plane inside")

print("\n--- the flesh: does the Cayley-Dickson product keep lengths (|xy| = |x||y|)?")
for n in (1, 2, 4, 8, 16, 32):
    xs = [rng.normal(size=n) for _ in range(200)]
    keeps = all(np.isclose(np.linalg.norm(mult(x, y)), np.linalg.norm(x) * np.linalg.norm(y))
                for x, y in zip(xs, xs[1:]))
    print(f"  dimension {n:2d}: lengths multiply = {keeps}")

# ---------------------------------------------------------------------------------------------
# Part 3: the symmetry of 7D (G2 = automorphisms of the octonions).
print("\n--- G2: derivations D with D(xy) = D(x)y + xD(y)")
rows = []
E = [e(k) for k in range(8)]
for a in range(8):
    for b in range(8):
        for out in range(8):
            # coefficient of D_{ij} in [D(e_a e_b) - D(e_a) e_b - e_a D(e_b)]_out ; D_{ij} = <e_i, D e_j>
            row = np.zeros(64)
            ab = mult(E[a], E[b])
            for j in range(8):
                if ab[j]: row[out * 8 + j] += ab[j]
            for i in range(8):
                row[i * 8 + a] -= mult(E[i], E[b])[out]
                row[i * 8 + b] -= mult(E[a], E[i])[out]
            rows.append(row)
null = 64 - np.linalg.matrix_rank(np.array(rows))
print("  dimension of the symmetry (G2):", null)

def plane_rot(angles, planes):
    R = np.eye(8)
    for th, (p, q) in zip(angles, planes):
        c, s = np.cos(th), np.sin(th)
        R[p, p] = c; R[q, q] = c; R[p, q] = -s; R[q, p] = s
    return R
def is_auto(R, trials=40):
    for _ in range(trials):
        x, y = rng.normal(size=8), rng.normal(size=8)
        if not np.allclose(R @ mult(x, y), mult(R @ x, R @ y)): return False
    return True

# Fix e1. The three Fano lines through e1 leave three planes: (e2,e3), (e4,e5), (e6,e7).
# Orient each plane by e1: (e_p, e1*e_p).
planes = []
for p in (2, 4, 6):
    q = int(np.flatnonzero(mult(e(1), e(p)))[0]); planes.append((p, q) if mult(e(1), e(p))[q] > 0 else (q, p))
print("  planes through e1, oriented by e1:", planes)
deg = np.pi / 180
tests = [(120, 120, 120), (90, 90, 180), (90, -90, 0), (30, 50, -80), (90, 90, 90), (120, 120, 0), (60, 60, 60)]
for t in tests:
    print(f"  turn the three planes by {t} deg (sum {sum(t):4d}): keeps the octonion product = "
          f"{is_auto(plane_rot([a * deg for a in t], planes))}")
rnd = [(a, b, -(a + b)) for a, b in rng.uniform(-180, 180, size=(200, 2))]
print("  200 random angle triples with sum 0, all automorphisms:",
      all(is_auto(plane_rot([a * deg for a in t], planes), 8) for t in rnd))
rnd_bad = [tuple(rng.uniform(-180, 180, size=3)) for _ in range(200)]
print("  200 random triples with sum != 0 mod 360, any automorphism:",
      any(is_auto(plane_rot([a * deg for a in t], planes), 8) for t in rnd_bad if abs(((sum(t) + 180) % 360) - 180) > 1))

# ---------------------------------------------------------------------------------------------
# Part 4: the 120 in 7D. E7 = E8 roots orthogonal to one root; angles between roots.
r8 = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = np.zeros(8); v[i] = si; v[j] = sj; r8.append(v)
for signs in itertools.product((0.5, -0.5), repeat=8):
    if sum(s < 0 for s in signs) % 2 == 0: r8.append(np.array(signs))
r8 = np.array(r8)
r7 = r8[np.isclose(r8 @ r8[0], 0)]
ang = sorted({int(round(np.degrees(np.arccos(np.clip(a @ b / 2, -1, 1))))) for a in r7 for b in r7 if not np.allclose(a, b)})
print(f"\nE8 roots: {len(r8)};  E7 roots: {len(r7)};  angles between E7 roots: {ang}")
