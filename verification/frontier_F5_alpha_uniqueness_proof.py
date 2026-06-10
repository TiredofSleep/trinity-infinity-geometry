#!/usr/bin/env python3
"""
Frontier F5 -- structural proof attempt for Conjecture 4.2 (alpha-uniqueness).

Sets up the 4-core fixed-point system parametric in alpha, eliminates v, br, r
to obtain a univariate polynomial P(xi; alpha) in xi = h/br with coefficients
in Q(alpha), and computes the discriminant Delta(alpha).

Then tests Q-rational alpha-values to identify which ones (if any) admit a
genuine algebraic relation between H/Br and r/br beyond alpha = 1/2.

The system from J01 / J15 (Proposition fuse-data):

    T_fuse[0] = v^2 + 2*v*br + 2*v*r
    T_fuse[7] = h^2 + 2*h*br + 2*h*r + 2*h*v + br^2 + 2*br*r + r^2
    T_fuse[8] = 0
    T_fuse[9] = 0

    B_fuse[0] = v^2 + 2*h*r + r^2
    B_fuse[7] = br^2 + 2*h*v
    B_fuse[8] = h^2 + 2*v*br + 2*br*r
    B_fuse[9] = 2*h*br + 2*v*r

Fixed-point (polynomial, with v + h + br + r = 1):
    v  = alpha * T_fuse[0] + (1-alpha) * B_fuse[0]
    h  = alpha * T_fuse[7] + (1-alpha) * B_fuse[7]
    br = (1-alpha) * B_fuse[8]                       (since T_fuse[8] = 0)
    r  = (1-alpha) * B_fuse[9]                       (since T_fuse[9] = 0)

Reproduce: python verification/frontier_F5_alpha_uniqueness_proof.py
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp


def build_system():
    """Return (vars, eqs) for the 4-core fixed-point system parametric in alpha."""
    v, h, br, r, a = sp.symbols('v h br r a', positive=True)

    # T-fuse on 4-core (from J01 manuscript verification, J15 prop fuse-data)
    Tf0 = v**2 + 2*v*br + 2*v*r
    Tf7 = h**2 + 2*h*br + 2*h*r + 2*h*v + br**2 + 2*br*r + r**2
    Tf8 = sp.Integer(0)
    Tf9 = sp.Integer(0)

    # B-fuse on 4-core
    Bf0 = v**2 + 2*h*r + r**2
    Bf7 = br**2 + 2*h*v
    Bf8 = h**2 + 2*v*br + 2*br*r
    Bf9 = 2*h*br + 2*v*r

    # Fixed-point equations (with Z_T = Z_B = (v+h+br+r)^2 = 1):
    eq_v  = sp.Eq(v,  a*Tf0 + (1-a)*Bf0)
    eq_h  = sp.Eq(h,  a*Tf7 + (1-a)*Bf7)
    eq_br = sp.Eq(br, a*Tf8 + (1-a)*Bf8)
    eq_r  = sp.Eq(r,  a*Tf9 + (1-a)*Bf9)
    eq_unit = sp.Eq(v + h + br + r, 1)

    return (v, h, br, r, a), (eq_v, eq_h, eq_br, eq_r, eq_unit)


def print_system(vars_, eqs):
    v, h, br, r, a = vars_
    print("=" * 70)
    print("Fixed-point system parametric in alpha (variables: v, h, br, r)")
    print("Unit-mass constraint v + h + br + r = 1")
    print("=" * 70)
    for eq in eqs:
        print(f"  {sp.simplify(eq.lhs - eq.rhs)} = 0")
    print()


def reduce_to_xi_polynomial(vars_, eqs):
    """Eliminate v, h, br, r (modulo their fixed-point eqs and unit-mass)
    via Groebner basis at general alpha to find a polynomial relation
    among (xi = h/br, mu = r/br, alpha).

    Strategy: rewrite as polynomial system in (v, h, br, r) with parameter a,
    homogenize by introducing xi = h/br and mu = r/br as new ratio variables,
    then eliminate v, h, br, r.
    """
    v, h, br, r, a = vars_

    # Move to polynomial form -- each eq becomes lhs - rhs = 0
    polys = [sp.expand(eq.lhs - eq.rhs) for eq in eqs]

    print("Polynomial form (= 0):")
    for p in polys:
        print(f"  {p}")
    print()
    return polys


def attempt_groebner(polys, vars_, elim_vars, order='lex'):
    """Attempt to compute a Groebner basis with elimination order."""
    print(f"--- Groebner basis attempt: eliminate {[str(x) for x in elim_vars]} ---")
    G = sp.groebner(polys, *vars_[:4], a := vars_[4], order=order)
    print(f"  Basis has {len(G)} elements:")
    for g in G:
        deg = sp.Poly(g, *vars_[:4]).total_degree() if g != 0 else 0
        print(f"    deg {deg}: {g}")
    return G


def alpha_specific_solve(alpha_val, label=""):
    """At a SPECIFIC alpha value, solve the polynomial system exactly with sympy.
    Returns dict of solutions (positive orthant filter)."""
    v, h, br, r = sp.symbols('v h br r', positive=True)

    # T-fuse / B-fuse at general (v, h, br, r)
    Tf0 = v**2 + 2*v*br + 2*v*r
    Tf7 = h**2 + 2*h*br + 2*h*r + 2*h*v + br**2 + 2*br*r + r**2
    Bf0 = v**2 + 2*h*r + r**2
    Bf7 = br**2 + 2*h*v
    Bf8 = h**2 + 2*v*br + 2*br*r
    Bf9 = 2*h*br + 2*v*r

    a = sp.Rational(*alpha_val) if isinstance(alpha_val, tuple) else sp.Rational(alpha_val)
    eqs = [
        sp.Eq(v,  a*Tf0 + (1-a)*Bf0),
        sp.Eq(h,  a*Tf7 + (1-a)*Bf7),
        sp.Eq(br, (1-a)*Bf8),
        sp.Eq(r,  (1-a)*Bf9),
        sp.Eq(v + h + br + r, 1),
    ]

    print(f"\n=== alpha = {a} ({label}) ===")
    # try solve with positive constraint
    try:
        sols = sp.solve(eqs, [v, h, br, r], dict=True, positive=True)
    except Exception as e:
        print(f"  sympy.solve failed: {e}")
        return None

    real_pos = []
    for s in sols:
        vals = {k: sp.simplify(val) for k, val in s.items()}
        # filter for real positive
        try:
            all_pos = all(sp.simplify(val).is_real for val in vals.values())
            all_real_finite = all(
                sp.N(val, 50) > 0 for val in vals.values()
            )
            if all_pos and all_real_finite:
                real_pos.append(vals)
        except Exception:
            pass

    if not real_pos:
        print(f"  No real positive solutions found among {len(sols)} solutions")
        return None

    for sol in real_pos:
        print(f"  Solution:")
        for var, val in sol.items():
            num = sp.N(val, 25)
            print(f"    {var} = {val}  ~ {num}")
        # report ratios
        xi = sp.simplify(sol[h] / sol[br])
        mu = sp.simplify(sol[r] / sol[br])
        print(f"    xi = h/br = {xi}  ~ {sp.N(xi, 25)}")
        print(f"    mu = r/br = {mu}  ~ {sp.N(mu, 25)}")

        # Check whether xi is algebraic of low degree over Q
        try:
            minp_xi = sp.minimal_polynomial(xi, sp.Symbol('x'))
            print(f"    minimal_polynomial(xi) = {minp_xi}  deg {sp.degree(minp_xi)}")
        except Exception as e:
            print(f"    minimal_polynomial(xi) failed: {e}")

        try:
            minp_mu = sp.minimal_polynomial(mu, sp.Symbol('y'))
            print(f"    minimal_polynomial(mu) = {minp_mu}  deg {sp.degree(minp_mu)}")
        except Exception as e:
            print(f"    minimal_polynomial(mu) failed: {e}")

    return real_pos


def reduce_at_general_alpha(timeout_seconds=60):
    """Attempt to derive a single-variable polynomial in xi = h/br with
    coefficients in Q(alpha) by elimination.

    Approach:
    1. Use the structural fact T_fuse[8] = T_fuse[9] = 0, so:
         br = (1-a) * B_fuse[8]
         r  = (1-a) * B_fuse[9]
    2. Use v = 1 - h - br - r (from unit mass) to eliminate v.
    3. Substitute these into eq_h to obtain a polynomial in (h, br, r, a).
    4. Substitute xi := h / br, mu := r / br to homogenize; use br as remaining var.
    """
    h, br, r, a = sp.symbols('h br r a', positive=False)
    xi, mu = sp.symbols('xi mu', positive=False)

    # v = 1 - h - br - r (unit mass)
    v = 1 - h - br - r

    # T-fuse[8] = T-fuse[9] = 0 ==> br and r eqs become:
    Bf8 = h**2 + 2*v*br + 2*br*r
    Bf9 = 2*h*br + 2*v*r

    eq_br = br - (1 - a) * Bf8
    eq_r  = r  - (1 - a) * Bf9

    # T-fuse and B-fuse for h-coordinate
    Tf7 = h**2 + 2*h*br + 2*h*r + 2*h*v + br**2 + 2*br*r + r**2
    Bf7 = br**2 + 2*h*v
    eq_h = h - (a*Tf7 + (1-a)*Bf7)

    print("--- Three eqs (in h, br, r, a) after eliminating v=1-h-br-r ---")
    print(f"  eq_h  = {sp.expand(eq_h)}")
    print(f"  eq_br = {sp.expand(eq_br)}")
    print(f"  eq_r  = {sp.expand(eq_r)}")
    print()

    # Substitute h = xi * br, r = mu * br (br factored out, so set br * dummy)
    # Each equation becomes polynomial in (br, xi, mu, a). Then check the
    # br-degree distribution.

    # Substitute h -> xi*br, r -> mu*br in eq_br:
    eqB = sp.expand(eq_br.subs({h: xi*br, r: mu*br}))
    eqR = sp.expand(eq_r.subs({h: xi*br, r: mu*br}))
    eqH = sp.expand(eq_h.subs({h: xi*br, r: mu*br}))

    print("--- After substituting h = xi*br, r = mu*br ---")
    print(f"  eqB := br * (...) = 0:")
    print(f"    eqB = {eqB}")
    print()
    print(f"  eqR := br * (...) = 0:")
    print(f"    eqR = {eqR}")
    print()
    print(f"  eqH := br * (...) = 0:")
    print(f"    eqH = {eqH}")
    print()

    # Divide eqB by br (it should factor out, since each term in Bf8 is
    # quadratic in {h, br, r, v} where v = 1 - ...):
    # Specifically br = (1-a) * (h^2 + 2*v*br + 2*br*r)
    # After h = xi*br, r = mu*br: br = (1-a) * (xi^2*br^2 + 2*v*br + 2*br*(mu*br))
    #                                = (1-a) * br * (xi^2*br + 2*v + 2*mu*br)
    # So 1 = (1-a) * (xi^2*br + 2*v + 2*mu*br) [dividing by br]
    # 1 = (1-a) * (xi^2*br + 2*(1 - xi*br - br - mu*br) + 2*mu*br)
    # 1 = (1-a) * (xi^2*br + 2 - 2*xi*br - 2*br - 2*mu*br + 2*mu*br)
    # 1 = (1-a) * (xi^2*br + 2 - 2*xi*br - 2*br)
    # 1 = (1-a) * (br*(xi^2 - 2*xi - 2) + 2)

    eqB_div = sp.cancel(eqB / br)
    eqR_div = sp.cancel(eqR / br)
    print("--- After dividing eqB by br ---")
    print(f"  eqB/br = {sp.expand(eqB_div)}")
    print()
    print("--- After dividing eqR by br ---")
    print(f"  eqR/br = {sp.expand(eqR_div)}")
    print()

    # Solve eqB_div = 0 for br in terms of xi, mu, a -- linear in br!
    print("--- Solving (eqB)/br = 0 for br as function of (xi, mu, a) ---")
    br_sol = sp.solve(eqB_div, br)
    print(f"  br = {br_sol}")
    print()
    if not br_sol:
        print("  No solution; abort")
        return None
    br_expr = br_sol[0]
    br_expr_simplified = sp.simplify(br_expr)
    print(f"  br_simplified = {br_expr_simplified}")
    print()

    # Now substitute br into eqR/br = 0 and eqH/br (need to divide eqH by br too)
    eqH_div = sp.cancel(eqH / br)
    print("--- After dividing eqH by br ---")
    print(f"  eqH/br = {sp.expand(eqH_div)}")
    print()

    print("--- Substituting br = {} into eqR/br ---".format(br_expr_simplified))
    eqR_sub = sp.simplify(eqR_div.subs(br, br_expr_simplified))
    print(f"  eqR_sub = {eqR_sub}")
    print()

    print("--- Substituting br = {} into eqH/br ---".format(br_expr_simplified))
    eqH_sub = sp.simplify(eqH_div.subs(br, br_expr_simplified))
    print(f"  eqH_sub = {eqH_sub}")
    print()

    # Now eqR_sub and eqH_sub are polynomial relations in (xi, mu, a)
    # Multiply through to clear denominators
    eqR_num = sp.together(eqR_sub).as_numer_denom()
    eqH_num = sp.together(eqH_sub).as_numer_denom()
    print("--- Numerators (polynomial in xi, mu, a) ---")
    print(f"  eqR_numer = {sp.expand(eqR_num[0])}")
    print(f"  eqH_numer = {sp.expand(eqH_num[0])}")
    print()
    print(f"  eqR_denom = {eqR_num[1]}")
    print(f"  eqH_denom = {eqH_num[1]}")
    print()

    return {
        'xi': xi, 'mu': mu, 'a': a,
        'br_expr': br_expr_simplified,
        'eqR_numer': sp.expand(eqR_num[0]),
        'eqH_numer': sp.expand(eqH_num[0]),
    }


def resultant_mu(elim_result):
    """Compute the resultant of eqR_numer and eqH_numer with respect to mu,
    obtaining a polynomial in (xi, a)."""
    xi = elim_result['xi']
    mu = elim_result['mu']
    a  = elim_result['a']

    eqR = elim_result['eqR_numer']
    eqH = elim_result['eqH_numer']

    print("--- Resultant w.r.t. mu (eliminating mu, leaving xi, a) ---")
    t0 = time.time()
    res = sp.resultant(eqR, eqH, mu)
    t1 = time.time()
    res_expanded = sp.expand(res)
    res_factored = sp.factor(res_expanded)
    print(f"  Computed in {t1-t0:.2f}s")
    print(f"  resultant (expanded) ~ deg {sp.Poly(res_expanded, xi, a).total_degree()}")
    print()
    print(f"  factored: {res_factored}")
    print()
    return res_factored


def test_q_rationals(alpha_rationals):
    """For each rational alpha in the list, attempt exact symbolic solve and
    report (xi, mu) algebraic data."""
    results = {}
    for alpha in alpha_rationals:
        try:
            res = alpha_specific_solve(alpha, label=f"{alpha}")
            results[str(alpha)] = res
        except Exception as e:
            print(f"  FAILED for alpha={alpha}: {e}")
            results[str(alpha)] = None
    return results


def main():
    print("\n" + "#"*70)
    print("# F5 -- structural proof attempt for Conjecture 4.2")
    print("#"*70)
    print()

    # Step 1: print the parametric system
    vars_, eqs = build_system()
    print_system(vars_, eqs)
    polys = reduce_to_xi_polynomial(vars_, eqs)
    print()

    # Step 2: do the elimination by hand using the structural fact
    print("\n" + "#"*70)
    print("# STAGE 1: Reduction at general alpha")
    print("#"*70)
    print()
    elim = reduce_at_general_alpha()
    if elim is None:
        print("Elimination failed -- abort")
        return

    # Step 3: compute resultant w.r.t. mu
    print("\n" + "#"*70)
    print("# STAGE 2: Resultant eliminating mu, leaving polynomial in (xi, alpha)")
    print("#"*70)
    print()
    res_factored = resultant_mu(elim)

    # Step 4: At each Q-rational alpha, test for algebraic relations
    print("\n" + "#"*70)
    print("# STAGE 3: Q-rational alpha test for algebraic relations")
    print("#"*70)

    test_alphas = [
        sp.Rational(1, 4),
        sp.Rational(1, 3),
        sp.Rational(2, 5),
        sp.Rational(1, 2),
        sp.Rational(3, 5),
        sp.Rational(2, 3),
        sp.Rational(3, 4),
    ]
    rational_results = {}
    for a_val in test_alphas:
        try:
            res = alpha_specific_solve((a_val.p, a_val.q), label=f"alpha={a_val}")
            rational_results[str(a_val)] = res
        except Exception as e:
            print(f"\n=== alpha = {a_val} === FAILED: {e}")
            rational_results[str(a_val)] = None

    print("\n" + "#"*70)
    print("# F5 complete")
    print("#"*70)


if __name__ == '__main__':
    main()
