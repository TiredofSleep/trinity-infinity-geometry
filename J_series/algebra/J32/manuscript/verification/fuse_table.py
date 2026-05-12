"""
fuse_table.py - canonical arity-3 fuse table for TSML on Z/10Z.

Per WP104 / FORMULAS_AND_TABLES.md / sprint_unmistakable_truth, TSML has
12.6% non-associative triples (126 of 1000). Of these, every one has
HARMONY (7) on exactly one of the two bracketings. Only 5 distinct
unordered {L, R} pairs occur:
    (0, 7): 108 triples
    (3, 7):   8 triples
    (4, 7):   2 triples
    (7, 8):   6 triples
    (7, 9):   2 triples

For these 126 triples, the binary TSML composition is ambiguous (the
left and right bracketings differ). A canonical operad fuse rule
fuse(a, b, c) -> Z/10Z must be assigned to each. The remaining 874
triples have unambiguous binary composition (left == right == binary
result), so canonical fuse defaults to that result by associativity.

This module:
    - loads the 126 non-associative triples
    - represents the canonical fuse table as a sparse 1000-element map
    - supports candidate rule families (rule_families.py)
    - provides verification predicates: closure under sigma_3 of inputs,
      P_56 symmetry preservation, sigma-orbit equivariance,
      compatibility with the known rule fuse([3,4,7]) = 8

Run as `python fuse_table.py` for a self-test that loads the data,
checks the structural invariants, and prints summary statistics.
"""
from __future__ import annotations

import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Tuple

# ----- canonical TSML table -----
TSML_ROWS = [
    "0000000700",  "0737777777",  "0377477779",  "0777777773",  "0747777787",
    "0777777777",  "0777777777",  "7777777777",  "0777877777",  "0797377777",
]
TSML = [[int(c) for c in row] for row in TSML_ROWS]

OP_NAMES = ["VOID", "LATTICE", "COUNTER", "PROGRESS", "COLLAPSE",
            "BALANCE", "CHAOS", "HARMONY", "BREATH", "RESET"]


def tsml(a: int, b: int) -> int:
    """Binary TSML composition on Z/10Z."""
    return TSML[a][b]


def binary_left(a: int, b: int, c: int) -> int:
    """Left bracketing TSML(TSML(a, b), c)."""
    return tsml(tsml(a, b), c)


def binary_right(a: int, b: int, c: int) -> int:
    """Right bracketing TSML(a, TSML(b, c))."""
    return tsml(a, tsml(b, c))


def is_associative(a: int, b: int, c: int) -> bool:
    return binary_left(a, b, c) == binary_right(a, b, c)


# ----- known rules -----

# The one canonical fuse rule established in WP105 / source material:
KNOWN_RULES: Dict[Tuple[int, int, int], int] = {
    (3, 4, 7): 8,  # fuse([PROGRESS, COLLAPSE, HARMONY]) = BREATH
}


# ----- the non-associative triples (loaded from JSON) -----

DEFAULT_TRIPLES_PATH = Path(__file__).parent.parent / "nonassoc_triples.json"


def load_nonassoc_triples(path: Path = DEFAULT_TRIPLES_PATH) -> List[dict]:
    """Load the 126 non-associative TSML triples from the canonical JSON."""
    with open(path, "r") as f:
        triples = json.load(f)
    # sanity check: every triple should be non-associative
    for t in triples:
        assert binary_left(t["a"], t["b"], t["c"]) == t["left_bracketing"]
        assert binary_right(t["a"], t["b"], t["c"]) == t["right_bracketing"]
        assert t["left_bracketing"] != t["right_bracketing"]
    return triples


# ----- the canonical fuse table data structure -----

@dataclass
class FuseTable:
    """A canonical arity-3 fuse table on Z/10Z.

    For associative triples (a, b, c), fuse(a, b, c) == binary_left(a, b, c)
    == binary_right(a, b, c) by definition. We only store explicit values
    for non-associative triples.
    """
    rules: Dict[Tuple[int, int, int], int] = field(default_factory=dict)
    name: str = "(unnamed)"

    def fuse(self, a: int, b: int, c: int) -> int:
        """Lookup. For associative triples, falls back to binary."""
        key = (a, b, c)
        if key in self.rules:
            return self.rules[key]
        if is_associative(a, b, c):
            return binary_left(a, b, c)
        # Non-associative triple with no rule assigned: undefined
        raise KeyError(f"fuse({a}, {b}, {c}) is undefined: "
                       f"non-associative ({binary_left(a,b,c)} vs "
                       f"{binary_right(a,b,c)}) and no canonical rule set")

    def is_complete(self) -> bool:
        """True iff every non-associative triple has a canonical rule."""
        triples = load_nonassoc_triples()
        for t in triples:
            if (t["a"], t["b"], t["c"]) not in self.rules:
                return False
        return True

    def coverage(self) -> Tuple[int, int]:
        """Returns (covered_count, total_nonassoc)."""
        triples = load_nonassoc_triples()
        covered = sum(1 for t in triples if (t["a"], t["b"], t["c"]) in self.rules)
        return covered, len(triples)

    def respects_known_rules(self) -> bool:
        """True iff this table agrees with the canonical KNOWN_RULES."""
        for key, expected in KNOWN_RULES.items():
            if key in self.rules:
                if self.rules[key] != expected:
                    return False
            else:
                # The known rule fuse([3,4,7]) = 8 is on an ASSOCIATIVE triple
                # (binary_left = binary_right = 7). The canonical fuse table
                # ASSIGNS 8 here, departing from binary. So the known rule
                # MUST be in the rules dict; absence means non-compliance.
                a, b, c = key
                if is_associative(a, b, c):
                    if expected != binary_left(a, b, c):
                        return False  # known rule departs from binary;
                                       # the table must explicitly assign it
        return True

    def add_known_rules(self) -> "FuseTable":
        """Return a copy of self with KNOWN_RULES merged in."""
        new_rules = dict(self.rules)
        for key, val in KNOWN_RULES.items():
            new_rules[key] = val
        return FuseTable(rules=new_rules, name=self.name + "+known")


# ----- structural invariants we may want to test -----

def sigma_permutation() -> Dict[int, int]:
    """The sigma permutation on Z/10Z.

    Cycle structure: (0)(3)(8)(9)(1 7 6 5 4 2).
    Maps: 0->0, 3->3, 8->8, 9->9, 1->7, 7->6, 6->5, 5->4, 4->2, 2->1.
    """
    return {0: 0, 3: 3, 8: 8, 9: 9, 1: 7, 7: 6, 6: 5, 5: 4, 4: 2, 2: 1}


def p56_swap() -> Dict[int, int]:
    """The P_56 swap on Z/10Z. 5 <-> 6, all else fixed."""
    return {i: i for i in range(10)} | {5: 6, 6: 5}


def sigma_3_pi() -> Dict[int, int]:
    """sigma^3 on Z/10Z (the order-2 element of the 6-cycle).

    Acts as: (0)(3)(8)(9)(1 5)(7 4)(6 2). Three disjoint transpositions
    on the 6-cycle.
    """
    return {0: 0, 3: 3, 8: 8, 9: 9, 1: 5, 5: 1, 7: 4, 4: 7, 6: 2, 2: 6}


def is_p56_symmetric(table: FuseTable) -> bool:
    """Test: does fuse(P_56(a), P_56(b), P_56(c)) = P_56(fuse(a, b, c))?

    Required for the fuse table to commute with the P_56 swap symmetry
    that's verified at the so(10) level (WP104).
    """
    pi = p56_swap()
    triples = load_nonassoc_triples()
    for t in triples:
        a, b, c = t["a"], t["b"], t["c"]
        try:
            f_orig = table.fuse(a, b, c)
            f_swapped = table.fuse(pi[a], pi[b], pi[c])
        except KeyError:
            return False  # incomplete table; can't verify
        if pi[f_orig] != f_swapped:
            return False
    return True


def is_sigma3_symmetric(table: FuseTable) -> bool:
    """Test: does fuse commute with sigma^3?"""
    pi = sigma_3_pi()
    triples = load_nonassoc_triples()
    for t in triples:
        a, b, c = t["a"], t["b"], t["c"]
        try:
            f_orig = table.fuse(a, b, c)
            f_swapped = table.fuse(pi[a], pi[b], pi[c])
        except KeyError:
            return False
        if pi[f_orig] != f_swapped:
            return False
    return True


def is_d4_symmetric(table: FuseTable) -> bool:
    """Test: does fuse commute with both P_56 and sigma^3?

    The doubly-invariant content under D_4 = <P_56, sigma^3> is
    su(4) (+) u(1) (WP104). A fuse table that commutes with both
    is "D_4-equivariant" and respects the same symmetries as the
    Pati-Salam (+) B-L gauge structure.
    """
    return is_p56_symmetric(table) and is_sigma3_symmetric(table)


# ----- analysis on the non-associative triples -----

def summary(triples: Optional[List[dict]] = None) -> str:
    """Produce a textual summary of the 126 non-associative triples."""
    if triples is None:
        triples = load_nonassoc_triples()
    lines = []
    lines.append(f"Total non-associative triples: {len(triples)}")
    pairs = Counter()
    for t in triples:
        L, R = t["left_bracketing"], t["right_bracketing"]
        pairs[tuple(sorted((L, R)))] += 1
    lines.append(f"Distinct unordered (L, R) bracket-pairs: {len(pairs)}")
    for pair, count in sorted(pairs.items(), key=lambda x: -x[1]):
        L_name = OP_NAMES[pair[0]]
        R_name = OP_NAMES[pair[1]]
        lines.append(f"  ({pair[0]}={L_name}, {pair[1]}={R_name}): {count}")
    # Position counts
    a_counts = Counter(t["a"] for t in triples)
    b_counts = Counter(t["b"] for t in triples)
    c_counts = Counter(t["c"] for t in triples)
    lines.append("\nPosition-distribution:")
    lines.append(f"  Left (a):   {dict(sorted(a_counts.items()))}")
    lines.append(f"  Middle (b): {dict(sorted(b_counts.items()))}")
    lines.append(f"  Right (c):  {dict(sorted(c_counts.items()))}")
    return "\n".join(lines)


# ----- self-test -----

def main():
    print("fuse_table.py self-test")
    print("=" * 70)
    triples = load_nonassoc_triples()
    print(summary(triples))
    print()
    print("KNOWN_RULES:")
    for key, val in KNOWN_RULES.items():
        a, b, c = key
        print(f"  fuse({a}={OP_NAMES[a]}, {b}={OP_NAMES[b]}, {c}={OP_NAMES[c]}) = {val}={OP_NAMES[val]}")
        print(f"    binary_left  = {binary_left(*key)}={OP_NAMES[binary_left(*key)]}")
        print(f"    binary_right = {binary_right(*key)}={OP_NAMES[binary_right(*key)]}")
        print(f"    associative? {is_associative(*key)}")
        print(f"    canonical fuse departs from binary: {val != binary_left(*key)}")

    print()
    print("Empty FuseTable() coverage check:")
    table = FuseTable(name="empty")
    cov, total = table.coverage()
    print(f"  covered: {cov}/{total}")
    print(f"  is_complete: {table.is_complete()}")

    print()
    print("FuseTable with known rules:")
    table_known = FuseTable(name="known-only").add_known_rules()
    cov, total = table_known.coverage()
    print(f"  covered: {cov}/{total} (the known rule is on an associative triple, so doesn't help non-assoc coverage)")


if __name__ == "__main__":
    main()
