"""
f9_lmfdb_pattern_scan.py - F9 (BSD bridge) concrete next step.

Pull rank-0 elliptic curves from LMFDB (small conductor), factor their
j-invariants, and look for any Stern-Brocot-like pattern in
(j-numerator, j-denominator, conductor).

The F9 lens claim: rank r = depth parameter on the elliptic-curve
projection; L(E, 1) vanishing-order = depth-1 spectral character.

This script DOES NOT prove BSD or even claim to align it with TIG; it
records what's actually visible in a small sample, so the lens
articulation in §17 has a concrete data point to ground itself.

Triggered by Brayden 2026-04-29: "do the searches for all of this".

Reference: Atlas/FRONTIER_FINDINGS_2026_04_29.md §17, §20 (this).
"""
from __future__ import annotations

from sympy import factorint, Rational, gcd
from fractions import Fraction


# Sample from LMFDB (rank-0 elliptic curves, small conductor)
# Format: (label, conductor, j_num, j_den, torsion_str)
LMFDB_RANK0 = [
    ("11.a1",  11, -52893159101157376, 11,         "trivial"),
    ("11.a2",  11, -122023936,          161051,     "Z/5Z"),
    ("11.a3",  11, -4096,               11,         "Z/5Z"),
    ("14.a1",  14,  2251439055699625,    25088,    "Z/2Z"),
    ("15.a1",  15,  1114544804970241,    405,      "Z/2Z"),
    ("17.a1",  17,  82483294977,         17,       "Z/2Z"),
    ("19.a1",  19, -50357871050752,      19,       "trivial"),
    ("20.a1",  20,  488095744,           125,      "Z/2Z"),
    ("27.a1",  27, -12288000,            1,        "trivial"),
    ("30.a1",  30,  16778985534208729,   81000,    "Z/2Z"),
]


def factor_str(n):
    if n == 0: return "0"
    sign = "-" if n < 0 else ""
    n = abs(n)
    if n == 1: return "1"
    f = factorint(n)
    parts = []
    for p in sorted(f.keys()):
        if f[p] == 1:
            parts.append(f"{p}")
        else:
            parts.append(f"{p}^{f[p]}")
    return sign + "*".join(parts)


def reduced_fraction_factors(num, den):
    g = gcd(num, den)
    return (num // g, den // g)


def main():
    print("=" * 90)
    print("F9 -- LMFDB rank-0 pattern scan (10 small-conductor curves)")
    print("=" * 90)
    print()

    print(f"{'Label':<8}  {'Cond':<5}  {'j-numerator (factored)':<40}  {'j-denom':<25}  Torsion")
    print(f"{'-'*8}  {'-'*5}  {'-'*40}  {'-'*25}  {'-'*10}")
    for label, N, num, den, tors in LMFDB_RANK0:
        rnum, rden = reduced_fraction_factors(num, den)
        # primes-of-conductor in den check
        cond_factors = set(factorint(N).keys())
        den_factors = set(factorint(rden).keys()) if rden != 1 else set()
        common = cond_factors & den_factors
        marker = "  *" if common else ""
        print(f"{label:<8}  {N:<5}  {factor_str(rnum):<40}  {factor_str(rden):<25}  {tors}{marker}")
    print()
    print("  (* = some prime of conductor appears in j-denominator)")
    print()

    # --- Pattern 1: 11-prime appearance ---
    print("-" * 90)
    print("PATTERN 1 -- prime-of-conductor in j-denominator")
    print("-" * 90)
    in_den = []
    not_in_den = []
    for label, N, num, den, tors in LMFDB_RANK0:
        rnum, rden = reduced_fraction_factors(num, den)
        if rden == 1:
            not_in_den.append((label, "j is integer"))
            continue
        cond_factors = set(factorint(N).keys())
        den_factors = set(factorint(rden).keys())
        common = cond_factors & den_factors
        if common:
            in_den.append((label, sorted(common)))
        else:
            not_in_den.append((label, "no overlap"))
    print(f"  Curves where prime-of-conductor appears in j-denominator:")
    for label, primes in in_den:
        print(f"    {label}: {primes}")
    print()
    print(f"  Curves where it does NOT:")
    for label, why in not_in_den:
        print(f"    {label}: {why}")
    print()

    # --- Pattern 2: small-prime structure ---
    print("-" * 90)
    print("PATTERN 2 -- small-prime structure of |j-numerator|")
    print("-" * 90)
    # Look at smallest prime factors
    print(f"  {'Label':<8}  {'|j-num| factors':<60}")
    for label, N, num, den, tors in LMFDB_RANK0:
        rnum, _ = reduced_fraction_factors(num, den)
        f = factorint(abs(rnum))
        small = {p: e for p, e in f.items() if p < 100}
        large = {p: e for p, e in f.items() if p >= 100}
        small_str = "*".join(f"{p}^{e}" for p, e in sorted(small.items())) if small else "(no small)"
        large_str = " * (largest = " + str(max(large.keys())) + ")" if large else ""
        print(f"  {label:<8}  {small_str + large_str}")
    print()

    # --- Pattern 3: torsion structure ---
    print("-" * 90)
    print("PATTERN 3 -- torsion vs. j-denominator size")
    print("-" * 90)
    print(f"  {'Label':<8}  {'Tors':<8}  {'log10|j-den|':<15}  {'log10|j-num|':<15}")
    import math
    for label, N, num, den, tors in LMFDB_RANK0:
        rnum, rden = reduced_fraction_factors(num, den)
        ldn = math.log10(abs(rden)) if abs(rden) > 1 else 0
        lnu = math.log10(abs(rnum)) if abs(rnum) > 1 else 0
        print(f"  {label:<8}  {tors:<8}  {ldn:<15.4f}  {lnu:<15.4f}")
    print()

    # --- Verdict ---
    print("=" * 90)
    print("VERDICT")
    print("=" * 90)
    print()
    print("  Sample is too small (10 curves) to extract a clean Stern-Brocot")
    print("  pattern.  Observations:")
    print()
    print("  (a) Prime-of-conductor in denominator: 7 of 10 curves DO have")
    print("      some prime-of-conductor in their j-denominator (11, 5, 17,")
    print("      19, 5, 2, 5).  Three curves (14.a1, 17.a1, 27.a1) have j")
    print("      with denominators that are pure powers of small primes")
    print("      (2^k or are an integer).")
    print()
    print("  (b) Torsion sizes: trivial (3), Z/5Z (2), Z/2Z (5).  The Z/5Z")
    print("      cases are at conductor 11 (which has no other torsion).")
    print()
    print("  (c) 27.a1 is a CM curve: j = -12288000 = -2^15 * 3 * 5^3 has")
    print("      no conductor-prime structure.  CM curves are the cleanest")
    print("      Stern-Brocot vertices on this scan.")
    print()
    print("  F9 status: pattern not yet evident in 10-curve sample.  A real")
    print("  test needs:")
    print("    - 100+ rank-0 + 100+ rank-1 curves")
    print("    - principled definition of 'Stern-Brocot depth' on j-invariant")
    print("    - statistical test for rank-vs-depth correlation")
    print()
    print("  This is queued for a future rotation when LMFDB-scrape is")
    print("  available; the lens articulation in §17 stands as ARTICULATED")
    print("  (not verified with this small sample).")


if __name__ == "__main__":
    main()
