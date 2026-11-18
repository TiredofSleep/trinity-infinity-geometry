"""diagonal_coin.py -- round 31 of PREREG.md: is the T gate the best diagonal gate exactly when p = 1 (mod 3)?

    "1 yes, round 31 first, then the email"  -- the author, 17 November 2026

Rounds 29 and 30 found the T state the most Wigner-negative of all diagonal states at p = 3 (Li and Luo) and,
numerically, at p = 7, but beaten at 5 (Feng and Luo) and at 11 (round 29). The T states split into three classes when
p = 1 (mod 3) and form one when p = 2 (mod 3).  This round asks whether that is a coin: optimal when p = 1 (mod 3),
beaten when p = 2.

The search, fixed before the test.  A diagonal state is psi_phi = sum_x exp(i phi(x)) |x> / sqrt p with phi(0) = 0.
From every start, L-BFGS-B maximizes the smoothed size S_eps = sum sqrt(W^2 + eps^2) with its exact gradient, first
with eps = 1e-5 and then with eps = 1e-8; the exact S = sum |W| is taken at the end.  The starts at each prime:
  400 uniform random phase vectors; 100 random p-th-root phase functions; 100 random p^2-th-root phase functions;
  and, for each class of T state, 30 copies of its phases plus Gaussian noise of 0.3 radians.
A state "beats" the T state when its S exceeds the best T class's by more than 1e-6.  A witness is decisive; finding
nothing is numerical evidence, not a proof.

  python diagonal_coin.py calibrate   # before the registration: the gradient, and the search at 5, 7, 11 -> diagonal_coin_calibrate.log
  python diagonal_coin.py test        # round 31: 13, 17, 19, 23                                      -> diagonal_coin_test.log
  python diagonal_coin.py edge        # round 32: where the coin ends, 29, 31, 37, 43 (same search)    -> diagonal_coin_edge.log

numpy + scipy + one_wheel.py + fine_phases.py.  Four worker processes at below-normal priority.  ASCII output.
"""
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
import one_wheel as ow  # noqa: E402  (sets below-normal priority on import)
import fine_phases as fp  # noqa: E402

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


class Geometry:
    def __init__(self, p):
        self.p = p
        h = pow(2, -1, p)
        q, y = np.arange(p)[:, None], np.arange(p)[None, :]
        self.A, self.B = (q + y * h) % p, (q - y * h) % p

    def wigner(self, phi):
        E = np.exp(1j * (phi[self.A] - phi[self.B]))
        return E, (np.fft.fft(E, axis=1) / self.p ** 2).real

    def smoothed(self, v, eps):
        """-S_eps and its gradient in the p - 1 free phases"""
        p = self.p
        phi = np.concatenate([[0.0], v])
        E, W = self.wigner(phi)
        r = np.sqrt(W * W + eps * eps)
        c = W / r
        C = np.fft.fft(c, axis=1)                                   # C(q, y) = sum_s c(q, s) w^(-s y)
        G = (1j * E * C).real / p ** 2
        grad = np.bincount(self.A.ravel(), G.ravel(), p) - np.bincount(self.B.ravel(), G.ravel(), p)
        return -float(r.sum()), -grad[1:]

    def size(self, v):
        return float(np.abs(self.wigner(np.concatenate([[0.0], v]))[1]).sum())


def climb(geo, v0):
    v = v0
    for eps in (1e-5, 1e-8):
        r = minimize(geo.smoothed, v, args=(eps,), jac=True, method="L-BFGS-B", options={"maxiter": 3000})
        v = r.x
    return geo.size(v), np.mod(v, 2 * np.pi)


def t_phases(t, p):
    """the phases of the T state of class t, f(x) = 4t x^3 (so that t = c/4)"""
    x = np.arange(p)
    return 2 * np.pi * ((4 * t * x ** 3) % p) / p


def starts(p):
    rng = np.random.default_rng([SEED, 31, p])
    out = [rng.uniform(0, 2 * np.pi, p - 1) for _ in range(400)]
    out += [2 * np.pi * rng.integers(0, p, p - 1) / p for _ in range(100)]
    out += [2 * np.pi * rng.integers(0, p * p, p - 1) / (p * p) for _ in range(100)]
    for t in ow.classes(p):
        base = t_phases(t, p)
        out += [np.mod(base[1:] - base[0] + rng.normal(0, 0.3, p - 1), 2 * np.pi) for _ in range(30)]
    return out


def _search(args):
    p, chunk = args
    ow.er.low_priority()
    geo = Geometry(p)
    best, bestv = -1.0, None
    for v0 in chunk:
        s, v = climb(geo, v0)
        if s > best:
            best, bestv = s, v
    return best, bestv


def search(p, workers=4):
    from multiprocessing import Pool
    st = starts(p)
    chunks = [st[i::workers] for i in range(workers)]
    with Pool(workers) as pool:
        res = pool.map(_search, [(p, c) for c in chunks])
    best, bestv = max(res, key=lambda r: r[0])
    return best, bestv, len(st)


def best_T(p):
    return max(ow.T_size(t, p) for t in ow.classes(p))


def interpolation_degree(f, p):
    """the degree of the polynomial of degree < p through the values f(0..p-1) over F_p (Gaussian elimination mod p)"""
    M = [[pow(x, k, p) for k in range(p)] + [f[x] % p] for x in range(p)]
    for c in range(p):
        r = next(i for i in range(c, p) if M[i][c] % p)
        M[c], M[r] = M[r], M[c]
        inv = pow(M[c][c], -1, p)
        M[c] = [(v * inv) % p for v in M[c]]
        for i in range(p):
            if i != c and M[i][c]:
                M[i] = [(a - M[i][c] * b) % p for a, b in zip(M[i], M[c])]
    coeffs = [M[k][p] for k in range(p)]
    return max((k for k in range(p) if coeffs[k]), default=0)


def describe(v, p):
    """the phases in units of 2 pi / p, and whether they are p-th roots (then the polynomial degree)"""
    ph = np.concatenate([[0.0], v]) / (2 * np.pi) * p
    near = np.round(ph) % p
    on_grid = bool(np.max(np.abs(((ph - np.round(ph)) + 0.5) % 1 - 0.5)) < 1e-4)
    deg = None
    if on_grid:
        deg = interpolation_degree([int(x) for x in near], p)
    return [round(float(x), 4) for x in ph], on_grid, deg


def calibrate():
    global LOG
    if "--runs" in sys.argv:
        os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
        LOG = open(os.path.join(HERE, "runs", "diagonal_coin_calibrate.log"), "w", encoding="utf-8")
    else:
        LOG = open(os.path.join(HERE, "diagonal_coin_calibrate.log"), "w", encoding="utf-8")
    t0 = time.time()
    rng = np.random.default_rng(SEED)
    say("diagonal_coin.py calibrate -- round 31, before the registration")
    say()
    ok = True
    for p in (5, 7, 13):
        geo = Geometry(p)
        for _ in range(3):
            v = rng.uniform(0, 2 * np.pi, p - 1)
            f0, g = geo.smoothed(v, 1e-5)
            num = np.array([(geo.smoothed(v + 1e-6 * np.eye(p - 1)[i], 1e-5)[0] - f0) / 1e-6 for i in range(p - 1)])
            ok &= np.max(np.abs(num - g)) < 1e-4 * max(1.0, np.max(np.abs(g)))
            ok &= abs(geo.size(v) - fp.size_from_phases(np.concatenate([[0.0], v]), p)) < 1e-12
    check("K1 the smoothed size's gradient agrees with finite differences, and the size with round 30's, p = 5, 7, 13", ok)
    for p in (11, 13, 17, 19, 23):
        say(f"     the best T class at {p} (p = {p % 3} mod 3): S = {best_T(p):.6f} = {best_T(p) / math.sqrt(p):.4f} sqrt p")
    b5, v5, n5 = search(5)
    b7, v7, n7 = search(7)
    b11, v11, n11 = search(11)
    say(f"     5: best of {n5} climbs S = {b5:.6f}; 7: {b7:.6f} (T {best_T(7):.6f}); 11: {b11:.6f} (T {best_T(11):.6f}, "
        f"round 29's degree-10 phase 2.877321)")
    check("K2 the search reproduces rounds 29 and 30: at 5 it beats T (1.977576), at 7 it finds only T, and at 11 it "
          "reaches round 29's witness", abs(b5 - 1.977576) < 1e-5 and abs(b7 - best_T(7)) < 1e-6 and b11 >= 2.877321 - 1e-6)
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


def test():
    global LOG
    LOG = open(os.path.join(HERE, "diagonal_coin_test.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("Round 31: is the T gate the best diagonal gate exactly when p = 1 (mod 3)? (PREREG.md)")
    say()
    names = {13: "R1", 17: "R2", 19: "R3", 23: "R4"}
    for p in (13, 17, 19, 23):
        T = best_T(p)
        b, v, n = search(p)
        ph, on_grid, deg = describe(v, p)
        beats = b > T + 1e-6
        say(f"  p = {p} (p = {p % 3} mod 3): best of {n} climbs S = {b:.6f} = {b / math.sqrt(p):.4f} sqrt p; the best T class "
            f"{T:.6f} = {T / math.sqrt(p):.4f} sqrt p; beats T: {beats}")
        say(f"     its phases in units of 2 pi/p: {ph}; on the p-th-root grid: {on_grid}"
            + (f", a polynomial of degree {deg}" if on_grid else ""))
        if p % 3 == 1:
            check(f"{names[p]} at {p} (= 1 mod 3) the search finds nothing above the best T class", not beats,
                  f"{b:.6f} against {T:.6f}")
        else:
            check(f"{names[p]} at {p} (= 2 mod 3) the search finds a diagonal state above the T state", beats,
                  f"{b:.6f} against {T:.6f}")
        say(f"     ({(time.time() - t0) / 60:.1f} minutes so far)")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


def edge():
    """round 32: the same search at 29 (= 2 mod 3, the control), and 31, 37, 43 (= 1 mod 3, where the best T class has
    dropped below the level the other diagonal states reached at 5 to 23)"""
    global LOG
    LOG = open(os.path.join(HERE, "diagonal_coin_edge.log"), "w", encoding="utf-8")
    t0 = time.time()
    say("Round 32: where the coin ends (PREREG.md)")
    say()
    for p, name in ((29, "E1"), (31, "E2"), (37, "E3"), (43, "E4")):
        T = best_T(p)
        b, v, n = search(p)
        ph, on_grid, deg = describe(v, p)
        beats = b > T + 1e-6
        say(f"  p = {p} (p = {p % 3} mod 3): best of {n} climbs S = {b:.6f} = {b / math.sqrt(p):.4f} sqrt p; the best T class "
            f"{T:.6f} = {T / math.sqrt(p):.4f} sqrt p; beats T: {beats}")
        say(f"     on the p-th-root grid: {on_grid}" + (f", a polynomial of degree {deg}" if on_grid else ""))
        if p == 29:
            check(f"{name} at 29 (= 2 mod 3, the control) the search beats the T state", beats, f"{b:.6f} against {T:.6f}")
            check(f"{name}b and its best reaches 0.875 sqrt 29, the level of 5 to 23", b / math.sqrt(p) >= 0.875,
                  f"{b / math.sqrt(p):.4f}")
        else:
            check(f"{name} at {p} (= 1 mod 3) the coin breaks: the search beats the best T class", beats,
                  f"{b:.6f} against {T:.6f}")
        say(f"     ({(time.time() - t0) / 60:.1f} minutes so far)")
    say()
    say(f"time {(time.time() - t0) / 60:.1f} minutes")
    say(f"{'ALL PASS' if not FAILS else 'FAILED: ' + ', '.join(FAILS)}")
    LOG.close()


if __name__ == "__main__":
    {"calibrate": calibrate, "test": test, "edge": edge}[sys.argv[1] if len(sys.argv) > 1 else "calibrate"]()
