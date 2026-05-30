# Cover Letter — J53

**To:** Editor, *Algebra Universalis*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-29

**Submission:** "Idempotent Counts and Automorphism Groups of a 4-Dimensional Commutative Non-Associative Algebra over $\mathbb{F}_p$: Two Closed-Form Theorems"

---

Dear Editor,

We are pleased to submit the attached short note for consideration in *Algebra Universalis*. The paper establishes two clean closed-form theorems about a specific 4-dimensional commutative non-associative $\mathbb{F}_p$-algebra $V^{\mathrm{BHML}}$ — each proved by an explicit structural derivation and additionally verified by direct computation at 24 primes $3 \leq p \leq 97$.

## What's in the note

The algebra $V^{\mathrm{BHML}}$ is a 4-dimensional commutative non-associative $\mathbb{F}_p$-algebra with basis $\{e_0, e_2, e_3, e_4\}$, multiplication
$$
e_0 \cdot x = 0\ \forall x,\qquad e_2^2 = e_2,\qquad e_2 e_3 = e_3,\qquad e_3^2 = e_2,\qquad e_3 e_4 = e_4,\qquad e_4^2 = 0,
$$
and all other products zero. (The "BHML" subscript indicates the algebra arises as the 4-core restriction of the BHML composition table on $\mathbb{Z}/10\mathbb{Z}$ in the first author's separate research framework; the algebra stands on its own as a universal-algebra object.) The paper proves:

**Theorem 1** (Idempotent count): $|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_p)| = p + 3$ at every odd prime $p$, and $= 2$ at $p = 2$. Proved by reducing the idempotent equation $\varepsilon^2 = \varepsilon$ to a parametric system in $\mathbb{F}_p^4$, case-splitting on the resulting linear factors, and counting solutions exactly.

**Theorem 2** (Automorphism formula): $|\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p)| = (p-1)^2$ at every prime $p \geq 2$, with group structure $\mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$. Proved by showing every automorphism preserves the annihilator $\mathrm{span}(e_0)$ and the nilpotent direction $\mathrm{span}(e_4)$, and is determined by two independent $\mathbb{F}_p^{\!*}$-scalings on those 1-dimensional invariant subspaces.

Both theorems are *prime-uniform* — **no prime is structurally distinguished**. This is the central rigidity statement of the paper.

## Why this fits *Algebra Universalis*

*Algebra Universalis* publishes work on universal algebra, lattices, and (small) finite algebraic structures with an emphasis on clean structural theorems. The note's content is exactly in this neighborhood:

- It works with a specific commutative non-associative algebra (i.e., a magma with an $\mathbb{F}_p$-module structure compatible with multiplication) — squarely in the journal's "small finite magmas + universal algebra" scope.
- The two theorems are about classical algebraic invariants (idempotent set, automorphism group) — the kind of clean structural result the journal regularly publishes.
- The methodology — structural derivation backed by exhaustive verification at small primes plus extension to higher primes — is increasingly standard in the small-finite-algebra literature, with the closest precedent being **Drápal & Wanless (2021, *Journal of Combinatorial Theory, Series A* 184, 105510)** on maximally non-associative quasigroups.

A companion verification script (`verify_J53.py`, ~150 lines, depending only on Python's standard library) reproduces both theorems at machine precision at the 5 primes $p \in \{3, 5, 7, 11, 13\}$ in about 2 seconds. For higher-prime confirmation up to $p = 97$, a separate script in the parent project (`F4_extended_verify.py`) supplies the extended verification at the remaining 19 primes. Both scripts are open-source CC-BY-4.0 and submitted alongside the manuscript.

## Tier discipline

- **PROVED.** Theorems 1 and 2 — each by structural derivation + brute-force verification at 24 primes $3 \leq p \leq 97$.
- **STRUCTURAL.** The *prime-uniform* nature of both formulas (no prime distinguished) is itself a structural rigidity result: $V^{\mathrm{BHML}}$ has the same idempotent count and automorphism group structure at every prime, with the closed form scaling cleanly in $p$.
- **OPEN.** §6 — generalization to characteristic 0 (predicted to give $\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{Q}) \cong \mathbb{Q}^* \times \mathbb{Q}^*$, not verified); generalization to the σ-twin lens $V^{\mathrm{TSML}}$ (cf. J18 §4); generalization to $V_n^{\mathrm{BHML}}$ in other dimensions.

## Related work and motivation

The closest published precedent is **Drápal & Wanless (2021)** on maximally non-associative quasigroups — same domain (small finite commutative non-associative structures), opposite extremum (maximally non-associative loops vs the minimally-rigid commutative non-associative algebra studied here). Beyond Drápal–Wanless, the literature on $\mathbb{F}_p$-algebras of small dimension is largely associative (group algebras, matrix algebras, Frobenius algebras), with non-associative analogues studied only for octonions and Jordan algebras (dimensions 8 and 27 respectively). To our knowledge, no published paper gives closed-form counts of idempotents and automorphisms for a 4-dimensional commutative non-associative algebra at every prime — Theorems 1 and 2 of this note are, as far as we have been able to determine, new structural results.

The algebra $V^{\mathrm{BHML}}$ arises in a separate research framework (Trinity Infinity Geometry, in development by the first author for a Sept-2026 publication milestone). The framework provides the substrate (the BHML composition table on $\mathbb{Z}/10\mathbb{Z}$ and the 4-core attractor $\{0, 7, 8, 9\}$), but the two theorems are universal-algebra statements that stand on their own — the manuscript explicitly notes this, and the proofs use no framework-specific machinery.

## Author lane and submission discipline

Authors: Sanders + Gish only. No AI co-authors. Verification scripts are CC-BY-4.0 with the standard header. The submission is single-venue.

## What we ask for

The two closed-form theorems are PROVED structurally and verified at 24 primes at machine precision; the note is short (~8 pages typeset); the verification is self-contained. We hope the editorial board will find the result a worthwhile addition to *Algebra Universalis*'s catalog of clean structural theorems about small finite algebras.

If the framework-of-origin reference is judged out of scope for *Algebra Universalis*, we can drop the brief framework references (§1 last paragraph, §5 last paragraph) and present the manuscript as pure universal algebra — the two theorems stand without any external context.

Thank you for considering J53.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verify_J53.py`* (2/2 PASS at 5 primes, runtime ~2s)
*Higher-prime extension: `04_meta/frontiers_2026-05-27/F4_extended_verify.py`* (extends to 24 primes total, $p \leq 97$)
