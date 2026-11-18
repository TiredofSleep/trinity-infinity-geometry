"""fine_phases.py -- round 30 of PREREG.md: diagonal magic states whose phases are p^2-th roots of unity.

    "Livne proof first, then the p^2-root phases"  -- the author, 17 November 2026

Round 29 measured the phase states psi_f = sum_x w^f(x)|x>/sqrt p, w = exp(2 pi i/p): the diagonal gates whose phases
are p-th roots of unity.  The Clifford hierarchy also holds gates whose phases are p^m-th roots of unity (Cui,
Gottesman and Krishna); the qutrit T gate is one, with ninth roots.  This round takes m = 2: the fine-phase states
    psi_g = p^(-1/2) sum_x z^g(x) |x>,   z = exp(2 pi i/p^2),   g: F_p -> Z/p^2,
and, for comparison, diagonal states with arbitrary real phases.  The measure is round 29's: S = sum |W|.

  python fine_phases.py calibrate   # before the registration: the Wigner function; Li and Luo at p = 3 -> fine_phases_calibrate.log
  python fine_phases.py test        # round 30: P1-P5                                                     -> fine_phases_test.log

numpy + scipy + one_wheel.py.  Below-normal priority; four worker processes for the large primes.  ASCII output.
"""
import itertools
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
import sympy
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import one_wheel as ow  # noqa: E402  (sets below-normal priority on import, through edge_rule and coin_at_five)

SEED = 20261117
LOG = None
FAILS = []


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(name, ok, detail=""):
    say(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))
    if not ok:
        FAILS.append(name)


def size_from_phases(phi, p):
    """S = sum |W| for the diagonal state sum_x exp(i phi(x)) |x> / sqrt p, phi real (an array of length p)"""
    h = pow(2, -1, p)
    q, y = np.arange(p)[:, None], np.arange(p)[None, :]
    G = np.exp(1j * (phi[(q + y * h) % p] - phi[(q - y * h) % p]))
    return float(np.abs((np.fft.fft(G, axis=1) / p ** 2).real).sum())


def sizes_batch(PHI, p):
    """S for a batch of phase vectors (rows of PHI)"""
    h = pow(2, -1, p)
    q, y = np.arange(p)[:, None], np.arange(p)[None, :]
    A, B = (q + y * h) % p, (q - y * h) % p
    G = np.exp(1j * (PHI[:, A] - PHI[:, B]))
    return np.abs((np.fft.fft(G, axis=2) / p ** 2).real).sum(axis=(1, 2))


def fine_exhaustive(p, batch=50000):
    """every g: F_p -> Z/p^2 with g(0) = 0 (the global phase): the best S, its g, and how many beat a threshold later"""
    N = p * p
    best, arg = -1.0, None
    allS = []
    it = itertools.product(range(N), repeat=p - 1)
    while True:
        C = np.array(list(itertools.islice(it, batch)), dtype=np.int64)
        if len(C) == 0:
            break
        G = np.concatenate([np.zeros((len(C), 1), dtype=np.int64), C], axis=1)
        S = sizes_batch(2 * np.pi * G / N, p)
        allS.append(S)
        i = int(np.argmax(S))
        if S[i] > best:
            best, arg = float(S[i]), G[i].copy()
    return best, arg, np.concatenate(allS)


def general_optimum(p, starts, rng):
    """the largest S over arbitrary real phases (phi(0) = 0), by Nelder-Mead from random starts, then Powell"""
    f = lambda v: -size_from_phases(np.concatenate([[0.0], v]), p)
    best, bestv = -1.0, None
    for _ in range(starts):
        v0 = rng.uniform(0, 2 * np.pi, p - 1)
        r = minimize(f, v0, method="Nelder-Mead", options={"maxiter": 4000, "xatol": 1e-9, "fatol": 1e-12})
        r = minimize(f, r.x, method="Powell", options={"xtol": 1e-10, "ftol": 1e-13})
        if -r.fun > best:
            best, bestv = -r.fun, np.mod(r.x, 2 * np.pi)
    return best, bestv


# ------------------------------------------------------------------ calibrate
def calibrate():
    global LOG
    if "--runs" in sys.argv:
        os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
        LOG = open(os.path.join(HERE, "runs", "fine_phases_calibrate.log"), "w", encoding="utf-8")
    else:
        LOG = open(os.path.join(HERE, "fine_phases_calibrate.log"), "w", encoding="utf-8")
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    say("fine_phases.py calibrate -- round 30, before the registration")
    say()
    ok = True
    for p in (3, 5, 7, 11, 13):
        for _ in range(5):
            phi = rng.uniform(0, 2 * np.pi, p)
            W = ow.wigner_state(np.exp(1j * phi) / math.sqrt(p), p)
            ok &= abs(np.abs(W).sum() - size_from_phases(phi, p)) < 1e-12
    check("C1 the diagonal-state Wigner norm equals the one computed from the state, p = 3..13", ok)
    # Li and Luo: the qutrit T gate (ninth roots) is optimal among all diagonal gates
    best3, arg3, all3 = fine_exhaustive(3)
    T3 = size_from_phases(2 * np.pi * np.array([0, 1, 8]) / 9, 3)
    gen3, v3 = general_optimum(3, 200, rng)
    say(f"     p = 3: best of the 81 ninth-root phase states S = {best3:.6f} at g = {[int(v) for v in arg3]}; Howard and Vala's "
        f"T state (0, 1, -1)/9: {T3:.6f}; arbitrary phases (200 starts): {gen3:.6f}")
    check("C2 at p = 3 the best ninth-root state is the qutrit T state, and no diagonal state with arbitrary phases beats "
          "it (Li and Luo)", abs(best3 - T3) < 1e-9 and gen3 < T3 + 1e-6)
    # the p-th-root T state at 5 and 7, as round 29 found it
    T5 = max(ow.T_size(t, 5) for t in ow.classes(5))
    T7 = max(ow.T_size(t, 7) for t in ow.classes(7))
    check("C3 round 29's best T states: S = 1 + 2/sqrt 5 at 5 and 2.450304 at 7",
          abs(T5 - (1 + 2 / math.sqrt(5))) < 1e-12 and abs(T7 - 2.450304) < 1e-6, f"{T5:.6f}, {T7:.6f}")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


# ------------------------------------------------------------------ test (round 30)
def _random_fine(p):
    """S/sqrt p for ten seeded random g: F_p -> Z/p^2, and for the structured g = x^a mod p^2 (a = 2, 3, 4)"""
    ow.er.low_priority()
    rng = np.random.default_rng([SEED, p])
    N = p * p
    rand = [size_from_phases(2 * np.pi * rng.integers(0, N, p) / N, p) / math.sqrt(p) for _ in range(10)]
    x = np.arange(p, dtype=object)
    struct = {a: size_from_phases(2 * np.pi * np.array([int(v) ** a % N for v in x], dtype=float) / N, p) / math.sqrt(p)
              for a in (2, 3, 4)}
    return p, rand, struct


def test():
    global LOG
    LOG = open(os.path.join(HERE, "fine_phases_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    rng = np.random.default_rng([SEED, 30])
    say("Round 30: diagonal magic states with p^2-th-root phases (PREREG.md)")
    say()
    T5 = 1 + 2 / math.sqrt(5)
    T7 = max(ow.T_size(t, 7) for t in ow.classes(7))

    best5, arg5, all5 = fine_exhaustive(5)
    beat5 = int((all5 > T5 + 1e-9).sum())
    say(f"  p = 5: all {len(all5)} fine-phase states (g(0) = 0): best S = {best5:.6f} ({best5 / math.sqrt(5):.4f} of "
        f"sqrt 5) at g = {[int(v) for v in arg5]} (in 25ths); {beat5} beat the T state's {T5:.6f}")
    check("P1 at 5 some fine-phase state beats the T state", best5 > T5 + 1e-9)
    gen5, v5 = general_optimum(5, 300, rng)
    say(f"  p = 5: arbitrary phases (300 starts): S = {gen5:.6f} ({gen5 / math.sqrt(5):.4f} of sqrt 5) at phases/(2 pi) = "
        f"{[round(float(v) / (2 * np.pi), 4) for v in np.concatenate([[0.0], v5])]}")
    check("P2 at 5 the best fine-phase state is within 1% of the best diagonal state with arbitrary phases",
          best5 >= 0.99 * gen5, f"{best5:.6f} against {gen5:.6f}")
    gen7, v7 = general_optimum(7, 400, rng)
    say(f"  p = 7: arbitrary phases (400 starts): S = {gen7:.6f} ({gen7 / math.sqrt(7):.4f} of sqrt 7) at phases/(2 pi) = "
        f"{[round(float(v) / (2 * np.pi), 4) for v in np.concatenate([[0.0], v7])]}; the T state {T7:.6f}")
    check("P3 at 7 some diagonal state with arbitrary phases beats the T state", gen7 > T7 + 1e-6,
          f"{gen7:.6f} against {T7:.6f}")
    # fine phases at 7, sampled
    N7 = 49
    bestf7 = -1.0
    for _ in range(50):
        G = np.concatenate([np.zeros((20000, 1), dtype=np.int64), rng.integers(0, N7, (20000, 6))], axis=1)
        bestf7 = max(bestf7, float(sizes_batch(2 * np.pi * G / N7, 7).max()))
    say(f"  read: p = 7, 10^6 sampled fine-phase states: best S = {bestf7:.6f}")
    say()

    from multiprocessing import Pool
    PL = [int(p) for p in sympy.primerange(500, 1001)]
    with Pool(4) as pool:
        res = pool.map(_random_fine, PL)
    H = {p: ow.haar_size(p) / math.sqrt(p) for p in PL}
    mean_rand = float(np.mean([v for _, r, _ in res for v in r]))
    mean_haar = float(np.mean([H[p] for p in PL for _ in range(10)]))
    say(f"  primes 500..1000 ({len(PL)}), ten random fine-phase states each: mean S/sqrt(p) = {mean_rand:.5f}; the exact "
        f"Haar mean over the same primes {mean_haar:.5f}")
    check("P4 random fine-phase states have the random-state value: the mean S/sqrt(p) is within 0.002 of the Haar mean",
          abs(mean_rand - mean_haar) < 0.002, f"difference {mean_rand - mean_haar:+.5f}")
    for a in (2, 3, 4):
        vals = [s[a] for _, _, s in res]
        say(f"  read: g = x^{a} mod p^2: mean S/sqrt(p) = {np.mean(vals):.5f} (range {min(vals):.5f} .. {max(vals):.5f})")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


if __name__ == "__main__":
    {"calibrate": calibrate, "test": test}[sys.argv[1] if len(sys.argv) > 1 else "calibrate"]()
