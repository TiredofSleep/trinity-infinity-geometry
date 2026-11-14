#!/usr/bin/env python3
"""alpha_test.py -- the registered test of PREREG.md (lab/alpha_137): does the prime gradient at 137 make the inverse
fine-structure constant?  Committed with its predictions before any run.  [FENCE: a physics reading, not a claim.]

    "why is the edge of the coin 137 edges... the answer is in how primes form direction on the interleaved
     staircase"  -- the author, 14 November 2026

The grammar G: fourteen atoms at x = p = 137 (PREREG.md's table) and four forms, with s = +1 or -1:
  F1  137 + s a_i          F2  137 (1 + s a_i)          F3  137 + s a_i a_j (i < j), 137 + s a_i^2
  F4  137 + s a_i / a_j (i != j)                                                              630 expressions
The statistic: d*, the distance from the target to the nearest expression.  The null: a target drawn uniformly from
[137, 138]; the p-value is the length of the union of the intervals [Q - d*, Q + d*] inside [137, 138], exactly.

  python alpha_test.py calibrate   # A0: the atoms' cross-checks only; prints no distance to any target
  python alpha_test.py run         # A0 to A3; writes alpha_test_run.log

numpy + mpmath + towers/seven_levels/oscillator_states.py.  One process, below-normal priority.  ASCII output.
"""
import ctypes
import math
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import mpmath
import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "towers", "seven_levels"))
import oscillator_states as osc                                          # noqa: E402

X = 137
TARGET, SIGMA = 137.035999177, 0.000000021                                # CODATA 2022, zero momentum transfer
DECOYS = [("137 + (pi - 3)", 137 + math.pi - 3), ("137 + (e - 2)", 137 + math.e - 2),
          ("137 + (sqrt 2 - 1)", 137 + math.sqrt(2) - 1)]
GAMMA = 0.57721566490153286
LOG = None
FAILS = []


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(tag, label, ok):
    if not ok:
        FAILS.append(tag)
    say(("PASS  " if ok else "FAIL  ") + tag + "  " + label)


def primes_upto(n):
    return [k for k in range(2, n + 1) if all(k % d for d in range(2, math.isqrt(k) + 1))]


def kloosterman(p):
    """K(m, p) = sum over a in F_p* of cos(2 pi (a + m/a)/p), for m = 0, ..., p - 1 (real, since K is)"""
    a = np.arange(1, p)
    inv = np.array([pow(int(v), -1, p) for v in a])
    return np.array([np.cos(2 * np.pi * ((a + m * inv) % p) / p).sum() for m in range(p)])


def norm_sum_of_sizes(p):
    """the norm state's S = sum |W| on three wheels of p, by NORM_STATE.md's closed form"""
    K = kloosterman(p)
    return ((p + 1) + (p * p + p + 1) * np.abs(K[1:]).sum()) / p ** 2


def atoms():
    P = primes_upto(X)
    psi = sum(math.log(q) * sum(1 for k in range(1, 20) if q ** k <= X) for q in P)
    theta = sum(math.log(q) for q in P)
    mert = math.exp(GAMMA) * math.log(X) * math.prod(1 - 1 / q for q in P)
    Li = float(mpmath.li(X) - mpmath.li(2))
    p = X
    K1 = kloosterman(p)[1]
    A = [("a1", "1/ln 137", 1 / math.log(X)),
         ("a2", "1/(137 ln^2 137)", 1 / (X * math.log(X) ** 2)),
         ("a3", "1/sqrt 137", 1 / math.sqrt(X)),
         ("a4", "1/137", 1 / X),
         ("a5", "1/137^2", 1 / X ** 2),
         ("a6", "2e^-g - 1", 2 * math.exp(-GAMMA) - 1),
         ("a7", "1 - e^g ln 137 prod(1 - 1/p)", 1 - mert),
         ("a8", "(psi(137) - 137)/137", (psi - X) / X),
         ("a9", "(theta(137) - 137)/137", (theta - X) / X),
         ("a10", "1 - pi(137)/(li(137) - li(2))", 1 - len(P) / Li),
         ("a11", "(p + 2)/((p + 1) sqrt(p - 1))", (p + 2) / ((p + 1) * math.sqrt(p - 1))),
         ("a12", "2/(p + 1)", 2 / (p + 1)),
         ("a13", "8/(3 pi) - S/p^(3/2)", 8 / (3 * math.pi) - norm_sum_of_sizes(p) / p ** 1.5),
         ("a14", "|K(1, 137)|/(2 sqrt 137)", abs(K1) / (2 * math.sqrt(p)))]
    return A, dict(P=P, psi=psi, theta=theta, K1=K1)


def grammar(A):
    G = []
    for s in (1, -1):
        sg = "+" if s > 0 else "-"
        for t, _, a in A:
            G.append((f"137 {sg} {t}", X + s * a))
            G.append((f"137 (1 {sg} {t})", X * (1 + s * a)))
        for i, (ti, _, ai) in enumerate(A):
            G.append((f"137 {sg} {ti}^2", X + s * ai * ai))
            for j, (tj, _, aj) in enumerate(A):
                if i < j:
                    G.append((f"137 {sg} {ti} {tj}", X + s * ai * aj))
                if i != j:
                    G.append((f"137 {sg} {ti}/{tj}", X + s * ai / aj))
    return G


def union_length(vals, d, lo=137.0, hi=138.0):
    iv = sorted((max(lo, v - d), min(hi, v + d)) for v in vals if v + d > lo and v - d < hi)
    total, cur_a, cur_b = 0.0, None, None
    for a, b in iv:
        if cur_b is None or a > cur_b:
            if cur_b is not None:
                total += cur_b - cur_a
            cur_a, cur_b = a, b
        else:
            cur_b = max(cur_b, b)
    if cur_b is not None:
        total += cur_b - cur_a
    return total / (hi - lo)


def calibrate():
    A, info = atoms()
    p = X
    ok = len(info["P"]) == 33 and all(abs(a) > 0 and math.isfinite(a) for _, _, a in A)
    check("A0a", f"the atoms are finite and nonzero, and pi(137) = {len(info['P'])}", ok)
    n5, n7 = (norm_sum_of_sizes(5) - 1) / 2, (norm_sum_of_sizes(7) - 1) / 2
    check("A0b", "the norm state's closed form gives the logged negativities at p = 5 and 7 (4.252724292100, "
          "7.902228372133)", abs(n5 - 4.252724292100) < 1e-9 and abs(n7 - 7.902228372133) < 1e-9)
    V = osc.nonsplit_states(p)[0]
    W = osc.wigner(V, p)
    Wf = W.reshape(len(W), -1)
    z = (Wf - Wf.mean(axis=1, keepdims=True)) / Wf.std(axis=1, keepdims=True)
    off = Wf[:, 1:]
    raw4 = ((off ** 4).mean(axis=1) / ((off ** 2).mean(axis=1)) ** 2).mean()
    a11 = dict((t, a) for t, _, a in A)["a11"]
    a12 = dict((t, a) for t, _, a in A)["a12"]
    check("A0c", "at p = 137 the oscillator states themselves give a11 (minus their average standardized third moment) "
          "and a12 (2 minus their average fourth-moment ratio)",
          abs((z ** 3).mean() + a11) < 1e-10 and abs((2 - raw4) - a12) < 1e-10)
    check("A0d", "|K(1, 137)| <= 2 sqrt 137 (Weil)", abs(info["K1"]) <= 2 * math.sqrt(p))
    G = grammar(A)
    check("A0e", f"the grammar has {len(G)} expressions, as registered (630)", len(G) == 630)
    return A, G


def nearest(G, target):
    d = [abs(v - target) for _, v in G]
    order = np.argsort(d)
    return [(G[i][0], G[i][1], d[i]) for i in order[:5]]


def run():
    global LOG
    LOG = open(os.path.join(HERE, "alpha_test_run.log"), "w", encoding="utf-8")
    say("alpha_test.py run: the registered test of lab/alpha_137/PREREG.md [FENCE]")
    say()
    A, G = calibrate()
    say()
    say("the atoms at x = p = 137:")
    for t, name, a in A:
        say(f"  {t:4s} {name:32s} {a:+.12f}")
    vals = [v for _, v in G]
    inside = sum(1 for v in vals if 137 <= v <= 138)
    lo, hi = 0.0, 1.0
    for _ in range(80):                                                   # the null's median distance
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if union_length(vals, mid) < 0.5 else (lo, mid)
    say()
    say(f"the grammar: {len(G)} expressions, {inside} of them in [137, 138]; under the null the median distance from a "
        f"random target to the nearest is {hi:.3e}")
    say()
    top = nearest(G, TARGET)
    dstar = top[0][2]
    pval = union_length(vals, dstar)
    say(f"the target, alpha^-1 = {TARGET:.9f} (sigma {SIGMA:.1e}): the nearest expressions")
    for lab, v, d in top:
        say(f"  {lab:28s} {v:.9f}   distance {d:.3e} = {d / SIGMA:.3g} sigma")
    say(f"  d* = {dstar:.3e}; look-elsewhere p-value {pval:.4f}")
    say()
    dec = []
    for name, t in DECOYS:
        b = nearest(G, t)[0]
        pv = union_length(vals, b[2])
        dec.append(pv)
        say(f"decoy {name} = {t:.9f}: nearest {b[0]} = {b[1]:.9f}, distance {b[2]:.3e}, p-value {pv:.4f}")
    say()
    a1 = dstar <= 3 * SIGMA
    a2 = pval < 0.01
    a3 = all(pv >= 0.01 for pv in dec)
    say(f"A0 {'HELD' if not FAILS else 'DIED'}: the atoms' cross-checks")
    say(f"A1 {'HELD' if a1 else 'DIED'}: some expression lies within 3 sigma of alpha^-1 (nearest: {dstar / SIGMA:.3g} sigma)")
    say(f"A2 {'HELD' if a2 else 'DIED'}: the nearest expression is closer than chance (p-value {pval:.4f}, against 0.01)")
    say(f"A3 {'HELD' if a3 else 'DIED'}: no decoy has a p-value below 0.01 ({', '.join(f'{v:.4f}' for v in dec)})")
    say()
    say("The running: alpha^-1 is 137.036 at zero momentum transfer, about 133.5 at the tau mass and 127.95 at the Z "
        "mass (MS-bar, PDG 2017). This grammar is built on 137 and so presupposes the zero-momentum limit.")
    LOG.close()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "calibrate"
    if mode == "run":
        run()
    else:
        calibrate()
    sys.exit(1 if FAILS else 0)
