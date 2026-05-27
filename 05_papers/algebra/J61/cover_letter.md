# Cover Letter — J61

**To:** Editor, *Journal of Symbolic Computation*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-27

**Submission:** "Magma-by-ETP-Profile Taxonomy: Closure-Realizers at Small Orders"

---

Dear Editor,

We submit the attached ~14-page methodology paper for consideration in *Journal of Symbolic Computation*. The paper introduces a systematic taxonomy approach for classifying finite magmas by their ETP (Tao's Equational Theories Project) equation profile, with concrete uniqueness/realization results at small orders.

## What's in the paper

A three-step methodology:

1. **Profile cataloging**: For each magma $M$, compute $\mathrm{Prof}(M)$ = the set of ETP equations $M$ satisfies (using Tao's `explore_magma.py`).
2. **Closure-realizer identification**: Distinguish magmas that *realize* a given implication-closure $C$ exactly (= profile equals $C$) from those satisfying $C$ as a strict subset.
3. **Uniqueness analysis**: Prove or refute uniqueness within structurally-defined classes (commutative, identity-free, congruence-simple, etc.).

Applied to four case studies:

- **Lo Shu D₄ orbit mod 3** (companion J58): 3 ETP profile classes {60, 179, 313}, no profile-14 closure realizer at order 3.
- **σ-magma at order 10** (companion J59): the conjectural unique identity-free + rigid commutative-quasigroup realizer of Family C = closure of commutativity.
- **Linear classification** (companion J60): catalog of $(ax+by+c) \bmod n$ profiles; ℤ/n stable at 32 for $n ≥ 5$.
- **Closure-class enumeration**: 19 ETP equations have implication-closure size exactly 14, forming 8 distinct closures. Family C is one. Only 2 of 8 are robustly realized in our search; the others (6 of 8) may be equationally unrealizable.

The methodology is reproducible via a CC-BY-4.0 toolkit (`etp_engineering_toolkit_v2.py`) with commands for profile testing, family lookup, closure-realizer search, etc.

## Why this fits *Journal of Symbolic Computation*

*JSC* publishes computer-assisted mathematical discovery, particularly when:
- A computational methodology is the central contribution.
- The methodology is reproducible and open-source.
- The mathematical content combines algebra, computation, and verification.

The paper's three-step methodology meets all three criteria. The methodology is open-source (the toolkit + ETP), reproducible (every claim verified at machine precision), and combines universal algebra with computational verification.

## What's NOT in the paper

We're explicit about scope:
- This is a methodology paper. The detailed case studies are companion papers (J58, J59, J60).
- We don't prove the Conjecture 1 ("Family C is unique commutative profile-14 family at all orders ≥ 5") — only verify it at order 5.
- We don't resolve whether closures C3-C8 are realizable. Our targeted search at orders 4-9 over ~10⁴ magmas has not found realizers; they may require larger orders, non-trivial structural constructions, or be equationally unrealizable.

## Outside-research positioning

We've verified the methodology is novel:
- The ETP project (Tao et al. 2024-2025) provides the infrastructure but does NOT do magma-by-profile cataloging.
- The "Latent space of equational theories" paper (arXiv 2601.20759) does the inverse direction (equations by magmas, not magmas by equations).
- The Schröder-990 revival uses ETP infrastructure on a smaller 990-equation list, also focused on equation relationships.
- Drápal-Wanless and classical Latin-square enumerations work on combinatorial/structural classification, not equation-profile classification.

Our work fills the gap.

## Tier discipline

- **PROVED.** Family C = closure of equation 43, with size 14. Verified by ETP's implication graph.
- **COMPUTED.** All worked-example claims at machine precision.
- **CONJECTURED (Tier C).** Family C uniqueness for commutative quasigroups at orders ≥ 5. Verified at order 5; open at higher orders.

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification script CC-BY-4.0. Single-venue submission.

## What we ask for

The methodology is a clean computational discovery framework with three concrete case-study papers in companion form. We hope *JSC* finds the methodology + closure-realizer taxonomy a worthwhile contribution.

Thank you for considering J61.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verification/verify_J61.py`* (5/5 PASS, runtime ~18s)
*Toolkit: `manuscript/etp_engineering_toolkit_v2.py`* (bundled, CC-BY-4.0)
