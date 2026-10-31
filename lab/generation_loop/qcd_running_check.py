#!/usr/bin/env python3
"""qcd_running_check.py -- an independent check of generation_loop/round9.py's QCD running.

Written without reading round9.py's integration code. Different on purpose:
  * coefficients in the a = alpha_s/(4 pi) normalization, as printed in the four-loop papers
    (beta: van Ritbergen, Vermaseren, Larin 1997; gamma_m: Chetyrkin 1997, Vermaseren, Larin, van Ritbergen 1997);
  * a hand-written fixed-step RK4 in t = ln mu^2 for the coupling;
  * the mass ratio as an integral over the coupling, ln m(mu1)/m(mu0) = int gamma(a)/beta(a) da / a, by Simpson;
  * decoupling at mu = m_h(m_h): alpha_s^(nl) = alpha_s^(nh) (1 + 11/72 (alpha_s/pi)^2), masses
    m^(nl) = m^(nh) (1 + 89/432 (alpha_s/pi)^2) (Chetyrkin, Kniehl, Steinhauser 1997/2000).
It prints alpha_s at m_b, 2 GeV and 1 GeV, m_b(M_Z), m_c(3 GeV), m_c/m_s at 2 GeV, and the two G9 angles,
for comparison with round9.log. ASCII output; needs numpy only.
"""
import cmath
import math

Z3, Z4, Z5 = 1.2020569031595942, math.pi ** 4 / 90, 1.0369277551433699
MZ = 91.1876


def beta4pi(nf):        # d a/d ln mu^2 = -(b0 a^2 + b1 a^3 + b2 a^4 + b3 a^5), a = alpha_s/(4 pi)
    b0 = 11 - 2 * nf / 3
    b1 = 102 - 38 * nf / 3
    b2 = 2857 / 2 - 5033 * nf / 18 + 325 * nf ** 2 / 54
    b3 = (149753 / 6 + 3564 * Z3 - (1078361 / 162 + 6508 * Z3 / 27) * nf
          + (50065 / 162 + 6472 * Z3 / 81) * nf ** 2 + 1093 * nf ** 3 / 729)
    return b0, b1, b2, b3


def gamma4pi(nf):       # d ln m/d ln mu^2 = -(g0 a + g1 a^2 + g2 a^3 + g3 a^4)
    g0 = 4.0
    g1 = 202 / 3 - 20 * nf / 9
    g2 = 1249 + (-2216 / 27 - 160 * Z3 / 3) * nf - 140 * nf ** 2 / 81
    g3 = (4603055 / 162 + 135680 * Z3 / 27 - 8800 * Z5
          + (-91723 / 27 - 34192 * Z3 / 9 + 880 * Z4 + 18400 * Z5 / 9) * nf
          + (5242 / 243 + 800 * Z3 / 9 - 160 * Z4 / 3) * nf ** 2
          + (-332 / 243 + 64 * Z3 / 27) * nf ** 3)
    return g0, g1, g2, g3


def run_a(a, mu0, mu1, nf, steps=4000):
    """RK4 for a = alpha_s/(4 pi) in t = ln mu^2."""
    b = beta4pi(nf)
    f = lambda x: -(b[0] * x ** 2 + b[1] * x ** 3 + b[2] * x ** 4 + b[3] * x ** 5)
    t, t1 = 2 * math.log(mu0), 2 * math.log(mu1)
    h = (t1 - t) / steps
    for _ in range(steps):
        k1 = f(a); k2 = f(a + h * k1 / 2); k3 = f(a + h * k2 / 2); k4 = f(a + h * k3)
        a += h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return a


def log_mass_ratio(a0, a1, nf, n=2000):
    """ln m(mu1)/m(mu0) = int_{a0}^{a1} gamma(a) / (a beta(a)) ... with the signs of the two definitions."""
    b, g = beta4pi(nf), gamma4pi(nf)
    F = lambda x: (g[0] * x + g[1] * x ** 2 + g[2] * x ** 3 + g[3] * x ** 4) / \
                  (b[0] * x ** 2 + b[1] * x ** 3 + b[2] * x ** 4 + b[3] * x ** 5)
    h = (a1 - a0) / n                       # Simpson on [a0, a1]
    s = F(a0) + F(a1) + sum((4 if i % 2 else 2) * F(a0 + i * h) for i in range(1, n))
    return s * h / 3


def decouple(a4pi):
    ap = 4 * a4pi                           # alpha_s/pi
    return a4pi * (1 + 11 / 72 * ap ** 2), math.log(1 + 89 / 432 * ap ** 2)


def chain(als_mz, mc, mb, mt):
    """Coupling (a = alpha_s/4pi) and cumulative ln(mass factor) at each scale, walking m_t -> 1 GeV."""
    a = run_a(als_mz / (4 * math.pi), MZ, mt, 5)
    pts = {"mt": (a, 0.0)}
    L = 0.0
    for lab, mu0, mu1 in (("MZ", mt, MZ), ("mb", MZ, mb)):
        a1 = run_a(a, mu0, mu1, 5); L += log_mass_ratio(a, a1, 5); a = a1; pts[lab] = (a, L)
    a, jump = decouple(a); L += jump
    prev = mb
    for lab, mu in (("3", 3.0), ("2", 2.0), ("mc", mc)):
        a1 = run_a(a, prev, mu, 4); L += log_mass_ratio(a, a1, 4); a = a1; pts[lab] = (a, L); prev = mu
    a, jump = decouple(a); L += jump
    a1 = run_a(a, mc, 1.0, 3); L += log_mass_ratio(a, a1, 3); pts["1"] = (a1, L)
    return pts


def angle(light, middle, heavy):
    r = [math.sqrt(heavy), math.sqrt(light), math.sqrt(middle)]       # labels n = 0, 1, 2 as in the PREREG
    c1 = sum(r[n] * cmath.exp(-2j * math.pi * n / 3) for n in range(3)) / 3
    return cmath.phase(c1)


m_in = dict(u=2.14e-3, d=4.70e-3, s=93.46e-3, c=1.278, b=4.200, t=162.5)
ref = dict(u="2", d="2", s="2", c="mc", b="mb", t="mt")
pts = chain(0.1180, m_in["c"], m_in["b"], m_in["t"])
at = lambda sc: {q: m_in[q] * math.exp(pts[sc][1] - pts[ref[q]][1]) for q in m_in}
pi4 = 4 * math.pi
print("independent 4-loop running (alpha_s(M_Z) = 0.1180, m_c(m_c) = 1.278, m_b(m_b) = 4.200, m_t(m_t) = 162.5 GeV)")
print("  alpha_s(m_b) = %.4f, alpha_s(2 GeV) = %.4f, alpha_s(1 GeV) = %.4f"
      % (pts["mb"][0] * pi4, pts["2"][0] * pi4, pts["1"][0] * pi4))
print("  m_b(M_Z) = %.3f GeV; m_c(3 GeV) = %.3f GeV; m_c/m_s at 2 GeV = %.2f"
      % (at("MZ")["b"], at("3")["c"], at("2")["c"] / at("2")["s"]))
m1 = at("1")
print("  masses at 1 GeV (MeV): " + ", ".join(f"{q} {v * 1e3:.4g}" for q, v in m1.items()))
for sc in ("1", "2", "3", "MZ"):
    m = at(sc)
    print(f"  mu = {sc:>2s}: delta_up = {angle(m['u'], m['c'], m['t']):.5f}, delta_down = {angle(m['d'], m['s'], m['b']):.5f}")
pts2 = chain(0.1180, 1.275, 4.200, 162.5)
print("  m_c(3 GeV) for m_c(m_c) = 1.275 GeV: %.3f (FLAG's m_c(3 GeV) = 0.988 corresponds to m_c(m_c) ~ 1.275-1.28)"
      % (1.275 * math.exp(pts2["3"][1] - pts2["mc"][1])))
