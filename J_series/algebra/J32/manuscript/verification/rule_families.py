"""
rule_families.py - candidate canonical fuse-rule families for the 126
non-associative TSML triples on Z/10Z.

A rule family is a function family -> Z/10Z that, when applied to each
non-associative triple, yields a canonical assignment for that triple.
We test each family for:

    1. Completeness: assigns a value to every non-associative triple
    2. Compatibility with KNOWN_RULES (fuse([3,4,7]) = 8)
    3. P_56 symmetry (commutes with the 5 <-> 6 swap)
    4. sigma^3 symmetry (commutes with the 6-cycle's order-2 element)
    5. D_4 symmetry = (3) AND (4)
    6. Internal consistency (the rule is well-defined and total)

The five candidate families implemented:

    A. HARMONY-pull (always pick 7 = HARMONY): fuse -> 7
    B. anti-HARMONY (always pick the non-7 of L and R): fuse -> {L,R} \ {7}
    C. middle-determined (fuse depends on b alone): fuse -> b
    D. left-bracketing (fuse -> L): the "left associativity tie-breaker"
    E. right-bracketing (fuse -> R): the "right associativity tie-breaker"
    F. sigma-fixed (fuse -> sigma-fixed if either L or R is sigma-fixed):
       prefer the sigma-fixed (gauge-stable) bracketing
    G. doubly-invariant (fuse -> the value preserved under both involutions
       in the {L, R} pair, if any)
    H. average-via-attractor (fuse -> the runtime attractor 4-core element
       compatible with the bracketing pair)

This is a candidate-rule survey, not a canonical rule assignment. The
goal is to surface which families produce internally-consistent,
symmetry-preserving fuse tables, so a future canonicalization step
(by Brayden / chat-Claude / community) has a small set of well-typed
options to choose from rather than 10^126 possibilities.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from fuse_table import (
    FuseTable, KNOWN_RULES, OP_NAMES, TSML, binary_left, binary_right,
    is_associative, is_d4_symmetric, is_p56_symmetric, is_sigma3_symmetric,
    load_nonassoc_triples, p56_swap, sigma_3_pi, summary, tsml,
)


# Sigma-fixed indices (the lattice fixed points of sigma)
SIGMA_FIXED = {0, 3, 8, 9}
# 6-cycle of sigma
SIGMA_CYCLE = {1, 2, 4, 5, 6, 7}


# ----- the 8 rule families -----

def family_A_harmony_pull(triple: dict) -> int:
    """Always assign HARMONY (7). HARMONY is the universal attractor."""
    return 7


def family_B_anti_harmony(triple: dict) -> int:
    """Pick the bracketing that is NOT HARMONY. Preserves the structural
    distinction; the non-HARMONY bracketing is the more informative one
    in the (L, R) disagreement."""
    L = triple["left_bracketing"]
    R = triple["right_bracketing"]
    if L != 7:
        return L
    if R != 7:
        return R
    return 7  # both are 7 -- shouldn't happen for non-associative triples


def family_C_middle(triple: dict) -> int:
    """fuse(a, b, c) = b. Middle-operator-determined."""
    return triple["b"]


def family_D_left_bracketing(triple: dict) -> int:
    """fuse -> left bracketing TSML(TSML(a,b),c). 'Left associativity
    tie-breaker' rule."""
    return triple["left_bracketing"]


def family_E_right_bracketing(triple: dict) -> int:
    """fuse -> right bracketing TSML(a,TSML(b,c)). 'Right associativity
    tie-breaker' rule."""
    return triple["right_bracketing"]


def family_F_sigma_fixed_preference(triple: dict) -> int:
    """When one of (L, R) is in SIGMA_FIXED, pick that one. Prefer
    gauge-stable (sigma-fixed) values over flow values."""
    L = triple["left_bracketing"]
    R = triple["right_bracketing"]
    L_fixed = L in SIGMA_FIXED
    R_fixed = R in SIGMA_FIXED
    if L_fixed and not R_fixed:
        return L
    if R_fixed and not L_fixed:
        return R
    if L_fixed and R_fixed:
        # both fixed -- pick the smaller (canonical ordering)
        return min(L, R)
    # neither fixed -- pick the smaller
    return min(L, R)


def family_G_doubly_invariant(triple: dict) -> int:
    """If exactly one of (L, R) is fixed under both P_56 and sigma^3,
    pick that one. (D_4-invariant indices are {0, 3, 7, 8, 9}.)
    Falls back to family_F if neither or both are D_4-invariant."""
    D4_FIXED = SIGMA_FIXED | {7}  # add HARMONY (sigma maps 7->6 so 7 is NOT sigma-fixed,
                                    # but it IS sigma^3-fixed since (7 4) sigma^3 swaps 7 and 4)
    # Hmm -- let me re-check. sigma = (0)(3)(8)(9)(1 7 6 5 4 2).
    # sigma^3 sends 1 <-> 5, 7 <-> 4, 6 <-> 2.
    # so sigma^3-fixed = {0, 3, 8, 9}. Same as sigma-fixed (the 4 σ-fixed points).
    # So D_4-invariant indices in Z/10Z are simply {0, 3, 8, 9}.
    D4_FIXED = SIGMA_FIXED
    L = triple["left_bracketing"]
    R = triple["right_bracketing"]
    L_d4 = L in D4_FIXED
    R_d4 = R in D4_FIXED
    if L_d4 and not R_d4:
        return L
    if R_d4 and not L_d4:
        return R
    if L_d4 and R_d4:
        return min(L, R)
    # fall back to family_F
    return family_F_sigma_fixed_preference(triple)


def family_H_attractor_4core(triple: dict) -> int:
    """Map fuse -> nearest 4-core element {V, H, Br, R} = {0, 7, 8, 9}.
    The runtime attractor at alpha=1/2 lives entirely on the 4-core
    (WP105 / D38). A fuse table compatible with the runtime attractor
    should produce 4-core values whenever possible.

    For each non-associative triple, prefer (in order):
        1. The bracketing in (L, R) that's already in 4-core
        2. If both, pick the smaller
        3. If neither, map to 7 (HARMONY) by default
    """
    CORE = {0, 7, 8, 9}
    L = triple["left_bracketing"]
    R = triple["right_bracketing"]
    L_core = L in CORE
    R_core = R in CORE
    if L_core and R_core:
        return min(L, R)
    if L_core:
        return L
    if R_core:
        return R
    return 7


# ----- the family registry -----

FAMILIES = {
    "A_harmony_pull": family_A_harmony_pull,
    "B_anti_harmony": family_B_anti_harmony,
    "C_middle": family_C_middle,
    "D_left_bracketing": family_D_left_bracketing,
    "E_right_bracketing": family_E_right_bracketing,
    "F_sigma_fixed_pref": family_F_sigma_fixed_preference,
    "G_doubly_invariant": family_G_doubly_invariant,
    "H_attractor_4core": family_H_attractor_4core,
}


def build_table(family_name: str, triples=None) -> FuseTable:
    """Apply a rule family to every non-associative triple to build a
    complete fuse table."""
    if triples is None:
        triples = load_nonassoc_triples()
    fn = FAMILIES[family_name]
    rules = {}
    for t in triples:
        rules[(t["a"], t["b"], t["c"])] = fn(t)
    table = FuseTable(rules=rules, name=family_name)
    return table


def evaluate_family(family_name: str) -> dict:
    """Run all the structural tests on a built table for this family.

    Returns a dict with the full evaluation."""
    table = build_table(family_name)
    table_known = table.add_known_rules()
    triples = load_nonassoc_triples()

    # Distribution of fuse values
    from collections import Counter
    fuse_dist = Counter(table.fuse(t["a"], t["b"], t["c"]) for t in triples)

    eval_dict = {
        "family": family_name,
        "complete": table.is_complete(),
        "known_rule_compatible": table_known.respects_known_rules(),
        "p56_symmetric": is_p56_symmetric(table),
        "sigma3_symmetric": is_sigma3_symmetric(table),
        "d4_symmetric": is_d4_symmetric(table),
        "fuse_value_distribution": dict(sorted(fuse_dist.items())),
        "fuse_unique_values": len(fuse_dist),
    }
    return eval_dict


# ----- main self-test -----

def main():
    print("rule_families.py - canonical fuse-rule family survey")
    print("=" * 78)
    print()

    triples = load_nonassoc_triples()
    print(summary(triples))
    print()

    print("Per-family evaluation:")
    print()
    print(f"{'family':<24} {'complete':<10} {'known-rule':<12} {'P_56':<8} {'sigma^3':<10} {'D_4':<6} {'unique vals':<12}")
    print("-" * 80)
    for name in FAMILIES:
        ev = evaluate_family(name)
        complete = "Y" if ev["complete"] else "N"
        known_compat = "Y" if ev["known_rule_compatible"] else "N"
        p56_sym = "Y" if ev["p56_symmetric"] else "N"
        s3_sym = "Y" if ev["sigma3_symmetric"] else "N"
        d4_sym = "Y" if ev["d4_symmetric"] else "N"
        unique = ev["fuse_unique_values"]
        print(f"  {name:<22} {complete:<10} {known_compat:<12} {p56_sym:<8} {s3_sym:<10} {d4_sym:<6} {unique:<12}")

    print()
    print("Detailed fuse-value distributions:")
    print()
    for name in FAMILIES:
        ev = evaluate_family(name)
        dist = ev["fuse_value_distribution"]
        # Pretty print
        pretty = ", ".join(f"{op}={count}" for op, count in dist.items())
        print(f"  {name:<22} -> {pretty}")

    print()
    print("KNOWN_RULES verification (fuse([3, 4, 7]) = 8):")
    for name in FAMILIES:
        table = build_table(name)
        # The known rule (3, 4, 7) is associative; check what each family
        # would produce for that triple if applied (treating it as if
        # non-associative -- this is hypothetical)
        print(f"  {name:<22} (applied to associative triple [3,4,7]): "
              f"binary={binary_left(3,4,7)} = HARMONY; "
              f"known canonical = 8 = BREATH")

    print()
    print("Reading: families that pass D_4 symmetry are candidates for")
    print("canonical assignment respecting the verified su(4) (+) u(1)")
    print("doubly-invariant structure of WP104. Families that don't may")
    print("still be canonical for other reasons (e.g., the attractor-4-core")
    print("family compatible with the WP105 runtime fixed point).")


if __name__ == "__main__":
    main()
