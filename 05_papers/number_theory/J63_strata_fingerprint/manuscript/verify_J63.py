"""verify_J63.py -- Independent verification of all four theorems of J63.

Theorem 1: 23/24 Niemeier strata-clean (kissing number)
Theorem 2: 21/24 Niemeier Weyl-strata-clean (with polynomial-vs-factorial mechanism)
Theorem 3: 8/26 sporadic finite simple groups strata-clean
Theorem 4: prime 71 appears in exactly one sporadic order -- the Monster

Runtime: <2 seconds. Dependencies: sympy + math.
"""
import sys
from math import factorial
from functools import reduce
from operator import mul
from sympy import factorint


STRATA = {2, 3, 5, 7, 11, 13}  # Strata I-III primes


def is_strata_clean(N):
    return all(p in STRATA for p in factorint(N))


def extra_primes(N):
    return sorted(p for p in factorint(N) if p not in STRATA)


def W_A(n): return factorial(n + 1)
def W_D(n): return 2**(n - 1) * factorial(n)
W_E6, W_E7, W_E8 = 51840, 2903040, 696729600


def A_roots(n): return n * (n + 1)
def D_roots(n): return 2 * n * (n - 1)
E6_roots, E7_roots, E8_roots = 72, 126, 240


# Niemeier lattices: (label, kissing #, Weyl-component-orders list)
NIEMEIERS = [
    ("Leech",           196560,                  []),
    ("A_1^24",          24 * A_roots(1),         [W_A(1)] * 24),
    ("A_2^12",          12 * A_roots(2),         [W_A(2)] * 12),
    ("A_3^8",           8 * A_roots(3),          [W_A(3)] * 8),
    ("A_4^6",           6 * A_roots(4),          [W_A(4)] * 6),
    ("D_4^6",           6 * D_roots(4),          [W_D(4)] * 6),
    ("A_5^4 D_4",       4 * A_roots(5) + D_roots(4), [W_A(5)] * 4 + [W_D(4)]),
    ("A_6^4",           4 * A_roots(6),          [W_A(6)] * 4),
    ("A_7^2 D_5^2",     2 * A_roots(7) + 2 * D_roots(5), [W_A(7)] * 2 + [W_D(5)] * 2),
    ("A_8^3",           3 * A_roots(8),          [W_A(8)] * 3),
    ("D_6^4",           4 * D_roots(6),          [W_D(6)] * 4),
    ("A_9^2 D_6",       2 * A_roots(9) + D_roots(6), [W_A(9)] * 2 + [W_D(6)]),
    ("E_6^4",           4 * E6_roots,            [W_E6] * 4),
    ("A_11 D_7 E_6",    A_roots(11) + D_roots(7) + E6_roots, [W_A(11), W_D(7), W_E6]),
    ("A_12^2",          2 * A_roots(12),         [W_A(12)] * 2),
    ("D_8^3",           3 * D_roots(8),          [W_D(8)] * 3),
    ("A_15 D_9",        A_roots(15) + D_roots(9), [W_A(15), W_D(9)]),
    ("A_17 E_7",        A_roots(17) + E7_roots,  [W_A(17), W_E7]),
    ("D_10 E_7^2",      D_roots(10) + 2 * E7_roots, [W_D(10), W_E7, W_E7]),
    ("A_24",            A_roots(24),             [W_A(24)]),
    ("D_12^2",          2 * D_roots(12),         [W_D(12)] * 2),
    ("E_8^3",           3 * E8_roots,            [W_E8] * 3),
    ("D_16 E_8",        D_roots(16) + E8_roots,  [W_D(16), W_E8]),
    ("D_24",            D_roots(24),             [W_D(24)]),
]


def theorem_1():
    """Theorem 1: 23/24 Niemeier kissing strata-clean."""
    print("[Theorem 1] Niemeier kissing strata-fingerprint")
    failures = []
    for label, k, _ in NIEMEIERS:
        if not is_strata_clean(k):
            failures.append((label, k, extra_primes(k)))
    print(f"  Total: 24, PASS: {24 - len(failures)}, FAIL: {len(failures)}")
    for label, k, ex in failures:
        print(f"    {label}: kissing {k} has extra primes {ex}")
    assert len(failures) == 1 and failures[0][0] == "D_24", \
        f"Expected only D_24 to fail; got {failures}"
    assert failures[0][2] == [23], f"D_24 should fail with prime 23, got {failures[0][2]}"
    print("  PASS: D_24 is the unique outlier; failure = prime 23 from (n-1)=23.\n")


def theorem_2():
    """Theorem 2: 21/24 Niemeier Weyl strata-clean."""
    print("[Theorem 2] Niemeier Weyl group strata-fingerprint")
    print("  Mechanism: |W(A_n)| = (n+1)!, |W(D_n)| = 2^(n-1) * n!")
    print("  Factorials accumulate ALL primes <= n; kissing polynomial only its specific factors.")
    weyl_failures = []
    for label, _, w_comps in NIEMEIERS:
        if not w_comps:
            continue  # Leech: no Weyl content from roots
        w = reduce(mul, w_comps, 1)
        if not is_strata_clean(w):
            weyl_failures.append((label, w, extra_primes(w)))
    print(f"  Total non-Leech: 23, Weyl-PASS: {23 - len(weyl_failures)}, Weyl-FAIL: {len(weyl_failures)}")
    for label, _, ex in weyl_failures:
        print(f"    {label}: extra Weyl primes {ex}")
    expected = {("A_17 E_7", (17,)),
                ("A_24", (17, 19, 23)),
                ("D_24", (17, 19, 23))}
    actual = {(lbl, tuple(ex)) for lbl, _, ex in weyl_failures}
    assert actual == expected, f"Expected {expected}, got {actual}"
    print("  PASS: exactly A_17 E_7, A_24, D_24 fail Weyl strata.")
    print("  Mechanism: each contains a factorial of n >= 17, picking up 17 (and 19, 23 at n>=23).\n")


def theorem_3():
    """Theorem 3: 8/26 sporadics strata-clean."""
    SPORADICS = {
        "M_11": 7920, "M_12": 95040, "M_22": 443520,
        "M_23": 10200960, "M_24": 244823040,
        "J_1": 175560, "J_2": 604800, "J_3": 50232960,
        "J_4": 86775571046077562880,
        "HS": 44352000, "McL": 898128000, "Suz": 448345497600,
        "He": 4030387200, "Ru": 145926144000,
        "Co_1": 4157776806543360000, "Co_2": 42305421312000, "Co_3": 495766656000,
        "Fi_22": 64561751654400, "Fi_23": 4089470473293004800,
        "Fi_24'": 1255205709190661721292800,
        "HN": 273030912000000, "Ly": 51765179004000000,
        "Th": 90745943887872000, "O'N": 460815505920,
        "B": 4154781481226426191177580544000000,
        "M": 808017424794512875886459904961710757005754368000000000,
    }
    print("[Theorem 3] Sporadic finite simple group strata-fingerprint")
    passing = []
    for label, order in SPORADICS.items():
        if is_strata_clean(order):
            passing.append(label)
    expected_pass = {"M_11", "M_12", "M_22", "J_2", "HS", "McL", "Suz", "Fi_22"}
    assert set(passing) == expected_pass, f"Expected {expected_pass}, got {set(passing)}"
    print(f"  PASS: {len(passing)} of 26 sporadics ({sorted(passing)})")
    # Boundary analysis: how many fail due to 23?
    fails_with_23 = [s for s, o in SPORADICS.items() if 23 in factorint(o) and s not in expected_pass]
    print(f"  Of the 18 failures, {len(fails_with_23)} contain prime 23")
    print(f"  This is the natural Mathieu/Conway-Leech cutoff boundary.\n")


def theorem_4():
    """Theorem 4: prime 71 appears in exactly one sporadic -- the Monster.

    Conway-Norton 1979 anchor: 71 is the largest supersingular prime,
    i.e., the largest p for which X_0(p) has genus 0 (Hauptmodul exists).
    The Monster's prime divisors are exactly the 15 supersingular primes.
    So '71 in M only' is the upper boundary of the genus-0 spectrum,
    not a cardinality effect.
    """
    SPORADIC_ORDERS = {
        "M_11": 7920, "M_12": 95040, "M_22": 443520,
        "M_23": 10200960, "M_24": 244823040,
        "J_1": 175560, "J_2": 604800, "J_3": 50232960,
        "J_4": 86775571046077562880,
        "HS": 44352000, "McL": 898128000, "Suz": 448345497600,
        "He": 4030387200, "Ru": 145926144000,
        "Co_1": 4157776806543360000, "Co_2": 42305421312000, "Co_3": 495766656000,
        "Fi_22": 64561751654400, "Fi_23": 4089470473293004800,
        "Fi_24'": 1255205709190661721292800,
        "HN": 273030912000000, "Ly": 51765179004000000,
        "Th": 90745943887872000, "O'N": 460815505920,
        "B": 4154781481226426191177580544000000,
        "M": 808017424794512875886459904961710757005754368000000000,
    }
    print("[Theorem 4] Stratum IV: prime 71 in exactly one sporadic")
    with_71 = [s for s, o in SPORADIC_ORDERS.items() if 71 in factorint(o)]
    print(f"  Sporadics containing 71: {with_71}")
    assert with_71 == ["M"], f"Expected only Monster; got {with_71}"
    # Verify it's actually in the Monster's order
    M_order = SPORADIC_ORDERS["M"]
    M_factors = factorint(M_order)
    assert 71 in M_factors
    print(f"  PASS: 71 appears in the Monster's order with exponent {M_factors[71]}.")
    print(f"  This validates TIG's Stratum IV designation for prime 71.\n")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        try: sys.stdout.reconfigure(encoding="utf-8")
        except: pass
    print("=== J63 verification ===\n")
    theorem_1()
    theorem_2()
    theorem_3()
    theorem_4()
    print("=" * 60)
    print("  All four theorems PASS at machine precision.")
    print("  Theorem 1 (kissing strata): 23/24, only D_24 fails.")
    print("  Theorem 2 (Weyl strata):    21/24, A_17 E_7 + A_24 + D_24 fail.")
    print("  Theorem 3 (sporadic):       8/26 pass.")
    print("  Theorem 4 (Monster 71):     unique sporadic with 71.")
    print("=" * 60)


if __name__ == "__main__":
    main()
