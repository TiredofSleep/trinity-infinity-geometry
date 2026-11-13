"""oscillator_states.py -- round 11 of PREREG.md: the magic of the oscillator states, committed with its predictions
before the run.

    "zoom out, and look for work that shares ground, let's see if what we have is useful"  -- the author, 12 Nov 2026

Round 8's two wheels are the two kinds of maximal torus in SL(2, p): the multiplying wheel (x -> ax, p - 1 steps) is
the split torus, and the turning wheel (p + 1 steps) the non-split one.  Their one-line eigenvectors are the
oscillator system of Gurevich, Hadani and Sochen, and the Hecke eigenfunctions of the quantized cat map.  This script
computes the Wigner negativity of every one of them at every prime from 5 to 401:
  - the split torus: the p - 2 states sum over x != 0 of chi(x)|x> / sqrt(p - 1), for the nontrivial characters chi
    of F_p* (the trivial character shares its eigenspace with |0>, so that eigenspace has two dimensions and is left
    out);
  - the non-split torus: the p eigenvectors of the chirp U = sum_(x,y) w^((t/4)(x^2 + y^2) - xy) |x><y| / sqrt p, a
    Clifford unitary whose symplectic map is [[t/2, 1], [t^2/4 - 1, t/2]]; t is chosen so that this map has order
    p + 1, and the script checks U's action on X and Z.
The Wigner function is round 3's: W(q, k) = (1/p) sum_s conj psi(q + s) psi(q - s) w^(2ks).  For each state the run
logs the negativity N, S/sqrt p (S = 1 + 2N, the sum of sizes) and the ratio mu4/mu2^2 of its Wigner values off the
origin.  A state that a torus fixes has a Wigner function constant on the torus's orbits, so it takes at most p + 2
values; the script checks that too.  `combine` scores O0 to O4.

numpy only.  One process, one thread, below-normal priority.  ASCII output.
Run:  python oscillator_states.py calibrate   (seconds; writes oscillator_states_calibrate.log)
      python oscillator_states.py run         (about six minutes; writes oscillator_states_run.log)
      python oscillator_states.py combine     (writes oscillator_states_combined.log)
"""
import ctypes
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
PRIMES = [x for x in range(5, 402) if all(x % d for d in range(2, int(x ** 0.5) + 1))]
ST, GAUSS, ARCSINE = 8 / (3 * np.pi), np.sqrt(2 / np.pi), 2 * np.sqrt(2) / np.pi
# round 8's logged bests of the full tori's families (two_wheels_A.log, two_wheels_B.log): the turning wheel's order
# p + 1, whose eigenspaces all have one dimension
ROUND8_TURNING = {5: 0.556677223, 7: 0.721570212, 11: 1.022656198, 13: 1.105228575, 17: 1.377452883, 19: 1.458481547,
                  23: 1.627721703, 29: 1.901698621}
# the Legendre state, one of the split torus's one-line states (rounds 1 to 7; verify_seven_levels.py)
LEGENDRE = {7: 0.728262097006, 17: 1.250924335054, 19: 1.356950270213, 23: 1.341641910165, 29: 1.878678879531,
            31: 1.736567405507}
# the best states known from rounds 2 to 7, found by searches
WINNERS = {7: 0.732522000011, 11: 1.032586, 13: 1.168522054, 17: 1.402567380, 19: 1.507862142, 23: 1.700022328,
           29: 1.963715306, 31: 2.045297}
LOG = None
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


# ------------------------------------------------------------------ the states
def wigner(Psi, p):
    """W[m, q, k] = (1/p) sum_s conj psi_m(q + s) psi_m(q - s) w^(2ks), one Fourier transform per q"""
    x = np.arange(p)
    plus, minus = (x[:, None] + x[None, :]) % p, (x[:, None] - x[None, :]) % p
    two = (2 * x) % p
    out = []
    for i in range(0, len(Psi), 16):
        P = Psi[i:i + 16]
        f = P.conj()[:, plus] * P[:, minus]
        out.append(np.fft.ifft(f, axis=2)[:, :, two].real)
    return np.concatenate(out)


def split_states(p):
    g = next(a for a in range(2, p) if len({pow(a, e, p) for e in range(1, p)}) == p - 1)
    log = np.zeros(p, dtype=np.int64)
    for e in range(p - 1):
        log[pow(g, e, p)] = e
    Psi = np.zeros((p - 2, p), complex)
    for j in range(1, p - 1):
        Psi[j - 1, 1:] = np.exp(2j * np.pi * j * log[1:] / (p - 1)) / np.sqrt(p - 1)
    return Psi


def mat_order(S, p, limit):
    M, I = S.copy(), np.eye(2, dtype=np.int64)
    for n in range(1, limit + 1):
        if np.array_equal(M % p, I):
            return n
        M = (M @ S) % p
    return None


def weyl_label(M, p):
    """(a, b) with M proportional to X^a Z^b, where X|x> = |x + 1> and Z|x> = w^x |x>, or None"""
    a = int(np.argmax(np.abs(M[:, 0])))
    c = M[a, 0]
    b = int(round(np.angle(M[(1 + a) % p, 1] / c) / (2 * np.pi / p))) % p
    x = np.arange(p)
    ref = np.zeros((p, p), complex)
    ref[(x + a) % p, x] = np.exp(2j * np.pi * b * x / p)
    return (a, b) if np.allclose(M, c * ref, atol=1e-9) else None


def nonsplit_states(p):
    """the eigenvectors of a Clifford chirp whose symplectic map generates the non-split torus; with its checks"""
    i4 = pow(4, -1, p)
    for t in range(p):
        S = np.array([[t * pow(2, -1, p), 1], [(t * t * i4 - 1) % p, t * pow(2, -1, p)]], dtype=np.int64) % p
        if mat_order(S, p, 2 * (p + 1)) == p + 1:
            break
    else:
        raise ValueError(p)
    x = np.arange(p)
    U = np.exp(2j * np.pi * ((t * i4 * (x[:, None] ** 2 + x[None, :] ** 2) - x[:, None] * x[None, :]) % p) / p) / np.sqrt(p)
    X = np.roll(np.eye(p), 1, axis=0)
    Z = np.diag(np.exp(2j * np.pi * x / p))
    unitary = np.allclose(U @ U.conj().T, np.eye(p), atol=1e-10)
    lx, lz = weyl_label(U @ X @ U.conj().T, p), weyl_label(U @ Z @ U.conj().T, p)
    induced = None if lx is None or lz is None else np.array([[lx[0], lz[0]], [lx[1], lz[1]]], dtype=np.int64)
    order = None if induced is None else mat_order(induced, p, 2 * (p + 1))
    ev, V = np.linalg.eig(U)
    gap = min(abs(ev[i] - ev[j]) for i in range(p) for j in range(i))
    V = V / np.linalg.norm(V, axis=0, keepdims=True)
    ortho = np.allclose(V.conj().T @ V, np.eye(p), atol=1e-8)
    return V.T, dict(t=t, unitary=unitary, order=order, gap=gap, ortho=ortho)


def stats(W, p):
    S = np.abs(W).sum(axis=(1, 2))
    off = W.reshape(len(W), -1)[:, 1:]                                    # every point but the origin (q, k) = (0, 0)
    mu2, mu4 = (off ** 2).mean(axis=1), (off ** 4).mean(axis=1)
    levels = [1 + int((np.diff(np.sort(w.ravel() * p ** 1.5)) > 1e-7).sum()) for w in W]   # distinct values
    return (S - 1) / 2, S / np.sqrt(p), mu4 / mu2 ** 2, max(levels), np.sign(W[:, 0, 0])


# ------------------------------------------------------------------ the parts
def calibrate():
    global LOG
    LOG = open(os.path.join(HERE, "oscillator_states_calibrate.log"), "w", encoding="utf-8")
    say("the code against values already logged: round 8's turning wheel of order p + 1, and the Legendre states")
    ok_all = True
    for p, want in ROUND8_TURNING.items():
        Psi, chk = nonsplit_states(p)
        N = stats(wigner(Psi, p), p)[0]
        ok = abs(N.max() - want) < 2e-9 and chk["unitary"] and chk["order"] == p + 1 and chk["gap"] > 1e-6 and chk["ortho"]
        ok_all &= ok
        say(f"  {p}: the chirp is unitary {chk['unitary']}, its map has order {chk['order']} (p + 1 = {p + 1}), its "
            f"eigenvalues are distinct {chk['gap'] > 1e-6}, its eigenvectors orthonormal {chk['ortho']}; the best "
            f"one-line state equals round 8's {want:.9f}: {abs(N.max() - want) < 2e-9}")
    for p, want in LEGENDRE.items():
        Psi = split_states(p)
        N = stats(wigner(Psi, p), p)[0]
        j = (p - 1) // 2 - 1                                              # the character of order 2
        ok = abs(N[j] - want) < 1e-9
        ok_all &= ok
        say(f"  {p}: the split torus's state of the character of order 2 is the Legendre state, {want:.12f}: {ok}")
    say(f"CALIBRATE {ok_all}")
    LOG.close()


def run():
    global LOG
    LOG = open(os.path.join(HERE, "oscillator_states_run.log"), "w", encoding="utf-8")
    say(f"round 11: the one-line oscillator states at the {len(PRIMES)} primes from 5 to 401")
    say("TORUS p kind count bestN bestShare meanS/sqrtp sdS/sqrtp minS/sqrtp maxS/sqrtp meanR4 maxLevels bestParity "
        "checks")
    for p in PRIMES:
        ceiling = (np.sqrt(p) - 1) / 2
        for kind in ("nonsplit", "split"):
            if kind == "nonsplit":
                Psi, chk = nonsplit_states(p)
                checks = chk["unitary"] and chk["order"] == p + 1 and chk["gap"] > 1e-6 and chk["ortho"]
            else:
                Psi, checks = split_states(p), True
            N, s, r4, levels, par = stats(wigner(Psi, p), p)
            i = int(np.argmax(N))
            say(f"TORUS {p} {kind} {len(N)} {N[i]:.9f} {N[i] / ceiling:.6f} {s.mean():.6f} {s.std():.6f} {s.min():.6f} "
                f"{s.max():.6f} {r4.mean():.6f} {levels} {'even' if par[i] > 0 else 'odd'} {checks}")
    say(f"[{time.time() - T0:.0f} s]")
    LOG.close()


def combine():
    global LOG
    rows = {}
    for line in open(os.path.join(HERE, "oscillator_states_run.log"), encoding="utf-8"):
        f = line.split()
        if line.startswith("TORUS ") and f[1].isdigit():
            rows[int(f[1]), f[2]] = dict(count=int(f[3]), bestN=float(f[4]), share=float(f[5]), mean=float(f[6]),
                                         sd=float(f[7]), lo=float(f[8]), hi=float(f[9]), r4=float(f[10]),
                                         levels=int(f[11]), parity=f[12], checks=f[13] == "True")
    cal = [l.split() for l in open(os.path.join(HERE, "oscillator_states_calibrate.log"), encoding="utf-8")
           if l.startswith("CALIBRATE ")][0]
    LOG = open(os.path.join(HERE, "oscillator_states_combined.log"), "w", encoding="utf-8")
    big = [p for p in PRIMES if p >= 211]
    w = [(rows[p, k]["count"], rows[p, k]["mean"], rows[p, k]["r4"]) for p in big for k in ("nonsplit", "split")]
    tot = sum(c for c, _, _ in w)
    mean_s = sum(c * m for c, m, _ in w) / tot
    mean_r4 = sum(c * r for c, _, r in w) / tot
    wins = [p for p in PRIMES if rows[p, "nonsplit"]["bestN"] > rows[p, "split"]["bestN"] + 1e-9]
    best_share = {p: max(rows[p, k]["share"] for k in ("nonsplit", "split")) for p in PRIMES}
    over = [p for p in PRIMES if p >= 37 and best_share[p] >= 0.90]
    beats = [p for p in WINNERS if max(rows[p, k]["bestN"] for k in ("nonsplit", "split")) > WINNERS[p] + 1e-6]
    torus_ok = all(r["checks"] and r["levels"] <= p + 2 for (p, k), r in rows.items())
    say(f"  the primes from 211 to 401: {tot} one-line states; mean S/sqrt p {mean_s:.6f} (Sato-Tate {ST:.6f}, "
        f"Gaussian {GAUSS:.6f}, uniform angle {ARCSINE:.6f}); mean mu4/mu2^2 {mean_r4:.4f} (Sato-Tate 2, Gaussian 3, "
        f"uniform angle 1.5)")
    say(f"  the non-split torus's best beats the split torus's at {len(wins)} of {len(PRIMES)} primes; it loses at "
        f"{[p for p in PRIMES if p not in wins]}")
    say(f"  the best one-line state's share of the ceiling, by prime: "
        + ", ".join(f"{p} {best_share[p]:.4f}" for p in PRIMES))
    say(f"  every chirp checks out and every state's Wigner function takes at most p + 2 values: {torus_ok}")
    for name, ok, what in (
            ("O0", cal[1] == "True" and torus_ok, "calibration: round 8's turning-wheel bests and the Legendre states "
                                                  "again; the torus checks hold at every prime"),
            ("O1", abs(mean_s - ST) <= 0.01, "the primes from 211 to 401: the mean S/sqrt p of the one-line states is "
                                             "within 0.01 of 8/(3 pi)"),
            ("O2", abs(mean_r4 - 2) <= 0.1, "the primes from 211 to 401: the mean mu4/mu2^2 is within 0.1 of 2"),
            ("O3", len(wins) > 0.75 * len(PRIMES), "the non-split torus's best beats the split torus's at more than "
                                                  "three quarters of the primes from 5 to 401"),
            ("O4", not over, "from 37 to 401 no one-line oscillator state reaches 90% of the ceiling"
                             + (f" (reached at {over})" if over else ""))):
        say(f"{name} {'HELD' if ok else 'DIED'}: {what}")
    say(f"  (check) no one-line oscillator state beats the best state known at 7 to 31: {not beats}"
        + (f" (beaten at {beats})" if beats else ""))
    LOG.close()


if __name__ == "__main__":
    part = sys.argv[1] if len(sys.argv) > 1 else "run"
    {"calibrate": calibrate, "run": run, "combine": combine}[part]()
