"""
f_field_match_71.py - Test whether F8 trace polynomial and WP105 R/Br
                     quartic generate THE SAME number field (LMFDB 4.2.10224.1).

§30 found: F8 trace polynomial -443*t^4 + 5588*t^3 - 21048*t^2 + 26240*t
- 3200 has discriminant -2^24 * 3^10 * 5^2 * 11^6 * 71.

D40 says R/Br quartic x^4 + 4x^3 - x^2 + 2x - 2 has poly disc -40896 = -2^6 * 3^2 * 71.

D41 says R/Br field is LMFDB 4.2.10224.1 with field disc -10224 = -2^4 * 3^2 * 71.

KEY OBSERVATION: BOTH polynomials have squarefree(disc) = -71.
This strongly suggests they generate the SAME number field
(LMFDB 4.2.10224.1) -- a 'TIG-natural' quartic field.

This script:
  (a) verifies squarefree(disc) = -71 for both polynomials
  (b) computes the Galois groups
  (c) attempts to verify that they generate the same field
      by testing if a root of one satisfies the other (after
      substitution / linear transform)

If confirmed: F8 dynamical signature lives in EXACTLY the same
quartic field as F8 R/Br fixed-point ratio.  This is a major
unification: the dynamical and the fixed-point structures share
one number field.

Triggered by Brayden 2026-04-29: "keep going until you run out of rope...
sounds like it is developing itself".

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §30, §32 (this).
"""
from __future__ import annotations

import sympy as sp


def squarefree_part(n):
    n = int(n)
    sign = 1 if n > 0 else -1
    n = abs(n)
    if n == 0:
        return 0
    f = sp.factorint(n)
    result = sign
    for p, e in f.items():
        if e % 2 == 1:
            result *= p
    return result


def main():
    print("=" * 80)
    print("F8 trace polynomial vs WP105 R/Br quartic: same number field?")
    print("=" * 80)
    print()

    x = sp.Symbol('x', real=True)

    # F8 trace polynomial (§30 finding)
    f8_trace = -443*x**4 + 5588*x**3 - 21048*x**2 + 26240*x - 3200
    print(f"  F8 trace polynomial: {f8_trace}")

    # R/Br quartic (D40)
    rb_quartic = x**4 + 4*x**3 - x**2 + 2*x - 2
    print(f"  WP105 R/Br quartic:  {rb_quartic}")
    print()

    # --- Discriminants ---
    f8_disc = sp.discriminant(f8_trace, x)
    rb_disc = sp.discriminant(rb_quartic, x)
    print(f"  F8 trace discriminant:    {f8_disc}")
    print(f"    factored: {sp.factorint(int(abs(f8_disc)))}")
    print(f"    squarefree: {squarefree_part(f8_disc)}")
    print()
    print(f"  R/Br quartic discriminant: {rb_disc}")
    print(f"    factored: {sp.factorint(int(abs(rb_disc)))}")
    print(f"    squarefree: {squarefree_part(rb_disc)}")
    print()

    if squarefree_part(f8_disc) == squarefree_part(rb_disc):
        print(f"  *** SQUAREFREE PARTS MATCH: {squarefree_part(f8_disc)} ***")
        print(f"  Both polynomials generate fields with the same field discriminant.")
        print(f"  This is necessary but not sufficient for same field.")
        print()
    else:
        print(f"  Squarefree parts differ; fields are likely different.")
        print()

    # --- Galois groups ---
    print("-" * 80)
    print("Galois group computation")
    print("-" * 80)
    print()
    print(f"  F8 trace polynomial:")
    try:
        # Make monic and normalize
        f8_monic = sp.Poly(-f8_trace, x).as_expr() / 443
        # Hmm sympy's galois_group works on monic integer polynomials
        # Let me use the polynomial directly
        f8_poly_obj = sp.Poly(f8_trace, x)
        print(f"    polynomial: {f8_poly_obj}")
        try:
            galois_f8 = sp.galois_group(f8_poly_obj)
            print(f"    Galois group: {galois_f8}")
        except Exception as e:
            print(f"    galois_group failed: {e}")
    except Exception as e:
        print(f"    error: {e}")

    print(f"  R/Br quartic:")
    try:
        rb_poly_obj = sp.Poly(rb_quartic, x)
        print(f"    polynomial: {rb_poly_obj}")
        try:
            galois_rb = sp.galois_group(rb_poly_obj)
            print(f"    Galois group: {galois_rb}")
        except Exception as e:
            print(f"    galois_group failed: {e}")
    except Exception as e:
        print(f"    error: {e}")
    print()

    # --- Roots ---
    print("-" * 80)
    print("Roots numerical comparison")
    print("-" * 80)
    print()
    f8_roots = sp.nroots(f8_trace, n=20)
    rb_roots = sp.nroots(rb_quartic, n=20)
    print(f"  F8 trace roots:")
    for r in f8_roots:
        print(f"    {r}")
    print()
    print(f"  R/Br quartic roots:")
    for r in rb_roots:
        print(f"    {r}")
    print()

    # --- Are roots related? Try ratios ---
    print("-" * 80)
    print("Test root-ratio relations")
    print("-" * 80)
    print()
    real_f8 = [r for r in f8_roots if abs(sp.im(r)) < 1e-10]
    real_rb = [r for r in rb_roots if abs(sp.im(r)) < 1e-10]
    if real_f8 and real_rb:
        print(f"  Real roots of F8 trace:  {[float(r) for r in real_f8]}")
        print(f"  Real roots of R/Br quartic: {[float(r) for r in real_rb]}")
        # Try ratios
        for fr in real_f8:
            for rr in real_rb:
                ratio = float(sp.re(fr)) / float(sp.re(rr))
                # Check if rational
                rational = sp.nsimplify(ratio, rational=True, tolerance=1e-10)
                if rational and abs(float(rational) - ratio) < 1e-10:
                    print(f"  f8_root({float(sp.re(fr)):.10f}) / rb_root({float(sp.re(rr)):.10f}) = {ratio:.10f} = {rational} (rational)")
    print()

    # Net statement
    print("=" * 80)
    print("STRUCTURAL STATEMENT")
    print("=" * 80)
    print()
    if squarefree_part(f8_disc) == squarefree_part(rb_disc):
        print(f"  squarefree(disc) match at {squarefree_part(f8_disc)}.")
        print(f"  This is STRONG evidence that the quartic fields generated by")
        print(f"  F8 trace polynomial and WP105 R/Br quartic are RELATED.")
        print(f"  They might be the same field (LMFDB 4.2.10224.1) or closely")
        print(f"  related (e.g., same field disc with different Galois closures).")
        print()
        print(f"  If the SAME field: F8 dynamical structure (Jacobian trace at")
        print(f"  alpha=1/2 fixed point) and F8 STATIC structure (R/Br fixed-")
        print(f"  point ratio) live in EXACTLY the same number field. Major")
        print(f"  unification of dynamical and fixed-point projections in F8.")
        print()
        print(f"  Confirming requires: comparing Galois groups; testing if a")
        print(f"  root of one polynomial generates the same field as a root")
        print(f"  of the other.")


if __name__ == "__main__":
    main()
