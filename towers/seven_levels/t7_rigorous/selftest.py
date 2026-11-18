"""selftest.py -- checks of t7_rigorous.exe against 50-digit arithmetic and against the float prover.

    "make it rigor"  -- the author, 18 November 2026

The proof rests on the reasoning in RIGOROUS.md, not on these tests.  They look for mistakes in the program:
  T1. cos and sin enclosures at 20 000 doubles (random, and next to multiples of pi/4, where the reduction switches):
      the true value, computed in 50-digit arithmetic for the exact double, must lie inside.
  T2. cos and sin ranges over 20 000 intervals [a, b] (widths from 1e-12 to 6.5, endpoints next to the extrema):
      the true range, from the endpoints and every interior critical point, must lie inside.
  T3. eval_box on 3 000 boxes (sizes from the first grid down to 1e-7, many near the maximizers): the rigorous upper
      bound must agree with the float prover's to 1e-9 and lie above S at 64 sampled points of each box; the smooth and
      monotone flags must agree with the float prover's.
Usage: python selftest.py   (about a minute)   -> selftest.log
"""
import math
import os
import random
import struct
import subprocess
import sys

import mpmath as mp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import t_optimal_7 as T7  # noqa: E402

mp.mp.dps = 50
EXE = os.path.join(HERE, "t7_rigorous.exe")
LOG = open(os.path.join(HERE, "selftest.log"), "w", encoding="utf-8")
rng = random.Random(20261118)


def say(s=""):
    print(s, flush=True)
    LOG.write(s + "\n")
    LOG.flush()


def b(d):
    return struct.unpack("<Q", struct.pack("<d", d))[0]


def d(h):
    return struct.unpack("<d", struct.pack("<Q", int(h, 16)))[0]


def run(mode, lines):
    fin, fout = os.path.join(HERE, f"_{mode}_in.txt"), os.path.join(HERE, f"_{mode}_out.txt")
    open(fin, "w").write("\n".join(lines) + "\n")
    subprocess.run([EXE, mode, fin, fout], check=True)
    out = open(fout).read().split("\n")
    os.remove(fin)
    os.remove(fout)
    return [x for x in out if x.strip()]


def near_points(n):
    pts = []
    for _ in range(n):
        k = rng.randint(-18, 10)
        base = k * math.pi / 4
        off = rng.choice([0.0, 1e-17, 1e-15, 1e-12, 1e-8, 1e-4]) * rng.choice([-1, 1])
        pts.append(base + off)
    return pts


def t1():
    pts = [rng.uniform(-14.0, 10.0) for _ in range(10000)] + near_points(10000)
    out = run("selftest", [f"P {b(a):016x} {b(a):016x}" for a in pts])
    bad = 0
    wmax = 0.0
    for a, line in zip(pts, out):
        f = line.split()
        ok = int(f[1])
        clo, chi, slo, shi = (d(x) for x in f[2:6])
        x = mp.mpf(a)
        c, s = mp.cos(x), mp.sin(x)
        if not ok or not (mp.mpf(clo) <= c <= mp.mpf(chi)) or not (mp.mpf(slo) <= s <= mp.mpf(shi)):
            bad += 1
        wmax = max(wmax, chi - clo, shi - slo)
    say(f"[{'PASS' if bad == 0 else 'FAIL'}] T1: cos/sin enclosures at {len(pts)} doubles contain the 50-digit values "
        f"({bad} failures); widest enclosure {wmax:.2e}")
    return bad == 0


def true_range(a, b_):
    xa, xb = mp.mpf(a), mp.mpf(b_)
    cands = [xa, xb]
    k0, k1 = int(mp.floor(xa / (mp.pi / 2))) - 1, int(mp.ceil(xb / (mp.pi / 2))) + 1
    for k in range(k0, k1 + 1):
        t = k * mp.pi / 2
        if xa <= t <= xb:
            cands.append(t)
    cs = [mp.cos(t) for t in cands]
    ss = [mp.sin(t) for t in cands]
    return min(cs), max(cs), min(ss), max(ss)


def t2():
    pairs = []
    for i in range(20000):
        if i % 2 == 0:
            a = rng.uniform(-14.0, 9.0)
        else:
            a = rng.randint(-18, 10) * math.pi / 2 + rng.choice([-1, 1]) * rng.choice([1e-16, 1e-13, 1e-9, 1e-5, 1e-2])
        w = rng.choice([0.0, 1e-12, 1e-6, 1e-3, 0.1, 1.0, 3.0, 6.5]) * rng.uniform(0.5, 1.0)
        pairs.append((a, a + w))
    out = run("selftest", [f"R {b(a):016x} {b(c):016x}" for a, c in pairs])
    bad = 0
    slack = 0.0
    for (a, c), line in zip(pairs, out):
        f = line.split()
        ok = int(f[1])
        cmn, cmx, smn, smx = (mp.mpf(d(x)) for x in f[2:6])
        tc0, tc1, ts0, ts1 = true_range(a, c)
        if not ok or not (cmn <= tc0 and tc1 <= cmx and smn <= ts0 and ts1 <= smx):
            bad += 1
        slack = max(slack, float(tc0 - cmn), float(cmx - tc1), float(ts0 - smn), float(smx - ts1))
    say(f"[{'PASS' if bad == 0 else 'FAIL'}] T2: cos/sin ranges over {len(pairs)} intervals contain the true ranges "
        f"({bad} failures); largest overestimate {slack:.2e}")
    return bad == 0


def S_np(phi6):
    phi7 = np.concatenate([np.zeros((phi6.shape[0], 1)), phi6], axis=1)
    return T7.S_of(phi7)


def t3():
    phis = []
    for c in (3, 4):
        f = [(c * (v ** 3 + 4 * v * v + 2 * v)) % 7 for v in range(7)]
        phis.append(np.array([2 * math.pi * k / 7 for k in f[1:]]))
    lo_d = np.array([-math.pi / 7] * 2 + [0.0] * 4)
    hi_d = np.array([math.pi / 7] * 2 + [2 * math.pi] * 4)
    boxes = []
    for i in range(3000):
        kind = i % 4
        if kind == 0:
            h = np.array([rng.choice([math.pi / 14, math.pi / 4, 0.1, 0.01, 1e-3, 1e-5, 1e-7])] * 6)
            cen = np.array([rng.uniform(lo_d[j], hi_d[j]) for j in range(6)])
        elif kind == 3:                     # small boxes inside the cubes, to exercise rule (c)
            h = np.array([rng.uniform(1e-4, 1e-3) for _ in range(6)])
            cen = phis[i % 2] + np.array([rng.uniform(-0.002, 0.002) for _ in range(6)])
        else:
            h = np.array([rng.choice([0.03, 0.01, 4e-3, 1e-3, 1e-4])] * 6) * np.array([rng.uniform(0.5, 1.0) for _ in range(6)])
            cen = phis[kind - 1] + np.array([rng.uniform(-0.01, 0.01) for _ in range(6)])
        boxes.append((cen - h, cen + h))
    lines = [" ".join(f"{b(x):016x}" for x in list(lo) + list(hi)) for lo, hi in boxes]
    out = run("boxtest", lines)
    lo = np.array([bx[0] for bx in boxes])
    hi = np.array([bx[1] for bx in boxes])
    m = np.clip(0.5 * lo + 0.5 * hi, lo, hi)
    r = np.maximum(m - lo, hi - m)
    Uf, smf, mof, _ = T7.bounds(m, r)
    bad_u = bad_s = bad_flags = fails = 0
    dmax = 0.0
    n_mono = n_smooth = n_cube = 0
    for i, line in enumerate(out):
        f = line.split()
        U = d(f[0])
        sm, mo, fl, cube = int(f[1]), int(f[2]), int(f[3]), int(f[4])
        fails += fl
        n_mono += mo
        n_smooth += sm
        n_cube += cube
        dmax = max(dmax, abs(U - Uf[i]))
        if abs(U - Uf[i]) > 1e-9 or U < Uf[i] - 1e-12:
            bad_u += 1
        if sm != int(smf[i]) or mo != int(mof[i]):
            bad_flags += 1
        pts = lo[i] + (hi[i] - lo[i]) * np.array([[rng.random() for _ in range(6)] for _ in range(64)])
        if S_np(pts).max() > U + 1e-12:
            bad_s += 1
    ok = bad_u == 0 and bad_s == 0 and bad_flags == 0 and fails == 0
    say(f"[{'PASS' if ok else 'FAIL'}] T3: {len(boxes)} boxes ({n_smooth} smooth, {n_mono} monotone, {n_cube} inside a "
        f"cube): rigorous bound vs float prover differs by at most {dmax:.2e} ({bad_u} disagreements over 1e-9); "
        f"S at 64 sampled points never exceeds the bound ({bad_s} violations); flags agree ({bad_flags} disagreements); "
        f"{fails} reduction failures")
    return ok


if __name__ == "__main__":
    say("selftest.py -- t7_rigorous.exe against 50-digit arithmetic and the float prover")
    res = [t1(), t2(), t3()]
    say(f"[{'PASS' if all(res) else 'FAIL'}] selftest: {sum(res)}/3")
    LOG.close()
    sys.exit(0 if all(res) else 1)
