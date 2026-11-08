"""round6.py -- round 6 of PREREG.md: the author's prediction against the Legendre-side reading.

  W1 (the author's): "even only wins the lows, the odd wins the rest" -- the odd side wins at 23 and at 29.
  W2 (the rival):    the Legendre state's side wins -- the odd side at 23, the even side at 29.

The predictions were registered at commit 32e5282, before any run at 23 or 29; this script is committed before its
run, as the registration promised.  It uses round 5's machinery: the sign ascent from random states, at least two
million climbs on each side, and the exceptional groups' states (not scored; the forced rule of round 4).

numpy only.  One process per prime at below-normal priority and three threads; the two can run at once.  ASCII
output; each part writes round6_<part>.log.
Run:  python round6.py twentythree
      python round6.py twentynine
      python round6.py combine        (after both: scores W1 and W2 from the two logs)
Set ROUND6_SMOKE=1 for a quick test of the code at a tiny size; its scores mean nothing.
"""
import os
import sys

PART = sys.argv[1] if len(sys.argv) > 1 else "twentythree"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import time
from collections import Counter

import numpy as np

import round3 as r3
import round5 as r5

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261111
SMOKE = os.environ.get("ROUND6_SMOKE") == "1"
CLIMBS = {"twentythree": 2_000_000, "twentynine": 2_000_000}
LOG = None
T0 = time.time()
SC = {}


def n(x):
    return max(x // 20000, 2) if SMOKE else x


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def clock():
    return f"[{time.time() - T0:.0f} s]"


def symmetries_about(W, d, lins, u0):
    """the Clifford symmetries of a state whose unique ceiling or floor point is u0: they must fix u0, so only the
    linear part varies (one translation per linear map), which is d^2 times faster than the general search"""
    q0, p0 = divmod(u0, d)
    q, p = np.divmod(np.arange(d * d), d)
    out = []
    for (Sq, Sp) in lins:
        t1, t2 = (q0 - Sq[u0]) % d, (p0 - Sp[u0]) % d                   # the translation that keeps u0 in place
        idx = ((Sq + t1) % d) * d + (Sp + t2) % d
        if np.abs(W[idx] - W).max() < 1e-7:
            out.append(idx)
    return out


def alone_about(psi, A, d, sym):
    """is the state the only one its symmetries fix?  (round 3's test, with the symmetries already found)"""
    label, changed = np.arange(d * d), True
    while changed:
        changed = False
        for g in sym:
            new = np.minimum(label, label[g])
            if (new != label).any():
                label, changed = new, True
    worst = 0.0
    for o in np.unique(label):
        v = A[label == o].sum(axis=0) @ psi
        worst = max(worst, np.linalg.norm(v - np.vdot(psi, v) * psi))
    return worst < 1e-8


def describe_side(psi, A, d, lins):
    """symmetry count and orders, ceiling and floor points, negative points, deepest value: for a state on a side"""
    W = r3.wigner(psi[None, :], A, d)[0]
    ext = np.where(np.abs(np.abs(W) - 1 / d) < 1e-9)[0]
    up, down = int((np.abs(W - 1 / d) < 1e-9).sum()), int((np.abs(W + 1 / d) < 1e-9).sum())
    if len(ext) != 1:
        return None, up, down, int((W < -1e-12).sum()), W.min()
    sym = symmetries_about(W, d, lins, int(ext[0]))
    orders = dict(sorted(Counter(r3.perm_order(g) for g in sym).items()))
    return (len(sym), orders, alone_about(psi, A, d, sym)), up, down, int((W < -1e-12).sum()), W.min()


def run(p, rng):
    A = r3.phase_points(p)
    E, O = r3.sides(p)
    P = r3.basics(p)[4]
    leg = 1 if pow(p - 1, (p - 1) // 2, p) == 1 else -1
    L = r3.legendre(p)
    NL = r3.negativity(r3.wigner(L[None, :], A, p)[0])
    say(f"{p} levels: the Legendre state is {'even' if leg == 1 else 'odd'} (parity "
        f"{np.real(np.vdot(L, P @ L)):+.0f}), total negativity {NL:.12f}")
    best = {}
    for name, Q in (("even", E), ("odd", O)):
        Ns, reps, stuck = r3.search(r3.compress(A, Q), p, n(CLIMBS[PART]), rng, batch=5000)
        best[name] = (Ns.max(), Q @ reps[max(reps)][0], Ns, reps, Q)
        say(f"  {CLIMBS[PART]} climbs among {name} states: best {Ns.max():.12f} (reached "
            f"{int((Ns > Ns.max() - 1e-9).sum())} times; {stuck} still moving) {clock()}")
    even_side = max(best["even"][0], NL if leg == 1 else -1)
    odd_side = max(best["odd"][0], NL if leg == -1 else -1)
    margin = even_side - odd_side
    say(f"  the even side {even_side:.12f}, the odd side {odd_side:.12f}: the even side ahead by {margin:.6f} "
        f"({'even' if margin > 0 else 'odd'} wins)")
    lins = r3.linear_parts(p)
    for name in ("even", "odd"):
        sym, up, down, neg, deep = describe_side(best[name][1], A, p, lins)
        say(f"  the best {name} state found: symmetries {sym[0] if sym else '?'}, orders {sym[1] if sym else '?'}, "
            f"ceiling points {up}, floor points {down}, negative points {neg}, deepest {deep:+.6f}; fixed by its "
            f"symmetries alone: {sym[2] if sym else '?'}")
        Ns, reps = best[name][2], best[name][3]
        say(f"    the five highest {name} tops: "
            + ", ".join(f"{v:.9f} x{c}" for v, c in sorted(Counter(np.round(Ns, 9)).items(), reverse=True)[:5]))
    say(clock())
    Wl = r5.Weil(p, A)
    say(f"  the exceptional groups in SL(2, {p}) ({len(Wl.parent)} elements), one from each conjugacy class "
        f"(not scored; round 4's forced rule puts their states on the Legendre state's side):")
    for gname, a, b in r5.exceptional(Wl, p):
        states = r5.fixed_states(r5.operator(Wl, a), r5.operator(Wl, b))
        pars = [round(float(np.real(np.vdot(s, P @ s))), 6) for s in states]
        vals = [round(float(r3.negativity(r3.wigner(s[None, :], A, p)[0])), 6) for s in states]
        say(f"    {gname}: fixes {len(states)} state(s); parities {pars}; total negativities {vals}")
    say(clock())
    return margin


def combine():
    global LOG
    m = {}
    for part, tag in (("twentythree", "23"), ("twentynine", "29")):
        for line in open(os.path.join(HERE, f"round6_{part}.log"), encoding="utf-8"):
            if line.startswith(f"margin at {tag}:"):
                m[tag] = float(line.split(":")[1])
    LOG = open(os.path.join(HERE, "round6_combined.log"), "w", encoding="utf-8")
    win = {t: ("even" if m[t] > 1e-6 else "odd" if m[t] < -1e-6 else "a tie") for t in m}
    say(f"the even side ahead by {m['23']:.6f} at 23 ({win['23']} wins) and by {m['29']:.6f} at 29 ({win['29']} wins)")
    w1 = win["23"] == "odd" and win["29"] == "odd"
    w2 = win["23"] == "odd" and win["29"] == "even"
    say(f"W1 {'HELD' if w1 else 'DIED'}: the author's prediction, the odd side wins at 23 and at 29")
    say(f"W2 {'HELD' if w2 else 'DIED'}: the Legendre-side reading, the odd side at 23 and the even side at 29")
    LOG.close()


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.windll.kernel32.GetCurrentProcess(), 0x00004000)
    except Exception:
        pass
    if PART == "combine":
        combine()
        return
    p = {"twentythree": 23, "twentynine": 29}[PART]
    LOG = open(os.path.join(HERE, f"round6_{PART}.log"), "w", encoding="utf-8")
    margin = run(p, np.random.default_rng([SEED, p]))
    say(f"\nmargin at {p}: {margin:.9f}")
    LOG.close()


if __name__ == "__main__":
    main()
