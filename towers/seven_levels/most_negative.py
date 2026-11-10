"""most_negative.py -- round 2 of PREREG.md (registered at commit 5651c9d): the most Wigner-negative state of
three and of seven levels, found by search and compared up to the Clifford group's symmetry.

numpy + scipy.  One process at below-normal priority.  ASCII output; also written to most_negative.log.
Run:  python most_negative.py      (about a minute and a half; seeded, so a rerun repeats it)
"""
import ctypes
import math
import os
import sys
from collections import Counter

import numpy as np
from scipy.optimize import minimize

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "most_negative.log"), "w", encoding="utf-8")
rng = np.random.default_rng(20261107)
mp = np.linalg.matrix_power


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def setting(d):
    w = np.exp(2j * np.pi / d)
    X = np.roll(np.eye(d), 1, axis=0)
    Z = np.diag(w ** np.arange(d))
    F = np.array([[w ** (j * k) for k in range(d)] for j in range(d)]) / np.sqrt(d)
    P = np.zeros((d, d))
    for k in range(d):
        P[(-k) % d, k] = 1
    return w, X, Z, F, P


def wigner_ops(d):
    w, X, Z, F, P = setting(d)
    return np.array([mp(Z, p) @ mp(X, q) @ P @ (mp(Z, p) @ mp(X, q)).conj().T for q in range(d) for p in range(d)])


def wigner(psi, A, d):
    psi = psi / np.linalg.norm(psi)
    return np.real(np.einsum("i,nij,j->n", psi.conj(), A, psi)) / d


def negativity(psi, A, d):
    W = wigner(psi, A, d)
    return -W[W < 0].sum()


def search(d, starts):
    A = wigner_ops(d)
    out = []
    for _ in range(starts):
        x = rng.normal(size=2 * d)
        for _ in range(2):                                       # Powell, then once more from where it stopped
            r = minimize(lambda v: -negativity(v[:d] + 1j * v[d:], A, d), x, method="Powell",
                         options={"xtol": 1e-10, "ftol": 1e-13, "maxfev": 40000})
            x = r.x
        psi = (x[:d] + 1j * x[d:]) / np.linalg.norm(x[:d] + 1j * x[d:])
        out.append((negativity(psi, A, d), psi))
    out.sort(key=lambda t: -t[0])
    return out, A


def clifford(d):
    """the Clifford group of d levels, up to phase (d prime)"""
    w, X, Z, F, P = setting(d)
    T = np.diag([w ** ((pow(2, -1, d) * k * k) % d) for k in range(d)])
    g = next(a for a in range(2, d) if len({pow(a, e, d) for e in range(1, d)}) == d - 1)
    M = np.zeros((d, d))
    for k in range(d):
        M[(g * k) % d, k] = 1
    gens = [X, Z, F, T, M]

    def canon(U):
        flat = U.ravel()
        i = int(np.argmax(np.abs(flat) > 1e-6))
        return U / (flat[i] / abs(flat[i]))

    def key(U):
        return tuple(np.round(np.concatenate([U.real.ravel(), U.imag.ravel()]), 6))

    start = np.eye(d, dtype=complex)
    group = {key(start): start}
    frontier = [start]
    while frontier:
        new = []
        for U in frontier:
            for G in gens:
                V = canon(G @ U)
                k = key(V)
                if k not in group:
                    group[k] = V
                    new.append(V)
        frontier = new
    return np.array(list(group.values()))


def same_orbit(psi, ref, C, tol=1e-4):
    images = np.einsum("nij,j->ni", C, ref)
    return np.abs(images.conj() @ psi).max() > 1 - tol


def stabilizer(psi, C, tol=1e-4):
    images = np.einsum("nij,j->ni", C, psi)
    return C[np.abs(images.conj() @ psi) > 1 - tol]


def order_up_to_phase(U, limit=60):
    Q, n = U.copy(), 1
    while n <= limit:
        if abs(abs(np.trace(Q)) - U.shape[0]) < 1e-6:            # a multiple of the identity
            return n
        Q, n = Q @ U, n + 1
    return None


SCORES = {}

# ------------------------------------------------------------------ three levels (the calibration)
res3, A3 = search(3, 100)
best3 = res3[0][0]
strange = np.array([0, 1, -1], complex) / np.sqrt(2)
norrell = np.array([0, 1, 1], complex) / np.sqrt(2)                 # |N+> in Jain and Prakash (2020)
C3 = clifford(3)
say(f"three levels: {len(C3)} Clifford operations up to phase")
say(f"  best total negativity found from 100 starts: {best3:.9f}; the strange state {negativity(strange, A3, 3):.9f};"
    f" the Norrell state {negativity(norrell, A3, 3):.9f}")
say(f"  the best state is the strange state up to symmetry: {same_orbit(res3[0][1], strange, C3)}")
SCORES["R1"] = abs(best3 - 1 / 3) < 1e-6
say(f"R1 {'HELD' if SCORES['R1'] else 'DIED'}: the three-level maximum is {best3:.9f} (1/3 = {1 / 3:.9f})")

# ------------------------------------------------------------------ seven levels
res7, A7 = search(7, 400)
best7, psi7 = res7[0]
C7 = clifford(7)
say(f"\nseven levels: {len(C7)} Clifford operations up to phase")
top = [psi for v, psi in res7 if v > best7 - 1e-5]
say(f"  best total negativity from 400 starts: {best7:.9f}; {len(top)} starts came within 1e-5 of it")
say("  the twenty best values: " + ", ".join(f"{v:.6f}" for v, _ in res7[:20]))
orbit_ok = all(same_orbit(psi, psi7, C7) for psi in top)
SCORES["R2"] = orbit_ok
say(f"R2 {'HELD' if orbit_ok else 'DIED'}: all {len(top)} near-best states are the same up to symmetry: {orbit_ok}")
stab = stabilizer(psi7, C7)
orders = Counter(order_up_to_phase(U) for U in stab)
SCORES["R3"] = len(stab) > 1
say(f"R3 {'HELD' if SCORES['R3'] else 'DIED'}: the maximizer's symmetry group has {len(stab)} element(s) up to phase,"
    f" with orders {dict(sorted(orders.items(), key=lambda t: (t[0] is None, t[0])))}")
SCORES["R4"] = best7 < 0.75
say(f"R4 {'HELD' if SCORES['R4'] else 'DIED'}: the seven-level maximum found is {best7:.9f}")
W7 = wigner(psi7, A7, 7)
SCORES["R5"] = W7.min() > -1 / 7 + 1e-9
say(f"R5 {'HELD' if SCORES['R5'] else 'DIED'}: the maximizer's deepest Wigner value is {W7.min():.9f} "
    f"(-1/7 = {-1 / 7:.9f}); it has {int((W7 < -1e-12).sum())} negative points out of 49")
say("  its Wigner values, sorted: " + ", ".join(f"{x:+.5f}" for x in np.sort(W7)))
psi_show = psi7 * np.exp(-1j * np.angle(psi7[np.argmax(np.abs(psi7))]))
say("  the maximizer, amplitudes on |0>..|6> (8 decimals): "
    + ", ".join(f"{z.real:+.8f}{z.imag:+.8f}i" for z in np.round(psi_show, 8)))
legendre = np.array([0] + [1 if pow(k, 3, 7) == 1 else -1 for k in range(1, 7)], complex) / np.sqrt(6)
say(f"  for comparison: the Legendre state {negativity(legendre, A7, 7):.9f}; "
    f"its deepest value {wigner(legendre, A7, 7).min():.9f}")
say(f"\nROUND 2 SCORE: {sum(SCORES.values())} of {len(SCORES)} held: "
    + ", ".join(f"{k} {'held' if v else 'died'}" for k, v in SCORES.items()))

# ------------------------------------------------------------------ beyond the registered round (not scored)
say("\nBEYOND THE REGISTERED ROUND (not scored)")
w7, X7, Z7, F7, P7 = setting(7)
i0 = int(np.argmax(W7))
q0, p0 = divmod(i0, 7)
phi = (mp(Z7, p0) @ mp(X7, q0)).conj().T @ psi7
say(f"  the maximizer's +1/7 point is (q, p) = {(q0, p0)}; moved to the centre it is even under the half turn: "
    f"{np.allclose(P7 @ phi, phi, atol=1e-5)}")
for U4 in [U for U in stab if order_up_to_phase(U) == 4]:            # its two quarter turns, U and U^3
    views = [S_.conj().T @ psi7 for S_ in C7                          # seen through S, where U4 is S F S^-1
             if abs(abs(np.trace((S_ @ F7 @ S_.conj().T).conj().T @ U4)) - 7) < 1e-6]
    lams = [v.conj() @ F7 @ v for v in views]
    worst = max(np.linalg.norm(F7 @ v - l * v) for v, l in zip(views, lams))
    n_real = sum(bool(abs(np.sum(v * v)) > 1 - 1e-8) for v in views)  # |sum of squares| = 1: real up to phase
    say(f"  a quarter turn of its symmetry is the Fourier transform in {len(views)} Clifford frames; in each the state "
        f"is a Fourier eigenstate with eigenvalue {lams[0].real:+.6f}{lams[0].imag:+.6f}i (the same in all: "
        f"{all(abs(l - lams[0]) < 1e-6 for l in lams)}; largest residual {worst:.1e}); real up to phase in {n_real}")
ev, V = np.linalg.eig(F7)
for target in (1, -1, 1j, -1j):
    idx = [k for k in range(7) if abs(ev[k] - target) < 1e-6]
    Q, _ = np.linalg.qr(V[:, idx])
    k = len(idx)
    best_e, arg = 0.0, None
    for _ in range(200 if k > 1 else 1):
        r = minimize(lambda v: -negativity(Q @ (v[:k] + 1j * v[k:]), A7, 7), rng.normal(size=2 * k), method="Powell",
                     options={"xtol": 1e-11, "ftol": 1e-14, "maxfev": 20000})
        if -r.fun > best_e:
            best_e, arg = -r.fun, Q @ (r.x[:k] + 1j * r.x[k:])
    arg = arg / np.linalg.norm(arg)
    say(f"  the most negative state in the Fourier eigenspace {target} (dimension {k}): {best_e:.6f}, parity "
        f"{np.real(arg.conj() @ P7 @ arg):+.3f}, deepest value {wigner(arg, A7, 7).min():+.6f}")
st3 = int((np.abs(np.einsum("nij,j->ni", C3, strange).conj() @ strange) > 1 - 1e-6).sum())
no3 = int((np.abs(np.einsum("nij,j->ni", C3, norrell).conj() @ norrell) > 1 - 1e-6).sum())
say(f"  three levels: the strange and Norrell states both reach 1/3 and are not the same up to symmetry "
    f"({not same_orbit(norrell, strange, C3, tol=1e-6)}); their symmetry groups have {st3} and {no3} elements")
tops3 = [p for v, p in res3 if v > 1 / 3 - 1e-6]
n_st = sum(bool(same_orbit(p, strange, C3, tol=1e-6)) for p in tops3)
n_no = sum(bool(same_orbit(p, norrell, C3, tol=1e-6)) for p in tops3)
say(f"  three levels: {len(tops3)} of the 100 starts reached 1/3 within 1e-6: {n_st} at the strange state up to "
    f"symmetry, {n_no} at the Norrell state, {len(tops3) - n_st - n_no} elsewhere")
for name, s in (("strange", strange), ("Norrell", norrell)):
    say(f"  the {name} state's Wigner values times 9, sorted: "
        + ", ".join(f"{x:+.3f}" for x in np.sort(wigner(s, A3, 3)) * 9))
LOG.close()
