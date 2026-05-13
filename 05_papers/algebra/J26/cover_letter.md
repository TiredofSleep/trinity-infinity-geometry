# Cover letter — J26: F_p Extensions of the BHML 4-Core Algebra: A Generic Universality Theorem with Explicit Excluded Primes

**To:** Editors, *Communications in Algebra*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *F_p Extensions of the BHML 4-Core Algebra: A Generic Universality Theorem with Explicit Excluded Primes*

---

## Summary

The BHML 4-core algebra V^BHML is a 4-dimensional commutative non-associative algebra over Z defined by an explicit multiplication table on the basis {e_0, e_2, e_3, e_4}. We give a generic structural-skeleton theorem (Theorem 3.1): in every characteristic, the F_p-reduction V^BHML_{F_p} has identical eigenspace signatures of left-multiplications L_{e_2} (signature (2, 2)) and L_{e_0} (signature (0, 4)), satisfies power-associativity, and has a 1-dimensional associator image. These four invariants follow from integer-level structural facts (a Z-diagonalization of L_{e_2}^Z, a vanishing L_{e_0}^Z, a polynomial-identity power-associativity, and an integer rank-1 associator image), each preserved under reduction modulo every prime. We honestly note that the idempotent count is not an invariant — it grows with p (values 2, 6, 8, 10, 14, 16 for p = 2, 3, 5, 7, 11, 13). We further give an honest rank-preservation profile (Proposition 5.1) for the chain shells of the BHML composition table on Z/10Z: rank-preservation holds at every chain shell only for p ∈ {7, 11}; explicit failure shells listed for p ∈ {2, 3, 5, 13}. The integer determinant det(BHML_8^o) = +70 (Theorem 4.1) is verified by direct computation; we report this as an integer identity without claiming a structural derivation of the equality 70 = C(8, 4).

## Why Communications in Algebra

- The paper studies a small finite commutative non-associative algebra over F_p with explicit structural invariants. The closest published precedent is Drápal-Wanless 2021 (*JCT-A* 184, 105510) on maximally non-associative quasigroups — same domain, different specific structure. The neighborhood is well-served by *Communications in Algebra*.
- The generic universality result is established by integer-level structural arguments, not per-prime verification. The technique (Z-diagonalization + characteristic-independent rank arguments) is a clean exercise in finite-field algebra appropriate to the venue.
- The honest rank-preservation profile (Proposition 5.1) corrects a previously circulated false claim and provides explicit modular failure data verified by direct integer computation. This kind of honest computational follow-through is in the venue's tradition.

## Revision history

This is a Major-Revision resubmission following an external referee report (2026-05-07). The revision adopts the referee's central recommendation: **replace per-prime verification with a generic structural argument over Z**. Specific changes:

(i) The previously-claimed "rank-preservation at p ∈ {3, 11, 13} across all chain shells" is corrected. Verified via sympy.Matrix.det on the BHML 10x10 directly (script `bhml_chain_shells.py`): rank-preservation holds at every chain shell only at p ∈ {7, 11}; at p = 13 the BHML_6 shell fails; at p = 5 the BHML_4 shell fails; at p ∈ {2, 3} four of seven shells fail (BHML_6, BHML_8, BHML_9, BHML_10).

(ii) The previously-claimed "L_{e_2} eigenspace signature (1, 3)" is corrected to **(2, 2)**, verified by direct computation on the explicit 4x4 multiplication table T^BHML.

(iii) The previously-claimed "$|\Aut(V_p)| = 40$ across all primes" is removed — that claim was not actually verified, and the manuscript no longer makes it. The genuinely-invariant features are now the eigenspace signatures, power-associativity, and the associator-image dimension.

(iv) The previously-claimed "4 idempotents in all characteristics" is corrected: the idempotent count over F_p is **not invariant**, growing with p (2, 6, 8, 10, 14, 16 for p = 2, 3, 5, 7, 11, 13). The manuscript honestly reports this.

(v) The "BHML_8_YM = 70 = C(8, 4)" framing is rewritten: the "YM" subscript (which implied a Yang-Mills connection that is not established) is renamed to a neutral $\circ$. The equality 70 = C(8, 4) is reported as a small-integer coincidence pending further investigation; no Lindström-Gessel-Viennot or Cauchy-Binet-style derivation is claimed.

(vi) Two verification scripts are added: `bhml_chain_shells.py` (computes chain-shell determinants directly from BHML 10x10, factors them, tabulates mod-p reductions, verifies Proposition 5.1) and `bhml_fp_universality.py` (verifies eigenspace signatures, power-associativity, associator-image dimension at each p ∈ {2, 3, 5, 7, 11, 13}; reports actual idempotent counts).

## Companion submissions

- J21 (submitted, *American Mathematical Monthly*) — *The 5D Force Vector as a CRT Fourier Embedding of Z/10Z into R^5*. The companion CRT-Fourier embedding for the same Z/10Z substrate; cited for the σ-permutation and the 4-core {0, 7, 8, 9}.
- J25 (submitted, *Algebraic Combinatorics*) — *The CL_TSML Composition Lattice on Z/10Z: Structural Axioms, Independence, and a 73-HARMONY Forcing Theorem*. The forcing-axiom characterization of the parallel TSML lattice; positions the BHML lattice in the lens family.
- (in preparation) — *The 4-Core {0, 7, 8, 9}: Joint TSML+BHML Closure and the Universal Attractor*. Establishes joint preservation of the 4-element subset under both TSML and BHML composition; provides the chain framework cited in §5.

## Reproducibility

Two verification scripts: `bhml_chain_shells.py` (sympy.Matrix.det on the BHML 10x10 chain shells; runs in <1s) and `bhml_fp_universality.py` (brute enumeration of idempotents and eigenspace dimensions over F_p; runs in <30s combined). All numerical claims of the manuscript are reproduced by these scripts.

## Suggested reviewers

- An expert in commutative non-associative algebras (Albert / Schafer / axial-algebra lineage).
- An expert in finite-field linear algebra and characteristic-independent invariants of small finite algebras.
- An expert in F_p extensions of Z-defined multiplication tables, particularly in the Drápal-Wanless 2021 line of work.

(Specific names available on request from the corresponding author.)

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Per-venue cap note

This is the second paper from this research program targeting *Communications in Algebra*. Per-venue cap is 1/quarter; the venue is within budget.

---

Sincerely,
B.R. Sanders
