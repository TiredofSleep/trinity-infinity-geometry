"""verify_symmetry_and_energy.py -- checks every [FORCED] line of SYMMETRY_AND_ENERGY.md
("Symmetry and energy: when the most symmetric arrangement wins every contest").

numpy + scipy.  ASCII output.  Exit code 1 on any failure.
Run:  python verify_symmetry_and_energy.py      (about a minute)
"""
import math
import sys
from itertools import product

import numpy as np
from numpy.polynomial import chebyshev, legendre
from scipy.optimize import brentq, minimize, minimize_scalar

FAILED = []
rng = np.random.default_rng(31102026)


def check(label, ok):
    print(("PASS  " if ok else "FAIL  ") + label)
    if not ok:
        FAILED.append(label)


# ------------------------------------------------------------------ the contests
# A potential is a function f of the squared distance t, with its derivative.  Riesz 1/r^s and the
# Gaussians are completely monotone in t; the logarithm is their limit.
def riesz(s):
    return (lambda t: t ** (-s / 2), lambda t: (-s / 2) * t ** (-s / 2 - 1))


def gauss(a):
    return (lambda t: np.exp(-a * t), lambda t: -a * np.exp(-a * t))


PANEL = {"Riesz s=1 (Coulomb)": riesz(1), "Riesz s=3": riesz(3), "Riesz s=12": riesz(12),
         "Riesz s=40": riesz(40), "Gaussian a=1": gauss(1), "Gaussian a=4": gauss(4),
         "log": (lambda t: -0.5 * np.log(t), lambda t: -0.5 / t)}


def energy(X, pot):
    T = ((X[:, None, :] - X[None, :, :]) ** 2).sum(-1)
    return pot[0](T[np.triu_indices(len(X), 1)]).sum()


def fun_grad(y, n, d, pot):
    Y = y.reshape(n, d)
    r = np.linalg.norm(Y, axis=1)
    X = Y / r[:, None]
    D = X[:, None, :] - X[None, :, :]
    T = (D ** 2).sum(-1)
    np.fill_diagonal(T, 1.0)
    F, dF = pot[0](T), pot[1](T)
    np.fill_diagonal(F, 0.0)
    np.fill_diagonal(dF, 0.0)
    gX = 2 * (dF[:, :, None] * D).sum(1)                      # dE/dX
    gX -= (gX * X).sum(1)[:, None] * X                        # tangent part
    return F.sum() / 2, (gX / r[:, None]).ravel()


def spread_start(n, d, gap):
    while True:
        X = rng.normal(size=(n, d))
        X /= np.linalg.norm(X, axis=1)[:, None]
        T = ((X[:, None] - X[None]) ** 2).sum(-1) + 9 * np.eye(n)
        if T.min() > gap * gap:
            return X


def best(n, d, pot, starts, seeds=()):
    out = None
    inits = [spread_start(n, d, 0.5 if d == 3 else 0.3) for _ in range(starts)]
    inits += [S + 0.01 * rng.normal(size=S.shape) for S in seeds]
    for X0 in inits:
        r = minimize(fun_grad, X0.ravel(), args=(n, d, pot), jac=True, method="L-BFGS-B",
                     options={"maxiter": 20000, "maxcor": 30, "ftol": 1e-16, "gtol": 1e-12})
        X = r.x.reshape(n, d)
        X /= np.linalg.norm(X, axis=1)[:, None]
        e = energy(X, pot)
        if out is None or e < out[0]:
            out = (e, X)
    return out


def fingerprint(X):
    U = X @ X.T
    return np.sort(U[np.triu_indices(len(X), 1)])


def strength_and_distances(X, sphere=True):
    """(design strength t <= 12, number m of distinct inner products): sharp when t >= 2m - 1."""
    U = np.clip(X @ X.T, -1, 1)
    t = 0
    for k in range(1, 13):
        c = np.zeros(k + 1)
        c[k] = 1
        s = (legendre.legval(U, c) if sphere else chebyshev.chebval(U, c)).sum()
        if abs(s) > 1e-8 * len(X) ** 2:
            break
        t = k
    v = fingerprint(X)
    m = 1 + int((np.diff(v) > 1e-7).sum())
    return t, m


# ------------------------------------------------------------------ shapes
phi = (1 + 5 ** 0.5) / 2
cyc = lambda v: [v, (v[2], v[0], v[1]), (v[1], v[2], v[0])]
unit = lambda A: np.asarray(A, float) / np.linalg.norm(np.asarray(A, float), axis=1)[:, None]
cube = unit(list(product([-1, 1], repeat=3)))
shapes = {
    2: unit([[0, 0, 1], [0, 0, -1]]),
    3: unit([[math.cos(2 * math.pi * k / 3), math.sin(2 * math.pi * k / 3), 0] for k in range(3)]),
    4: cube[np.prod(np.sign(cube), axis=1) > 0],
    6: unit([s * np.eye(3)[i] for i in range(3) for s in (1, -1)]),
    12: unit([w for a, b in product([-1, 1], repeat=2) for w in cyc((0, a, b * phi))]),
}
dodeca = unit(np.vstack([np.array(list(product([-1, 1], repeat=3)), float),
                         [w for a, b in product([-1, 1], repeat=2) for w in cyc((0, a / phi, b * phi))]]))
tbp = unit([[0, 0, 1], [0, 0, -1]] + [[math.cos(2 * math.pi * k / 3), math.sin(2 * math.pi * k / 3), 0]
                                      for k in range(3)])


def ring(n, z=0.0, turn=0.0):
    rho = math.sqrt(1 - z * z)
    return np.array([[rho * math.cos(turn + 2 * math.pi * k / n), rho * math.sin(turn + 2 * math.pi * k / n), z]
                     for k in range(n)])


# ------------------------------------------------------------------ 1. the sharpness test
sharp = {n: strength_and_distances(X) for n, X in shapes.items()}
check("sharp (Cohn-Kumar's test, strength t >= 2m - 1): segment " + str(sharp[2]) + ", triangle "
      + str(sharp[3]) + ", tetrahedron " + str(sharp[4]) + ", octahedron " + str(sharp[6])
      + ", icosahedron " + str(sharp[12]) + "  [as (t, m)]",
      sharp == {2: (1, 1), 3: (1, 1), 4: (2, 1), 6: (3, 2), 12: (5, 3)})
ns = {"cube": strength_and_distances(cube), "dodecahedron": strength_and_distances(dodeca),
      "triangular bipyramid": strength_and_distances(tbp)}
check("not sharp: cube " + str(ns["cube"]) + ", dodecahedron " + str(ns["dodecahedron"])
      + ", triangular bipyramid " + str(ns["triangular bipyramid"]),
      ns == {"cube": (3, 3), "dodecahedron": (5, 5), "triangular bipyramid": (1, 3)})
circ = {n: strength_and_distances(ring(n)[:, :2], sphere=False) for n in range(2, 13)}
check("on the circle every regular n-gon is sharp: strength n - 1 with floor(n/2) distances (n = 2..12)",
      all(circ[n] == (n - 1, n // 2) for n in circ))

# ------------------------------------------------------------------ 2. the circle
ok_circle = True
for n in range(3, 10):
    reg = ring(n)[:, :2]
    for name, pot in PANEL.items():
        e, _ = best(n, 2, pot, 8)
        e0 = energy(reg, pot)
        ok_circle &= abs(e - e0) <= 1e-9 * max(1.0, abs(e0))
check("on the circle the regular n-gon wins every contest in the panel (n = 3..9; 7 potentials)", ok_circle)

# ------------------------------------------------------------------ 3. the sphere
winners = {}
for n in (2, 3, 4, 5, 6, 7, 8, 9, 12):
    winners[n] = {}
    prev = []
    for name, pot in PANEL.items():
        winners[n][name] = best(n, 3, pot, 12, seeds=prev)
        prev = [winners[n][name][1]]
thomson = {2: 0.5, 3: 1.732050808, 4: 3.674234614, 5: 6.474691495, 6: 9.985281374, 7: 14.452977414,
           8: 19.675287861, 9: 25.759986531, 12: 49.165253058}
check("the search reproduces the published Thomson (Coulomb) energies for n = 2..9 and 12",
      all(abs(winners[n]["Riesz s=1 (Coulomb)"][0] - e) < 2e-9 for n, e in thomson.items()))
check("the segment, triangle, tetrahedron, octahedron and icosahedron win every contest in the panel",
      all(abs(winners[n][k][0] - energy(shapes[n], PANEL[k])) <= 1e-9 * max(1.0, abs(winners[n][k][0]))
          for n in shapes for k in PANEL))
spread = {}
for n in (5, 7, 8, 9):
    F = [fingerprint(w[1]) for w in winners[n].values()]
    spread[n] = max(np.abs(a - b).max() for a in F for b in F)
print("      how far the winners differ across the panel: "
      + ", ".join(f"n={n}: {v:.3f}" for n, v in spread.items()))
check("at 5, 7, 8 and 9 the winner changes with the contest (no arrangement wins them all)",
      all(v > 1e-3 for v in spread.values()))
flat = {5: ring(5), 7: ring(7), 9: ring(9)}
check("the base's flat faces put on a great circle (pentagon, heptagon, nonagon) lose every contest",
      all(energy(X, PANEL[k]) > winners[n][k][0] + 1e-9 for n, X in flat.items() for k in PANEL))

# the cube and its twist
h = 1 / math.sqrt(3)


def twisted(psi):
    return np.vstack([ring(4, h, math.pi / 4), ring(4, -h, math.pi / 4 + psi)])


check("twisting one face of the cube is a 3-design all the way round (strength 3 at every twist)",
      all(strength_and_distances(twisted(p))[0] >= 3 for p in np.linspace(0, math.pi / 2, 13)))
grid = np.linspace(0, math.pi / 2, 91)
ok_twist = True
for name, pot in PANEL.items():
    E = np.array([energy(twisted(p), pot) for p in grid])
    ok_twist &= bool((E[1:-1] < E[0] - 1e-12).all() and abs(E[-1] - E[0]) < 1e-9 * abs(E[0])
                     and E[45] < E[0])
check("for every potential in the panel the cube (twist 0) is the worst of its twists, and the 45-degree "
      "twist (a square antiprism) beats it", ok_twist)
check("so the cube loses every contest in the panel: the best found is lower each time",
      all(winners[8][k][0] < energy(cube, PANEL[k]) - 1e-9 for k in PANEL))


def antiprism_best(pot):
    return minimize_scalar(lambda z: energy(np.vstack([ring(4, z), ring(4, -z, math.pi / 4)]), pot),
                           bounds=(0.05, 0.95), method="bounded", options={"xatol": 1e-12}).fun


check("the Coulomb winner at 8 is a square antiprism (its best height gives the same energy)",
      abs(antiprism_best(PANEL["Riesz s=1 (Coulomb)"]) - winners[8]["Riesz s=1 (Coulomb)"][0]) < 1e-9)


# the dodecahedron (the prediction registered in ../THE_LENS.md, section 7), and rigid against floppy
def tangent_basis(X):
    B = []
    for x in X:
        a = np.array([1.0, 0, 0]) if abs(x[0]) < 0.9 else np.array([0, 1.0, 0])
        e1 = a - (a @ x) * x
        e1 /= np.linalg.norm(e1)
        B.append((e1, np.cross(x, e1)))
    return B


def moved(X, B, u):
    return X + np.array([u[2 * i] * B[i][0] + u[2 * i + 1] * B[i][1] for i in range(len(X))])


def hess_sphere(X, pot, h=1e-5):
    """second derivative of the energy at X, for moves of the corners along the sphere"""
    B, n = tangent_basis(X), len(X)

    def g(u):
        _, gr = fun_grad(moved(X, B, u).ravel(), n, 3, pot)
        gr = gr.reshape(-1, 3)
        return np.array([[gr[i] @ B[i][0], gr[i] @ B[i][1]] for i in range(n)]).ravel()

    H = np.zeros((2 * n, 2 * n))
    for k in range(2 * n):
        e = np.zeros(2 * n)
        e[k] = h
        H[:, k] = (g(e) - g(-e)) / (2 * h)
    return (H + H.T) / 2


def edge_matrix(X, B):
    """first-order change of each edge's squared length, for each move along the sphere"""
    T = ((X[:, None] - X[None]) ** 2).sum(-1)
    t0 = T[np.triu_indices(len(X), 1)].min()
    E = [(i, j) for i in range(len(X)) for j in range(i + 1, len(X)) if abs(T[i, j] - t0) < 1e-9]
    R = np.zeros((len(E), 2 * len(X)))
    for r, (i, j) in enumerate(E):
        d = X[i] - X[j]
        R[r, 2 * i:2 * i + 2] = [2 * d @ B[i][0], 2 * d @ B[i][1]]
        R[r, 2 * j:2 * j + 2] = [-2 * d @ B[j][0], -2 * d @ B[j][1]]
    return R


def lowest_moves(H):
    """the lowest eigenvalue once the three turns (zero) are set aside, and its eigenvectors"""
    lam, V = np.linalg.eigh(H)
    sc = np.abs(lam).max()
    keep = np.where(np.abs(lam) >= 1e-6 * sc)[0]
    same = keep[np.abs(lam[keep] - lam[keep[0]]) < 1e-6 * sc]
    return lam[keep[0]], V[:, same]


solids = {"tetrahedron": shapes[4], "octahedron": shapes[6], "cube": cube, "icosahedron": shapes[12],
          "dodecahedron": dodeca}
n_flex, saddle = {}, {}
for name, X in solids.items():
    n_flex[name] = 2 * len(X) - 3 - np.linalg.matrix_rank(edge_matrix(X, tangent_basis(X)), tol=1e-9)
    saddle[name] = [lowest_moves(hess_sphere(X, pot))[0] < 0 for pot in PANEL.values()]
check("rigid against floppy: with bars along the edges and the corners kept on the sphere, the tetrahedron, "
      "octahedron and icosahedron cannot flex; the cube has 2 flexes and the dodecahedron 8",
      n_flex == {"tetrahedron": 0, "octahedron": 0, "cube": 2, "icosahedron": 0, "dodecahedron": 8})
check("... and the three rigid solids are local minima in all seven contests, while the two that flex are "
      "saddles in all seven", all(not any(v) for k, v in saddle.items() if n_flex[k] == 0)
      and all(all(v) for k, v in saddle.items() if n_flex[k] > 0))
Bc = tangent_basis(cube)
twist = np.array([[np.cross([0, 0, 1], x) @ Bc[i][0], np.cross([0, 0, 1], x) @ Bc[i][1]] if x[2] > 0 else [0.0, 0.0]
                  for i, x in enumerate(cube)]).ravel()
check("the cube's twist is one of its flexes: turning the top face keeps every edge's length to first order",
      np.abs(edge_matrix(cube, Bc) @ twist).max() < 1e-12)
Bd = tangent_basis(dodeca)
_, V3 = lowest_moves(hess_sphere(dodeca, PANEL["Riesz s=1 (Coulomb)"]))
check("the dodecahedron's unstable moves under Coulomb's law are a family of 3, and every one of them keeps "
      "every edge's length to first order: they are flexes",
      V3.shape[1] == 3 and np.abs(edge_matrix(dodeca, Bd) @ V3).max() < 1e-8)
block_ok, lams = True, []
for pot in PANEL.values():
    H = hess_sphere(dodeca, pot)
    M = V3.T @ H @ V3
    lam_b = np.trace(M) / 3
    block_ok &= bool(np.linalg.norm(H @ V3 - V3 @ M) < 1e-7 * np.linalg.norm(H)
                     and np.linalg.norm(M - lam_b * np.eye(3)) < 1e-6 * abs(lam_b))
    lams.append(lam_b)
check("in all seven contests that family is one block of the second derivative, a single number times the "
      "identity, and the number is negative", block_ok and all(v < 0 for v in lams))
check("so a small move along it lowers the dodecahedron's energy in every contest",
      all(min(energy(unit(moved(dodeca, Bd, s * 1e-3 * V3[:, 0])), pot) for s in (1, -1)) < energy(dodeca, pot)
          for pot in PANEL.values()))
gauss_lams = [np.trace(V3.T @ hess_sphere(dodeca, gauss(a)) @ V3) / 3 for a in (0.1, 0.3, 1, 3, 10, 30)]
check("[measured; the exact proof is verify_dodecahedron.py] the same number is negative for the Gaussians "
      "a = 0.1, 0.3, 1, 3, 10 and 30",
      all(v < 0 for v in gauss_lams))
best20 = math.inf
for _ in range(6):
    r = minimize(fun_grad, unit(rng.normal(size=(20, 3))).ravel(), args=(20, 3, PANEL["Riesz s=1 (Coulomb)"]),
                 jac=True, method="L-BFGS-B", options={"maxiter": 20000, "maxcor": 30, "ftol": 1e-16, "gtol": 1e-12})
    best20 = min(best20, energy(unit(r.x.reshape(20, 3)), PANEL["Riesz s=1 (Coulomb)"]))
check(f"under Coulomb's law a short search finds 20 points at {best20:.9f}, Thomson's published minimum "
      f"150.881568334, below the dodecahedron's {energy(dodeca, PANEL['Riesz s=1 (Coulomb)']):.9f}",
      abs(best20 - 150.881568334) < 2e-9)

# ------------------------------------------------------------------ 4. five points: the switch
def e_tbp(s):
    return 2 ** (-s) + 6 * 2 ** (-s / 2) + 3 * 3 ** (-s / 2)


def e_sp(s):
    def f(p):
        a, b = 2 - 2 * math.cos(p), 2 * math.sin(p) ** 2
        return 4 * a ** (-s / 2) + 4 * b ** (-s / 2) + 2 * (2 * b) ** (-s / 2)
    return minimize_scalar(f, bounds=(math.pi / 2 - 0.4, math.pi - 1e-3), method="bounded",
                           options={"xatol": 1e-14}).fun


s_star = brentq(lambda s: e_tbp(s) - e_sp(s), 14.5, 15.5, xtol=1e-13)
shin = 15.0480773927797
print(f"      five points: the bipyramid and the best square pyramid tie at s = {s_star:.10f}")
check(f"the five-point switch lands on Schwartz's constant 15.0480773927797 (|difference| < 1e-8)",
      abs(s_star - shin) < 1e-8)
check("below it the bipyramid wins (s = 1, 6, 15), above it the square pyramid (s = 15.1, 20, 40)",
      all(e_tbp(s) < e_sp(s) for s in (1, 6, 15)) and all(e_sp(s) < e_tbp(s) for s in (15.1, 20, 40)))


# ------------------------------------------------------------------ 5. lattices
def theta(B, a):
    """Sum over the lattice with basis rows B (zero vector included) of exp(-a |v|^2)."""
    d = B.shape[0]
    R2 = 46.0 / a
    K = int(math.ceil(math.sqrt(R2) / np.linalg.svd(B, compute_uv=False).min())) + 1
    r = np.arange(-K, K + 1)
    C = np.array(np.meshgrid(*([r] * d), indexing="ij")).reshape(d, -1).T
    n2 = ((C @ B) ** 2).sum(1)
    return float(np.exp(-a * n2[n2 <= R2]).sum())


def norms(B, R2):
    K = int(math.ceil(math.sqrt(R2) / np.linalg.svd(B, compute_uv=False).min())) + 1
    r = np.arange(-K, K + 1)
    C = np.array(np.meshgrid(*([r] * B.shape[0]), indexing="ij")).reshape(B.shape[0], -1).T
    n2 = ((C @ B) ** 2).sum(1)
    return np.sort(n2[(n2 <= R2) & (n2 > 1e-12)])


def dual(B):
    return np.linalg.inv(B).T


Z2 = np.eye(2)
A2 = math.sqrt(2 / math.sqrt(3)) * np.array([[1, 0], [0.5, math.sqrt(3) / 2]])
alphas2 = (0.3, 1, 2, math.pi, 5, 10)
check("the plane: the triangular and square lattices are each their own dual, so "
      "theta(a) = (pi/a) theta(pi^2/a) for both",
      all(abs(theta(L, a) - (math.pi / a) * theta(L, math.pi ** 2 / a)) < 1e-11 * theta(L, a)
          for L in (A2, Z2) for a in (0.7, 1.9, 4)))
check("the triangular lattice beats the square lattice in every Gaussian contest tried",
      all(theta(A2, a) < theta(Z2, a) for a in alphas2))
rand_l = []
for _ in range(200):
    x = rng.uniform(-0.5, 0.5)
    y = rng.uniform(math.sqrt(1 - x * x), 3)
    rand_l.append(np.array([[1, 0], [x, y]]) / math.sqrt(y))
check("and every one of 200 random lattices of the same density (a = 1, pi, 4)",
      all(theta(A2, a) <= theta(L, a) + 1e-12 for L in rand_l for a in (1, math.pi, 4)))

FCC = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], float) / 2 ** (1 / 3)
BCC = np.array([[-1, 1, 1], [1, -1, 1], [1, 1, -1]], float) / 4 ** (1 / 3)
Z3 = np.eye(3)
check("space: at equal density the dual of face-centred cubic is body-centred cubic (same lengths)",
      np.allclose(norms(dual(FCC), 12), norms(BCC, 12)) and abs(abs(np.linalg.det(FCC)) - 1) < 1e-12)
check("Poisson's coin: theta_FCC(a) = (pi/a)^(3/2) theta_BCC(pi^2/a) (a = 0.8, 1.7, 2.5, 6)",
      all(abs(theta(FCC, a) - (math.pi / a) ** 1.5 * theta(BCC, math.pi ** 2 / a)) < 1e-11 * theta(FCC, a)
          for a in (0.8, 1.7, 2.5, 6)))
tie = abs(theta(FCC, math.pi) - theta(BCC, math.pi))
check(f"so they tie on the coin's edge, a = pi (difference {tie:.1e})", tie < 1e-12)
check("face-centred cubic wins steeper contests (a = 3.3, 4, 6, 10), body-centred cubic gentler ones "
      "(a = 0.5, 1, 2, 3): no lattice wins them all",
      all(theta(FCC, a) < theta(BCC, a) for a in (3.3, 4, 6, 10))
      and all(theta(BCC, a) < theta(FCC, a) for a in (0.5, 1, 2, 3)))
check("the self-dual cubic lattice loses to both on the edge", theta(Z3, math.pi) > theta(FCC, math.pi))
shells = {k: int((norms(L, 3)[:30] < norms(L, 3)[0] + 1e-9).sum()) for k, L in
          (("FCC", FCC), ("BCC", BCC), ("Z3", Z3))}
check(f"nearest shells: FCC {shells['FCC']}, BCC {shells['BCC']}, simple cubic {shells['Z3']} "
      "(with the centre: 13, 9 and 7)", shells == {"FCC": 12, "BCC": 8, "Z3": 6})

print("-" * 72)
if FAILED:
    print(f"{len(FAILED)} check(s) FAILED")
    sys.exit(1)
print("all checks passed")
