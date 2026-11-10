"""round7.py -- round 7 of PREREG.md: the author's 7-wheel against the rival observation.

  X1 (the author's): the even side wins exactly when the 7-wheel (the powers of 7 modulo p) passes through the half
                     turn.  At 31 the 7-wheel has period 15 and at 37 period 9, so it never reaches the half turn
                     there: the odd side wins at 31 and at 37.
  X2 (the rival):    the odd side's wins fall at primes 4 more than a multiple of 5; neither 31 nor 37 is one, so the
                     even side wins at both.

The predictions were registered at commit de3719d, before any run at 31 or 37; this script is committed before its
run, as the registration promised.  It uses round 6's machinery (round6.py): the sign ascent from random states, two
million climbs on each side, the Legendre state on its side, and the exceptional groups' states (not scored).

numpy only.  One process at below-normal priority and three threads.  ASCII output; each part writes
round7_<part>.log.
Run:  python round7.py thirtyone      (about an hour and a half)
      python round7.py thirtyseven    (not yet run)
      python round7.py combine        (scores X1 and X2 from the logs that exist)
Set ROUND7_SMOKE=1 for a quick test of the code at a tiny size; its scores mean nothing.
"""
import os
import sys

PART = sys.argv[1] if len(sys.argv) > 1 else "thirtyone"
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "3")
import time
from collections import Counter

import numpy as np

import round3 as r3
import round5 as r5
import round6 as r6

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261113
SMOKE = os.environ.get("ROUND7_SMOKE") == "1"
PRIMES = {"thirtyone": 31, "thirtyseven": 37}
CLIMBS = 2_000_000
LOG = None
T0 = time.time()


def n(x):
    return max(x // 20000, 2) if SMOKE else x


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def clock():
    return f"[{time.time() - T0:.0f} s]"


def period(b, p):
    """the 7-wheel's period: how many steps b, b^2, b^3, ... take to return to 1 modulo p"""
    r, x = 1, b % p
    while x != 1:
        x, r = x * b % p, r + 1
    return r


def run(p, rng):
    """round 6's run (round6.run), at p"""
    r = period(7, p)
    say(f"{p} levels: the 7-wheel has period {r}: "
        + (f"it passes through the half turn (7^{r // 2} = -1 mod {p}), so X1 calls the even side"
           if r % 2 == 0 else "it never reaches the half turn, so X1 calls the odd side")
        + f"; {p} leaves {p % 5} on division by 5, so X2 calls the " + ("odd" if p % 5 == 4 else "even") + " side")
    A = r3.phase_points(p)
    E, O = r3.sides(p)
    P = r3.basics(p)[4]
    leg = 1 if pow(p - 1, (p - 1) // 2, p) == 1 else -1
    L = r3.legendre(p)
    NL = r3.negativity(r3.wigner(L[None, :], A, p)[0])
    say(f"  the Legendre state is {'even' if leg == 1 else 'odd'} (parity {np.real(np.vdot(L, P @ L)):+.0f}), total "
        f"negativity {NL:.12f}")
    best = {}
    for name, Q in (("even", E), ("odd", O)):
        Ns, reps, stuck = r3.search(r3.compress(A, Q), p, n(CLIMBS), rng, batch=5000)
        best[name] = (Ns.max(), Q @ reps[max(reps)][0], Ns, reps, Q)
        say(f"  {CLIMBS} climbs among {name} states: best {Ns.max():.12f} (reached "
            f"{int((Ns > Ns.max() - 1e-9).sum())} times; {stuck} still moving) {clock()}")
    even_side = max(best["even"][0], NL if leg == 1 else -1)
    odd_side = max(best["odd"][0], NL if leg == -1 else -1)
    margin = even_side - odd_side
    say(f"  the even side {even_side:.12f}, the odd side {odd_side:.12f}: the even side ahead by {margin:.6f} "
        f"({'even' if margin > 1e-6 else 'odd' if margin < -1e-6 else 'neither'} wins)")
    lins = r3.linear_parts(p)
    for name in ("even", "odd"):
        sym, up, down, neg, deep = r6.describe_side(best[name][1], A, p, lins)
        say(f"  the best {name} state found: symmetries {sym[0] if sym else '?'}, orders {sym[1] if sym else '?'}, "
            f"ceiling points {up}, floor points {down}, negative points {neg}, deepest {deep:+.6f}; fixed by its "
            f"symmetries alone: {sym[2] if sym else '?'}")
        Ns = best[name][2]
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
    for part, p in PRIMES.items():
        path = os.path.join(HERE, f"round7_{part}.log")
        if os.path.exists(path):
            for line in open(path, encoding="utf-8"):
                if line.startswith(f"margin at {p}:"):
                    m[p] = float(line.split(":")[1])
    LOG = open(os.path.join(HERE, "round7_combined.log"), "w", encoding="utf-8")
    win = {p: ("even" if v > 1e-6 else "odd" if v < -1e-6 else "neither") for p, v in m.items()}
    for p in sorted(m):
        say(f"the even side ahead by {m[p]:.6f} at {p} ({win[p]} wins)")
    for name, call, who in (("X1", "odd", "the author's 7-wheel, the odd side wins at 31 and at 37"),
                            ("X2", "even", "the rival observation, the even side wins at 31 and at 37")):
        if any(win[p] != call for p in win):
            verdict = "DIED"
        elif len(win) == 2:
            verdict = "HELD"
        else:
            verdict = "STANDS at " + " and ".join(str(p) for p in sorted(win)) + " (37 not run)"
        say(f"{name} {verdict}: {who}")
    LOG.close()


def main():
    global LOG
    try:
        import ctypes
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass
    if PART == "combine":
        combine()
        return
    p = PRIMES[PART]
    LOG = open(os.path.join(HERE, f"round7_{PART}.log"), "w", encoding="utf-8")
    margin = run(p, np.random.default_rng([SEED, p]))
    say(f"\nmargin at {p}: {margin:.9f}")
    LOG.close()


if __name__ == "__main__":
    main()
