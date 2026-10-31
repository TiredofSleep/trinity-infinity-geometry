#!/usr/bin/env python3
"""
round9.py -- generation_loop/PREREG.md Round G9: the quark families read "where color locks".
Reading A: all six MS-bar masses run (4-loop QCD) to mu = 1 GeV.  Reading B: constituent (hadron-locked) masses.
Run from generation_loop/:  python3 round9.py     Prints ASCII only. Needs numpy and scipy.
"""
import cmath, math
import numpy as np
from scipy.integrate import solve_ivp

Z3, Z4, Z5 = 1.2020569031595942, math.pi ** 4 / 90, 1.0369277551433699
MZ = 91.1876
TARGET = 2 / 9


def beta(nf):
    return (11 / 4 - nf / 6,
            51 / 8 - 19 * nf / 24,
            2857 / 128 - 5033 * nf / 1152 + 325 * nf ** 2 / 3456,
            ((149753 / 6 + 3564 * Z3) - (1078361 / 162 + 6508 / 27 * Z3) * nf
             + (50065 / 162 + 6472 / 81 * Z3) * nf ** 2 + 1093 / 729 * nf ** 3) / 256)


def gamma(nf):
    return (1.0,
            (202 / 3 - 20 * nf / 9) / 16,
            (1249 + (-2216 / 27 - 160 / 3 * Z3) * nf - 140 / 81 * nf ** 2) / 64,
            (4603055 / 162 + 135680 / 27 * Z3 - 8800 * Z5
             + (-91723 / 27 - 34192 / 9 * Z3 + 880 * Z4 + 18400 / 9 * Z5) * nf
             + (5242 / 243 + 800 / 9 * Z3 - 160 / 3 * Z4) * nf ** 2
             + (-332 / 243 + 64 / 27 * Z3) * nf ** 3) / 256)


def seg(a, L, mu0, mu1, nf):
    """Run a = alpha_s/pi and L = ln(universal mass factor) from mu0 to mu1 with nf flavors (t = ln mu^2)."""
    b, g = beta(nf), gamma(nf)
    f = lambda t, y: [-y[0] ** 2 * sum(bi * y[0] ** i for i, bi in enumerate(b)),
                      -y[0] * sum(gi * y[0] ** i for i, gi in enumerate(g))]
    s = solve_ivp(f, (2 * math.log(mu0), 2 * math.log(mu1)), [a, L], rtol=1e-11, atol=1e-13)
    return s.y[0, -1], s.y[1, -1]


def running(als_mz, mc, mb, mt):
    """Return {scale label: (mu, L(mu), a(mu))} along one downward path m_t -> 1 GeV. L(m_t) = 0."""
    a_mt, _ = seg(als_mz / math.pi, 0.0, MZ, mt, 5)
    rec = {"mt": (mt, 0.0, a_mt)}
    a, L = a_mt, 0.0
    for lab, mu, nf in (("MZ", MZ, 5), ("mb", mb, 5)):
        a, L = seg(a, L, rec[list(rec)[-1]][0], mu, nf); rec[lab] = (mu, L, a)
    L += math.log(1 + 89 / 432 * a ** 2); a *= 1 + 11 / 72 * a ** 2           # decouple b
    rec["mb-"] = (mb, L, a)
    for lab, mu, nf in (("3", 3.0, 4), ("2", 2.0, 4), ("mc", mc, 4)):
        a, L = seg(a, L, rec[list(rec)[-1]][0], mu, nf); rec[lab] = (mu, L, a)
    L += math.log(1 + 89 / 432 * a ** 2); a *= 1 + 11 / 72 * a ** 2           # decouple c
    rec["mc-"] = (mc, L, a)
    a, L = seg(a, L, mc, 1.0, 3); rec["1"] = (1.0, L, a)
    return rec


def masses_at(scale, rec, m):
    """m: dict of inputs (GeV): u, d, s at 2 GeV; c at m_c; b at m_b; t at m_t. All masses at one scale."""
    Ls = rec[scale][1]
    ref = {"u": "2", "d": "2", "s": "2", "c": "mc", "b": "mb", "t": "mt"}
    out = {}
    for q, r in ref.items():
        Lr = rec[r][1]
        # a mass defined above a threshold crossed on the way down picks up that decoupling jump
        out[q] = m[q] * math.exp(Ls - Lr)
    return out


def fit(light, middle, heavy):
    r = {0: math.sqrt(heavy), 1: math.sqrt(light), 2: math.sqrt(middle)}
    A = sum(r.values()) / 3
    c1 = sum(r[n] * cmath.exp(-2j * math.pi * n / 3) for n in range(3)) / 3
    return A, 2 * abs(c1) / A, cmath.phase(c1)


def koide(m):
    return sum(m) / sum(math.sqrt(x) for x in m) ** 2


CENTRAL = dict(u=2.14e-3, d=4.70e-3, s=93.46e-3, c=1.278, b=4.200, t=162.5, als=0.1180)
ERR = dict(u=0.08e-3, d=0.05e-3, s=0.58e-3, c=0.013, b=0.014, t=1.8, als=0.0009)


def reading_a(p, scale="1"):
    rec = running(p["als"], p["c"], p["b"], p["t"])
    m = masses_at(scale, rec, p)
    return fit(m["u"], m["c"], m["t"]), fit(m["d"], m["s"], m["b"]), m, rec


def main():
    # ---------------- checks on the running
    (up, dn, m1, rec) = reading_a(CENTRAL)
    mz = masses_at("MZ", rec, CENTRAL); m3 = masses_at("3", rec, CENTRAL); m2 = masses_at("2", rec, CENTRAL)
    print("checks: alpha_s(m_b) = %.4f, alpha_s(2 GeV) = %.4f, alpha_s(1 GeV) = %.4f"
          % (rec["mb"][2] * math.pi, rec["2"][2] * math.pi, rec["1"][2] * math.pi))
    print("        m_b(M_Z) = %.3f GeV (literature ~2.86-2.87); m_c(3 GeV) = %.3f GeV (FLAG 0.988 for m_c(m_c) ~1.28);"
          " m_c/m_s at 2 GeV = %.2f (FLAG lattice 11.77)" % (mz["b"], m3["c"], m2["c"] / m2["s"]))
    print("        masses at 1 GeV (MeV): " + ", ".join(f"{q} {v*1e3:.4g}" for q, v in m1.items()))
    for sc in ("1", "2", "3", "MZ"):
        u_, d_, _, _ = reading_a(CENTRAL, sc)
        print(f"        mu = {sc:>2s}: delta_up = {u_[2]:.5f}, delta_down = {d_[2]:.5f}   (same at every common scale)")

    # ---------------- Reading A, Monte Carlo
    rng = np.random.default_rng(9)
    N = 1500
    du, dd = [], []
    for _ in range(N):
        p = {k: rng.normal(CENTRAL[k], ERR[k]) for k in CENTRAL}
        u_, d_, _, _ = reading_a(p)
        du.append(u_[2]); dd.append(d_[2])
    res = {}
    for key, lab, cen, arr in (("G9a", "up-type   (u, c, t) at 1 GeV", up, du), ("G9b", "down-type (d, s, b) at 1 GeV", dn, dd)):
        sig = float(np.std(arr)); z = (cen[2] - TARGET) / sig
        print(f"{key} {lab}: b = {cen[1]:.4f} (b^2 = {cen[1]**2:.3f}), Q = {(1 + cen[1]**2/2)/3:.4f},"
              f" delta = {cen[2]:.5f} +- {sig:.5f} rad ({math.degrees(cen[2]):.3f} deg); {z:+.1f} sigma from 2/9")
        res[key] = abs(z) <= 2

    # ---------------- Reading B, constituent masses (Griffiths 2008)
    con = dict(u=336.0, d=340.0, s=486.0, c=1550.0, b=4730.0, t=177000.0)
    A, b, d = fit(con["d"], con["s"], con["b"])
    rng = np.random.default_rng(99)
    draws = [con[q] * (1 + 0.10 * rng.standard_normal(200000)) for q in ("d", "s", "b")]
    ds = np.array([fit(x, y, z)[2] for x, y, z in zip(*draws)])
    sig = float(ds.std()); z = (d - TARGET) / sig
    chance = min(1.0, 4 * sig / (math.pi / 3))
    print(f"G9c down-type constituent (340, 486, 4730): b = {b:.4f}, Q = {koide([340, 486, 4730]):.4f},"
          f" delta = {d:.5f} +- {sig:.5f} rad ({math.degrees(d):.3f} deg); {z:+.1f} sigma from 2/9;"
          f" chance of a 2-sigma hit at random: {chance:.1%}")
    res["G9c"] = abs(z) <= 2
    A, b, d = fit(con["u"], con["c"], con["t"])
    print(f"    (unscored) up-type constituent with Griffiths' free top (336, 1550, 177000): b = {b:.4f},"
          f" delta = {d:.5f} rad ({math.degrees(d):.3f} deg) -- the top never locks, so this family is not defined here")
    tau_t = 6.582e-25 / 1.42
    print(f"    top lifetime hbar/Gamma_t = {tau_t:.1e} s vs locking time hbar/Lambda_QCD ~ {6.582e-25/0.21:.1e} s"
          f" (ratio {6.582e-25/0.21/tau_t:.1f})")
    print("\nSCORE:", {k: ("HELD" if v else "LOST") for k, v in res.items()})


if __name__ == "__main__":
    main()
