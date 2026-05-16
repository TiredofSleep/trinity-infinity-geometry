"""
Canonical tables from FORMULAS_AND_TABLES.md §5, §6, §6.7.
Single source of truth for this sync.
Transcribed verbatim; verified inline below.
"""

# §5 — TSML_10 (= TSML_Jordan). Canonical reference.
# H_TRUE = 7. From sprint18_b1_nscg_benchmark/impl/generator/generate_nscg.py.
TSML_10 = [
    [0,0,0,0,0,0,0,7,0,0],
    [0,7,3,7,7,7,7,7,7,7],
    [0,3,7,7,4,7,7,7,7,9],
    [0,7,7,7,7,7,7,7,7,3],
    [0,7,4,7,7,7,7,7,8,7],
    [0,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,7,7,7,7,7,7],
    [7,7,7,7,7,7,7,7,7,7],
    [0,7,7,7,8,7,7,7,7,7],
    [0,7,9,3,7,7,7,7,7,7],  # row 9: NOTE the (9,3)=3, (9,2)=9 per §5
]

# §6 — BHML_10. Canonical reference. Luther closure 2026-04-01.
BHML_10 = [
    [0,1,2,3,4,5,6,7,8,9],
    [1,2,3,4,5,6,7,2,6,6],
    [2,3,3,4,5,6,7,3,6,6],
    [3,4,4,4,5,6,7,4,6,6],
    [4,5,5,5,5,6,7,5,7,7],
    [5,6,6,6,6,6,7,6,7,7],
    [6,7,7,7,7,7,7,7,7,7],
    [7,2,3,4,5,6,7,8,9,0],
    [8,6,6,6,7,7,7,9,7,8],
    [9,6,6,6,7,7,7,0,8,0],
]

# σ permutation on Z/10Z (§2)
# σ = (0)(3)(8)(9)(1 7 6 5 4 2)
SIGMA = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9]

# Operator names
OPS = ["VOID","LATTICE","COUNTER","PROGRESS","COLLAPSE","BALANCE","CHAOS","HARMONY","BREATH","RESET"]

# Constants
T_STAR = (5, 7)        # 5/7
W = (3, 50)            # wobble 3/50
S_MAX = [(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)]
S_ADD = [(1,2),(2,1)]
H_TRUE = 7
UNITS_TRUE = [1, 3, 7, 9]
CORE_TRUE = [3, 7, 9]
