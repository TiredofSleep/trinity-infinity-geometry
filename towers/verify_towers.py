#!/usr/bin/env python3
"""verify_towers.py -- checks every [FORCED] floor of THE_TOWERS.md.

    python verify_towers.py      (~20 s)

Each tower rises from a shape or picture of the base. This script checks the floors that can be
computed; the deep theorems at the tops (Hurwitz, Galois, Hales, Viazovska, Bott) are cited, not
reproved.

  1  the three towers in every dimension: simplex (n+1 corners), cross-polytope (2n), cube (2^n);
     their face counts, Euler's relation, duality; and the count of regular polytopes by
     dimension (5 in 3-D, 6 in 4-D, 3 from 5-D on), by Coxeter's criterion
  2  the number tower: doubling 1 -> 2 -> 4 -> 8 -> 16 loses order, commutativity,
     associativity, then division
  3  the symmetry tower: the Platonic rotation groups (12, 24, 60), their classes, why A5 is
     simple and A4, S4 are not; unit quaternions double-cover the rotations
  4  the lattice tower: packing densities and kissing numbers of the cubic lattices; E8's 240
  5  the harmonic tower: the magic angle is P2's zero; Legendre orthogonality; 2l+1 harmonics
  6  the real-number tower: the best fractions for sqrt(2) (Pell)
  7  the growth tower: the exponential of a turn is a rotation; exp maps so(3) onto rotations
"""
import itertools
from math import comb, factorial

import numpy as np

rng = np.random.default_rng(11)
PHI = (1 + 5 ** 0.5) / 2


def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"claim failed: {name}"


# =============================================================== 1. the three eternal towers
print("1 -- the simplex, cross-polytope and cube towers")
simplex = lambda n: np.eye(n + 1)                                      # n+1 equal points, in R^(n+1)
cross = lambda n: np.vstack([np.eye(n), -np.eye(n)])                   # the 2n points +-e_i
cube = lambda n: np.array(list(itertools.product((1, -1), repeat=n)), float)   # the 2^n corners


def edge_count(P):
    d = np.linalg.norm(P[:, None] - P[None], axis=-1)[np.triu_indices(len(P), 1)]
    return int(np.isclose(d, d.min()).sum())


ok("corners grow by +1 (simplex), +2 (cross-polytope), x2 (cube): in 3-D, 4, 6, 8",
   [len(simplex(3)), len(cross(3)), len(cube(3))] == [4, 6, 8])
ok("edges from the coordinates match the formulas C(n+1,2), 2n(n-1), n*2^(n-1)  (n = 2..6)",
   all(edge_count(simplex(n)) == comb(n + 1, 2) and edge_count(cross(n)) == 2 * n * (n - 1)
       and edge_count(cube(n)) == n * 2 ** (n - 1) for n in range(2, 7)))
fs = lambda n: [comb(n + 1, k + 1) for k in range(n)]                  # k-faces of the n-simplex
fx = lambda n: [comb(n, k + 1) * 2 ** (k + 1) for k in range(n)]       # of the n-cross-polytope
fc = lambda n: [comb(n, k) * 2 ** (n - k) for k in range(n)]           # of the n-cube
euler = lambda f: sum((-1) ** k * x for k, x in enumerate(f))
ok("Euler's relation holds on every floor: alternating face sum = 1 - (-1)^n  (n = 1..10)",
   all(euler(F(n)) == 1 - (-1) ** n for F in (fs, fx, fc) for n in range(1, 11)))
ok("the cube and the cross-polytope are duals: k-faces of one = (n-1-k)-faces of the other",
   all(fc(n)[k] == fx(n)[n - 1 - k] for n in range(1, 11) for k in range(n)))
ok("the octahedron's and the cube's symmetry: signed permutations, 2^n n! -> 2, 8, 48, 384",
   [2 ** n * factorial(n) for n in range(1, 5)] == [2, 8, 48, 384])


def regular_polytopes(d):
    """Schlafli symbols {p1..p_(d-1)} whose Coxeter group is finite (Gram matrix positive definite)."""
    found = []
    for s in itertools.product(range(3, 8), repeat=d - 1):
        G = np.eye(d)
        for i, p in enumerate(s):
            G[i, i + 1] = G[i + 1, i] = -np.cos(np.pi / p)
        if np.linalg.eigvalsh(G).min() > 1e-9:
            found.append(s)
    return found


counts = {d: len(regular_polytopes(d)) for d in range(3, 9)}
ok(f"regular polytopes by dimension (Coxeter's criterion): {counts}",
   counts == {3: 5, 4: 6, 5: 3, 6: 3, 7: 3, 8: 3})
ok("from 5-D on the three are exactly the simplex {3,..,3}, the cube {4,3,..} and the cross-polytope {..,3,4}",
   all(set(regular_polytopes(d)) == {(3,) * (d - 1), (4,) + (3,) * (d - 2), (3,) * (d - 2) + (4,)} for d in range(5, 9)))
ok("the two extra 3-D solids carry five-fold symmetry: {3,5} icosahedron and {5,3} dodecahedron",
   set(regular_polytopes(3)) - {(3, 3), (3, 4), (4, 3)} == {(3, 5), (5, 3)})
ok("the five-fold line climbs one floor -- {3,3,5} (600-cell) and {5,3,3} (120-cell) in 4-D -- then ends",
   {(3, 3, 5), (5, 3, 3)} <= set(regular_polytopes(4)) and all(5 not in sym for d in range(5, 9) for sym in regular_polytopes(d)))


# =============================================================== 2. the number tower
print("2 -- the number tower: R -> C -> H -> O -> sedenions (Cayley-Dickson doubling)")


def conj(x):
    return np.concatenate([x[:1], -x[1:]])


def mul(a, b):
    n = len(a)
    if n == 1:
        return a * b
    h = n // 2
    a1, a2, b1, b2 = a[:h], a[h:], b[:h], b[h:]
    return np.concatenate([mul(a1, b1) - mul(conj(b2), a2), mul(b2, a1) + mul(a2, conj(b1))])


def props(n, trials=40):
    rs = [rng.normal(size=n) for _ in range(3 * trials)]
    comm = all(np.allclose(mul(a, b), mul(b, a)) for a, b in zip(rs[::3], rs[1::3]))
    assoc = all(np.allclose(mul(mul(a, b), c), mul(a, mul(b, c))) for a, b, c in zip(rs[::3], rs[1::3], rs[2::3]))
    alt = all(np.allclose(mul(mul(a, a), b), mul(a, mul(a, b))) for a, b in zip(rs[::3], rs[1::3]))
    norm = all(np.isclose(np.linalg.norm(mul(a, b)), np.linalg.norm(a) * np.linalg.norm(b)) for a, b in zip(rs[::3], rs[1::3]))
    return comm, assoc, alt, norm


P = {n: props(n) for n in (1, 2, 4, 8, 16)}
ok("R and C commute; H (4) does not -- ij = -ji", P[2][0] and not P[4][0])
ok("H is associative; O (8) is not -- but O is still 'alternative'", P[4][1] and not P[8][1] and P[8][2])
ok("|xy| = |x||y| holds through O and fails at 16", all(P[n][3] for n in (1, 2, 4, 8)) and not P[16][3])
e = np.eye(16)
pairs = list(itertools.combinations(range(1, 16), 2))
zero_div = next((f"(e{i} + e{j})(e{k} {'+' if t > 0 else '-'} e{l}) = 0" for (i, j) in pairs for (k, l) in pairs for t in (1, -1)
                 if np.allclose(mul(e[i] + e[j], e[k] + t * e[l]), 0)), None)
ok(f"the sedenions (16) have zero divisors: {zero_div}", zero_div is not None)
i2 = np.array([0.0, 1.0])
ok("the second floor is C: (0,1)^2 = -1", np.allclose(mul(i2, i2), [-1, 0]))


# =============================================================== 3. the symmetry tower
print("3 -- the symmetry tower: the Platonic rotation groups")


def rot(axis, ang):
    a = np.asarray(axis, float)
    a = a / np.linalg.norm(a)
    K = np.array([[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]])
    return np.eye(3) + np.sin(ang) * K + (1 - np.cos(ang)) * K @ K


def closure(gens):
    key = lambda M: tuple(np.round(M, 6).ravel())
    elems, frontier = {key(np.eye(3)): np.eye(3)}, [np.eye(3)]
    while frontier:
        new = []
        for A in frontier:
            for g in gens:
                if key(g @ A) not in elems:
                    elems[key(g @ A)] = g @ A
                    new.append(g @ A)
        frontier = new
    return list(elems.values())


def class_sizes(G):
    key = lambda M: tuple(np.round(M, 6).ravel())
    seen, sizes = set(), []
    for h in G:
        if key(h) in seen:
            continue
        cls = {key(g @ h @ g.T) for g in G}
        seen |= cls
        sizes.append(len(cls))
    return sorted(sizes)


def solvable_hint(sizes):
    """proper normal subgroups must be unions of classes (with the identity) whose size divides |G|"""
    n, others = sum(sizes), sizes[1:]
    return sorted({1 + sum(c) for r in range(1, len(others)) for c in itertools.combinations(others, r)
                   if n % (1 + sum(c)) == 0})


Tg = closure([rot([1, 1, 1], 2 * np.pi / 3), rot([0, 0, 1], np.pi)])
Og = closure([rot([0, 0, 1], np.pi / 2), rot([1, 1, 1], 2 * np.pi / 3)])
Ig = closure([rot([0, 1, PHI], 2 * np.pi / 5), rot([1, 1, 1], 2 * np.pi / 3)])
ok("rotation groups: tetrahedron 12, octahedron/cube 24, icosahedron/dodecahedron 60",
   [len(Tg), len(Og), len(Ig)] == [12, 24, 60])
ok(f"conjugacy classes: {class_sizes(Tg)} (A4), {class_sizes(Og)} (S4), {class_sizes(Ig)} (A5)",
   class_sizes(Tg) == [1, 3, 4, 4] and class_sizes(Og) == [1, 3, 6, 6, 8] and class_sizes(Ig) == [1, 12, 12, 15, 20])
ok(f"A4 and S4 have candidate normal subgroups {solvable_hint(class_sizes(Tg))}, {solvable_hint(class_sizes(Og))}",
   solvable_hint(class_sizes(Tg)) == [4] and solvable_hint(class_sizes(Og)) == [4, 12])
ok("A5 has none: no union of its classes with the identity divides 60 -- A5 is simple (the break at 5)",
   solvable_hint(class_sizes(Ig)) == [])


def R(q):
    """the rotation v -> q v q* of a unit quaternion"""
    Mv = lambda v: mul(mul(q, np.concatenate([[0], v])), conj(q))[1:]
    return np.column_stack([Mv(v) for v in np.eye(3)])


qs = [x / np.linalg.norm(x) for x in rng.normal(size=(20, 4))]
ok("every unit quaternion gives a rotation, and q and -q give the same one (the double cover)",
   all(np.allclose(R(q).T @ R(q), np.eye(3)) and np.isclose(np.linalg.det(R(q)), 1) and np.allclose(R(q), R(-q)) for q in qs))
ok("and multiplying quaternions composes the rotations: R(pq) = R(p)R(q)",
   all(np.allclose(R(mul(p, q)), R(p) @ R(q)) for p, q in zip(qs[::2], qs[1::2])))


# =============================================================== 4. the lattice tower
print("4 -- the lattice tower: from a centred shape to sphere packing")
box = np.array(list(itertools.product(range(-2, 3), repeat=3)), float)
fcc = np.array([p for p in itertools.product(range(-4, 5), repeat=3) if sum(p) % 2 == 0], float) / 2
lattices = {"simple cubic": (box, 1), "body-centred cubic": (np.vstack([box, box + 0.5]), 2),
            "face-centred cubic": (fcc, 4)}
dens, kiss = {}, {}
for nm, (L, per_cell) in lattices.items():
    d = np.linalg.norm(L, axis=1)
    dmin = d[d > 1e-9].min()
    kiss[nm] = int(np.isclose(d, dmin).sum())
    dens[nm] = float(per_cell * 4 / 3 * np.pi * (dmin / 2) ** 3)
ok(f"kissing numbers {list(kiss.values())} -- 6, 8, 12", list(kiss.values()) == [6, 8, 12])
ok(f"densities {[round(v, 4) for v in dens.values()]} = pi/6, pi*sqrt3/8, pi/sqrt18",
   np.allclose(list(dens.values()), [np.pi / 6, np.pi * np.sqrt(3) / 8, np.pi / np.sqrt(18)]))
e8 = [v for v in itertools.product((-1, 0, 1), repeat=8) if sum(map(abs, v)) == 2]
e8 += [v for v in itertools.product((-0.5, 0.5), repeat=8) if sum(x < 0 for x in v) % 2 == 0]
ok(f"E8 in 8 dimensions: {len(e8)} closest neighbours, all at the same distance",
   len(e8) == 240 and len({round(float(np.dot(v, v)), 9) for v in e8}) == 1)


# =============================================================== 5. the harmonic tower
print("5 -- the harmonic tower: from the tetrahedron's 1/3")
x0 = 1 / np.sqrt(3)
ok("the half-angle 54.74 deg (cos^2 = 1/3) is the zero of P2(x) = (3x^2 - 1)/2 -- the magic angle",
   abs((3 * x0 ** 2 - 1) / 2) < 1e-12 and abs(np.degrees(np.arccos(x0)) - 54.7356) < 1e-3)
xg, wg = np.polynomial.legendre.leggauss(20)
Pl = [np.polynomial.legendre.Legendre.basis(l)(xg) for l in range(6)]
gram = np.array([[np.sum(wg * a * b) for b in Pl] for a in Pl])
ok("the Legendre polynomials are orthogonal on [-1, 1] (norms 2/(2l+1))",
   np.allclose(gram, np.diag([2 / (2 * l + 1) for l in range(6)])))


def harmonic_dim(l):
    mons = [m for m in itertools.product(range(l + 1), repeat=3) if sum(m) == l]
    low = [m for m in itertools.product(range(l + 1), repeat=3) if sum(m) == l - 2]
    if l < 2:
        return len(mons)
    idx = {m: i for i, m in enumerate(low)}
    A = np.zeros((len(low), len(mons)))
    for j, (a, b, c) in enumerate(mons):
        for axis, (p, q, r) in enumerate(((a, b, c), (b, a, c), (c, a, b))):
            if p >= 2:
                t = [a, b, c]
                t[axis] -= 2
                A[idx[tuple(t)], j] += p * (p - 1)
    return int(len(mons) - np.linalg.matrix_rank(A))


ok(f"harmonic polynomials of degree l: {[harmonic_dim(l) for l in range(7)]} -- 2l + 1",
   [harmonic_dim(l) for l in range(7)] == [2 * l + 1 for l in range(7)])


# =============================================================== 6. the real-number tower
print("6 -- the real-number tower: from sqrt(2)")
fr, p, q = [], 1, 1
for _ in range(6):
    fr.append((p, q))
    p, q = p + 2 * q, p + q
ok(f"the best fractions for sqrt(2): {[f'{a}/{b}' for a, b in fr]}, each with p^2 - 2q^2 = +-1",
   fr == [(1, 1), (3, 2), (7, 5), (17, 12), (41, 29), (99, 70)] and all(abs(a * a - 2 * b * b) == 1 for a, b in fr))
ok("each is closer than 1/q^2 -- and none is exact", all(0 < abs(a / b - 2 ** 0.5) < 1 / b ** 2 for a, b in fr))


# =============================================================== 7. the growth tower
print("7 -- the growth tower: from e to the exponential map")


def expm(A, terms=60):
    out, term = np.eye(len(A)), np.eye(len(A))
    for k in range(1, terms):
        term = term @ A / k
        out = out + term
    return out


J = np.array([[0.0, -1.0], [1.0, 0.0]])
th = 0.7
ok("exp(theta J), with J the quarter-turn, is the rotation by theta -- e^(i theta) as a matrix",
   np.allclose(expm(th * J), [[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]]))
ok("exp of any 3x3 skew matrix is a rotation (the Lie algebra so(3) exponentiates onto rotations)",
   all(np.allclose((M := expm(S - S.T)).T @ M, np.eye(3)) and np.isclose(np.linalg.det(M), 1)
       for S in rng.normal(size=(10, 3, 3))))

print("\nALL [FORCED] FLOORS OF THE_TOWERS.md VERIFIED.")
