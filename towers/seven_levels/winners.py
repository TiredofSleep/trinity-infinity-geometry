"""winners.py -- round 33 of PREREG.md: what the diagonal states that beat the T gate share.

    "keep going, find what the p = 2 winners share"  -- the author, 17 November 2026

The T state's Wigner function W(q, s) = S_t(3c q^2 - s)/p^2 is fixed by every map (q, s) -> (q + d, s + 6c d q + 3c d^2)
(p of them), by the reflection (q, s) -> (-q, s) (complex conjugation and parity: the phase c x^3 is odd), and, when
p = 1 (mod 3), by (q, s) -> (z q, s / z) for a cube root of unity z.  So its affine symmetry group has order 2p, or 6p
when p = 1 (mod 3).  The states that beat it (rounds 30-32) are asked what symmetry they keep.

  python winners.py explore   # the reads before the registration                 -> winners_explore.log
  python winners.py test      # round 33 at 41 and 47 (= 2 mod 3)                   -> winners_test.log
  python winners.py forced    # F1 to 13, for verify_seven_levels.py (under a minute)        -> runs/winners_forced.log

numpy + scipy + diagonal_coin.py (round 31's search) + one_wheel.py.  Four worker processes at below-normal priority.
"""
import itertools
import math
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np
from scipy.optimize import minimize

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import diagonal_coin as dc  # noqa: E402
import one_wheel as ow  # noqa: E402

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


def w_symmetries(W, p, tol):
    """every affine map u -> g u + t of F_p^2 (det g = +-1) with W(g u + t) = W(u): (det, g, t)"""
    q, s = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    out = []
    for a, b, c, d in itertools.product(range(p), repeat=4):
        det = (a * d - b * c) % p
        if det not in (1, p - 1):
            continue
        Q, S = (a * q + b * s) % p, (c * q + d * s) % p
        for t1 in range(p):
            for t2 in range(p):
                if np.max(np.abs(W[(Q + t1) % p, (S + t2) % p] - W)) < tol:
                    out.append((1 if det == 1 else -1, (a, b, c, d), (t1, t2)))
    return out


# ------------------------------------------------------------------ all climbs, and the odd-restricted search
def _climbs(args):
    p, chunk = args
    ow.er.low_priority()
    geo = dc.Geometry(p)
    return [dc.climb(geo, v0) for v0 in chunk]


def all_climbs(p):
    from multiprocessing import Pool
    st = dc.starts(p)
    with Pool(4) as pool:
        res = pool.map(_climbs, [(p, st[i::4]) for i in range(4)])
    out = [r for chunk in res for r in chunk]
    out.sort(key=lambda r: -r[0])
    return out


def odd_full(u, p):
    phi = np.zeros(p)
    h = (p - 1) // 2
    phi[1:h + 1] = u
    phi[p - h:] = -u[::-1]
    return phi


def odd_objective(u, geo, eps):
    p = geo.p
    f, g = geo.smoothed(odd_full(u, p)[1:], eps)
    full = np.concatenate([[0.0], g])
    h = (p - 1) // 2
    return f, full[1:h + 1] - full[p - 1:p - h - 1:-1]


def _odd_chunk(args):
    p, chunk = args
    ow.er.low_priority()
    geo = dc.Geometry(p)
    best = -1.0
    for u in chunk:
        for eps in (1e-5, 1e-8):
            u = minimize(odd_objective, u, args=(geo, eps), jac=True, method="L-BFGS-B", options={"maxiter": 3000}).x
        best = max(best, geo.size(odd_full(u, p)[1:]))
    return best


def odd_best(p):
    """the best odd phase state, phi(-x) = -phi(x), from 600 random starts and 30 perturbed copies of each T class"""
    from multiprocessing import Pool
    rng = np.random.default_rng([20261117, 33, p])
    h = (p - 1) // 2
    st = [rng.uniform(0, 2 * np.pi, h) for _ in range(600)]
    for t in ow.classes(p):
        base = dc.t_phases(t, p)[1:h + 1]
        st += [base + rng.normal(0, 0.3, h) for _ in range(30)]
    with Pool(4) as pool:
        return max(pool.map(_odd_chunk, [(p, st[i::4]) for i in range(4)]))


# ------------------------------------------------------------------ explore (before the registration)
def explore():
    global LOG
    if "--runs" in sys.argv:
        os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
        LOG = open(os.path.join(HERE, "runs", "winners_explore.log"), "w", encoding="utf-8")
    else:
        LOG = open(os.path.join(HERE, "winners_explore.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("winners.py explore -- what the diagonal states that beat the T gate share (reads before round 33)")
    say()
    ok = True
    for p in (5, 7, 11, 13, 17, 19):
        for t in ow.classes(p):
            sym = w_symmetries(dc.Geometry(p).wigner(dc.t_phases(t, p))[1], p, 1e-9)
            n_u, n_a = sum(1 for e, *_ in sym if e == 1), sum(1 for e, *_ in sym if e == -1)
            ok &= n_u == n_a == (3 * p if p % 3 == 1 else p)
    check("F1 every T state has exactly 2p affine symmetries of its Wigner function (p symplectic, p antisymplectic), "
          "or 6p when p = 1 (mod 3), p = 5..19, every class", ok)
    say()
    say("  p  mod3  best/sqrt p  climbs reaching it  distinct optima  best odd/sqrt p  gap")
    for p in (5, 11, 17, 23, 29, 31, 37, 43):
        cl = all_climbs(p)
        best = cl[0][0]
        hits = sum(1 for s, _ in cl if s > best - 1e-6)
        sigs = {tuple(np.round(np.sort(np.abs(dc.Geometry(p).wigner(np.concatenate([[0.0], v]))[1]).ravel()), 5))
                for s, v in cl}
        ob = odd_best(p)
        say(f"  {p:2d}  {p % 3}     {best / math.sqrt(p):.4f}       {hits:3d} of {len(cl)}         {len(sigs):3d}           "
            f"{ob / math.sqrt(p):.4f}       {(best - ob) / math.sqrt(p):+.4f}")
        if p == 5:
            phi = np.concatenate([[0.0], cl[0][1]])
            x = np.arange(5)
            psi = (phi - 2 * np.pi * (x * x) / 5) / (2 * np.pi) % 1          # remove the Clifford phase w^(x^2)
            sym = w_symmetries(dc.Geometry(5).wigner(phi)[1], 5, 1e-6)
            say(f"      at 5: phases minus x^2/5, in turns: {[round(float(v), 4) for v in psi]}; odd: "
                f"{max(abs((psi[k] + psi[(-k) % 5] + 0.5) % 1 - 0.5) for k in range(5)) < 1e-4}; W's affine symmetries: "
                f"{sum(1 for e, *_ in sym if e == 1)} symplectic, {sum(1 for e, *_ in sym if e == -1)} antisymplectic")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


# ------------------------------------------------------------------ test (round 33)
def test():
    global LOG
    LOG = open(os.path.join(HERE, "winners_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("Round 33: what the states that beat the T gate share, at 41 and 47 (PREREG.md)")
    say()
    for p, (n1, n2, n3) in ((41, ("W1a", "W2a", "W3a")), (47, ("W1b", "W2b", "W3b"))):
        T = dc.best_T(p)
        cl = all_climbs(p)
        best = cl[0][0]
        hits = sum(1 for s, _ in cl if s > best - 1e-6)
        ob = odd_best(p)
        say(f"  p = {p}: best of {len(cl)} climbs {best / math.sqrt(p):.4f} sqrt p (T {T / math.sqrt(p):.4f}); reached by "
            f"{hits}; the best odd state {ob / math.sqrt(p):.4f}; gap {(best - ob) / math.sqrt(p):+.4f} sqrt p")
        check(f"{n1} at {p} the search beats the T state", best > T + 1e-6)
        check(f"{n2} at {p} the best value is reached by exactly one climb", hits == 1, f"{hits}")
        check(f"{n3} at {p} the best odd state falls short of it by more than 0.003 sqrt p", (best - ob) / math.sqrt(p) > 0.003,
              f"{(best - ob) / math.sqrt(p):+.4f}")
        say(f"     ({(time.time() - t0) / 60:.1f} minutes so far)")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


def forced():
    """F1 alone, for the verifier: the T state's affine symmetry group, exactly, at every class for p = 5..13 (the explore
    log records it to 19; counting every affine map at 19 takes minutes)"""
    global LOG
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    LOG = open(os.path.join(HERE, "runs", "winners_forced.log"), "w", encoding="utf-8")
    ok = True
    for p in (5, 7, 11, 13):
        for t in ow.classes(p):
            sym = w_symmetries(dc.Geometry(p).wigner(dc.t_phases(t, p))[1], p, 1e-9)
            n_u, n_a = sum(1 for e, *_ in sym if e == 1), sum(1 for e, *_ in sym if e == -1)
            ok &= n_u == n_a == (3 * p if p % 3 == 1 else p)
    check("F1 every T state has 2p affine symmetries, or 6p when p = 1 (mod 3), p = 5..13, every class", ok)
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


if __name__ == "__main__":
    {"explore": explore, "test": test, "forced": forced}[sys.argv[1] if len(sys.argv) > 1 else "explore"]()
