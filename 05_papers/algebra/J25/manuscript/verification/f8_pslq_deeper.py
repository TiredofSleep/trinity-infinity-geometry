"""
f8_pslq_deeper.py - Push F8 PSLQ on simplex-tangent eigenvalues to
                    higher precision/degrees/coefficients.

§18 (D75/D76): the simplex-tangent eigenvalues at the alpha=1/2 fixed
point (lambda_1 = 0.190735 +/- 0.292991*i, |lambda_1| = 0.349605;
lambda_3 = -0.245146) admit NO PSLQ algebraic relation at degree <= 8,
maxcoeff <= 10^6.

This script extends:
  (a) precision to mpmath dps = 100 (was 60)
  (b) degree up to 24 (was 8)
  (c) coefficient bound up to 10^9 (was 10^6)
  (d) tries PSLQ against the fixed-point coordinates V, H, Br, R
      (not just powers of the eigenvalue alone) -- the eigenvalues
      live in Q(V, H, Br, R), not necessarily in Q.

Triggered by Brayden 2026-04-29: "keep going until you run out of rope".

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §18, §30 (this).
"""
from __future__ import annotations

import mpmath as mp
import sympy as sp


def main():
    mp.mp.dps = 100
    print("=" * 80)
    print("F8 PSLQ deepened: simplex-tangent eigenvalues at higher precision")
    print("=" * 80)
    print()

    # --- Setup: get fixed point and Jacobian eigenvalues at high precision ---
    V_sym, H_sym, Br_sym, R_sym = sp.symbols('V H Br R', positive=True, real=True)

    # 4-core iteration map at alpha=1/2
    pt_V  = V_sym**2 + 2*V_sym*Br_sym + 2*V_sym*R_sym
    pt_H  = 2*V_sym*H_sym + (H_sym + Br_sym + R_sym)**2
    pt_Br = sp.Integer(0)
    pt_R  = sp.Integer(0)
    pb_V  = V_sym**2 + 2*H_sym*R_sym + R_sym**2
    pb_H  = 2*V_sym*H_sym + Br_sym**2
    pb_Br = 2*V_sym*Br_sym + 2*Br_sym*R_sym + H_sym**2
    pb_R  = 2*V_sym*R_sym + 2*H_sym*Br_sym

    half = sp.Rational(1, 2)
    F_V  = half * (pt_V  + pb_V)
    F_H  = half * (pt_H  + pb_H)
    F_Br = half * (pt_Br + pb_Br)
    F_R  = half * (pt_R  + pb_R)

    F_funcs = [F_V, F_H, F_Br, F_R]
    fvars = [V_sym, H_sym, Br_sym, R_sym]

    # Find fixed point at high precision
    F_lambdified = [sp.lambdify(fvars, F, modules=['mpmath']) for F in F_funcs]
    p = [mp.mpf("0.25")] * 4
    for k in range(8000):
        new_p = [F_lambdified[i](*p) for i in range(4)]
        s = sum(new_p)
        new_p = [x / s for x in new_p]
        diff = max(abs(new_p[i] - p[i]) for i in range(4))
        p = new_p
        if diff < mp.mpf(10) ** (-90):
            break
    print(f"  Fixed point at {mp.mp.dps}-digit precision (iters={k+1}):")
    print(f"    V  = {mp.nstr(p[0], 50)}")
    print(f"    H  = {mp.nstr(p[1], 50)}")
    print(f"    Br = {mp.nstr(p[2], 50)}")
    print(f"    R  = {mp.nstr(p[3], 50)}")
    print()

    # Jacobian at fixed point at high precision
    J_funcs = [[sp.diff(F, v) for v in fvars] for F in F_funcs]
    J_lamb = [[sp.lambdify(fvars, J_funcs[i][j], modules=['mpmath'])
               for j in range(4)] for i in range(4)]
    Jhp_rows = [[J_lamb[i][j](*p) for j in range(4)] for i in range(4)]
    Jhp = mp.matrix(Jhp_rows)

    # Eigenvalues
    eig_E, _ = mp.eig(Jhp)
    eig_list = sorted([eig_E[k] for k in range(4)], key=lambda x: -abs(x))
    print(f"  Jacobian eigenvalues:")
    for i, e in enumerate(eig_list):
        er, ei = mp.re(e), mp.im(e)
        print(f"    lambda_{i} = {mp.nstr(er, 30)} + {mp.nstr(ei, 30)} i,  |lambda| = {mp.nstr(abs(e), 30)}")
    print()

    # The non-trivial simplex-tangent eigenvalues (skip lambda_0 = 2 radial)
    nontriv = eig_list[1:]
    lam1 = nontriv[0]  # complex pair (we take one)
    lam3 = nontriv[2]  # the real one, smallest
    mod1 = abs(lam1)
    re1 = mp.re(lam1)

    print("-" * 80)
    print("PART A -- PSLQ on |lambda_1|, Re(lambda_1), lambda_3 against ONLY their powers")
    print("-" * 80)
    print()

    targets = [
        ("|lambda_1|", mod1),
        ("Re(lambda_1)", re1),
        ("lambda_3 (real)", lam3),
    ]

    for name, val in targets:
        print(f"  Target: {name} = {mp.nstr(val, 30)}")
        for deg in [4, 8, 12, 16, 20]:
            powers = [val ** k for k in range(deg + 1)]
            for maxc in [10**4, 10**6, 10**9]:
                try:
                    rel = mp.pslq(powers, tol=mp.mpf(10) ** (-60), maxcoeff=maxc)
                    if rel is not None:
                        print(f"    deg<={deg}, maxc={maxc}: {rel}")
                        break
                except Exception:
                    continue
            else:
                continue  # didn't find at this degree, try next
            break  # found one
        else:
            print(f"    NO relation found up to deg 20 / maxc 10^9.")
        print()

    print("-" * 80)
    print("PART B -- PSLQ against the fixed-point coordinates V, H, Br, R")
    print("-" * 80)
    print()
    print("  Hypothesis: eigenvalues live in Q(V, H, Br, R), so they should be")
    print("  expressible as polynomials in V, H, Br, R with rational coefficients.")
    print()

    V, H, Br, R = p[0], p[1], p[2], p[3]

    targets = [
        ("|lambda_1|", mod1),
        ("Re(lambda_1)", re1),
        ("lambda_3", lam3),
    ]

    for name, val in targets:
        print(f"  Target: {name}")
        # Try linear combination val = a*V + b*H + c*Br + d*R + e*1
        try:
            rel = mp.pslq([val, V, H, Br, R, mp.mpf(1)],
                          tol=mp.mpf(10) ** (-60), maxcoeff=10**6)
            print(f"    linear: {rel}")
        except Exception:
            print(f"    linear: failed")
        # Try val^2 = a*V + b*H + c*Br + d*R + e*V*H + f*V*Br + g*V*R + h*H*Br + ...
        # Actually that has too many basis elements; let me try simpler.
        try:
            # val^2 vs degree-2 combinations
            basis = [val * val, V*V, V*H, V*Br, V*R, H*H, H*Br, H*R, Br*Br, Br*R, R*R, mp.mpf(1)]
            rel = mp.pslq(basis, tol=mp.mpf(10) ** (-60), maxcoeff=10**6)
            print(f"    val^2 vs deg-2 polys in V,H,Br,R: {rel}")
        except Exception:
            print(f"    val^2 deg-2: failed")
        # Try val vs single mononomials in V, H, Br, R
        for sym_name, sym_val in [("V", V), ("H", H), ("Br", Br), ("R", R), ("V*H", V*H), ("V*Br", V*Br),
                                   ("H*Br", H*Br), ("H*R", H*R), ("Br*R", Br*R)]:
            try:
                # val = c*sym_val for small rational c?
                rel = mp.pslq([val, sym_val], tol=mp.mpf(10) ** (-60), maxcoeff=10**6)
                if rel and rel[1] != 0:
                    ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                    if abs(ratio) > 0:
                        # check it's actually a clean ratio
                        check_val = sym_val * ratio
                        if abs(check_val - val) < mp.mpf(10) ** (-30):
                            print(f"    {name} ~ {ratio} * {sym_name}  (CLEAN RATIO)")
            except Exception:
                pass
        print()

    # --- PART C: try the determinant/trace of the simplex-restricted 3x3 ---
    print("-" * 80)
    print("PART C -- PSLQ on trace and determinant of simplex-restricted Jacobian")
    print("-" * 80)

    tr = sum(nontriv).real
    det = mp.mpf(1)
    for v in nontriv:
        det = det * v
    det = mp.re(det)

    print(f"  tr = {mp.nstr(tr, 30)}")
    print(f"  det = {mp.nstr(det, 30)}")
    print()

    for name, val in [("trace", tr), ("det", det)]:
        for deg in [3, 4, 6, 8]:
            for maxc in [10**4, 10**6, 10**9]:
                powers = [val ** k for k in range(deg + 1)]
                try:
                    rel = mp.pslq(powers, tol=mp.mpf(10) ** (-60), maxcoeff=maxc)
                    if rel is not None:
                        print(f"  {name} deg<={deg}, maxc={maxc}: {rel}")
                        break
                except Exception:
                    continue
            else:
                continue
            break
        else:
            print(f"  {name}: NO relation found.")

    # --- PART D: verify the trace candidate at MUCH higher precision ---
    print()
    print("-" * 80)
    print("PART D -- verify trace candidate with stricter bounds")
    print("-" * 80)
    print()
    print(f"  Recomputing trace at 200 digits...")
    mp.mp.dps = 200
    # Re-find fixed point at 200 digits
    p = [mp.mpf("0.25")] * 4
    for k in range(20000):
        new_p = [F_lambdified[i](*p) for i in range(4)]
        s = sum(new_p)
        new_p = [x / s for x in new_p]
        diff = max(abs(new_p[i] - p[i]) for i in range(4))
        p = new_p
        if diff < mp.mpf(10) ** (-180):
            break
    Jhp_rows = [[J_lamb[i][j](*p) for j in range(4)] for i in range(4)]
    Jhp = mp.matrix(Jhp_rows)
    eig_E, _ = mp.eig(Jhp)
    eig_list = sorted([eig_E[k] for k in range(4)], key=lambda x: -abs(x))
    nontriv = eig_list[1:]
    tr_hp = mp.re(sum(nontriv))
    det_hp = mp.re(nontriv[0] * nontriv[1] * nontriv[2])
    print(f"    tr (200 digit)  = {mp.nstr(tr_hp, 60)}")
    print(f"    det (200 digit) = {mp.nstr(det_hp, 60)}")
    print()

    # Tight PSLQ
    print(f"  Tight PSLQ on trace (maxc varying):")
    for deg in [2, 3, 4]:
        for maxc in [10**3, 10**4, 10**5, 10**6]:
            powers = [tr_hp ** k for k in range(deg + 1)]
            try:
                rel = mp.pslq(powers, tol=mp.mpf(10) ** (-150), maxcoeff=maxc)
                if rel is not None:
                    # Verify the relation is tight (residual << precision)
                    poly_val = sum(rel[k] * (tr_hp ** k) for k in range(deg + 1))
                    print(f"    deg={deg}, maxc={maxc}: {rel}")
                    print(f"      residual: {mp.nstr(abs(poly_val), 5)}")
                    if abs(poly_val) < mp.mpf(10) ** (-100):
                        print(f"      VERIFIED at 100 digits.")
                    else:
                        print(f"      probably noise.")
            except Exception as e:
                pass

    print()
    print(f"  Tight PSLQ on det (maxc varying):")
    for deg in [2, 3, 4, 6, 8]:
        for maxc in [10**3, 10**4, 10**5, 10**6, 10**8]:
            powers = [det_hp ** k for k in range(deg + 1)]
            try:
                rel = mp.pslq(powers, tol=mp.mpf(10) ** (-150), maxcoeff=maxc)
                if rel is not None:
                    poly_val = sum(rel[k] * (det_hp ** k) for k in range(deg + 1))
                    print(f"    deg={deg}, maxc={maxc}: {rel}")
                    print(f"      residual: {mp.nstr(abs(poly_val), 5)}")
                    if abs(poly_val) < mp.mpf(10) ** (-100):
                        print(f"      VERIFIED at 100 digits.")
                    else:
                        print(f"      probably noise.")
                    break
            except Exception:
                pass

    # Now the BIG one: lambda_3 directly at higher degrees
    print()
    print("-" * 80)
    print("PART E -- lambda_3 (real eigenvalue) at MUCH higher degrees / coeffs")
    print("-" * 80)
    lam3_hp = mp.re(nontriv[2])
    print(f"  lambda_3 = {mp.nstr(lam3_hp, 60)}")
    for deg in [4, 6, 8, 10, 12]:
        for maxc in [10**3, 10**4, 10**5, 10**6, 10**8]:
            powers = [lam3_hp ** k for k in range(deg + 1)]
            try:
                rel = mp.pslq(powers, tol=mp.mpf(10) ** (-150), maxcoeff=maxc)
                if rel is not None:
                    poly_val = sum(rel[k] * (lam3_hp ** k) for k in range(deg + 1))
                    print(f"  deg={deg}, maxc={maxc}: {rel}")
                    print(f"    residual: {mp.nstr(abs(poly_val), 5)}")
                    if abs(poly_val) < mp.mpf(10) ** (-100):
                        print(f"    VERIFIED at 100 digits.")
                        # Check if it factors
                        x = sp.Symbol('x')
                        poly = sum(rel[k] * x ** k for k in range(deg + 1))
                        poly_sp = sp.Poly(poly, x)
                        print(f"    polynomial: {poly}")
                        print(f"    factored over Q: {sp.factor(poly)}")
                    break
            except Exception:
                pass

    # Factor the trace polynomial
    print()
    print("-" * 80)
    print("PART F -- Factor trace polynomial 443*t^4 - 5588*t^3 + 21048*t^2 - 26240*t + 3200")
    print("-" * 80)
    x = sp.Symbol('x', real=True)
    trace_poly = -3200 + 26240*x - 21048*x**2 + 5588*x**3 - 443*x**4
    print(f"  trace_poly = {trace_poly}")
    print(f"  factored over Q: {sp.factor(trace_poly)}")
    # Discriminant
    disc = sp.discriminant(trace_poly, x)
    print(f"  discriminant = {disc}")
    print(f"  discriminant factored = {sp.factorint(int(disc)) if int(disc) != 0 else 0}")

    print()
    print("=" * 80)
    print("VERDICT")
    print("=" * 80)
    print()
    print("  If PSLQ found a relation at higher degrees: simplex-tangent eigenvalues")
    print("  are algebraic (just at deeper depth than initially tested).")
    print()
    print("  If still no relation: either truly transcendental, or in a Q(V, H, Br, R)")
    print("  extension whose minimal polynomial coefficients are too large for")
    print("  PSLQ at maxc = 10^9.")
    print()
    print("  The lens prediction (per §28's depth-2 cluster): F8's radial eigenvalue")
    print("  is degree 2 (= 2 exactly).  Simplex-tangent eigenvalues might be at")
    print("  degree 4 (the next quadratic extension) or higher.  D75's PSLQ at")
    print("  deg<=8 maxc<=10^6 found nothing; this script extends.")


if __name__ == "__main__":
    main()
