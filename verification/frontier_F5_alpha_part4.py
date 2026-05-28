#!/usr/bin/env python3
"""
F5 part 4 -- compute the discriminant of Q(xi, a) as a polynomial in a.

Q(xi, a) is the load-bearing factor of the (eqR, eqH) resultant w.r.t. mu,
after dividing out the (2a-1)^2 factor. It has degree 7 in xi and degree 4
in a.

The discriminant disc_xi(Q) is a polynomial in a alone. Its rational roots
give the alpha-values where Q has a repeated root in xi -- i.e., the
candidate alpha values where the structural degeneracy occurs.

At alpha = 1/2: Q factors as xi^2 * (xi^2 - 2xi - 2)^2. The (xi^2 - 2xi - 2)
piece is squared, hence the discriminant must vanish at a = 1/2.

We compute disc_xi(Q) and identify its rational roots.
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp

a = sp.Symbol('a', real=True)
xi = sp.Symbol('xi', real=True)

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

print("=" * 70)
print("F5 part 4: discriminant of Q(xi, a) as a polynomial in a")
print("=" * 70)
print()

Q_poly = sp.Poly(Q, xi)
print(f"Q viewed as polynomial in xi: deg = {Q_poly.total_degree()}")
print(f"Q leading coeff in xi: {Q_poly.LC()}")
print()

print("Computing disc_xi(Q)...")
t0 = time.time()
disc = sp.discriminant(Q, xi)
t1 = time.time()
print(f"  computed in {t1-t0:.2f}s")
print()

disc_expanded = sp.expand(disc)
print(f"disc_xi(Q) viewed as polynomial in a: deg = {sp.degree(disc_expanded, a)}")
print()

print("disc_xi(Q) factored:")
t0 = time.time()
disc_factored = sp.factor(disc_expanded)
t1 = time.time()
print(f"  computed in {t1-t0:.2f}s")
print(f"  {disc_factored}")
print()

# Extract the Q-rational roots of disc(Q) = 0 in a
print("Identifying rational roots in a:")
# disc is polynomial in a, factor first
factors = sp.factor_list(disc_expanded)
print(f"Factor list: leading={factors[0]}")
for f, mult in factors[1]:
    f_poly = sp.Poly(f, a)
    print(f"  Factor: {f}  multiplicity {mult}  deg_a = {f_poly.total_degree()}")
    if f_poly.total_degree() == 1:
        # rational root
        root = sp.solve(f, a)
        if root:
            print(f"    --> linear factor, root: a = {root[0]}")
print()

# Print explicit rational roots
print("=" * 70)
print("RATIONAL ROOTS of disc_xi(Q) = 0 in a:")
print("=" * 70)
all_roots = sp.roots(disc_expanded, a)
rational_roots = []
for r, m in all_roots.items():
    is_rat = r.is_rational if hasattr(r, 'is_rational') else False
    if is_rat:
        rational_roots.append((r, m))
        print(f"  a = {r}  (mult {m})")

if not rational_roots:
    print("  No rational roots found")
print()

# Test the conjecture: a = 1/2 should be among them
half = sp.Rational(1, 2)
print(f"Confirming a = 1/2 is a root: disc(Q)|_{{a=1/2}} =")
t0 = time.time()
disc_at_half = sp.expand(disc.subs(a, half))
t1 = time.time()
print(f"  {disc_at_half}  (computed in {t1-t0:.2f}s)")
print()


# Re-do discriminant in unexpanded form first to be sure
print("=" * 70)
print("Sanity check: explicitly evaluate Q at all rational roots and factor")
print("=" * 70)

def factor_Q_at(a_val):
    print(f"\n  a = {a_val}:")
    Qa = sp.expand(Q.subs(a, a_val))
    Qa_f = sp.factor(Qa)
    print(f"    factored: {Qa_f}")
    # Test if there are repeated factors
    sqfree = sp.sqf(Qa)
    sqfree_factored = sp.factor(sqfree)
    print(f"    square-free part factored: {sqfree_factored}")
    same = sp.simplify(Qa - sqfree) == 0
    print(f"    is square-free: {same}")
    return Qa_f


# Test some special values to see if Q has repeated roots
test_special = [sp.Rational(1, 2), sp.Integer(0), sp.Integer(1)]
for a_v in test_special:
    factor_Q_at(a_v)


# Also examine the "main" non-trivial factor of disc(Q) -- if there's a
# higher-degree irreducible factor, factor it and look for low-degree pieces
print("\n" + "=" * 70)
print("Examining all factors of disc_xi(Q)")
print("=" * 70)
for f, mult in factors[1]:
    f_poly = sp.Poly(f, a)
    deg = f_poly.total_degree()
    if deg >= 2:
        # higher-degree factor
        print(f"\n  Factor of deg {deg} (mult {mult}):")
        print(f"    {f}")
        # Find roots
        try:
            roots_f = sp.roots(f, a)
            for r, m in roots_f.items():
                print(f"      root: a = {r}  (mult {m})")
                if hasattr(r, 'is_rational') and r.is_rational:
                    print(f"        Q-rational!")
                elif hasattr(r, 'is_algebraic') and r.is_algebraic:
                    print(f"        algebraic over Q")
        except Exception as e:
            print(f"    roots() failed: {e}")
        # Try real_roots
        try:
            real_roots = sp.real_roots(f)
            print(f"    real roots:")
            for r in real_roots:
                rn = sp.N(r, 25)
                print(f"      a = {rn}  (exact: {r})")
        except Exception as e:
            print(f"    real_roots() failed: {e}")


print("\n" + "#" * 70)
print("# F5 part 4 complete")
print("#" * 70)
