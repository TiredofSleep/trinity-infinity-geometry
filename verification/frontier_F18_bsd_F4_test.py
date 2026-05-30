#!/usr/bin/env python3
"""
Frontier F18 -- BSD bridge with F4 closed forms.

CONTEXT:
  F16 closed F4 -> Yang-Mills (NO-TRACTION) and recommended F4 -> BSD as
  the next candidate. F4's two closed forms on V^BHML over F_p are:
    (A) |idem(V^BHML / F_p)| = p + 3       (odd p, 24 primes verified)
    (B) |Aut(V^BHML / F_p)| = (p - 1)^2     (group is F_p* x F_p*)

  The BSD conjecture for an elliptic curve E/Q ties together:
    - rank E(Q),
    - ord_{s=1} L(E, s),
    - and at each prime p of good reduction the point-count
      #E(F_p) = p + 1 - a_p   with |a_p| <= 2 sqrt(p) (Hasse-Weil).

  ANGLES TO TEST WITH F4 DATA:

    (i)   Structural rhyme F_p* x F_p* vs E(F_p)[p] ~= Z/p x Z/p
          (the latter occurs in supersingular reduction).

    (ii)  Does (p+3) match #E(F_p) at any specific curve E and prime p?
          (p+3) is the point count whose a_p value is -2 (since
           p + 1 - a_p = p + 3  =>  a_p = -2).

    (iii) Does (p-1)^2 match #E(F_p) at any specific curve E and prime p?
          (p-1)^2 = p^2 - 2p + 1, so a_p = p + 1 - (p-1)^2 = -p^2 + 3p
                 = -p(p-3), which has |a_p| = p(p-3).
          For p >= 5 this VIOLATES Hasse: 2 sqrt(p) < p(p-3) for p >= 5.
          So (p-1)^2 is NOT achievable as #E(F_p) for any elliptic curve
          at any prime p >= 5.  (At p=3, (p-1)^2 = 4 needs a_p = 0;
          at p=2, (p-1)^2 = 1, needs a_p = 2 -- inside Hasse |a_p|<=2.83.)

    (iv)  Substrate primes {3, 7, 11, 13}: do small-conductor E's over Q
          have any distinguished a_p behavior at these primes?

    (v)   "p + 3" occurrence frequency: how often does a_p(E) = -2 occur
          at substrate primes, across the LMFDB curves with conductor
          dividing 30?

GOAL: bounded scoping. Either find a striking pattern (curve E with
#E(F_p) = p + 3 at multiple substrate primes; or supersingular at the
substrate primes; or some structural rhyme that suggests a curve-to-
corridor map for BSD.1) -- or report NO-TRACTION cleanly.

CURVES TESTED (small-conductor Cremona):
  11a1: y^2 + y = x^3 - x^2 - 10x - 20    (conductor 11, rank 0)
  14a1: y^2 + xy + y = x^3 + 4x - 6        (conductor 14, rank 0)
  15a1: y^2 + xy + y = x^3 + x^2 - 10x - 10 (conductor 15, rank 0)
  17a1: y^2 + xy + y = x^3 - x^2 - x - 14   (conductor 17, rank 0)
  19a1: y^2 + y = x^3 + x^2 - 9x - 15       (conductor 19, rank 0)
  21a1: y^2 + xy = x^3 - 4x - 1             (conductor 21, rank 0)
  26a1: y^2 + xy + y = x^3 - 5x - 8         (conductor 26, rank 0)
  37a1: y^2 + y = x^3 - x                   (conductor 37, rank 1!)
  43a1: y^2 + y = x^3 + x^2                 (conductor 43, rank 1)
  389a1: y^2 + y = x^3 + x^2 - 2x           (conductor 389, rank 2)
  X0(11) congruence: 11a3 is X_0(11), CM-like via Atkin-Lehner.
  (CM-by-Q(sqrt(-7)) example: y^2 = x^3 - 1715x + 33614, conductor 49)

DEPS: stdlib only.  Naive O(p) point-count via brute enumeration.

Runtime: ~30 seconds for primes <= 100 across all curves.
"""
from __future__ import annotations
import sys
from typing import Iterable

# ----------------------------------------------------------------------
# Small-conductor elliptic curves (Cremona labels).
# Given as (a1, a2, a3, a4, a6) for general Weierstrass form
#   y^2 + a1 x y + a3 y = x^3 + a2 x^2 + a4 x + a6
# Conductors and ranks from LMFDB.
# ----------------------------------------------------------------------
CURVES = [
    # label, (a1, a2, a3, a4, a6), conductor, rank
    ("11a1",  (0, -1, 1, -10, -20),       11, 0),
    ("11a2",  (0, -1, 1, -7820, -263580), 11, 0),
    ("11a3",  (0, -1, 1, 0, 0),           11, 0),   # X_0(11)
    ("14a1",  (1, 0, 1, 4, -6),           14, 0),
    ("15a1",  (1, 1, 1, -10, -10),        15, 0),
    ("17a1",  (1, -1, 1, -1, -14),        17, 0),
    ("19a1",  (0, 1, 1, -9, -15),         19, 0),
    ("21a1",  (1, 0, 0, -4, -1),          21, 0),
    ("26a1",  (1, 0, 1, -5, -8),          26, 0),
    ("26b1",  (1, -1, 1, -3, 3),          26, 0),
    ("27a1",  (0, 0, 1, 0, -7),           27, 0),   # CM by Z[zeta_3]
    ("32a1",  (0, 0, 0, 4, 0),            32, 0),   # CM by Z[i]
    ("36a1",  (0, 0, 0, 0, 1),            36, 0),   # CM by Z[zeta_3]
    ("37a1",  (0, 0, 1, -1, 0),           37, 1),   # rank 1!
    ("37b1",  (0, 1, 1, -23, -50),        37, 0),
    ("43a1",  (0, 1, 1, 0, 0),            43, 1),   # rank 1
    ("389a1", (0, 1, 1, -2, 0),           389, 2),  # rank 2
    ("49a1",  (1, -1, 0, -2, -1),         49, 0),   # CM by Q(sqrt(-7))!
    ("49a2",  (1, -1, 0, -107, 552),      49, 0),
    # Substrate-prime curves:
    ("121a1", (1, 0, 0, -30, -76),       121, 0),   # conductor 11^2
    ("169a1", (0, 0, 0, -1, 0),          169, 0),   # CM by Q(sqrt(-13)); cond 13^2
    ("169b1", (1, 1, 0, -4, 1),          169, 0),
]


def reduce_curve_F_p(a1, a2, a3, a4, a6, p):
    """Reduce a Weierstrass curve modulo p and return (a1', ..., a6') mod p."""
    return (a1 % p, a2 % p, a3 % p, a4 % p, a6 % p)


def is_singular_at_p(a1, a2, a3, a4, a6, p):
    """Return True iff E has bad reduction at p (singular curve over F_p).
    Test: the discriminant Delta mod p == 0."""
    # Standard discriminant formula for y^2 + a1 xy + a3 y = x^3 + a2 x^2 + a4 x + a6:
    #   b2 = a1^2 + 4 a2
    #   b4 = 2 a4 + a1 a3
    #   b6 = a3^2 + 4 a6
    #   b8 = a1^2 a6 - a1 a3 a4 + 4 a2 a6 + a2 a3^2 - a4^2
    #   c4 = b2^2 - 24 b4
    #   c6 = -b2^3 + 36 b2 b4 - 216 b6
    #   Delta = -b2^2 b8 - 8 b4^3 - 27 b6^2 + 9 b2 b4 b6
    b2 = a1 * a1 + 4 * a2
    b4 = 2 * a4 + a1 * a3
    b6 = a3 * a3 + 4 * a6
    b8 = a1 * a1 * a6 - a1 * a3 * a4 + 4 * a2 * a6 + a2 * a3 * a3 - a4 * a4
    delta = -b2 * b2 * b8 - 8 * b4 ** 3 - 27 * b6 * b6 + 9 * b2 * b4 * b6
    return (delta % p) == 0


def count_points_naive(a1, a2, a3, a4, a6, p):
    """Count points #E(F_p) by brute enumeration of (x, y) in F_p^2.
    Includes the point at infinity.  O(p^2) -- fine for p <= 100."""
    if p == 2:
        # Specialized: just brute force.
        count = 1  # point at infinity
        for x in range(2):
            for y in range(2):
                lhs = (y * y + a1 * x * y + a3 * y) % 2
                rhs = (x ** 3 + a2 * x * x + a4 * x + a6) % 2
                if lhs == rhs:
                    count += 1
        return count
    count = 1  # point at infinity
    for x in range(p):
        for y in range(p):
            lhs = (y * y + a1 * x * y + a3 * y) % p
            rhs = (x ** 3 + a2 * x * x + a4 * x + a6) % p
            if lhs == rhs:
                count += 1
    return count


def hasse_check(num_points, p):
    """Compute a_p and check Hasse bound |a_p| <= 2 sqrt(p)."""
    a_p = p + 1 - num_points
    bound = 2 * (p ** 0.5)
    return a_p, abs(a_p) <= bound + 1e-9


# ----------------------------------------------------------------------
# F4 prediction comparators
# ----------------------------------------------------------------------
def predicted_p_plus_3(p):
    return p + 3


def predicted_pminus1_sq(p):
    return (p - 1) ** 2


# ----------------------------------------------------------------------
# Main test driver
# ----------------------------------------------------------------------

def run_all():
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
              59, 61, 67, 71, 73, 79, 83, 89, 97]

    # Show explicit Hasse-impossibility of (p-1)^2:
    print("=" * 78)
    print("F18 -- BSD bridge with F4 closed forms")
    print("=" * 78)
    print()
    print("[STEP 0]  Hasse-Weil viability check for F4 predictions")
    print("-" * 78)
    print(f"{'p':>4} {'(p+3)':>8} {'a_p needed':>12} {'|a_p|<=2sqrt p':>16} "
          f"{'(p-1)^2':>10} {'a_p needed':>14} {'Hasse OK?':>10}")
    for p in primes[:8]:
        pp3 = predicted_p_plus_3(p)
        a_p_pp3 = p + 1 - pp3   # = -2 always
        pm1sq = predicted_pminus1_sq(p)
        a_p_pm1sq = p + 1 - pm1sq
        bound = 2 * (p ** 0.5)
        ok_pp3 = abs(a_p_pp3) <= bound + 1e-9
        ok_pm1sq = abs(a_p_pm1sq) <= bound + 1e-9
        print(f"{p:>4} {pp3:>8} {a_p_pp3:>+12d} {'OK' if ok_pp3 else 'NO':>16} "
              f"{pm1sq:>10} {a_p_pm1sq:>+14d} {'OK' if ok_pm1sq else 'IMPOSS':>10}")
    print()
    print("VERDICT step 0: (p-1)^2 violates Hasse-Weil for p >= 5,")
    print("                so NO elliptic curve over Q can have #E(F_p) = (p-1)^2 at any p >= 5.")
    print("                Only p+3 (= a_p = -2) is achievable at any prime.")
    print()

    # ------------------------------------------------------------------
    # Main scan: for each curve, compute #E(F_p) for each prime of good
    # reduction, compare to p+3, and tabulate.
    # ------------------------------------------------------------------
    print("=" * 78)
    print("[STEP 1]  Curve-by-curve a_p computation and (p+3) match check")
    print("-" * 78)

    pp3_match_count = {}   # curve_label -> list of primes where #E = p+3
    pm1sq_match_count = {} # curve_label -> list of primes where #E = (p-1)^2
    pp3_at_substrate = {}  # primes where match occurs at substrate primes {3,7,11,13}
    supersingular = {}     # primes where a_p = 0 mod p (supersingular)

    SUBSTRATE_PRIMES = {3, 7, 11, 13}

    for label, coeffs, conductor, rank in CURVES:
        a1, a2, a3, a4, a6 = coeffs
        pp3_match_count[label] = []
        pm1sq_match_count[label] = []
        pp3_at_substrate[label] = []
        supersingular[label] = []
        for p in primes:
            if conductor % p == 0 or is_singular_at_p(a1, a2, a3, a4, a6, p):
                continue
            n = count_points_naive(a1, a2, a3, a4, a6, p)
            a_p, ok = hasse_check(n, p)
            if not ok:
                print(f"  WARNING: Hasse violated for {label} at p={p}: a_p={a_p}")
            if n == predicted_p_plus_3(p):
                pp3_match_count[label].append(p)
                if p in SUBSTRATE_PRIMES:
                    pp3_at_substrate[label].append(p)
            if n == predicted_pminus1_sq(p):
                pm1sq_match_count[label].append(p)
            if a_p % p == 0:
                supersingular[label].append(p)

    print()
    print("[STEP 2]  Match summary table")
    print("-" * 78)
    print(f"{'curve':>10} {'cond':>6} {'rank':>5} "
          f"{'# p+3 hits':>11} {'p+3 at sub p':>14} {'(p-1)^2':>9} {'supersing p':>12}")
    print("-" * 78)
    for label, coeffs, conductor, rank in CURVES:
        n_pp3 = len(pp3_match_count[label])
        substrate_hits = pp3_at_substrate[label]
        n_pm1sq = len(pm1sq_match_count[label])
        n_ss = len(supersingular[label])
        substr_str = ",".join(map(str, substrate_hits)) if substrate_hits else "-"
        print(f"{label:>10} {conductor:>6} {rank:>5} "
              f"{n_pp3:>11} {substr_str:>14} {n_pm1sq:>9} {n_ss:>12}")

    # ------------------------------------------------------------------
    # Step 3: Substrate-prime analysis
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("[STEP 3]  Substrate-prime a_p distribution across curves")
    print("=" * 78)
    print(f"{'p':>4} ", end="")
    for label, _, _, _ in CURVES:
        print(f"{label:>7}", end="")
    print()
    print("-" * (4 + 7 * len(CURVES)))
    for p in [3, 5, 7, 11, 13, 17, 19, 23]:
        print(f"{p:>4} ", end="")
        for label, coeffs, conductor, rank in CURVES:
            a1, a2, a3, a4, a6 = coeffs
            if conductor % p == 0 or is_singular_at_p(a1, a2, a3, a4, a6, p):
                print(f"{'bad':>7}", end="")
                continue
            n = count_points_naive(a1, a2, a3, a4, a6, p)
            a_p = p + 1 - n
            print(f"{a_p:>+7d}", end="")
        print()

    print()
    print("(rows are primes; entries are a_p; 'bad' = bad reduction)")
    print()
    print("Look for curves with a_p = -2 (= n=p+3 match):")
    for label, coeffs, conductor, rank in CURVES:
        if len(pp3_match_count[label]) >= 2:
            print(f"  {label}: a_p = -2 at primes {pp3_match_count[label]}")

    # ------------------------------------------------------------------
    # Step 4: count curves with a_p = -2 at substrate primes
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("[STEP 4]  Substrate-prime concentration of a_p = -2")
    print("=" * 78)
    substrate_concentration = {}
    for label, coeffs, conductor, rank in CURVES:
        a1, a2, a3, a4, a6 = coeffs
        hits = []
        for p in (3, 7, 11, 13):
            if conductor % p == 0 or is_singular_at_p(a1, a2, a3, a4, a6, p):
                continue
            n = count_points_naive(a1, a2, a3, a4, a6, p)
            a_p = p + 1 - n
            if a_p == -2:
                hits.append(p)
        substrate_concentration[label] = hits
    print(f"{'curve':>10} {'cond':>6} {'rank':>5} {'a_p=-2 at substrate p':>30}")
    for label, hits in substrate_concentration.items():
        cond = next(c for L, _, c, _ in CURVES if L == label)
        rk = next(r for L, _, _, r in CURVES if L == label)
        h = ",".join(map(str, hits)) if hits else "(none)"
        print(f"{label:>10} {cond:>6} {rk:>5} {h:>30}")

    # ------------------------------------------------------------------
    # Step 5: explicit (p-1)^2 check at p=2,3 only (where it's possible)
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("[STEP 5]  (p-1)^2 check at p in {2, 3} (only achievable primes)")
    print("=" * 78)
    print(f"  at p=3: (p-1)^2 = 4. Need a_p = 3+1-4 = 0. (supersingular at 3)")
    print(f"  at p=2: (p-1)^2 = 1. Need a_p = 2+1-1 = 2.")
    print()
    print(f"{'curve':>10} {'cond':>6} {'#E(F_2)':>10} {'#E(F_3)':>10} "
          f"{'==(p-1)^2 at p=2':>18} {'==(p-1)^2 at p=3':>18}")
    for label, coeffs, conductor, rank in CURVES:
        a1, a2, a3, a4, a6 = coeffs
        cells = []
        for p in (2, 3):
            if conductor % p == 0 or is_singular_at_p(a1, a2, a3, a4, a6, p):
                cells.append("bad")
            else:
                n = count_points_naive(a1, a2, a3, a4, a6, p)
                cells.append(str(n))
        m2 = (cells[0] == "1")
        m3 = (cells[1] == "4")
        print(f"{label:>10} {conductor:>6} {cells[0]:>10} {cells[1]:>10} "
              f"{'YES' if m2 else 'no':>18} {'YES' if m3 else 'no':>18}")

    # ------------------------------------------------------------------
    # Step 6: distinguished substrate prime check
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("[STEP 6]  Are substrate primes {3, 7, 11, 13} distinguished in")
    print("          a_p distribution across rank-0 vs rank-1 curves?")
    print("=" * 78)
    rank0_aps_substrate = []
    rank1_aps_substrate = []
    for label, coeffs, conductor, rank in CURVES:
        a1, a2, a3, a4, a6 = coeffs
        for p in (3, 7, 11, 13):
            if conductor % p == 0 or is_singular_at_p(a1, a2, a3, a4, a6, p):
                continue
            n = count_points_naive(a1, a2, a3, a4, a6, p)
            a_p = p + 1 - n
            if rank == 0:
                rank0_aps_substrate.append((label, p, a_p))
            elif rank == 1:
                rank1_aps_substrate.append((label, p, a_p))
    print(f"  rank-0 a_p values at substrate primes (n={len(rank0_aps_substrate)}):")
    aps0 = [t[2] for t in rank0_aps_substrate]
    if aps0:
        print(f"    mean = {sum(aps0)/len(aps0):.3f}, "
              f"var = {sum((x - sum(aps0)/len(aps0))**2 for x in aps0)/len(aps0):.3f}")
        from collections import Counter
        print(f"    distribution: {dict(Counter(aps0))}")
    print(f"  rank-1 a_p values at substrate primes (n={len(rank1_aps_substrate)}):")
    aps1 = [t[2] for t in rank1_aps_substrate]
    if aps1:
        print(f"    mean = {sum(aps1)/len(aps1):.3f}, "
              f"var = {sum((x - sum(aps1)/len(aps1))**2 for x in aps1)/len(aps1):.3f}")
        from collections import Counter
        print(f"    distribution: {dict(Counter(aps1))}")

    # ------------------------------------------------------------------
    # Verdict
    # ------------------------------------------------------------------
    print()
    print("=" * 78)
    print("[VERDICT]")
    print("=" * 78)
    total_pp3_substrate_hits = sum(len(v) for v in pp3_at_substrate.values())
    total_pm1sq_hits = sum(len(v) for v in pm1sq_match_count.values())
    n_curves_with_2plus_pp3 = sum(1 for v in pp3_match_count.values() if len(v) >= 2)
    n_curves_pp3_substr = sum(1 for v in pp3_at_substrate.values() if len(v) >= 1)
    print(f"  Total p+3 matches at substrate primes (across all {len(CURVES)} curves): "
          f"{total_pp3_substrate_hits}")
    print(f"  Total (p-1)^2 matches at any prime: {total_pm1sq_hits}")
    print(f"  Curves with >=2 (p+3) matches at any prime in {primes}: "
          f"{n_curves_with_2plus_pp3}")
    print(f"  Curves with >=1 (p+3) match at a substrate prime: {n_curves_pp3_substr}")
    print()
    # Sato-Tate baseline check: for non-CM curves, P(a_p = -2) per prime is
    #   (2/pi) sqrt(1 - 1/p) / (2 sqrt(p)).
    # Expected substrate-prime fraction of (p+3) hits:
    import math
    expected_total_per_curve = 0.0
    expected_sub_per_curve = 0.0
    for p in primes:
        x = -1.0 / math.sqrt(p)
        density = (2 / math.pi) * math.sqrt(1 - x * x)
        prob = density / (2 * math.sqrt(p))
        expected_total_per_curve += prob
        if p in SUBSTRATE_PRIMES:
            expected_sub_per_curve += prob
    expected_sub_fraction = expected_sub_per_curve / expected_total_per_curve
    observed_sub_fraction = (total_pp3_substrate_hits /
                              max(sum(len(v) for v in pp3_match_count.values()), 1))
    print(f"  Sato-Tate predicted substrate fraction of (p+3) hits: {expected_sub_fraction:.2%}")
    print(f"  Observed substrate fraction of (p+3) hits: {observed_sub_fraction:.2%}")
    print()
    if abs(observed_sub_fraction - expected_sub_fraction) < 0.10:
        print("  >>> NO-TRACTION <<<")
        print("  Observed substrate-prime fraction matches Sato-Tate baseline")
        print("  within ~1-10 percentage points. Apparent substrate enrichment")
        print("  is entirely explained by the small-prime weighting of the")
        print("  Sato-Tate measure (smaller p gives higher density at a_p = -2).")
        print("  F4 closed forms do NOT distinguish substrate primes in BSD a_p data.")
    elif observed_sub_fraction > expected_sub_fraction + 0.10:
        print("  >>> POTENTIAL TRACTION <<<")
        print("  Observed substrate fraction exceeds Sato-Tate baseline by >10pp.")
        print("  Worth deeper investigation.")
    else:
        print("  NEGATIVE: observed substrate fraction BELOW Sato-Tate baseline.")
    print()
    print("  Hasse-Weil note: (p-1)^2 is IMPOSSIBLE as #E(F_p) for any elliptic")
    print("  curve over Q at any prime p >= 5 (forces |a_p| > 2 sqrt(p)).")
    print("  This is the DECISIVE non-traction result.")


if __name__ == "__main__":
    run_all()
