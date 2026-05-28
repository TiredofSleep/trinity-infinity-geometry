"""
d4_orbit_decomposition.py - decompose the 126 non-associative TSML triples
into D_4 = <P_56, sigma^3> orbits.

The diagonal action of D_4 on (Z/10Z)^3 is:
    g . (a, b, c) = (g(a), g(b), g(c)) for g in D_4

D_4 has order 8: {id, P_56, sigma^3, P_56 * sigma^3, ...}.

For a D_4-equivariant fuse rule, all triples in the same D_4-orbit must
fuse to images of one another under D_4. So the assignment of fuse values
is constrained orbit-by-orbit, not triple-by-triple.

This script:
    1. Enumerates the 8 elements of D_4
    2. Computes the D_4-orbit of each non-associative triple
    3. Groups the 126 triples by orbit
    4. For each orbit, identifies the D_4-equivariance constraint on
       any canonical fuse rule

If every orbit has a self-consistent assignment (i.e., the bracketing
pair (L, R) maps coherently across the orbit), then a D_4-equivariant
fuse rule exists. If any orbit has incompatible (L, R) pairs across its
triples, no D_4-equivariant fuse rule exists.

This is the structural test the OPERAD_FINDINGS.md doc identified as
the next step after the 8-family rule survey.
"""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, FrozenSet, List, Tuple

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))

from fuse_table import (
    KNOWN_RULES, OP_NAMES, binary_left, binary_right, is_associative,
    load_nonassoc_triples, p56_swap, sigma_3_pi, summary,
)


# ---------- D_4 group elements ----------

def compose(pi1: Dict[int, int], pi2: Dict[int, int]) -> Dict[int, int]:
    """Composition of permutations: (pi1 . pi2)(x) = pi1(pi2(x))."""
    return {x: pi1[pi2[x]] for x in pi2}


def identity_perm() -> Dict[int, int]:
    return {i: i for i in range(10)}


def d4_elements() -> Dict[str, Dict[int, int]]:
    """Generate all 8 elements of D_4 = <P_56, sigma^3>.

    D_4 has structure: r^4 = s^2 = (rs)^2 = e where r is the rotation
    (order 4) and s is the reflection (order 2). For our generators
    P_56 (order 2, single transposition) and sigma^3 (order 2, three
    transpositions), the products generate a group of order 8.
    """
    p56 = p56_swap()
    s3 = sigma_3_pi()
    e = identity_perm()
    elements = {"e": e, "P56": p56, "sigma3": s3}
    # Add products
    elements["P56*sigma3"] = compose(p56, s3)
    elements["sigma3*P56"] = compose(s3, p56)
    elements["P56*sigma3*P56"] = compose(p56, compose(s3, p56))
    elements["sigma3*P56*sigma3"] = compose(s3, compose(p56, s3))
    elements["P56*sigma3*P56*sigma3"] = compose(p56, compose(s3, compose(p56, s3)))
    # Deduplicate
    seen = set()
    unique = {}
    for name, perm in elements.items():
        # Hashable key
        key = tuple((i, perm[i]) for i in range(10))
        if key not in seen:
            seen.add(key)
            unique[name] = perm
    return unique


# ---------- orbit computation ----------

def diag_action(g: Dict[int, int], triple: Tuple[int, int, int]) -> Tuple[int, int, int]:
    a, b, c = triple
    return (g[a], g[b], g[c])


def orbit_of(triple: Tuple[int, int, int],
             group_elements: Dict[str, Dict[int, int]]) -> FrozenSet[Tuple[int, int, int]]:
    """The D_4-orbit of a single triple."""
    return frozenset(diag_action(g, triple) for g in group_elements.values())


def all_d4_orbits(triples_list: List[dict],
                   group_elements: Dict[str, Dict[int, int]]
                   ) -> List[FrozenSet[Tuple[int, int, int]]]:
    """Decompose the input list of triples into D_4-orbits.

    Returns a list of orbits, each as a frozenset of (a, b, c) tuples.
    """
    triples = [(t["a"], t["b"], t["c"]) for t in triples_list]
    triples_set = set(triples)
    seen = set()
    orbits = []
    for triple in triples:
        if triple in seen:
            continue
        orbit = orbit_of(triple, group_elements)
        # Filter to only triples actually in our input set
        orbit_in_set = orbit & triples_set
        if orbit_in_set:
            orbits.append(frozenset(orbit_in_set))
            seen.update(orbit_in_set)
    return orbits


# ---------- bracketing-pair coherence check ----------

def orbit_bracketing_pairs(orbit: FrozenSet[Tuple[int, int, int]],
                            triples_dict: Dict[Tuple[int, int, int], dict]
                            ) -> List[Tuple[int, int]]:
    """For each triple in the orbit, return its (L, R) bracketing pair.
    The pair is unordered for D_4-coherence purposes (the rule depends
    on which bracketing is which up to D_4-conjugation).
    """
    pairs = []
    for t in orbit:
        if t in triples_dict:
            entry = triples_dict[t]
            L, R = entry["left_bracketing"], entry["right_bracketing"]
            pairs.append(tuple(sorted((L, R))))
    return pairs


def orbit_has_coherent_bracketings(orbit: FrozenSet[Tuple[int, int, int]],
                                     triples_dict: Dict[Tuple[int, int, int], dict],
                                     group_elements: Dict[str, Dict[int, int]]
                                     ) -> Tuple[bool, str]:
    """Check whether the bracketing pairs across the orbit are
    D_4-equivariantly coherent. Returns (coherent, reason).

    For D_4-equivariance: if g.t1 = t2 in the orbit, then
    (L(t2), R(t2)) should equal (g(L(t1)), g(R(t1))) as a multiset.
    """
    triples_in_orbit = list(orbit)
    if len(triples_in_orbit) <= 1:
        return True, "singleton orbit"

    # Pick the first triple as base; compute (L, R) for every group element
    # mapping base to other triples in the orbit
    base = triples_in_orbit[0]
    if base not in triples_dict:
        return True, "base not in dict (skipped)"
    base_entry = triples_dict[base]
    base_L, base_R = base_entry["left_bracketing"], base_entry["right_bracketing"]

    # For each other triple in the orbit, check D_4-coherence
    for t in triples_in_orbit[1:]:
        if t not in triples_dict:
            continue
        # Find a group element g such that g(base) = t
        g_found = None
        for name, g in group_elements.items():
            if diag_action(g, base) == t:
                g_found = (name, g)
                break
        if g_found is None:
            return False, f"no g maps base {base} to {t}"
        # The expected (L, R) for t under D_4-equivariance
        name, g = g_found
        expected_L = g[base_L]
        expected_R = g[base_R]
        actual_L = triples_dict[t]["left_bracketing"]
        actual_R = triples_dict[t]["right_bracketing"]
        # Compare as multisets (since (L, R) ordering is symmetric)
        if {expected_L, expected_R} != {actual_L, actual_R}:
            return False, (
                f"under {name}, base ({base_L}, {base_R}) -> "
                f"({expected_L}, {expected_R}); but t={t} has "
                f"({actual_L}, {actual_R})"
            )
    return True, "D_4-coherent"


# ---------- main ----------

def main():
    print("d4_orbit_decomposition.py")
    print("=" * 72)
    print()

    triples_list = load_nonassoc_triples()
    triples_dict = {(t["a"], t["b"], t["c"]): t for t in triples_list}

    # 1. D_4 group structure
    elements = d4_elements()
    print(f"D_4 = <P_56, sigma^3> has {len(elements)} elements:")
    for name in elements:
        print(f"  {name}")
    print()

    # 2. Orbit decomposition
    orbits = all_d4_orbits(triples_list, elements)
    print(f"D_4-orbits of the {len(triples_list)} non-associative triples:")
    print(f"  number of orbits: {len(orbits)}")

    orbit_sizes = [len(o) for o in orbits]
    from collections import Counter
    size_dist = Counter(orbit_sizes)
    print(f"  orbit size distribution:")
    for size, count in sorted(size_dist.items()):
        print(f"    {count} orbits of size {size}")
    print()

    # 3. Sample orbits (smallest and largest)
    sorted_orbits = sorted(orbits, key=len)
    print("Smallest orbits (first 5):")
    for orbit in sorted_orbits[:5]:
        print(f"  size {len(orbit)}: {sorted(orbit)}")
    print()
    print("Largest orbits (last 3):")
    for orbit in sorted_orbits[-3:]:
        print(f"  size {len(orbit)}: {sorted(orbit)}")
    print()

    # 4. D_4-coherence check on each orbit
    print("D_4-equivariance coherence per orbit:")
    coherent_count = 0
    incoherent_orbits = []
    for orbit in orbits:
        coherent, reason = orbit_has_coherent_bracketings(orbit, triples_dict, elements)
        if coherent:
            coherent_count += 1
        else:
            incoherent_orbits.append((orbit, reason))
    print(f"  coherent orbits:   {coherent_count} / {len(orbits)}")
    print(f"  incoherent orbits: {len(incoherent_orbits)}")
    print()

    if incoherent_orbits:
        print("First 5 incoherent orbits (these block any D_4-equivariant fuse):")
        for orbit, reason in incoherent_orbits[:5]:
            print(f"  orbit (size {len(orbit)}): {sorted(orbit)}")
            print(f"    reason: {reason}")
            for t in sorted(orbit):
                if t in triples_dict:
                    e = triples_dict[t]
                    print(f"      {t}: L={e['left_bracketing']}, R={e['right_bracketing']}")
        print()

    # 5. Verdict
    print("=" * 72)
    print("VERDICT")
    print("=" * 72)
    if not incoherent_orbits:
        print("  All non-associative triple orbits are D_4-equivariantly coherent.")
        print("  A D_4-equivariant canonical fuse rule EXISTS (constrained per orbit).")
    else:
        print(f"  {len(incoherent_orbits)} of {len(orbits)} orbits are D_4-incoherent.")
        print("  This means: NO D_4-equivariant canonical fuse rule exists for")
        print("  the 126 non-associative triples. Any canonical assignment must")
        print("  break D_4-symmetry; the operad-DOF carries content orthogonal to")
        print("  the doubly-invariant gauge structure of WP104.")
        print()
        print("  This is a real structural finding: the operad layer (arity-3 fuse")
        print("  rules) is NOT compatible with the D_4 = <P_56, sigma^3> symmetry")
        print("  group that governs the WP104 doubly-invariant subalgebra.")
        print()
        print("  The natural canonical choice is then to break the symmetry along")
        print("  an explicit direction (e.g., prefer P_56-equivariance, or prefer")
        print("  sigma^3-equivariance) and document which choice was made.")


if __name__ == "__main__":
    main()
