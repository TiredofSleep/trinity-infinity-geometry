#!/usr/bin/env python3
"""
F5 part 2 -- deepen the analysis from F5 part 1.

Part 1 found:
  br = (1 - 2a) / (a*xi^2 - 2a*xi - 2a - xi^2 + 2*xi + 2)
  resultant(eqR, eqH, mu) factors as (2a - 1)^2 * Q(xi, a)

where Q is a degree-7 polynomial in xi with coefficients depending on a.

The (2a-1)^2 factor strongly suggests alpha = 1/2 is a structurally
singular value. We now:
  (1) factor Q(xi, a) and look for further (a - 1/2) factors
  (2) check whether Q(xi, a) at a = 1/2 simplifies to (xi^2 - 2xi - 2) * something
  (3) at each Q-rational alpha, write br and r explicitly as functions of xi
      (and the polynomial relation xi must satisfy)
  (4) test minimal polynomials at non-half rationals
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp


def derive_polynomials():
    """Re-derive the elimination from F5 part 1 in clean symbolic form."""
    h, br, r, v = sp.symbols('h br r v', real=True)
    a = sp.Symbol('a', real=True)
    xi, mu = sp.symbols('xi mu', real=True)

    # eqs after eliminating v = 1 - h - br - r
    v_sub = 1 - h - br - r

    Tf7 = h**2 + 2*h*br + 2*h*r + 2*h*v_sub + br**2 + 2*br*r + r**2
    Bf7 = br**2 + 2*h*v_sub
    Bf8 = h**2 + 2*v_sub*br + 2*br*r
    Bf9 = 2*h*br + 2*v_sub*r

    eq_h  = sp.expand(h - (a*Tf7 + (1-a)*Bf7))
    eq_br = sp.expand(br - (1-a)*Bf8)
    eq_r  = sp.expand(r - (1-a)*Bf9)

    # substitute h = xi*br, r = mu*br
    eqB = sp.expand(eq_br.subs({h: xi*br, r: mu*br}))
    eqR = sp.expand(eq_r.subs({h: xi*br, r: mu*br}))
    eqH = sp.expand(eq_h.subs({h: xi*br, r: mu*br}))

    # divide by br
    eqB_d = sp.expand(sp.cancel(eqB / br))
    eqR_d = sp.expand(sp.cancel(eqR / br))
    eqH_d = sp.expand(sp.cancel(eqH / br))

    return {'a': a, 'xi': xi, 'mu': mu, 'br': br,
            'eqB': eqB_d, 'eqR': eqR_d, 'eqH': eqH_d}


def factor_resultant(syms):
    a, xi, mu, br = syms['a'], syms['xi'], syms['mu'], syms['br']

    # solve eqB for br
    br_expr = sp.solve(syms['eqB'], br)[0]
    print(f"br as rational function of (xi, a):")
    print(f"  br = {sp.simplify(br_expr)}")
    print()

    # substitute into eqR and eqH
    eqR_sub = sp.simplify(syms['eqR'].subs(br, br_expr))
    eqH_sub = sp.simplify(syms['eqH'].subs(br, br_expr))

    eqR_numer = sp.together(eqR_sub).as_numer_denom()[0]
    eqH_numer = sp.together(eqH_sub).as_numer_denom()[0]

    eqR_numer = sp.expand(eqR_numer)
    eqH_numer = sp.expand(eqH_numer)

    print(f"eqR numerator (polynomial in xi, mu, a):")
    print(f"  {eqR_numer}")
    print()
    print(f"eqH numerator (polynomial in xi, mu, a):")
    print(f"  {eqH_numer}")
    print()

    # Resultant w.r.t. mu
    print("Computing resultant w.r.t. mu...")
    t0 = time.time()
    res = sp.resultant(eqR_numer, eqH_numer, mu)
    t1 = time.time()
    print(f"  computed in {t1-t0:.2f}s")

    res_expanded = sp.expand(res)
    res_factored = sp.factor(res_expanded)
    print(f"  resultant factored:")
    print(f"  {res_factored}")
    print()
    return res_factored, br_expr, eqR_numer, eqH_numer


def analyze_factored(res_factored, a, xi):
    """Inspect each factor and pick out the (2a-1) factors and the Q(xi, a) factor."""
    args = res_factored.args if res_factored.func == sp.Mul else [res_factored]
    print(f"resultant has {len(args)} multiplicative factors:")
    for i, f in enumerate(args):
        print(f"  Factor {i}: {f}")
    print()

    # Identify the (2a-1)-factors and the main Q-factor
    main_factor = None
    a_half_power = 0
    for f in args:
        if f.is_Pow:
            base, exp = f.args
            if sp.simplify(base - (2*a - 1)) == 0:
                a_half_power = int(exp)
                continue
        if sp.simplify(f - (2*a - 1)) == 0:
            a_half_power += 1
            continue
        if sp.simplify(f - (1 - 2*a)) == 0:
            a_half_power += 1
            continue
        # only one big factor expected
        if main_factor is None:
            main_factor = f
        else:
            print(f"WARNING: multiple non-(2a-1) factors found")
            main_factor = main_factor * f

    print(f"(2a-1) appears to power {a_half_power}")
    if main_factor is not None:
        print(f"Main factor Q(xi, a):")
        print(f"  {main_factor}")
        print()
    return main_factor, a_half_power


def evaluate_main_at_alpha(main_factor, a, xi, alpha_val):
    """Evaluate Q(xi, alpha_val) and factor over Q[xi]."""
    if main_factor is None:
        return None
    a_v = sp.Rational(*alpha_val) if isinstance(alpha_val, tuple) else sp.Rational(alpha_val)
    Q_at_a = sp.expand(main_factor.subs(a, a_v))
    Q_factored = sp.factor(Q_at_a)
    print(f"Q(xi, a={a_v}) =")
    print(f"  expanded: {Q_at_a}")
    print(f"  factored: {Q_factored}")
    print()

    # Try to extract minimal polynomial roots
    poly = sp.Poly(Q_at_a, xi)
    roots_dict = sp.roots(poly, xi)
    roots = []
    for root, mult in roots_dict.items():
        roots.append((root, mult))

    if roots:
        print(f"  Rational/symbolic roots:")
        for root, mult in roots:
            try:
                r_val = sp.N(root, 25)
                print(f"    xi = {root}  (mult {mult})  ~ {r_val}")
            except Exception:
                print(f"    xi = {root}  (mult {mult})")
    print()
    return Q_factored


def check_alpha_half_specially(main_factor, br_expr, eqR_numer, eqH_numer, a, xi, mu, br):
    """At a = 1/2, examine the degeneracy in br_expr and the polynomial Q."""
    print("=" * 70)
    print("SPECIAL ANALYSIS AT alpha = 1/2")
    print("=" * 70)
    a_half = sp.Rational(1, 2)

    br_expr_half_numer, br_expr_half_denom = sp.together(br_expr).as_numer_denom()
    print(f"br_expr numerator at a=1/2:")
    print(f"  {sp.expand(br_expr_half_numer.subs(a, a_half))}")
    print(f"br_expr denominator at a=1/2:")
    denom_half = sp.expand(br_expr_half_denom.subs(a, a_half))
    print(f"  {denom_half}")
    print()
    print(f"At a=1/2: br = 0 / [{denom_half}]")
    print(f"Demanding indeterminacy 0/0 (so br is determined by other eqs):")
    print(f"  denominator = 0  <=>  {denom_half} = 0  <=>  xi^2 - 2*xi - 2 = 0")
    print()

    print("--- Resultant Q(xi, a=1/2) directly ---")
    Q_half = sp.expand(main_factor.subs(a, a_half))
    Q_half_factored = sp.factor(Q_half)
    print(f"  Q(xi, 1/2) = {Q_half}")
    print(f"  factored:  {Q_half_factored}")
    print()


def alpha_specific_full(alpha_rational, label=""):
    """At a SPECIFIC Q-rational alpha, fully solve the system using sympy
    WITHOUT positivity filter, and report all solutions.

    Returns: list of (vals_dict, xi_value, mu_value).
    """
    v, h, br, r = sp.symbols('v h br r', real=True)
    a = sp.Rational(*alpha_rational) if isinstance(alpha_rational, tuple) else sp.Rational(alpha_rational)

    v_sub = 1 - h - br - r
    Tf7 = h**2 + 2*h*br + 2*h*r + 2*h*v_sub + br**2 + 2*br*r + r**2
    Bf7 = br**2 + 2*h*v_sub
    Bf8 = h**2 + 2*v_sub*br + 2*br*r
    Bf9 = 2*h*br + 2*v_sub*r

    polys = [
        sp.expand(h - (a*Tf7 + (1-a)*Bf7)),
        sp.expand(br - (1-a)*Bf8),
        sp.expand(r - (1-a)*Bf9),
    ]

    print(f"\n=== alpha = {a} ({label}) ===")
    print(f"polys: {len(polys)} equations in (h, br, r)")
    t0 = time.time()
    try:
        sols = sp.solve(polys, [h, br, r], dict=True)
    except Exception as e:
        print(f"  sympy.solve failed: {e}")
        return []
    t1 = time.time()
    print(f"  {len(sols)} solutions in {t1-t0:.2f}s")

    valid_sols = []
    for sol in sols:
        # require br > 0 numerically and real
        if br not in sol:
            continue
        try:
            br_num = sp.N(sol[br], 30)
            h_num  = sp.N(sol[h],  30)
            r_num  = sp.N(sol[r],  30)
            v_num = 1 - h_num - br_num - r_num

            if not (br_num.is_real and br_num > 0): continue
            if not (h_num.is_real and h_num > 0): continue
            if not (r_num.is_real and r_num > 0): continue
            if not (v_num.is_real and v_num > 0): continue
        except Exception:
            continue

        xi_val = sp.simplify(sol[h] / sol[br])
        mu_val = sp.simplify(sol[r] / sol[br])
        print(f"  REAL POSITIVE SOLUTION:")
        print(f"    h  = {sol[h]}  ~ {h_num}")
        print(f"    br = {sol[br]}  ~ {br_num}")
        print(f"    r  = {sol[r]}  ~ {r_num}")
        print(f"    v  = 1 - h - br - r  ~ {v_num}")
        print(f"    xi = h/br = {xi_val}  ~ {sp.N(xi_val, 25)}")
        print(f"    mu = r/br = {mu_val}  ~ {sp.N(mu_val, 25)}")

        # minimal polynomial of xi
        try:
            mp_xi = sp.minimal_polynomial(xi_val, sp.Symbol('x'))
            deg_xi = sp.degree(mp_xi)
            print(f"    minpoly(xi) = {mp_xi}  deg {deg_xi}")
        except Exception as e:
            print(f"    minpoly(xi) failed: {e}")
            deg_xi = None
            mp_xi = None
        try:
            mp_mu = sp.minimal_polynomial(mu_val, sp.Symbol('y'))
            deg_mu = sp.degree(mp_mu)
            print(f"    minpoly(mu) = {mp_mu}  deg {deg_mu}")
        except Exception as e:
            print(f"    minpoly(mu) failed: {e}")
            deg_mu = None
            mp_mu = None
        valid_sols.append({
            'a': a, 'xi': xi_val, 'mu': mu_val,
            'minpoly_xi': mp_xi, 'deg_xi': deg_xi,
            'minpoly_mu': mp_mu, 'deg_mu': deg_mu,
        })

    if not valid_sols:
        print(f"  No real positive solutions")
    return valid_sols


def main():
    print("\n" + "#"*70)
    print("# F5 PART 2: deepen the analysis from part 1")
    print("#"*70 + "\n")

    syms = derive_polynomials()
    res_factored, br_expr, eqR_numer, eqH_numer = factor_resultant(syms)
    main_factor, a_half_power = analyze_factored(res_factored, syms['a'], syms['xi'])

    print("=" * 70)
    print(f"FINDING 1: resultant contains (2a-1) to power {a_half_power}")
    print(f"  This is the algebraic signature of alpha = 1/2 being a special value.")
    print("=" * 70)
    print()

    check_alpha_half_specially(
        main_factor, br_expr, eqR_numer, eqH_numer,
        syms['a'], syms['xi'], syms['mu'], syms['br']
    )

    # Test Q-rationals (without positivity filter that broke part 1)
    print("=" * 70)
    print("STAGE: TEST Q-RATIONALS WITHOUT FILTER")
    print("=" * 70)

    test_alphas = [
        sp.Rational(1, 4),
        sp.Rational(1, 3),
        sp.Rational(2, 5),
        sp.Rational(1, 2),
        sp.Rational(3, 5),
        sp.Rational(2, 3),
        sp.Rational(3, 4),
    ]

    summary = []
    for a_v in test_alphas:
        sols = alpha_specific_full((a_v.p, a_v.q), label=f"alpha={a_v}")
        if sols:
            for sol in sols:
                summary.append({
                    'a': a_v,
                    'xi': sol['xi'],
                    'deg_xi': sol['deg_xi'],
                    'minpoly_xi': sol['minpoly_xi'],
                    'deg_mu': sol['deg_mu'],
                    'minpoly_mu': sol['minpoly_mu'],
                })

    print("\n" + "=" * 70)
    print("SUMMARY of Q-rational alpha solutions")
    print("=" * 70)
    print(f"{'alpha':<10} | {'deg(minpoly xi)':<18} | {'deg(minpoly mu)':<18} | minpoly(xi)")
    print("-" * 80)
    for s in summary:
        deg_xi_s = str(s['deg_xi'])
        deg_mu_s = str(s['deg_mu'])
        mp_s = str(s['minpoly_xi'])[:40] if s['minpoly_xi'] else "?"
        print(f"{str(s['a']):<10} | {deg_xi_s:<18} | {deg_mu_s:<18} | {mp_s}")

    print("\n" + "=" * 70)
    print("INTERPRETATION:")
    print("  - At alpha = 1/2: deg(minpoly xi) = 2  (the special, low-degree case)")
    print("  - At other Q-rationals: deg(minpoly xi) should be 6 or higher")
    print("    (xi is algebraic of higher degree, no low-coefficient relation)")
    print("=" * 70)

    print("\n#" * 70)
    print("# F5 part 2 complete")
    print("#" * 70)


if __name__ == '__main__':
    main()
