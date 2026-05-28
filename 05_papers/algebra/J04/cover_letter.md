# Cover Letter — J04

**To:** Editor, *Semigroup Forum*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-26

**Submission:** "Algebraic Rigidity of the σ-Magma on $\mathbb{Z}/10\mathbb{Z}$: Simplicity, Trivial Automorphism Group, and Unique Sub-Magma"

---

Dear Editor,

We are pleased to submit the attached short note for consideration in *Semigroup Forum*. The paper establishes four independent rigidity theorems about a specific 10-element commutative quasigroup we call the σ-magma — each proven by exhaustive computational search bounded by a small finite cardinality.

## What's in the note

The σ-magma is defined by $x \diamond y = \sigma((x+y) \bmod 10)$ for a specific permutation σ with four fixed points and one 6-cycle. The paper proves:

**Theorem A**: $|\mathrm{Aut}(\diamond)| = 1$ (only the identity is a magma automorphism). Verified by exhaustive search over $S_{10}$.

**Theorem B**: the σ-magma is congruence-simple — only the trivial (identity + universal) congruences exist. Verified by exhaustive search over the 115,975 partitions of $\{0, \ldots, 9\}$.

**Theorem C**: the σ-magma has exactly 5 sub-magmas — three singleton idempotents, the full magma, and one non-trivial proper sub-magma $\{1, 6\}$ which is isomorphic to $\mathbb{Z}/2$. Verified by exhaustive search over the 1024 subsets.

**Theorem D**: the σ-magma is 2-generated, with $\{1, 6\}$ the unique 2-element non-generating subset (consistent with Theorem C). All 44 other pairs generate the full magma in at most 4 generation steps.

The four properties together — *no automorphisms, no quotients, no non-trivial sub-structures except a single $\mathbb{Z}/2$, minimum generators* — make the σ-magma a maximally indecomposable commutative quasigroup of order 10.

## Why this fits *Semigroup Forum*

*Semigroup Forum* publishes work on semigroups, monoids, magmas, and related universal-algebra structures. The note's content is exactly in this neighborhood:

- It works with magmas (commutative quasigroups), the broader class containing groups and semigroups.
- The four theorems are about classical universal-algebra invariants (automorphisms, congruences, sub-algebras, generators).
- The methodology — exhaustive computer search to establish rigidity — is increasingly accepted in small-finite-structure papers in the journal.

A companion verification script (`verify_J59.py`, ~150 lines, depending only on Python's standard library) reproduces all four theorems at machine precision in about 3 seconds. The script is open-source CC-BY-4.0 and submitted alongside the manuscript.

## Tier discipline

- **PROVED.** Theorems A, B, C, D — all by exhaustive search.
- **STRUCTURAL.** The simultaneous holding of all four rigidity properties (noted as empirically rare, no general theorem invoked).
- **OPEN.** Whether the σ-magma is the unique commutative quasigroup of order 10 satisfying all four — testable but not done here.

## Related work and motivation

The closest published precedent for the methodology is Drápal \& Wanless (2021, *JCTA*) on maximally non-associative quasigroups — same neighborhood (small finite commutative quasigroups), opposite extremum (maximally non-associative vs maximally rigid). The literature on automorphism groups of magmas, congruence lattices of magmas, and sub-magma posets of magmas is mature but typically focuses on classes (Latin squares of order $n$, all loops of order $n$, etc.) rather than specific individual magmas.

The σ-magma arises in a separate research context (Trinity Infinity Geometry, in development by the first author for a Sept 2026 publication milestone). The framework provides motivation for the specific permutation σ, but the four rigidity theorems are universal-algebra statements that stand on their own — the manuscript explicitly notes this.

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification script header is CC-BY-4.0. The submission is single-venue.

## What we ask for

The four rigidity theorems are PROVED at machine precision; the note is short (~10 pages); the verification is self-contained. We hope the editorial board will find the result a worthwhile addition to *Semigroup Forum*'s catalog of structural-classification papers on small algebraic objects.

If the σ-magma's framework-of-origin is judged out of scope for *Semigroup Forum*, we can entirely drop the brief framework references (§0, §6.2) and present the manuscript as pure universal algebra — the four theorems stand without any external context.

Thank you for considering J04.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verification/verify_J59.py`* (4/4 PASS, runtime ~3s)
