#!/usr/bin/env python3
"""
ledger_math.py -- recompute every number in predictions/PREDICTIONS.md from its stated inputs.
Run:  python3 ledger_math.py      Needs numpy and scipy. Prints ASCII only.
When an input moves (a new PDG or FLAG value), edit it here, rerun, and compare against the ledger.
"""
import math
import numpy as np
from scipy.integrate import quad

# ---------------------------------------------------------------- inputs (MeV unless noted)
ME, MMU, MTAU, DMTAU = 0.51099895, 105.6583755, 1776.93, 0.09            # PDG
DM21, DM31, S12, S13 = 7.50e-5, 2.529e-3, 0.307, 0.0222                  # JUNO 2025 dm21; NuFIT 6.1 dm31 (eV^2)
DDM21, DDM31 = 0.12e-5, 0.021e-3                                          # their 1-sigma errors
DELTA_E = 0.2222220471                                                    # Brannen angle from e, mu (Koide exact)
FLAG_UP = (2.14, 1278.0)                                                  # m_u(2 GeV), m_c(m_c)
FLAG_DN = (4.70, 93.46, 4200.0)                                           # m_d, m_s (2 GeV), m_b(m_b)
MT_MSBAR_XSEC = 162.5                                                     # GeV, from cross sections
MT_DIRECT, DMT_DIRECT = 172.52, 0.33                                      # GeV, ATLAS+CMS
ALPHA_S_MZ, MZ = 0.1180, 91.1876


def koide_Q(m):
    r = np.sqrt(np.asarray(m, float))
    return (r ** 2).sum() / r.sum() ** 2


def turning(m):
    """Turning / stillness weight of a three-mass family (1 = Koide balance)."""
    return 3 * koide_Q(m) - 1


def bisect(f, lo, hi, n=200):
    flo = f(lo)
    for _ in range(n):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def p1():
    Q = koide_Q([ME, MMU, MTAU])
    dQ = abs(koide_Q([ME, MMU, MTAU + DMTAU]) - Q)
    mt_pred = bisect(lambda m: koide_Q([ME, MMU, m]) - 2 / 3, 1700, 1850)
    print(f"P1  Koide Q = {Q:.7f} +- {dQ:.7f}; exact 2/3 needs m_tau = {mt_pred:.3f} MeV (PDG {MTAU} +- {DMTAU})")


def p2():
    def masses(m1):
        return m1, math.sqrt(m1 ** 2 + DM21), math.sqrt(m1 ** 2 + DM31)

    def g(m1):
        a, b, c = masses(m1)
        return (a + b + c) / (-math.sqrt(a) + math.sqrt(b) + math.sqrt(c)) ** 2 - 2 / 3

    m1 = bisect(g, 1e-9, 0.01)
    m = masses(m1)
    ue = [(1 - S12) * (1 - S13), S12 * (1 - S13), S13]
    terms = [u * x * 1e3 for u, x in zip(ue, m)]
    mbb_lo, mbb_hi = max(0, max(terms) - (sum(terms) - max(terms))), sum(terms)
    mbeta = math.sqrt(sum(u * (x * 1e3) ** 2 for u, x in zip(ue, m)))
    print(f"P2  neutrinos (normal ordering, lightest root reversed): {m[0]*1e3:.3f}, {m[1]*1e3:.2f}, {m[2]*1e3:.2f} meV;"
          f" sum {sum(m)*1e3:.1f} meV; m_bb {mbb_lo:.1f}-{mbb_hi:.1f} meV; m_beta {mbeta:.1f} meV")


def p5():
    a_qcd, b_em = 2.52, 1.2933 - 2.52

    def f(delta):
        me = ME * (1 + delta)
        e0 = a_qcd * (1 + delta) + b_em
        return quad(lambda e: e * math.sqrt(e * e - me * me) * (e0 - e) ** 2, me, e0)[0]

    need = 888.1 / 877.8 - 1
    d = bisect(lambda x: f(x) / f(0) - 1 - need, 0.0, 0.01)
    print(f"P5  a local Higgs-field rise of {d:.1e} would shorten bottle lifetimes by {need:.2%}; atomic clocks bound such shifts at ~1e-18")


def alpha_s(mu):
    b0 = 23 / (12 * math.pi)
    return ALPHA_S_MZ / (1 + b0 * ALPHA_S_MZ * math.log(mu ** 2 / MZ ** 2))


def pole_from_msbar(mbar):
    a = alpha_s(mbar) / math.pi
    return mbar * (1 + 4 / 3 * a + 8.236 * a ** 2 + 73.64 * a ** 3 + 1700 * a ** 4)


def p6():
    td = turning(FLAG_DN)
    mt = bisect(lambda m: turning([FLAG_UP[0], FLAG_UP[1], m]) - td - 1 / 3, 1e4, 1e6)
    tu_x = turning([FLAG_UP[0], FLAG_UP[1], MT_MSBAR_XSEC * 1e3])
    print(f"P6  up - down turning (own-mass convention) with m_t(m_t) = {MT_MSBAR_XSEC} GeV: {tu_x - td:.4f};"
          f" exact 1/3 needs m_t(m_t) = {mt/1e3:.1f} GeV")
    pole = pole_from_msbar(mt / 1e3)
    check = pole_from_msbar(MT_MSBAR_XSEC)
    print(f"    conversion check: m_t(m_t) {MT_MSBAR_XSEC} -> pole {check:.1f} GeV; predicted {mt/1e3:.1f} -> pole {pole:.1f} GeV")
    for amb in (0.5, 1.0):
        z = (MT_DIRECT - pole) / math.sqrt(DMT_DIRECT ** 2 + amb ** 2 + 0.2 ** 2)
        print(f"    vs direct {MT_DIRECT} +- {DMT_DIRECT} GeV with {amb} GeV definition ambiguity: {z:.1f} sigma")
    print(f"    fallout: SM W mass {80.357 + 0.0061 * (pole - 172.5):.3f} GeV (measured ~80.365 +- 0.010);"
          f" Higgs vacuum {'absolutely stable' if pole < 171.5 else 'metastable'} (stability needs pole < ~171.5 GeV)")


def p7():
    d = DELTA_E + math.pi / 12
    lam = [1 + math.sqrt(2) * math.cos(d + 2 * math.pi * n / 3) for n in range(3)]
    h, l, m = [x * x for x in lam]
    pred = (m * m - l * l) / (h * h - l * l)
    meas = DM21 / DM31
    err = meas * math.hypot(DDM21 / DM21, DDM31 / DM31)
    alik = (3 - 2 * math.sqrt(2)) ** 2
    s = math.sqrt(DM31 / (h * h - l * l))
    print(f"P7  15-deg step: dm21^2/dm31^2 = {pred:.5f} vs measured {meas:.5f} +- {err:.5f} ({(pred - meas) / err:+.2f} sigma);"
          f" rival m1=0 relation {alik:.5f} ({(alik - meas) / err:+.2f} sigma)")
    print(f"    masses {s*l*1e3:.3f}, {s*m*1e3:.2f}, {s*h*1e3:.2f} meV; sum {s*(l+m+h)*1e3:.1f} meV")


def p8():
    import mpmath as mp
    mp.mp.dps = 30
    me, mmu = mp.mpf(ME), mp.mpf(MMU)
    c = lambda d, b, n: 1 + b * mp.cos(d + 2 * mp.pi * n / 3)
    d = mp.mpf(2) / 9
    b = mp.findroot(lambda b: c(d, b, 2) / c(d, b, 1) - mp.sqrt(mmu / me), mp.sqrt(2))
    A = mp.sqrt(me) / c(d, b, 1)
    mt = (A * c(d, b, 0)) ** 2
    Q = (me + mmu + mt) / (mp.sqrt(me) + mp.sqrt(mmu) + mp.sqrt(mt)) ** 2
    print(f"P8  angle exactly 2/9: Koide Q = {mp.nstr(Q, 10)}, m_tau = {mp.nstr(mt, 10)} MeV (Koide-exact P1: 1776.969)")


if __name__ == "__main__":
    p1()
    p2()
    p5()
    p6()
    p7()
    p8()
