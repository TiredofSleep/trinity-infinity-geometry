#!/usr/bin/env python3
# ============================================================
# verify_J15_galois.py
#
# Verification for: "Galois D_4 over LMFDB 4.2.10224.1:
# Number-Field Identification of the Four-Core Attractor"
# (Sanders, Gish, 2026).
#
# Six checks for the Galois-theoretic content of the quartic
#   f(x) = x^4 + 4x^3 - x^2 + 2x - 2.
#
#   1. Irreducibility over Q (case-by-case + mod-7 cross-check;
#      mod-5 negative example also recorded).
#   2. Polynomial discriminant = -2^6 * 3^2 * 71 = -40896.
#   3. Cubic resolvent g(y) = y^3 + y^2 + 16y + 36
#                    = (y + 2)(y^2 - y + 18).
#   4. Galois group D_4 (vs C_4): direct via
#      sympy.factor(f, extension=[sqrt(-71)]).
#   5. Q(sqrt(3)) subfield: explicit factorization of f as a
#      product of two quadratics over Q(sqrt(3))[x].
#   6. LMFDB 4.2.10224.1 identification: Tschirnhaus x -> -x - 1
#      maps f to the canonical defining polynomial
#      x^4 - 7x^2 - 12x - 8; index of Z[alpha] in O_K is 2.
#
# Total runtime: ~2 seconds. Run:
#   /c/ck_venv/lora312/Scripts/python.exe verify_J15_galois.py
#
# Copyright (c) 2026 B.R. Sanders and M. Gish.
# Licensed under the Creative Commons Attribution 4.0 International
# License (CC-BY-4.0). https://creativecommons.org/licenses/by/4.0/
# ============================================================

import sys
import sympy as sp


def hr(label):
    print()
    print("=" * 60)
    print(label)
    print("=" * 60)


def check_irreducibility():
    hr("Check 1: f(x) = x^4 + 4x^3 - x^2 + 2x - 2 irreducible over Q")
    x = sp.Symbol('x')
    f = x**4 + 4*x**3 - x**2 + 2*x - 2

    # No integer roots: f(+/-1), f(+/-2) all nonzero
    roots_test = {n: int(f.subs(x, n)) for n in (-2, -1, 1, 2)}
    print(f"  f at +/-1, +/-2:    {roots_test}")
    no_int_roots = all(v != 0 for v in roots_test.values())
    print(f"  no integer roots:   {no_int_roots}")

    # Case-by-case for f = (x^2 + ax + b)(x^2 + cx + d) over Z:
    # bd = -2, so (b, d) in {(1, -2), (-1, 2), (2, -1), (-2, 1)}.
    # a + c = 4, ac + b + d = -1, ad + bc = 2.
    # For each (b, d) eliminate c = 4 - a, solve linear ad + bc = 2 for a,
    # then check the quadratic constraint ac = -1 - b - d.
    cases = []
    for b, d in [(1, -2), (-1, 2), (2, -1), (-2, 1)]:
        # ad + bc = 2  =>  a*d + b*(4 - a) = 2  =>  a*(d - b) = 2 - 4*b
        denom = d - b
        if denom == 0:
            cases.append((b, d, None, "indeterminate (d == b)"))
            continue
        num = 2 - 4*b
        if num % denom != 0:
            cases.append((b, d, sp.Rational(num, denom), "a not in Z"))
            continue
        a = num // denom
        c = 4 - a
        if a*c == -1 - b - d:
            cases.append((b, d, a, "QUADRATIC CONSTRAINT SATISFIED -- need closer look"))
        else:
            cases.append((b, d, a, f"a={a},c={c}: ac={a*c} != {-1 - b - d}"))
    for (b, d, a, note) in cases:
        print(f"  (b, d) = ({b}, {d}): {note}")
    case_ok = all("CONSTRAINT SATISFIED" not in note for (_b, _d, _a, note) in cases)
    print(f"  No integer (a, b, c, d) quadratic factorization: {case_ok}")

    # mod-7 cross-check (manuscript's "one-line proof")
    f_mod7 = sp.factor(f, modulus=7)
    mod7_irreducible = (f_mod7 == f) or (sp.Poly(f_mod7, x).degree() == 4 and not isinstance(f_mod7, sp.Mul))
    # Robust check: a degree-4 polynomial mod p is irreducible iff factor() returns it unchanged
    # (sympy's factor with modulus normalizes leading coefficients).
    f_mod7_explicit = sp.Poly(f, x, modulus=7).factor_list()
    mod7_irreducible = (len(f_mod7_explicit[1]) == 1 and f_mod7_explicit[1][0][1] == 1
                       and sp.Poly(f_mod7_explicit[1][0][0], x).degree() == 4)
    print(f"  f mod 7 factor_list: {f_mod7_explicit}")
    print(f"  Irreducible mod 7:   {mod7_irreducible}")

    # mod-5 negative example (recorded; not used for proof)
    f_mod5 = sp.factor(f, modulus=5)
    print(f"  f mod 5 factored:    {f_mod5}  (reducible -- the recorded counterexample)")

    ok = no_int_roots and case_ok and mod7_irreducible
    print()
    print(f"  Check 1 PASS: {ok}")
    return ok


def check_discriminant():
    hr("Check 2: polynomial discriminant = -40896 = -2^6 * 3^2 * 71")
    x = sp.Symbol('x')
    f = x**4 + 4*x**3 - x**2 + 2*x - 2
    disc = int(sp.Poly(f, x).discriminant())
    factored = sp.factorint(abs(disc))
    print(f"  disc(f) = {disc}")
    print(f"  |disc|  = {factored}")
    sign_ok = (disc < 0)
    val_ok  = (disc == -40896)
    fact_ok = (factored == {2: 6, 3: 2, 71: 1})
    ok = sign_ok and val_ok and fact_ok
    print(f"  Sign negative:                {sign_ok}")
    print(f"  Value = -40896:               {val_ok}")
    print(f"  Prime factorization 2^6.3^2.71: {fact_ok}")
    print()
    print(f"  Check 2 PASS: {ok}")
    return ok


def check_resolvent_cubic():
    hr("Check 3: cubic resolvent g(y) = (y+2)(y^2 - y + 18)")
    y = sp.Symbol('y')

    # Standard cubic resolvent of x^4 + b x^3 + c x^2 + d x + e is
    #   g(y) = y^3 - c y^2 + (b d - 4 e) y - (b^2 e - 4 c e + d^2).
    # For f = x^4 + 4x^3 - x^2 + 2x - 2, (b, c, d, e) = (4, -1, 2, -2):
    b, c, d, e = 4, -1, 2, -2
    g = y**3 - c*y**2 + (b*d - 4*e)*y - (b**2*e - 4*c*e + d**2)
    print(f"  g(y) =          {sp.expand(g)}")
    expected = y**3 + y**2 + 16*y + 36
    matches_form = (sp.expand(g - expected) == 0)
    print(f"  matches y^3 + y^2 + 16y + 36: {matches_form}")

    g_factored = sp.factor(g)
    expected_factored = (y + 2) * (y**2 - y + 18)
    same_factorization = (sp.expand(g - expected_factored) == 0)
    print(f"  g factored:      {g_factored}")
    print(f"  matches (y+2)(y^2 - y + 18): {same_factorization}")

    # The irreducible quadratic factor has discriminant 1 - 72 = -71 (not a square).
    quad = y**2 - y + 18
    quad_disc = sp.Poly(quad, y).discriminant()
    print(f"  irreducible quadratic disc:  {quad_disc}  (expected -71)")
    disc_ok = (int(quad_disc) == -71)

    # Exactly one rational root in the resolvent cubic.
    rational_roots = [r for r in sp.solve(g, y) if r.is_rational]
    print(f"  resolvent rational roots:    {rational_roots}")
    one_rational = (rational_roots == [-2])

    ok = matches_form and same_factorization and disc_ok and one_rational
    print()
    print(f"  Check 3 PASS: {ok}")
    return ok


def check_galois_D4():
    hr("Check 4: Galois group is D_4 (not C_4)")
    x = sp.Symbol('x')
    f = x**4 + 4*x**3 - x**2 + 2*x - 2

    # By the standard quartic-Galois classification (Cohen 1993, sec 6.3.2):
    # with exactly one rational root in the cubic resolvent, Gal(f/Q) is
    # either C_4 or D_4. The two are distinguished by whether f remains
    # irreducible over Q(sqrt(Delta_f)) = Q(sqrt(-71)):
    #   irreducible there -> D_4,
    #   factors there     -> C_4.
    sqm71 = sp.sqrt(-71)
    f_over_Qsqrtm71 = sp.factor(f, extension=[sqm71])
    print(f"  f factored over Q(sqrt(-71)): {f_over_Qsqrtm71}")
    # The factor returns the polynomial unchanged iff f stays irreducible.
    stays_irreducible = (sp.expand(f_over_Qsqrtm71 - f) == 0) or (
        # Robust: check via factor_list count of nontrivial factors.
        len(sp.factor_list(f, extension=[sqm71])[1]) == 1
        and sp.factor_list(f, extension=[sqm71])[1][0][1] == 1
        and sp.Poly(sp.factor_list(f, extension=[sqm71])[1][0][0], x).degree() == 4
    )
    print(f"  f irreducible over Q(sqrt(-71)): {stays_irreducible}")
    print(f"  Therefore Gal(f/Q) = D_4 (not C_4): {stays_irreducible}")

    ok = stays_irreducible
    print()
    print(f"  Check 4 PASS: {ok}")
    return ok


def check_Qsqrt3_subfield():
    hr("Check 5: Q(sqrt(3)) subfield -- explicit factorization")
    x = sp.Symbol('x')
    f = x**4 + 4*x**3 - x**2 + 2*x - 2
    sq3 = sp.sqrt(3)

    # The manuscript's explicit factorization:
    #   f(x) = (x^2 + (2 + sqrt 3)x - (1 + sqrt 3)) *
    #          (x^2 + (2 - sqrt 3)x - (1 - sqrt 3)).
    g1 = x**2 + (2 + sq3)*x - (1 + sq3)
    g2 = x**2 + (2 - sq3)*x - (1 - sq3)
    product = sp.expand(g1 * g2)
    print(f"  g1(x) = {g1}")
    print(f"  g2(x) = {g2}")
    print(f"  g1 * g2 expanded = {product}")
    explicit_ok = (sp.simplify(product - f) == 0)
    print(f"  Equals f over Q(sqrt(3)):  {explicit_ok}")

    # Cross-check via sympy.factor
    f_over_Qsqrt3 = sp.factor(f, extension=[sq3])
    print(f"  sympy.factor over Q(sqrt(3)): {f_over_Qsqrt3}")
    factor_list_count = len(sp.factor_list(f, extension=[sq3])[1])
    print(f"  sympy factor count over Q(sqrt(3)): {factor_list_count}  (expected 2)")
    sympy_factors_2 = (factor_list_count == 2)

    # The two conjugate quadratic discriminants must be Galois conjugates.
    # Each is delta(g1) = (2 + sqrt 3)^2 + 4(1 + sqrt 3) = 4 + 4 sqrt 3 + 3 + 4 + 4 sqrt 3
    #                   = 11 + 8 sqrt 3,
    # and delta(g2) = 11 - 8 sqrt 3.  Norm = 11^2 - 64 * 3 = 121 - 192 = -71 (matches).
    delta_g1 = sp.expand((2 + sq3)**2 + 4*(1 + sq3))
    delta_g2 = sp.expand((2 - sq3)**2 + 4*(1 - sq3))
    norm = sp.expand(delta_g1 * delta_g2)
    print(f"  delta(g1) = {delta_g1}")
    print(f"  delta(g2) = {delta_g2}")
    print(f"  norm to Q  = {norm}  (expected -71)")
    norm_ok = (int(norm) == -71)

    ok = explicit_ok and sympy_factors_2 and norm_ok
    print()
    print(f"  Check 5 PASS: {ok}")
    return ok


def check_LMFDB_identification():
    hr("Check 6: K = LMFDB 4.2.10224.1 via Tschirnhaus x -> -x - 1")
    x = sp.Symbol('x')
    f = x**4 + 4*x**3 - x**2 + 2*x - 2

    # Tschirnhaus substitution mapping f to LMFDB's canonical defining
    # polynomial of 4.2.10224.1.
    y = sp.Symbol('y')
    f_sub = sp.expand(f.subs(x, -y - 1))
    print(f"  f(-y - 1) expanded:       {f_sub}")
    h_canonical = y**4 - 7*y**2 - 12*y - 8
    matches = (sp.expand(f_sub - h_canonical) == 0)
    print(f"  Canonical LMFDB polynomial: {h_canonical}")
    print(f"  Tschirnhaus match:          {matches}")

    # Field discriminant = -10224 = -2^4 * 3^2 * 71.
    # Polynomial discriminant = -40896 = -2^6 * 3^2 * 71.
    # Index of Z[alpha] in O_K is sqrt(disc(f) / d_K) = sqrt(40896 / 10224) = 2.
    disc_f = abs(int(sp.Poly(f, x).discriminant()))
    d_K = 10224
    index_sq = disc_f // d_K
    print(f"  |disc(f)| / |d_K| = {disc_f} / {d_K} = {index_sq}")
    index_ok = (index_sq == 4)
    print(f"  Index [O_K : Z[alpha]] = 2: {index_ok}")

    # Field discriminant prime factorization
    field_disc_factored = sp.factorint(d_K)
    print(f"  d_K factored:               {field_disc_factored}")
    field_disc_ok = (field_disc_factored == {2: 4, 3: 2, 71: 1})

    ok = matches and index_ok and field_disc_ok
    print()
    print(f"  Check 6 PASS: {ok}")
    return ok


def main():
    results = {
        "1. Irreducibility over Q":            check_irreducibility(),
        "2. Polynomial discriminant -40896":   check_discriminant(),
        "3. Cubic resolvent (y+2)(y^2-y+18)":  check_resolvent_cubic(),
        "4. Galois group D_4":                 check_galois_D4(),
        "5. Q(sqrt(3)) subfield":              check_Qsqrt3_subfield(),
        "6. LMFDB 4.2.10224.1 identification": check_LMFDB_identification(),
    }
    hr("SUMMARY")
    for k, v in results.items():
        print(f"  {('OK' if v else 'FAIL'):4s}  {k}")
    overall = all(results.values())
    print()
    print(f"Overall: {'PASS' if overall else 'FAIL'}")
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
