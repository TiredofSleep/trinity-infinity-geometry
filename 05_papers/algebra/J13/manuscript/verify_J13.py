"""
verify_J13.py
Copyright (c) 2026 B.R. Sanders and M. Gish.
Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0).
https://creativecommons.org/licenses/by/4.0/

Self-contained verification of J13:
  "The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice):
   Cyclotomic Forcing on Z/10Z"

Six checks mapped one-to-one to the manuscript's load-bearing claims:

  C1  Minimal polynomial identification at p=7:
        g(x) = x^3 - x^2 - 2x + 1 is the minimal polynomial of A_7 = 2 cos(pi/7)
        over Q. Verified via sympy (a) symbolic minimal_polynomial, and
        (b) algebraic substitution into g(x) and high-precision numerical zero.
  C2  Erroneous-polynomial disambiguation (the M1 referee fix):
        h(x) = 8 x^3 - 4 x^2 - 4 x + 1 is the minimal polynomial of cos(pi/7)
        (not 2 cos(pi/7)). Verified: h(cos(pi/7)) = 0 and h(2 cos(pi/7)) != 0,
        and the substitution h(x/2) * 8 / 8 = x^3 - x^2 - 2 x + 1 = g(x).
  C3  Irreducibility of g over Q:
        g is monic in Z[x]; rational-root candidates are {+1, -1};
        g(1) = -1, g(-1) = 1, both nonzero, so g has no rational root,
        so g (degree 3, monic, no rational root) is irreducible over Q.
        Sympy `Poly.is_irreducible` confirms.
  C4  Discriminant of g equals 7^2 = 49 (a perfect square):
        disc(g) = 49, so Gal(g/Q) <= A_3.
  C5  Galois group of g is the cyclic group Z/3Z:
        since g is irreducible of degree 3 and disc(g) is a rational square,
        Gal(g/Q) is the unique transitive subgroup of S_3 contained in A_3,
        which is A_3 = Z/3Z. (Splitting field is the totally real cubic
        subfield of Q(zeta_7).)
  C6  Cyclotomic threshold at p=5 vs p=7:
        deg_Q(A_p) = (p-1)/2 for odd primes p. At p=5 the minimal polynomial
        of A_5 = 2 cos(pi/5) = phi over Q is x^2 - x - 1 (degree 2). At p=7
        the minimal polynomial is g(x) above (degree 3). The threshold (the
        smallest prime with deg_Q(A_p) >= 3) is p=7. This is the structural
        content selecting r=7 in Theorem 1.1 of the manuscript.

Author lane: B.R. Sanders, M. Gish
License: CC-BY-4.0 (journal-bundled submission script)
Runtime: < 5 s on standard hardware. Dependencies: sympy, mpmath (sympy core).
"""

import sys

from sympy import (
    Poly, Symbol, cos, pi, sqrt, simplify, sympify, Rational, S, expand,
)
from sympy.polys.numberfields import minimal_polynomial
from sympy.polys.polytools import Poly as _Poly
from sympy import nsimplify, N


def title(s):
    print("=" * 70)
    print(s)
    print("=" * 70)


def check(name, passed, detail=""):
    flag = "PASS" if passed else "FAIL"
    print(f"  [{flag}] {name}" + (f"   ({detail})" if detail else ""))
    return passed


def main():
    x = Symbol("x")

    A7 = 2 * cos(pi / 7)           # 2 cos(pi/7) -- the algebraic number of interest
    A5 = 2 * cos(pi / 5)           # phi = (1 + sqrt 5) / 2

    g = x**3 - x**2 - 2*x + 1       # claimed minimal polynomial of A_7
    h = 8*x**3 - 4*x**2 - 4*x + 1   # the erroneous polynomial (actually m.p. of cos(pi/7))

    all_pass = True

    # ----- C1 -----
    title("C1  Minimal polynomial of 2 cos(pi/7) over Q is x^3 - x^2 - 2 x + 1")
    mp_A7 = minimal_polynomial(A7, x)
    c1_symbolic = simplify(mp_A7 - g) == 0
    # Trig identities for sympy don't fold to 0 under simplify() alone;
    # the gold standard is (a) sympy's minimal_polynomial returns g and
    # (b) 50-digit mpmath shows the substitution lies at < 1e-40 from zero.
    c1_numeric_abs = abs(N(g.subs(x, A7), 50))
    c1_numeric = c1_numeric_abs < Rational(1, 10**40)
    ok = c1_symbolic and c1_numeric
    check("sympy minimal_polynomial(A_7, x) == g(x)", c1_symbolic,
          detail=f"got {mp_A7}")
    check("|g(2 cos(pi/7))| < 1e-40 at 50-digit precision", c1_numeric,
          detail=f"|...| = {c1_numeric_abs}")
    all_pass &= ok

    # ----- C2 -----
    title("C2  Disambiguation: 8 x^3 - 4 x^2 - 4 x + 1 is m.p. of cos(pi/7), not 2 cos(pi/7)")
    # sympy.minimal_polynomial returns an integer-coefficient minimal
    # polynomial; for cos(pi/7) it returns exactly 8 x^3 - 4 x^2 - 4 x + 1.
    # (Confirms the classical Lehmer / Niven form of the cos(pi/7) MP.)
    mp_cos = minimal_polynomial(cos(pi / 7), x)
    c2_eight_times = simplify(mp_cos - h) == 0
    # h(cos(pi/7)) = 0 at 50-digit precision (sympy simplify doesn't fold
    # trig automatically, but numerical evaluation does).
    h_at_cos = abs(N(h.subs(x, cos(pi / 7)), 50))
    c2_h_kills_cos = h_at_cos < Rational(1, 10**40)
    # h(2 cos(pi/7)) is far from zero (this is the M1 fix: if you put
    # 2 cos(pi/7) into the cos(pi/7) polynomial, you do NOT get a root).
    h_at_A7 = abs(N(h.subs(x, A7), 50))
    c2_h_does_not_kill_A7 = h_at_A7 > Rational(1, 100)
    # Calibration bridge: h(x/2) = (1/1) * g(x) up to the leading-coefficient
    # 8 vs 1 normalisation; computed exactly below.
    h_sub = expand(h.subs(x, x / 2))
    # h(x/2) = x^3 - (1/2) x^2 - (1/2) x + 1/8; multiplied by 8 gives the same
    # leading-coefficient form as h, but the monic form is g(x).
    c2_substitution_bridge = simplify(h_sub - g) == 0
    ok = (c2_eight_times and c2_h_kills_cos and c2_h_does_not_kill_A7
          and c2_substitution_bridge)
    check("sympy minimal_polynomial(cos(pi/7), x) == 8 x^3 - 4 x^2 - 4 x + 1",
          c2_eight_times, detail=f"sympy m.p. of cos(pi/7) = {mp_cos}")
    check("|h(cos(pi/7))| < 1e-40 at 50-digit precision",
          c2_h_kills_cos, detail=f"|h(cos pi/7)| = {h_at_cos}")
    check("|h(2 cos(pi/7))| > 1e-2 numerically (it is far from a root)",
          c2_h_does_not_kill_A7,
          detail=f"|h(A_7)| = {N(h.subs(x, A7), 8)}")
    check("h(x/2) = g(x): the calibration bridge cos vs 2 cos",
          c2_substitution_bridge,
          detail=f"h(x/2) = {h_sub}")
    all_pass &= ok

    # ----- C3 -----
    title("C3  Irreducibility of g over Q")
    g_poly = _Poly(g, x, domain="QQ")
    c3_irred = g_poly.is_irreducible
    # The two rational-root candidates by the rational root theorem are +/- 1
    g_at_pos1 = g.subs(x, 1)
    g_at_neg1 = g.subs(x, -1)
    c3_rrt = (g_at_pos1 != 0) and (g_at_neg1 != 0)
    ok = c3_irred and c3_rrt
    check("sympy Poly(g, x).is_irreducible over QQ", c3_irred)
    check("g(1) = -1, g(-1) = 1 (no rational root)", c3_rrt,
          detail=f"g(1) = {g_at_pos1}, g(-1) = {g_at_neg1}")
    all_pass &= ok

    # ----- C4 -----
    title("C4  Discriminant of g equals 49 = 7^2 (a perfect square)")
    disc_g = g_poly.discriminant()
    c4_disc_value = disc_g == 49
    sqrt_disc = int(disc_g) ** 0.5
    c4_perfect_square = abs(sqrt_disc - round(sqrt_disc)) < 1e-9
    ok = c4_disc_value and c4_perfect_square
    check("disc(g) == 49", c4_disc_value, detail=f"disc(g) = {disc_g}")
    check("disc(g) is a perfect square (sqrt = 7)", c4_perfect_square,
          detail=f"sqrt = {sqrt_disc}")
    all_pass &= ok

    # ----- C5 -----
    title("C5  Galois group of g over Q is the cyclic group Z/3Z (=A_3)")
    # Theorem: for irreducible cubic over Q, Gal = A_3 iff disc is a Q-square,
    # else Gal = S_3. We verified irreducibility (C3) and disc = 49 = 7^2 (C4).
    c5 = c3_irred and c4_disc_value and c4_perfect_square
    check("Gal(g/Q) = Z/3Z (cyclic) by Disc-square criterion for cubics",
          c5, detail="irreducible cubic + disc a Q-square => Gal = A_3 = Z/3Z")
    all_pass &= c5

    # ----- C6 -----
    title("C6  Cyclotomic threshold: deg_Q(A_p) = (p-1)/2, so p=7 is the first cubic")
    mp_A5 = minimal_polynomial(A5, x)
    mp_A5_poly = _Poly(mp_A5, x)
    mp_A7_poly = _Poly(mp_A7, x)
    c6_A2_degree = 0       # A_2 = 0 is rational; the m.p. of 0 is x, often reported as degree 1
    c6_A3_degree = 1       # A_3 = 1 is rational; m.p. = x - 1
    c6_A5_degree = mp_A5_poly.degree() == 2
    c6_A7_degree = mp_A7_poly.degree() == 3
    # Confirm A_5 is the golden ratio: m.p. x^2 - x - 1
    c6_A5_polynomial = simplify(mp_A5 - (x**2 - x - 1)) == 0
    ok = c6_A5_degree and c6_A7_degree and c6_A5_polynomial
    check("deg_Q(A_5) = 2", c6_A5_degree, detail=f"m.p.(A_5) = {mp_A5}")
    check("m.p.(A_5) = x^2 - x - 1 (the golden-ratio polynomial)", c6_A5_polynomial)
    check("deg_Q(A_7) = 3", c6_A7_degree, detail=f"m.p.(A_7) = {mp_A7}")
    check("threshold deg<=2 at p=5, deg>=3 at p=7 (cyclotomic 5/7 driver)",
          c6_A5_degree and c6_A7_degree)
    all_pass &= ok

    print()
    title("SUMMARY")
    if all_pass:
        print("  6 / 6 PASS")
        print()
        print("  Structural content reproduced at machine precision:")
        print("    - M1 fix verified: x^3 - x^2 - 2 x + 1 is m.p. of 2 cos(pi/7)")
        print("    - 8 x^3 - 4 x^2 - 4 x + 1 is m.p. of cos(pi/7), NOT 2 cos(pi/7)")
        print("    - Substitution h(x/2) = g(x) records the calibration bridge")
        print("    - g irreducible / disc 49 / Gal = Z/3Z (the totally real")
        print("      cubic subfield of Q(zeta_7))")
        print("    - Cyclotomic threshold deg<=2 at p=5 vs deg>=3 at p=7 selects 5/7")
        sys.exit(0)
    else:
        print("  AT LEAST ONE CHECK FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
