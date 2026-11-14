"""cubic_magic.py -- round 13 of PREREG.md: the magic of every cubic-phase state on two and three wheels, committed
with its predictions before the run.

    "it's okay to drift, i am the visionary, you are the drafter... let's pick a useful direction"  -- the author,
    14 November 2026

A cubic-phase state on n wheels of p levels is psi_f = sum_x w^f(x) |x> / sqrt q, q = p^n, for a polynomial f of degree
at most 3 on F_p^n.  These are the magic states of the third level's diagonal gates (Cui, Gottesman and Krishna), the
gates used for fault-tolerant quantum computing with qudits.  Round 10's norm states are examples.

The identity (PREREG.md, round 13, proved there): if C is f's homogeneous cubic part, psi_f's Wigner function takes the
values  S(w)/q^2,  S(w) = sum_s w^(w.s - 2C(s)),  each q times, over w in F_p^n.  So a cubic state's negativity is
    N = ((1/q) sum_w |S(w)| - 1)/2,
the L1 norm of the Walsh spectrum of -2C, and it depends only on C.  Over F_3 a cubic part uses the monomials of
degree 3 with no exponent above 2 (x^3 = x there).

This script
  - calibrate: checks the identity against the Wigner function computed directly from the state, for random cubic
    states, and reproduces round 10's norm states and flat_states.py's Alltop states;
  - run: every cubic form on two wheels for p = 3 to 23, every one on three wheels for p = 3 and 5, and 2 000 000 random
    ones on three wheels of 7 (plus named forms); logs the best negativity, the form reaching it, its values' count,
    and the number of F_p-points of its projective curve;
  - combine: scores K0 to K6.
numpy only.  One process, below-normal priority.  ASCII output.
Run:  python cubic_magic.py calibrate   (seconds)
      python cubic_magic.py run         (a few minutes)
      python cubic_magic.py combine
"""
import ctypes
import itertools
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import time

import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
SEED = 20261114
TWO = [3, 5, 7, 11, 13, 17, 19, 23]
THREE_ALL = [3, 5]
SAMPLE73 = 2_000_000
LOG = None
T0 = time.time()
# round 9's and round 10's best states found by search, and the norm states (exact)
SEARCH = {(3, 2): 8 / 9, (5, 2): 1.766937254162, (7, 2): 2.719253432179, (3, 3): 17 / 9, (5, 3): 4.301387418094,
          (7, 3): 7.902228372133}
NORM = {3: 17 / 9, 5: 4.252724292100, 7: 7.902228372133}


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def monomials(p, n):
    """the exponent vectors of the degree-3 monomials, no exponent above min(3, p - 1)"""
    top = min(3, p - 1)
    return [e for e in itertools.product(range(top + 1), repeat=n) if sum(e) == 3]


def points(p, n):
    return np.array(list(itertools.product(range(p), repeat=n)), dtype=np.int64)   # kron order, first wheel first


def monomial_values(p, n):
    X = points(p, n)
    mons = monomials(p, n)
    return mons, np.array([np.prod(X ** np.array(e), axis=1) % p for e in mons], dtype=np.int64)   # (#mon, q)


def negativities(coeffs, Mv, p, n):
    """N for each row of coeffs (integer coefficient vectors on the monomials), by the Walsh identity"""
    q = p ** n
    C = (coeffs @ Mv) % p                                                 # (B, q)
    ph = np.exp(-2j * np.pi * (2 * C % p) / p).reshape((len(coeffs),) + (p,) * n)
    S = np.fft.ifftn(ph, axes=tuple(range(1, n + 1))) * q                 # S(w) = sum_s w^(w.s - 2C(s))
    tot = np.abs(S).reshape(len(coeffs), -1).sum(axis=1) / q
    return (tot - 1) / 2, S.reshape(len(coeffs), -1)


def curve_points(c, Mv, p, n):
    """the number of points of the projective curve (or set) C = 0 over F_p"""
    C = (np.asarray(c) @ Mv) % p
    return int(((C == 0).sum() - 1) // (p - 1))


def direct_negativity(f_vals, p, n):
    """the Wigner function computed from the state itself (round 10's formula), for the identity check"""
    q = p ** n
    X = points(p, n)
    wt = p ** np.arange(n - 1, -1, -1)
    psi = np.exp(2j * np.pi * f_vals / p) / np.sqrt(q)
    plus = ((X[:, None, :] + X[None, :, :]) % p) @ wt
    minus = ((X[:, None, :] - X[None, :, :]) % p) @ wt
    F = np.fft.ifftn((psi.conj()[plus] * psi[minus]).reshape((q,) + (p,) * n), axes=tuple(range(1, n + 1))).reshape(q, q)
    W = F[:, ((2 * X) % p) @ wt].real
    return (np.abs(W).sum() - 1) / 2


def norm_coeffs(p):
    """the cubic part of the norm of F_p[t]/(t^3 + a t + b), as a function of the coordinates, by interpolation over
    every monomial of degree at most 3 (over F_3 the norm's x^3 terms are the linear functions x)"""
    import verify_norm_state as vns
    _, N, _ = vns.trace_norm(p)
    X = points(p, 3)
    top = min(3, p - 1)
    basis = [e for e in itertools.product(range(top + 1), repeat=3) if sum(e) <= 3]
    A = np.array([np.prod(X ** np.array(e), axis=1) % p for e in basis], dtype=np.int64).T      # (q, #basis)
    M = np.concatenate([A, (N % p)[:, None]], axis=1) % p
    rows, cols = A.shape
    r, piv = 0, []
    for c in range(cols):
        i = next((i for i in range(r, rows) if M[i, c] % p), None)
        if i is None:
            continue
        M[[r, i]] = M[[i, r]]
        M[r] = (M[r] * pow(int(M[r, c]), -1, p)) % p
        for j in range(rows):
            if j != r and M[j, c]:
                M[j] = (M[j] - M[j, c] * M[r]) % p
        piv.append(c)
        r += 1
    assert not (M[r:, cols] % p).any(), "the norm is a polynomial of degree at most 3"
    coef = np.zeros(cols, dtype=np.int64)
    for k, c in enumerate(piv):
        coef[c] = M[k, cols]
    assert np.array_equal((A @ coef) % p, N % p)
    mons = monomials(p, 3)
    return np.array([coef[basis.index(e)] for e in mons], dtype=np.int64)


def calibrate():
    global LOG
    LOG = open(os.path.join(HERE, "cubic_magic_calibrate.log"), "w", encoding="utf-8")
    rng = np.random.default_rng([SEED, 0])
    say("the Walsh identity against the Wigner function computed from the state, and known values")
    ok_all = True
    for p, n in ((3, 2), (5, 2), (7, 2), (3, 3), (5, 3)):
        mons, Mv = monomial_values(p, n)
        worst = 0.0
        for _ in range(5):
            c = rng.integers(0, p, len(mons))
            low = rng.integers(0, p, 1 + n + n * (n + 1) // 2)                # a random quadratic and linear part
            X = points(p, n)
            quad = [(i, j) for i in range(n) for j in range(i, n)]
            extra = (low[0] + X @ low[1:1 + n] + sum(low[1 + n + k] * X[:, i] * X[:, j] for k, (i, j) in enumerate(quad))) % p
            f = ((c @ Mv) + extra) % p
            Nw = negativities(c[None, :], Mv, p, n)[0][0]
            worst = max(worst, abs(Nw - direct_negativity(f, p, n)))
        ok = worst < 1e-10
        ok_all &= ok
        say(f"  {n} wheels of {p}: the identity holds for random cubic states with random lower terms: {ok}")
    for p in (3, 5, 7):
        mons, Mv = monomial_values(p, 3)
        Nn = negativities(norm_coeffs(p)[None, :], Mv, p, 3)[0][0]
        ok = abs(Nn - NORM[p]) < 1e-9
        ok_all &= ok
        say(f"  three wheels of {p}: the norm form gives round 10's {NORM[p]:.9f}: {ok}")
    say(f"CALIBRATE {ok_all}")
    LOG.close()


def best_of(coeff_iter, Mv, p, n, batch=4096):
    best, arg, hist = -1.0, None, {}
    for c in coeff_iter:
        N, _ = negativities(c, Mv, p, n)
        i = int(np.argmax(N))
        if N[i] > best:
            best, arg = float(N[i]), c[i].copy()
        for v in np.round(N, 6):
            hist[v] = hist.get(v, 0) + 1
    return best, arg, hist


def all_forms(p, m, batch=4096):
    total = p ** m
    for start in range(0, total, batch):
        idx = np.arange(start, min(start + batch, total))
        yield np.stack([(idx // p ** k) % p for k in range(m)], axis=1)


def run():
    global LOG
    LOG = open(os.path.join(HERE, "cubic_magic_run.log"), "w", encoding="utf-8")
    say("round 13: the cubic-phase states")
    say("BEST p n forms best_N share ceiling distinct_values curve_points form")
    for p, n in [(p, 2) for p in TWO] + [(p, 3) for p in THREE_ALL]:
        mons, Mv = monomial_values(p, n)
        best, arg, hist = best_of(all_forms(p, len(mons)), Mv, p, n)
        ceil = (np.sqrt(p ** n) - 1) / 2
        _, S = negativities(arg[None, :], Mv, p, n)
        nvals = len(np.unique(np.round(S[0].real / p ** n, 9)))
        say(f"BEST {p} {n} {p ** len(mons)} {best:.12f} {best / ceil:.6f} {ceil:.6f} {nvals} {curve_points(arg, Mv, p, n)} "
            + ",".join(f"{c}:{''.join(map(str, e))}" for c, e in zip(arg, mons) if c))
        top = sorted(hist.items(), reverse=True)[:6]
        say(f"  the top values and their counts: " + ", ".join(f"{v:.6f} ({k})" for v, k in top))
    # three wheels of 7: a random sample, plus named forms
    p, n = 7, 3
    mons, Mv = monomial_values(p, n)
    rng = np.random.default_rng([SEED, 7, 3])
    named = {"norm": norm_coeffs(p)}
    def mono(e):
        v = np.zeros(len(mons), dtype=np.int64)
        v[mons.index(e)] = 1
        return v
    named["xyz"] = mono((1, 1, 1))
    named["x3+y3+z3"] = mono((3, 0, 0)) + mono((0, 3, 0)) + mono((0, 0, 3))
    named["x3"] = mono((3, 0, 0))
    def sample():
        for _ in range(SAMPLE73 // 4096):
            yield rng.integers(0, p, (4096, len(mons)))
        yield np.stack(list(named.values()))
    best, arg, hist = best_of(sample(), Mv, p, n)
    ceil = (np.sqrt(p ** n) - 1) / 2
    _, S = negativities(arg[None, :], Mv, p, n)
    nvals = len(np.unique(np.round(S[0].real / p ** n, 9)))
    say(f"BEST {p} {n} {SAMPLE73 + len(named)} {best:.12f} {best / ceil:.6f} {ceil:.6f} {nvals} {curve_points(arg, Mv, p, n)} "
        + ",".join(f"{c}:{''.join(map(str, e))}" for c, e in zip(arg, mons) if c))
    top = sorted(hist.items(), reverse=True)[:6]
    say(f"  the top values and their counts: " + ", ".join(f"{v:.6f} ({k})" for v, k in top))
    # the named states, and single-wheel cubics for the per-qudit comparison
    for (pp, nn) in ((3, 3), (5, 3), (7, 3)):
        mons_, Mv_ = monomial_values(pp, nn)
        xyz = np.zeros(len(mons_), dtype=np.int64)
        xyz[mons_.index((1, 1, 1))] = 1
        say(f"NAMED {pp} {nn} xyz {negativities(xyz[None, :], Mv_, pp, nn)[0][0]:.12f}")
    for pp in (5, 7):
        mons_, Mv_ = monomial_values(pp, 1)
        say(f"NAMED {pp} 1 x3 {negativities(np.array([[1]]), Mv_, pp, 1)[0][0]:.12f}")
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


def combine():
    global LOG
    best, named = {}, {}
    for line in open(os.path.join(HERE, "cubic_magic_run.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("BEST ") and f[1].isdigit():
            best[int(f[1]), int(f[2])] = dict(N=float(f[4]), share=float(f[5]), nvals=int(f[7]), pts=int(f[8]),
                                              form=f[9] if len(f) > 9 else "")
        elif line.startswith("NAMED "):
            named[int(f[1]), int(f[2]), f[3]] = float(f[4])
    cal = [l.split() for l in open(os.path.join(HERE, "cubic_magic_calibrate.log"), encoding="utf-8")
           if l.startswith("CALIBRATE ")][0]
    LOG = open(os.path.join(HERE, "cubic_magic_combined.log"), "w", encoding="utf-8")
    S = lambda N: 1 + 2 * N
    per = lambda N, n: S(N) ** (1 / n)                                    # sum of sizes per wheel
    for (p, n), b in sorted(best.items()):
        ref = SEARCH.get((p, n))
        say(f"  {n} wheels of {p}: best cubic {b['N']:.9f} ({b['share']:.4f} of the ceiling; {b['nvals']} values; "
            f"{b['pts']} points on its curve; form {b['form']})" + (f"; best by search {ref:.9f}" if ref else ""))
    k1 = all(b["share"] < 1 - 1e-9 for b in best.values())
    k2 = all(abs(best[p, 2]["N"] - SEARCH[p, 2]) < 1e-6 for p in (5, 7))
    k3 = best[3, 3]["N"] <= NORM[3] + 1e-9
    k4 = best[5, 3]["N"] > NORM[5] + 1e-9
    k5 = best[7, 3]["N"] <= NORM[7] + 1e-9
    k6 = all(per(best[p, 3]["N"], 3) > max(per(named[p, 3, "xyz"], 3), S(named.get((p, 1, "x3"), 0.0))) + 1e-9
             for p in (5, 7)) and per(best[3, 3]["N"], 3) > per(named[3, 3, "xyz"], 3) + 1e-9
    for name, ok, what in (
            ("K0", cal[1] == "True", "calibration: the Walsh identity against the state's own Wigner function, and round "
                                     "10's norm states"),
            ("K1", k1, "no cubic-phase state reaches the ceiling (forced, by the identity and Mesnager, Ozbudak and Sinak)"),
            ("K2", k2, "two wheels of 5 and of 7: the best cubic state reaches round 9's search best"),
            ("K3", k3, "three wheels of 3: no cubic form beats the norm form's 17/9"),
            ("K4", k4, "three wheels of 5: some cubic form beats the norm form's 4.252724"),
            ("K5", k5, "three wheels of 7: no sampled cubic form beats the norm form's 7.902228"),
            ("K6", k6, "per wheel, the best cubic state on three wheels beats the CCZ-type state xyz and the single-wheel "
                       "cubic x^3 (at 3: beats xyz)")):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    LOG.close()


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"calibrate": calibrate, "run": run, "combine": combine}[part]()
