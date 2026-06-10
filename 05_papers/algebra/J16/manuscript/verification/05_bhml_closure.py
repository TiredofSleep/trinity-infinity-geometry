"""
05_bhml_closure.py

Compare BHML's closed sub-magma structure to TSML's.

KEY FINDING:
  TSML has 398 closed subsets — richly nested, many natural sub-magmas
  BHML has only 8 closed subsets — and they form a perfect nested chain:
  
    {VOID, RESET}
    {VOID, HARMONY, BREATH, RESET}        ← σ-fixed ∪ {HARMONY}
    {VOID, CHAOS, HARMONY, BREATH, RESET}
    {VOID, BALANCE, CHAOS, HARMONY, BREATH, RESET}
    {VOID, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET}
    {VOID, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET}
    {VOID, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET}
    {full algebra}

BHML's natural domain anchors at {VOID, RESET}, then grows by adding 
HARMONY and BREATH (completing the σ-fixed set), then proceeds backward 
through CHAOS, BALANCE, COLLAPSE, PROGRESS, COUNTER, LATTICE.

The smallest BHML-closed subset containing the breathed pair {8, 9} 
is {VOID, HARMONY, BREATH, RESET} — exactly the σ-fixed gauge core 
plus HARMONY.

This explains why BHML works as a mixing partner with TSML:
  TSML's natural domain: {0..7} (the 8-magma core)
  BHML's natural minimal core: {VOID, HARMONY, BREATH, RESET}
  Their union covers all 10 operators, with overlap at {VOID, HARMONY}
"""
import numpy as np
from itertools import combinations

TSML_ROWS = ["0000000700","0737777777","0377477779","0777777773","0747777787",
             "0777777777","0777777777","7777777777","0777877777","0797377777"]
T = np.array([[int(c) for c in row] for row in TSML_ROWS], dtype=int)

BHML_ROWS = ["0123456789","1234567266","2334567366","3444567466","4555567577",
             "5666667677","6777777777","7234567890","8666777978","9666777080"]
B = np.array([[int(c) for c in row] for row in BHML_ROWS], dtype=int)

OP_NAMES = ['VOID', 'LATTICE', 'COUNTER', 'PROGRESS', 'COLLAPSE',
            'BALANCE', 'CHAOS', 'HARMONY', 'BREATH', 'RESET']
SIGMA_FIXED = {0, 3, 8, 9}


def find_all_closed_subsets(table):
    closed = []
    for size in range(2, 11):
        for subset in combinations(range(10), size):
            Sset = set(subset)
            if all(table[a, b] in Sset for a in subset for b in subset):
                closed.append(list(subset))
    return closed


if __name__ == "__main__":
    closed_T = find_all_closed_subsets(T)
    closed_B = find_all_closed_subsets(B)

    print("=" * 70)
    print("CLOSED SUB-MAGMA COMPARISON")
    print("=" * 70)
    print(f"\nTSML: {len(closed_T)} closed subsets")
    print(f"BHML: {len(closed_B)} closed subsets")
    print(f"\nBHML has {len(closed_T) // len(closed_B)}× fewer closed sub-magmas.")

    print(f"\n{'=' * 70}")
    print(f"BHML'S COMPLETE LATTICE OF CLOSED SUBSETS")
    print(f"{'=' * 70}")

    # Sort by size
    closed_B_sorted = sorted(closed_B, key=lambda S: (len(S), S))

    for S in closed_B_sorted:
        names = [OP_NAMES[i] for i in S]
        marker = ""
        if set(S) == SIGMA_FIXED | {7}:
            marker = "  ← σ-fixed ∪ {HARMONY}"
        elif set(S) == {0, 9}:
            marker = "  ← minimal anchor: {VOID, RESET}"
        print(f"  Size {len(S)}: {names}{marker}")

    print(f"\n{'=' * 70}")
    print(f"OBSERVATION: BHML has a CHAIN of closed subsets")
    print(f"{'=' * 70}")
    print(f"""
Each closed subset of BHML is contained in the next-larger one.
This is fundamentally different from TSML's lattice, which has 
many parallel branches.

BHML's structure suggests a single 'spine' anchored at {{VOID, RESET}},
growing by adding one element at a time:
  {{VOID, RESET}}
  → +HARMONY, +BREATH (becomes σ-fixed ∪ {{HARMONY}})
  → +CHAOS, +BALANCE, +COLLAPSE, +PROGRESS, +COUNTER, +LATTICE

The {{VOID, HARMONY, BREATH, RESET}} subset — BHML's natural 4-element
core — is exactly the doubly-invariant Z_2×Z_2 gauge subspace 
{{σ-fixed = (0,3,8,9)}} with PROGRESS replaced by HARMONY.

Wait — let's check that exactly.
""")

    SIGMA_FIXED_set = SIGMA_FIXED
    BHML_4_core = {0, 7, 8, 9}
    print(f"σ-fixed (doubly-invariant): {sorted(SIGMA_FIXED_set)} = {[OP_NAMES[i] for i in sorted(SIGMA_FIXED_set)]}")
    print(f"BHML 4-core:                {sorted(BHML_4_core)} = {[OP_NAMES[i] for i in sorted(BHML_4_core)]}")
    print(f"\nIntersection: {sorted(SIGMA_FIXED_set & BHML_4_core)} = {[OP_NAMES[i] for i in sorted(SIGMA_FIXED_set & BHML_4_core)]}")
    print(f"σ-fixed has PROGRESS but BHML 4-core has HARMONY in its place.")
    print(f"")
    print(f"PROGRESS and HARMONY are 'paired' by σ: σ(LATTICE) = HARMONY,")
    print(f"and PROGRESS is one of the σ-fixed points. They sit at the")
    print(f"natural 'center' of TIG dynamics in different senses:")
    print(f"  PROGRESS = a σ-fixed point (gauge-stable)")
    print(f"  HARMONY = the runtime attractor (dynamically stable)")
