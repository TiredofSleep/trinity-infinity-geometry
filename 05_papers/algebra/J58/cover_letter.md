# Cover Letter — J58

**To:** Editor, *Mathematics Magazine*
**From:** Brayden Ross Sanders, 7Site LLC, Hot Springs, AR
**Co-author:** Monica Gish (Independent Researcher, Hot Springs, AR)
**Date:** 2026-05-26

**Submission:** "The Lo Shu D₄ Orbit Modulo 3: Four Distinct Magmas and a Cumulant Spectrum"

---

Dear Editor,

We are pleased to submit the attached note for consideration in *Mathematics Magazine*. The paper is a ~12-page didactic exposition of a small but clean structural observation about the Lo Shu magic square.

## What's in the note

We take the unique $3 \times 3$ magic square (the Lo Shu, dating to roughly the 2nd millennium BCE in Chinese mathematics) and look at its $D_4$ orbit under the standard dihedral action. The orbit has 8 distinct elements. Reading each element mod 3 as a magma multiplication table on $\{0, 1, 2\}$, we find **exactly four distinct tables**, each appearing twice in the orbit. The four are:

1. The cyclic group $\mathbb{Z}/3$.
2. A commutative quasigroup with no identity element.
3. A non-commutative quasigroup.
4. Its anti-isomorphic mirror (opposite magma of #3).

The note's structural payoff is a **cumulant witness**: the second cumulant $\kappa(M) = \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2$, computed on the integer-valued orbit element *before* mod-3 reduction, takes exactly two values: $\kappa = -48$ if the resulting mod-3 magma is commutative, $\kappa = +48$ if it is non-commutative. The cumulant of the magic square diagnoses the algebraic structure of its mod-3 reduction without ever reducing.

## Why this fits *Mathematics Magazine*

The note is intended for an undergraduate audience comfortable with:

- The dihedral group $D_4$ (rotations and flips of a square).
- Modular arithmetic.
- Definitions of magma, quasigroup, commutativity.
- Trace and matrix multiplication.

Nothing beyond a standard sophomore abstract-algebra course is required. The substrate (the Lo Shu) is among the oldest objects in recorded mathematics, which makes the paper a natural bridge between historical/cultural context and modern small-finite-algebra structure.

A companion Python script (`verify_J58.py`, ~140 lines depending only on `numpy` and stdlib) reproduces every theorem at machine precision in under one second. Students can run it themselves and watch the structural facts emerge from the data.

## Tier discipline

- **PROVEN.** Theorems A, B, C, D, F by direct enumeration of 8 orbit elements.
- **COMPUTED.** Theorem E and the full cumulant table (6/6 PASS in `verify_J58.py`).
- **STRUCTURAL RHYME.** The cumulant-witnesses-commutativity correlation is observed in this specific 8-element family; we do not derive it from a more general theorem and explicitly mark this as an open generalization question (§7.1).
- **OPEN.** Generalization to other small magic squares' mod-$n$ reductions.

## Related work

The note's intellectual neighborhood is small finite commutative non-associative algebras. The closest published precedent is Drápal & Wanless (2021), *JCTA* **184**, 105510, on maximally non-associative quasigroups. Their work treats the high-non-associativity extremum at small orders; the present note treats a specific 8-element family at order 3, where maximal non-associativity is not the relevant extremum. We cite Drápal-Wanless as a structural reference.

The mod-3 reduction of the Lo Shu has appeared in undergraduate-textbook examples of small finite arithmetic systems, and the cyclic-group identification (Theorem F) is folklore. To our knowledge the four-table refinement (Theorem B) and the cumulant witness (Theorem E) have not been published.

## Author lane and submission discipline

Authors are listed as Sanders + Gish only. No AI co-authors. The script header is CC-BY-4.0 (standard journal-compatible). The submission is single-venue (not under simultaneous review elsewhere).

## What we ask for

We hope the editorial board will find the note's pedagogical clarity and its small-but-clean structural payoff worth a place in *Mathematics Magazine*. If the cumulant witness's mechanism is judged to need a deeper derivation before publication, we are happy to either expand §3.2 with more explicit bookkeeping or to retitle the note as "An empirical correlation" rather than "A cumulant spectrum" — we have no commitment to the framing beyond what the mathematics supports.

Thank you for considering J58.

Sincerely,

Brayden Ross Sanders
7Site LLC, Hot Springs, AR
brayden@7site.co

with Monica Gish, Independent Researcher, Hot Springs, AR

---

*Manuscript: `manuscript/manuscript.md`*
*Verification: `manuscript/verification/verify_J58.py`* (6/6 PASS, runtime <1s)
