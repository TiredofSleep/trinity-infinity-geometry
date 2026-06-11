"""b2_lp_crosscheck.py -- B2 action item: numerical cross-check of the
dim-6 magic-function candidate against the Cohn-Elkies LP landscape.

WHAT THIS COMPUTES (all well-defined today, no analytic continuation):

  C1  I_-(r^2) profile by EXACT termwise Laplace transform:
        I_-(r^2) = sum_n a_n * 2/(pi (r^2+2n))^3
      (a_n = coefficients of eta(t)^6 eta(3t)^6; absolutely convergent,
       a_n = O(n^3) by Deligne). Cross-checked against direct quadrature.

  C2  The t->0 endpoint of I_+ AS WRITTEN diverges for EVERY r^2:
      psi_+ has a simple pole at cusp 0, so psi_+(it) ~ C e^{2pi/(3t)}
      as t->0. Verified numerically via the Fricke functional equation.
      (The handoff's "converges for r^2 > 2" tracked only the infinity
      cusp. The true object requires the Viazovska contour definition.)

  C3  The cusp-infinity-REGULARIZED profile
        Ihat(r^2) = int_{1/sqrt3}^inf [psi_+(it) + 728 e^{2pi t} + 5376]
                        e^{-pi r^2 t} t^2 dt
                    - 728 * G3(pi(r^2-2)/sqrt3) / (pi(r^2-2))^3
                    - 5376 * G3(pi r^2 /sqrt3) / (pi r^2)^3
      where G3(x) = upper incomplete gamma(3, x) -- i.e. the part of I_+
      visible from the infinity cusp, with the two singular Laurent terms
      reattached in closed form (valid r^2 > 2).

  C4  Sign/feasibility slice: f_6 = sin^2(pi r^2/2) [alpha I_+ + beta I_-]
      needs alpha*I_+ + beta*I_- <= 0 on [2, inf). Report the sign
      structure of Ihat and I_- and the implied (alpha, beta) region.

  C5  LP-landscape verdict row: with K(R^6) <= 77 (de Laat-Leijenhorst-
      de Muinck Keizer 2024, SDP) and the plain two-point LP optimum
      strictly ABOVE the SDP value, LP-sharpness at 72 is impossible;
      print the reframing options for Paper 1.

CC-BY-4.0. Sanders + Claude (B2 execution 2026-06-10).
"""
import io
import json
import os

import mpmath as mp

mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

N_ETA = 120


# ----------------------------------------------------------------------
# eta(t)^6 eta(3t)^6 coefficients (exact ints, same routine as the
# independent verifier)
# ----------------------------------------------------------------------
def series_mul(a, b, n):
    out = [0] * n
    for i, ai in enumerate(a):
        if ai == 0 or i >= n:
            continue
        for j, bj in enumerate(b):
            if i + j >= n:
                break
            if bj:
                out[i + j] += ai * bj
    return out


def eta_power6(n, step=1):
    base = [0] * n
    base[0] = 1
    for m in range(1, (n - 1) // step + 1):
        nxt = base[:]
        for i in range(n - step * m):
            if base[i]:
                nxt[i + step * m] -= base[i]
        base = nxt
    out = [0] * n
    out[0] = 1
    for _ in range(6):
        out = series_mul(out, base, n)
    return out


prod = series_mul(eta_power6(N_ETA, 1), eta_power6(N_ETA, 3), N_ETA)
a = {n + 1: prod[n] for n in range(N_ETA - 1)}          # F = q * prod

# psi_+ Laurent coefficients from the independent-verification data
with io.open(os.path.join(DATA, "claudecode_independent.json"),
             encoding="utf-8") as fh:
    psi_tab = {int(k): int(v) for k, v in
               json.load(fh)["psi_plus_laurent"].items()}
PSI_MAX = max(psi_tab)

print("=" * 70)
print("B2 -- LP cross-check for the dim-6 magic-function candidate")
print("=" * 70)

# ----------------------------------------------------------------------
# C1: I_- exact termwise Laplace vs direct quadrature
# ----------------------------------------------------------------------
def I_minus(r2):
    return mp.nsum(lambda n: a.get(int(n), 0) * 2 / (mp.pi * (r2 + 2 * n)) ** 3,
                   [1, N_ETA - 1])


def F_num(t):
    q = mp.exp(-2 * mp.pi * t)
    return mp.nsum(lambda n: a.get(int(n), 0) * q ** int(n), [1, N_ETA - 1])


r2_test = mp.mpf(3)
direct = mp.quad(lambda t: F_num(t) * mp.exp(-mp.pi * r2_test * t) * t ** 2,
                 [0, mp.inf])
term = I_minus(r2_test)
c1 = abs(direct - term) / abs(term) < mp.mpf("1e-12")
print(f"\nC1 I_-(3): termwise {mp.nstr(term, 10)} vs quad {mp.nstr(direct, 10)}"
      f"  {'OK' if c1 else 'FAIL'}")

# ----------------------------------------------------------------------
# C2: t->0 divergence of the I_+ integrand (cusp-0 pole)
# ----------------------------------------------------------------------
def psi_num(t):
    q = mp.exp(-2 * mp.pi * t)
    return mp.fsum(psi_tab[k] * q ** k for k in sorted(psi_tab))


print("\nC2 cusp-0 growth of psi_+(it) as t->0 (via Fricke eq "
      "psi(it) = -27 t'^6 psi(it') with t' = 1/(3t)):")
c2 = True
prev = None
for t in (mp.mpf("0.12"), mp.mpf("0.08"), mp.mpf("0.05")):
    tp = 1 / (3 * t)
    val = -27 * tp ** 6 * psi_num(tp)
    pred = mp.exp(2 * mp.pi / (3 * t))          # leading growth scale
    print(f"   t={float(t):.2f}: psi_+(it) = {mp.nstr(val, 6)}   "
          f"(e^(2pi/3t) = {mp.nstr(pred, 4)})")
    if prev is not None and abs(val) <= abs(prev):
        c2 = False
    prev = val
print(f"   => integrand diverges at t->0 for EVERY r^2; the naive real "
      f"integral I_+ is ill-defined at the 0-end  {'OK' if c2 else 'FAIL'}")

# ----------------------------------------------------------------------
# C3: cusp-infinity-regularized Ihat(r^2) for r^2 > 2
# ----------------------------------------------------------------------
T0 = 1 / mp.sqrt(3)


def G3(x):
    return mp.gammainc(3, x)            # upper incomplete gamma


def psi_reg(t):
    """psi_+(it) + 728 e^{2pi t} + 5376  (the n>=1 tail; decays e^{-2pi t})."""
    q = mp.exp(-2 * mp.pi * t)
    return mp.fsum(psi_tab[k] * q ** k for k in sorted(psi_tab) if k >= 1)


def I_hat(r2):
    tail = mp.quad(lambda t: psi_reg(t) * mp.exp(-mp.pi * r2 * t) * t ** 2,
                   [T0, mp.inf])
    s1 = mp.pi * (r2 - 2)
    s0 = mp.pi * r2
    sing = (-728) * G3(s1 * T0) / s1 ** 3 + (-5376) * G3(s0 * T0) / s0 ** 3
    return tail + sing


print("\nC3 profiles on r^2 in (2, 12]:")
print(f"   {'r^2':>6} | {'Ihat(r^2)':>16} | {'I_-(r^2)':>14} | ratio Ihat/I_-")
grid = [mp.mpf(x) / 100 for x in
        (205, 210, 225, 250, 300, 400, 500, 600, 800, 1000, 1200)]
profile = []
for r2 in grid:
    ih = I_hat(r2)
    im = I_minus(r2)
    profile.append((float(r2), float(ih), float(im)))
    print(f"   {float(r2):>6.2f} | {mp.nstr(ih, 8):>16} | "
          f"{mp.nstr(im, 8):>14} | {mp.nstr(ih / im, 6)}")

# ----------------------------------------------------------------------
# C4: sign / feasibility slice
# ----------------------------------------------------------------------
ih_signs = {s for _, ih, _ in profile for s in [ih > 0]}
im_pos = all(im > 0 for _, _, im in profile)
ih_neg = all(ih < 0 for _, ih, _ in profile)
print("\nC4 sign structure:")
print(f"   I_-  > 0 on the whole grid: {im_pos}")
print(f"   Ihat < 0 on the whole grid: {ih_neg}"
      f"   (Ihat -> -inf like -1456/(pi(r^2-2))^3 as r^2 -> 2+)")
if ih_neg and im_pos:
    rat_min = min(-ih / im for _, ih, im in profile)
    rat_max = max(-ih / im for _, ih, im in profile)
    print(f"   bracket alpha*Ihat + beta*I_- <= 0 on the grid iff "
          f"beta/alpha <= min(-Ihat/I_-) = {rat_min:.6g}  (alpha > 0)")
    print(f"   [-Ihat/I_- ranges {rat_min:.6g} .. {rat_max:.6g} on the grid]")

# ----------------------------------------------------------------------
# C5: LP-landscape verdict
# ----------------------------------------------------------------------
print("""
C5 LP-landscape verdict (external anchors, 2026-06-10):
   K(R^6) lower bound:            72   (E_6 root system)
   K(R^6) best upper bound:       77   (de Laat-Leijenhorst-de Muinck
                                        Keizer 2024, SDP / D_4 optimality
                                        paper; via cohn.mit.edu table)
   Plain two-point LP optimum:    strictly ABOVE the SDP value 77
                                  (SDP refines LP; LP alone gave ~82
                                  in Odlyzko-Sloane 1979)

   CONSEQUENCE: no function satisfying ONLY the two-point Cohn-Elkies
   kissing conditions can certify 72. The conjecture's sharpness claim
   must therefore live BEYOND the plain LP:
     (a) reframe f_6 as the explicit ANALYTIC feasible function attaining
         (or approaching) the LP optimum ~78-82 -- still novel: no
         explicit modular-form LP function is known in dim 6; or
     (b) keep 72 as the target but state that sharpness requires
         higher-order (three-point / SDP) positivity structure -- i.e.
         the level-3 analog of WHY dim 6 is not dim 8; or
     (c) honest negative: document the obstruction precisely (this is
         itself the 'where level 3 differs from level 1' theorem).
   Paper 1 Section 5 must adopt one of these framings BEFORE submission.
""")

out = {
    "anchors": {"lower": 72, "upper_SDP_2024": 77,
                "LP_two_point": "strictly above 77 (LP >= SDP); ~82 in Odlyzko-Sloane 1979"},
    "I_profiles": [{"r2": r, "I_hat_reg": ih, "I_minus": im}
                   for r, ih, im in profile],
    "verdict": "LP-sharpness at 72 impossible; reframe per C5 (a)/(b)/(c)",
}
with io.open(os.path.join(DATA, "b2_lp_crosscheck.json"), "w",
             encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print("Saved: data/b2_lp_crosscheck.json")
