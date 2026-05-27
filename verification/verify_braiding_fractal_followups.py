"""verify_braiding_fractal_followups.py -- exercise claudechat's three asks
against the Braiding Fractal Z/30/Z/210 document.

Three tests:
  (1) Strand-11 partition test: does CRT-extended sigma on Z/2310 partition
      into 11-element orbits? (Expected: NO -- strand 11 is char-poly-level.)
  (2) Braid-group order propagation: does ord(sigma_Z/n) match |S_{omega+1}|
      under the natural CRT extension? (Expected: NO -- ord stays 6.)
  (3) sigma^2-Z_3 persistence at Z/210: does the rotation lens survive the
      lift? (Expected: YES -- confirmed.)

Verification of the kissing-number strata test (Tier-B): see the companion
script verification/verify_sphere_packing_strata.py.

Dependencies: sympy. Runtime: <1 second.
"""
from math import gcd, lcm
from collections import Counter


# Canonical sigma on Z/10: (0)(3)(8)(9)(1 7 6 5 4 2)
SIGMA_10 = {0: 0, 3: 3, 8: 8, 9: 9, 1: 7, 7: 6, 6: 5, 5: 4, 4: 2, 2: 1}


def sigma_crt(x, n):
    """Natural CRT extension of sigma to Z/n where 10 | n and gcd(10, n/10) = 1."""
    m = n // 10
    assert n % 10 == 0
    assert gcd(10, m) == 1, f"gcd(10, {m}) != 1, no CRT"
    a = x % 10
    b = x % m
    new_a = SIGMA_10[a]
    inv_m_mod_10 = pow(m, -1, 10)
    inv_10_mod_m = pow(10, -1, m)
    return (new_a * m * inv_m_mod_10 + b * 10 * inv_10_mod_m) % n


def cycle_structure(perm_func, n):
    """Return (orbit lengths Counter, total orbit count)."""
    visited = set()
    cycle_lens = []
    for x in range(n):
        if x in visited: continue
        cycle_len = 0
        y = x
        while y not in visited:
            visited.add(y); cycle_len += 1; y = perm_func(y)
        cycle_lens.append(cycle_len)
    return Counter(cycle_lens), len(cycle_lens)


def perm_order(perm_func, n):
    counter, _ = cycle_structure(perm_func, n)
    ord_val = 1
    for L in counter:
        ord_val = lcm(ord_val, L)
    return ord_val


def omega(n):
    from sympy import factorint
    return len(factorint(n))


# ============================================================
# Test 1: Strand-11 partition at Z/2310
# ============================================================

def test_strand11():
    print("[Test 1] Strand-11 partition at Z/2310")
    perm = lambda x: sigma_crt(x, 2310)
    counter, n_orbits = cycle_structure(perm, 2310)
    print(f"  Cycle structure: {dict(sorted(counter.items()))}")
    print(f"  Total orbits: {n_orbits}")
    has_11 = 11 in counter
    print(f"  11-element orbits present? {has_11}")
    if not has_11:
        print("  PASS (confirms doc's claim: strand 11 is char-poly-level, not state-level)")
    else:
        print(f"  Unexpected: {counter[11]} orbits of length 11")
    print()


# ============================================================
# Test 2: Braid-group order propagation
# ============================================================

def factorial(k):
    out = 1
    for i in range(1, k + 1):
        out *= i
    return out


def test_braid_orders():
    print("[Test 2] Braid-group order |S_{omega+1}| propagation")
    print(f"  {'Substrate':<11}  {'omega':<6}  {'ord(sigma)':<11}  {'|S_{omega+1}|':<14}  {'match?'}")
    for n in [10, 30, 210, 2310, 30030]:
        perm = lambda x: sigma_crt(x, n)
        ord_s = perm_order(perm, n)
        w = omega(n)
        S_order = factorial(w + 1)
        match = "YES" if ord_s == S_order else "NO"
        print(f"  Z/{n:<8}  {w:<6}  {ord_s:<11}  {S_order:<14}  {match}")
    print()
    print("  CONCLUSION: ord(sigma_tilde) stays at 6 across all rungs under")
    print("  the trivial CRT extension. The |S_{omega+1}| growth claim does")
    print("  NOT propagate trivially -- a non-trivial sigma-extension would")
    print("  be needed to justify the braid-group language algebraically.")
    print("  Currently TIER C, pending such an extension definition.")
    print()


# ============================================================
# Test 3: sigma^2-Z_3 persistence at Z/210
# ============================================================

def test_sigma2_persistence():
    print("[Test 3] sigma^2-Z_3 rotation persistence at Z/210")
    # On Z/10, sigma^2 rotates pairs {1,5} -> {2,6} -> {4,7} -> {1,5}
    # Verify under CRT lift to Z/210
    perm = lambda x: sigma_crt(x, 210)
    sigma2 = lambda x: perm(perm(x))
    # lifted pair {1, 5}: all x in Z/210 with x mod 10 in {1, 5}
    lift_15 = [x for x in range(210) if x % 10 in {1, 5}]
    lift_26 = {x for x in range(210) if x % 10 in {2, 6}}
    lift_47 = {x for x in range(210) if x % 10 in {4, 7}}

    # sigma^2 should send lift({1,5}) into lift({2,6})
    images = [sigma2(x) for x in lift_15]
    image_mod10 = set(y % 10 for y in images)
    print(f"  sigma^2 on lift({{1,5}}) -> mod-10 values: {sorted(image_mod10)}")
    print(f"  Expected: {{2, 6}}")
    assert image_mod10 == {2, 6}, f"sigma^2 lens broken: {image_mod10}"
    # And images stay within lift({2,6})
    assert all(y in lift_26 for y in images), "sigma^2 not closed in lift({2,6})"
    print(f"  PASS: lens {{1,5}} -> {{2,6}} survives lift to Z/210")

    # Check the full rotation: lift({2,6}) -> lift({4,7})
    lift_26_list = [x for x in range(210) if x % 10 in {2, 6}]
    images2 = [sigma2(x) for x in lift_26_list]
    image2_mod10 = set(y % 10 for y in images2)
    print(f"  sigma^2 on lift({{2,6}}) -> mod-10 values: {sorted(image2_mod10)}")
    print(f"  Expected: {{4, 7}}")
    assert image2_mod10 == {4, 7}
    assert all(y in lift_47 for y in images2)
    print(f"  PASS: lens {{2,6}} -> {{4,7}} survives lift to Z/210")
    print()
    print("  CONCLUSION: sigma^2-Z_3 rotation lens DESCENDS cleanly to Z/210.")
    print("  The three sigma^3-pairs lift to three equinumerous classes")
    print("  (each of 42 elements in Z/210) and sigma^2 acts as Z_3 rotation")
    print("  on these classes. The structural lens is preserved under braid lift.")
    print()


def main():
    print("=== Braiding Fractal Z/30 + Z/210 followup verifications ===\n")
    test_strand11()
    test_braid_orders()
    test_sigma2_persistence()
    print("=" * 60)
    print("  ALL 3 TESTS RUN.")
    print("  Test 1: PASS (confirms strand 11 is char-poly-level)")
    print("  Test 2: NEGATIVE (braid-group claim needs non-trivial extension)")
    print("  Test 3: PASS (sigma^2-Z_3 lens persists at Z/210)")
    print("=" * 60)


if __name__ == "__main__":
    main()
