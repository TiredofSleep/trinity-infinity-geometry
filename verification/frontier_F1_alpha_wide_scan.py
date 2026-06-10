#!/usr/bin/env python3
"""
Frontier F1 — α-uniqueness extended REAL grid scan (Conjecture 4.2).

Builds on:
  - D57 / J15 17-pt Stern-Brocot rational scan (PSLQ deg <= 8, |c| <= 50)
  - 02_results/dynamics/ALPHA_UNIQUENESS_EXTENDED.md 41-candidate scan
    (10 irrational + 31 Stern-Brocot rationals q <= 10; PSLQ deg <= 12, |c| <= 100)

This scan extends to:
  - Specific algebraic irrationals: 1/sqrt(2), 1/sqrt(3), sqrt(2)-1, 1/phi
  - Specific transcendentals: 1/e, pi/4, ln(2), 1/pi
  - Finer real scan around 1/2: 0.3, 0.4, 0.45, 0.49, 0.5 (control),
    0.51, 0.55, 0.6, 0.7
  - Re-tests at MULTIPLE precisions: 50, 100, 200 digits, to determine
    precision threshold at which alpha = 1/2's relation appears.

For each alpha:
  1) iterate T+B mix to convergence on 4-core {V=0, H=7, Br=8, R=9}
  2) compute H/Br and r/br (= R/Br) attractor moments
  3) attempt PSLQ at deg <= 8 with |c| <= 50 (matches D57 grid)
  4) AND at deg <= 12 with |c| <= 100 (matches May-12 wider grid)
  5) filter spurious "rational root near x" hits via sympy.ground_roots

If alpha = 1/2 remains the unique value with a genuine algebraic relation:
  -> empirical evidence FOR Conjecture 4.2
If any other alpha produces a genuine algebraic relation:
  -> counterexample (or near-miss) to Conjecture 4.2

This is exploratory frontier work; NOT a J-paper modification.
Reproduce: python verification/frontier_F1_alpha_wide_scan.py
Runtime: ~2-4 minutes at 50-digit precision (one pass per precision level).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mpmath as mp
from math import gcd
from ck_tables import TSML, BHML


# ============================================================
# Core attractor iteration (matches existing alpha_pslq_sweep.py)
# ============================================================
TOL_EXP = 40         # convergence tolerance 10^-TOL_EXP
MAX_STEPS = 4000


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


def joint_attractor(alpha, max_iter=MAX_STEPS):
    """Iterate the T+B mix at alpha (mpmath) to convergence on the 4-core start."""
    tol = mp.mpf(10) ** (-TOL_EXP)
    alpha = mp.mpf(alpha)
    one_minus = mp.mpf(1) - alpha

    p = [mp.mpf(0)] * 10
    for c in [0, 7, 8, 9]:
        p[c] = mp.mpf(1) / 4

    for step in range(max_iter):
        Tf = fuse(TSML, p)
        Bf = fuse(BHML, p)
        sT = sum(Tf); sB = sum(Bf)
        if sT == 0 or sB == 0:
            return p, step
        Tf = [x / sT for x in Tf]
        Bf = [x / sB for x in Bf]
        out = [alpha * Tf[k] + one_minus * Bf[k] for k in range(10)]
        s = sum(out)
        new_p = [x / s for x in out]
        delta = max(abs(new_p[k] - p[k]) for k in range(10))
        p = new_p
        if delta < tol:
            return p, step + 1
    return p, max_iter


# ============================================================
# PSLQ search with two grid settings
# ============================================================
def pslq_polynomial(x, max_degree, coeff_bound):
    """Search for an integer polynomial P(x) approx 0 with
       2 <= deg P <= max_degree and |c_i| <= coeff_bound.
       Returns (coeffs_ascending, residual) or (None, None)."""
    tol = mp.mpf(10) ** -(mp.mp.dps - 8)
    if not isinstance(x, mp.mpf):
        x = mp.mpf(x)

    best = None
    for d in range(2, max_degree + 1):
        basis = [x ** i for i in range(d + 1)]
        try:
            rel = mp.pslq(basis, tol=tol, maxcoeff=coeff_bound)
        except Exception:
            rel = None
        if rel is None:
            continue
        coeffs = list(rel)
        while coeffs and coeffs[-1] == 0:
            coeffs.pop()
        if len(coeffs) <= 1:
            continue
        sup = max(abs(c) for c in coeffs)
        if sup > coeff_bound:
            continue
        resid = abs(sum(coeffs[i] * (x ** i) for i in range(len(coeffs))))
        eff_deg = len(coeffs) - 1
        if best is None or (eff_deg, sup) < (best[0], best[2]):
            best = (eff_deg, tuple(coeffs), sup, resid)
    if best is None:
        return None, None
    return best[1], best[3]


def is_spurious_relation(rel, x, tol=mp.mpf(10) ** -3):
    """A relation is spurious if the polynomial has a rational root near x."""
    try:
        from sympy import Symbol, Poly
        s = Symbol('s', rational=True)
        coeffs = [int(c) for c in rel]
        poly = Poly(sum(coeffs[k] * s**k for k in range(len(coeffs))), s)
        rational_roots = poly.ground_roots()
        for root, mult in rational_roots.items():
            try:
                root_val = mp.mpf(str(root))
                if abs(x - root_val) < tol:
                    return True, root, mult
            except Exception:
                continue
        return False, None, None
    except Exception:
        return False, None, None


def format_poly(coeffs):
    parts = []
    for k, c in enumerate(coeffs):
        if c == 0:
            continue
        if k == 0:
            parts.append(f"{c:+d}")
        elif k == 1:
            parts.append(f"{c:+d}*x")
        else:
            parts.append(f"{c:+d}*x^{k}")
    return " ".join(parts) + " = 0"


# ============================================================
# Candidate alpha values: the user-requested REAL grid
# ============================================================
def build_candidates():
    """Returns list of (name, alpha_mpf, category)."""
    cs = []
    # Algebraic irrationals
    cs.append(("1/sqrt(2)",    1 / mp.sqrt(2),                "alg-irr"))
    cs.append(("1/sqrt(3)",    1 / mp.sqrt(3),                "alg-irr"))
    cs.append(("sqrt(2)-1",    mp.sqrt(2) - 1,                "alg-irr"))
    cs.append(("1/phi",        2 / (1 + mp.sqrt(5)),          "alg-irr"))
    # Transcendentals
    cs.append(("1/e",          1 / mp.e,                      "trans"))
    cs.append(("pi/4",         mp.pi / 4,                     "trans"))
    cs.append(("ln(2)",        mp.ln(2),                      "trans"))
    cs.append(("1/pi",         1 / mp.pi,                     "trans"))
    # Finer real scan around 1/2 (mixed values per task spec)
    for a_str, a_val in [("0.3", mp.mpf("0.3")),
                         ("0.4", mp.mpf("0.4")),
                         ("0.45", mp.mpf("0.45")),
                         ("0.49", mp.mpf("0.49")),
                         ("0.5",  mp.mpf("0.5")),    # control
                         ("0.51", mp.mpf("0.51")),
                         ("0.55", mp.mpf("0.55")),
                         ("0.6",  mp.mpf("0.6")),
                         ("0.7",  mp.mpf("0.7"))]:
        cs.append((a_str, a_val, "mixed-near-half"))
    return cs


# ============================================================
# Main: run scan at multiple precisions
# ============================================================
def run_scan_at_precision(dps, pslq_settings):
    """pslq_settings = list of (deg, coeff_bound) tuples."""
    mp.mp.dps = dps

    candidates = build_candidates()
    print()
    print("=" * 90)
    print(f"  SCAN at {dps}-digit precision   ({len(candidates)} alpha values)")
    print("=" * 90)

    # Print header
    settings_str = ", ".join([f"deg<={d}/|c|<={c}" for (d, c) in pslq_settings])
    print(f"  PSLQ grids: {settings_str}")
    print()
    header = f"{'alpha':<14} {'category':<18} {'H/Br':<22} {'r/br':<22} {'genuine?':<10}"
    print(header)
    print("-" * len(header))

    results = []
    for name, alpha, cat in candidates:
        try:
            p, _ = joint_attractor(alpha)
            if p[8] == 0:
                print(f"{name:<14} {cat:<18} {'Br=0; skip':<60}")
                continue
            H_Br = p[7] / p[8]
            r_br = p[9] / p[8]

            hits = {"H/Br": [], "r/br": []}
            spurious = {"H/Br": [], "r/br": []}

            for label, x in [("H/Br", H_Br), ("r/br", r_br)]:
                for deg, cb in pslq_settings:
                    rel, err = pslq_polynomial(x, max_degree=deg, coeff_bound=cb)
                    if rel is None:
                        continue
                    is_sp, sp_root, sp_mult = is_spurious_relation(rel, x)
                    if is_sp:
                        spurious[label].append((deg, cb, rel, err, sp_root, sp_mult))
                    else:
                        hits[label].append((deg, cb, rel, err))
                        break   # found genuine; no need to try higher-degree grids

            genuine = "BOTH" if (hits["H/Br"] and hits["r/br"]) else \
                      ("H/Br" if hits["H/Br"] else
                       ("r/br" if hits["r/br"] else "no"))
            print(f"{name:<14} {cat:<18} {mp.nstr(H_Br, 14):<22} {mp.nstr(r_br, 14):<22} {genuine:<10}")

            results.append({
                "name": name, "alpha": alpha, "category": cat,
                "H_Br": H_Br, "r_br": r_br,
                "hits": hits, "spurious": spurious,
            })
        except Exception as e:
            print(f"{name:<14} ERROR: {e}")

    # Detailed report
    print()
    print("DETAILED GENUINE HITS (and spurious filtered):")
    for r in results:
        had_anything = (r["hits"]["H/Br"] or r["hits"]["r/br"]
                        or r["spurious"]["H/Br"] or r["spurious"]["r/br"])
        if not had_anything:
            continue
        print(f"\n  alpha = {r['name']}  ({r['category']})")
        for label in ["H/Br", "r/br"]:
            for (deg, cb, rel, err) in r["hits"][label]:
                print(f"    GENUINE {label} relation @ (deg<={deg}, |c|<={cb}): "
                      f"{format_poly(list(rel))}    residual = {mp.nstr(err, 4)}")
            for (deg, cb, rel, err, sp_root, sp_mult) in r["spurious"][label]:
                print(f"    spurious {label} (deg<={deg}, |c|<={cb}): "
                      f"{format_poly(list(rel))}  -> rational root {sp_root} (mult {sp_mult})")

    # Summary
    print()
    print(f"SUMMARY at dps = {dps}:")
    genuine_non_half = [r for r in results
                        if abs(r["alpha"] - mp.mpf("0.5")) > mp.mpf(10)**-30
                        and (r["hits"]["H/Br"] or r["hits"]["r/br"])]
    genuine_half = [r for r in results
                    if abs(r["alpha"] - mp.mpf("0.5")) <= mp.mpf(10)**-30
                    and (r["hits"]["H/Br"] or r["hits"]["r/br"])]
    print(f"  alpha = 1/2  genuine hits: {len(genuine_half)}  (expected 1)")
    print(f"  non-1/2 alpha genuine hits: {len(genuine_non_half)}  (expected 0 if Conj 4.2 holds)")

    return results, genuine_non_half


def main():
    print("=" * 90)
    print("Frontier F1: extended alpha-uniqueness REAL-grid scan")
    print("Testing Conjecture 4.2 over algebraic-irrationals, transcendentals,")
    print("and a finer mixed-decimal scan around alpha = 1/2.")
    print("=" * 90)

    # Two PSLQ grids: D57 grid and the May-12 wider grid
    pslq_grids = [(8, 50), (12, 100)]

    summary_by_precision = {}
    for dps in [50, 100]:
        results, non_half_genuine = run_scan_at_precision(dps, pslq_grids)
        summary_by_precision[dps] = {
            "results": results,
            "non_half_genuine": non_half_genuine,
        }

    # Final verdict
    print()
    print("=" * 90)
    print("FINAL VERDICT")
    print("=" * 90)
    for dps, info in summary_by_precision.items():
        n_nh = len(info["non_half_genuine"])
        if n_nh == 0:
            print(f"  dps = {dps:3d}: NO non-1/2 alpha produced a GENUINE relation.")
            print(f"            -> empirical evidence FOR Conjecture 4.2 at this precision.")
        else:
            print(f"  dps = {dps:3d}: {n_nh} non-1/2 alpha(s) produced GENUINE relations!")
            for r in info["non_half_genuine"]:
                print(f"            counterexample candidate: alpha = {r['name']}")
                for label in ["H/Br", "r/br"]:
                    for (deg, cb, rel, err) in r["hits"][label]:
                        print(f"              {label}: {format_poly(list(rel))}  resid={mp.nstr(err,3)}")


if __name__ == "__main__":
    main()
