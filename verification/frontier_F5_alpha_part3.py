#!/usr/bin/env python3
"""
F5 part 3 -- per-alpha minimal polynomial check via Q(xi, a) substitution.

We have:
  br = (1 - 2a) / D(xi, a)   where D(xi, a) = a*xi^2 - 2a*xi - 2a - xi^2 + 2*xi + 2
  resultant(eqR, eqH, mu) = (2a-1)^2 * Q(xi, a)

where Q(xi, a) is a polynomial in xi of degree 7 (and degree 4 in a).

The polynomial xi satisfies for the attractor is EITHER:
  (A) at a = 1/2: D(xi, 1/2) = -1/2 (xi^2 - 2xi - 2) = 0
      AND the br numerator (1 - 2a) = 0, jointly indeterminate
      so the constraint xi^2 - 2xi - 2 = 0 comes from D = 0 alone
  (B) at general a: Q(xi, a) = 0, which is degree 7 in xi
      with coefficients in Q[a]

At each Q-rational a != 1/2, Q(xi, a) restricted to xi positive real gives the
minimal polynomial of xi over Q (after factoring out spurious branches).

We:
  1) Substitute each Q-rational alpha into Q(xi, a)
  2) Factor over Q[xi]
  3) Find the real positive root of Q (= the attractor xi-value)
  4) Confirm that root has minpoly of degree >= 3 (NOT a low-deg algebraic relation)
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp
import mpmath as mp

# The polynomials from F5 part 1/2
a = sp.Symbol('a', real=True)
xi = sp.Symbol('xi', real=True)
mu = sp.Symbol('mu', real=True)

# Q-factor (degree-7 in xi, deg-4 in a)
Q = (
    4*a**4*xi**6 - 8*a**4*xi**5 - 16*a**4*xi**4 + 16*a**4*xi**3
    + 16*a**4*xi**2 - 64*a**4*xi
    - 2*a**3*xi**7 + 28*a**3*xi**5 - 12*a**3*xi**4 - 16*a**3*xi**3
    + 32*a**3*xi**2 + 160*a**3*xi
    + 3*a**2*xi**7 - 13*a**2*xi**6 - 12*a**2*xi**5 + 64*a**2*xi**4
    - 84*a**2*xi**3 - 108*a**2*xi**2 - 144*a**2*xi + 16*a**2
    - a*xi**7 + 8*a*xi**6 - 8*a*xi**5 - 27*a*xi**4 + 100*a*xi**3
    + 52*a*xi**2 + 40*a*xi - 16*a
    - 20*xi**3 + 4
)

# br rational function from the linear-in-br equation:
br_expr = (1 - 2*a) / (a*xi**2 - 2*a*xi - 2*a - xi**2 + 2*xi + 2)

print("=" * 70)
print("F5 part 3: minimal polynomial of xi at each Q-rational alpha")
print("=" * 70)
print()
print("Q(xi, a) [degree 7 in xi, 4 in a]:")
print(f"  Q = {Q}")
print()

# At each alpha, evaluate Q and factor
def numerical_attractor(alpha_rational, dps=80):
    """Iterate the 4-core fixed-point to high precision and read off xi, mu."""
    mp.mp.dps = dps
    a_val = mp.mpf(alpha_rational.p) / mp.mpf(alpha_rational.q)

    p = [mp.mpf(0)] * 10
    for c in [0, 7, 8, 9]:
        p[c] = mp.mpf(1) / 4
    one_minus_a = 1 - a_val

    # Import the tables
    sys.path.insert(0, '/c/Users/brayd/OneDrive/Desktop/trinity-infinity-geometry')
    try:
        from ck_tables import TSML, BHML
    except ImportError as e:
        print(f"  Cannot import ck_tables: {e}")
        return None

    def fuse(table, p):
        out = [mp.mpf(0)] * 10
        for i in range(10):
            if p[i] == 0:
                continue
            pi = p[i]
            for j in range(10):
                if p[j] == 0:
                    continue
                out[table[i][j]] += pi * p[j]
        return out

    n = 0
    for n in range(2000):
        Tf = fuse(TSML, p)
        Bf = fuse(BHML, p)
        out = [a_val * Tf[c] + one_minus_a * Bf[c] for c in range(10)]
        s = sum(out)
        new_p = [x / s for x in out]
        delta = max(abs(p[c] - new_p[c]) for c in range(10))
        if delta < mp.mpf(10) ** -(dps - 5):
            p = new_p
            break
        p = new_p

    h_val = p[7]
    br_val = p[8]
    r_val = p[9]
    v_val = p[0]
    if br_val == 0:
        return None
    return {'h': h_val, 'br': br_val, 'r': r_val, 'v': v_val,
            'xi': h_val / br_val, 'mu': r_val / br_val,
            'iters': n, 'dps': dps}


def factor_Q_at_alpha(alpha_rational):
    """Substitute alpha into Q(xi, a), factor over Q[xi], identify the real positive root."""
    a_v = alpha_rational if isinstance(alpha_rational, sp.Rational) else sp.Rational(alpha_rational)
    Qa = sp.expand(Q.subs(a, a_v))
    Qa_factored = sp.factor(Qa)
    print(f"--- alpha = {a_v} ---")
    print(f"  Q(xi, {a_v}) = {Qa}")
    print(f"  factored:    {Qa_factored}")

    # Get xi-polynomial in standard form
    p_xi = sp.Poly(Qa, xi)
    print(f"  degree in xi: {p_xi.total_degree()}")

    # Numerical root finding
    numerical = numerical_attractor(a_v)
    if numerical is None:
        print(f"  iteration did not converge")
        return None

    xi_num = numerical['xi']
    mu_num = numerical['mu']
    print(f"  numerical xi (attractor) = {mp.nstr(xi_num, 35)}")
    print(f"  numerical mu (attractor) = {mp.nstr(mu_num, 35)}")

    # Plug numerical xi into Qa to verify it's actually a root
    Qa_xi = float(Qa.subs(xi, sp.Float(str(xi_num), 60)))
    print(f"  Q(xi_num, {a_v}) = {Qa_xi:.6e}  (should be ~ 0)")

    # PSLQ check on numerical xi: find minpoly over Q of low degree
    mp.mp.dps = 60
    found_minpoly = None
    for deg in range(1, 9):
        basis = [xi_num**k for k in range(deg + 1)]
        try:
            rel = mp.pslq(basis, tol=mp.mpf(10)**-50, maxcoeff=10**8)
        except Exception:
            rel = None
        if rel:
            # Check whether this is genuine (not a spurious "rational root near x")
            coeffs = list(rel)
            poly_test = sum(coeffs[k] * sp.Symbol('x')**k for k in range(deg + 1))
            poly_test = sp.Poly(poly_test, sp.Symbol('x'))
            # The polynomial must have xi_num as a root to high precision
            val_at = poly_test.eval(float(xi_num))
            if abs(val_at) > 1e-30:
                continue
            # Check if irreducible
            factored = sp.factor(poly_test.as_expr())
            if factored.is_Mul:
                # Find the factor that has xi_num as a root
                for f in factored.args:
                    if hasattr(f, 'is_Pow'):
                        base = f.base if f.is_Pow else f
                        try:
                            r_test = sp.Poly(base, sp.Symbol('x')).eval(float(xi_num))
                            if abs(r_test) < 1e-30:
                                found_minpoly = base
                                break
                        except Exception:
                            pass
            else:
                found_minpoly = poly_test.as_expr()
            if found_minpoly:
                break

    if found_minpoly:
        print(f"  PSLQ minpoly(xi) at deg <= {deg}: {found_minpoly}")
    else:
        print(f"  No PSLQ relation up to degree 8 found at coefficient bound 10^8")

    return {'alpha': a_v, 'Qa_factored': Qa_factored, 'xi_num': xi_num,
            'minpoly_pslq': found_minpoly}


def main():
    print("\n#" * 70)
    print("# F5 part 3: minimal polynomial of xi at each Q-rational alpha")
    print("#" * 70)
    print()

    rational_alphas = [
        sp.Rational(1, 4),
        sp.Rational(1, 3),
        sp.Rational(2, 5),
        sp.Rational(1, 2),
        sp.Rational(3, 5),
        sp.Rational(2, 3),
        sp.Rational(3, 4),
        sp.Rational(1, 5),
        sp.Rational(4, 5),
        sp.Rational(1, 7),
        sp.Rational(2, 7),
        sp.Rational(3, 7),
        sp.Rational(4, 7),
        sp.Rational(5, 7),
        sp.Rational(6, 7),
    ]

    summary = []
    for a_v in rational_alphas:
        res = factor_Q_at_alpha(a_v)
        if res:
            summary.append(res)
        print()

    print("\n" + "=" * 75)
    print("F5 PART 3 SUMMARY")
    print("=" * 75)
    print(f"{'alpha':<8} | {'Q(xi, a) factored over Q[xi]':<50}")
    print("-" * 75)
    for s in summary:
        a_s = str(s['alpha'])
        f_s = str(s['Qa_factored'])[:50]
        print(f"{a_s:<8} | {f_s}")
    print()

    # The key check: does any non-half alpha admit a degree-2 (or low) factor?
    print("Key check: any alpha != 1/2 with a low-degree (xi^2 + ... ) factor?")
    for s in summary:
        if s['alpha'] == sp.Rational(1, 2):
            continue
        if s['minpoly_pslq'] is not None:
            mp_str = str(s['minpoly_pslq'])
            deg_mp = sp.degree(s['minpoly_pslq'], sp.Symbol('x'))
            print(f"  alpha = {s['alpha']}: PSLQ found minpoly of degree {deg_mp}: {mp_str}")

    print("\n#" * 70)
    print("# F5 part 3 complete")
    print("#" * 70)


if __name__ == '__main__':
    main()
