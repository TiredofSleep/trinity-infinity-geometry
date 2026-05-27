# Cover Letter — J60

**To:** Editor, *Experimental Mathematics*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-27

**Submission:** "ETP Profile Structure of Linear Magmas $(ax+by+c) \bmod n$: Cyclic Groups, Negation Magmas, and the Commutativity-Forced Minimum"

---

Dear Editor,

We submit the attached ~12-page paper for consideration in *Experimental Mathematics*. The paper catalogs equational-theory-project (ETP) profile sizes for linear magmas on $\mathbb{Z}/n\mathbb{Z}$, using Tao's Equational Theories Project repository as the verification backbone.

## What's in the paper

Four theorems, each verified at machine precision via `equational_theories/scripts/explore_magma.py`:

**Theorem 1**: $\mathbb{Z}/n$ (the cyclic group, $a = b = 1, c = 0$) has ETP profile size exactly **32** for all $n \in \{5, 6, 7, 8, 9, 10\}$, with universally identical equation IDs.

**Theorem 2**: $-(x+y) \bmod n$ has ETP profile **294** for $n = 4$ and $n = 10$ (the orders tested).

**Theorem 3**: At any order $\geq 5$, every commutative magma satisfies at least 14 specific ETP equations (IDs `[1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677]` — reflexivity + commutativity + 12 single-substitution derivatives). Many magmas achieve exactly these 14: the σ-magma at order 10 (from the parent framework), BHML, CL_STD, σ_10^min — all have IDENTICAL 14-equation profiles.

**Theorem 4**: Profile 14 is NOT unique to commutativity. ETP's tabulated 1,355-magma data contains **22 distinct non-commutative profile-14 equation families** at orders 3-9. Each is anchored on a different single-variable power identity (depth 3-5 expressions in $x$). The σ-magma's commutativity-anchored family (Family C, anchor = equation 43) is the 23rd known profile-14 family.

A companion verification script (`verify_J60.py`) reproduces all four theorems at machine precision in ~10 seconds.

## Why this fits *Experimental Mathematics*

*Experimental Mathematics* publishes computer-assisted, machine-verified discoveries in pure mathematics — exactly the methodology of this paper. The four theorems are stated, verified by direct ETP queries, and accompanied by reproducible code. The structural observations (especially the 22-family-explosion at profile 14) emerged from exhaustive ETP-tabulated-data analysis, which is the journal's wheelhouse.

The closest published precedent is the Equational Theories Project itself (Tao et al., 2024-2025) — though that is collaborative blueprint-driven research rather than journal-published. Our paper extracts a specific structural sub-story: the place of cyclic-group, negation-magma, and σ-magma profiles in the broader ETP landscape.

## Tier discipline

- **PROVED.** All four theorems by direct ETP computation at machine precision (Tier A per the parent framework's discipline notation).
- **CONJECTURED (Tier C).** Two open conjectures stated: (i) the negation-magma profile-294 is universal across $n \geq 4$, and (ii) Family C is the unique commutative profile-14 family at all orders ≥ 5.

## Connection to broader framework

This paper is the third in a related set:
- **J58** (submitted to *Mathematics Magazine*): Lo Shu D₄ orbit modulo 3 — 4-magma refinement and cumulant witness.
- **J59** (submitted to *Semigroup Forum*): σ-magma at order 10 — four rigidity theorems (|Aut|=1, congruence-simple, unique sub-magma, 2-generated).
- **J60 (this paper)** (submitted to *Experimental Mathematics*): The σ-magma's "14 ETP equations" reframed as the commutativity-forced minimum, with the 23-family explosion at profile 14.

Each paper is self-contained; the parent framework reference appears only as motivation.

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification script CC-BY-4.0. The submission is single-venue.

## What we ask for

The four theorems are PROVED at machine precision via Tao's open ETP catalog; the verification is reproducible in 10 seconds; the open-source verification script is bundled. We hope *Experimental Mathematics* finds the structural observations (especially Theorems 3 and 4) worthy contributions to the ETP-adjacent literature on small-finite-magma equational structure.

Thank you for considering J60.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verification/verify_J60.py`* (4/4 PASS, runtime ~10s)
