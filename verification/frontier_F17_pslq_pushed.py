#!/usr/bin/env python3
"""
Frontier F17 -- PSLQ pushed harder.

The main F17 sweep at maxcoeff=50 found PSLQ relations only among the BASIS
elements (e.g., near-zero combinations of pi, pi/7, 7) -- the target 1/alpha
never participated. This is the honest signal: at bounded height, 1/alpha
is INDEPENDENT of the substrate primitives chosen.

Here we push PSLQ at:
  - maxcoeff up to 1000
  - precision up to 120 dps
  - smaller, more curated bases (so PSLQ doesn't waste degrees of freedom
    on degenerate basis-internal relations)

We also test the J42 "structural intuition":
    1/alpha ∈ Q-span{1, sqrt(7), pi/7}
by direct PSLQ on that 3-element basis.

If even with maxcoeff=1000 the target stays out of the relation, the
honest verdict is NO-FIT.
"""
import sys, os, time
import mpmath as mp

mp.mp.dps = 120

INV_ALPHA_PDG = mp.mpf("137.035999084")
INV_ALPHA_MZ  = mp.mpf("127.951")

PRIMS = {
    "1":         mp.mpf(1),
    "3":         mp.mpf(3),
    "7":         mp.mpf(7),
    "11":        mp.mpf(11),
    "13":        mp.mpf(13),
    "23":        mp.mpf(23),
    "71":        mp.mpf(71),
    "sqrt3":     mp.sqrt(3),
    "sqrt5":     mp.sqrt(5),
    "sqrt7":     mp.sqrt(7),
    "sqrt11":    mp.sqrt(11),
    "sqrt13":    mp.sqrt(13),
    "sqrt13/2":  mp.sqrt(13)/2,
    "phi":       (1+mp.sqrt(5))/2,
    "pi":        mp.pi,
    "pi/7":      mp.pi/7,
    "pi/11":     mp.pi/11,
    "pi^2/7":    mp.pi**2/7,
    "e":         mp.e,
    "gamma":     mp.euler,
    "ln2":       mp.log(2),
    "ln7":       mp.log(7),
    "ln3":       mp.log(3),
    "zeta3":     mp.zeta(3),
    "G":         mp.catalan,
}

def pslq_target_in(target_val, basis_names, maxcoeff, tol_exp=-40):
    """
    PSLQ on [target_val, basis_vals]. Returns (coeffs, residual) or None.
    Filters out 'no target coefficient' relations: if coeffs[0]==0, try
    to detect a relation just among basis -- still report but flag.
    """
    basis = [target_val] + [PRIMS[n] for n in basis_names]
    try:
        coeffs = mp.pslq(basis, tol=mp.mpf(10)**tol_exp, maxcoeff=maxcoeff)
    except Exception as e:
        return None, str(e)
    if coeffs is None:
        return None, "no relation"
    s = mp.mpf(0)
    for c, v in zip(coeffs, basis):
        s += c * v
    return (list(coeffs), s), None

def main():
    bases = [
        ("J42 intuition: {1, sqrt(7), pi/7}",
            ["1", "sqrt7", "pi/7"]),
        ("J42 + 7",
            ["1", "7", "sqrt7", "pi/7"]),
        ("J42 + 71",
            ["1", "7", "71", "sqrt7", "pi/7"]),
        ("substrate primes only (no irrationals)",
            ["1", "3", "7", "11", "13", "23", "71"]),
        ("substrate primes + sqrt7",
            ["1", "3", "7", "11", "13", "23", "71", "sqrt7"]),
        ("substrate primes + phi",
            ["1", "3", "7", "11", "13", "23", "71", "phi"]),
        ("substrate primes + sqrt7 + phi",
            ["1", "3", "7", "11", "13", "23", "71", "sqrt7", "phi"]),
        ("substrate + sqrt13/2 (9-vec)",
            ["1", "3", "7", "11", "13", "23", "71", "sqrt13/2"]),
        ("just 1 and pi",
            ["1", "pi"]),
        ("just 1 and pi/7",
            ["1", "pi/7"]),
        ("just 1, pi/7, sqrt7",
            ["1", "pi/7", "sqrt7"]),
    ]
    print(f"PSLQ pushed: dps={mp.mp.dps}")
    print(f"target 1/alpha(0) = {INV_ALPHA_PDG}")
    print(f"target 1/alpha(M_Z) = {INV_ALPHA_MZ}")
    print()
    for target_name, target_val in [
        ("1/alpha(0)",   INV_ALPHA_PDG),
        ("1/alpha(M_Z)", INV_ALPHA_MZ),
    ]:
        print(f"\n===== Target: {target_name} = {target_val} =====")
        for label, names in bases:
            print(f"\n  Basis: {label}")
            print(f"  primitives: {names}")
            for maxc in [50, 100, 200, 500, 1000]:
                res, err = pslq_target_in(target_val, names, maxc, tol_exp=-30)
                if res is None:
                    print(f"    maxcoeff={maxc:4d}: NO RELATION ({err})")
                    continue
                coeffs, residual = res
                if coeffs[0] == 0:
                    # target not in relation; basis-internal degeneracy
                    print(f"    maxcoeff={maxc:4d}: TARGET NOT IN RELATION (basis-internal: {coeffs})")
                    # don't break; try higher maxcoeff in hopes target enters
                    continue
                # target IS in the relation
                # express target = -sum(c_i * v_i)/c0
                c0 = coeffs[0]
                rest = coeffs[1:]
                parts = []
                for c, n in zip(rest, names):
                    if c == 0:
                        continue
                    parts.append(f"({-c}/{c0})*{n}")
                rhs = " + ".join(parts) if parts else "0"
                print(f"    maxcoeff={maxc:4d}: TARGET IN RELATION")
                print(f"      coeffs: {coeffs}")
                print(f"      {target_name} = {rhs}")
                print(f"      residual: {mp.nstr(residual, 6)}")
                # verify
                rebuilt = mp.mpf(0)
                for c, n in zip(rest, names):
                    rebuilt += (-c)/c0 * PRIMS[n]
                err_check = abs(rebuilt - target_val) / abs(target_val)
                print(f"      rebuilt:  {mp.nstr(rebuilt, 12)}  (relerr {mp.nstr(err_check, 4)})")
                break  # exit maxcoeff loop, found a real fit

if __name__ == "__main__":
    t0 = time.time()
    main()
    print(f"\nruntime: {time.time()-t0:.1f}s")
