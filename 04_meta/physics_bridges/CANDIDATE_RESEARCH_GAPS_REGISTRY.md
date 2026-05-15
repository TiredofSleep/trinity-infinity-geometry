# CANDIDATE_RESEARCH_GAPS_REGISTRY

## Open gaps that, when closed, would convert candidate derivations to proved derivations

**Locked**: 2026-05-14
**Status**: Registry document — tracks open research gaps with specific verification paths
**Framework location**: `04_meta/physics_bridges/CANDIDATE_RESEARCH_GAPS_REGISTRY.md`
**Strategic context**: per Brayden 2026-05-14, the framework is being SEEDED, not rushed. These gaps are completeness targets, not external-deadline-driven priorities.

---

## §0. Purpose

The framework has reached candidate-derivation precision in several places (α at CODATA precision, threshold canon from Cl(0,10), c-and-mass structural bridges). For each candidate derivation to become a proved derivation, specific gaps need closing. This document lists those gaps with their verification paths so independent researchers can attempt closure.

Each gap is named, scoped, and given a concrete test that would close it.

---

## §1. Gaps from CHIRALITY_DECOMPOSITION_DERIVES_THRESHOLD_CANON.md

The chirality-decomposition arc (2026-05-14) derived T*, S*, and surplus from Cl(0,10) shell-decomposition arithmetic. Five gaps remain before the derivation is fully rigorous.

### Gap 1: Canonical projection π not defined

**Status**: open.
**Scope**: the spin-projection picture requires a specific map π: Cl(0,10) → Z/10 that identifies each substrate position with a specific spinor-space element.
**Verification path**: explicitly construct π by mapping each γ_i (i ∈ {1..10}) in Cl(0,10) to its substrate residue, then verify that the chirality decomposition (T* = d/f, S* = (s+p)/f, surplus = (non-f − f)/f) emerges naturally under this map.
**Effort**: 2-4 weeks Clifford-algebra calculation.
**When closed**: Gap 2 becomes tractable.

### Gap 2: TSML and BHML as π-projections

**Status**: open.
**Scope**: canon §5 and §6 give TSML and BHML as explicit tables. The chirality-decomposition reading needs these tables to emerge from Cl(0,10) products projected through π.
**Verification path**: for arbitrary substrate positions i, j ∈ Z/10, compute γ_i · γ_j in Cl(0,10) (with index identification from Gap 1). Project the result through π. Compare to TSML(i,j) and BHML(i,j).
**Expected outcome**: TSML corresponds to one projection convention (perhaps positive chirality), BHML to the dual (negative chirality), with the 22 disagreement cells being where the two projections differ.
**Effort**: 1-2 months after Gap 1 closes.
**When closed**: the framework presentation reduces to "Cl(0,10) + canonical projection π = everything else."

### Gap 3: σ_outer at depth-5 verification

**Status**: open.
**Scope**: canon D31 says P_56 is the spinor outer automorphism. The α derivation has depth-5 correction at the σ_outer crossing.
**Verification path**: compute (γ_5 − γ_6)/√2 in Cl(0,10), verify it's the spinor outer automorphism (sends +chirality 16 entirely into −chirality 16, residual = 0), and verify it appears at depth 5 in the α expansion through π.
**Effort**: 2-3 weeks. Some of this is done — canon D31 establishes the +chirality/−chirality swap at 100% in the 54 irrep. What's needed is the depth-5 connection.
**When closed**: the α expansion's exponent structure is fully explained.

### Gap 4: 315 uniquely from Cl(0,10) — partially closed

**Status**: partially closed. The 7·45 = HARMONY × C(10,2) reading is most structural.
**Scope**: 315 has three canonical readings: (a) 7 × 45 = HARMONY × C(10,2), (b) 9!/3!4! = a binomial coefficient, (c) other. The chirality-decomposition reading needs 315 to emerge uniquely from Cl(0,10) projection structure.
**Verification path**: prove that 7·45 is the unique reading consistent with the Cl(0,10) → Z/10 projection π from Gap 1.
**Effort**: 2-3 weeks after Gap 1 closes.
**When closed**: the α expansion's depth-7 base is fully derived.

### Gap 5: W = 3/50 from projection residue structure

**Status**: open.
**Scope**: W is canon D17 derived from cross-cycle structure. The chirality-decomposition reading might derive it as 6/(p-subshell × substrate²) = 6/(6·25) = 6/150 = 1/25, OR more naturally as 3/50 from another projection-residue identity.
**Verification path**: in the Cl(0,10) → Z/10 projection from Gap 1, compute the residue that's preserved under π. Verify it equals 3/50 by an independent identity.
**Effort**: 1-2 months after Gap 1 closes.
**When closed**: every constant in the α expansion is derived rather than empirical.

---

## §2. Status summary

| Gap | Scope | Effort estimate | When closed |
|-----|-------|----------------|-------------|
| Gap 1 | Define π: Cl(0,10) → Z/10 explicitly | 2-4 weeks | Enables Gaps 2, 4, 5 |
| Gap 2 | TSML/BHML from Cl(0,10) products | 1-2 months | Framework becomes "Cl(0,10) + π" |
| Gap 3 | σ_outer at depth-5 verified | 2-3 weeks | α exponents explained |
| Gap 4 | 315 uniquely from Cl(0,10) | 2-3 weeks | Depth-7 base derived |
| Gap 5 | W = 3/50 from residue structure | 1-2 months | All α constants derived |

**Total effort to convert all candidates to proved**: 2-3 months of focused Clifford-projection mathematics, with Gap 1 as the critical dependency.

---

## §3. Tier post-closure

When all five gaps close:

- **α derivation**: from Tier B-suggestive-strong (current) → Tier B-rigorous
- **Threshold canon**: from Tier B-suggestive-strong (current) → Tier B-rigorous
- **TSML/BHML**: from independently-specified (current) → derived from Cl(0,10)
- **Framework presentation**: simplifies to *"Cl(0,10) is the substrate. π: Cl(0,10) → Z/10 is the canonical projection. Everything else is derived."*

That's the framework's structural endpoint. The roads to it are named.

---

## §4. Tier discipline reminder

These gaps are open by design. The framework's posture is to declare candidates at their honest tier (B-suggestive-strong here) and name the remaining gaps explicitly. This is the OPPOSITE of closure-claiming.

The 2-3 month estimate is for serious Clifford-algebra work, not a hand-wave. Until the gaps close, the candidate derivations remain candidates. The numerical match at experimental precision (α at CODATA, 1.73 × 10⁻¹¹) is theorem-level fact (verifiable arithmetic); the structural derivation through Cl(0,10) is suggestive-strong, not closure.

---

## §5. For future updates

When a gap closes:
- update its `Status` field above to `closed`
- add the closing artifact (paper, script, manuscript section) as a reference
- update §2 status table
- update the per-tier promotion in §3

When a gap NEW gap is identified elsewhere in the framework:
- add a new sub-section in §1 (numbered Gap N where N continues)
- include scope, verification path, effort estimate
- cross-reference the source document

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC*
*Licensed under the 7SiTe Public Sovereignty License v2.1*
*Trinity Infinity Geometry — Candidate Research Gaps Registry, locked 2026-05-14.*
