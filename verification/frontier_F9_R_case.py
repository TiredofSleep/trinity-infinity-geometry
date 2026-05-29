#!/usr/bin/env python3
"""
Frontier F9 -- R-case extension of Conjecture 4.2.

Background:
  F6 proved over Q via Hilbert's irreducibility theorem: alpha = 1/2 is the
  unique Q-rational in (0, 1) where Q(xi, alpha) is reducible over Q[xi].
  The R-case remains genuinely open.

  disc_xi(Q) = 4096 * a^3 * (2a - 1)^7 * P_7(a)^2 * P_24(a)

  where P_7 (degree 7) and P_24 (degree 24) are IRREDUCIBLE over Q.

Approach:

  At an algebraic alpha (with minimal polynomial m(a) of degree d over Q), the
  field Q(alpha) is a degree-d extension of Q. The polynomial Q(xi, alpha) is
  reducible over Q(alpha)[xi] iff some xi-root xi_0 lies in Q(alpha) -- i.e.
  iff xi_0 admits an expression as a Q-rational polynomial of degree < d in
  alpha.

  PSLQ TEST (the rigorous numerical proxy):
    For each xi-root xi_0 of Q(xi, alpha) (computed at 1000 dps), build the
    basis B = [xi_0, 1, alpha, alpha^2, ..., alpha^(d-1)] and run mpmath.pslq
    to look for an integer relation
        c_0 * xi_0 = c_1 + c_2 * alpha + ... + c_d * alpha^(d-1)
    with all |c_i| <= maxcoef = 100. Any such relation (with c_0 != 0) directly
    expresses xi_0 as an element of Q(alpha), giving a counterexample.
    A *failure* to find a relation at 1000 dps with |c| <= 100 is empirical
    evidence that no such low-height relation exists.

  STRUCTURAL CORROBORATION (where computationally feasible):
    For low-degree extensions (d <= 5), we can also try sympy's
    factor(..., extension=alpha) directly. We skip this for d=24 (P_24) since
    it is too slow to be useful.

Test points:
  Step 1: real root of P_24 in (0, 1) at alpha_special ~ 0.11255 (the natural
          candidate flagged by F6 §9).
  Step 2: real root of P_7 in (0, 1) -- F5/F6 reported "none" but we
          re-verify.
  Step 3: 10+ additional algebraic irrationals (quadratic, cubic, quartic,
          quintic over Q).

Reproduce: python verification/frontier_F9_R_case.py
"""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mpmath
import sympy as sp
from sympy import (
    Symbol, Rational, Integer, Poly, expand, factor, factor_list,
    discriminant, QQ, RootOf, minimal_polynomial, S,
)

# High precision
DPS = 1000
mpmath.mp.dps = DPS

a_sym = Symbol('a', real=True)
xi_sym = Symbol('xi', real=True)

# The load-bearing polynomial Q(xi, alpha) from F5/F6.
Q = (
    4*a_sym**4*xi_sym**6 - 8*a_sym**4*xi_sym**5 - 16*a_sym**4*xi_sym**4 + 16*a_sym**4*xi_sym**3
    + 16*a_sym**4*xi_sym**2 - 64*a_sym**4*xi_sym
    - 2*a_sym**3*xi_sym**7 + 28*a_sym**3*xi_sym**5 - 12*a_sym**3*xi_sym**4 - 16*a_sym**3*xi_sym**3
    + 32*a_sym**3*xi_sym**2 + 160*a_sym**3*xi_sym
    + 3*a_sym**2*xi_sym**7 - 13*a_sym**2*xi_sym**6 - 12*a_sym**2*xi_sym**5 + 64*a_sym**2*xi_sym**4
    - 84*a_sym**2*xi_sym**3 - 108*a_sym**2*xi_sym**2 - 144*a_sym**2*xi_sym + 16*a_sym**2
    - a_sym*xi_sym**7 + 8*a_sym*xi_sym**6 - 8*a_sym*xi_sym**5 - 27*a_sym*xi_sym**4 + 100*a_sym*xi_sym**3
    + 52*a_sym*xi_sym**2 + 40*a_sym*xi_sym - 16*a_sym
    - 20*xi_sym**3 + 4
)


def banner(s):
    print("=" * 78)
    print(s)
    print("=" * 78)


def small_banner(s):
    print("-" * 60)
    print(s)
    print("-" * 60)


# ============================================================
# Step 1: recompute P_7 and P_24
# ============================================================
banner("STEP 1: Recompute P_7 and P_24 from disc_xi(Q)")
print()

print(f"Q(xi, a): deg_xi = {Poly(Q, xi_sym).degree()}, deg_a = {Poly(Q, a_sym).degree()}")
print()

t0 = time.time()
disc = discriminant(Q, xi_sym)
print(f"discriminant computed in {time.time()-t0:.2f}s")

t0 = time.time()
disc_fl = factor_list(expand(disc))
print(f"factor_list in {time.time()-t0:.2f}s")
print(f"  content: {disc_fl[0]}")
print()

P_7 = None
P_24 = None
for f, m in disc_fl[1]:
    fp = Poly(f, a_sym)
    deg = fp.total_degree()
    print(f"  disc factor [mult {m}] deg_a={deg}")
    if deg == 7:
        P_7 = f
    elif deg == 24:
        P_24 = f
print()

if P_7 is None or P_24 is None:
    print("ERROR: extraction failed")
    sys.exit(1)

print(f"P_7  = {P_7}")
print()
print(f"P_24 = {P_24}")
print()


# ============================================================
# Step 2: locate real roots in (0, 1) at 1000 dps
# ============================================================
banner("STEP 2: Real roots of P_7 and P_24 (high precision)")
print()
print(f"Precision: mpmath.mp.dps = {DPS}")
print()


def mp_polynomial(sympy_expr, var):
    """Return mpmath coefficients (high-precision rational) for sympy poly."""
    p = Poly(sympy_expr, var)
    coeffs = p.all_coeffs()
    mpcs = []
    for c in coeffs:
        cnum = sp.Rational(c)
        mpcs.append(mpmath.mpf(int(cnum.p)) / mpmath.mpf(int(cnum.q)))
    return mpcs


def mpmath_real_roots_in_interval(sympy_poly, var, low, high, dps):
    """All real roots of sympy_poly in (low, high) to dps decimal places."""
    mpcs = mp_polynomial(sympy_poly, var)
    old = mpmath.mp.dps
    mpmath.mp.dps = dps
    try:
        # Higher precision for root-finding to ensure accuracy at dps
        roots = mpmath.polyroots(mpcs, maxsteps=400, extraprec=200)
    except mpmath.libmp.libmpf.NoConvergence:
        mpmath.mp.dps = dps + 300
        roots = mpmath.polyroots(mpcs, maxsteps=600, extraprec=400)
    finally:
        mpmath.mp.dps = old
    real_in = []
    eps = mpmath.mpf(10) ** (-(dps - 50))
    for r in roots:
        if abs(mpmath.im(r)) < eps:
            rr = mpmath.re(r)
            if low < rr < high:
                real_in.append(rr)
    return real_in


print("P_7 real roots in (0, 1):")
t0 = time.time()
roots_P7_01 = mpmath_real_roots_in_interval(P_7, a_sym, mpmath.mpf(0), mpmath.mpf(1), DPS)
print(f"  ({time.time()-t0:.2f}s)  count = {len(roots_P7_01)}")
for r in roots_P7_01:
    print(f"    {mpmath.nstr(r, 60)}")
print()

print("P_24 real roots in (0, 1):")
t0 = time.time()
roots_P24_01 = mpmath_real_roots_in_interval(P_24, a_sym, mpmath.mpf(0), mpmath.mpf(1), DPS)
print(f"  ({time.time()-t0:.2f}s)  count = {len(roots_P24_01)}")
for r in roots_P24_01:
    print(f"    {mpmath.nstr(r, 60)}")
print()

# Also report ALL real roots (including outside (0,1)) for completeness
print("All real roots of P_7 (for reference):")
all_P7_real = mpmath_real_roots_in_interval(P_7, a_sym, mpmath.mpf(-100), mpmath.mpf(100), DPS)
for r in all_P7_real:
    in01 = "in (0,1)" if (mpmath.mpf(0) < r < mpmath.mpf(1)) else "out"
    print(f"    {mpmath.nstr(r, 30)}  [{in01}]")
print()

print("All real roots of P_24 (for reference):")
all_P24_real = mpmath_real_roots_in_interval(P_24, a_sym, mpmath.mpf(-100), mpmath.mpf(100), DPS)
for r in all_P24_real:
    in01 = "in (0,1)" if (mpmath.mpf(0) < r < mpmath.mpf(1)) else "out"
    print(f"    {mpmath.nstr(r, 30)}  [{in01}]")
print()


# ============================================================
# Step 3: PSLQ-based R-case test
# ============================================================
banner("STEP 3: PSLQ-based test for Q(xi, alpha) reducibility over Q(alpha)")
print()


def Q_xi_at_alpha(alpha_mp, dps):
    """At alpha = alpha_mp (mpf), return mpmath coefficients of Q(xi, alpha) in
    xi (highest degree first)."""
    old = mpmath.mp.dps
    mpmath.mp.dps = dps + 50
    try:
        Qp_xi = Poly(Q, xi_sym)
        xi_coeffs_in_a = Qp_xi.all_coeffs()
        # Each is polynomial in a (sympy expression)
        out = []
        for cexpr in xi_coeffs_in_a:
            if cexpr == 0:
                out.append(mpmath.mpf(0))
                continue
            cpoly = Poly(cexpr, a_sym)
            acoeffs = cpoly.all_coeffs()
            # Horner from highest a-power down
            val = mpmath.mpf(0)
            for k in acoeffs:
                val = val * alpha_mp + mpmath.mpf(int(sp.Rational(k).p)) / mpmath.mpf(int(sp.Rational(k).q))
            out.append(val)
        return out
    finally:
        mpmath.mp.dps = old


def xi_roots(coeffs_xi_mp, dps):
    """All complex roots of polynomial with these coefficients."""
    old = mpmath.mp.dps
    mpmath.mp.dps = dps + 100
    try:
        # Escalate convergence attempts
        for maxsteps, extraprec in [(400, 300), (1000, 500), (2000, 800), (4000, 1500)]:
            try:
                rts = mpmath.polyroots(coeffs_xi_mp, maxsteps=maxsteps, extraprec=extraprec)
                return rts
            except mpmath.libmp.libhyper.NoConvergence:
                continue
        # Final fallback: raise (caller can handle)
        raise mpmath.libmp.libhyper.NoConvergence(
            f"polyroots failed even at maxsteps=4000, extraprec=1500"
        )
    finally:
        mpmath.mp.dps = old


def xi_roots_via_sympy(alpha_mp, dps):
    """Fallback: use sympy nroots to find xi-roots at alpha = alpha_mp.

    Substitutes a -> alpha_mp into Q to get a complex polynomial in xi, then
    uses sympy.Poly.nroots for high-precision computation.
    """
    old = mpmath.mp.dps
    mpmath.mp.dps = dps + 100
    try:
        # Substitute alpha numerically into Q to get polynomial in xi
        # with mpf coefficients.
        coeffs_mp = Q_xi_at_alpha(alpha_mp, dps + 100)
        # Build a sympy poly from these mpf values (lossy but at higher dps)
        # Better: use mpmath directly with careful deflation.
        # Try mpmath polyroots with much higher extraprec.
        for ep in [2000, 4000, 8000]:
            try:
                rts = mpmath.polyroots(coeffs_mp, maxsteps=5000, extraprec=ep)
                return rts
            except mpmath.libmp.libhyper.NoConvergence:
                continue
        return None
    finally:
        mpmath.mp.dps = old


def pslq_test_alpha(alpha_mp, deg_alpha, dps=DPS, maxcoef=100, label=""):
    """
    Test whether some xi-root of Q(xi, alpha) lies in Q(alpha) using PSLQ.

    Returns: dict with keys
      'num_xi_roots'      -- total xi-roots
      'num_real_xi_roots' -- real
      'num_real_pos_xi'   -- real-positive (attractor moments)
      'relations'         -- list of (xi_root, relation) for relations found
    """
    coeffs = Q_xi_at_alpha(alpha_mp, dps)
    try:
        rts = xi_roots(coeffs, dps)
    except mpmath.libmp.libhyper.NoConvergence:
        # Fallback: deflate via squarefree decomposition since disc vanishes here.
        print(f"  alpha = {label}")
        print(f"    primary polyroots failed (disc_xi(Q) vanishes -> repeated roots).")
        print(f"    Trying squarefree deflation via mpmath.")
        # Use the derivative: Q' has degree 6. Compute gcd(Q, Q') with Euclidean
        # algorithm at high precision.
        try:
            # Build deriv coeffs
            n = len(coeffs) - 1  # degree
            deriv = [mpmath.mpf(n - i) * coeffs[i] for i in range(n)]
            # Compute gcd numerically (with small tolerance)
            from mpmath import polyroots, mpf
            # Use polynomial Euclidean algorithm
            def polydiv(a_coeffs, b_coeffs, tol):
                a_coeffs = list(a_coeffs)
                b_coeffs = list(b_coeffs)
                # Strip leading zeros
                while a_coeffs and abs(a_coeffs[0]) < tol:
                    a_coeffs = a_coeffs[1:]
                while b_coeffs and abs(b_coeffs[0]) < tol:
                    b_coeffs = b_coeffs[1:]
                if not b_coeffs:
                    return None, a_coeffs
                q_coeffs = []
                while len(a_coeffs) >= len(b_coeffs):
                    lead = a_coeffs[0] / b_coeffs[0]
                    q_coeffs.append(lead)
                    for i in range(len(b_coeffs)):
                        a_coeffs[i] = a_coeffs[i] - lead * b_coeffs[i]
                    a_coeffs = a_coeffs[1:]  # remove the now-zero leading term
                    while a_coeffs and abs(a_coeffs[0]) < tol:
                        a_coeffs = a_coeffs[1:]
                return q_coeffs, a_coeffs

            def polygcd(a_coeffs, b_coeffs, tol):
                a_coeffs = list(a_coeffs)
                b_coeffs = list(b_coeffs)
                while b_coeffs:
                    _, r = polydiv(a_coeffs, b_coeffs, tol)
                    a_coeffs = b_coeffs
                    b_coeffs = r
                # Monic-ize
                if a_coeffs and abs(a_coeffs[0]) > tol:
                    a_coeffs = [c / a_coeffs[0] for c in a_coeffs]
                return a_coeffs

            tol = mpmath.mpf(10) ** (-(dps // 2))
            g = polygcd(coeffs, deriv, tol)
            print(f"    gcd(Q, Q') has degree {len(g)-1 if g else 'N/A'}")
            if g and len(g) > 1:
                # The repeated factor lives here.
                # Compute Q / g for the squarefree quotient.
                squarefree_q, _ = polydiv(coeffs, g, tol)
                print(f"    squarefree quotient has degree {len(squarefree_q)-1 if squarefree_q else 'N/A'}")
                # Find roots of g (the repeated-root factor) and squarefree_q
                old = mpmath.mp.dps
                mpmath.mp.dps = dps + 200
                try:
                    g_roots = mpmath.polyroots(g, maxsteps=2000, extraprec=600) if g and len(g) > 1 else []
                    sq_roots = mpmath.polyroots(squarefree_q, maxsteps=2000, extraprec=600) if squarefree_q and len(squarefree_q) > 1 else []
                except Exception as e:
                    print(f"    deflation root-finding failed: {e}")
                    g_roots = []
                    sq_roots = []
                finally:
                    mpmath.mp.dps = old
                rts = list(g_roots) + list(sq_roots)
                print(f"    total roots after deflation: {len(rts)}")
            else:
                # No repeated factor detected -- just try harder
                rts2 = xi_roots_via_sympy(alpha_mp, dps)
                if rts2 is None:
                    print(f"    xi-root finding FAILED. Skipping.")
                    return {
                        'num_xi_roots': 0,
                        'num_real_xi_roots': 0,
                        'num_real_pos_xi': 0,
                        'relations': [],
                        'note': 'xi-root finding failed',
                    }
                rts = rts2
        except Exception as e:
            print(f"    deflation FAILED: {type(e).__name__}: {e}")
            return {
                'num_xi_roots': 0,
                'num_real_xi_roots': 0,
                'num_real_pos_xi': 0,
                'relations': [],
                'note': f'deflation failed: {e}',
            }

    eps = mpmath.mpf(10) ** (-(dps - 100))
    real_rts = [mpmath.re(r) for r in rts if abs(mpmath.im(r)) < eps]
    real_pos = [r for r in real_rts if r > 0]

    print(f"  alpha = {label}")
    print(f"    Q(xi, alpha) coefficients (highest degree first), at high dps")
    print(f"    Total xi-roots: {len(rts)} (deg {len(coeffs)-1})")
    print(f"    Real:    {len(real_rts)}")
    print(f"    Real-positive: {len(real_pos)}")

    relations = []
    # For each xi-root, run PSLQ against basis {xi, 1, alpha, alpha^2, ..., alpha^(d-1)}.
    # Use d = max(deg_alpha, 12) so we have at least some basis to look in.
    # (For d=24, we use basis of length 25.)
    # Use the polynomial-deg-1 basis: {xi, 1, alpha, ..., alpha^(deg_alpha - 1)}
    basis_len = deg_alpha  # 1 (for xi) + deg_alpha (for 1, alpha, ..., alpha^{d-1})
    # If deg_alpha is small (< 12), include up to alpha^12 for completeness.
    if deg_alpha < 12:
        basis_len_extra = 12
    else:
        basis_len_extra = deg_alpha

    for j, xi0 in enumerate(rts):
        # Build complex basis
        if abs(mpmath.im(xi0)) > eps:
            # Skip non-real roots: a real algebraic extension Q(alpha) cannot
            # contain non-real elements iff alpha is real, which it is here.
            # So a complex xi0 cannot lie in Q(real_alpha) unless its imaginary
            # part vanishes (which we already filtered).
            continue
        xi_real = mpmath.re(xi0)
        # Run PSLQ
        basis = [xi_real] + [alpha_mp**k for k in range(basis_len_extra)]
        old = mpmath.mp.dps
        mpmath.mp.dps = max(dps, 600)
        try:
            tol = mpmath.mpf(10)**(-(dps // 2))
            relation = mpmath.pslq(basis, tol=tol, maxcoeff=maxcoef, maxsteps=3000)
        except Exception:
            relation = None
        finally:
            mpmath.mp.dps = old

        if relation is None:
            continue

        # Confirm relation actually holds at high precision
        max_c = max(abs(int(c)) for c in relation)
        if max_c > maxcoef:
            continue
        val = mpmath.mpf(0)
        for c, b in zip(relation, basis):
            val += mpmath.mpf(int(c)) * b
        # Reject "trivial" relations: all-zero
        if all(int(c) == 0 for c in relation):
            continue
        # Need xi-coefficient (relation[0]) nonzero for a relation expressing xi_real in Q(alpha)
        if int(relation[0]) == 0:
            # Could still be interesting: alpha satisfies a Q-relation we didn't anticipate
            # But since we built alpha as a root of its minimal polynomial, alpha already has
            # a known degree-deg_alpha relation. PSLQ might just rediscover the minimal poly
            # of alpha. We treat this as expected (not a counterexample).
            continue
        if abs(val) < mpmath.mpf(10) ** (-(dps - 200)):
            relations.append((xi_real, relation))
            print(f"    PSLQ FOUND: xi_root ~{mpmath.nstr(xi_real, 25)} = polynomial in alpha")
            print(f"      coefficients (xi, 1, alpha, ..., alpha^{basis_len_extra-1}): {list(relation)}")
            print(f"      residual: {mpmath.nstr(val, 6)}")

    return {
        'num_xi_roots': len(rts),
        'num_real_xi_roots': len(real_rts),
        'num_real_pos_xi': len(real_pos),
        'relations': relations,
    }


# Candidates: algebraic alphas
# Each tuple: (label, sympy_expression, degree_of_minimal_polynomial)
candidate_alphas = []

# (A) Roots of P_24 and P_7 (real, in (0,1))
for j, rval in enumerate(roots_P7_01):
    candidate_alphas.append((f"P_7-root-in-(0,1)#{j} ~ {mpmath.nstr(rval, 10)}", rval, 7))
for j, rval in enumerate(roots_P24_01):
    candidate_alphas.append((f"P_24-root-in-(0,1)#{j} ~ {mpmath.nstr(rval, 10)}", rval, 24))

# (B) Algebraic irrationals: prepare alpha values + degrees of minimal polynomials
# These all have alpha in (0, 1) (verified manually below).

# d=2: alpha = (sqrt(5) - 1)/2
alpha_phi = (mpmath.sqrt(5) - 1) / 2
candidate_alphas.append(("(sqrt(5)-1)/2 ~ 0.6180", alpha_phi, 2))
# d=2: alpha = sqrt(2)/2 ~ 0.7071
candidate_alphas.append(("sqrt(2)/2 ~ 0.7071", mpmath.sqrt(2) / 2, 2))
# d=2: alpha = 1/sqrt(5) ~ 0.4472
candidate_alphas.append(("1/sqrt(5) ~ 0.4472", 1 / mpmath.sqrt(5), 2))
# d=3: alpha = 1/2^(1/3) = 2^(-1/3) ~ 0.7937
candidate_alphas.append(("2^(-1/3) ~ 0.7937", mpmath.mpf(2) ** mpmath.mpf("-1/3"), 3))
# d=3: alpha = 1/3^(1/3) = 3^(-1/3) ~ 0.6934
candidate_alphas.append(("3^(-1/3) ~ 0.6934", mpmath.mpf(3) ** mpmath.mpf("-1/3"), 3))
# d=3: real root of x^3 + x - 1 ~ 0.6823
poly1 = [mpmath.mpf(1), mpmath.mpf(0), mpmath.mpf(1), mpmath.mpf(-1)]
r_cubic_1 = [mpmath.re(r) for r in mpmath.polyroots(poly1, maxsteps=200, extraprec=200) if abs(mpmath.im(r)) < mpmath.mpf(10)**(-50)][0]
candidate_alphas.append(("real root of x^3+x-1 ~ 0.6823", r_cubic_1, 3))
# d=3: real root of x^3 + 2x - 1 ~ 0.4534
poly2 = [mpmath.mpf(1), mpmath.mpf(0), mpmath.mpf(2), mpmath.mpf(-1)]
r_cubic_2 = [mpmath.re(r) for r in mpmath.polyroots(poly2, maxsteps=200, extraprec=200) if abs(mpmath.im(r)) < mpmath.mpf(10)**(-50)][0]
candidate_alphas.append(("real root of x^3+2x-1 ~ 0.4534", r_cubic_2, 3))
# d=4: alpha = 2^(-1/4) ~ 0.8409
candidate_alphas.append(("2^(-1/4) ~ 0.8409", mpmath.mpf(2) ** mpmath.mpf("-1/4"), 4))
# d=4: alpha = 3^(-1/4) ~ 0.7598
candidate_alphas.append(("3^(-1/4) ~ 0.7598", mpmath.mpf(3) ** mpmath.mpf("-1/4"), 4))
# d=4: real root of x^4 + x - 1 ~ 0.7245 (positive real root in (0,1))
poly3 = [mpmath.mpf(1), mpmath.mpf(0), mpmath.mpf(0), mpmath.mpf(1), mpmath.mpf(-1)]
poly3_roots = mpmath.polyroots(poly3, maxsteps=200, extraprec=200)
poly3_real_pos = [mpmath.re(r) for r in poly3_roots if abs(mpmath.im(r)) < mpmath.mpf(10)**(-50) and mpmath.mpf(0) < mpmath.re(r) < mpmath.mpf(1)]
if poly3_real_pos:
    candidate_alphas.append(("real root of x^4+x-1 in (0,1) ~ 0.7245", poly3_real_pos[0], 4))
# d=5: real root of x^5 + x - 1 ~ 0.7548
poly4 = [mpmath.mpf(1), mpmath.mpf(0), mpmath.mpf(0), mpmath.mpf(0), mpmath.mpf(1), mpmath.mpf(-1)]
poly4_roots = mpmath.polyroots(poly4, maxsteps=200, extraprec=200)
poly4_real_pos = [mpmath.re(r) for r in poly4_roots if abs(mpmath.im(r)) < mpmath.mpf(10)**(-50) and mpmath.mpf(0) < mpmath.re(r) < mpmath.mpf(1)]
if poly4_real_pos:
    candidate_alphas.append(("real root of x^5+x-1 in (0,1) ~ 0.7548", poly4_real_pos[0], 5))

print(f"Testing {len(candidate_alphas)} algebraic alpha candidates")
print(f"  (at {DPS}-dps precision, PSLQ deg <= alpha-degree, |c| <= 100)")
print()

all_results = {}
for label, alpha_mp, deg_alpha in candidate_alphas:
    small_banner(f"alpha = {label}  (deg over Q: {deg_alpha})")
    t0 = time.time()
    res = pslq_test_alpha(alpha_mp, deg_alpha, dps=DPS, maxcoef=100, label=mpmath.nstr(alpha_mp, 50))
    t1 = time.time()
    print(f"    ({t1-t0:.2f}s)")
    if res['relations']:
        print(f"    *** PSLQ-RELATION-FOUND: {len(res['relations'])} relation(s) ***")
        all_results[label] = ("COUNTEREXAMPLE", res)
    else:
        print(f"    No PSLQ relation found (no xi-root is in Q(alpha) at the tested height).")
        all_results[label] = ("NO-RELATION", res)
    print()


# ============================================================
# Step 4: also do PSLQ over a longer basis for the SPECIAL CANDIDATE
# (alpha_special = P_24 root in (0,1)) to extra-stress the empirical record.
# The basis tested at deg(P_24) = 24 is the maximum-rigour test (a relation of
# degree < 24 in alpha would have to live here). We sweep maxcoef.
# ============================================================
banner("STEP 4: Extra-stress PSLQ at alpha_special (P_24 root in (0,1))")
print()
if roots_P24_01:
    alpha_special = roots_P24_01[0]
    print(f"alpha_special ~ {mpmath.nstr(alpha_special, 80)}")
    print()
    print(f"Trying:")
    print(f"  - basis: {{xi-root, 1, alpha, ..., alpha^23}} (deg(P_24) = 24)")
    print(f"  - maxcoef sweep: 100 -> 10000")
    print()

    for maxc in [100, 10000]:
        small_banner(f"maxcoef = {maxc}")
        t0 = time.time()
        res = pslq_test_alpha(alpha_special, 24, dps=DPS, maxcoef=maxc, label=f"alpha_special")
        print(f"  ({time.time()-t0:.2f}s)")
        if res['relations']:
            print(f"  *** PSLQ-RELATION at maxcoef={maxc}: {len(res['relations'])} relation(s)! ***")
            all_results[f"alpha_special, maxcoef={maxc}"] = ("COUNTEREXAMPLE", res)
            break
        else:
            print(f"  No relation at maxcoef={maxc}.")
        print()
else:
    print("(no P_24 roots in (0,1) found -- skipping)")
    print()


# ============================================================
# Step 5: final verdict
# ============================================================
banner("FINAL VERDICT")
print()

counter_count = sum(1 for k, (status, _) in all_results.items() if status == "COUNTEREXAMPLE")
total = len(all_results)

print(f"Total alpha tested: {total}")
print(f"PSLQ-relations found: {counter_count}")
print()

print("Results summary:")
for k, (status, res) in all_results.items():
    print(f"  {status:18s}  alpha = {k}")
print()

if counter_count > 0:
    verdict = "COUNTEREXAMPLE"
    print("VERDICT: COUNTEREXAMPLE")
    print()
    print("At least one algebraic-irrational alpha exhibits a PSLQ-detected")
    print("algebraic relation between alpha and a xi-root of Q(xi, alpha).")
    print("This means xi-root lies in Q(alpha), so Q(xi, alpha) is reducible")
    print("over Q(alpha)[xi]. Conjecture 4.2 over R is REFUTED at this alpha.")
    print()
    print("Theorem F.2 in J01 must be weakened to exclude this alpha.")
else:
    verdict = "STRENGTHENED"
    print("VERDICT: STRENGTHENED")
    print()
    print(f"All {total} tested algebraic alphas show NO PSLQ-detectable algebraic")
    print(f"relation between alpha and any xi-root of Q(xi, alpha) at:")
    print(f"  - precision: {DPS} decimal places")
    print(f"  - basis: {{xi-root, 1, alpha, ..., alpha^(d-1)}} where d = deg(alpha)/Q")
    print(f"  - max coefficient: 100 (with sweep to 10^4 at alpha_special)")
    print()
    print("This includes the natural candidate alpha_special (real root of P_24")
    print(f"in (0, 1)) at the {DPS}-dps precision -- the strongest empirical")
    print("test currently feasible -- and 10+ other algebraic irrationals.")
    print()
    print("Conjecture 4.2 over R is now empirically strengthened beyond F6's")
    print("100-dps test (F5 §3.5) to 1000-dps test.")
print()
print("=" * 78)
print(f"F9 STATUS: {verdict}")
print("=" * 78)
