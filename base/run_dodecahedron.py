"""run_dodecahedron.py -- the run registered in ../THE_LENS.md, section 7 (commit 0a74851, 2026-11-07):
does the dodecahedron lose every energy contest, as the cube does?

THE REGISTERED RUN, in each of the seven contests of verify_symmetry_and_energy.py:
  - the dodecahedron's energy;
  - the lowest energy found from 200 random starts (for s = 12 and s = 40 each start is first spread out
    under Coulomb's law), and from 20 more starts that nudge the dodecahedron itself;
  - whether the dodecahedron is a saddle: whether some small move lowers its energy, once its three turns
    are set aside (the eigenvalues of the energy's second derivative on the sphere).
  Kill condition: the prediction dies if, in any of the seven contests, nothing below the dodecahedron
  is found.

BEYOND THE REGISTERED RUN (reported separately, not scored): the page names the weakest contests as the
place the prediction could fail, so the run also follows the Gaussians e^(-a r^2) from steep to weak, and
searches wherever the dodecahedron stops being a saddle.

numpy + scipy.  One process at below-normal priority.  ASCII output; also written to run_dodecahedron.log.
Run:  python run_dodecahedron.py      (several minutes)
"""
import ctypes
import math
import os
import sys
import time

import numpy as np
from scipy.optimize import minimize

try:                                                      # be gentle with the machine
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "run_dodecahedron.log"), "w", encoding="utf-8")
rng = np.random.default_rng(20261107)


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


# ------------------------------------------------------------------ the contests (as in verify_symmetry_and_energy.py)
def riesz(s):
    return (lambda t: t ** (-s / 2), lambda t: (-s / 2) * t ** (-s / 2 - 1))


def gauss(a):
    return (lambda t: np.exp(-a * t), lambda t: -a * np.exp(-a * t))


COULOMB = riesz(1)
PANEL = {"Riesz s=1 (Coulomb)": COULOMB, "Riesz s=3": riesz(3), "Riesz s=12": riesz(12),
         "Riesz s=40": riesz(40), "Gaussian a=1": gauss(1), "Gaussian a=4": gauss(4),
         "log": (lambda t: -0.5 * np.log(t), lambda t: -0.5 / t)}
STEEP = ("Riesz s=12", "Riesz s=40")


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
    gX = 2 * (dF[:, :, None] * D).sum(1)
    gX -= (gX * X).sum(1)[:, None] * X
    return F.sum() / 2, (gX / r[:, None]).ravel()


def unit(X):
    return X / np.linalg.norm(X, axis=1)[:, None]


def random_start(n, gap=0.25):
    while True:
        X = unit(rng.normal(size=(n, 3)))
        T = ((X[:, None] - X[None]) ** 2).sum(-1) + 9 * np.eye(n)
        if T.min() > gap * gap:
            return X


def relax(X0, pot, maxiter=20000):
    r = minimize(fun_grad, X0.ravel(), args=(len(X0), 3, pot), jac=True, method="L-BFGS-B",
                 options={"maxiter": maxiter, "maxcor": 30, "ftol": 1e-16, "gtol": 1e-12})
    X = unit(r.x.reshape(-1, 3))
    return energy(X, pot), X


def below(e, ref):
    return e < ref - 1e-9 * max(1.0, abs(ref))


# ------------------------------------------------------------------ the dodecahedron and its second derivative
PHI = (1 + 5 ** 0.5) / 2
corners = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
for p in (-1, 1):
    for q in (-1, 1):
        corners += [(0, p / PHI, q * PHI), (p / PHI, q * PHI, 0), (q * PHI, 0, p / PHI)]
DOD = unit(np.array(corners, float))
assert len(DOD) == 20
ANTI = [int(np.argmin(np.linalg.norm(DOD + x, axis=1))) for x in DOD]      # antipode of each corner


def tangent_basis(X):
    B = []
    for x in X:
        a = np.array([1.0, 0, 0]) if abs(x[0]) < 0.9 else np.array([0, 1.0, 0])
        e1 = a - (a @ x) * x
        e1 /= np.linalg.norm(e1)
        B.append((e1, np.cross(x, e1)))
    return B


BAS = tangent_basis(DOD)


def displaced(u, X=DOD, B=BAS):
    return X + np.array([u[2 * i] * B[i][0] + u[2 * i + 1] * B[i][1] for i in range(len(X))])


def grad_u(u, pot, X=DOD, B=BAS):
    n = len(X)
    _, g = fun_grad(displaced(u, X, B).ravel(), n, 3, pot)
    g = g.reshape(-1, 3)
    return np.array([[g[i] @ B[i][0], g[i] @ B[i][1]] for i in range(n)]).ravel()


def hessian(pot, X=DOD, B=BAS, h=1e-5):
    m = 2 * len(X)
    H = np.zeros((m, m))
    for k in range(m):
        e = np.zeros(m)
        e[k] = h
        H[:, k] = (grad_u(e, pot, X, B) - grad_u(-e, pot, X, B)) / (2 * h)
    return (H + H.T) / 2


def parity(vecs):
    """+1 if the modes are even under x -> -x, -1 if odd (average over an eigenspace)."""
    out = []
    for v in vecs.T:
        W = np.array([v[2 * i] * BAS[i][0] + v[2 * i + 1] * BAS[i][1] for i in range(20)])
        S = np.array([-W[ANTI[j]] for j in range(20)])            # inversion carries u at x to -u at -x
        out.append(float((S * W).sum() / (W * W).sum()))
    return float(np.mean(out))


def modes(pot):
    """lowest non-rotational eigenvalue of the second derivative, its multiplicity and parity."""
    H = hessian(pot)
    lam, V = np.linalg.eigh(H)
    scale = np.abs(lam).max()
    rot = np.abs(lam) < 1e-6 * scale
    keep = np.where(~rot)[0]
    low = lam[keep[0]]
    same = keep[np.abs(lam[keep] - low) < 1e-6 * scale]
    return low, len(same), parity(V[:, same]), int(rot.sum()), scale


NAMES = {3: "T", 4: "G", 5: "H"}

# ------------------------------------------------------------------ THE REGISTERED RUN
say("THE REGISTERED RUN (THE_LENS.md section 7, registered at commit 0a74851)")
say(f"dodecahedron: 20 corners on the unit sphere; nearest distance {np.sqrt(((DOD[0] - DOD[1:]) ** 2).sum(1)).min():.6f}")
results = {}
t_all = time.time()
for name, pot in PANEL.items():
    t0 = time.time()
    e_d = energy(DOD, pot)
    best_e, best_X = math.inf, None
    for _ in range(200):
        X0 = random_start(20)
        if name in STEEP:
            _, X0 = relax(X0, COULOMB, maxiter=3000)
        e, X = relax(X0, pot)
        if e < best_e:
            best_e, best_X = e, X
    nudge = math.inf
    for _ in range(20):
        e, X = relax(unit(DOD + 0.01 * rng.normal(size=DOD.shape)), pot)
        nudge = min(nudge, e)
        if e < best_e:
            best_e, best_X = e, X
    low, mult, par, nrot, scale = modes(pot)
    g0 = np.abs(grad_u(np.zeros(40), pot)).max()
    # a certificate that needs no search: a small step along the lowest mode
    H = hessian(pot)
    lam, V = np.linalg.eigh(H)
    v = V[:, np.where(np.abs(lam) >= 1e-6 * np.abs(lam).max())[0][0]]
    step = e_d
    for eps in (1e-2, 3e-3, 1e-3):
        step = min(step, energy(unit(displaced(eps * v)), pot))
    U = np.clip(best_X @ best_X.T, -1, 1)
    iu = np.triu_indices(20, 1)
    m = 1 + int((np.diff(np.sort(U[iu])) > 1e-7).sum())
    results[name] = (e_d, best_e, below(best_e, e_d), low < 0)
    say(f"\n[{name}]  ({time.time() - t0:.0f} s)")
    say(f"  dodecahedron energy         {e_d:.10f}   (largest force on a corner: {g0:.1e})")
    say(f"  lowest found (220 starts)   {best_e:.10f}   below the dodecahedron by {e_d - best_e:.6g}")
    say(f"  lowest from the 20 nudges   {nudge:.10f}")
    say(f"  lowest found has {m} distinct distances; closest pair {math.degrees(math.acos(U[iu].max())):.3f} deg")
    say(f"  second derivative at the dodecahedron: {nrot} turning modes; lowest other eigenvalue {low:.6g} "
        f"(x{mult}, {NAMES.get(mult, '?')}{'g' if par > 0.5 else 'u' if par < -0.5 else '?'})")
    say(f"  a small step along that mode: energy {step:.10f} ({'lower' if below(step, e_d) else 'NOT lower'})")
    say(f"  verdict in this contest: the dodecahedron {'LOSES' if below(best_e, e_d) else 'is NOT beaten'}")

say("\nTHOMSON CHECK: the best Coulomb energy found, against the published minimum for 20 points, 150.881568334")
say(f"  found {results['Riesz s=1 (Coulomb)'][1]:.9f}")
lost = sum(r[2] for r in results.values())
say(f"\nSCORE: the dodecahedron loses {lost} of 7 contests; it is a saddle in "
    f"{sum(r[3] for r in results.values())} of 7.")
say("PREDICTION " + ("HOLDS in all seven registered contests." if lost == 7 else "DIES: kill condition met."))
say(f"(registered run: {time.time() - t_all:.0f} s)")

# ------------------------------------------------------------------ BEYOND THE REGISTERED RUN
say("\nBEYOND THE REGISTERED RUN (not scored)")


def platonic():
    tet = unit(np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], float))
    octa = np.vstack([np.eye(3), -np.eye(3)])
    cube = unit(np.array([(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)], float))
    ico = []
    for p in (-1, 1):
        for q in (-1, 1):
            ico += [(0, p, q * PHI), (p, q * PHI, 0), (q * PHI, 0, p)]
    return {"tetrahedron": tet, "octahedron": octa, "cube": cube, "icosahedron": unit(np.array(ico, float)),
            "dodecahedron": DOD}


def edges(X):
    T = ((X[:, None] - X[None]) ** 2).sum(-1)
    t0 = T[np.triu_indices(len(X), 1)].min()
    return [(i, j) for i in range(len(X)) for j in range(i + 1, len(X)) if abs(T[i, j] - t0) < 1e-9]


def rigidity(X, B, E):
    """first-order change of each edge's squared length, per tangent move"""
    R = np.zeros((len(E), 2 * len(X)))
    for r, (i, j) in enumerate(E):
        d = X[i] - X[j]
        R[r, 2 * i:2 * i + 2] = [2 * d @ B[i][0], 2 * d @ B[i][1]]
        R[r, 2 * j:2 * j + 2] = [-2 * d @ B[j][0], -2 * d @ B[j][1]]
    return R


# 1. rigid and floppy: the five Platonic solids, their edge frameworks on the sphere, and all seven contests
say("\n1. The five Platonic solids: the edge framework's floppy moves (Maxwell's count, then the rank),")
say("   and the lowest non-turning eigenvalue of the energy's second derivative in each of the seven contests")
for name, X in platonic().items():
    B = tangent_basis(X)
    E = edges(X)
    R = rigidity(X, B, E)
    floppy = 2 * len(X) - 3 - np.linalg.matrix_rank(R, tol=1e-9)
    lows = []
    for pot in PANEL.values():
        H = hessian(pot, X, B)
        lam = np.linalg.eigvalsh(H)
        sc = np.abs(lam).max()
        lam = lam[np.abs(lam) >= 1e-6 * sc]
        lows.append(lam[0] / sc)
    signs = "".join("-" if v < 0 else "+" for v in lows)
    say(f"   {name:13s} V={len(X):2d} E={len(E):2d}  Maxwell 2V-3-E = {2 * len(X) - 3 - len(E):3d}, floppy moves = "
        f"{floppy}  | seven contests: {signs}  (- = a saddle, + = a local minimum)")

# 2. the dodecahedron's unstable family: is it floppy, and is it one block in every contest?
H1 = hessian(COULOMB)
lam1, V1 = np.linalg.eigh(H1)
sc1 = np.abs(lam1).max()
idx = np.where(np.abs(lam1) >= 1e-6 * sc1)[0][:3]
V3 = V1[:, idx]                                           # the 3-fold even family (one copy, so one block)
R = rigidity(DOD, BAS, edges(DOD))
say("\n2. The dodecahedron's unstable family (3 moves, even under x -> -x):")
say(f"   largest first-order change of an edge length along it: {np.abs(R @ V3).max():.1e} (0 = a floppy move)")
say("   in each contest: the second derivative on the family, and how far it is from one number times the identity")


def block(pot):
    H = hessian(pot)
    M = V3.T @ H @ V3
    lam_b = np.trace(M) / 3
    leak = np.linalg.norm(H @ V3 - V3 @ M) / np.linalg.norm(H)
    spread = np.linalg.norm(M - lam_b * np.eye(3)) / max(abs(lam_b), 1e-300)
    return lam_b, leak, spread


for name, pot in PANEL.items():
    lam_b, leak, spread = block(pot)
    say(f"   {name:20s} lambda = {lam_b: .6e}   leak {leak:.1e}   spread {spread:.1e}")

# 3. one number per potential: lambda(a) for the Gaussians e^(-a r^2), which generate every completely
#    monotone potential (Bernstein); if lambda(a) < 0 for every a > 0, the dodecahedron is a saddle in every
#    completely monotone contest
say("\n3. lambda(a) on that family for the Gaussians e^(-a r^2), steep to weak (double precision):")
neg = True
for a in np.geomspace(1000, 0.1, 41):
    lam_b, leak, spread = block(gauss(a))
    neg &= lam_b < 0
    say(f"   a = {a:10.4f}   lambda = {lam_b: .6e}   lambda / a^6 = {lam_b / a ** 6: .4e}   (leak {leak:.0e})")
say(f"   negative at every a computed: {neg}")

# 4. the weak end, where lambda is tiny: high precision, second difference along one move of the family
try:
    import mpmath as mp
    mp.mp.dps = 90
    phi = (1 + mp.sqrt(5)) / 2
    C = [(x, y, z) for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)]
    for p in (-1, 1):
        for q in (-1, 1):
            C += [(0, p / phi, q * phi), (p / phi, q * phi, 0), (q * phi, 0, p / phi)]
    Cm = [[mp.mpf(c) for c in v] for v in C]
    Cm = [[c / mp.sqrt(sum(cc * cc for cc in v)) for c in v] for v in Cm]
    order = [int(np.argmin(np.linalg.norm(DOD - np.array([float(c) for c in v]), axis=1))) for v in Cm]
    v = V3[:, 0] / np.linalg.norm(V3[:, 0])
    W = [[mp.mpf(float(v[2 * i])) * mp.mpf(float(BAS[i][0][k])) + mp.mpf(float(v[2 * i + 1])) *
          mp.mpf(float(BAS[i][1][k])) for k in range(3)] for i in range(20)]

    def E_mp(eps, a):
        P = []
        for n_, row in enumerate(Cm):
            w = W[order[n_]]
            y = [row[k] + eps * w[k] for k in range(3)]
            r = mp.sqrt(sum(c * c for c in y))
            P.append([c / r for c in y])
        tot = mp.mpf(0)
        for i in range(20):
            for j in range(i + 1, 20):
                t = sum((P[i][k] - P[j][k]) ** 2 for k in range(3))
                tot += mp.e ** (-a * t)
        return tot

    say("\n4. The weak end in high precision (90 digits): lambda(a) from a second difference along one move")
    eps = mp.mpf("1e-20")
    for a in ("0.3", "0.1", "0.03", "0.01", "0.003", "0.001"):
        am = mp.mpf(a)
        lam_b = (E_mp(eps, am) + E_mp(-eps, am) - 2 * E_mp(0, am)) / eps ** 2
        say(f"   a = {a:6s}  lambda = {mp.nstr(lam_b, 12):>20s}   lambda / a^6 = {mp.nstr(lam_b / am ** 6, 10)}")
except ImportError:
    say("\n4. (mpmath not installed: the high-precision weak end was skipped)")

# 5. the other completely monotone families in the panel's spirit, for completeness
say("\n5. lambda for the powers 1/r^s and the logarithm:")
for s in (0.25, 0.5, 1, 2, 3, 6, 12, 24, 40, 80):
    say(f"   s = {s:5}   lambda = {block(riesz(s))[0]: .6e}")
say(f"   log       lambda = {block(PANEL['log'])[0]: .6e}")
say(f"(total {time.time() - t_all:.0f} s)")
LOG.close()
