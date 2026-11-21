"""prepare.py -- candidate maximizers for bb.c (floating point; bb.c certifies everything it uses).

For a small odd prime p: find the maximum of S = sum |W| over diagonal states numerically (L-BFGS from many starts,
then Newton's method with the signs of E fixed), map the maximizer through every symmetry of S (an affine map
x -> alpha x + t of F_p, complex conjugation, a Clifford phase (2 pi/p)(beta x + gamma x^2), multiples of 2 pi) into
the box D = [-pi/p, pi/p]^2 x [0, 2 pi]^(p-3), keep the distinct images, and write each with the symmetry that
produced it (bb.c re-checks the symmetry in interval arithmetic).  Nothing here is part of the proof except as input.

Usage: python prepare.py P [RHO]   -> candidates_P.txt, prepare_P.log
"""
import math
import os
import struct
import sys

import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
P = int(sys.argv[1])
RHO = float(sys.argv[2]) if len(sys.argv) > 2 else {3: 0.02, 5: 0.004, 7: 0.004}[P]
EPSK = 1e-9
NU, DIM = (P - 1) // 2, P - 1
Q = np.arange(P)
U = np.arange(1, NU + 1)
AI = (Q[:, None] + U[None, :]) % P
BI = (Q[:, None] - U[None, :]) % P
SH = 4 * np.pi * np.outer(np.arange(P), U) / P
LOG = open(os.path.join(HERE, f"prepare_{P}.log"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")


def parts(x):
    phi = np.concatenate([[0.0], x])
    ang = (phi[AI] - phi[BI])[:, None, :] - SH[None, :, :]
    return ang, 1 + 2 * np.cos(ang).sum(axis=2)


def S(x):
    return np.abs(parts(x)[1]).sum() / P ** 2


def grad(x):
    ang, E = parts(x)
    t = (np.sign(E)[:, :, None] * np.sin(ang)).sum(axis=1)
    g = np.zeros(P)
    np.add.at(g, AI.ravel(), (-2 * t).ravel())
    np.add.at(g, BI.ravel(), (2 * t).ravel())
    return g[1:] / P ** 2


def hess(x):
    ang, E = parts(x)
    H = np.zeros((P, P))
    for q in range(P):
        for s in range(P):
            for ui in range(NU):
                cv = -2 * np.sign(E[q, s]) * np.cos(ang[q, s, ui])
                a, b = AI[q, ui], BI[q, ui]
                H[a, a] += cv
                H[b, b] += cv
                H[a, b] -= cv
                H[b, a] -= cv
    return H[1:, 1:] / P ** 2


def normalize(psi):
    """psi: length p with psi[0] = 0 -> (point of D, k, n) with point_x = psi_x + 2 pi k_x/p + 2 pi n_x"""
    r1, r2 = round(psi[1] * P / (2 * math.pi)), round(psi[2] * P / (2 * math.pi))
    inv2 = (P + 1) // 2
    gamma = ((2 * r1 - r2) * inv2) % P
    beta = (-r1 - gamma) % P
    k = [(beta * x + gamma * x * x) % P for x in range(1, P)]
    v = [psi[x] + 2 * math.pi * k[x - 1] / P for x in range(1, P)]
    n = [(-round(v[i] / (2 * math.pi))) if i < 2 else (-math.floor(v[i] / (2 * math.pi))) for i in range(DIM)]
    pt = [v[i] + 2 * math.pi * n[i] for i in range(DIM)]
    return pt, k, n


def bits(d):
    return struct.unpack("<Q", struct.pack("<d", d))[0]


rng = np.random.default_rng(20261121 + P)
best, bx = -1.0, None
for _ in range(400):
    r = minimize(lambda z: -S(z), rng.uniform(0, 2 * np.pi, DIM), jac=lambda z: -grad(z), method="L-BFGS-B",
                 options={"maxiter": 4000, "gtol": 1e-13})
    if -r.fun > best:
        best, bx = -r.fun, r.x
for _ in range(30):                                   # Newton with the signs fixed
    step = np.linalg.solve(hess(bx), grad(bx))
    bx = bx - step
    if np.abs(step).max() < 1e-16:
        break
phi0, _, _ = normalize(np.concatenate([[0.0], bx]))
phi0 = np.array(phi0)
ang, E = parts(phi0)
say(f"p = {P}: numerical maximum S = {S(phi0):.15f} at {np.round(phi0, 12).tolist()}; |grad| = {np.abs(grad(phi0)).max():.1e}; "
    f"min |E| = {np.abs(E).min():.4f}; Hessian eigenvalues {np.round(np.linalg.eigvalsh(hess(phi0)), 4).tolist()}")
full0 = np.concatenate([[0.0], phi0])
cands = []
for eps in (1, -1):
    for alpha in range(1, P):
        for t in range(P):
            psi = [eps * (full0[(alpha * x + t) % P] - full0[t]) for x in range(P)]
            pt, k, n = normalize(psi)
            if all(np.abs(np.array(pt) - np.array(c[0])).max() > 1e-7 for c in cands):
                cands.append((pt, eps, alpha, t, k, n))
vals = [S(np.array(c[0])) for c in cands]
say(f"symmetry images in D: {len(cands)} distinct points (from {2 * (P - 1) * P} maps); S at each agrees to "
    f"{max(abs(v - vals[0]) for v in vals):.1e}; largest |grad| {max(np.abs(grad(np.array(c[0]))).max() for c in cands):.1e}")
assert cands[0][1:4] == (1, 1, 0) and all(v == 0 for v in cands[0][4] + cands[0][5])
with open(os.path.join(HERE, f"candidates_{P}.txt"), "w") as f:
    f.write(f"P {P}\nRHO {bits(RHO):016x}\nEPS {bits(EPSK):016x}\nNCAND {len(cands)}\n")
    for pt, eps, alpha, t, k, n in cands:
        f.write(" ".join(f"{bits(v):016x}" for v in pt) + f" {eps} {alpha} {t} " + " ".join(map(str, k)) + " "
                + " ".join(map(str, n)) + "\n")
say(f"wrote candidates_{P}.txt (certified half-width {RHO}, Krawczyk half-width {EPSK})")
LOG.close()
