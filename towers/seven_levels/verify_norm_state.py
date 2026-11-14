"""verify_norm_state.py -- checks NORM_STATE.md: on three wheels of an odd prime p, the norm-type state's Wigner
values are Kloosterman sums.

Setting: F = F_q with q = p^3, N(x) = x^(1 + p + p^2) its norm to F_p, Tr(x) = x + x^p + x^(p^2) its trace,
w = exp(2 pi i / p), and psi_c = sum_x w^(c N(x)) |x> / sqrt q for c = 1, ..., p - 1, with x written in a polynomial
basis.  The page proves that psi_c's Wigner function takes the value K(m)/p^5 at (p^2 + p + 1) q points for each m in
F_p*, where K(m) = sum over a in F_p* of w^(a + m/a), and -(p + 1)/p^5 at the other q points.  This script checks
  A. the whole statement, from the state itself, at p = 3, 5, 7, 11 and 13 and every c: the Wigner function computed
     as round 10 computes it (one Fourier transform per point), its values and their counts, the negativity formula,
     and the flatness (Weyl expectations 0 on the Z-type operators, 1/sqrt q on every other);
  B. each step of the proof at every odd prime p up to 101, from the joint counts of (Tr(s), N(s)) over the field:
     the norm's fibres (p^2 + p + 1 elements over each nonzero value), the sum at w = 0, -p(p + 1), Davenport and
     Hasse's lifting G(chi o N) = g(chi)^3 for every character chi, and the key identity
         T(mu) = sum over s in F of w^(Tr(s) - mu N(s)) = p K(1/mu)   for every mu in F_p*.

numpy only.  One process, one thread, below-normal priority.  ASCII output; writes verify_norm_state.log and exits
with 1 if a check fails.
Run:  python verify_norm_state.py      (about a minute)
"""
import ctypes
import os
import sys
import time

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "1")
import numpy as np

try:
    ctypes.windll.kernel32.SetPriorityClass(ctypes.c_void_p(-1), 0x00004000)
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = None                                                               # opened by main(), so imports leave the log alone
OK = True
T0 = time.time()


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


def check(label, ok):
    global OK
    OK &= bool(ok)
    say(("PASS  " if ok else "FAIL  ") + label)


def primes(lo, hi):
    return [x for x in range(lo, hi + 1) if x > 1 and all(x % d for d in range(2, int(x ** 0.5) + 1))]


# ------------------------------------------------------------------ the field F_p[t]/(t^3 + a t + b)
def cubic(p):
    """the first irreducible t^3 + a t + b over F_p: a cubic is irreducible exactly when it has no root"""
    x = np.arange(p)
    for a in range(p):
        for b in range(1, p):
            if np.all((x ** 3 + a * x + b) % p):
                return a, b
    raise ValueError(p)


def mul(X, Y, p, a, b):
    """products of field elements, arrays (..., 3) of coefficients of 1, t, t^2"""
    x0, x1, x2 = X[..., 0], X[..., 1], X[..., 2]
    y0, y1, y2 = Y[..., 0], Y[..., 1], Y[..., 2]
    c0, c1, c2 = x0 * y0, x0 * y1 + x1 * y0, x0 * y2 + x1 * y1 + x2 * y0
    c3, c4 = x1 * y2 + x2 * y1, x2 * y2
    c2 = c2 - a * c4                                                       # t^4 = -a t^2 - b t
    c1 = c1 - b * c4 - a * c3                                              # t^3 = -a t - b
    c0 = c0 - b * c3
    return np.stack([c0 % p, c1 % p, c2 % p], axis=-1)


def power(X, e, p, a, b):
    R = np.zeros_like(X)
    R[..., 0] = 1
    B = X.copy()
    while e:
        if e & 1:
            R = mul(R, B, p, a, b)
        B, e = mul(B, B, p, a, b), e >> 1
    return R


def elements(p):
    """every element, in the order of the basis states: index = c0 p^2 + c1 p + c2 (the first wheel is c0)"""
    i = np.arange(p ** 3)
    return np.stack([i // (p * p), (i // p) % p, i % p], axis=-1).astype(np.int64)


def trace_norm(p):
    a, b = cubic(p)
    X = elements(p)
    Xp = power(X, p, p, a, b)
    Xpp = power(Xp, p, p, a, b)
    N = mul(mul(X, Xp, p, a, b), Xpp, p, a, b)
    T = (X + Xp + Xpp) % p
    assert not N[:, 1:].any() and not T[:, 1:].any(), "the norm and the trace lie in F_p"
    return T[:, 0], N[:, 0], (a, b)


def kloosterman(p):
    """K(m) for m = 0, ..., p - 1 (K(0) = -1 is not used)"""
    a = np.arange(1, p)
    inv = np.array([pow(int(x), -1, p) for x in a])
    return np.array([np.exp(2j * np.pi * ((a + m * inv) % p) / p).sum() for m in range(p)])


# ------------------------------------------------------------------ A. the whole statement, from the state
def wigner_rows(psi, p, rows, digits, wt):
    """W(u, k) for the u in `rows`: (1/q) sum_s conj psi(u + s) psi(u - s) w^(2 k.s), as larger_arrays.py computes it"""
    U = digits[rows]
    plus = ((U[:, None, :] + digits[None, :, :]) % p) @ wt
    minus = ((U[:, None, :] - digits[None, :, :]) % p) @ wt
    f = psi.conj()[plus] * psi[minus]
    F = np.fft.ifftn(f.reshape((len(rows), p, p, p)), axes=(1, 2, 3)).reshape(len(rows), -1)
    two = ((2 * digits) % p) @ wt
    return F[:, two]


def part_a(p):
    q = p ** 3
    T, N, (a, b) = trace_norm(p)
    digits = elements(p)
    wt = np.array([p * p, p, 1])
    K = kloosterman(p)
    want = np.sort(np.concatenate([np.repeat(K[1:].real / p ** 5, (p * p + p + 1) * q), np.full(q, -(p + 1) / p ** 5)]))
    closed = (((p + 1) + (p * p + p + 1) * np.abs(K[1:].real).sum()) / p ** 2 - 1) / 2
    values_ok, imag, neg_ok, flat_ok = True, 0.0, True, True
    for c in range(1, p):
        psi = np.exp(2j * np.pi * c * N / p) / np.sqrt(q)
        W = np.concatenate([wigner_rows(psi, p, np.arange(i, min(i + 256, q)), digits, wt)
                            for i in range(0, q, 256)]).ravel()
        imag = max(imag, np.abs(W.imag).max())
        values_ok &= bool(np.allclose(np.sort(W.real), want, atol=1e-13))
        neg_ok &= abs((np.abs(W.real).sum() - 1) / 2 - closed) < 1e-9
        # the Weyl expectations |<psi| Z^b X^a |psi>|: row a, all b at once
        for i in range(0, q, 256):
            A = np.arange(i, min(i + 256, q))
            shift = ((digits[A][:, None, :] + digits[None, :, :]) % p) @ wt
            V = psi.conj()[shift] * psi[None, :]
            C = np.abs(np.fft.fftn(V.reshape((len(A), p, p, p)), axes=(1, 2, 3))).reshape(len(A), -1)
            for j, row in zip(A, C):
                flat_ok &= bool(np.allclose(row, [1.0] + [0.0] * (q - 1), atol=1e-9) if j == 0
                                else np.allclose(row, q ** -0.5, atol=1e-9))
    check(f"p = {p} (t^3 + {a} t + {b}): for every c, the Wigner function computed from the state takes the value "
          f"K(m)/p^5 at {(p * p + p + 1) * q} points for each m in F_p* and -(p + 1)/p^5 at {q} points (imaginary "
          f"parts below {imag:.0e}); its negativity is the formula's, {closed:.9f}; its Weyl expectations are 0 on the "
          f"Z-type operators and 1/sqrt q on every other", values_ok and neg_ok and flat_ok and imag < 1e-12)


# ------------------------------------------------------------------ B. each step of the proof, from the joint counts
def part_b(p):
    q = p ** 3
    T, N, _ = trace_norm(p)
    H = np.bincount(T * p + N, minlength=p * p).reshape(p, p)            # H[t, n] = #{s : Tr(s) = t, N(s) = n}
    w = np.exp(2j * np.pi * np.arange(p) / p)
    t_, n_ = np.meshgrid(np.arange(p), np.arange(p), indexing="ij")
    fibres = bool(H[:, 0].sum() == 1 and np.all(H[:, 1:].sum(axis=0) == p * p + p + 1))
    S0 = [np.sum(H * w[(-2 * c * n_) % p]) for c in range(1, p)]
    s0_ok = np.allclose(S0, -p * (p + 1), rtol=0, atol=1e-6)
    K = kloosterman(p)
    Tmu = np.array([np.sum(H * w[(t_ - mu * n_) % p]) for mu in range(1, p)])
    key = np.allclose(Tmu, [p * K[pow(mu, -1, p)] for mu in range(1, p)], rtol=0, atol=1e-6)
    # Davenport and Hasse: the Gauss sum over F of chi o N is the cube of chi's Gauss sum over F_p
    g = next(x for x in range(2, p) if len({pow(x, e, p) for e in range(1, p)}) == p - 1)   # a primitive root
    log = np.zeros(p, dtype=np.int64)
    for e in range(p - 1):
        log[pow(g, e, p)] = e
    dh = True
    for j in range(p - 1):
        chi = np.zeros(p, complex)
        chi[1:] = np.exp(2j * np.pi * j * log[1:] / (p - 1))
        gs = np.sum(chi * w)
        G = np.sum(H * chi[n_] * w[t_])
        dh &= bool(abs(G - gs ** 3) < 1e-6)
    return fibres, s0_ok, dh, key


def main():
    global LOG
    LOG = open(os.path.join(HERE, "verify_norm_state.log"), "w", encoding="utf-8")
    say("NORM_STATE.md: the norm-type state on three wheels of p; its Wigner values are Kloosterman sums")
    say()
    say("A. the whole statement, from the state itself")
    for p in (3, 5, 7, 11, 13):
        part_a(p)
    say(f"[{time.time() - T0:.0f} s]")
    say()
    say("B. each step of the proof, at every odd prime up to 101")
    ps = primes(3, 101)
    res = {p: part_b(p) for p in ps}
    for name, k in (("the norm's fibres: one element over 0 and p^2 + p + 1 over each nonzero value", 0),
                    ("the sum at w = 0: sum over s of w^(-2c N(s)) = -p(p + 1), for every c", 1),
                    ("Davenport and Hasse: G(chi o N) = g(chi)^3, for every character chi of F_p*", 2),
                    ("the key identity: T(mu) = sum over s of w^(Tr(s) - mu N(s)) = p K(1/mu), for every mu", 3)):
        bad = [p for p in ps if not res[p][k]]
        check(f"{name}: at all {len(ps)} odd primes from 3 to 101" + (f" except {bad}" if bad else ""), not bad)
    say(f"[{time.time() - T0:.0f} s]")
    say()
    say("ALL PASS" if OK else "A CHECK FAILED")
    LOG.close()
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()
