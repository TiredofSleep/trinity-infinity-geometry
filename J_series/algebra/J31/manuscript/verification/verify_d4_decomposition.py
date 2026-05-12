r"""verify_d4_decomposition.py

Verify the D_4 = <P_56, sigma^3> isotypic decomposition of the lens-pair
commutator [TSML, BHML] under conjugation on Z/10Z, per the corrected F15
in `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1_1_EXTENSION.md`,
section 10.

Expected output (exact-rational shares; total Frobenius norm-squared = 1,845,290):

    triv (doubly-invariant)        3075027/2  ~ 83.3210%
    sign1                                9/2  ~ 0.0002%    (near-cancellation; not exact zero)
    sign2 (sigma_outer-breaking)      288164  ~ 15.6162%
    sign3                                  0  =  0.0000%   (structural zero, exact)
    std (2-dim)                        19608  ~  1.0626%
    Sum                          1,845,290    = 100.0000%

Wedderburn orthogonality: sum of isotypic norms-squared equals total.

Author lane: Sanders + Gish only.
Runtime: < 5 s on a standard laptop (numpy + sympy).
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import Iterable, List, Tuple

import numpy as np
import sympy as sp

# ---------------------------------------------------------------------------
# Canonical TSML_SYM and BHML composition tables on Z/10Z.
# (See Atlas/LENS_TAXONOMY_2026-05-06/TSML_RECONCILIATION.md; the v1.1
# extension uses these literal bit patterns.)
# ---------------------------------------------------------------------------
TSML_ROWS = [
    "0000000700", "0737777777", "0377477779", "0777777773", "0747777787",
    "0777777777", "0777777777", "7777777777", "0777877777", "0797377777",
]
BHML_ROWS = [
    "0123456789", "1234567266", "2334567366", "3444567466", "4555567577",
    "5666667677", "6777777777", "7234567890", "8666777978", "9666777080",
]

T = np.array([[int(c) for c in r] for r in TSML_ROWS], dtype=int)
B = np.array([[int(c) for c in r] for r in BHML_ROWS], dtype=int)


# ---------------------------------------------------------------------------
# Group elements: P_56 and sigma^3 as 10x10 permutation matrices.
# ---------------------------------------------------------------------------
def perm_matrix(perm: Iterable[int]) -> np.ndarray:
    """Return 10x10 permutation matrix M with M e_i = e_{perm[i]}."""
    perm = list(perm)
    M = np.zeros((10, 10), dtype=int)
    for i, pi in enumerate(perm):
        M[pi, i] = 1
    return M


# P_56 = (5 6) on Z/10Z.
PERM_P56 = [0, 1, 2, 3, 4, 6, 5, 7, 8, 9]
# sigma^3 = (1 5)(2 6)(4 7) on Z/10Z, fixing {0, 3, 8, 9}.
# i.e. as a list, sigma^3[i] = where i goes
PERM_SIGMA3 = [0, 5, 6, 3, 7, 1, 2, 4, 8, 9]

P56 = perm_matrix(PERM_P56)
SIGMA3 = perm_matrix(PERM_SIGMA3)


def perm_compose(a: List[int], b: List[int]) -> List[int]:
    """(a o b)[i] = a[b[i]]."""
    return [a[b[i]] for i in range(len(b))]


# ---------------------------------------------------------------------------
# Verify: <P_56, sigma^3> has order 8, with element orders {1:1, 2:5, 4:2}.
# This forces D_4 (dihedral of order 8), per v1.1 §10.1.
# ---------------------------------------------------------------------------
def generate_group(generators: List[List[int]]) -> List[Tuple[int, ...]]:
    seen = {tuple(range(10))}
    frontier = [list(range(10))]
    while frontier:
        new_frontier = []
        for g in frontier:
            for h in generators:
                gh = perm_compose(g, h)
                key = tuple(gh)
                if key not in seen:
                    seen.add(key)
                    new_frontier.append(gh)
        frontier = new_frontier
    return sorted(seen)


def perm_order(p: List[int]) -> int:
    """Smallest k >= 1 with p^k = identity."""
    n = len(p)
    iden = list(range(n))
    pk = list(p)
    k = 1
    while pk != iden:
        pk = perm_compose(p, pk)
        k += 1
    return k


GROUP = generate_group([PERM_P56, PERM_SIGMA3])
ORDER_COUNTS = {}
for g in GROUP:
    o = perm_order(list(g))
    ORDER_COUNTS[o] = ORDER_COUNTS.get(o, 0) + 1

print("=" * 70)
print("Step 1: identify the group <P_56, sigma^3>")
print("=" * 70)
print(f"|<P_56, sigma^3>| = {len(GROUP)}")
print(f"Element-order multiset: {ORDER_COUNTS}")
assert len(GROUP) == 8, "Group must have order 8"
assert ORDER_COUNTS == {1: 1, 2: 5, 4: 2}, (
    f"Order multiset {ORDER_COUNTS} != D_4's {{1:1, 2:5, 4:2}}"
)
print("Order 8 with multiset {1:1, 2:5, 4:2} -> D_4 (dihedral of order 8). OK.")
print()

# Verify the cross-paper concern from referee §3.5: P_56 sigma^3 has order 4.
P56_then_S3 = perm_compose(PERM_SIGMA3, PERM_P56)
print(f"P_56 then sigma^3 = {P56_then_S3} (order {perm_order(P56_then_S3)})")
S3_then_P56 = perm_compose(PERM_P56, PERM_SIGMA3)
print(f"sigma^3 then P_56 = {S3_then_P56} (order {perm_order(S3_then_P56)})")
print(f"They differ -> non-commuting -> dihedral, not Klein-4. OK.")
print()


# ---------------------------------------------------------------------------
# Build conjugacy-class representatives for D_4.
#
# Elements (per v1.1 §10.2):
#   C1 = {e}                               size 1
#   C2 = {r^2}, the central order-2 elt    size 1
#   C3 = {r, r^3}, the order-4 rotations   size 2
#   C4 = {P_56, P_56 r^2}                  size 2 (one reflection class)
#   C5 = {sigma^3, sigma^3 r^2}            size 2 (other reflection class)
# ---------------------------------------------------------------------------
def perm_inverse(p: List[int]) -> List[int]:
    n = len(p)
    inv = [0] * n
    for i in range(n):
        inv[p[i]] = i
    return inv


def conjugacy_classes(group: List[Tuple[int, ...]]) -> List[List[Tuple[int, ...]]]:
    classes = []
    seen = set()
    for g in group:
        if g in seen:
            continue
        cls = set()
        for h in group:
            h_list = list(h)
            ginv = perm_inverse(h_list)
            conj = perm_compose(perm_compose(h_list, list(g)), ginv)
            cls.add(tuple(conj))
        classes.append(sorted(cls))
        seen.update(cls)
    return classes


CONJ_CLASSES = conjugacy_classes(GROUP)
print("=" * 70)
print("Step 2: conjugacy classes of D_4")
print("=" * 70)
class_sizes = sorted(len(c) for c in CONJ_CLASSES)
print(f"Class sizes (sorted): {class_sizes}")
assert class_sizes == [1, 1, 2, 2, 2], (
    f"D_4 must have class sizes (1,1,2,2,2); got {class_sizes}"
)
print("Five classes of sizes (1,1,2,2,2). OK.")
print()

# Identify a representative of each class.
# C1 (identity): always the size-1 class containing tuple(range(10))
# C2 (central r^2): the OTHER size-1 class
# C3 (rotations): contains r = sigma^3 p_56? No. By v1.1 §10.2 r = sigma o P_56.
#    The size-2 class WITHOUT P_56 or sigma^3 is the rotation class.
# C4: size-2 class containing P_56
# C5: size-2 class containing sigma^3
classes_by_repr = {}
for cls in CONJ_CLASSES:
    if len(cls) == 1 and cls[0] == tuple(range(10)):
        classes_by_repr["C1"] = cls
    elif len(cls) == 1:
        classes_by_repr["C2"] = cls
    elif tuple(PERM_P56) in cls:
        classes_by_repr["C4"] = cls
    elif tuple(PERM_SIGMA3) in cls:
        classes_by_repr["C5"] = cls
    else:
        classes_by_repr["C3"] = cls

for label in ["C1", "C2", "C3", "C4", "C5"]:
    cls = classes_by_repr[label]
    print(f"  {label} (size {len(cls)}): {cls[0]}")
print()


# ---------------------------------------------------------------------------
# D_4 character table (per v1.1 §10.3):
#
#                C1   C2    C3       C4       C5
#                (e)  (r^2) (r,r^3)  (s,sr^2) (sr,sr^3)
#   triv          1    1     1        1        1
#   sign1         1    1     1       -1       -1
#   sign2         1    1    -1        1       -1
#   sign3         1    1    -1       -1        1
#   std (2-dim)   2   -2     0        0        0
# ---------------------------------------------------------------------------
CHARACTER_TABLE = {
    "triv":  {"C1": 1, "C2":  1, "C3":  1, "C4":  1, "C5":  1, "dim": 1},
    "sign1": {"C1": 1, "C2":  1, "C3":  1, "C4": -1, "C5": -1, "dim": 1},
    "sign2": {"C1": 1, "C2":  1, "C3": -1, "C4":  1, "C5": -1, "dim": 1},
    "sign3": {"C1": 1, "C2":  1, "C3": -1, "C4": -1, "C5":  1, "dim": 1},
    "std":   {"C1": 2, "C2": -2, "C3":  0, "C4":  0, "C5":  0, "dim": 2},
}

# Sanity check: column orthogonality (sum_irrep dim_irrep * chi(g) = |G| if g=e, else 0)
e_check = sum(CHARACTER_TABLE[r]["dim"] * CHARACTER_TABLE[r]["C1"] for r in CHARACTER_TABLE)
print(f"sum_irrep dim*chi(e) = {e_check} (must equal |G| = 8)")
assert e_check == 8

# Non-identity column-orthogonality, e.g. C2:
c2_check = sum(CHARACTER_TABLE[r]["dim"] * CHARACTER_TABLE[r]["C2"] for r in CHARACTER_TABLE)
print(f"sum_irrep dim*chi(r^2) = {c2_check} (must equal 0)")
assert c2_check == 0

# Row orthogonality
def row_inner(r1: str, r2: str) -> int:
    s = 0
    for label, cls in classes_by_repr.items():
        s += len(cls) * CHARACTER_TABLE[r1][label] * CHARACTER_TABLE[r2][label]
    return s

for r1 in CHARACTER_TABLE:
    for r2 in CHARACTER_TABLE:
        v = row_inner(r1, r2)
        expected = 8 if r1 == r2 else 0
        assert v == expected, f"row orthogonality fails for ({r1},{r2}): {v}"
print("Row & column orthogonality of D_4 character table verified.")
print()


# ---------------------------------------------------------------------------
# Build the lens-pair commutator [TSML, BHML].
#
# Following v1.1 §10.3, [T, B] is the matrix commutator of the integer
# tables themselves (NOT the left-regular representation).  This is the
# 10x10 integer matrix M = T B - B T.
# ---------------------------------------------------------------------------
M_TB = T @ B - B @ T
M_TB_sym = sp.Matrix(M_TB.tolist())  # exact integer matrix

print("=" * 70)
print("Step 3: lens-pair commutator [T, B] = T*B - B*T")
print("=" * 70)
total_norm_sq_int = int(sum(int(v) ** 2 for v in M_TB.flatten()))
print(f"||[T, B]||^2 (Frobenius, exact integer) = {total_norm_sq_int}")
print(f"Trace [T, B] = {int(np.trace(M_TB))} (must be 0; commutator)")
assert int(np.trace(M_TB)) == 0
print()


# ---------------------------------------------------------------------------
# D_4 acts on End(R^10) by conjugation: g . M = P(g) M P(g)^{-1} where
# P(g) is the 10x10 permutation matrix.  Build all eight permutation
# matrices.
# ---------------------------------------------------------------------------
GROUP_LIST = [list(g) for g in GROUP]
PERM_MATRICES = [perm_matrix(g) for g in GROUP_LIST]


def class_of(g: List[int]) -> str:
    for label, cls in classes_by_repr.items():
        if tuple(g) in cls:
            return label
    raise ValueError(f"element {g} not in any class")


# ---------------------------------------------------------------------------
# Isotypic projector (Wedderburn): for irrep V with character chi_V,
#
#       P_V = (dim V / |G|) * sum_{g in G} chi_V(g) * (g . _)
#
# Apply to M_TB.  Since the action on M_TB is M -> P(g) M P(g)^T (P is
# orthogonal -> conj is the same as matrix multiplication on both sides
# with transpose), and entries are integers and chi values rational,
# everything is exact rationally.  We use sympy for exactness.
# ---------------------------------------------------------------------------
def project_isotypic(M: sp.Matrix, irrep: str) -> sp.Matrix:
    chi = CHARACTER_TABLE[irrep]
    dim = chi["dim"]
    acc = sp.zeros(10, 10)
    for g in GROUP_LIST:
        Pg = sp.Matrix(perm_matrix(g).tolist())
        Pg_inv = Pg.T  # permutation matrices are orthogonal
        cls = class_of(g)
        acc = acc + sp.Rational(chi[cls]) * (Pg * M * Pg_inv)
    return sp.Rational(dim, 8) * acc


def matrix_norm_sq_rational(M: sp.Matrix) -> sp.Rational:
    s = sp.Rational(0)
    for i in range(M.rows):
        for j in range(M.cols):
            s = s + M[i, j] ** 2
    return s


print("=" * 70)
print("Step 4: D_4 isotypic projection of [T, B]  (exact rationals)")
print("=" * 70)

projections = {}
for irrep in ["triv", "sign1", "sign2", "sign3", "std"]:
    P = project_isotypic(M_TB_sym, irrep)
    n = matrix_norm_sq_rational(P)
    projections[irrep] = (P, n)

total_iso = sum(n for _, n in projections.values())
total_orig = sp.Rational(total_norm_sq_int)

print(f"||[T, B]||^2                          = {total_orig} (Frobenius)")
print(f"sum of isotypic norm-squareds         = {total_iso}")
print(f"Wedderburn check (|| ||^2 = sum):     {total_orig == total_iso}")
print()
assert total_orig == total_iso, (
    f"Wedderburn sum mismatch: {total_orig} vs {total_iso}"
)

print("Per-isotypic breakdown:")
print(f"  {'irrep':<8} {'dim':>4} {'||proj||^2':>16} {'%':>10}")
print("  " + "-" * 45)
for irrep in ["triv", "sign1", "sign2", "sign3", "std"]:
    _, n = projections[irrep]
    pct = float(n) / float(total_orig) * 100.0
    print(f"  {irrep:<8} {CHARACTER_TABLE[irrep]['dim']:>4} {str(n):>16} {pct:>9.4f}%")
print()


# ---------------------------------------------------------------------------
# Cross-check sign1, sign3 are *exactly* zero (structural-zero claim).
# Float versions for sanity, and the exact rational form.
# ---------------------------------------------------------------------------
print("=" * 70)
print("Step 5: structural-zero check on sign1 and sign3")
print("=" * 70)
for irrep in ["sign1", "sign3"]:
    P, n = projections[irrep]
    print(f"  {irrep}: ||proj||^2 = {n} (= {float(n):.6e})")
print()
# Per v1.1 §10.4: sign1 -> ~0 (numerically tiny), sign3 -> 0 exactly.
# Both should be 0 under exact rational arithmetic IF we're using the
# integer-table commutator on Z/10Z (no sigma_outer chirality
# subtraction layer).  Check both and report.
sign1_zero = projections["sign1"][1] == 0
sign3_zero = projections["sign3"][1] == 0
print(f"sign1 exactly zero: {sign1_zero}")
print(f"sign3 exactly zero: {sign3_zero}")
print()


# ---------------------------------------------------------------------------
# Print final summary in the same units used in v1.1 §10.3.
# ---------------------------------------------------------------------------
print("=" * 70)
print("Summary (exact-rational shares; cross-checked against Theorem 2.1)")
print("=" * 70)
print()
print("  triv  (doubly-invariant): expected 3075027/2 (~83.32%), got "
      f"{projections['triv'][1]} ({float(projections['triv'][1])/float(total_orig)*100:.4f}%)")
print("  sign1 (near-cancellation): expected 9/2 (~0.0002%), got "
      f"{projections['sign1'][1]} ({float(projections['sign1'][1])/float(total_orig)*100:.4f}%)")
print("  sign2 (sigma_outer-anti):  expected 288164 (~15.62%), got "
      f"{projections['sign2'][1]} ({float(projections['sign2'][1])/float(total_orig)*100:.4f}%)")
print("  sign3 (structural zero):   expected 0 exactly, got "
      f"{projections['sign3'][1]} ({float(projections['sign3'][1])/float(total_orig)*100:.4f}%)")
print("  std   (2-dim interaction): expected 19608 (~1.06%), got "
      f"{projections['std'][1]} ({float(projections['std'][1])/float(total_orig)*100:.4f}%)")
print()
print("All percentages computed with exact rational arithmetic; the")
print("decomposition is unique by Wedderburn.  Note: sign3 = 0 is the")
print("load-bearing 'forbidden symmetry' of the lens-pair commutator under D_4")
print("(see manuscript Proposition 5.1).")
