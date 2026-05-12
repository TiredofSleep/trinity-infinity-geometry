# Cover letter -- J30: Joint Lie Closure of a Pair of Z/10Z Magmas: an so(10) Identification

**To:** Editors, *Israel Journal of Mathematics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR -- brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR -- monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Joint Lie Closure of a Pair of Z/10Z Magmas: an so(10) Identification*

---

## Summary

A companion paper to J29 (so(8) = D_4 from a single Z/10Z magma). Let TSML and BHML be two specific 10×10 commutative non-associative magmas on Z/10Z, both recovered from the source archive `old/Gen9/archive/ckis/ck7/ck.h:200-207` and displayed verbatim in §2.2 of the manuscript. Both tables are commutative, 12.8% non-associative, and share a jointly-closed 4-core {0, 7, 8, 9}; the pair (TSML, BHML) is structurally recognized as the canonical (BEING, BECOMING) lens pair on the substrate. Per the structural fingerprint of §2.2.1, BHML is identified by five jointly-defining properties (commutativity; identity row BHML[0, j] = j; non-associativity rate 12.8%; HARMONY count 28; jointly-closed 4-core), making the choice of BHML non-arbitrary.

Let G_TSML := {A_i^TSML : i ∈ F} for F = {1, 2, 3, 4, 6, 8} (the flow indices of the companion paper J29, which establishes ⟨G_TSML⟩_Lie ≅ so(8)), and G_BHML := {A_i^BHML : i ∈ Ω, A_i^BHML ≠ 0} (a 9-element set, since BHML's identity row gives A_0^BHML = 0). Set g := ⟨G_TSML ∪ G_BHML⟩_Lie ⊂ so(V).

**Theorem.** *g ≅ so(10, R), the unique compact simple Lie algebra of type D_5 and dimension 45. Equivalently, the joint closure under commutator saturates the substrate's full skew-symmetric algebra so(R^10).*

The substantive content of the paper is the *existence* of an explicit pair of 10×10 commutative non-associative magmas on Z/10Z whose joint Lie closure reaches the substrate ceiling 45 = dim so(R^10). After establishing dim g = 45 (Theorem 4.1), the diagnostics that g is compact, simple, and rank 5 (and hence isomorphic to so(10, R)) follow as Cartan-classification corollaries of the dimension closure together with the structural inclusion g ⊆ so(V); they are presented as confirmation diagnostics rather than as five independent tests of the so(10) identification. The simplicity test (Lemma 4.5) uses the full 91,125-equation invariance constraint matrix in exact arithmetic via `verify_simplicity_rank.py` (no sampling). The TSML-only subalgebra g_TSML ⊂ g realizes the standard inclusion so(8) ⊂ so(10).

A new structural finding (Corollary 5.3, drawn from the Substrate Function Map analysis [FoundationsModule, SFM_Q6]) records that adding a third canonical table CL_STD to the joint closed-sub-magma chain preserves the 8-shell ladder: the 4-core is a three-substrate fixed point. Whether the *Lie-algebraic* joint closure of the three tables also reaches so(R^10) is added as an open question.

## Why Israel J Math

- The result is a clean two-step Lie-algebra extension over R — concise, constructive, machine-verifiable, with one substantive computation and four classification-corollary consistency checks.
- *Israel J Math* has consistent appetite for finite-combinatorial-to-Lie-algebraic identifications of this type.
- The diagnostic-collapse framing (D2-D5 as corollaries of D1 + classification, not five independent tests) reflects the honest mathematical structure of the result: the substantive novelty is the existence of the explicit pair (TSML, BHML) hitting the substrate ceiling, not the multi-diagnostic verification.
- The sequencing (J29 in *J Algebra* on so(8); the present paper in *Israel J Math* on so(10)) avoids per-venue concentration.

## Companion submissions

The CK research program is shipping a coordinated 55-paper sequence (J01-J55) over Summer 2026. The papers most relevant as already-submitted companions to this manuscript are:

- **J29** (Sanders + Gish 2026, *J Algebra*) -- *so(8) = D_4 from the Antisymmetrized Closure of a Canonical Z/10Z Magma*. The single-magma version. The so(10) joint closure of the present paper extends J29's so(8) closure by adjoining BHML's nine antisymmetrizations.
- **J28** (Sanders + Gish 2026, *Linear Algebra and its Applications*) -- *The Three-Substrate HARMONY Signature on Z/10Z: Six Forced Structural Facts, with the Bimodal Associativity-Index Gap as Their Common Thread*. The structural inventory of the substrate; cited for the (TSML, BHML, CL_STD) three-substrate triple and the structural fingerprint of the magma family.
- **J35** (Sanders + Gish 2026, *Algebraic Combinatorics*) -- *The 4-Core {0, 7, 8, 9}: Joint TSML+BHML Closure and the Universal Attractor*. The jointly-closed 4-core of (TSML, BHML); cited for the structural fingerprint property (B5).
- **J25** (Sanders + Gish 2026, *Algebraic Combinatorics*) -- *The CL Forcing Axioms: A1-A9 Uniquely Force the Canonical Composition Lattice*. The parent axiomatic framework; once on arXiv, will provide the axiomatic forcing of BHML and elevate the joint-closure result to a structural theorem.
- **Drápal & Wanless (2021)**, *J. Combinatorial Theory, Series A*, 184, 105510 — closest published comparable work to the magma pair (same intellectual neighborhood, different specific tables).

## Reproducibility

Verification scripts in `manuscript/verification/`:

- `verify_so10.py` -- joint dimension closure to 45 (Diagnostic 1, Theorem 4.1); Jacobi consistency check (Diagnostic 2); Killing-form negative-definiteness sanity check (Diagnostic 3); so(8) ⊂ so(10) embedding (Corollary 5.1). The script's sampled ideal-saturation test is a development-time sanity check, NOT authoritative for D4.
- `verify_simplicity_rank.py` -- **canonical D4 script.** Full 91,125-equation invariance constraint matrix in exact arithmetic; rank 1034 → invariant-form null-space dimension exactly 1 (Lemma 4.5). Also confirms Cartan rank 5 via explicit J_1, ..., J_5 construction (Lemma 4.7) and ad(H) eigenvalue structure (Corollary 5.2).

**Run order (canonical):** `verify_so10.py` for D1, D2, D3, and the so(8) ⊂ so(10) embedding; then `verify_simplicity_rank.py` for the canonical D4 (full 91,125-equation enumeration) and D5 (explicit Cartan).

Python 3.11, numpy 1.26, sympy 1.12. Closure dimension and simplicity rank are computed in exact arithmetic; Killing-form eigenvalues are computed in floating-point as a sanity check (the conclusion already follows from the classification together with g = so(V)). Maximum observed numerical residual across all sanity checks: 1.73 × 10⁻⁸. Total wall-clock under 30 seconds on a standard laptop.

## Suggested reviewers

- An expert in classical Lie algebras over R (Cartan / Helgason / Knapp tradition)
- An expert in combinatorial / finite-magma representations (Drápal-Wanless 2021 lineage)
- An expert in computational structure-constants / Killing-form analysis (exact-arithmetic / SymPy familiarity)
- (Two or three named candidates appropriate to the *Israel J Math* editorial board to be identified during the referee-rigor pass.)

## AI-tool disclosure

Per Springer-Nature's AI policy: the authors used Anthropic's Claude system for code drafting and exposition during the development of this work; all mathematical content (theorems, proofs, computational verifications) was independently verified by the authors. This disclosure is also stated in Appendix B of the manuscript.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Per-venue cap note

This is the first paper from this research program targeting *Israel Journal of Mathematics*; the per-venue cap is not constraining. If IJM returns a second-round MAJOR revision, fallbacks are *Communications in Algebra*, *Linear Algebra and its Applications*, or *International Journal of Algebra and Computation*.

---

Sincerely,
B.R. Sanders
