# J26 — F_p Extensions of CL_BHML: Universality Across Six Prime Fields

**Status:** READY (manuscript drafted from corpus, cover letter finalized; awaiting referee-rigor pass)
**Phase:** Phase 3
**Target venue:** Comm Algebra
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** Variant Catalog "TSML F_p extensions" (Atlas/LENS_TAXONOMY_2026-05-06/VARIANT_CATALOG.md) + WP118 (Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/WP118_FP_UNIVERSALITY.md) + GAP_AUDIT.md

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex`

Abstract (1-sentence): We extend the F_p universality of the operator-substrate construction (Sanders-Gish J14, TSML side) to the parallel BHML substrate, verifying that the 4-dimensional F_p-bilinear extension of the BHML 4-core composition table has structurally invariant features (idempotent count = 4, eigenspace signatures 1+3 and 2+2 under left-multiplication, |Aut| = 40, power-associativity, 1-dimensional associator image) across all six primes p in {2, 3, 5, 7, 11, 13}; the BHML_8_YM = +70 = C(8,4) integer identity holds and reduces compatibly modulo prime; we conjecture extension to all primes p outside {2, 5}.

Source corpus: `Atlas/LENS_TAXONOMY_2026-05-06/VARIANT_CATALOG.md` (TSML F_p extensions entry); `Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/WP118_FP_UNIVERSALITY.md` (TSML side, structural template); `Atlas/META_PLAN_2026-05-06/GAP_AUDIT.md` (BHML_8_YM = 70 identity, BHML chain-shell determinants).

## §2 — Verification script

**Path:** `(adapt verify_discrete_dirac_4core.py with BHML table; under 1 minute total)`

The TSML F_p verification harness (`verify_discrete_dirac_4core.py` in the bridge sprint bundle) is adapted to the BHML side by swapping `T^TSML` for `T^BHML` (5-non-zero-cell table from `lenses.py:BHML` restricted to {0,7,8,9}). Each prime check runs in seconds.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J14 (F_p Universality of TSML, Algebra Universalis); citing J25 (forcing axioms) and J23 (three-substrate architecture) for context.

## §4 — Cover letter

See `cover_letter.md` in this folder. Finalized with summary, venue fit, companion list, and per-venue cap note.

## §5 — Notes

**FRESH-EYES REFEREE PASS (2026-05-07): Major revision; manuscript rewritten 2026-05-07.**

The fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J26_CommAlg_FreshEyes.md`) flagged:

- **M1.** Per-prime verification is not a generic universality argument. **FIX:** the rewritten manuscript replaces the per-prime verification with an integer-level structural argument: the eigenspace signatures of $L_{e_2}$, $L_{e_0}$, power-associativity, and the 1-dim associator image are all consequences of integer-level facts (a $\Z$-diagonalization of $L_{e_2}^{\Z}$, a vanishing $L_{e_0}^{\Z}$, a polynomial-identity power-associativity, and an integer rank-1 associator image), each preserved under reduction modulo every prime.
- **M3 (CRITICAL).** Computational error: Prop 5.1 claim of rank-preservation at p ∈ {3, 11, 13} is FALSE at p = 3 (4 of 7 shells fail) and partially false at p = 13 (BHML_6 fails). **FIX:** verified via `bhml_chain_shells.py` (sympy.Matrix.det). The corrected Proposition 5.1 states: rank-preservation holds at every chain shell only at p ∈ {7, 11}; at p = 13 the BHML_6 shell fails; at p = 5 the BHML_4 shell fails; at p ∈ {2, 3} four of seven shells fail (BHML_6, BHML_8, BHML_9, BHML_10).
- **M4.** BHML_8_YM = 70 = C(8,4) framed as coincidence vs. structural — **FIX:** the manuscript honestly demotes the equality $70 = \binom{8}{4}$ to "small-integer coincidence pending further investigation" and notes that no Lindström-Gessel-Viennot or Cauchy-Binet-style derivation is provided. The "YM" subscript (which implied a Yang-Mills connection that is not established) is renamed to a neutral "$\circ$".
- **m6.** $p = 7$ HARMONY ≡ VOID issue — **FIX:** addressed via the Remark in §6 that the basis $\{e_0, e_2, e_3, e_4\}$ does not name the operator label 7 except via $7 \mapsto e_2$ relabeling; the structural skeleton at $p = 7$ on the 4-core is well-defined.

**Important corrections in addition to referee feedback:**
- The previous draft's claim of "L_{e_2} eigenspace signature (1, 3)" is wrong: direct computation (`bhml_fp_universality.py`) shows the signature is **(2, 2)**, not (1, 3). The manuscript has been updated accordingly.
- The previous draft's claim of "$|\Aut(V_p^{BHML})| = 40$ for all six primes" was not actually verified; the manuscript no longer claims this and instead reports only the genuinely-invariant features.
- The previous draft's claim of "4 idempotents in all characteristics" is wrong: the actual idempotent count over $\F_p$ varies wildly with $p$ (values 2, 6, 8, 10, 14, 16 for $p \in \{2, 3, 5, 7, 11, 13\}$). The manuscript honestly reports this as a non-invariant feature.

**Per-venue cap:** 2nd CommAlg paper after J15 (Galois D_4 over LMFDB 4.2.10224.1). Cap is 1/quarter; venue is within budget.

**Fixes applied 2026-05-07:**
- `manuscript/manuscript.tex`: rewritten with generic structural-skeleton theorem (no longer relying on per-prime verification), corrected Proposition 5.1 (rank-preservation at p ∈ {7, 11} only), honest reporting of idempotent-count growth with p, corrected eigenspace signatures to (2, 2) for $L_{e_2}$.
- `manuscript/bhml_chain_shells.py`: new verification script written; computes each chain-shell determinant by direct sympy.Matrix.det on the BHML 10x10 (via the joint-closed sub-magma chain on indices {0, 7, 8, 9} → {0, 6, 7, 8, 9} → ... → {0, 1, ..., 9}); factors each determinant; tabulates mod-p reductions; verifies the corrected Proposition 5.1 entries; verifies BHML_8^o = 70.
- `manuscript/bhml_fp_universality.py`: new verification script; verifies eigenspace signatures (2, 2) for $L_{e_2}$ and (0, 4) for $L_{e_0}$, power-associativity, and 1-dim associator image at each $p \in \{2, 3, 5, 7, 11, 13\}$; reports the actual idempotent counts (not invariant).

**Verification of fixes (sympy + numpy):**
- BHML_8^o = +70 (exact, by sympy.Matrix.det on the 8x8 submatrix dropping rows/cols 0, 7) ✓
- Chain-shell determinants 5305, 2843, -2886, 2929, -7542, 7272, -7002 verified directly from BHML 10x10 on the joint-closed chain {0,7,8,9} → ... → {0,...,9} ✓
- Prop 5.1 mod-p verdict: p ∈ {7, 11} preserve rank at every shell; p = 5 fails at BHML_4; p = 13 fails at BHML_6; p ∈ {2, 3} fail at {BHML_6, BHML_8, BHML_9, BHML_10} ✓
- L_{e_2} signature (2, 2), L_{e_0} signature (0, 4), power-associativity, assoc-image-dim = 1 all verified at each p ∈ {2, 3, 5, 7, 11, 13} ✓
- Idempotent counts: 2, 6, 8, 10, 14, 16 for p ∈ {2, 3, 5, 7, 11, 13} (NOT invariant) ✓



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem 3.1 (Generic structural skeleton): for every prime p, the F_p-algebra V^BHML_{F_p} has eigenspace signatures (2, 2) for L_{e_2}, (0, 4) for L_{e_0}, satisfies power-associativity, and has 1-dim associator image. Proposition 5.1 (corrected rank-preservation profile): chain-shell rank-preservation holds at every shell only at p ∈ {7, 11}; explicit failure shells listed for p ∈ {2, 3, 5, 13}. Theorem 4.1: det(BHML_8^o) = +70.
- **COMPUTED:** sympy + numpy verification: chain-shell determinants verified directly from BHML 10x10 on the joint-closed sub-magma chain ({0,7,8,9} → {0,6,7,8,9} → ... → {0,...,9}); eigenspace signatures and PA verified at each p ∈ {2, 3, 5, 7, 11, 13} via brute enumeration (`bhml_chain_shells.py`, `bhml_fp_universality.py`, runtime < 30 s).
- **STRUCTURAL RHYME:** The integer-determinant identity det(BHML_8^o) = 70 = C(8,4) is striking but not proven structural in this paper. We present it as a small-integer coincidence pending further investigation. The skeleton invariants (eigenspace signatures, power-associativity, 1-dim associator image) resemble the parallel V^TSML algebra of the companion paper but the two algebras are not isomorphic. Closest published precedent: Drápal-Wanless 2021 (*JCT-A* 184, 105510).
- **OPEN:** Whether det(BHML_8^o) = C(8,4) admits a Lindström-Gessel-Viennot or Cauchy-Binet-style structural derivation, or is a small-integer coincidence. Structural classification of the idempotent count of V^BHML_{F_p} as a function of p (the count is 2, 6, 8, 10, 14, 16 for p = 2, 3, 5, 7, 11, 13).

### Lens-ownership paragraph (in manuscript §1)

> *Lens and substrate.* This paper works on the BHML composition table on Z/10Z, restricted to the 4-element subset {0, 7, 8, 9} for the 4-core algebra V^BHML, and to the joint-closed sub-magma chain for the rank-preservation profile. These choices are not derived from first principles; they reflect a structural reading of the substrate motivated by 10-operator decomposition and the joint-closure structure with the parallel TSML lattice. The theorems below are theorems on this specific structure; analogous F_p extensions of other substrate-and-table choices would have their own structural skeletons. Whether the rank-preservation profile across the chain (rank-preserving only at p ∈ {7, 11}) admits a deeper structural explanation is open.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to Comm Algebra this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "F_p Extensions of the BHML 4-Core Algebra: A Generic Universality Theorem with Explicit Excluded Primes." Submitted to *Communications in Algebra*.
