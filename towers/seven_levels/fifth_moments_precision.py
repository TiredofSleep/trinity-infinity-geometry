"""fifth_moments_precision.py -- read after round 17 (PREREG.md), not a score: which operator values carry the rounding
error at 409..509?  The same computation as exact_moments.counts, reporting each I_n and J_n's distance to its integer."""
import ctypes
import os
import sys

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

TRIN = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TRIN)


def low():
    try:
        ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
    except Exception:
        pass


def dist(p):
    low()
    import oscillator_states as osc
    NMAX = 6
    V = osc.nonsplit_states(p)[0]
    x = np.arange(p)
    eps = np.rint(np.real(np.sum(V.conj() * V[:, (-x) % p], axis=1)))
    acc = np.zeros((len(V), NMAX + 1))
    two_k = (2 * x) % p
    for q in range(p):
        F = V.conj()[:, (q + x) % p] * V[:, (q - x) % p]
        Wq = np.real(np.fft.ifft(F, axis=1)[:, two_k])
        if q == 0:
            Wq = Wq[:, 1:]
        Wq = Wq * p ** 1.5
        Wn = np.ones_like(Wq)
        for n in range(1, NMAX + 1):
            Wn = Wn * Wq
            acc[:, n] += Wn.sum(axis=1)
    m = p + 1
    out = {}
    for n in range(2, NMAX + 1):
        scale = p ** n * m ** (n - 1) / p ** (1.5 * n)
        for name, w in (("I", np.ones(len(V))), ("J", eps)):
            raw = float((w * acc[:, n]).sum()) * scale
            out[f"{name}{n}"] = abs(raw - round(raw))
    return p, out


if __name__ == "__main__":
    from multiprocessing import Pool
    import sympy
    ps = [q for q in range(409, 510) if sympy.isprime(q)]
    low()
    with Pool(4) as pool:
        res = pool.map(dist, ps)
    worst = {}
    for p, d in sorted(res):
        print(p, " ".join(f"{k}:{v:.3f}" for k, v in d.items()), flush=True)
        for k, v in d.items():
            worst[k] = max(worst.get(k, 0), v)
    print("WORST per quantity over 409..509:", " ".join(f"{k}:{v:.3f}" for k, v in worst.items()))
