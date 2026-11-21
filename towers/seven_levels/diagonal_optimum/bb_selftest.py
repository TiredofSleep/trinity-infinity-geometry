"""bb_selftest.py -- checks of bb3/bb5/bb7.exe (the generalized prover) against floating-point S.

Not part of the proof; it looks for mistakes in the generalization of t7_rigorous.c (indexing by p, the lower bound L,
the flags).  For each p in 3, 5, 7: 2000 random boxes (sizes from the first grid down to 1e-7, many near the maximizers);
for each, the rigorous upper bound U must lie above S, and the lower bound L below S, at 64 sampled points; where the
program reports S smooth and monotone, the sampled gradients must have one fixed sign in some coordinate.  At p = 7 the
bounds must agree with ../t7_rigorous/t7_rigorous.exe on the same boxes when that program has been built.

Usage: python bb_selftest.py   -> bb_selftest.log
"""
import math
import os
import random
import struct
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = open(os.path.join(HERE, "bb_selftest.log"), "w", encoding="utf-8")
rng = random.Random(20261121)


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def b(d):
    return struct.unpack("<Q", struct.pack("<d", d))[0]


def d(h):
    return struct.unpack("<d", struct.pack("<Q", int(h, 16)))[0]


def model(P):
    NU = (P - 1) // 2
    Q, U = np.arange(P), np.arange(1, NU + 1)
    AI, BI = (Q[:, None] + U[None, :]) % P, (Q[:, None] - U[None, :]) % P
    SH = 4 * np.pi * np.outer(np.arange(P), U) / P

    def S_and_grad(X):                       # X: (n, p-1)
        phi = np.concatenate([np.zeros((X.shape[0], 1)), X], axis=1)
        ang = (phi[:, AI] - phi[:, BI])[:, :, None, :] - SH[None, None, :, :]
        E = 1 + 2 * np.cos(ang).sum(axis=3)
        S = np.abs(E).sum(axis=(1, 2)) / P ** 2
        t = (np.sign(E)[:, :, :, None] * np.sin(ang)).sum(axis=2)        # (n, q, u)
        g = np.zeros((X.shape[0], P))
        for q in range(P):
            for ui in range(NU):
                g[:, AI[q, ui]] += -2 * t[:, q, ui]
                g[:, BI[q, ui]] += 2 * t[:, q, ui]
        return S, g[:, 1:] / P ** 2
    return S_and_grad


def candidates(P):
    lines = open(os.path.join(HERE, f"candidates_{P}.txt")).read().split("\n")
    n = int(lines[3].split()[1])
    return [np.array([d(h) for h in lines[4 + i].split()[:P - 1]]) for i in range(n)]


def run(exe, boxes):
    fin, fout = os.path.join(HERE, "_bt_in.txt"), os.path.join(HERE, "_bt_out.txt")
    open(fin, "w").write("\n".join(" ".join(f"{b(v):016x}" for v in list(lo) + list(hi)) for lo, hi in boxes) + "\n")
    subprocess.run([exe, "boxtest", fin, fout], check=True)
    out = [x.split() for x in open(fout).read().split("\n") if x.strip()]
    os.remove(fin)
    os.remove(fout)
    return out


def test(P):
    DIM = P - 1
    S_and_grad = model(P)
    lo_d = np.array([-math.pi / P] * min(2, DIM) + [0.0] * (DIM - 2))
    hi_d = np.array([math.pi / P] * min(2, DIM) + [2 * math.pi] * (DIM - 2))
    cands = candidates(P) if os.path.exists(os.path.join(HERE, f"candidates_{P}.txt")) else []
    boxes = []
    for i in range(2000):
        if i % 2 == 0 or not cands:
            h = np.array([rng.choice([math.pi / 8, 0.3, 0.05, 0.01, 1e-3, 1e-5, 1e-7])] * DIM) * \
                np.array([rng.uniform(0.5, 1.0) for _ in range(DIM)])
            cen = np.array([rng.uniform(lo_d[j], hi_d[j]) for j in range(DIM)])
        else:
            h = np.array([rng.choice([0.02, 4e-3, 1e-3, 1e-4, 1e-6])] * DIM) * np.array([rng.uniform(0.5, 1.0) for _ in range(DIM)])
            cen = cands[i % len(cands)] + np.array([rng.uniform(-0.01, 0.01) for _ in range(DIM)])
        boxes.append((cen - h, cen + h))
    out = run(os.path.join(HERE, f"bb{P}.exe"), boxes)
    bad_u = bad_l = bad_mono = fails = n_mono = n_smooth = 0
    for (lo, hi), row in zip(boxes, out):
        U, L, sm, mo, fl = d(row[0]), d(row[1]), int(row[2]), int(row[3]), int(row[4])
        fails += fl
        n_mono += mo
        n_smooth += sm
        X = lo + (hi - lo) * np.array([[rng.random() for _ in range(DIM)] for _ in range(64)])
        S, g = S_and_grad(X)
        if S.max() > U + 1e-12:
            bad_u += 1
        if S.min() < L - 1e-12:
            bad_l += 1
        if mo and not any((g[:, j] > 0).all() or (g[:, j] < 0).all() for j in range(DIM)):
            bad_mono += 1
    agree = ""
    t7 = os.path.join(HERE, "..", "t7_rigorous", "t7_rigorous.exe")
    if P == 7 and os.path.exists(t7):
        fin, fout = os.path.join(HERE, "_t7_in.txt"), os.path.join(HERE, "_t7_out.txt")
        open(fin, "w").write("\n".join(" ".join(f"{b(v):016x}" for v in list(lo) + list(hi)) for lo, hi in boxes) + "\n")
        subprocess.run([t7, "boxtest", fin, fout], check=True)
        t7out = [x.split() for x in open(fout).read().split("\n") if x.strip()]
        os.remove(fin)
        os.remove(fout)
        du = max(abs(d(r1[0]) - d(r2[0])) for r1, r2 in zip(out, t7out))
        same = sum(1 for r1, r2 in zip(out, t7out) if abs(d(r1[0]) - d(r2[0])) <= 1e-12 and r1[2] == r2[1] and r1[3] == r2[2])
        agree = (f"; against t7_rigorous.exe the upper bounds differ by at most {du:.1e} (its constants 2 pi k/7 are "
                 f"exact-rational enclosures, here they are computed in interval arithmetic) and agree with the flags "
                 f"on {same}/{len(boxes)} boxes")
    ok = bad_u == bad_l == bad_mono == fails == 0 and (not agree or f"{len(boxes)}/{len(boxes)}" in agree)
    say(f"[{'PASS' if ok else 'FAIL'}] p = {P}: {len(boxes)} boxes ({n_smooth} smooth, {n_mono} monotone): S above U at "
        f"sampled points {bad_u} times, below L {bad_l} times; monotone flag contradicted {bad_mono} times; "
        f"{fails} reduction failures{agree}")
    return ok


if __name__ == "__main__":
    say("bb_selftest.py -- the generalized prover against floating-point S")
    res = [test(P) for P in (3, 5, 7)]
    say(f"[{'PASS' if all(res) else 'FAIL'}] bb_selftest: {sum(res)}/3")
    LOG.close()
    sys.exit(0 if all(res) else 1)
