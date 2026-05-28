"""
alpha_pslq_sweep.py - F3 sharpening: high-precision PSLQ sweep on the
T+B-mix runtime attractor over a fine rational alpha grid.

WP105 D42 established empirically that alpha = 1/2 is the unique value
in [0.05, 0.95] (sweep at 19 points) where the attractor admits a small-
coefficient quadratic relation H/Br + small-coefficient quartic for r/br.

This script sharpens that statement by:

    1. Computing the runtime attractor at HIGH precision (mpmath, 50 digits)
       on a finer rational alpha grid (Stern-Brocot fractions through depth
       6, plus all p/q with q <= 7).

    2. For each alpha, applying PSLQ to detect the minimal-degree integer
       polynomial relation satisfied by H/Br up to degree 8 with
       coefficient bound |c| <= 50.

    3. Reporting: degree of minimal poly found (or "none up to limit"),
       sup-norm of coefficient vector, and PSLQ residual.

Result format: a compact table comparing every alpha against alpha=1/2.

Reproduction:
    python alpha_pslq_sweep.py [--precision 60] [--max-degree 8]
                                [--max-coeff 50]
"""
from __future__ import annotations

import argparse
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp


# ----- canonical TSML / BHML tables -----
TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
BHML_ROWS = [
    "0123456789",  "1234567266",  "2334567366",  "3444567466",  "4555567577",
    "5666667677",  "6777777777",  "7234567890",  "8666777978",  "9666777080",
]


def fuse_mp(p, table):
    """Bilinear fusion p (x) p under multiplication table 'table'.
    Inputs: p is a list of 10 mpmath mpfs. Returns a list of 10 mpfs."""
    r = [mp.mpf(0)] * 10
    for a in range(10):
        if p[a] == 0:
            continue
        pa = p[a]
        for b in range(10):
            if p[b] == 0:
                continue
            r[table[a][b]] += pa * p[b]
    return r


def normalize_l1(v):
    s = sum(v)
    if s == 0:
        return v
    return [x / s for x in v]


def attractor_mp(alpha, T, B, max_iter=4000, tol=None):
    """Iterate the T+B-mix at a given alpha (mpmath precision).
    alpha can be a Fraction or an mpf.
    Returns: (final probability vector, iterations).
    """
    if tol is None:
        tol = mp.mpf(10) ** (-mp.mp.dps + 5)
    if isinstance(alpha, Fraction):
        alpha_mp = mp.mpf(alpha.numerator) / mp.mpf(alpha.denominator)
    else:
        alpha_mp = mp.mpf(alpha)
    one_minus = mp.mpf(1) - alpha_mp

    # Start from uniform on the 4-core {V=0, H=7, Br=8, R=9}
    p = [mp.mpf(0)] * 10
    p[0] = p[7] = p[8] = p[9] = mp.mpf("0.25")

    for k in range(max_iter):
        p_t = normalize_l1(fuse_mp(p, T))
        p_b = normalize_l1(fuse_mp(p, B))
        p_new = normalize_l1([alpha_mp * p_t[i] + one_minus * p_b[i] for i in range(10)])
        # Convergence
        diff = max(abs(p_new[i] - p[i]) for i in range(10))
        p = p_new
        if diff < tol:
            return p, k + 1
    return p, max_iter


def pslq_polynomial(x, max_degree=8, max_coeff=50, tol=None):
    """Search for an integer polynomial P(x) = sum c_i x^i with
    1 <= deg P <= max_degree and |c_i| <= max_coeff such that |P(x)| < tol.

    Strategy: invoke PSLQ on the basis [1, x, x^2, ..., x^d] for each d,
    progressively. Return the lowest-degree (smallest sup-norm) result.
    """
    if tol is None:
        tol = mp.mpf(10) ** (-mp.mp.dps + 8)
    if not isinstance(x, mp.mpf):
        x = mp.mpf(x)

    best = None  # (degree, coeffs, sup_norm, residual)
    for d in range(2, max_degree + 1):
        basis = [x ** i for i in range(d + 1)]
        try:
            rel = mp.pslq(basis, tol=tol, maxcoeff=max_coeff)
        except Exception:
            rel = None
        if rel is None:
            continue
        # rel is the integer relation: rel[0]*1 + rel[1]*x + ... + rel[d]*x^d ~= 0
        # Coefficient vector ascending: c_0, c_1, ..., c_d
        coeffs = list(rel)
        # Skip if leading coefficient is 0 (degenerate)
        if coeffs[-1] == 0:
            # Drop trailing zeros; effective degree is lower
            while coeffs and coeffs[-1] == 0:
                coeffs.pop()
            if len(coeffs) <= 1:
                continue
        sup = max(abs(c) for c in coeffs)
        if sup > max_coeff:
            continue
        # Compute residual
        resid = sum(coeffs[i] * (x ** i) for i in range(len(coeffs)))
        eff_deg = len(coeffs) - 1
        candidate = (eff_deg, tuple(coeffs), sup, abs(resid))
        # Prefer smaller degree, then smaller sup-norm
        if best is None or (eff_deg, sup) < (best[0], best[2]):
            best = candidate
    return best


def stern_brocot_fractions(depth):
    """All rationals p/q in (0, 1) with q <= depth and gcd(p, q) = 1."""
    from math import gcd
    seen = set()
    for q in range(2, depth + 1):
        for p in range(1, q):
            if gcd(p, q) == 1:
                seen.add(Fraction(p, q))
    return sorted(seen)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--precision", type=int, default=50,
                        help="mpmath decimal precision (default 50)")
    parser.add_argument("--max-degree", type=int, default=8)
    parser.add_argument("--max-coeff", type=int, default=50)
    parser.add_argument("--depth", type=int, default=7,
                        help="Max denominator in Stern-Brocot grid (default 7)")
    args = parser.parse_args()

    mp.mp.dps = args.precision

    print("=" * 90)
    print(f"WP113 -- alpha-uniqueness PSLQ sweep")
    print(f"  precision: {args.precision} digits")
    print(f"  max degree:  {args.max_degree}")
    print(f"  max coeff:   +/-{args.max_coeff}")
    print("=" * 90)
    print()

    T = [[int(c) for c in row] for row in TSML_ROWS]
    B = [[int(c) for c in row] for row in BHML_ROWS]

    alphas = stern_brocot_fractions(args.depth)
    print(f"Sweeping {len(alphas)} rational alpha values (q <= {args.depth}):")
    if len(alphas) <= 25:
        print(f"  {[str(a) for a in alphas]}")
    else:
        print(f"  {[str(a) for a in alphas[:10]]} ... {[str(a) for a in alphas[-5:]]}")
    print()

    print(f"{'alpha':<10} {'H/Br':<14} {'H/Br min poly':<28} {'r/br':<14} {'r/br min poly':<28}")
    print("-" * 130)

    rows = []
    for alpha in alphas:
        attr, iters = attractor_mp(alpha, T, B, max_iter=4000)
        V, H, Br, R = attr[0], attr[7], attr[8], attr[9]

        # H/Br
        if Br < mp.mpf(10) ** (-args.precision + 10):
            h_ratio = mp.inf
            h_poly = None
        else:
            h_ratio = H / Br
            h_poly = pslq_polynomial(h_ratio, max_degree=args.max_degree,
                                       max_coeff=args.max_coeff)

        # r/br
        if Br < mp.mpf(10) ** (-args.precision + 10):
            rbr_ratio = mp.inf
            rbr_poly = None
        else:
            rbr_ratio = R / Br
            rbr_poly = pslq_polynomial(rbr_ratio, max_degree=args.max_degree,
                                         max_coeff=args.max_coeff)

        def poly_str(poly):
            if poly is None:
                return "(none)"
            deg, coeffs, sup, resid = poly
            terms = []
            for i, c in enumerate(coeffs):
                if c == 0:
                    continue
                if i == 0:
                    terms.append(f"{c:+d}")
                elif i == 1:
                    terms.append(f"{c:+d}x")
                else:
                    terms.append(f"{c:+d}x^{i}")
            s = " ".join(terms)
            return s if len(s) <= 26 else s[:23] + "..."

        h_str = f"{float(h_ratio):.6f}" if h_ratio != mp.inf else "inf"
        rbr_str = f"{float(rbr_ratio):.6f}" if rbr_ratio != mp.inf else "inf"
        print(f"{str(alpha):<10} {h_str:<14} {poly_str(h_poly):<28} {rbr_str:<14} {poly_str(rbr_poly):<28}")
        rows.append((alpha, iters, h_ratio, h_poly, rbr_ratio, rbr_poly))

    print()
    print("=" * 90)
    print("VERDICT")
    print("=" * 90)
    print()

    # Identify minimum-degree alphas
    clean_h = [r for r in rows if r[3] is not None]
    clean_rbr = [r for r in rows if r[5] is not None]
    print(f"Total alphas tested:                {len(rows)}")
    print(f"Alphas with H/Br algebraic relation (deg <= {args.max_degree}, coeff <= {args.max_coeff}):    {len(clean_h)}")
    print(f"Alphas with r/br algebraic relation (deg <= {args.max_degree}, coeff <= {args.max_coeff}):    {len(clean_rbr)}")
    print()

    if clean_h:
        clean_h.sort(key=lambda r: (r[3][0], r[3][2]))
        print("Cleanest H/Br relations:")
        for alpha, iters, ratio, h_poly, _, _ in clean_h[:5]:
            deg, coeffs, sup, resid = h_poly
            print(f"  alpha = {alpha}: H/Br ~= {float(ratio):.10f}, deg {deg}, sup-coeff {sup}")
            print(f"    coeffs ascending: {coeffs}, residual {float(resid):.2e}")

    print()
    if clean_rbr:
        clean_rbr.sort(key=lambda r: (r[5][0], r[5][2]))
        print("Cleanest r/br relations:")
        for alpha, iters, _, _, rbr_ratio, rbr_poly in clean_rbr[:5]:
            deg, coeffs, sup, resid = rbr_poly
            print(f"  alpha = {alpha}: r/br ~= {float(rbr_ratio):.10f}, deg {deg}, sup-coeff {sup}")
            print(f"    coeffs ascending: {coeffs}, residual {float(resid):.2e}")

    print()
    # F3 specific check: is alpha = 1/2 uniquely lowest-degree for both H/Br and r/br?
    half = next((r for r in rows if r[0] == Fraction(1, 2)), None)
    if half and half[3] is not None and half[5] is not None:
        deg_h = half[3][0]
        sup_h = half[3][2]
        deg_rbr = half[5][0]
        sup_rbr = half[5][2]
        n_other_h = len([r for r in clean_h if r[0] != Fraction(1, 2)])
        n_other_rbr = len([r for r in clean_rbr if r[0] != Fraction(1, 2)])
        print("=" * 90)
        print(f"  alpha = 1/2: H/Br is degree {deg_h} (sup-coeff {sup_h});  "
              f"r/br is degree {deg_rbr} (sup-coeff {sup_rbr})")
        print(f"  Other alphas with H/Br algebraic:  {n_other_h}")
        print(f"  Other alphas with r/br algebraic:  {n_other_rbr}")
        print()
        if n_other_h == 0 and n_other_rbr == 0:
            print(f"  >> alpha = 1/2 is the UNIQUE rational in the {len(rows)}-point grid")
            print(f"     where the runtime attractor admits low-degree algebraic relations")
            print(f"     for BOTH H/Br and r/br within the (degree, coefficient) bounds tested.")
            print(f"  >> This SHARPENS WP105 D42 from a 19-point linspace sweep")
            print(f"     to a {len(rows)}-point Stern-Brocot sweep with PSLQ at {args.precision}-digit precision.")
        else:
            print(f"  Note: some other alphas have algebraic relations (see lists above).")


if __name__ == "__main__":
    main()
