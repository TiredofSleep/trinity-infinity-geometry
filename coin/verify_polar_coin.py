"""verify_polar_coin.py -- checks every [FORCED] line of THE_POLAR_COIN.md
("The polar's coin: the cube, the octahedron and the round ball").

numpy + scipy (Qhull for convex hulls).  ASCII output.  Exit code 1 on any failure.
Run:  python verify_polar_coin.py      (about half a minute)
"""
import math
import sys
from itertools import permutations, product

import numpy as np
from scipy.optimize import minimize
from scipy.spatial import ConvexHull

FAILED = []
rng = np.random.default_rng(20261031)


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILED.append(label)


# ------------------------------------------------------------------ helpers
def polar(V):
    """Vertices of the polar {y : v.y <= 1 for every v in V}; the origin must be inside conv(V).

    Each facet a.x = b of conv(V) (b > 0) gives the polar corner a / b.  Qhull splits flat facets
    into simplices, so equal corners are merged."""
    h = ConvexHull(np.asarray(V, float))
    if (h.equations[:, -1] >= -1e-12).any():
        raise ValueError("origin not strictly inside")
    out = {}
    for eq in h.equations:
        p = eq[:-1] / -eq[-1]
        out.setdefault(tuple(np.round(p, 7)), p)
    return np.array(list(out.values()))


def corners(V):
    V = np.asarray(V, float)
    return V[ConvexHull(V).vertices]


def same_set(A, B, tol=1e-7):
    A, B = np.asarray(A, float), np.asarray(B, float)
    if A.shape != B.shape:
        return False
    D = np.linalg.norm(A[:, None, :] - B[None, :, :], axis=2)
    return bool((D.min(axis=1) < tol).all() and (D.min(axis=0) < tol).all())


def vol(V):
    return ConvexHull(np.asarray(V, float)).volume


def P(V):
    """The volume product |K| |K polar|, with the origin where it is."""
    return vol(V) * vol(polar(V))


def shape_key(V):
    """Sorted inner products of the corners scaled to radius 1: equal for congruent regular shapes."""
    U = np.asarray(V, float)
    U = U / np.linalg.norm(U, axis=1)[:, None]
    return np.sort((U @ U.T).ravel())


def ngon(n, r=1.0, turn=0.0):
    t = turn + 2 * np.pi * np.arange(n) / n
    return r * np.column_stack([np.cos(t), np.sin(t)])


def fvec3(V):
    """(corners, edges, faces) of a 3-dimensional polytope, edges by Euler's formula."""
    c, f = len(corners(V)), len(polar(V))
    return c, c + f - 2, f


phi = (1 + 5 ** 0.5) / 2
cube = np.array(list(product([-1, 1], repeat=3)), float)
octa = np.array([s * np.eye(3)[i] for i in range(3) for s in (1, -1)])
tet = cube[np.prod(cube, axis=1) > 0]          # the cube's even corners
tet2 = cube[np.prod(cube, axis=1) < 0]         # and its odd corners
cyc = lambda v: [v, (v[2], v[0], v[1]), (v[1], v[2], v[0])]
ico = np.array([w for a, b in product([-1, 1], repeat=2) for w in cyc((0, a, b * phi))], float)
dod = np.vstack([cube, np.array([w for a, b in product([-1, 1], repeat=2)
                                 for w in cyc((0, a / phi, b * phi))], float)])
solids = {"tetrahedron": tet, "cube": cube, "octahedron": octa, "icosahedron": ico, "dodecahedron": dod}


def random_body(d, k, symmetric=False):
    """k random points (and their negatives, if symmetric) around the origin; returns its corners."""
    while True:
        X = rng.normal(size=(k, d))
        X *= (0.5 + rng.random(k))[:, None] / np.linalg.norm(X, axis=1)[:, None]
        if symmetric:
            X = np.vstack([X, -X])
        try:
            h = ConvexHull(X)
        except Exception:
            continue
        if (h.equations[:, -1] < -1e-6).all():
            return X[h.vertices]


def best_origin_product(V):
    """min over z inside K of |K| |(K - z) polar|: the volume product at the Santalo point."""
    V = np.asarray(V, float)
    c0 = V.mean(axis=0)

    def f(z):
        try:
            return vol(polar(V - z))
        except ValueError:
            return 1e9
    r = minimize(f, c0, method="Nelder-Mead", options={"xatol": 1e-9, "fatol": 1e-12, "maxiter": 4000})
    return vol(V) * r.fun, r.x


# ------------------------------------------------------------------ 1. the coin
names = list(solids)
check("polarity is a flip: polar(polar(K)) = K for the five regular solids",
      all(same_set(polar(polar(solids[k])), corners(solids[k])) for k in names))
check("polar(polar(K)) = K for the regular polygons n = 3..12",
      all(same_set(polar(polar(ngon(n))), ngon(n)) for n in range(3, 13)))
rand2 = [random_body(2, 9) for _ in range(40)]
rand3 = [random_body(3, 14) for _ in range(40)]
check("polar(polar(K)) = K for 40 random polygons and 40 random polyhedra",
      all(same_set(polar(polar(K)), K, 1e-6) for K in rand2 + rand3))
check("a bigger shape has a smaller polar: polar(tK) = polar(K)/t (cube, t = 1/2, 2, 3), and inside "
      "the cube sits the octahedron, inside whose polar (the cube) sits the cube's polar (the octahedron)",
      all(same_set(polar(t * cube), polar(cube) / t) for t in (0.5, 2, 3)))
fv = {k: fvec3(solids[k]) for k in names}
check(f"faces and corners swap: tetrahedron {fv['tetrahedron']}, cube {fv['cube']} <-> octahedron "
      f"{fv['octahedron']}, icosahedron {fv['icosahedron']} <-> dodecahedron {fv['dodecahedron']}",
      fv["tetrahedron"] == (4, 6, 4) and fv["cube"] == (8, 12, 6) and fv["octahedron"] == (6, 12, 8)
      and fv["icosahedron"] == (12, 30, 20) and fv["dodecahedron"] == (20, 30, 12))

# ------------------------------------------------------------------ 2. the base's shapes on the coin
check("polar(cube [-1,1]^3) = the octahedron +-x, +-y, +-z, and polar(octahedron) = the cube",
      same_set(polar(cube), octa) and same_set(polar(octa), cube))
quarter = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
check("polar(the cube's even tetrahedron) = its odd tetrahedron, exactly; a quarter turn carries "
      "one onto the other (two sides of the same shape)",
      same_set(polar(tet), tet2) and same_set(tet @ quarter.T, tet2))
check("polar(icosahedron) is a regular dodecahedron and polar(dodecahedron) a regular icosahedron",
      np.allclose(shape_key(polar(ico)), shape_key(dod)) and np.allclose(shape_key(polar(dod)), shape_key(ico)))
check("in the plane every regular polygon is its own polar, turned by pi/n: for n = 3..12 the polar "
      "of the n-gon of radius 1 is the n-gon of inradius 1",
      all(same_set(polar(ngon(n)), ngon(n, 1 / math.cos(math.pi / n), math.pi / n)) for n in range(3, 13)))

# ------------------------------------------------------------------ 3. the measure
A_s = [rng.normal(size=(3, 3)) for _ in range(12)]
check("the volume product is unchanged by any linear map: P(AK) = P(K) for 12 random A, on the "
      "cube and on 12 random polyhedra",
      all(abs(P(cube @ A.T) - P(cube)) < 1e-8 * P(cube) for A in A_s)
      and all(abs(P(K @ A.T) - P(K)) < 1e-7 * P(K) for K, A in zip(rand3, A_s)))
Pn = [P(ngon(n)) for n in range(3, 13)]
check("regular n-gon: P = n^2 sin^2(pi/n): 27/4 (triangle), 8 (square), 9 (hexagon), rising with n",
      all(abs(p - n * n * math.sin(math.pi / n) ** 2) < 1e-9 for n, p in zip(range(3, 13), Pn))
      and abs(Pn[0] - 27 / 4) < 1e-9 and abs(Pn[1] - 8) < 1e-9 and abs(Pn[3] - 9) < 1e-9
      and all(a < b for a, b in zip(Pn, Pn[1:])))
p1000 = P(ngon(1000))
check(f"and toward the disk: P(1000-gon) = {p1000:.6f}, just below pi^2 = {math.pi ** 2:.6f}",
      0 < math.pi ** 2 - p1000 < 1e-4)


def icosphere(levels):
    V = list(ico / np.linalg.norm(ico[0]))
    for _ in range(levels):
        faces = ConvexHull(np.array(V)).simplices
        new = {tuple(np.round(v, 12)) for v in V}
        for f in faces:
            for i, j in ((0, 1), (1, 2), (0, 2)):
                m = np.array(V[f[i]]) + np.array(V[f[j]])
                new.add(tuple(np.round(m / np.linalg.norm(m), 12)))
        V = [np.array(v) for v in new]
    return np.array(V)


S642 = icosphere(3)
vals = {"tetrahedron": P(tet), "cube": P(cube), "octahedron": P(octa), "icosahedron": P(ico),
        "dodecahedron": P(dod), "sphere (642 corners)": P(S642)}
ball = (4 * math.pi / 3) ** 2
print("      volume products in space: " + ", ".join(f"{k} {v:.4f}" for k, v in vals.items())
      + f", ball {ball:.4f}")
check("in space: tetrahedron 64/9, cube = octahedron 32/3, icosahedron = dodecahedron, then a 642-corner "
      "sphere just under the ball's 16 pi^2/9: rounder is larger",
      len(S642) == 642 and abs(vals["tetrahedron"] - 64 / 9) < 1e-9
      and abs(vals["cube"] - 32 / 3) < 1e-9 and abs(vals["octahedron"] - 32 / 3) < 1e-9
      and abs(vals["icosahedron"] - vals["dodecahedron"]) < 1e-9
      and vals["tetrahedron"] < vals["cube"] < vals["icosahedron"] < vals["sphere (642 corners)"] < ball
      and ball - vals["sphere (642 corners)"] < 0.01 * ball)

# ------------------------------------------------------------------ 4. where the extremes sit
sym2 = [random_body(2, int(rng.integers(2, 9)), True) for _ in range(300)]
m2 = min(P(K) for K in sym2)
check(f"plane, 300 random symmetric polygons: least P = {m2:.4f} >= 8 (Mahler 1939)", m2 >= 8 - 1e-9)
tri = [rng.normal(size=(3, 2)) for _ in range(30)]
tri_vals = [P(T - T.mean(axis=0)) for T in tri]
check("every triangle, measured from its centre, has P = 27/4 exactly (30 random triangles)",
      max(abs(v - 27 / 4) for v in tri_vals) < 1e-8)
gen2 = [best_origin_product(random_body(2, int(rng.integers(3, 9))))[0] for _ in range(60)]
check(f"plane, 60 random polygons with the origin at the best point: least P = {min(gen2):.4f} >= 27/4",
      min(gen2) >= 27 / 4 - 1e-7)
sym3 = [random_body(3, int(rng.integers(3, 12)), True) for _ in range(300)]
m3 = min(P(K) for K in sym3)
check(f"space, 300 random symmetric polyhedra: least P = {m3:.4f} >= 32/3 (Iriyeh-Shibata 2020)",
      m3 >= 32 / 3 - 1e-9)
pert = []
for _ in range(100):
    half = cube[:4] + rng.normal(scale=0.03, size=(4, 3))
    pert.append(P(np.vstack([half, -half])))
check(f"100 small symmetric nudges of the cube: least P = {min(pert):.6f} > 32/3", min(pert) > 32 / 3)
tets = [rng.normal(size=(4, 3)) for _ in range(30)]
check("every tetrahedron, measured from its centre, has P = 64/9 exactly (30 random tetrahedra)",
      max(abs(P(T - T.mean(axis=0)) - 64 / 9) for T in tets) < 1e-7)
off = [vol(tet) * vol(polar(tet - z)) for z in rng.uniform(-0.3, 0.3, size=(50, 3))]
check(f"the tetrahedron's centre is its best origin: 50 off-centre origins all give more "
      f"(least {min(off):.4f} > 64/9)", min(off) > 64 / 9)
gen3 = [best_origin_product(random_body(3, int(rng.integers(4, 10))))[0] for _ in range(40)]
check(f"space, 40 random polyhedra with the origin at the best point: least P = {min(gen3):.4f} >= 64/9",
      min(gen3) >= 64 / 9 - 1e-6)

# ------------------------------------------------------------------ 5. four dimensions and up
cube4 = np.array(list(product([-1, 1], repeat=4)), float)
cross4 = np.array([s * np.eye(4)[i] for i in range(4) for s in (1, -1)])
prism = np.array([(*v, s) for v in octa for s in (1, -1)], float)                  # segment x octahedron
bipyr = np.vstack([np.column_stack([cube, np.zeros(8)]), [[0, 0, 0, 1], [0, 0, 0, -1]]])  # join of cube, segment
hanner = {"tesseract": cube4, "16-cell": cross4, "octahedral prism": prism, "cubic bipyramid": bipyr}
hv = {k: P(v) for k, v in hanner.items()}
check("four dimensions: polar(tesseract) = 16-cell and polar(octahedral prism) = cubic bipyramid, "
      "and all four have P = 32/3 = 4^4/4!",
      same_set(polar(cube4), cross4) and same_set(polar(prism), bipyr)
      and all(abs(v - 32 / 3) < 1e-9 for v in hv.values()))
c24 = np.array(sorted({p for v in product([-1, 0, 1], repeat=4) if sum(map(abs, v)) == 2
                       for p in permutations(v)}), float)
check("the 24-cell is its own polar, turned: polar(24-cell) is again a 24-cell",
      len(c24) == 24 and np.allclose(shape_key(polar(c24)), shape_key(c24)))
evenperm = [p for p in permutations(range(4))
            if sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j]) % 2 == 0]
c600 = {tuple(s * np.eye(4)[i]) for i in range(4) for s in (1, -1)}
c600 |= set(product([-0.5, 0.5], repeat=4))
for p in evenperm:
    for sg in product([-1, 1], repeat=3):
        base = (sg[0] * phi / 2, sg[1] * 0.5, sg[2] / (2 * phi), 0.0)
        c600.add(tuple(base[p[i]] for i in range(4)))
c600 = np.array(sorted(c600))
p600 = polar(c600)
check(f"the 600-cell ({len(c600)} corners) and its polar the 120-cell ({len(p600)} corners) are a pair "
      "of sides", len(c600) == 120 and len(p600) == 600 and len(polar(p600)) == 120)


def simplex(d):
    """The regular simplex in R^d, centred: the corners of R^(d+1)'s standard simplex, projected."""
    E = np.eye(d + 1) - 1 / (d + 1)
    Q, _ = np.linalg.qr(E.T)
    return E @ Q[:, :d]


s4, s5 = simplex(4), simplex(5)
check("the simplex is its own polar, turned, in 4 and 5 dimensions",
      np.allclose(shape_key(polar(s4)), shape_key(s4)) and np.allclose(shape_key(polar(s5)), shape_key(s5)))
cube5 = np.array(list(product([-1, 1], repeat=5)), float)
cross5 = np.array([s * np.eye(5)[i] for i in range(5) for s in (1, -1)])
check("five dimensions: polar(5-cube) = 5-cross-polytope, P = 4^5/5!",
      same_set(polar(cube5), cross5) and abs(P(cube5) - 4 ** 5 / 120) < 1e-9)

print("-" * 72)
if FAILED:
    print(f"{len(FAILED)} check(s) FAILED")
    sys.exit(1)
print("all checks passed")
