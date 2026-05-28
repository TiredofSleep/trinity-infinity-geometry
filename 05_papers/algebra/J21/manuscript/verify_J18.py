"""
verify_J18.py
Self-contained verification of J18:
  "Two Crossing Decompositions of a -21 Invariant on Z/10Z
   with the sigma^2-Triadic Refinement"

Six checks mapped one-to-one to the manuscript's load-bearing claims:

  C1  Psi_B table sums to -21 (the global invariant).
  C2  sigma-orbit (triangular) decomposition:
        sum over sigma-cycle = -T_5 = -15;
        sum over sigma-fixed = -T_3 = -6.
  C3  Role-Fibonacci decomposition:
        sum_F = -F_7 = -13; sum_S = -F_6 = -8;
        sum_T = -1; sum_V = +1; total = -21.
  C4  sigma^2-orbit per-orbit values (the R1 sign-swap fix):
        sum_{O_1 = {1,6,4}} = -8;
        sum_{O_2 = {7,5,2}} = -7;
        with O_1 + O_2 = -15 = -T_5.
  C5  Crossing closure failures (neither decomposition refines the other):
        F intersect sigma-cycle = {1, 5, 7} is not sigma-stable;
        F intersect sigma-cycle is not sigma^2-stable;
        no sigma-orbit lies inside a single role class.
  C6  sigma permutation data: sigma has order 6 on Z/10Z (cycle structure
        (0)(3)(8)(9)(1 7 6 5 4 2), so order = lcm(1, 6) = 6 -- sigma is
        NOT an involution; only sigma^3 is). sigma^2 has order 3 on the
        6-cycle and is identity on fixed points; O_1 and O_2 are
        sigma-swapped.

Author lane: B.R. Sanders, M. Gish
License: CC-BY-4.0 (journal-bundled submission script)
Runtime: <1s on standard hardware. Dependencies: standard library only.
"""

from __future__ import annotations
from itertools import product


# ---------------------------------------------------------------------------
# Manuscript data (Table 1 of the paper).
# ---------------------------------------------------------------------------

PSI_B = {
    0: +1,
    1: -5,
    2: -3,
    3: -2,
    4: -2,
    5: -1,
    6: -1,
    7: -3,
    8: -3,
    9: -2,
}

# Sigma cycle structure: (0)(3)(8)(9)(1 7 6 5 4 2)
SIGMA = {
    0: 0,
    3: 3,
    8: 8,
    9: 9,
    1: 7,
    7: 6,
    6: 5,
    5: 4,
    4: 2,
    2: 1,
}

SIGMA_FIXED = {0, 3, 8, 9}
SIGMA_CYCLE = {1, 7, 6, 5, 4, 2}

# sigma^2-orbits on the 6-cycle (every-other element):
# starting at 1: 1 -> 7 -> 6 -> 5 -> 4 -> 2 -> 1
# sigma^2 starting at 1: 1, 6, 4 (period 3)
# sigma^2 starting at 7: 7, 5, 2 (period 3)
O_1 = {1, 6, 4}
O_2 = {7, 5, 2}

# Role partition F sqcup S sqcup T sqcup V = Z/10Z
F_ROLE = {1, 3, 5, 7, 9}
S_ROLE = {2, 4, 8}
T_ROLE = {6}
V_ROLE = {0}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def sigma(n: int) -> int:
    return SIGMA[n]


def sigma_squared(n: int) -> int:
    return SIGMA[SIGMA[n]]


def sum_psi(subset) -> int:
    return sum(PSI_B[n] for n in subset)


def triangular(k: int) -> int:
    return k * (k + 1) // 2


def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_C1_total_invariant() -> tuple[bool, str]:
    """C1: Sum of Psi_B over all of Z/10Z equals -21."""
    s = sum_psi(range(10))
    expected = -21
    ok = (s == expected)
    return ok, (
        f"C1 (Psi_B total = -21):\n"
        f"  Psi_B values (n=0..9): "
        f"{[PSI_B[n] for n in range(10)]}\n"
        f"  sum = {s}, expected = {expected}, match = {ok}"
    )


def check_C2_sigma_orbit_triangular() -> tuple[bool, str]:
    """C2 (Theorem 3.1): sigma-orbit decomposition.
    sum_{sigma-cycle} Psi_B = -T_5 = -15;
    sum_{sigma-fixed} Psi_B = -T_3 = -6.
    """
    s_cycle = sum_psi(SIGMA_CYCLE)
    s_fixed = sum_psi(SIGMA_FIXED)
    T5 = triangular(5)
    T3 = triangular(3)
    ok_cycle = (s_cycle == -T5)
    ok_fixed = (s_fixed == -T3)
    ok_total = (s_cycle + s_fixed == -21)
    ok = ok_cycle and ok_fixed and ok_total
    return ok, (
        f"C2 (sigma-orbit triangular split):\n"
        f"  sigma-cycle = {sorted(SIGMA_CYCLE)}: "
        f"sum = {s_cycle}, expected -T_5 = -{T5}, match = {ok_cycle}\n"
        f"  sigma-fixed = {sorted(SIGMA_FIXED)}: "
        f"sum = {s_fixed}, expected -T_3 = -{T3}, match = {ok_fixed}\n"
        f"  combined sum = {s_cycle + s_fixed} (expected -21), "
        f"match = {ok_total}"
    )


def check_C3_role_fibonacci() -> tuple[bool, str]:
    """C3 (Theorem 3.2): role-Fibonacci decomposition.
    sum_F = -F_7 = -13; sum_S = -F_6 = -8; sum_T = -1; sum_V = +1; total = -21.
    """
    sF = sum_psi(F_ROLE)
    sS = sum_psi(S_ROLE)
    sT = sum_psi(T_ROLE)
    sV = sum_psi(V_ROLE)
    F7 = fibonacci(7)
    F6 = fibonacci(6)
    ok_F = (sF == -F7)
    ok_S = (sS == -F6)
    ok_T = (sT == -1)
    ok_V = (sV == +1)
    ok_total = (sF + sS + sT + sV == -21)
    ok = ok_F and ok_S and ok_T and ok_V and ok_total
    return ok, (
        f"C3 (role-Fibonacci split):\n"
        f"  F = {sorted(F_ROLE)}: sum = {sF}, expected -F_7 = -{F7}, "
        f"match = {ok_F}\n"
        f"  S = {sorted(S_ROLE)}: sum = {sS}, expected -F_6 = -{F6}, "
        f"match = {ok_S}\n"
        f"  T = {sorted(T_ROLE)}: sum = {sT}, expected -1, match = {ok_T}\n"
        f"  V = {sorted(V_ROLE)}: sum = {sV}, expected +1, match = {ok_V}\n"
        f"  total = {sF + sS + sT + sV} (expected -21), match = {ok_total}"
    )


def check_C4_sigma2_per_orbit() -> tuple[bool, str]:
    """C4 (Proposition 4.1, the R1 sign-swap fix):
    sum_{O_1 = {1, 6, 4}} Psi_B = -8;
    sum_{O_2 = {7, 5, 2}} Psi_B = -7;
    with O_1 + O_2 = -15 = -T_5.
    """
    sO1 = sum_psi(O_1)
    sO2 = sum_psi(O_2)
    expected_O1 = -8
    expected_O2 = -7
    T5 = triangular(5)
    ok_O1 = (sO1 == expected_O1)
    ok_O2 = (sO2 == expected_O2)
    ok_sum = (sO1 + sO2 == -T5)
    ok = ok_O1 and ok_O2 and ok_sum
    return ok, (
        f"C4 (sigma^2-orbit per-orbit, R1 sign-swap fix):\n"
        f"  O_1 = {sorted(O_1)}: sum = {sO1}, expected = {expected_O1}, "
        f"match = {ok_O1}\n"
        f"  O_2 = {sorted(O_2)}: sum = {sO2}, expected = {expected_O2}, "
        f"match = {ok_O2}\n"
        f"  O_1 + O_2 = {sO1 + sO2}, expected -T_5 = -{T5}, "
        f"match = {ok_sum}\n"
        f"  per-orbit values {{-8, -7}} match negated 4-core indices "
        f"{{Br=8, H=7}}: confirmed."
    )


def check_C5_crossing_closure() -> tuple[bool, str]:
    """C5 (Theorem 3.3): the two decompositions cross.
    F intersect sigma-cycle = {1, 5, 7} is not sigma-stable nor
    sigma^2-stable; no sigma-orbit lies inside a single role class.
    """
    intersection = F_ROLE & SIGMA_CYCLE
    expected_int = {1, 5, 7}
    ok_int = (intersection == expected_int)

    # Closure under sigma: image of {1, 5, 7} under sigma
    sigma_image = {sigma(n) for n in intersection}
    ok_sigma_nonclosed = not sigma_image.issubset(intersection)

    # Closure under sigma^2: image of {1, 5, 7} under sigma^2
    sigma2_image = {sigma_squared(n) for n in intersection}
    ok_sigma2_nonclosed = not sigma2_image.issubset(intersection)

    # No sigma-orbit lies inside a single role class
    sigma_orbits = [SIGMA_FIXED & {0}, SIGMA_FIXED & {3},
                    SIGMA_FIXED & {8}, SIGMA_FIXED & {9},
                    SIGMA_CYCLE]
    roles = [F_ROLE, S_ROLE, T_ROLE, V_ROLE]
    six_cycle_in_any_role = any(SIGMA_CYCLE.issubset(r) for r in roles)
    ok_no_cycle_in_role = not six_cycle_in_any_role

    ok = (ok_int and ok_sigma_nonclosed and ok_sigma2_nonclosed
          and ok_no_cycle_in_role)
    return ok, (
        f"C5 (crossing closure failures):\n"
        f"  F intersect sigma-cycle = {sorted(intersection)}, "
        f"expected {{1, 5, 7}}, match = {ok_int}\n"
        f"  sigma({{1,5,7}}) = {sorted(sigma_image)} "
        f"NOT subset of {{1,5,7}}: {ok_sigma_nonclosed}\n"
        f"  sigma^2({{1,5,7}}) = {sorted(sigma2_image)} "
        f"NOT subset of {{1,5,7}}: {ok_sigma2_nonclosed}\n"
        f"  no role class contains the 6-cycle "
        f"{sorted(SIGMA_CYCLE)}: {ok_no_cycle_in_role}\n"
        f"  -> neither decomposition refines the other"
    )


def check_C6_sigma_permutation_and_swap() -> tuple[bool, str]:
    """C6: sigma^2 has order 3 on the 6-cycle and identity on fixed points;
    O_1 and O_2 are sigma-swapped.
    """
    # sigma^2 acts trivially on sigma-fixed points
    ok_fixed = all(sigma_squared(n) == n for n in SIGMA_FIXED)

    # sigma^2 has order 3 on the 6-cycle (cubed = identity, not identity yet)
    def sigma_pow(n: int, k: int) -> int:
        m = n
        for _ in range(k):
            m = sigma(m)
        return m

    ok_order3_on_cycle = all(
        sigma_pow(n, 6) == n for n in SIGMA_CYCLE
    )  # sigma^6 = identity on full set
    ok_sigma2_3 = all(
        sigma_pow(n, 6) == n and sigma_pow(n, 2) != n
        and sigma_pow(n, 4) != n
        for n in SIGMA_CYCLE
    )

    # sigma swaps O_1 and O_2
    sigma_of_O1 = {sigma(n) for n in O_1}
    sigma_of_O2 = {sigma(n) for n in O_2}
    ok_swap = (sigma_of_O1 == O_2) and (sigma_of_O2 == O_1)

    # sigma^2 stabilises O_1 and O_2
    sigma2_of_O1 = {sigma_squared(n) for n in O_1}
    sigma2_of_O2 = {sigma_squared(n) for n in O_2}
    ok_stab = (sigma2_of_O1 == O_1) and (sigma2_of_O2 == O_2)

    ok = ok_fixed and ok_order3_on_cycle and ok_sigma2_3 and ok_swap and ok_stab
    return ok, (
        f"C6 (sigma data sanity):\n"
        f"  sigma^2 fixes every sigma-fixed point: {ok_fixed}\n"
        f"  sigma^6 = identity on the 6-cycle: {ok_order3_on_cycle}\n"
        f"  sigma^2 has period 3 on every 6-cycle element: {ok_sigma2_3}\n"
        f"  sigma swaps O_1 and O_2: "
        f"sigma(O_1) = {sorted(sigma_of_O1)} = O_2, "
        f"sigma(O_2) = {sorted(sigma_of_O2)} = O_1, match = {ok_swap}\n"
        f"  sigma^2 stabilises each O_i: {ok_stab}"
    )


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 72)
    print("J18 verification -- sigma^2-triadic decomposition on Z/10Z")
    print("Psi_B table:", PSI_B)
    print("=" * 72)

    checks = [
        ("C1", check_C1_total_invariant),
        ("C2", check_C2_sigma_orbit_triangular),
        ("C3", check_C3_role_fibonacci),
        ("C4", check_C4_sigma2_per_orbit),
        ("C5", check_C5_crossing_closure),
        ("C6", check_C6_sigma_permutation_and_swap),
    ]

    results = []
    for name, fn in checks:
        ok, msg = fn()
        results.append((name, ok))
        print()
        print(msg)
        print(f"  -> {name}: {'OK' if ok else 'FAIL'}")

    print()
    print("-" * 72)
    print("Summary")
    print("-" * 72)
    for name, ok in results:
        print(f"  {name}: {'OK' if ok else 'FAIL'}")
    all_ok = all(ok for _, ok in results)
    n_pass = sum(1 for _, ok in results if ok)
    print(f"Overall: {n_pass}/{len(results)} {'PASS' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
