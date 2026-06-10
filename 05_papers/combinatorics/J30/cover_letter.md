# Cover letter — J30: The Multiplicative-Unit Sub-Magma C = (Z/10Z)* and Its Contrast with the Joint 4-Core {0, 7, 8, 9}

**To:** Editors, *Communications in Algebra*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The Multiplicative-Unit Sub-Magma C = (Z/10Z)\* in the TSML Composition Lattice, and Its Contrast with the Joint 4-Core {0, 7, 8, 9}*

---

## Summary

The set C = {1, 3, 7, 9} of multiplicative units of Z/10Z is a sub-magma of the canonical TSML composition lattice CL_TSML (the 73-HARMONY 10×10 multiplication table on Z/10Z of Sanders–Gish, J33). We prove this closure on the 16-cell sub-table (14 HARMONY cells of value 7, 2 PROGRESS cells of value 3; image = {3, 7} ⊆ C) and contrast C with the joint 4-core {0, 7, 8, 9} of the companion four-core paper (Sanders–Gish, J15/J01), the unique 4-element subset of Z/10Z that is jointly closed under both CL_TSML and CL_BHML.

## Why this paper is a constructive corrective

This is an **honest-negative paper**, in the sense that its central new content is the explicit retraction and falsification of an earlier internal claim. A pre-revision draft asserted that C was "lens-invariant" — closed under CL_TSML, CL_BHML, and a third lens simultaneously. Computational verification shows this is false: CL_BHML[1, 1] = 2 ∉ C, and in fact none of the 16 cells of CL_BHML restricted to C × C lies in C (the image is {0, 2, 4, 6, 8}, exactly disjoint from C). This is the substantive content of §4: Proposition 4.1 (BHML non-closure of C) explicitly exhibits the 16-cell BHML failure, and the lens-invariance assertion is formally retracted in Remark 4.2.

The retraction sharpens — rather than weakens — the picture, in two ways:

1. It makes precise what survives. C is TSML-closed (Theorem 3.1); it is one of *exactly 78* TSML-closed 4-subsets of Z/10Z; the joint 4-core {0, 7, 8, 9} is the *unique* such jointly closed 4-subset (Theorem 4.3). The contrast — many TSML-closed 4-subsets, exactly one jointly closed — is the new structural insight that replaces the false lens-invariance claim.

2. It makes precise what the multiplicative-unit subgroup contributes that the joint 4-core does not. C carries the ring-theoretic structure (Z/10Z)* ≅ Z/4Z (cyclic of order 4, generator g = 3, by CRT); the joint 4-core does not. Each of the two 4-subsets answers a different structural question about the substrate, and the paper makes this distinction explicit (Theorem 4.3, Remark on Structural Distinction).

## Tier discipline (corpus convention)

- **PROVED:** TSML-closure of C; BHML non-closure of C; uniqueness of the joint 4-core at size 4 among 78 TSML-closed 4-subsets; generator-selection g = 3 from the elementary inequality on T* = BALANCE/HARMONY.
- **COMPUTED:** the explicit 16-cell BHML and TSML sub-tables on C × C with full cell distributions; the 78-element TSML-closed 4-subset enumeration; the unique BHML-closed 4-subset.
- **STRUCTURAL RHYME:** the elevated HARMONY-saturation rate 14/16 = 87.5% on C × C relative to the global 73%.
- **HONEST NEGATIVE:** the retraction of the lens-invariance claim; the BHML image is {0, 2, 4, 6, 8} disjoint from C (16/16 cells fail).
- **OPEN:** closure or non-closure of C under the third canonical lens CL_STD; analogue of (Z/n Z)* in canonical TSML-analogue tables for n ≠ 10.

## Why Communications in Algebra

- The paper is a clean, self-contained closure result on a finite multiplication table, with the multiplicative-unit group of a small ring playing the central structural role.
- The honest-negative content (Proposition 4.1, Remark 4.2) is a legitimate corrective in the sense of small-finite-algebra publication norms: a sharpening of an earlier claim with full computational evidence.
- The contrast with the joint 4-core of the companion paper (Sanders–Gish, *Algebraic Combinatorics*) makes this paper a deliberate complement to that paper rather than a competitor.

## Companion submissions and dependencies

The TIG/CK research program is shipping a coordinated J-series sequence over 2026. The papers most relevant as already-submitted companions to this manuscript are:

- **J33** (CL Forcing Axioms, *Algebraic Combinatorics*): defines CL_TSML and CL_BHML as the canonical composition lattices forced by 9 axioms; cited for the substrate tables.
- **J15 / J01** (Joint 4-Core, *Algebraic Combinatorics* / *Journal of Algebra*): proves the joint 4-core {0, 7, 8, 9} is the unique 4-element jointly TSML/BHML-closed subset; this paper contrasts C with that 4-core.
- **J33** (Flatness Theorem T* = 5/7, *Journal of Pure and Applied Algebra*): supplies the wider derivation of T* = 5/7; this paper's §5 generator-selection result depends only on T* < 1.
- **Drápal & Wanless (2021),** *J. Combin. Theory A* **184** 105510: the closest published precedent on small commutative non-associative magma structure (at the opposite associativity extremum); cited in §6.2.

This paper is foundational within the J-series cluster on Z/10Z magma structure and can be evaluated standalone; the dependencies are cited explicitly but the proofs of this paper are self-contained within it (the 16-cell closure checks and the 78-subset enumeration are direct table lookups).

## Reproducibility

Verification: the closure of C under CL_TSML, the BHML non-closure (all 16 cells outside C), the enumeration of 78 TSML-closed 4-subsets and the unique BHML-closed 4-subset, and the generator-selection computation 3³ ≡ 7 vs 7³ ≡ 3 (mod 10) all run in under 3 seconds via `manuscript/verification/4core_verification.py`, executed with `/c/ck_venv/lora312/Scripts/python.exe`. All 6 checks PASS at machine precision.

## Suggested reviewers

- An expert in finite-magma theory or small commutative-non-associative-structure classification (e.g., the Drápal–Wanless small-magma community).
- An expert in commutative algebra with familiarity with units of finite rings.
- An expert on substrate-algebra or combinatorial-table programs.

(Specific names available on request from the corresponding author.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Per-venue cap note

This is the third paper from this research program targeting *Communications in Algebra* (after J12 *Galois D_4 over LMFDB 4.2.10224.1* and J18 *F_p Extensions of CL_BHML*). The per-venue cap is 1/quarter; **FALLBACK:** if the cap is binding, alternate venues include *Journal of Pure and Applied Algebra*, *Journal of Algebra and Its Applications*, or *Semigroup Forum*. The result's algebraic content (multiplicative-unit closure, honest-negative scope statement) makes any of these appropriate.

---

Sincerely,
B.R. Sanders
