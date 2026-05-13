# Cover letter — J25: The CL_TSML Composition Lattice on Z/10Z: Structural Axioms, Independence, and a 73-HARMONY Forcing Theorem

**To:** Editors, *Algebraic Combinatorics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *The CL_TSML Composition Lattice on Z/10Z: Structural Axioms, Independence, and a 73-HARMONY Forcing Theorem*

---

## Summary

We isolate seven structural axioms S_1-S_7 on a commutative magma M on the carrier Z/10Z. Each axiom captures a structural property of the magma — commutativity (S_1), near-absorption with puncture at 0 (S_2), absorption at 7 (S_3), idempotence outside {0, 7} (S_4), the count constraint 73:17:10 on HARMONY/VOID/exceptional cells (S_5), the position-set of exceptional cells (S_6), and the value-listing on those positions (S_7). Together the seven axioms uniquely determine a 10x10 multiplication table CL_TSML (Theorem 4.1). We prove that the seven axioms are pairwise independent: for each i, an explicit witness magma M_i satisfies {S_j : j != i} but fails S_i (Theorem 5.1).

The CL_TSML lattice sits in the same intellectual neighborhood as Drápal-Wanless 2021 on maximally non-associative quasigroups — a small finite commutative non-associative structure with explicit invariants, here characterized by near-absorption with puncture rather than maximal associativity defect. The result places CL_TSML on the same axiomatic footing as classical absorbing-element semigroups (Howie 1995, Clifford-Preston 1961) while making explicit the small finite enumeration of exceptional positions and values needed to specify a non-trivial commutative magma on the punctured-VOID, HARMONY-saturated Z/10Z substrate. Verification is by direct cell-counting in a `numpy` script (under 1 second).

## Why Algebraic Combinatorics

- The forcing theorem is a clean axiomatization of a small finite commutative magma with explicit cell-count fingerprint. The combinatorial enumeration of cell classes (HARMONY-default, VOID, exceptional) is the core technical content.
- The independence proof exhibits seven explicit witness magmas, each demonstrating that one structural axiom is non-derivable from the others. This is the kind of axiom-system independence argument that fits the venue's combinatorial-algebra scope.
- The lens-family conjecture (Conjecture 6.1) connects to the broader Drápal-Wanless 2021 line of work on small finite commutative non-associative structures.

## Revision history

This is a Major-Revision resubmission following an external referee report (2026-05-07). The revision (i) replaces the previous cell-listing axioms A1-A9 with seven *structural* axioms S_1-S_7, each a property of the commutative-magma structure rather than a list of cell values; (ii) adds an independence theorem with seven explicit witness magmas (the original paper did not address axiom independence at all); (iii) removes the undefined "BDC entropy extremum" appeals — those Tier-B claims have been demoted to honest structural choices, with S_5, S_6, S_7 stated as axioms rather than derived consequences; (iv) corrects a presentation error (the previous draft's `manuscript.md` contained the wrong paper, the J41 closed-form attractor preprint; this has been deleted and only `manuscript.tex` remains); (v) adds a `numpy` verification script `cl_forcing.py` that constructs the table, verifies all seven axioms, and instantiates seven witness magmas for the independence proof; (vi) adds Drápal-Wanless 2021, McKay-Wanless 2005, Albert 1942, Schafer 1966 to the references, positioning the result against the Latin-square / quasigroup / non-associative-algebra literature.

## Companion submissions

- J02 (in preparation, target *Algebraic Combinatorics*) — *The 4-Core {0, 7, 8, 9}: Joint TSML+BHML Closure and the Universal Attractor*. Studies a parallel CL_BHML lattice and proves joint preservation of the 4-element subset {0, 7, 8, 9} under both TSML and BHML composition; provides the "lens family" framing referenced in §6 of the present paper.

## Reproducibility

Verification: a `numpy` cell-by-cell check of the forcing theorem and a witness-construction-and-verification routine for the independence theorem is implemented in `cl_forcing.py` (deposited in the manuscript folder). Runs in under 1 second on a standard laptop. The reference matrix CL_TSML is hardcoded in the script; the seven witness magmas M_1, ..., M_7 are constructed by explicit cell modifications.

## Suggested reviewers

- An expert in finite-magma classification, quasigroup theory, or absorbing-element semigroup theory (Drápal, Wanless, Vojtěchovský lineage).
- An expert in algebraic combinatorics or Latin-square forcing problems (McKay, Wanless lineage).
- An expert in non-associative algebra (Schafer, Albert lineage).

(Specific names available on request from the corresponding author.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Per-venue cap note

This is the third paper from this research program targeting *Algebraic Combinatorics* (after J02 and the present paper). Per-venue cap is 1/quarter; if the cap is binding, an alternative venue (the *European Journal of Combinatorics*, *Journal of Algebraic Combinatorics*, or *Discrete Mathematics*) would be appropriate fallbacks given the explicit combinatorial cell-class structure of the result.

---

Sincerely,
B.R. Sanders
