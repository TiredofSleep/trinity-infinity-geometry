"""Independent probe of J24 and J26 (fresh code; does not import the papers' scripts).

R(k,f) := |(1/k) sum_{j=1..k} exp(2 pi i j/f)|^2   (k >= 1, f >= 2)
"""
import math
import cmath
from math import gcd
import sympy as sp

PI = math.pi
fails = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))
    if not ok:
        fails.append(name)


def R_direct(k, f):
    s = sum(cmath.exp(2j * PI * j / f) for j in range(1, k + 1))
    return abs(s / k) ** 2


def R_closed(k, f):
    return math.sin(PI * k / f) ** 2 / (k * k * math.sin(PI / f) ** 2)


# 1. closed form (float) -------------------------------------------------------
dev = max(abs(R_direct(k, f) - R_closed(k, f)) for f in range(2, 61) for k in range(1, 3 * f + 1))
check("J24 Thm3.1 / J26 Thm3.1 closed form, f=2..60, k=1..3f (float)", dev < 1e-12, f"max dev {dev:.1e}")

# 2. exact symbolic identity (Fejer's two forms) --------------------------------
x = sp.symbols('x', real=True)
ok = True
for k in range(1, 16):
    lhs = (1 - sp.cos(x)) * (k + 2 * sum((k - m) * sp.cos(m * x) for m in range(1, k)))
    rhs = 1 - sp.cos(k * x)
    c = sp.symbols('c')
    # rewrite cos(m x) as Chebyshev T_m(cos x) and compare polynomials in c = cos x
    to_c = lambda e: sp.expand(e.rewrite(sp.cos).subs({sp.cos(m * x): sp.chebyshevt(m, c) for m in range(2, k + 1)}).subs(sp.cos(x), c))
    if sp.simplify(to_c(lhs) - to_c(rhs)) != 0:
        ok = False
check("exact: |sum_{j=1..k} e^{ijx}|^2 = k + 2 sum (k-m) cos(mx) = (1-cos kx)/(1-cos x), k=1..15", ok)

# 3. zero set, exact, in Z[z]/Phi_f(z) -------------------------------------------
z = sp.symbols('z')
ok = True
for f in range(2, 31):
    phi = sp.Poly(sp.cyclotomic_poly(f, z), z)
    for k in range(1, 2 * f + 2):
        s = sp.Poly(sum(z ** j for j in range(1, k + 1)), z)
        is_zero = s.rem(phi).is_zero
        if is_zero != (k % f == 0):
            ok = False
check("J24 Thm3.2 exact: sum_{j=1..k} zeta_f^j = 0 iff f | k  (f=2..30, k=1..2f+1)", ok)

# 4. endpoints and monotone first lap -------------------------------------------
ok = all(abs(R_closed(1, f) - 1) < 1e-14 and abs(R_closed(f - 1, f) - 1 / (f - 1) ** 2) < 1e-14 for f in range(2, 400))
check("J24 Cor3.3(i)(ii): R(1,f)=1, R(f-1,f)=1/(f-1)^2, f=2..399", ok)
ok = all(R_closed(k, f) > R_closed(k + 1, f) * (1 + 1e-12) for f in range(3, 300) for k in range(1, f - 1))
check("J24 Cor3.3(iv): strictly decreasing on 1..f-1, f=3..299", ok)

# 5. exact ratio: R(k,f) = sinc^2(k/f) / sinc^2(1/f) -----------------------------
sinc = lambda t: 1.0 if t == 0 else math.sin(PI * t) / (PI * t)
dev = max(abs(R_closed(k, f) - sinc(k / f) ** 2 / sinc(1 / f) ** 2) for f in range(2, 200) for k in range(1, f))
check("R(k,f) = sinc^2(k/f)/sinc^2(1/f) exactly (float check f<200)", dev < 1e-13, f"max dev {dev:.1e}")
print("     so |R(k,f) - sinc^2(k/f)| <= (1/sinc^2(1/f) - 1) = %.3e at f=100 (O(1/f^2))" % (1 / sinc(0.01) ** 2 - 1))

# 6. corridor average and Si(2 pi)/pi -------------------------------------------
I = float(sp.Si(2 * sp.pi).evalf(30) / sp.pi)
print(f"     Si(2pi)/pi = {I:.12f}; main-lobe fraction 2 Si(2pi)/pi = {2 * I:.6f}")
for f in [50, 100, 500, 1000, 10000, 100000]:
    avg = sum(R_closed(k, f) for k in range(1, f)) / (f - 1)
    print(f"     f={f:>6}: corridor average {avg:.9f}, deviation {avg - I:+.3e}, deviation*f {(avg - I) * f:+.4f}")
num = float(sp.Integral((sp.sin(sp.pi * x) / (sp.pi * x)) ** 2, (x, 0, 1)).evalf(25))
check("J24 Thm7.2: int_0^1 sinc^2 = Si(2pi)/pi", abs(num - I) < 1e-15, f"{num:.15f}")

# 7. J24 Remark 7.4 (concavity) ------------------------------------------------
t = sp.symbols('t', positive=True)
g = (sp.sin(sp.pi * t) / (sp.pi * t)) ** 2
g2 = sp.diff(g, t, 2)
print("     second derivative of sinc^2 at t=1/2:", sp.N(g2.subs(t, sp.Rational(1, 2)), 8))
grid = [i / 2000 for i in range(1, 2000)]
vals = [float(g2.subs(t, s)) for s in grid[::10]]
sgn_changes = [round(grid[::10][i], 3) for i in range(1, len(vals)) if vals[i - 1] * vals[i] < 0]
print("     sign changes of (sinc^2)'' on (0,1) near t =", sgn_changes)
check("J24 Rem7.4 logic: sinc^2(1/2) < int_0^1 sinc^2, so sinc^2 is NOT concave on [0,1] (Jensen)",
      sinc(0.5) ** 2 < I)

# 8. exact values ---------------------------------------------------------------
check("sin(pi/10) = (sqrt5-1)/4 (exact)", sp.simplify(sp.sin(sp.pi / 10) - (sp.sqrt(5) - 1) / 4) == 0)
v = float(25 * (sp.sqrt(5) - 1) ** 2 / (4 * sp.pi ** 2))
check("J26: sinc^2(1/10) = 25(sqrt5-1)^2/(4 pi^2) = 0.9675312093", abs(v - 0.9675312093) < 1e-10 and abs(sinc(0.1) ** 2 - v) < 1e-14, f"{v:.10f}")
check("sinc^2(1/2) = 4/pi^2 = (2/3)/zeta(2) (exact)", sp.simplify(sp.Rational(2, 3) / sp.zeta(2) - 4 / sp.pi ** 2) == 0)

# 9. J24 number-theory corollaries (exact integers) -------------------------------
def primes_of(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def mobius_sqfree(d, ps):
    return (-1) ** sum(1 for p in ps if d % p == 0)


ok = True
for b in list(range(2, 400)) + [2310, 30030]:
    ps = primes_of(b)
    divs = [1]
    for p in ps:
        divs += [d * p for d in divs]
    for kk in list(range(1, 200)) + [997, 2999]:
        direct = sum(1 for m in range(1, kk + 1) if gcd(m, b) > 1)
        ie = -sum(mobius_sqfree(d, ps) * (kk // d) for d in divs if d > 1)
        if direct != ie:
            ok = False
check("J24 Cor5.3 (Legendre/Moebius count of 1..k sharing a factor with b), exact", ok)
ok = True
for b in [2, 6, 10, 12, 30, 42, 105, 210, 2310]:
    r = 1
    for p in primes_of(b):
        r *= p
    cnt = sum(1 for m in range(1, r + 1) if gcd(m, b) > 1)
    phi = sum(1 for m in range(1, r + 1) if gcd(m, r) == 1)
    ok &= (cnt == r - phi)   # exact count over one full period rad(b)
check("J24 Cor5.4: over one period rad(b) the count is exactly rad(b)-phi(rad(b))", ok)
ok = True
for b in range(2, 3000):
    ps = primes_of(b)
    if any(b % (p * p) == 0 for p in ps):
        continue
    divs = [1]
    for p in ps:
        divs += [d * p for d in divs]
    for j in range(1, len(ps) + 1):
        bj = math.prod(ps[:j])
        ok &= sum(1 for d in divs if d > 1 and bj % d == 0) == 2 ** j - 1
check("J24 Thm6.1: #{d|b, d>1, d|b_j} = 2^j - 1 (= divisors>1 of a j-prime squarefree number), b<3000", ok)

# 10. J26 QM overlap on Z/N ---------------------------------------------------------
import numpy as np
N, f = 60, 12
phat = N // f
p_vec = np.exp(2j * np.pi * np.arange(N) * phat / N) / np.sqrt(N)
ok_overlap, ok_marg = True, True
for k in range(1, N + 1):
    w = np.zeros(N, complex)
    w[[j % N for j in range(1, k + 1)]] = 1 / np.sqrt(k)
    ov2 = abs(np.vdot(p_vec, w)) ** 2
    ok_overlap &= abs(ov2 - (k / N) * R_closed(k, f)) < 1e-12 if k % f else abs(ov2) < 1e-12
    ok_marg &= abs(sum(abs(p_vec[j % N]) ** 2 for j in range(1, k + 1)) - k / N) < 1e-12
check("J26 Prop4.1: |<p|w_k>|^2 = (k/N) R(k,f) on Z/60, f=12, all k", ok_overlap)
check("J26 note: position marginal of a momentum eigenstate on k sites = k/N", ok_marg)
N, f, k = 10000, 1000, 500
ov2 = (k / N) * R_closed(k, f)
print(f"     J26 continuum claim: N={N}, f={f}, k={k} (t=1/2): overlap^2 = {ov2:.5f};"
      f" paper's 'sinc^2(t)/N' = {sinc(0.5) ** 2 / N:.2e}; (k/N) sinc^2(t) = {(k / N) * sinc(0.5) ** 2:.5f}")
check("J26 continuum statement '-> sinc^2(t)/N' is off by the factor k", abs(ov2 - sinc(0.5) ** 2 / N) > 100 * sinc(0.5) ** 2 / N)

print("\nFAILURES:", fails if fails else "none")
