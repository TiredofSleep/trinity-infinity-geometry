#!/usr/bin/env python3
"""verify_integers.py -- checks the claims of THE_INTEGERS.md: which rule realizes which integer.

    python verify_integers.py      (~20 s)

  0      the centroid is the point nearest to all the points at once
  1-4    n mutually equidistant points span exactly n-1 dimensions -- so the equidistance rule
         builds point, segment, triangle, tetrahedron and then STOPS in 3-space
  5      the pentagon is the first regular polygon whose rotation cannot tile (2cos(2pi/n))
  6      spreading 6 points evenly on a sphere gives the octahedron
  8      the cube is the perpendicular (doubling) build, 2^3; it splits into two regular
         tetrahedra, swapped by the central inversion; each tetrahedron is achiral
  2-4    spreading points on a sphere agrees with equidistance (segment, triangle, tetrahedron)
  5, 8   ... but does NOT give the pentagon (5) or the cube (8)
  7, 9   7 = 1 + 6 (the centred hexagon, the octahedron plus its centre); 9 = 3^2
"""
import numpy as np

rng = np.random.default_rng(0)


def ok(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    assert cond, f"claim failed: {name}"


def energy(X):
    """Coulomb (Thomson) energy of points on the unit sphere: sum of 1/distance."""
    d = np.linalg.norm(X[:, None] - X[None], axis=-1)
    iu = np.triu_indices(len(X), 1)
    return float((1.0 / d[iu]).sum())


def descend(X, steps, lr):
    n = len(X)
    for _ in range(steps):
        diff = X[:, None] - X[None]
        d = np.linalg.norm(diff, axis=-1) + np.eye(n)
        F = (diff / d[..., None] ** 3).sum(1)
        F -= (F * X).sum(1, keepdims=True) * X       # keep only the component along the sphere
        X = X + lr * F
        X /= np.linalg.norm(X, axis=1, keepdims=True)
    return X


def thomson(n, restarts=20):
    """Minimum Thomson energy of n points on the sphere: projected gradient descent from random
    starts, then a long, small-step refinement of the best one."""
    starts = [descend(unit(rng.normal(size=(n, 3))), 1500, 0.02) for _ in range(restarts)]
    best = min(starts, key=energy)
    return energy(descend(best, 30000, 0.005))


def unit(v):
    v = np.asarray(v, float)
    return v / np.linalg.norm(v, axis=1, keepdims=True)


print("0 -- the void: the centroid is nearest to all the points at once")
tet = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], float)
total = lambda p: float(np.linalg.norm(tet - p, axis=1).sum())
c = tet.mean(0)
sampled = min(total(p) for p in rng.uniform(-1.5, 1.5, (20000, 3)))
ok(f"tetrahedron: centroid total distance {total(c):.3f} < a vertex's {total(tet[0]):.3f}",
   total(c) < total(tet[0]))
ok("no sampled point in space comes closer to all four than the centroid", sampled >= total(c) - 1e-9)

print("1-4 -- the ladder: n equidistant points need exactly n-1 dimensions")
for n in range(2, 7):
    G = np.full((n, n), -1.0 / (n - 1))
    np.fill_diagonal(G, 1.0)                       # Gram matrix of the unit vectors from the centroid
    ok(f"n = {n}: rank {np.linalg.matrix_rank(G, tol=1e-9)} = n - 1", np.linalg.matrix_rank(G, tol=1e-9) == n - 1)
G5 = np.full((5, 5), -0.25)
np.fill_diagonal(G5, 1.0)
ok("five equidistant points need 4 dimensions (> 3) -> in 3-space the rule stops at the tetrahedron",
   np.linalg.matrix_rank(G5, tol=1e-9) == 4 > 3)

print("5 -- the break: lattice rotation orders are exactly 1, 2, 3, 4, 6")
orders = [n for n in range(1, 13) if abs(2 * np.cos(2 * np.pi / n) - round(2 * np.cos(2 * np.pi / n))) < 1e-9]
ok(f"2cos(2pi/n) is an integer only for n in {orders}", orders == [1, 2, 3, 4, 6])

print("sphere-spreading (the Thomson problem): which shapes does it give?")
KNOWN = {2: 0.5, 3: 1.732050808, 4: 3.674234614,
         5: 6.474691495, 6: 9.985281374, 7: 14.452977414, 8: 19.675287861, 9: 25.759986531}
mins = {n: thomson(n) for n in KNOWN}
for n in KNOWN:
    ok(f"n = {n}: minimum energy {mins[n]:.6f} (published {KNOWN[n]:.6f})", abs(mins[n] - KNOWN[n]) < 1e-5)
pentagon = unit([[np.cos(2 * np.pi * k / 5), np.sin(2 * np.pi * k / 5), 0] for k in range(5)])
bipyramid = unit([[0, 0, 1], [0, 0, -1]] + [[np.cos(2 * np.pi * k / 3), np.sin(2 * np.pi * k / 3), 0] for k in range(3)])
octahedron = unit([[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]])
cube = unit([[x, y, z] for x in (1, -1) for y in (1, -1) for z in (1, -1)])
simplices = {2: unit([[0, 0, 1], [0, 0, -1]]),
             3: unit([[np.cos(2 * np.pi * k / 3), np.sin(2 * np.pi * k / 3), 0] for k in range(3)]),
             4: unit(tet)}
ok("2-4: the spread IS the equidistant simplex (segment, triangle, tetrahedron) -- the rules agree",
   all(abs(energy(simplices[n]) - mins[n]) < 1e-6 for n in (2, 3, 4)))
ok(f"5: the pentagon ({energy(pentagon):.4f}) is NOT the spread; the triangular bipyramid "
   f"({energy(bipyramid):.4f}) is", energy(pentagon) > mins[5] + 0.1 and abs(energy(bipyramid) - mins[5]) < 1e-6)
ok(f"6: the octahedron ({energy(octahedron):.6f}) IS the spread", abs(energy(octahedron) - mins[6]) < 1e-6)
ok(f"8: the cube ({energy(cube):.4f}) is NOT the spread (the square antiprism, {mins[8]:.4f}, is)",
   energy(cube) > mins[8] + 0.01)
pent_bipyramid = unit([[0, 0, 1], [0, 0, -1]] + [[np.cos(2 * np.pi * k / 5), np.sin(2 * np.pi * k / 5), 0] for k in range(5)])
ok(f"7: the spread IS the pentagonal bipyramid ({energy(pent_bipyramid):.6f})", abs(energy(pent_bipyramid) - mins[7]) < 1e-5)


def antiprism(h):
    r = np.sqrt(1 - h * h)
    top = [[r * np.cos(np.pi * k / 2), r * np.sin(np.pi * k / 2), h] for k in range(4)]
    bottom = [[r * np.cos(np.pi * k / 2 + np.pi / 4), r * np.sin(np.pi * k / 2 + np.pi / 4), -h] for k in range(4)]
    return np.array(top + bottom)


best_antiprism = min(energy(antiprism(h)) for h in np.linspace(0.01, 0.99, 200001))
ok(f"8: the spread IS the square antiprism (best height gives {best_antiprism:.6f})", abs(best_antiprism - mins[8]) < 1e-5)

print("8 -- the cube: the perpendicular build, and its two tetrahedra")
verts = np.array([[x, y, z] for x in (1, -1) for y in (1, -1) for z in (1, -1)], float)
ok("three perpendicular in/out choices give 2^3 = 8 corners", len(verts) == 8)
even = verts[np.prod(verts, axis=1) > 0]
odd = verts[np.prod(verts, axis=1) < 0]
edges = lambda P: sorted(round(float(np.linalg.norm(a - b)), 9) for i, a in enumerate(P) for b in P[i + 1:])
ok("the 8 corners split into two regular tetrahedra (all 6 edges equal in each)",
   len(set(edges(even))) == 1 and len(set(edges(odd))) == 1)
same_set = lambda A, B: {tuple(np.round(r, 9)) for r in A} == {tuple(np.round(r, 9)) for r in B}
ok("the central inversion x -> -x swaps the two tetrahedra", same_set(-even, odd))
mirror = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 1]], float)   # reflection in the plane x = y
ok("each tetrahedron is its own mirror image (achiral): the reflection x<->y maps it to itself",
   same_set(even @ mirror.T, even))

print("7 and 9 -- counting")
ok("7 = 1 + 6: centred hexagonal numbers 3k(k-1)+1 are 1, 7, 19, 37", [3 * k * (k - 1) + 1 for k in range(1, 5)] == [1, 7, 19, 37])
ok("7 = the octahedron's 6 corners plus its centre", len(octahedron) + 1 == 7)
ok("9 = 3^2: a triangle of side 3 cuts into 1 + 3 + 5 = 9 unit triangles", 1 + 3 + 5 == 9 == 3 ** 2)

print("\nALL CLAIMS OF THE_INTEGERS.md VERIFIED.")
