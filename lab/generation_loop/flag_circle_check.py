#!/usr/bin/env python3
"""flag_circle_check.py -- the exact mathematics inside Rounds G3 and G6 (the "flag circle"), checked symbolically.

For unit vectors u_i with projectors P_i = u_i u_i^T and weights w_i > 0, the mixture rho = (sum w_i P_i) / (sum w_i)
has purity tr(rho^2) = (sum_i w_i^2 + 2 sum_{i<j} c_ij w_i w_j) / (sum w_i)^2, where c_ij = (u_i . u_j)^2.
So purity 2/3 (Koide's value) is the quadric
        sum_i w_i^2 + 6 sum_{i<j} (c_ij - 2/3) w_i w_j = 0,
and a cross term drops out exactly when that pair's squared cosine is 2/3.
On the cube's flag (edge e, face diagonal f, body diagonal b) the squared cosines are 1/2, 1/3 and 2/3, so the
f-b term vanishes, and with w_e = 1 the quadric is the circle (w_f - 1/2)^2 + (w_b - 1)^2 = 1/4.
Also: an equal pair has purity (1 + c)/2, which is 2/3 exactly at c = 1/3, the magic angle (the base's 1/3).
ASCII output; needs sympy.
"""
import sympy as sp

FAILS = []


def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok:
        FAILS.append(name)


def proj(v):
    v = sp.Matrix(v) / sp.sqrt(sum(x ** 2 for x in v))
    return v * v.T


e, f, b = proj([1, 0, 0]), proj([1, 1, 0]), proj([1, 1, 1])
c = lambda P, Q: sp.simplify((P * Q).trace())
check("the flag's squared cosines are 1/2 (e-f), 1/3 (e-b) and 2/3 (f-b)",
      (c(e, f), c(e, b), c(f, b)) == (sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(2, 3)))

we, wf, wb, phi = sp.symbols("w_e w_f w_b phi", real=True)
rho = (we * e + wf * f + wb * b) / (we + wf + wb)
purity = sp.together((rho * rho).trace())
num = sp.expand(sp.numer(sp.together(purity - sp.Rational(2, 3))) )
quad = sp.expand(we ** 2 + wf ** 2 + wb ** 2 - we * wf - 2 * we * wb)
check("purity 2/3 is the quadric w_e^2 + w_f^2 + w_b^2 - w_e w_f - 2 w_e w_b = 0", sp.simplify(num / quad).is_number)
check("with w_e = 1 the quadric is the circle (w_f - 1/2)^2 + (w_b - 1)^2 = 1/4",
      sp.expand(quad.subs(we, 1) - ((wf - sp.Rational(1, 2)) ** 2 + (wb - 1) ** 2 - sp.Rational(1, 4))) == 0)
on = purity.subs({we: 1, wf: sp.Rational(1, 2) + sp.cos(phi) / 2, wb: 1 + sp.sin(phi) / 2})
check("every point of the circle, w_f = 1/2 + cos(phi)/2, w_b = 1 + sin(phi)/2, has purity exactly 2/3",
      sp.simplify(on - sp.Rational(2, 3)) == 0)

cc, w1, w2 = sp.symbols("c w1 w2", positive=True)
gen = sp.expand(3 * (w1 ** 2 + w2 ** 2 + 2 * cc * w1 * w2) - 2 * (w1 + w2) ** 2)
check("for two lines, purity 2/3 is w1^2 + w2^2 + 6(c - 2/3) w1 w2 = 0 (the cross term vanishes iff c = 2/3)",
      sp.expand(gen - (w1 ** 2 + w2 ** 2 + 6 * (cc - sp.Rational(2, 3)) * w1 * w2)) == 0)
pair = sp.simplify(((e + b) / 2 * (e + b) / 2).trace())
check("an equal edge + body-diagonal pair (the magic angle, cos^2 = 1/3) has purity (1 + 1/3)/2 = 2/3",
      pair == sp.Rational(2, 3))

for wts in ((1, 0.141796, 1.348841), (1, 0.103649, 0.695195)):
    r2 = (wts[1] - 0.5) ** 2 + (wts[2] - 1) ** 2
    check(f"the G6 lepton point {wts} lies on the circle: (w_f - 1/2)^2 + (w_b - 1)^2 = {r2:.6f}",
          abs(r2 - 0.25) < 5e-6)

print()
print("FAILED: " + ", ".join(FAILS) if FAILS else "All checks passed.")
raise SystemExit(1 if FAILS else 0)
