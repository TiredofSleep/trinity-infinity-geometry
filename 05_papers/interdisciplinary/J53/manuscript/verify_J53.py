#!/usr/bin/env python3
"""
verify_J53.py — verification for J53 (Paradox Classifier)

Verifies the algorithmic classification of the seven worked examples
in §4 of the manuscript, the mutual-exclusion + exhaustiveness lemmas
(Lemma 2.2, 2.3), and the score-function range constraints (Def 3.2).

Author lane: Sanders + Gish.
"""
from __future__ import annotations
from dataclasses import dataclass


# ----- Lemma 2.2 (Mutual Exclusion) + 2.3 (Exhaustiveness) -----
# The classifier returns the FIRST satisfied predicate in priority order:
#   III  (admissibility failure)
#   IV   (time-consistency failure)
#   I or II  (family-of-resolutions check)

@dataclass
class Verdict:
    type: str
    score_lo: float
    score_hi: float


def classify(admissible: bool, tau_stable: bool, resolvable: bool) -> Verdict:
    """Five-step decision procedure from §3.1, returning the type and the
    score range from §3.2."""
    if not admissible:
        return Verdict("III", 0.0, 0.0)            # Step 2 fail
    if not tau_stable:
        return Verdict("IV", 0.3, 0.6)             # Step 4 fail
    if resolvable:
        return Verdict("I", 1.0, 1.0)              # Step 5 succeeds
    return Verdict("II", 0.0, 0.8)                 # Step 5 fails


# ----- Seven worked examples from §4 -----
# (admissible, tau_stable, resolvable, expected_type)
EXAMPLES = [
    ("Russell",            False, True,  False, "III"),  # §4.1
    ("Liar (Tarski)",      False, True,  False, "III"),  # §4.2
    ("Berry",              True,  True,  False, "II"),   # §4.3
    ("Curry (ZFC)",        False, True,  False, "III"),  # §4.4
    ("CH (in ZFC)",        True,  True,  False, "II"),   # §4.5
    ("Newcomb",            True,  False, False, "IV"),   # §4.6
    ("Sorites",            True,  True,  False, "II"),   # §4.7
]


def test_examples() -> None:
    for name, adm, tau, res, expected in EXAMPLES:
        v = classify(adm, tau, res)
        assert v.type == expected, (
            f"{name}: expected Type {expected}, got Type {v.type}"
        )
        # score within stated range
        assert 0.0 <= v.score_lo <= v.score_hi <= 1.0
    print(f"OK seven examples ({len(EXAMPLES)}) classify as in §4.")


def test_mutual_exclusion() -> None:
    """Lemma 2.2: the classifier returns exactly one of {I, II, III, IV}
    for every assignment of the three predicates."""
    types_seen = set()
    for adm in (True, False):
        for tau in (True, False):
            for res in (True, False):
                v = classify(adm, tau, res)
                assert v.type in {"I", "II", "III", "IV"}
                types_seen.add(v.type)
    print(f"OK mutual exclusion: 2^3=8 input combos all map to one type.")


def test_exhaustiveness() -> None:
    """Lemma 2.3: on admissible + tau-stable inputs, every case is Type I
    or Type II (the resolvable / not-resolvable dichotomy)."""
    for res in (True, False):
        v = classify(True, True, res)
        assert v.type in {"I", "II"}
    print("OK exhaustiveness: admissible + tau-stable -> Type I or II.")


def test_score_ranges() -> None:
    """Def 3.2: score in [0,1]; Type I = 1.0; Type III = 0.0;
    Type II in [0, 0.8); Type IV in [0.3, 0.6]."""
    bounds = {
        "I":   (1.0, 1.0),
        "II":  (0.0, 0.8),
        "III": (0.0, 0.0),
        "IV":  (0.3, 0.6),
    }
    for adm in (True, False):
        for tau in (True, False):
            for res in (True, False):
                v = classify(adm, tau, res)
                lo_b, hi_b = bounds[v.type]
                assert v.score_lo == lo_b
                assert v.score_hi == hi_b
    print("OK score ranges per Def 3.2.")


def test_priority_order() -> None:
    """Verify that Type III precedes IV which precedes I/II (Lemma 2.2)."""
    # Inadmissible AND not tau-stable -> III (not IV)
    assert classify(False, False, True).type == "III"
    # Admissible but not tau-stable AND resolvable -> IV (not I)
    assert classify(True, False, True).type == "IV"
    print("OK priority III > IV > I/II.")


if __name__ == "__main__":
    test_examples()
    test_mutual_exclusion()
    test_exhaustiveness()
    test_score_ranges()
    test_priority_order()
    print("VERIFY OK J53")
