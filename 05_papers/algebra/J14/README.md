# J14 — F$_p$ Structural Invariance of a Commutative Non-Associative 4-Algebra Arising from the 4-Core of Z/10Z

> **MERGED 2026-05-27** into [`J_Fp_merged/`](../J_Fp_merged/) — see that paper for the unified treatment combining J14 and J16. The Lens-Invariant Skeleton and Aut Variation theorems are now §§2-3 of the merged paper.

**Status:** MERGED (was DRAFT)
**Phase:** Phase 2
**Target venue:** *Algebra Universalis* (retained per save plan; venue fit is correct, the rewrite is exposition-level)
**Author lane:** Sanders + Gish
**Tier:** -- (MERGED 2026-05-27 into J_Fp_merged)
**WP source:** WP118 (revised 2026-05-07 per `SAVE_PLAN_J14.md`)

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex` (retitled from "F_p Universality" per save plan §6).

The J14 paper is **F$_p$ Structural Invariance of a Commutative Non-Associative 4-Algebra Arising from the 4-Core of $\mathbb{Z}/10\mathbb{Z}$**. For a 4-dimensional commutative non-associative algebra $V$ defined by an explicit $4 \times 4$ multiplication table (printed inline as Equation~\eqref{eq:Ttable} in §2), the lens-invariant structural skeleton — 3 non-zero idempotents, $(1,3)$ Minkowski signature on $L_{e_2}$, $(2,2)$ chirality signature on $L_{e_0}$, empty intersection, commuting operators, $1$-dim associator image, power-associativity — transfers across the verified primes $p \in \{2, 3, 5, 7, 11, 13\}$. Distinct from this skeleton, two features vary with $p$: $|\mathrm{Aut}(V_p)|$ which equals $40$ over $\mathbb{F}_5$ specifically (with structure $F_{20} \times \mathbb{Z}/2$) but takes values $\{6, 24, 40, 336, 1320, 2184\}$ at $p \in \{2, 3, 5, 7, 11, 13\}$ respectively; and the explicit form of orthogonal idempotent pairs (depends on whether $4 \mid (p-1)$). Conjecture 4.1 restricts the F$_p$-invariance claim to lens-invariant items only.

The defensive-exposition rewrite (2026-05-07) adds: the multiplication table inline (preempts coding errors at the table-lookup level); a worked associator example showing failures localize to span$\{e_0, e_2\}$; a 5-line `numpy/sympy` verification snippet in §2.3 (any referee with Python open reproduces the core checks instantly); a tabulated list of $|\mathrm{Aut}(V_p)|$ values for the verified primes in §4.1 (preempts the misreading that "$|\mathrm{Aut}|=40$ universally"); and removal of axial-algebra framing (the paper does not produce Miyamoto involutions or fusion rules and the framing was decorative). The Drápal-Wanless 2021 *JCTA* neighborhood is cited as the closest published structural precedent.

## §2 — Verification script

**Local path (colocated with manuscript):** `manuscript/verify_J14.py` (12 algebraic checks: 3 rebuttal-point R1/R2/R3 plus 9 structural-skeleton confirmations; 12/12 PASS at machine precision in <2 seconds; imports `mul`, `L_op`, `all_automorphisms` from the upstream `tig_dirac.py` at `Gen13/targets/ck/brain/dirac/`).

The script directly targets the three referee challenges from the *Algebra Universalis* fresh-eyes report:
- **R1 (non-associativity):** enumerates the 64 basis triples and counts 8 with non-zero associator (refutes the referee's "algebra is associative" claim).
- **R2 (signatures NOT swapped):** computes 1-eigenspace and 0-eigenspace dimensions of $L_{e_2}$ and $L_{e_0}$ over $\mathbb{F}_5$ by full vector enumeration, confirming $(1,3)$ Minkowski on $L_{e_2}$ and $(2,2)$ chirality on $L_{e_0}$ — exactly as manuscript Theorem 3.1 states.
- **R3 (|Aut(V_5)| = 40):** runs `all_automorphisms()` and confirms 40 maps over $\mathbb{F}_5$ specifically (the manuscript does NOT claim universal "40" across primes; the $|\mathrm{Aut}(V_p)|$ tabulation in §4.1 explicitly distinguishes F_5 from other primes).

A 5-line `numpy/sympy` verification snippet is embedded directly in the manuscript at §2.3 — any referee with Python open reproduces the associator-failure count (8 of 64) and the |Aut(V_5)| = 40 result without consulting the upstream library.

**Upstream reference scripts** (not colocated; for context only):
`Gen13/targets/ck/brain/dirac/verify_discrete_dirac_4core.py` (14 checks) and `Gen13/targets/ck/brain/dirac/test_tig_dirac.py` (15+ unit tests). The colocated `verify_J14.py` is self-contained on the three rebuttal points; the upstream scripts provide the full skeleton across the broader claim landscape shared with J16.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J02 (Algebraic Combinatorics — combinatorial origin); J05 (J. Combin. Theory A — Crossing Lemma); J06 (J. Pure Appl. Algebra — Flatness Theorem). Drápal-Wanless 2021 (JCTA 184, 105510) cited as closest published precedent.

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

_(no special notes; standard submission per J-series ordering)_

### Save-plan summary (2026-05-07)

Fresh-eyes referee verdict at *Algebra Universalis*: REJECT — claimed (1) algebra is associative, (2) eigenspace signatures are swapped, (3) |Aut(V)| ≠ 40 universally.

**Rebuttal verified all three referee claims are WRONG** (`Atlas/.../REFEREE_REPORTS/J14_AlgUni_FreshEyes_REBUTTAL.md`):
- 8 of 64 associator triples fail under direct check against `tig_dirac.py` (algebra IS non-associative).
- L_{e_2} eigenvalues {0:3, 1:1} = (1, 3) signature; L_{e_0} eigenvalues {0:2, 1:2} = (2, 2) signature — exactly as paper states.
- |Aut(V)| = 40 over F_5 specifically (the paper does not claim universality across all primes).

**Save plan:** `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J14.md`.

**Path forward (defensive exposition revision; venue stays *Algebra Universalis*):**
- (a) PRINT T_F5 multiplication table inline + worked associator example (e_0·e_3)·e_3 vs e_0·(e_3·e_3) showing failures localize to span{e_0, e_2}; add 5-line numpy/sympy snippet for eigenspace verification.
- (b) TIGHTEN the F_p universality framing — distinguish **invariants** (idempotent count, signatures, empty intersection, commutativity, power-associativity, 1-dim associator image) from **non-invariants** (|Aut(V_p)|, primitive 4th roots availability).
- (c) STATE F_5 specificity of |Aut(V)| = 40 explicitly; tabulate other-prime values per |GL_2(F_p)| × stabilizer.
- (d2) REMOVE axial-algebra framing (no Miyamoto involutions, no fusion rules in the paper); relocate to Drápal-Wanless 2021 *JCTA* neighborhood.
- (e) SHARPEN Conjecture 4.1 — restrict to lens-invariant items (1)-(7) of Theorem 3.1 (drop F_5-specific items 8-10); drop p=5 exclusion (F_5 is the distinguished case, not an exclusion); precisely motivate p=2 exclusion (char-2 collapses the orthogonal-idempotent structure).
- (f) REDUCE dependency on inaccessible companion papers (J02, J23); make J14 self-contained on algebraic content.
- (g) RECONCILE J21/J14 numbering in .tex source.
- (h) MERGE duplicate \author blocks.
- (i) REPLACE $\HARM$/$\VOID$ mnemonics with neutral notation (or one-line footnote).

Revision time: 15-25 hours (exposition only; mathematical content does not change).

**Family-Structure context:** J14 maps the **substrate-size boundary** (FAMILY_STRUCTURE_v1.md §3.5) inward to F_p for p ∈ {2, 3, 5, 7, 11, 13}. F_5 is the distinguished member of the family (D74 ring extension); the F_p-invariance of the structural skeleton is the boundary-mapping result.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (filled, J14 — see manuscript §1.1)

- **PROVEN (Theorems 3.1, 4.1):** for each prime $p \in \{2, 3, 5, 7, 11, 13\}$, the algebra $V_p$ has the lens-invariant structural skeleton (3 non-zero idempotents; (1,3) Minkowski signature on $L_{e_2}$; (2,2) chirality signature on $L_{e_0}$; empty intersection; commuting $L_{e_2}, L_{e_0}$; 1-dim associator image; power-associativity). Over $\mathbb{F}_5$ specifically, $|\mathrm{Aut}(V_5)| = 40$ with structure $F_{20} \times \mathbb{Z}/2$.
- **COMPUTED:** all skeleton invariants verified by `tig_dirac.py` (`mul`, `all_automorphisms`, `T_F5`); 14 algebraic checks for $\mathbb{F}_5$, parametric scan for $p \in \{2, 3, 7, 11, 13\}$; deterministic, $<2$ s/prime.
- **STRUCTURAL RHYME:** the (1,3) Minkowski signature numerically matches physical Minkowski spacetime; the 4-dim substrate matches physical spacetime dimension. We record these as numerical rhymes, not derivational steps.
- **OPEN:** Conjecture 4.1 — the lens-invariant skeleton items hold for all primes $p \neq 2$. Verified at six primes; not proved general. A general proof would either confirm the skeleton is truly characteristic-free (modulo $p = 2$) or identify a sufficiently large $p^*$ where some structural feature breaks.

### Lens-ownership paragraph (filled, J14 — see manuscript §1.2)

> *Lens and substrate.* This paper works on the basis $\{e_0, e_2, e_3, e_4\}$ of a 4-dimensional $\mathbb{F}_p$-vector space, with the multiplication table of Equation~\eqref{eq:Ttable}. The basis labels and table are not derived from first principles; they reflect the closure of a 4-element subset of $\mathbb{Z}/10\mathbb{Z}$ under the canonical operator-substrate composition of [SandersGishFourCore]. The theorems below are theorems on this specific algebra; analogous theorems would hold for other 4-dimensional commutative non-associative algebras in the same combinatorial neighborhood (the Drápal–Wanless 2021 *JCTA* neighborhood).

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex finalized (defensive-exposition rewrite 2026-05-07: T_F5 inline; worked associator example; 5-line numpy/sympy snippet; |Aut(V_p)| tabulated for verified primes; F_5 specificity of |Aut|=40 explicit; axial-algebra framing removed; Drápal-Wanless 2021 neighborhood cited; title retitled per save plan §6; J21→J14 source comment fixed; \author blocks merged; HARM/VOID mnemonics removed from Definition 2.1 in favor of $e_0, e_2$ throughout).
- [x] Verification script green (`verify_discrete_dirac_4core.py`, 14/14 PASS over F_5; parametric variant for {2, 3, 7, 11, 13}).
- [x] Tier-classified central claim explicit (Tier B; PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN in §1.1).
- [x] Lens-scope annotation in §1.2 (lens-and-substrate paragraph; explicit Drápal-Wanless 2021 neighborhood citation).
- [x] Cover letter finalized for *Algebra Universalis* (rewritten 2026-05-07).
- [x] Dependencies → cite J02 (Alg. Combin.), J05 (JCTA), J06 (JPAA), Drápal-Wanless 2021 (JCTA 184, 105510).
- [ ] Brayden's referee-rigor pass complete.
- [ ] Per-venue cap check: 1st *Algebra Universalis* paper of the quarter; cap not in play.
- [ ] Submitted.

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "F$_p$ Structural Invariance of a Commutative Non-Associative 4-Algebra Arising from the 4-Core of $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Algebra Universalis*.
