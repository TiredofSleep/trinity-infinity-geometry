"""verify_circle_operator.py -- the circle operator S_C = sum over a circle of phase-point operators stays inside
the square-root limit |lambda| <= 2 sqrt(p), as Gurevich and Hadani's Theorem 4.2 implies (CIRCLE_OPERATOR.md).

Conventions are TORUS_MOMENTS.md section 1: <a|A_(q,k)|b> = [a + b = 2q] w^(k (a - b)), w = exp(2 pi i/p). A circle is
C = {(q, k) : q^2 - d k^2 = c}, d the least quadratic non-residue, c != 0; it has p + 1 points.

Checks:
  C1. S_C is Hermitian with trace p + 1, for every prime 5 <= p <= 397 and c = 1, 2, 3; the lens handoff's convention
      (w^(2k(x - q)), i.e. k -> -k) gives the same matrix, because circles are symmetric under k -> -k.
  C2. Every eigenvalue satisfies |lambda| < 2 sqrt(p): p <= 397 with c = 1, 2, 3, and p <= 997 with c = 1.
  C3. For p = 11, 31, 101, each eigenvector psi of S_C has the same expectation <psi|A_v|psi> at every point v of C,
      and lambda = (p + 1) <psi|A_v|psi> (the eigenvectors are the torus's eigenstates, and the torus moves v around C).
  C4. At p = 251 the 2nd, 4th and 6th moments of lambda/sqrt(p) are near the semicircle's 1, 2, 5 (TORUS_MOMENTS.md).
Usage: python verify_circle_operator.py   (about a minute)  -> verify_circle_operator.log
"""
import math
import os
import sys

import numpy as np
from sympy import legendre_symbol, primerange

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "verify_circle_operator.log"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def circle(p, c):
    d = next(a for a in range(2, p) if legendre_symbol(a, p) == -1)
    return [(q, k) for q in range(p) for k in range(p) if (q * q - d * k * k - c) % p == 0]


def point_op(p, q, k, sign=1):
    A = np.zeros((p, p), complex)
    for b in range(p):
        a = (2 * q - b) % p
        A[a, b] = np.exp(2j * np.pi * (sign * k * (a - b) % p) / p)
    return A


def S_C(p, c, sign=1):
    S = np.zeros((p, p), complex)
    x = np.arange(p)
    for q, k in circle(p, c):
        a = (2 * q - x) % p
        S[a, x] += np.exp(2j * np.pi * ((sign * k * (a - x)) % p) / p)
    return S


ok_all = True
say("verify_circle_operator.py -- the circle operator and the square-root limit")
bad, worst, worst_at, n_ops = 0, 0.0, None, 0
for p in primerange(5, 398):
    for c in (1, 2, 3):
        S = S_C(p, c)
        C = circle(p, c)
        if len(C) != p + 1 or not np.allclose(S, S.conj().T) or abs(np.trace(S).real - (p + 1)) > 1e-9:
            bad += 1
        if not np.allclose(S, S_C(p, c, sign=-1)):
            bad += 1
        r = np.abs(np.linalg.eigvalsh(S)).max() / (2 * math.sqrt(p))
        n_ops += 1
        if r > worst:
            worst, worst_at = r, (p, c)
ok = bad == 0
ok_all &= ok
say(f"[{'PASS' if ok else 'FAIL'}] C1: {n_ops} operators (5 <= p <= 397, c = 1, 2, 3) are Hermitian with trace p + 1, "
    f"and the handoff's convention gives the same matrices ({bad} failures)")
over = 0
for p in primerange(398, 998):
    r = np.abs(np.linalg.eigvalsh(S_C(p, 1))).max() / (2 * math.sqrt(p))
    if r > worst:
        worst, worst_at = r, (p, 1)
    over += r >= 1
ok = worst < 1
ok_all &= ok
say(f"[{'PASS' if ok else 'FAIL'}] C2: every eigenvalue has |lambda| < 2 sqrt(p) (p <= 397 with c = 1, 2, 3; p <= 997 "
    f"with c = 1); the largest ratio |lambda| / (2 sqrt p) is {worst:.5f}, at p = {worst_at[0]}, c = {worst_at[1]}")
spread = 0.0
for p in (11, 31, 101):
    S = S_C(p, 1)
    lam, V = np.linalg.eigh(S)
    C = circle(p, 1)
    for j in range(p):
        psi = V[:, j]
        vals = np.array([np.vdot(psi, point_op(p, q, k) @ psi).real for q, k in C])
        spread = max(spread, np.abs(vals - vals[0]).max(), abs((p + 1) * vals[0] - lam[j]))
ok = spread < 1e-9
ok_all &= ok
say(f"[{'PASS' if ok else 'FAIL'}] C3: at p = 11, 31, 101 every eigenvector has one expectation at all p + 1 points of "
    f"the circle, and lambda = (p + 1) <psi|A_v|psi> (largest deviation {spread:.1e})")
lam = np.linalg.eigvalsh(S_C(251, 1)) / math.sqrt(251)
m = [float((lam ** k).mean()) for k in (2, 4, 6)]
ok = abs(m[0] - 1) < 0.02 and abs(m[1] - 2) < 0.05 and abs(m[2] - 5) < 0.2
ok_all &= ok
say(f"[{'PASS' if ok else 'FAIL'}] C4: at p = 251 the moments 2, 4, 6 of lambda/sqrt(p) are {m[0]:.3f}, {m[1]:.3f}, "
    f"{m[2]:.3f} (semicircle 1, 2, 5)")
say(f"[{'PASS' if ok_all else 'FAIL'}] verify_circle_operator: all checks")
LOG.close()
sys.exit(0 if ok_all else 1)
