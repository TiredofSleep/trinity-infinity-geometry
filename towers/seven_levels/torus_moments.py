"""torus_moments.py -- round 12 of PREREG.md: the higher moments of the oscillator states' Wigner values, committed
with its predictions before the run.

    "write the proof and test the higher moments"  -- the author, 13 November 2026

Round 11 found that the oscillator states' Wigner values follow the Sato-Tate law in two statistics: S/sqrt p, which
is mean |W| over rms W, and the fourth-moment ratio.  Under the Sato-Tate law the values, scaled to variance 1, follow
the semicircle law on [-2, 2], whose even moments are the Catalan numbers 1, 2, 5, 14 and whose odd moments vanish.
This script takes every one-line oscillator state of round 11 (oscillator_states.py builds them), standardizes its
Wigner values off the origin (mean 0, variance 1), and computes
  - their third, fourth, sixth and eighth moments, for every state at every prime from 5 to 401;
  - the averages of those moments over the non-split torus's eigenbasis, at each prime;
  - the Kolmogorov distance of all standardized values at the primes from 211 to 401, pooled, to the semicircle law,
    the Gaussian and the arcsine law (from a histogram with bins of width 0.002);
and as calibration it recomputes round 11's raw fourth-moment ratios and the identity 2p/(p + 1).

numpy only.  One process, one thread, below-normal priority.  ASCII output.
Run:  python torus_moments.py calibrate   (seconds; writes torus_moments_calibrate.log)
      python torus_moments.py run         (about eight minutes; writes torus_moments_run.log)
      python torus_moments.py combine     (writes torus_moments_combined.log)
"""
import ctypes
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time
from math import erf, sqrt, pi

import numpy as np

import oscillator_states as osc

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
PRIMES = osc.PRIMES                                                      # 5 to 401
EDGES = np.linspace(-4, 4, 4001)                                         # bins of width 0.002
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def moments(W):
    """the standardized moments 3, 4, 6, 8 of each state's Wigner values off the origin; its raw mu4/mu2^2; and the
    standardized values themselves"""
    off = W.reshape(len(W), -1)[:, 1:]
    raw4 = (off ** 4).mean(axis=1) / ((off ** 2).mean(axis=1)) ** 2
    Z = (off - off.mean(axis=1, keepdims=True)) / off.std(axis=1, keepdims=True)
    return {k: (Z ** k).mean(axis=1) for k in (3, 4, 6, 8)}, raw4, Z


def round11_r4():
    """round 11's logged mean raw mu4/mu2^2 by prime and torus"""
    out = {}
    for line in open(os.path.join(HERE, "oscillator_states_run.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("TORUS ") and f[1].isdigit():
            out[int(f[1]), f[2]] = float(f[10])
    return out


def calibrate():
    global LOG
    LOG = open(os.path.join(HERE, "torus_moments_calibrate.log"), "w", encoding="utf-8")
    say("the code against round 11: its mean raw mu4/mu2^2 by prime and torus, and the identity 2p/(p + 1)")
    logged = round11_r4()
    ok_all = True
    for p in [q for q in PRIMES if q <= 61]:
        for kind in ("nonsplit", "split"):
            Psi = osc.nonsplit_states(p)[0] if kind == "nonsplit" else osc.split_states(p)
            _, raw4, _ = moments(osc.wigner(Psi, p))
            ok = abs(raw4.mean() - logged[p, kind]) < 1e-6
            if kind == "nonsplit":
                ok &= abs(raw4.mean() - 2 * p / (p + 1)) < 1e-12
            ok_all &= ok
        say(f"  {p}: both tori's mean raw mu4/mu2^2 equal round 11's logged values, and the non-split one equals "
            f"2p/(p + 1): {ok_all}")
    say(f"CALIBRATE {ok_all}")
    LOG.close()


def run():
    global LOG
    LOG = open(os.path.join(HERE, "torus_moments_run.log"), "w", encoding="utf-8")
    say(f"round 12: the standardized moments of the one-line oscillator states at the {len(PRIMES)} primes from 5 to 401")
    say("MOM p kind count mean_m3 mean_m4 mean_m6 mean_m8 sd_m6 sd_m8 mean_raw4 raw4_matches_round11")
    logged = round11_r4()
    hist = np.zeros(len(EDGES) - 1)
    pooled = 0
    for p in PRIMES:
        for kind in ("nonsplit", "split"):
            Psi = osc.nonsplit_states(p)[0] if kind == "nonsplit" else osc.split_states(p)
            m3, m4, m6, m8, raws = [], [], [], [], []
            for i in range(0, len(Psi), 16):
                M, raw4, Z = moments(osc.wigner(Psi[i:i + 16], p))
                m3.append(M[3]), m4.append(M[4]), m6.append(M[6]), m8.append(M[8]), raws.append(raw4)
                if p >= 211:
                    hist += np.histogram(Z.ravel(), bins=EDGES)[0]
                    pooled += Z.size
            m3, m4, m6, m8, raws = map(np.concatenate, (m3, m4, m6, m8, raws))
            say(f"MOM {p} {kind} {len(m3)} {m3.mean():.6f} {m4.mean():.6f} {m6.mean():.6f} {m8.mean():.6f} "
                f"{m6.std():.6f} {m8.std():.6f} {raws.mean():.6f} {abs(raws.mean() - logged[p, kind]) < 1e-6}")
    F = np.concatenate(([0.0], np.cumsum(hist))) / pooled
    x = EDGES
    xs = np.clip(x, -2, 2)
    sc = np.where(x <= -2, 0.0, np.where(x >= 2, 1.0, 0.5 + xs * np.sqrt(4 - xs ** 2) / (4 * pi) + np.arcsin(xs / 2) / pi))
    ga = 0.5 * (1 + np.vectorize(erf)(x / sqrt(2)))
    xa = np.clip(x, -sqrt(2), sqrt(2))
    ar = np.where(x <= -sqrt(2), 0.0, np.where(x >= sqrt(2), 1.0, 0.5 + np.arcsin(xa / sqrt(2)) / pi))
    outside = 1 - F[-1] + F[0]
    say(f"KS {pooled} {np.abs(F - sc).max():.6f} {np.abs(F - ga).max():.6f} {np.abs(F - ar).max():.6f} {outside:.2e}")
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


def combine():
    global LOG
    rows, ks = {}, None
    for line in open(os.path.join(HERE, "torus_moments_run.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("MOM ") and f[1].isdigit():
            rows[int(f[1]), f[2]] = dict(count=int(f[3]), m3=float(f[4]), m4=float(f[5]), m6=float(f[6]),
                                         m8=float(f[7]), raw4=float(f[10]), match=f[11] == "True")
        elif line.startswith("KS ") and f[1].isdigit():
            ks = dict(n=int(f[1]), sc=float(f[2]), ga=float(f[3]), ar=float(f[4]))
    cal = [l.split() for l in open(os.path.join(HERE, "torus_moments_calibrate.log"), encoding="utf-8")
           if l.startswith("CALIBRATE ")][0]
    LOG = open(os.path.join(HERE, "torus_moments_combined.log"), "w", encoding="utf-8")
    big = [p for p in PRIMES if p >= 211]
    tot = sum(rows[p, k]["count"] for p in big for k in ("nonsplit", "split"))
    mean = {m: sum(rows[p, k]["count"] * rows[p, k][m] for p in big for k in ("nonsplit", "split")) / tot
            for m in ("m3", "m4", "m6", "m8")}
    ns6 = {p: rows[p, "nonsplit"]["m6"] for p in big}
    ns8 = {p: rows[p, "nonsplit"]["m8"] for p in big}
    match = all(r["match"] for r in rows.values()) and all(
        abs(rows[p, "nonsplit"]["raw4"] - 2 * p / (p + 1)) < 1e-6 for p in PRIMES)
    say(f"  the primes from 211 to 401: {tot} one-line states; mean standardized moments m3 {mean['m3']:.4f}, "
        f"m4 {mean['m4']:.4f}, m6 {mean['m6']:.4f}, m8 {mean['m8']:.4f} (semicircle 0, 2, 5, 14; Gaussian 0, 3, 15, 105; "
        f"arcsine 0, 1.5, 2.5, 4.375; two independent semicircles 0, 2.5, 8.75, 36.75)")
    say(f"  the non-split basis averages, m6 from {min(ns6.values()):.4f} to {max(ns6.values()):.4f} and m8 from "
        f"{min(ns8.values()):.4f} to {max(ns8.values()):.4f} at the primes from 211 to 401")
    say(f"  the pooled standardized values ({ks['n']} of them): Kolmogorov distance {ks['sc']:.4f} to the semicircle, "
        f"{ks['ga']:.4f} to the Gaussian, {ks['ar']:.4f} to the arcsine law")
    for name, ok, what in (
            ("M0", cal[1] == "True" and match, "calibration: round 11's mean raw mu4/mu2^2 at every prime and torus, and "
                                               "the identity 2p/(p + 1) at every prime"),
            ("M1", abs(mean["m3"]) <= 0.1, "the mean standardized third moment at 211 to 401 is within 0.1 of 0"),
            ("M2", abs(mean["m6"] - 5) <= 0.3, "the mean standardized sixth moment at 211 to 401 is within 0.3 of 5"),
            ("M3", abs(mean["m8"] - 14) <= 1.5, "the mean standardized eighth moment at 211 to 401 is within 1.5 of 14"),
            ("M4", all(abs(v - 5) <= 0.3 for v in ns6.values()) and all(abs(v - 14) <= 1.5 for v in ns8.values()),
             "at every prime from 211 to 401 the non-split basis averages of m6 and m8 are within 0.3 of 5 and 1.5 of 14"),
            ("M5", ks["sc"] < 0.015, "the pooled standardized values are within Kolmogorov distance 0.015 of the "
                                     "semicircle law")):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    LOG.close()


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"calibrate": calibrate, "run": run, "combine": combine}[part]()
