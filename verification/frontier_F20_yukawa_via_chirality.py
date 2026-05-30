#!/usr/bin/env python3
# ============================================================
# frontier_F20_yukawa_via_chirality.py
#
# F20 frontier: Yukawa structure via J37 Cl(0,10) chirality
# + 1+3+5+7 substrate decomposition.
#
# CONTEXT (per F15 closure of direct substrate-Yukawa anchor):
#   F15 closed the question of whether substrate first principles
#   predict y_t(M_X) directly (verdict: SUBSTRATE INDEPENDENT, the
#   GUT-scale top-Yukawa is RG-determined from the M_Z anchor).
#   The natural next entry point is the CHIRALITY STRUCTURE of
#   J37 Cl(0,10): the 32-dim spinor splits as 16 + 16 (left + right),
#   and J37 documents that each 16 further decomposes as 1+3+5+7
#   matching kernel base + substrate strand primes.
#
# QUESTION:
#   Does the 1+3+5+7 substrate decomposition correspond to a
#   representation-theoretic decomposition of the 16 of SO(10)
#   under some subgroup G? If so, do 16 x 16 x Higgs Yukawa
#   contractions decompose substrate-wise in a way that gives
#   any Yukawa prediction?
#
# OUTPUT: bounded honest scoping (CLEAR / PARTIAL / COINCIDENCE
# / NO-CORRESPONDENCE).
# ============================================================

from __future__ import annotations
import math
import sys
from itertools import combinations, product

# Standard SO(10) GUT facts (textbook, e.g. Slansky 1981):
#   - 16 of SO(10) splits under SU(5) x U(1) as:
#       1_{-5} + 5bar_{3} + 10_{-1}
#     i.e. 1 + 5 + 10 = 16, with U(1) charges (-5, +3, -1).
#   - One SM fermion generation = 16:
#       Q_L  (3, 2, 1/6)   in 10
#       u_R^c (3bar, 1, -2/3) in 10
#       e_R^c (1, 1, +1)    in 10
#       d_R^c (3bar, 1, +1/3) in 5bar
#       L_L  (1, 2, -1/2)  in 5bar
#       nu_R^c (1, 1, 0)   in 1
#
# Yukawa structure: 16 x 16 (antisymmetric) decomposes as
#       16 x 16 = 10 + 120 + 126   (sym part = 10 + 126; anti = 120)
#   Actually 16 x 16 = 10_s + 120_a + 126_s with subscripts denoting
#   symmetric/antisymmetric (since 16 is complex).
#   Total: 10 + 120 + 126 = 256 = 16^2.  CORRECT.
#
# So Yukawa terms 16 . 16 . phi for phi in {10, 120, 126}.
#
# ============================================================
# QUESTION 1: Is 1+3+5+7 a Lie-algebraic decomposition of 16
# under any subgroup G of SO(10)?
# ============================================================
#
# Candidate subgroups and their irreps that could sum to 16:
#
# G = SU(5) x U(1):   1 + 5bar + 10 = 16  YES (standard SU(5) decomp)
#                    Does NOT give 1+3+5+7. (5 ne 3, 10 ne 7, no 3.)
#
# G = SU(4) x SU(2) x SU(2) (Pati-Salam):
#                    16 = (4, 2, 1) + (4bar, 1, 2) = 8 + 8
#                    Does NOT give 1+3+5+7.
#
# G = SU(2)_L x SU(2)_R x SU(4):  same as above.
#
# G = SO(8) (via SO(10) -> SO(9) -> SO(8)):
#   SO(8) spinor irreps: 8_s, 8_c, 8_v all 8-dim.
#   SO(9) spinor is 16. Branching 16 -> SO(8): 8_s + 8_c.
#   Does NOT give 1+3+5+7.
#
# G = SO(7) (subgroup of SO(10) via SO(10) -> SO(7) x SO(3)):
#   SO(7) spinor is 8-dim.
#   Does NOT give 1+3+5+7.
#
# G = SO(5) x SO(5):
#   SO(5) spinor is 4-dim (Sp(4) = Spin(5)).
#   16 = 4 x 4 = (4, 4).
#   Does NOT give 1+3+5+7.
#
# G = SU(2) (single):
#   SU(2) irreps have dim 2j+1 for j = 0, 1/2, 1, 3/2, ...
#   So 1+3+5+7 IS a decomposition under SU(2) for j = 0, 1, 2, 3:
#       j = 0: dim 1
#       j = 1: dim 3
#       j = 2: dim 5
#       j = 3: dim 7
#   Total = 16. YES.
#
#   IS there an embedding SU(2) -> SO(10) whose 16-spinor
#   branches as j = 0 + 1 + 2 + 3?  This is a SU(2)-PRINCIPAL
#   embedding question.
#
# G = SO(3) (which is SU(2)/Z2):
#   Real irreps of SO(3) have dim 2l+1 for l = 0, 1, 2, 3, ...
#   Same dimensions: 1, 3, 5, 7. Same question as SU(2).
#
# This gives us a focused candidate: the PRINCIPAL SU(2) embedding
# (or equivalent SO(3)) such that the 16 branches as
#   16 = (j=0) + (j=1) + (j=2) + (j=3)
#
# QUESTION: does this embedding exist?
# ============================================================
#
# THEORY: any semisimple Lie group G of rank r has a PRINCIPAL
# sl(2)-triple (a Jacobson-Morozov sl(2) embedded as the principal
# nilpotent + its centralizer). The principal sl(2) is unique up
# to conjugacy. Branching irreps of G under the principal sl(2)
# gives an explicit decomposition.
#
# For SO(10) = D_5 the principal sl(2) is known. The 16-spinor
# rep's branching under the principal sl(2) of so(10) is computed
# from the exponents of so(10): {1, 3, 5, 7, 9} (for D_n, the
# exponents are 1, 3, ..., 2n-3, n-1; for D_5 = so(10) this is
# {1, 3, 5, 7, 4}).
#
# Actually for so(10) the exponents are {1, 3, 5, 7, 9} with the
# adjoint branching as sum of spin-(e_i)/2 irreps... but for
# the 16-spinor we need the SPINOR branching.
#
# The spinor of so(2n) under the principal sl(2): the highest
# weight of the spinor is (1/2, 1/2, ..., 1/2) so the projection
# onto the principal sl(2) (Cartan element 2*rho^v) gives the
# highest sl(2)-weight as:
#   2*rho^v . omega_spinor = sum of half-weights * 2 = n*(n-1)/2 ... need careful
#
# Empirical fact: for so(10) the principal sl(2) branches the
# 16-spinor as a sum of SU(2) irreps whose dimensions are computed
# from the spinor weights' projection on the principal sl(2)
# Cartan generator.
# ============================================================

print("="*70)
print("F20: Yukawa via J37 Cl(0,10) chirality + 1+3+5+7")
print("="*70)
print()

# ============================================================
# Step 1: Check dim-count consistency (sanity)
# ============================================================
print("Step 1: dimension-count sanity checks.")
print()

substrate_decomp = [1, 3, 5, 7]
assert sum(substrate_decomp) == 16, "substrate decomp must sum to 16"
print(f"  substrate 1+3+5+7 = {sum(substrate_decomp)} = 16  PASS")

# Standard SU(5) decomposition of 16 of SO(10):
su5_decomp = [1, 5, 10]
assert sum(su5_decomp) == 16
print(f"  SU(5) 1+5bar+10 = {sum(su5_decomp)} = 16  PASS")

# 16 x 16 = 10 + 120 + 126
yukawa = [10, 120, 126]
assert sum(yukawa) == 256, "Yukawa 10+120+126 must sum to 256"
print(f"  Yukawa 10+120+126 = {sum(yukawa)} = 256 = 16^2  PASS")
print()

# ============================================================
# Step 2: Test 1+3+5+7 as SU(2) (or SO(3)) decomposition.
# ============================================================
print("Step 2: Test 1+3+5+7 as branching under SU(2) / SO(3).")
print()

# SU(2) irrep of dimension 2j+1.
# 1+3+5+7 corresponds to j = 0, 1, 2, 3 (integer spins).
print("  SU(2) irreps: dim = 2j+1 for j = 0, 1, 2, 3 give 1, 3, 5, 7.")
print("  Sum = 16.")
print()
print("  CANDIDATE: principal SU(2) embedding inside SO(10).")
print("  -> 16 of SO(10) might branch under principal SU(2) as")
print("     j = 0 + j = 1 + j = 2 + j = 3.")
print()

# Compute the principal sl(2) branching for so(10).
# The principal sl(2) has Cartan generator 2*rho^v where rho^v is
# the half-sum of positive coroots. For so(10) = D_5:
#   positive coroots = positive roots (D_5 is simply-laced)
#   rho = (4, 3, 2, 1, 0) in the standard orthogonal basis e_1, ..., e_5
#   2*rho = (8, 6, 4, 2, 0)
#
# The 16-spinor weights are
#   (+-1/2, +-1/2, +-1/2, +-1/2, +-1/2) with even number of minus signs.
# (chiral 16)
#
# The principal sl(2) Cartan element h = 2*rho^v acts on weight mu by
# multiplication 2*rho^v . mu = (8, 6, 4, 2, 0) . mu.
#
# For each 16-spinor weight, compute h.mu.

def spinor_weights_16():
    """Return all 16 weights of the chiral 16 of so(10) as tuples
    of half-integers (eps_1/2, ..., eps_5/2) with even number of -1.
    """
    weights = []
    for signs in product([+1, -1], repeat=5):
        if signs.count(-1) % 2 == 0:  # chiral 16 has even number of -1
            w = tuple(s * 0.5 for s in signs)
            weights.append(w)
    return weights

def principal_h_action(weight):
    """Action of principal Cartan h = 2*rho = (8, 6, 4, 2, 0) on weight."""
    rho2 = (8, 6, 4, 2, 0)
    return sum(r * w for r, w in zip(rho2, weight))

weights = spinor_weights_16()
print(f"  Number of 16-spinor weights (chiral, even -1): {len(weights)}")
assert len(weights) == 16
print()

# Compute h-eigenvalues
h_eigs = sorted([principal_h_action(w) for w in weights], reverse=True)
print(f"  Principal sl(2) h-eigenvalues on 16:")
print(f"  {h_eigs}")
print()

# An SU(2) irrep of spin j contains weights -j, -j+1, ..., j-1, j (each once).
# To decompose, find the highest h-eigenvalue lambda_max; this is 2j_max.
# Then peel off the irrep of spin j_max which contains weights
# {-j_max, -j_max+1, ..., j_max} (2j_max+1 of them). Repeat.

def decompose_sl2(h_eig_list):
    """Greedy peel-off of SU(2) irreps from a list of h-eigenvalues."""
    remaining = list(h_eig_list)
    irrep_dims = []
    while remaining:
        lam_max = max(remaining)
        j = lam_max / 2.0
        dim = int(round(2 * j + 1))
        # Expected weights: lam_max, lam_max - 2, ..., -lam_max  (step 2 in h-eigval)
        expected = [lam_max - 2 * k for k in range(dim)]
        new_remaining = list(remaining)
        for e in expected:
            # Find a matching entry (within tolerance)
            found = False
            for r in new_remaining:
                if abs(r - e) < 1e-9:
                    new_remaining.remove(r)
                    found = True
                    break
            if not found:
                return None  # decomposition fails
        remaining = new_remaining
        irrep_dims.append(dim)
    return sorted(irrep_dims)

dims = decompose_sl2(h_eigs)
print(f"  SU(2) irrep decomposition of 16 under principal sl(2):")
print(f"  dims = {dims}  (sum = {sum(dims) if dims else 'N/A'})")
print()

if dims == sorted([1, 3, 5, 7]):
    print("  >> MATCH: 1+3+5+7 IS the principal sl(2) branching of 16.")
    principal_match = True
else:
    print(f"  >> NO MATCH: principal sl(2) gives {dims}, not 1+3+5+7.")
    principal_match = False
print()

# ============================================================
# Step 3: If principal SU(2) doesn't match, look for SUB-PRINCIPAL
# embeddings (other sl(2)-triples) that DO give 1+3+5+7.
# ============================================================
print("Step 3: Search for other sl(2) embeddings giving 1+3+5+7.")
print()

# Any sl(2) embedding in so(10) has a Cartan generator H that
# is a non-negative integer combination of simple coroots.
# The orbit of nilpotent elements under SO(10) is parameterized
# by partitions of 10 (for orthogonal Lie algebras, partitions
# in which even parts have even multiplicity).
#
# Each nilpotent orbit determines an sl(2)-triple up to conjugacy.
# The branching of the 16-spinor under each such sl(2) is a
# representation-theoretic computation.
#
# For brevity we enumerate the possible h-eigenvalue patterns:
# any sl(2) embedding gives a decomposition of 16 into SU(2)
# irreps whose dimensions are 2j_i + 1 with sum = 16.
#
# Partitions of 16 into ODD parts (since SU(2) irreps have
# dim = 2j+1 which is odd-or-even depending on integer/half-integer
# spin; for the chiral 16 to decompose into INTEGER-spin irreps
# requires the Cartan to act with integer eigenvalues on all
# spinor weights, which depends on the embedding).

# Generate all partitions of 16 into parts from {1, 3, 5, 7, 9, 11, 13, 15}
def partitions_of(n, allowed_parts):
    """Return all sorted-decreasing partitions of n using parts from allowed_parts."""
    allowed = sorted(allowed_parts, reverse=True)
    results = []
    def helper(remaining, start_idx, current):
        if remaining == 0:
            results.append(tuple(current))
            return
        for i in range(start_idx, len(allowed)):
            p = allowed[i]
            if p <= remaining:
                helper(remaining - p, i, current + [p])
    helper(n, 0, [])
    return results

odd_parts_16 = partitions_of(16, [1, 3, 5, 7, 9, 11, 13, 15])
print(f"  Partitions of 16 into odd parts (integer-spin SU(2) decomps):")
print(f"  Total: {len(odd_parts_16)}")
print()

# Mark 1+3+5+7 specially:
target = tuple(sorted([7, 5, 3, 1], reverse=True))
if target in odd_parts_16:
    print(f"  Target partition {target} IS in the list.")
    idx = odd_parts_16.index(target)
    print(f"  Position: {idx + 1} of {len(odd_parts_16)}.")
print()

# Of these partitions, which correspond to actual sl(2) embeddings
# in so(10) such that the 16-spinor branches that way?
#
# This is a representation-theoretic computation. For SO(10) = D_5,
# the nilpotent orbits are classified by "type-D partitions of 10":
# partitions where even parts occur with even multiplicity.
#
# For each nilpotent orbit lambda (partition of 10 of type D), the
# associated sl(2) triple branches the 10-vector V as
#   V = sum_i Sym^{lambda_i - 1}(C^2)
# and the spinor 16 branches in a more complex way.
#
# For the case of the PRINCIPAL nilpotent (partition (9, 1) since
# in D_5 there's no all-odd partition (10) — even-parts-even-mult
# rule), the 10-vector branches as
#   10 = Sym^8 + Sym^0 = 9 + 1 (j = 4 + j = 0)
# and the 16-spinor branches accordingly.
#
# The "subregular" nilpotent (partition (7, 3)) gives a different
# branching, and so on.
#
# We will check by direct computation: for each partition lambda of
# 10 (type D), compute the 16-spinor branching.

def is_type_D_partition(parts, n):
    """A partition of n is type D if even parts appear with even multiplicity."""
    if sum(parts) != n:
        return False
    from collections import Counter
    c = Counter(parts)
    for p, mult in c.items():
        if p % 2 == 0 and mult % 2 != 0:
            return False
    return True

def all_partitions(n):
    """All partitions of n (sorted decreasing)."""
    if n == 0:
        return [()]
    results = []
    def helper(remaining, max_part, current):
        if remaining == 0:
            results.append(tuple(current))
            return
        for p in range(min(remaining, max_part), 0, -1):
            helper(remaining - p, p, current + [p])
    helper(n, n, [])
    return results

partitions_10 = all_partitions(10)
type_D_partitions = [p for p in partitions_10 if is_type_D_partition(p, 10)]
print(f"  Type-D partitions of 10 (nilpotent orbits of so(10)):")
for p in type_D_partitions:
    print(f"    {p}")
print(f"  Total: {len(type_D_partitions)}")
print()

# For each type-D partition lambda = (lambda_1, ..., lambda_k) of 10,
# compute the 16-spinor branching under the corresponding sl(2).
#
# Method: the 10-vector V decomposes as
#   V = sum_i V_{lambda_i}   (where V_d is the d-dim irrep of sl(2))
# The spinor S of so(10) is built from V via Clifford algebra:
#   S = exterior algebra Lambda^*(V_+) / sign-relations
# where V_+ is a Lagrangian subspace.
#
# For computing the sl(2) action on S, we use the fact that the
# spinor weights are (+-1/2, ..., +-1/2) and the sl(2) Cartan
# eigenvalue on a spinor weight is sum_i +- (h_i / 2) where h_i
# are the sl(2) eigenvalues on the basis vectors e_i of V.
#
# For lambda = (lambda_1, ..., lambda_k), the sl(2) eigenvalues
# on the 10-vector basis (in suitable basis) are:
# for each block of size lambda_i, eigenvalues are
#   (lambda_i - 1, lambda_i - 3, ..., -(lambda_i - 1)).
#
# But for the SPINOR, we need eigenvalues 1/2 of these (since
# spinor weights are 1/2-integer combinations).
#
# Actually for the chiral 16 of so(10): weights are
# (1/2)(eps_1, ..., eps_5) with eps_i = +-1 and even number of -1.
# Under an sl(2) embedded with Cartan acting on the 10-vector with
# eigenvalues {+-a_1, +-a_2, ..., +-a_5} (so(10) is type D, must
# come in +- pairs since so(10) preserves a symmetric bilinear form),
# the spinor Cartan eigenvalue on weight (eps_1/2, ..., eps_5/2) is
#   (1/2) sum_i eps_i * a_i.
#
# So for a partition lambda of 10 with sl(2) eigenvalues on the
# 10-vector being a multiset E, we need to extract the values a_1, ..., a_5
# (the "positive half" of E) and then compute (1/2) * sum eps_i a_i
# for all 16 sign vectors with even # of -1.

def sl2_eigenvalues_on_vector(partition):
    """Eigenvalues of the principal sl(2) of a nilpotent orbit
    on the 10-vector. Each block of size d contributes
    eigenvalues (d-1, d-3, ..., -(d-1))."""
    eigs = []
    for d in partition:
        eigs.extend([d - 1 - 2 * k for k in range(d)])
    return eigs

def spinor_branching(partition):
    """Compute SU(2) irrep dim multiset for the chiral 16 of so(10)
    under the sl(2) of nilpotent orbit `partition`."""
    vec_eigs = sl2_eigenvalues_on_vector(partition)
    if len(vec_eigs) != 10:
        return None
    # so(10) preserves a symmetric form; the eigenvalues should come
    # in +/- pairs. Extract 5 "positive" values (with sign).
    # In an orthogonal basis e_1, e_1', e_2, e_2', ..., e_5, e_5',
    # the form pairs e_i with e_i' so their eigenvalues are negatives.
    # Sort eigenvalues; take the 5 largest (a_i with sign convention).
    sorted_eigs = sorted(vec_eigs, reverse=True)
    # Check: eigenvalues come in +/- pairs?
    # For a sl(2) in so(10), the vector representation must be
    # self-dual (since so(10) preserves a symmetric form), so the
    # multiset of eigenvalues is symmetric under e -> -e.
    eigs_check = sorted([-e for e in vec_eigs])
    if eigs_check != sorted(vec_eigs):
        # Not a valid so(10) sl(2)
        return None

    # Pair eigenvalues: for each positive a, there should be a -a.
    # Pick the 5 "positive part" values (one per pair). For zero
    # eigenvalues these are degenerate; for simplicity take half
    # of the multiset.
    from collections import Counter
    c = Counter(vec_eigs)
    half = []
    seen = Counter()
    for e in sorted(set(vec_eigs), reverse=True):
        if e > 0:
            # Take c[e] copies
            half.extend([e] * c[e])
        elif e == 0:
            # Take c[0] // 2 copies of 0
            half.extend([0] * (c[0] // 2))
    if len(half) != 5:
        # Try a different pairing if zero count is odd
        # For type D so(10), zero eigenvalues must come in pairs
        return None

    # Now compute spinor eigenvalues:
    # For each of the 16 sign vectors (eps_1, ..., eps_5) with even
    # number of -1, compute (1/2) sum eps_i a_i.
    spinor_eigs = []
    for signs in product([+1, -1], repeat=5):
        if signs.count(-1) % 2 == 0:  # chiral 16
            val = 0.5 * sum(s * a for s, a in zip(signs, half))
            spinor_eigs.append(val)
    assert len(spinor_eigs) == 16
    return decompose_sl2(spinor_eigs)

print("  Spinor branching under sl(2) for each type-D nilpotent of so(10):")
print()
for p in type_D_partitions:
    br = spinor_branching(p)
    match = " <--- MATCHES 1+3+5+7!" if br == sorted([1, 3, 5, 7]) else ""
    print(f"    nilpotent {str(p):20s} ->  16-spinor: {br}{match}")
print()

# ============================================================
# Step 4: Subgroup decomposition search (other approach)
# ============================================================
print("Step 4: Subgroup decomposition: find G s.t. 16 -> 1+3+5+7.")
print()

# Standard low-rank irreducible representations and their dimensions:
# SU(2) at dim 1, 3, 5, 7, ... (integer spin)
# SO(3) same
# SU(3) at dim 1, 3, 3bar, 6, 6bar, 8, 10, 15, 27, ...
# SO(4) = SU(2) x SU(2): dims (2j_L+1)(2j_R+1)
# SU(4): 1, 4, 4bar, 6, 10, 10bar, 15, 20, ...
# SO(5) = Sp(4): 1, 4, 5, 10, 14, 16, ...
# SO(6) = SU(4): same as SU(4)
# SO(7): 1, 7, 8, 21, 27, 35, 48, ...
# SO(8): 1, 8 (3 copies for triality), 28, 35 (3 copies), 56 (3 copies), ...
# SO(9): 1, 9, 16, 36, 44, 84, 126, 128, ...
# G_2: 1, 7, 14, 27, ...
# F_4: 1, 26, 52, 273, ...
#
# For 1+3+5+7 = 16 partition:
#
# - SU(2) [or SO(3)]: irreps 1, 3, 5, 7 are integer-spin reps. Match.
#   (Tested in Step 3 above.)
#
# - SO(7) has irreps 1, 7. Two copies of 7 + 1 + 1 = 16. Can we get 1+3+5+7
#   under SO(7)? 3, 5 are not standard SO(7) irrep dims. NO.
#
# - SU(2) x U(1): can decompose using SU(2) irreps + U(1) charges.
#   1+3+5+7 = singlets + triplet + quintet + septet under SU(2).
#   This is essentially the SU(2) story with extra U(1) labels.
#   Could correspond to an SU(2) embedded in SO(10) plus a U(1)
#   commuting with it. The natural commutant of principal SU(2)
#   in SO(10) is trivial (since principal SU(2) maximizes spread).
#   But sub-principal SU(2)s can have a non-trivial commutant.
#
# So the FUNDAMENTAL question reduces to: which sl(2) embedding in
# so(10) (if any) branches 16 as 1+3+5+7?
#
# Step 3 enumerated all nilpotent orbits and computed branchings.

# ============================================================
# Step 5: Test 1+3+5+7 against ALL valid sl(2) embeddings.
# ============================================================
print("Step 5: Summary of sl(2) branchings of 16 under all nilpotent orbits.")
print()
match_found = False
for p in type_D_partitions:
    br = spinor_branching(p)
    if br == sorted([1, 3, 5, 7]):
        match_found = True
        print(f"  >>> nilpotent {p} gives 16 -> 1+3+5+7 <<<")
print()
if not match_found:
    print("  >>> NO nilpotent sl(2) orbit branches 16 as 1+3+5+7. <<<")
    print()
    print("  Conclusion: 1+3+5+7 is NOT a representation-theoretic")
    print("  decomposition of the 16-spinor of SO(10) under any")
    print("  sl(2) subgroup.")
print()

# ============================================================
# Step 6: 16 x 16 substrate decomposition (if no rep-theory match)
# ============================================================
print("Step 6: Substrate-wise 16 x 16 decomposition.")
print()
# Even if 1+3+5+7 isn't a Lie-algebraic decomposition, we can ask
# what the naive substrate-wise Yukawa contraction looks like.
#
# Tensor product (1+3+5+7) x (1+3+5+7) = ?
# Naively: 1*1 + 1*3 + 1*5 + 1*7 + 3*1 + 3*3 + 3*5 + 3*7 + ...
# Total = 16*16 = 256.
# Block sizes:
labels = [1, 3, 5, 7]
print(f"  Substrate-wise 16 x 16 block structure:")
print(f"  {'':>6}" + "".join(f"{b:>6}" for b in labels))
for a in labels:
    row = f"{a:>6}"
    for b in labels:
        row += f"{a*b:>6}"
    print(row)
print(f"  Total: {sum(a*b for a in labels for b in labels)}")
print()

print("  Standard SO(10) 16 x 16 = 10 + 120 + 126 = 256.")
print()

# If 1+3+5+7 were an SU(2) decomp, we could use SU(2) Clebsch-Gordan:
# j1 x j2 = |j1 - j2| + ... + (j1 + j2)
# For 1+3+5+7 = j = 0, 1, 2, 3 of SU(2):
# (0+1+2+3) x (0+1+2+3) = full SU(2) Clebsch sum

def su2_tensor(j1, j2):
    """SU(2) tensor product: returns list of irrep dims for j1 x j2."""
    j_min = abs(j1 - j2)
    j_max = j1 + j2
    return [int(2 * j + 1) for j in [j_min + i for i in range(j_max - j_min + 1)]]

js = [0, 1, 2, 3]
total_irreps = []
for j1 in js:
    for j2 in js:
        total_irreps.extend(su2_tensor(j1, j2))

from collections import Counter
su2_count = Counter(total_irreps)
print(f"  If 1+3+5+7 were SU(2) j=0,1,2,3, then tensor square contains:")
for dim in sorted(su2_count.keys()):
    print(f"    {dim:>3}-dim irrep:  multiplicity {su2_count[dim]}")
print(f"  Total dimension: {sum(d * m for d, m in su2_count.items())}")
print()

# Compare to standard SO(10) Yukawa: 10 + 120 + 126
print(f"  Standard SO(10) Yukawa: 10 + 120 + 126 = 256.")
print(f"  Under SU(2) (j=0,1,2,3 inside), 10, 120, 126 would have to")
print(f"  branch into the SU(2) multiplicities above for the substrate")
print(f"  decomposition to make Yukawa sense.")
print()

# ============================================================
# Step 7: Detailed analysis of the (5, 5) nilpotent orbit
# ============================================================
print("="*70)
print("Step 7: Detailed analysis of the (5, 5) nilpotent orbit")
print("="*70)
print()
print("  The (5, 5) partition of 10 corresponds to a nilpotent orbit in so(10)")
print("  whose associated sl(2)-triple branches the 10-vector as")
print()

# 10-vector branching for (5, 5)
p55 = (5, 5)
vec_eigs_55 = sl2_eigenvalues_on_vector(p55)
vec_decomp_55 = decompose_sl2(vec_eigs_55)
print(f"  10 -> SU(2) irreps of dimension {vec_decomp_55}")
print(f"  i.e. two copies of the 5-dim irrep (j = 2 of SU(2))")
print()

# Also branch the 45-adjoint and the 10, 120, 126 Yukawa Higgs irreps.
# 45 (adjoint of so(10)) is Lambda^2(V_10).
# 10 is V_10 itself.
# 120 = Lambda^3(V_10).
# 126 is the self-dual part of Lambda^5(V_10) (50% of dim 252 = Lambda^5).

def antisym_sl2_decompose(vec_eigs, k):
    """Decompose the Lambda^k of vector representation under sl(2)
    given eigenvalues vec_eigs on the vector rep."""
    n = len(vec_eigs)
    if k > n:
        return []
    eigs = []
    for combo in combinations(range(n), k):
        eigs.append(sum(vec_eigs[i] for i in combo))
    return decompose_sl2(sorted(eigs, reverse=True))

# 10-vector under (5,5) sl(2):
print(f"  10 (vector) branching:        {decompose_sl2(sorted(vec_eigs_55, reverse=True))}")
print(f"  45 (= Lambda^2 V) branching:  {antisym_sl2_decompose(vec_eigs_55, 2)}")
print(f"  120 (= Lambda^3 V) branching: {antisym_sl2_decompose(vec_eigs_55, 3)}")

# 126 is the self-dual half of Lambda^5 of V_10. Dim = 252/2 = 126.
# Under sl(2), Lambda^5(V) sl(2)-decomposes and 126 is one of the halves.
lambda5 = antisym_sl2_decompose(vec_eigs_55, 5)
print(f"  Lambda^5 V (dim 252) branching: {lambda5}")
print(f"  126 is the self-dual half (dim 126).")
print()

# Spinor 16 branching (already computed):
print(f"  16 (chiral spinor) branching: {sorted([1, 3, 5, 7])}")
print(f"                                = SU(2) j = 0 + j = 1 + j = 2 + j = 3")
print()

# ============================================================
# Step 8: Yukawa structure under the (5,5) sl(2)
# ============================================================
print("="*70)
print("Step 8: Yukawa structure under the (5,5) sl(2)")
print("="*70)
print()
print("  Yukawa terms are 16 . 16 . Phi for Phi in {10, 120, 126}.")
print()
print("  Under the (5, 5) sl(2), the 16 branches as the SU(2)-spin")
print("  multiplet (j = 0) (+) (j = 1) (+) (j = 2) (+) (j = 3).")
print()
print("  This is a 'maximal-spin' decomposition: the substrate maps")
print("  one fermion generation = 16 onto the SU(2)-multiplet with")
print("  spins 0, 1, 2, 3 — interpretable as the 4 atomic shells")
print("  s, p, d, f at fixed n = 4 (Volume K D101–D102 structural rhyme).")
print()
print("  The 16 x 16 tensor square SU(2)-decomposes as:")

# Compute (1+3+5+7) x (1+3+5+7) under SU(2):
# Already done above as su2_count

print(f"    {dict(sorted(su2_count.items()))}")
print()

# Yukawa Higgs irreps must come from the symmetric part (10 + 126)
# and antisymmetric part (120) of 16 x 16.

# To check: do 10, 120, 126 SU(2)-decompose into the multiplicities
# implied by su2_count?

# 10 branching = vec_decomp_55 = [5, 5]  (two copies of 5-dim)
# 120 branching = antisym_sl2_decompose(vec_eigs_55, 3)
# 126: half of Lambda^5

print("  Higgs Yukawa irreps under (5,5) sl(2):")
print(f"    10  -> {decompose_sl2(sorted(vec_eigs_55, reverse=True))}")
print(f"    120 -> {antisym_sl2_decompose(vec_eigs_55, 3)}")
print(f"    Lambda^5 V (= 126 + 126bar in self-dual decomp) -> {lambda5}")
print()
ten_sl2 = decompose_sl2(sorted(vec_eigs_55, reverse=True))
one_twenty_sl2 = antisym_sl2_decompose(vec_eigs_55, 3)
total_higgs = Counter(ten_sl2) + Counter(one_twenty_sl2)
print(f"  Higgs (10 + 120 only): SU(2) multiplet pattern:")
for dim in sorted(total_higgs.keys()):
    print(f"    {dim:>3}-dim irrep:  multiplicity {total_higgs[dim]}")
print(f"  Total dim: {sum(d*m for d,m in total_higgs.items())}")
print()

# Check that 16x16 sym/antisym matches the Higgs irreps under sl(2)
# Compute (16 x 16)_sym and (16 x 16)_antisym SU(2)-decompositions
# from the spinor weights.
spinor_eigs = sorted([principal_h_action(w) for w in weights], reverse=True)

# For (5,5) sl(2), recompute spinor eigenvalues
def spinor_eigs_for_partition(partition):
    vec_eigs = sl2_eigenvalues_on_vector(partition)
    from collections import Counter
    c = Counter(vec_eigs)
    half = []
    for e in sorted(set(vec_eigs), reverse=True):
        if e > 0:
            half.extend([e] * c[e])
        elif e == 0:
            half.extend([0] * (c[0] // 2))
    if len(half) != 5:
        return None
    spinor_eigs = []
    for signs in product([+1, -1], repeat=5):
        if signs.count(-1) % 2 == 0:
            val = 0.5 * sum(s * a for s, a in zip(signs, half))
            spinor_eigs.append(val)
    return spinor_eigs

spinor_55 = spinor_eigs_for_partition(p55)
sym_sq_eigs = []
antisym_sq_eigs = []
for i, ei in enumerate(spinor_55):
    for j, ej in enumerate(spinor_55):
        if i <= j:
            sym_sq_eigs.append(ei + ej)
        if i < j:
            antisym_sq_eigs.append(ei + ej)

sym_dec = decompose_sl2(sorted(sym_sq_eigs, reverse=True))
asym_dec = decompose_sl2(sorted(antisym_sq_eigs, reverse=True))
print(f"  (16 x 16)_sym (dim {len(sym_sq_eigs)}) under (5,5) sl(2): {sym_dec}")
print(f"  (16 x 16)_antisym (dim {len(antisym_sq_eigs)}) under (5,5) sl(2): {asym_dec}")
print()
print(f"  STANDARD: (16 x 16)_sym = 10 + 126; (16 x 16)_antisym = 120.")

# Compare antisym to 120 sl(2) branching
print(f"  CHECK: antisym match 120? sl(2): {asym_dec} vs Lambda^3 V: {one_twenty_sl2}")
# (16 x 16)_sym branches must equal 10 sl(2) plus 126 sl(2)
# 126 sl(2) branching can be deduced:
# (16x16)_sym sl(2) - 10 sl(2)  = 126 sl(2)
ten_c = Counter(ten_sl2)
sym_c = Counter(sym_dec)
expected_126 = sym_c - ten_c
print(f"  126 sl(2) (= (16x16)_sym minus 10): {sorted(expected_126.elements())}")
print()

# ============================================================
# Step 9: SM fermion identification under (5,5) sl(2)?
# ============================================================
print("="*70)
print("Step 9: SM fermion identification under (5, 5) sl(2)")
print("="*70)
print()
print("  Standard 16 of SO(10) contains one SM fermion generation:")
print("  (under SU(5) x U(1)):  1_{-5} + 5bar_{+3} + 10_{-1}")
print("    1   = nu_R^c (right-handed neutrino)")
print("    5bar = d_R^c (3) + L_L (2 = e_L + nu_L)")
print("    10   = Q_L (6) + u_R^c (3) + e_R^c (1)")
print()
print("  Under the (5, 5) sl(2), the substrate decomposition")
print("  16 = 1 + 3 + 5 + 7 does NOT match this:")
print("    Substrate 1 vs SM SU(5)-1: only the singlet (nu_R^c) matches")
print("    Substrate 3 vs SM SU(5) parts of dim 3: NONE (5bar has 3-component")
print("                                            inside it but 3 alone is")
print("                                            not an SU(5) irrep in the 16)")
print("    Substrate 5 vs SM SU(5) 5bar: dim matches BUT the (5,5) sl(2) puts")
print("                                  5bar across DIFFERENT SU(2) multiplets")
print("                                  (5bar has SU(5) structure, while (5,5)")
print("                                  sl(2)'s 5 is a pure SU(2)-quintet)")
print("    Substrate 7 vs SM SU(5) 10:  dim 7 != 10. NO match.")
print()
print("  The substrate decomposition 1+3+5+7 is therefore NOT a refinement")
print("  of the standard SU(5) 1 + 5bar + 10 split.")
print()
print("  However the (5,5) sl(2) gives a STRUCTURAL CONSEQUENCE: there is")
print("  an SO(10) -> SO(5) x SO(5) -> SU(2)_diag (diagonal sl(2)) embedding")
print("  for which the 16-spinor's SU(2)_diag content matches j = 0, 1, 2, 3.")
print()
print("  This SU(2)_diag is the DIAGONAL principal sl(2) of the SO(5) x SO(5)")
print("  Pati-Salam subgroup (each SO(5) has its own principal sl(2), with")
print("  V branching 5 -> 5_SU(2), and the diagonal is what (5,5) extracts).")
print()
print("  In Pati-Salam SO(10) -> SU(4) x SU(2)_L x SU(2)_R, the 16 branches as")
print("    (4, 2, 1) + (4bar, 1, 2)")
print("  which is 8 + 8. This is NOT 1 + 3 + 5 + 7.")
print()
print("  The (5, 5) sl(2) is therefore DIFFERENT from the SU(2)_L x SU(2)_R of")
print("  Pati-Salam — it's a 'maximal-spin diagonal' that mixes left/right")
print("  rather than separating them. Under standard SM identification, this")
print("  is NOT a natural breaking direction.")

print()
# ============================================================
# Step 10: Final verdict
# ============================================================
print("="*70)
print("Step 10: VERDICT")
print("="*70)
print()
print("VERDICT: PARTIAL CORRESPONDENCE.")
print()
print("WHAT MATCHES:")
print("  - 1+3+5+7 = 16 IS a representation-theoretic decomposition of the")
print("    16-spinor of SO(10) — specifically, under the sl(2) embedding")
print("    associated to the (5, 5) nilpotent orbit of so(10).")
print("  - This sl(2) is the 'diagonal principal' sl(2) of the SO(5) x SO(5)")
print("    Pati-Salam subgroup, branching V_10 = 5 + 5 and S_16 = 1+3+5+7.")
print("  - The substrate decomposition is therefore NOT a mere numerical")
print("    coincidence: it corresponds to a specific (and rather distinguished)")
print("    sl(2)-embedding inside SO(10).")
print()
print("WHAT DOES NOT MATCH:")
print("  - The (5, 5) sl(2) is NOT the standard SU(5) x U(1) decomposition")
print("    (which would give 1 + 5bar + 10).")
print("  - The (5, 5) sl(2) is NOT the SU(2)_L x SU(2)_R of Pati-Salam (which")
print("    would give 8 + 8). It's the DIAGONAL of those two SU(2)s.")
print("  - The substrate 1, 3, 5, 7 components do NOT individually map to SM")
print("    fermion species: dim 7 doesn't match SU(5)'s 10, dim 5 doesn't match")
print("    SU(5)'s 5bar in a representation-theoretic way (both are dim 5 but")
print("    the substrate 5 is an SU(2)-quintet, not an SU(5) anti-fundamental).")
print()
print("YUKAWA IMPLICATION:")
print("  - The Yukawa 16 x 16 x Phi naturally decomposes under (5, 5) sl(2) as")
print("    SU(2)-Clebsch-Gordan sums. With substrate spins (0, 1, 2, 3):")
print("      (16 x 16)_sym  -> SU(2): " + str(sym_dec))
print("      (16 x 16)_antisym -> SU(2): " + str(asym_dec))
print("  - However, the Yukawa COUPLINGS (which are physical numbers) require")
print("    a Higgs VEV direction that picks out a specific SU(2)-channel.")
print("    The substrate framework does NOT specify which channel.")
print("  - Consequently, NO numerical Yukawa prediction follows from the")
print("    1+3+5+7 substrate decomposition at the level of representation")
print("    theory alone.")
print()
print("STRUCTURAL RHYME (Volume K D101–D102):")
print("  - The atomic-shell interpretation '1+3+5+7 = (2l+1) for l = s, p, d, f")
print("    at n = 4' aligns with the SU(2) angular-momentum spin labels of the")
print("    (5, 5) sl(2) — both have integer SU(2)-spins j = 0, 1, 2, 3.")
print("  - This is the structural rhyme already noted in J37 §2.1, now upgraded")
print("    from 'numerical coincidence' to 'specific sl(2) embedding in so(10)'.")
print("  - The atomic-shell rhyme does NOT extend to a SM fermion identification:")
print("    the SU(2)_diag of (5,5) is not the SU(5) x U(1) chiral structure.")
print()
print("CONCLUSION:")
print("  F20 finds PARTIAL CORRESPONDENCE. The 1+3+5+7 decomposition is")
print("  Lie-algebraically meaningful (it's the (5,5)-sl(2) branching of 16)")
print("  but does NOT match the standard SM fermion content of the 16, and")
print("  produces NO numerical Yukawa prediction.")
print()
print("="*70)
print("Verification complete.")
print("="*70)
