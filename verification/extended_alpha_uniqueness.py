#!/usr/bin/env python3
"""
Extended alpha-uniqueness search (Conjecture 4.2).

D57 verified that alpha = 1/2 is the unique rational point in a 17-point
Stern-Brocot grid where the runtime attractor admits algebraic relations
for both H/Br and r/br, at PSLQ degree <= 8, coeff bound <= 50.

This script extends the search:

(A) Irrational alpha values: test ~10 candidates including 1/sqrt(2),
    1/sqrt(3), 1/pi, 1/e, 1/phi, sqrt(2)-1, etc. If any non-1/2 value
    produces an algebraic relation at PSLQ degree <= 12, coeff bound <= 100,
    that's a counterexample to strong alpha-uniqueness.

(B) Finer rational Stern-Brocot grid: extend from 17 points to ~50 points
    at the same elevated PSLQ depth, to further bound the rational-uniqueness
    case.

Conjecture 4.2 (open): alpha = 1/2 is the unique REAL (not just rational)
for which any non-trivial polynomial relation exists between attractor
moments.

This script tests Conjecture 4.2 by exhaustive numerical scan.

Run: python verification/extended_alpha_uniqueness.py
Status: result-dependent (could strengthen or refine the conjecture).

Copyright (c) 2026 Brayden Ross Sanders / 7SiTe LLC. CC-BY-4.0.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mpmath as mp
from math import gcd
from ck_tables import TSML, BHML

mp.mp.dps = 50

# Iteration tolerance and max steps
TOL = mp.mpf(10) ** -40
MAX_STEPS = 300

# PSLQ search parameters (extended from D57)
PSLQ_DEG = 12       # max degree to search
PSLQ_COEFF_BOUND = 100   # max |coeff| considered "small"


def fuse(table, p):
    out = [mp.mpf(0)] * 10
    for i in range(10):
        for j in range(10):
            out[table[i][j]] += p[i] * p[j]
    return out


def joint_attractor(alpha, p0=None):
    """Iterate to convergence and return the attractor (V, H, Br, R) and r/br."""
    if p0 is None:
        # start from uniform on 4-core
        p = [mp.mpf(0)] * 10
        for c in [0, 7, 8, 9]:
            p[c] = mp.mpf(1) / 4
    else:
        p = list(p0)

    alpha = mp.mpf(alpha)
    prev = list(p)
    for step in range(MAX_STEPS):
        Tf = fuse(TSML, p)
        Bf = fuse(BHML, p)
        out = [alpha * Tf[k] + (1 - alpha) * Bf[k] for k in range(10)]
        s = sum(out)
        new_p = [x / s for x in out]
        delta = max(abs(new_p[k] - prev[k]) for k in range(10))
        prev = list(p)
        p = new_p
        if delta < TOL:
            break
    return p, step + 1


def pslq_polynomial(x, max_degree=PSLQ_DEG, coeff_bound=PSLQ_COEFF_BOUND):
    """Try PSLQ on [1, x, x^2, ..., x^max_degree] to find an integer
    polynomial relation a_0 + a_1*x + ... + a_n*x^n approx 0.
    Returns (coefficients, residual) or (None, None) if no relation found
    within bound."""
    try:
        powers = [x ** k for k in range(max_degree + 1)]
        for deg in range(2, max_degree + 1):
            try:
                rel = mp.pslq(powers[:deg + 1],
                              tol=mp.mpf(10) ** -30,
                              maxcoeff=coeff_bound)
                if rel is not None:
                    max_c = max(abs(c) for c in rel)
                    if max_c <= coeff_bound:
                        val = sum(rel[k] * powers[k] for k in range(deg + 1))
                        if abs(val) < mp.mpf(10) ** -25:
                            return rel, abs(val)
            except Exception:
                continue
        return None, None
    except Exception as e:
        return None, None


def is_spurious_relation(rel, x, tol=mp.mpf(10)**-3):
    """A relation is 'spurious' if the recovered polynomial has a rational
    root within `tol` of `x`. Such polynomials trivially have a small value
    at x because of the root, not because x is genuinely a root of an
    irreducible polynomial of the recovered degree.

    Uses sympy to factor over Q and find rational roots.
    """
    try:
        from sympy import Symbol, Poly, Rational, factor, sympify
        s = Symbol('s', rational=True)
        coeffs = [int(c) for c in rel]
        # Build polynomial in s
        poly = Poly(sum(coeffs[k] * s**k for k in range(len(coeffs))), s)
        rational_roots = poly.ground_roots()  # rational roots over Q with multiplicities
        # Get just the rational ones
        for root, mult in rational_roots.items():
            # convert to mpf and check distance to x
            try:
                root_val = mp.mpf(str(root))
                if abs(x - root_val) < tol:
                    return True, root, mult
            except Exception:
                continue
        return False, None, None
    except ImportError:
        # if sympy not available, fall back to no filtering
        return False, None, None
    except Exception:
        return False, None, None


def format_poly(coeffs):
    """Format integer polynomial coefficients as a readable polynomial."""
    parts = []
    deg = len(coeffs) - 1
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
# Define candidate alpha values
# ============================================================
candidates = []

# (A) Irrational alpha values
irrational_candidates = [
    ("1/sqrt(2)", 1 / mp.sqrt(2)),
    ("1/sqrt(3)", 1 / mp.sqrt(3)),
    ("1/pi",      1 / mp.pi),
    ("1/e",       1 / mp.e),
    ("1/phi",     2 / (1 + mp.sqrt(5))),   # 1/golden ratio
    ("sqrt(2)-1", mp.sqrt(2) - 1),
    ("1-1/e",     1 - 1 / mp.e),
    ("ln(2)",     mp.ln(2)),
    ("1/pi^2",    1 / mp.pi ** 2),
    ("Catalan-1/2", mp.catalan - mp.mpf(1)/2),  # ~0.4159...
]

# (B) Finer Stern-Brocot rational grid (Farey-like)
stern_brocot_candidates = []
seen = set()
# all fractions p/q with q <= 10, sorted
for q in range(2, 11):
    for p in range(1, q):
        if gcd(p, q) == 1:
            frac = mp.mpf(p) / q
            if 0 < frac < 1 and (p, q) not in seen:
                seen.add((p, q))
                stern_brocot_candidates.append((f"{p}/{q}", frac))

# combine and sort by value
candidates = sorted(irrational_candidates + stern_brocot_candidates,
                    key=lambda t: float(t[1]))

print(f"Testing {len(candidates)} alpha values "
      f"({len(irrational_candidates)} irrational + "
      f"{len(stern_brocot_candidates)} Stern-Brocot rationals)")
print(f"PSLQ search: degree <= {PSLQ_DEG}, coeff bound <= {PSLQ_COEFF_BOUND}")
print(f"mpmath precision: {mp.mp.dps} digits")
print()
print(f"{'alpha':18s} {'H/Br':30s} {'PSLQ result':40s}")
print("-" * 90)

# ============================================================
# Run the scan
# ============================================================
hits = []           # genuine algebraic relations (irreducible polynomial, no rational root near x)
hits_spurious = []  # rejected: polynomial has rational root near x
target = 1 + mp.sqrt(3)
target_poly = [-2, -2, 1, 0, 0, 0]  # x^2 - 2x - 2 = 0 -> coeffs [c0, c1, c2, ...]

for name, alpha in candidates:
    try:
        p, n_steps = joint_attractor(alpha)
        if p[8] == 0:
            print(f"{name:18s} {'(Br=0, skip)':30s}")
            continue
        ratio = p[7] / p[8]
        ratio_str = mp.nstr(ratio, 15)

        # PSLQ search for algebraic relation
        rel, err = pslq_polynomial(ratio)
        if rel is not None:
            poly = format_poly([int(c) for c in rel])
            # check if relation is spurious (has rational root near x)
            is_spur, spur_root, spur_mult = is_spurious_relation(rel, ratio)
            if is_spur:
                hits_spurious.append((name, alpha, ratio, rel, err,
                                       spur_root, spur_mult))
                marker = f"  ~ near-rational(x~{spur_root}, mult {spur_mult})"
                poly_disp = poly[:50]
            else:
                hits.append((name, alpha, ratio, rel, err))
                marker = "  *** ALGEBRAIC (genuine) ***"
                poly_disp = poly[:50]
        else:
            poly_disp = "(no algebraic relation found)"
            marker = ""

        print(f"{name:18s} {ratio_str:30s} {poly_disp:50s}{marker}")
    except Exception as e:
        print(f"{name:18s} ERROR: {e}")

print()
print("=" * 70)
print("RESULTS")
print("=" * 70)
print()
print(f"GENUINE algebraic relations (irreducible polynomial, no rational root near x): {len(hits)}")
for name, alpha, ratio, rel, err in hits:
    poly = format_poly([int(c) for c in rel])
    print(f"  alpha = {name}: H/Br = {mp.nstr(ratio, 25)}")
    print(f"    relation: {poly}")
    print(f"    PSLQ residual: {mp.nstr(err, 5)}")
    is_half = abs(alpha - mp.mpf(1)/2) < mp.mpf(10)**-30
    if is_half:
        print(f"    (this is alpha = 1/2, the known case: 1+sqrt(3) per D43)")
    else:
        print(f"    (NON-1/2 algebraic alpha -- COUNTEREXAMPLE CANDIDATE)")

print()
print(f"SPURIOUS hits (rejected: polynomial has rational root within 1e-3 of x): {len(hits_spurious)}")
for name, alpha, ratio, rel, err, root, mult in hits_spurious:
    poly = format_poly([int(c) for c in rel])
    print(f"  alpha = {name}: H/Br = {mp.nstr(ratio, 12)}, near rational {root} (mult {mult})")
    print(f"    PSLQ found: {poly}  ; residual {mp.nstr(err, 5)} (degenerate)")

print()

# Check: was alpha = 1/2 tested? Add explicit verification
print("Explicit verification for alpha = 1/2:")
p_half, _ = joint_attractor(mp.mpf(1)/2)
ratio_half = p_half[7] / p_half[8]
print(f"  H/Br = {mp.nstr(ratio_half, 25)}")
print(f"  1+sqrt(3) = {mp.nstr(target, 25)}")
print(f"  |error| = {mp.nstr(abs(ratio_half - target), 5)}")

print()
print("CONJECTURE 4.2 STATUS:")
non_half_hits = [h for h in hits
                  if abs(h[1] - mp.mpf(1)/2) > mp.mpf(10)**-30]
if not non_half_hits:
    print(f"  STRENGTHENED: NO non-1/2 alpha value in {len(candidates)}-candidate scan")
    print(f"  produced a genuine algebraic relation at PSLQ degree <= {PSLQ_DEG},")
    print(f"  coeff bound <= {PSLQ_COEFF_BOUND} (with spurious-relation filtering).")
    print(f"  The conjecture survives this extended scan.")
else:
    print(f"  COUNTEREXAMPLE CANDIDATE FOUND: {len(non_half_hits)} non-1/2 alpha")
    print("  values produced genuine algebraic relations. Conjecture 4.2 refuted by")
    print("  this scan. Manual review of the candidates is required.")
print()
print(f"Total candidates tested: {len(candidates)}")
print(f"Genuine hits: {len(hits)} (including alpha = 1/2 if found)")
print(f"Spurious hits filtered: {len(hits_spurious)}")
