"""constants.py -- the rigorous constants and lemmas for the p = 7 theorem (t7_rigorous.c).

    "make it rigor"  -- the author, 18 November 2026

Writes t7_constants.h: every real constant the C program uses, as the bit patterns of two doubles that enclose it, and
proves the lemmas the branch and bound relies on at the two maximizers phi_c = (2 pi/7) c (x^3 + 4x^2 + 2x), c = 3, 4.

Everything that the proof uses here is EXACT RATIONAL ARITHMETIC (Python integers and fractions); no floating-point
function is trusted, and every double is chosen by exact comparison with a rational enclosure.
  - pi is enclosed by Machin's formula pi = 16 atan(1/5) - 4 atan(1/239): each arctangent lies between two consecutive
    partial sums of its alternating series, whose terms decrease.
  - At the maximizers every angle is a multiple of 2 pi/7, so only c_k = cos(2 pi k/7) and s_k = sin(2 pi k/7) occur.
    c_1 > c_2 > c_3 are the three roots of 8x^3 + 4x^2 - 4x - 1 (proof below), isolated by exact bisection in disjoint
    brackets; c_0 = 1 and c_(7-k) = c_k.  The sines are s_k = sqrt(1 - c_k^2) > 0 for k = 1, 2, 3 (integer square
    roots), s_0 = 0 and s_(7-k) = -s_k.
  - The Taylor coefficients 1/n! and the remainders RMAX^n/n! are exact fractions, with RMAX the exact value of the
    double 0.8 that the C program compares against.
mpmath is used only for information (the Hessian's eigenvalues, and a cross-check of the cosines), not in the proof.

The lemmas, at both maximizers:
  K1. S_T = sum |E| / 49 is enclosed; ST_LO is a double below the enclosure, and the C program discards a box only
      when its rigorous upper bound is below ST_LO.  Every E has a certified sign.
  K2. The gradient of S is exactly 0 (proof below); the rational interval gradient contains 0.
  K3. -H - (24 rho0 + 1/100) I is positive definite, H the Hessian of S and rho0 the double nearest 0.004: an LDL^T
      factorization in exact rational interval arithmetic has every pivot positive.
  K4. min |E| exceeds 12 rho0.

Why the cosines are the roots.  Let zeta = exp(2 pi i k/7) with k = 1, 2 or 3, and y = zeta + 1/zeta = 2 c_k.  Dividing
1 + zeta + ... + zeta^6 = 0 by zeta^3 gives (zeta^3 + zeta^-3) + (zeta^2 + zeta^-2) + (zeta + zeta^-1) + 1 = 0, that is
(y^3 - 3y) + (y^2 - 2) + y + 1 = y^3 + y^2 - 2y - 1 = 0, and with y = 2x this is 8x^3 + 4x^2 - 4x - 1 = 0.  cos is
strictly decreasing on [0, pi] and 0 < 2 pi/7 < 4 pi/7 < 6 pi/7 < pi, so c_1 > c_2 > c_3 are the cubic's three roots,
in that order.

Proof of K2.  With f = c(x^3 + 4x^2 + 2x), f(q + u) - f(q - u) = c(2u^3 + u m_q) with m_q = 6q^2 + 16q + 4, so
E(q, s) = G(k) := 1 + 2 sum_u cos(2 pi (2c u^3 + u k)/7) with k = c m_q - 2s, and as s runs over F_7 so does k.  Hence
for each u the sum T_u = sum_s sign(E(q, s)) sin(angle(q, s, u)) = sum_k sign(G(k)) sin(2 pi (2c u^3 + u k)/7) does not
depend on q, and dS/dphi_x = (1/49) sum_u T_u (sum_q [-2 if q + u = x] + [2 if q - u = x]) = (1/49) sum_u T_u (-2 + 2) = 0.

The cube lemma (rule (c) of the C program).  Let C be the cube |phi_i - phi_c,i| <= rho0, i = 1..6 (phi_0 = 0).
Every angle theta = phi_a - phi_b - 4 pi s u/7 moves by |delta| <= 2 rho0 on C, so every E moves by at most
2 * 3 * 2 rho0 = 12 rho0, and by K4 no E changes sign: S = (1/49) sum sigma E is smooth on C, with Hessian
H(phi) = (1/49) sum_{q,s} sigma_{qs} sum_u (-2 cos theta_u) v_u v_u^T, v_u = e_a - e_b (|v_u|^2 <= 2).  Then
||H(phi) - H(phi_c)|| <= (1/49) * 147 * 2 * (2 rho0) * 2 = 24 rho0, and by K3 and Weyl's inequality every eigenvalue
of H(phi) is below -1/100.  So S is strictly concave on the convex set C, its gradient vanishes at the center (K2),
and S < S(phi_c) = S_T at every other point of C.

Usage: python constants.py           (seconds)   -> t7_constants.h, constants.log
       python constants.py --check   proves the lemmas and checks that t7_constants.h is exactly what it would write;
                                     writes nothing
"""
import math
import os
import struct
import sys
from fractions import Fraction as Q

HERE = os.path.dirname(os.path.abspath(__file__))
P = 7
NT = 8                      # Taylor terms: cos to R^16, sin to R^17
RMAX = 0.8                  # the C program reduces to |R| <= RMAX (this double), then uses the Taylor polynomial
RHO0 = 0.004                # the double nearest 0.004; the lemmas use this exact value
CHECK = "--check" in sys.argv
LOG = None if CHECK else open(os.path.join(HERE, "constants.log"), "w", encoding="utf-8")


def say(s=""):
    print(s, flush=True)
    if LOG:
        LOG.write(s + "\n")
        LOG.flush()


class RI:
    """a closed interval with exact rational ends"""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = Q(lo)
        hi = lo if hi is None else Q(hi)
        assert lo <= hi
        self.lo, self.hi = lo, hi

    def __add__(a, b):
        b = ri(b)
        return RI(a.lo + b.lo, a.hi + b.hi)

    __radd__ = __add__

    def __neg__(a):
        return RI(-a.hi, -a.lo)

    def __sub__(a, b):
        b = ri(b)
        return RI(a.lo - b.hi, a.hi - b.lo)

    def __rsub__(a, b):
        return ri(b) - a

    def __mul__(a, b):
        b = ri(b)
        p = (a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi)
        return RI(min(p), max(p))

    __rmul__ = __mul__

    def __truediv__(a, b):
        b = ri(b)
        assert b.lo > 0 or b.hi < 0
        return a * RI(1 / b.hi, 1 / b.lo)

    def width(self):
        return self.hi - self.lo


def ri(x):
    return x if isinstance(x, RI) else RI(x)


def atan_inv(x, terms):
    """atan(1/x) for an integer x > 1: between two consecutive partial sums of its alternating series"""
    s, prev = Q(0), Q(0)
    for n in range(terms + 1):
        prev = s
        s = s + Q((-1) ** n, (2 * n + 1) * x ** (2 * n + 1))
    return RI(min(prev, s), max(prev, s))


PI = 16 * atan_inv(5, 70) - 4 * atan_inv(239, 25)


def cubic(x):
    return 8 * x ** 3 + 4 * x ** 2 - 4 * x - 1


def root_in(a, b, steps=220):
    """the root of the cubic in [a, b], where it changes sign, by exact bisection"""
    a, b = Q(a), Q(b)
    fa, fb = cubic(a), cubic(b)
    assert fa * fb < 0
    for _ in range(steps):
        m = (a + b) / 2
        fm = cubic(m)
        if fm == 0:
            return RI(m)
        if (fm < 0) == (fa < 0):
            a, fa = m, fm
        else:
            b = m
    return RI(a, b)


def sqrt_ri(t, bits=240):
    """an enclosure of sqrt over the interval t >= 0, by integer square roots"""
    assert t.lo >= 0
    M = 1 << bits
    lo = math.isqrt(math.floor(t.lo * M * M))
    hi = math.isqrt(math.ceil(t.hi * M * M)) + 1
    return RI(Q(lo, M), Q(hi, M))


# the three brackets are disjoint and the cubic changes sign on each, so each holds exactly one of its three roots
C1, C2, C3 = root_in(Q(3, 5), Q(7, 10)), root_in(Q(-3, 10), Q(-1, 5)), root_in(Q(-1), Q(-9, 10))
assert C3.hi < C2.lo and C2.hi < C1.lo
COS = [RI(1), C1, C2, C3, C3, C2, C1]


def one_minus_sq(c):
    sq = (c.lo * c.lo, c.hi * c.hi)
    return RI(1 - max(sq), 1 - min(sq))


S1, S2, S3 = (sqrt_ri(one_minus_sq(c)) for c in (C1, C2, C3))
SIN = [RI(0), S1, S2, S3, -S3, -S2, -S1]


def lo_double(q):
    """the largest double <= the rational q, decided exactly"""
    d = float(q)
    while Q(d) > q:
        d = math.nextafter(d, -math.inf)
    while Q(math.nextafter(d, math.inf)) <= q:
        d = math.nextafter(d, math.inf)
    return d


def hi_double(q):
    """the smallest double >= the rational q, decided exactly"""
    d = float(q)
    while Q(d) < q:
        d = math.nextafter(d, math.inf)
    while Q(math.nextafter(d, -math.inf)) >= q:
        d = math.nextafter(d, -math.inf)
    return d


def enclose(x):
    x = ri(x)
    return lo_double(x.lo), hi_double(x.hi)


def bits(d):
    return struct.unpack("<Q", struct.pack("<d", d))[0]


lines = ["/* t7_constants.h -- generated by constants.py; every constant is a pair of doubles enclosing a real number */",
         "#include <stdint.h>"]


def emit(name, lohi):
    lo, hi = lohi
    assert lo <= hi
    lines.append(f"static const uint64_t {name}_LO_B = 0x{bits(lo):016x}ULL; /* {lo!r} */")
    lines.append(f"static const uint64_t {name}_HI_B = 0x{bits(hi):016x}ULL; /* {hi!r} */")


def emit_arr(name, pairs):
    lines.append(f"static const uint64_t {name}_LO_B[{len(pairs)}] = {{" + ", ".join(f"0x{bits(a):016x}ULL" for a, b in pairs) + "};")
    lines.append(f"static const uint64_t {name}_HI_B[{len(pairs)}] = {{" + ", ".join(f"0x{bits(b):016x}ULL" for a, b in pairs) + "};")


emit("PI", enclose(PI))
emit("TWO_PI", enclose(2 * PI))
emit("PIO2", enclose(PI / 2))
emit("PI7", enclose(PI / 7))
emit_arr("SHIFT", [enclose(2 * PI * k / 7) for k in range(P)])
emit_arr("COSC", [enclose(Q((-1) ** j, math.factorial(2 * j))) for j in range(NT + 1)])
emit_arr("SINC", [enclose(Q((-1) ** j, math.factorial(2 * j + 1))) for j in range(NT + 1)])
# Lagrange remainders for |R| <= RMAX (the exact value of the double): cos after R^(2NT), sin after R^(2NT+1)
emit("REMC", enclose(Q(RMAX) ** (2 * NT + 2) / math.factorial(2 * NT + 2)))
emit("REMS", enclose(Q(RMAX) ** (2 * NT + 3) / math.factorial(2 * NT + 3)))
lines.append(f"#define NT {NT}")
lines.append(f"static const double RMAX = {RMAX!r};")
lines.append(f"static const uint64_t RHO0_B = 0x{bits(RHO0):016x}ULL; /* {RHO0!r} */")
rho0 = Q(RHO0)

AI = [[(q + u) % P for u in (1, 2, 3)] for q in range(P)]
BI = [[(q - u) % P for u in (1, 2, 3)] for q in range(P)]


def ldl_positive(A):
    """True if the LDL^T factorization of the symmetric interval matrix A, in exact rational interval arithmetic,
    has every pivot > 0: then every real symmetric matrix inside A, the true one included, is positive definite"""
    n = len(A)
    L = [[None] * n for _ in range(n)]
    D = [None] * n
    for i in range(n):
        for j in range(i + 1):
            s = A[i][j]
            for k in range(j):
                s = s - L[i][k] * L[j][k] * D[k]
            if i == j:
                D[i] = s
                if not s.lo > 0:
                    return False, D
            else:
                L[i][j] = s / D[j]
    return True, D


say("constants.py -- the rigorous constants and lemmas for the p = 7 theorem (exact rational arithmetic)")
say(f"  pi enclosed by Machin's formula, width {float(PI.width()):.1e}; cos(2 pi k/7), k = 1, 2, 3, as roots of "
    f"8x^3 + 4x^2 - 4x - 1, widths {float(max(c.width() for c in (C1, C2, C3))):.1e}; sines widths "
    f"{float(max(s.width() for s in (S1, S2, S3))):.1e}")
phis, ok, st_los = [], True, []
for c in (3, 4):
    f = [(c * (v ** 3 + 4 * v * v + 2 * v)) % P for v in range(P)]
    phis.append([enclose(2 * PI * k / 7) for k in f[1:]])
    E, sig, kk = {}, {}, {}
    for q in range(P):
        for s in range(P):
            tot = RI(1)
            for ui, u in enumerate((1, 2, 3)):
                k = (f[AI[q][ui]] - f[BI[q][ui]] - 2 * s * u) % P     # the angle is 2 pi k/7
                kk[q, s, ui] = k
                tot = tot + 2 * COS[k]
            E[q, s] = tot
            sig[q, s] = 1 if tot.lo > 0 else (-1 if tot.hi < 0 else 0)
    signs_ok = all(v != 0 for v in sig.values())
    ok &= signs_ok
    absE = {key: (E[key] if sig[key] > 0 else -E[key]) for key in E}
    S = RI(0)
    for v in absE.values():
        S = S + v
    S = S / 49
    st_los.append(lo_double(S.lo))
    minE = min(v.lo for v in absE.values())
    k4 = minE > 12 * rho0
    grad = [RI(0)] * P
    H = [[RI(0)] * P for _ in range(P)]
    for q in range(P):
        for s in range(P):
            for ui in range(3):
                a, b, k = AI[q][ui], BI[q][ui], kk[q, s, ui]
                t = sig[q, s] * SIN[k]
                grad[a] = grad[a] - 2 * t
                grad[b] = grad[b] + 2 * t
                cv = -2 * sig[q, s] * COS[k]
                H[a][a] = H[a][a] + cv
                H[b][b] = H[b][b] + cv
                H[a][b] = H[a][b] - cv
                H[b][a] = H[b][a] - cv
    k2 = all(g.lo <= 0 <= g.hi and g.width() < Q(1, 10 ** 50) for g in grad[1:])
    shift = 24 * rho0 + Q(1, 100)
    A = [[(-H[i][j] / 49) - (shift if i == j else 0) for j in range(1, P)] for i in range(1, P)]
    k3, D = ldl_positive(A)
    say(f"  c = {c}: f = {f}; every E has a certified sign: {signs_ok}; S in [{float(S.lo)!r}, {float(S.hi)!r}] "
        f"(width {float(S.width()):.1e})")
    say(f"         K2 interval gradient contains 0, width < 1e-50: {k2}; K3 pivots of -H - (24 rho0 + 1/100) I: "
        f"{[round(float(d.lo), 6) for d in D]} (all > 0: {k3})")
    say(f"         K4 min |E| >= {float(minE):.12f} > 12 rho0 = {12 * RHO0}: {k4}")
    ok &= k2 and k3 and k4
    try:                                            # for information only, not part of the proof
        import mpmath as mpm
        mpm.mp.dps = 30
        mq = lambda x: mpm.mpf(x.numerator) / x.denominator
        Hmid = mpm.matrix([[mq((H[i][j].lo + H[i][j].hi) / 2) / 49 for j in range(1, P)] for i in range(1, P)])
        ev = mpm.eigsy(Hmid)[0]
        dc = max(abs(mq((COS[k].lo + COS[k].hi) / 2) - mpm.cos(2 * mpm.pi * k / 7)) for k in range(P))
        say(f"         (information) Hessian eigenvalues {[mpm.nstr(ev[i], 8) for i in range(6)]}; the cosines agree "
            f"with mpmath's to {mpm.nstr(dc, 2)}")
    except ImportError:
        pass
st_lo = min(st_los)
lines.append(f"static const uint64_t ST_LO_B = 0x{bits(st_lo):016x}ULL; /* {st_lo!r}, a double below S_T */")
emit_arr("PHI3", phis[0])
emit_arr("PHI4", phis[1])
text = "\n".join(lines) + "\n"
HEADER = os.path.join(HERE, "t7_constants.h")
if CHECK:
    same = os.path.exists(HEADER) and open(HEADER, encoding="utf-8").read() == text
    ok &= same
    say(f"[{'PASS' if same else 'FAIL'}] t7_constants.h is exactly the header these lemmas generate")
else:
    open(HEADER, "w", encoding="utf-8").write(text)
say(f"[{'PASS' if ok else 'FAIL'}] K1-K4 in exact rational arithmetic: S_T enclosed at both maximizers, ST_LO = "
    f"{st_lo!r}; the gradient is 0 (proved; the interval gradient contains 0); -H - (24 rho0 + 1/100) I is positive "
    f"definite (interval LDL^T); min |E| > 12 rho0")
if not CHECK:
    say("wrote t7_constants.h")
    LOG.close()
sys.exit(0 if ok else 1)
