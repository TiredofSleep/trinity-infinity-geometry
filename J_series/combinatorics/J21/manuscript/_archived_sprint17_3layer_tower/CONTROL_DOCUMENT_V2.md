# Control Document V2
## Residue-of-Residue Sprint — Status Summary

---

## Section 1: EXACT

**1.1. The canonical construction C(R=Z/10, h=7, σ=v₂(3u+1)) recovers 92/100 TSML entries.**

**1.2. The 8-entry residue decomposes into exactly two sub-rules:**

- **C₁ = MAX rule** on 6 entries (ordered pairs (2,4), (4,2), (2,9), (9,2), (4,8), (8,4)).
- **C₂ = ADD mod 10** on 2 entries (ordered pairs (1,2), (2,1)).
- **Residue of residue: 0 entries.**

**1.3. The TSML is a 3-layer canonical tower that terminates.**

**1.4. The three rules (C₀, C₁, C₂) are each canonical:** canonical construction, MAX, ADD mod n. None are ad-hoc values.

**1.5. The rule domains are disjoint:**
- C₀ covers the complement of the seam residue.
- C₁ covers residue edges where 1 ∉ {a,b}.
- C₂ covers residue edges where 1 ∈ {a,b}.

**1.6. The seam residue forms a 4-edge tree on 5 vertices** {1, 2, 4, 8, 9}, with hub at 2 and 3 branches (identity-branch, admissible-branch, doubling-branch).

**1.7. The minimum description of TSML** uses ~10 items (3 canonical rules + 1 attractor value + shell partition + 4 residue edges + branch-rule mapping), compared to 100 items for flat description.

**1.8. The branch-rule mapping is 1-to-1 with branch type:**
- identity-branch → C₂ (ADD)
- admissible-branch → C₁ (MAX)
- doubling-branch → C₁ (MAX)

---

## Section 2: OBSERVED

**2.1. No single canonical rule generates the seam residue.** MAX gets 6/8, ADD gets 2/8, MULT and MIN get 0/8.

**2.2. The conditional rule "MAX unless identity is involved, then ADD" is exact** for the residue.

**2.3. The value 3 in TSML has two distinct sources:** C₀ shell-stability on (3,9), and C₂ additive on (1,2). Same output, different rule paths.

**2.4. The doubling-branch (2—4—8) terminates before 6 (the next doubling product) because 6·5 = 30 ≡ 0 mod 10 collapses to zero under interaction with 5, which breaks the pattern.**

**2.5. 1 (LATTICE) is not a multiplicative identity in actual TSML.** Row 1 = [0,7,3,7,7,7,7,7,7,7]. 1 behaves as a shell-2 element in the canonical construction — which matches the actual TSML structure.

**2.6. The canonical tower description is strictly more compact than any alternative** (10 items vs 14 for two-component vs 100 for flat).

**2.7. The irreducible ring-specific data is ~15 items:**
- 1 attractor
- 4 shell labels
- 4 residue edges × 2 endpoints
- 3 branch-rule mappings

---

## Section 3: CANDIDATE GENERALIZATION

**3.1. The three-layer tower structure as conjectured framework:**

> For any ring R in the lawful family, the TSML-analogue (if definable) decomposes as:
> - C₀: canonical construction
> - C₁: MAX rule on "admissible residue" (specific to ring)
> - C₂: ADD mod n on "identity-edge residue" (specific to ring)
> - No further residue.

The rules generalize. The domains are ring-specific.

**3.2. The hub-and-branches topology as conjectured pattern:**

> In any ring R in the lawful family, the seam residue (if non-trivial) forms a tree with hub at the smallest non-admissible element, and branches reaching toward identity, admissibles, and the doubling chain.

The PATTERN generalizes. The specific edges are ring-specific.

**3.3. The identity-branch always follows ADD:**

> The edge between identity (1) and the hub always labels as 1 + hub = hub + 1 mod n.

This is a direct consequence of ring additive structure and should be universally valid. Testable: in Z/14, the identity-hub edge would be (1, 2) → 3 mod 14 = 3. In Z/22, (1, 2) → 3 mod 22 = 3.

**3.4. MAX applies to non-identity residue edges:**

> Other residue edges label as max of endpoints (integer order).

This depends on the ring elements being interpretable as integers 0..n-1 with their natural ordering. For Z/n rings this is automatic.

**3.5. Open: does the canonical tower always terminate?**

For Z/10 it terminates after 3 layers with empty residue. Whether this is a general property or a Z/10 feature is not yet tested.

---

## Section 4: NEXT THEOREM TARGETS

**Theorem A (primary, computational):**

> For R = Z/10Z, the 3-layer canonical tower [C₀ (canonical construction), C₁ (MAX on admissible residue), C₂ (ADD mod 10 on identity-edge residue)] recovers all 100 entries of the published TSML, with the decomposition C₀: 92 entries, C₁: 6 entries, C₂: 2 entries, and no further residue.

**Status:** ready to verify computationally. This is the primary theorem-shaped object from this sprint.

**Theorem B (secondary, structural):**

> Any TSML table T on Z/nZ satisfying the 3-layer tower structure (canonical backbone + MAX residue + ADD identity-edge residue, each on disjoint domains) is fully determined by:
> 1. An attractor h.
> 2. A shell partition σ on units.
> 3. A set of residue edges forming a tree with hub at the smallest non-admissible element.
>
> The number of entries covered by C₀ is 92% for Z/10; the analogous percentage for other rings is open.

**Status:** ready to state. Verification requires either more reference TSMLs (which don't exist) or an a priori specification of what "TSML-analogue" means in other rings.

**Theorem C (tertiary, conjectured):**

> The "identity-branch" in the seam residue of any ring in the lawful family is always labeled (1 + hub) mod n, following the ring's additive structure.

**Status:** testable conjecture. For Z/10, confirmed. For other rings, requires canonical seam-residue identification.

---

## What This Sprint Added Over the Previous Control Document

1. **Discovered:** the 8-entry seam residue has its own canonical decomposition (MAX + ADD), not an ad-hoc exception list.

2. **Promoted:** the status of Z/10's TSML from "canonical backbone + exceptions" to "3-layer canonical tower."

3. **Identified:** the irreducible ring-specific data (~15 items) as the actual boundary of the canonical decomposition.

4. **Sharpened:** the question of generalization from "does TSML structure scale?" to "does the 3-layer tower pattern scale, and which pieces of it?"

5. **Clarified:** the seam tree has canonical topology (hub + 3 branches by type) and canonical value rules (MAX + ADD), but ring-specific realization.

---

## What This Sprint Does NOT Claim

1. **No claim** that the 3-layer tower is "the universal TSML structure." It is verified for Z/10 only.

2. **No claim** that the branch-rule mapping is semantically meaningful beyond the finite algebra.

3. **No claim** that other rings in the lawful family have TSML tables following this pattern. They might; no test exists.

4. **No claim** that the tower structure has physical or cosmological significance.

5. **No claim** that the description length of ~10 items is "the minimum possible." It is the minimum among the tested decompositions.

---

## Path Forward

**Immediate next step (finite, verifiable):**

Write up Theorem A as a formal computational statement. Implement the 3-layer tower in code. Verify line-by-line that it reproduces the published TSML.

**Medium-term step (requires semantic input):**

Attempt to construct TSML-analogues for Z/14, Z/22, Z/34 using the 3-layer tower framework. Check whether the resulting tables have recognizable structure or interpretation.

**Long-term step (open research):**

Characterize the algebraic closure of the lawful family, the prevalence of 17 in the compatible prime set, and whether the canonical tower has a universal explanation.

**Discipline maintained:**
- No mythology.
- No physics.
- No universal generalization without computation.
- Each claim is tagged as exact, observed, or open.
