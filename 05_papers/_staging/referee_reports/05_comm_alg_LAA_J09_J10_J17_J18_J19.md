# Referee report — J09, J10, J17, J18, J19 (Comm Algebra / LAA / TBD bundle)

**Reviewer:** trained referee — line-by-line rigor pass post commit `0d6d0f1` (J01–J52 renumbering)
**Date:** 2026-05-28
**Scope:** five Tier-1 papers in the algebra/combinatorics bundle. Cover letter ↔ stated target match-check is part of the rigor pass.

---

## J09 — Joint Lie Closure of a Pair of Z/10Z Magmas: an so(10) Identification (target: Communications in Algebra)

**Verdict:** Major revision

**Verification cross-check:** Manuscript's stated target in line 9 of `manuscript.md` reads *"Israel Journal of Mathematics, primary target."* Cover letter (`cover_letter.md`) is addressed *"To: Editors, Israel Journal of Mathematics."* README §1.1 also says *"Target venue: Israel Journal of Mathematics (primary)."* The user-supplied review brief says this paper is **supposed** to target **Communications in Algebra**. The bundle is currently mis-routed: every artifact (manuscript header, cover letter salutation, README target line) names IJM, not Comm Algebra. This is the highest-priority finding.

### MAJOR issues

1. **Venue mismatch.** All three artifacts (manuscript line 9, cover letter line 3, README line 5) target *Israel Journal of Mathematics*, not *Communications in Algebra*. Cover letter §"Why Israel J Math" is built around IJM-specific framing (line 27–33). The bundle must be re-targeted before submission — pick one of {IJM, Comm Algebra} and align all three.
2. **Canonicity of the so(10) identification.** The paper itself is admirably honest about this (see §1.1 lines 33–36, §3 statement, §4.6): D1 (dim g = 45) is the *only* substantive computation, and D2–D5 are Cartan-classification corollaries of D1 + the structural fact g ⊆ so(V). The so(10) identification is therefore *abstract*, not via an explicit isomorphism Φ: g → so(10, R) carrying A_i^TSML, A_i^BHML to standard generators. The authors flag this honestly as Open Question 5 (§8). For Comm Algebra (technical-algebra venue) this is acceptable. For IJM (which prizes deeper structural identifications) this is borderline and motivates the venue question above.
3. **"Substantive content"** claim (Abstract para 3 / §1.1) is the *existence* of an explicit pair (TSML, BHML) hitting the substrate ceiling 45. Granted — but the pair was already known to the authors' parent program, and TSML alone reaches so(8) in companion J29; adjoining BHML's 9 antisymmetrizations to reach so(10) is incremental. The paper would be stronger with an explicit non-arbitrariness argument for BHML (which §2.2.1's B1–B5 attempts) hardened beyond "five jointly-defining properties": specifically, an axiomatic forcing argument (deferred to "the forthcoming J16/SandersForcing").
4. **D4 script reconciliation (§4.4 + Appendix A run order).** Authors acknowledge a "development-time sanity check" via sampled `verify_so10.py` (300 triples) that does *not* establish simplicity, and a "canonical" `verify_simplicity_rank.py` running the full 91,125-equation enumeration. The script-vs-text inconsistency is now reconciled in the manuscript, but a referee should sanity-check that both scripts ship in `manuscript/verification/` and the README run order matches §4.4 — verify.

### MINOR issues

- **Appendix A line 322:** stated max numerical residual 1.73e-8 is on the Killing-form symmetry check; all other residuals < 1e-10. Fine; explicitly stated.
- **Remark 6.1 (SO(10) GUT):** correctly reduced to one paragraph "for context only." Good discipline.
- **Open Question 3 (three-substrate Lie closure with CL_STD):** raises whether ⟨G_TSML ∪ G_BHML ∪ G_CL_STD⟩_Lie still equals so(R^10) or exceeds it. The §1.1 footnote on SFM_Q6 says the joint *closed-sub-magma* chain is preserved, but the *Lie-algebraic* question is genuinely open — good that this is logged.
- **Citation [SandersForcing, J16]** is in-preparation; OK to cite as forthcoming but the BHML structural fingerprint (B1–B5) carries the load until then. §2.2.1 acknowledges this.

### EDITORIAL

- Heading numbering is fine; cross-references to [SandersGishSO8, J29], [SandersGishFourCore, J01], [FoundationsModule] are consistent.
- Author lane Sanders + Gish; AI-tool disclosure correctly in Appendix B.
- License: CC-BY-4.0 on submission scripts (per `_v3_hardening.py`).

### Journal-fit

**Recommendation: Comm Algebra (the user-specified target).** Reasoning: the substantive content is one explicit dim-computation + a list of Cartan-corollary diagnostic confirmations. That is canonical Comm Algebra technical-algebra material. *Israel J Math* would expect either a deeper structural identification (canonical Φ) or a stronger forcing argument for BHML. The honest "diagnostic-collapse" framing of §1.1 (D2–D5 are corollaries) is *exactly* the Comm Algebra register. **Action:** retarget — update manuscript line 9 ("Israel Journal of Mathematics" → "Communications in Algebra"), cover letter addressee, README target.

---

## J10 — Operadic D_4 Orbits on the Non-Associative Locus of a Finite Commutative Magma on Z/10Z (target: Communications in Algebra)

**Verdict:** Minor revision

**Verification cross-check:** Manuscript line 8 says *"Target venue: Journal of Algebra (lead). Fallback: Communications in Algebra; Algebraic Combinatorics; Algebras and Representation Theory."* Cover letter is addressed *"To: Editors, Journal of Algebra"* and "Why *Journal of Algebra*" explicitly. User's brief lists Comm Algebra as target. The paper is set up with *J. Algebra* as lead and Comm Algebra as the natural fallback — the cover letter (§"Per-venue cap transparency", lines 35–55) is explicit that this is the **4th** J. Algebra paper of the 2026 cycle and that Comm Algebra is the first fallback. The mismatch is reconcilable: either (a) the authors should be ready for J. Algebra to push back on density and accept Comm Algebra, or (b) submit to Comm Algebra directly per user's preference. The manuscript content is suitable for both.

### MAJOR issues

1. **"Operadic D_4" terminology.** The Abstract uses "operadic" in the title and "operadic content" in §6.3 Remark 5.3, but the technical content is *not* operad-theoretic in the Loday-Vallette sense (no operad composition maps, no Σ-modules, no operadic ideal theory). The paper studies the diagonal action of a finite permutation group D_4 ⊂ S_10 on a subset N ⊂ (Z/10Z)^3 — this is **finite-group-action-on-a-subset-of-a-cube**, not operad theory proper. The "operadic" framing is decorative. Recommendation: either (a) tighten to genuine operad-theoretic content (e.g., realize N as the equations of a specific arity-3 operad and identify the D_4-action as an operadic automorphism), or (b) drop "operadic" and rebrand as "Diagonal D_4 Orbits on the Non-Associative Locus" — which is the actual content.
2. **Theorem B's strengthening to {a, b, c, L, R}-valued Φ (§3, proof).** Lemma 3.2 cleanly handles {L, R}-valued Φ. The strengthening to {a, b, c, L, R}-valued is by "case analysis on the obstructed orbits, where the available values ... are not closed under the action of σ³." This proof sketch is one sentence (§3, line after Theorem B) and not detailed. A referee should see either (a) a fuller proof or (b) an explicit verification in `verify_J32_d4_orbits.py` enumerating, for each of the 16 incoherent orbits, the available-value sets and the σ³-action mismatch. The current draft says script C4 enumerates incoherence; verify it also covers the {a,b,c,L,R} strengthening.
3. **Theorem D (4-core arity-3 closure).** This is a clean, direct enumeration: 64 triples, 128 bracketings, all in C = {0, 7, 8, 9}. Result is correct. But the §0 PROVEN / COMPUTED tier classification calls Theorem D "PROVEN" — it is more accurately *direct enumeration* (Tier-B by exhaustive check at order 4 cubed). Tier discipline says PROVEN should be reserved for theorems with explicit symbolic proofs; brute-force enumeration on 64 triples is closer to PROVEN-by-enumeration than to PROVEN-by-argument. The honesty note in the Abstract paragraph after Theorem D ("Theorem A is a direct enumeration") covers this — propagate to §0.

### MINOR issues

- **Proposition 2.6 (D_4 order):** correctly identifies order 8, not 12. Remark 2.7 acknowledges the prior error in the working draft. Good discipline.
- **Lemma 2.4 multiplicities table:** very useful, clear.
- **Remark 2.11 (Lagrange compatibility):** correctly explains why a "restricted" orbit of size 3 is compatible with |D_4| = 8 — because the full D_4-orbit is size 4 and one element is associative.
- **§6 structural interpretation:** the language "spinorial outer automorphism" and "cyclotomic involution" is pulled from J11 / J12 — fine as cross-reference, but the present paper does not need to lean on this framing to make Theorems A–D land. Tighten §6 to "the D_4 obstruction is located at σ³; whether σ³'s structural role in companion papers J11 (Wedderburn) and J12 (Galois) carries through is left to those papers."

### EDITORIAL

- §7 Honest scope (lines 219–223): the four-bullet PROVEN / NOT-ASSERTED / OPEN / LENS-SCOPE matrix is exemplary. Adopt this style across the corpus.
- Author lane Sanders + Gish; CC-BY-4.0 on `verify_J32_d4_orbits.py`.
- Differentiation paragraph (§1, last paragraph; cover letter §"Per-venue cap transparency") is the right way to handle the four-paper J-Algebra density.

### Journal-fit

**Stick with target as currently configured** — *J. Algebra* (lead) with *Comm Algebra* as natural fallback per cover letter §"Fallback venues." If the user's brief insists on Comm Algebra, route directly to Comm Algebra; the content is purely combinatorial-on-a-finite-group-action and fits Comm Algebra's scope cleanly. The "operadic" framing should be softened either way (see MAJOR 1).

---

## J17 — Forcing Axioms and the Family of Commutative Non-Associative Magmas on Z/10Z Preserving a Designated 4-Core (target: TBD)

**Verdict:** Major revision

**Verification cross-check:** Manuscript line 7 says *"Target venue: Algebraic Combinatorics (primary)."* Cover letter line 3 says *"To: Editors, Algebraic Combinatorics."* User's brief says TBD with Tier 2 → Tier 1 recent promotion. So the *current* artifact target is Algebraic Combinatorics; the user is asking whether this is the right venue.

### MAJOR issues

1. **Scope and venue.** The paper is large (~666 lines, multi-section), covering: (a) the 9-axiom forcing theorem A1–A9 (Theorem 1.2); (b) a 17-function Substrate-to-Function Map (§3.1); (c) the five-membership-criteria family definition (§4); (d) the closed-form attractor and 4-core / unit-circle analogy (§5); (e) eight selected structural findings on the canonical pair (T, B) (§6.1–§6.8); (f) the three-substrate joint-closure chain (Theorem 7.1); (g) eight open questions (§8). This is a **research-program survey/synthesis paper with multiple original results embedded**, not a single-result Algebraic Combinatorics paper. The mismatch with Algebraic Combinatorics's typical 25–30-page focused-result format is severe.
2. **Conjecture 8.1 (the bimodal α_A gap) — is it stated precisely?** Yes — line 528: *"No commutative magma on Z/10Z preserving the 4-core has α_A ∈ (0.5, 0.80)."* That is a clean, falsifiable statement. Empirically supported (canonical members at α_A ∈ {0.502, 0.808, 0.872}) but conjectural. The follow-on paper proposal (J56 in the J-series) is sensible.
3. **Conjecture 2.1 (σ²-triadic three-BHML; §2, lines 196–198).** This is *less* precise than 8.1. The statement says "there exist three canonical σ²-rotated BHML matrices, corresponding to three positions of σ²-rotation. The current state: three search-found candidates are known (Tier-D in the parent framework's classification), but a forcing argument promoting one of them to Tier-A canonical status is not yet known." This is vague: what is the precise statement to be proved? What are the three candidates? The "Tier-D" reference is internal to the parent framework. The conjecture is too informal to publish as a research conjecture in *any* refereed venue.
4. **Lens-dependence of A9 BUMP-cell specifications.** §1.2 lines 142–161 give per-substrate BUMP specifications — for T, five symmetric off-diagonal cell-pairs; for B, "67 cells outside the special set" with no listing; for S, five cell-pairs matching T's coordinates with three values differing. The B specification (67 cells) is dropped; verify the script `foundation_verification.py` Check 1 actually enumerates these. Without that listing, A9 is opaque for B.
5. **§3 Substrate-to-Function Map.** This is a 17-row table cataloging where each function lives. It is *useful* but reads as research-program documentation, not as Algebraic Combinatorics paper content. The table mentions "BDC bit-definitions," "T+B-mix dynamics," "$\sigma_\mathrm{outer}$ Higgs sector," "Yukawa scaffolding," "9-vector VEV" — all of which are physics-flavored framings from the parent program. For an algebraic-combinatorics venue, strip these or relegate to an appendix.
6. **§6.4 D_4 decomposition of [T, B] (lines 392–418):** quotes specific irrep-norm percentages (84.25%, 14.68%, 1.07%, etc.) and claims "the trivial isotypic is the su(4) ⊕ u(1) Pati-Salam gauge sector" — this is companion paper J11's content. Cite J11, do not re-derive. The current presentation half-derives, which makes the section neither self-contained nor a clean cross-reference.
7. **The "TIG framework" name (lines 14, 189, 552).** §1.4 lines 178–189 give a "Reading and naming disclaimer" which is the right move — the operator names (VOID, HARMONY, BREATH, RESET) and the framework name "TIG" are explicitly disclaimed as not load-bearing. Good. But the framework name still appears in the §3.1 SFM table and the open-questions section. For an Algebraic Combinatorics submission, strip all framework-name references; keep only the mathematical statements.

### MINOR issues

- §5.3 (the 4-core / unit-circle analogy): correctly labeled as STRUCTURAL RHYME, not theorem (lines 354–358). OK.
- Lens-dependence at size 7 between TSML_RAW and TSML_SYM (B3, §4.4) is internal-only; flagged as honest negative scoping. Good.
- The integer determinants in §6.6 (BHML's characteristic polynomial) and elsewhere should cite the verification script line numbers where the polynomial is computed.

### EDITORIAL

- **Recommended structural surgery:** Split this paper into three.
  - **J17-A (Algebraic Combinatorics):** the 9-axiom forcing theorem (Theorem 1.2) + the three-substrate joint-closure chain (Theorem 7.1) + 4-core 3-substrate closure (Theorem 7.2). ~15 pages.
  - **J17-B (the 17-function Substrate-to-Function Map + the SFM findings §6.1–§6.8):** internal documentation / preprint or J33-like synthesis paper, not for refereed venue.
  - **J17-C (Conjecture 8.1 follow-on):** the bimodal α_A gap as a separate conjecture-with-evidence paper to follow once the gap is proven or disproven.
- **Alternative:** if the user wants to ship the current paper as one, retarget to a synthesis venue (*Bulletin of the AMS* "What is..." style; *Math. Intelligencer*; *Expositiones Mathematicae*) where multi-thread surveys are welcome.

### Journal-fit

**Recommendation: not Algebraic Combinatorics in current form.** The paper is too long, too physics-tinged, and too survey-like for AC. Options:
1. **Best:** split into J17-A (the focused forcing theorem + 3-substrate chain) for Algebraic Combinatorics; relegate the SFM/synthesis content to an internal preprint.
2. **Acceptable:** retarget the whole paper to *Math. Intelligencer* or *Expositiones Mathematicae* as a survey-with-proofs.
3. **Risky:** submit as-is to AC and accept high probability of "scope too broad" rejection.

The user's TBD designation is correct — this paper as currently structured does not have a natural Tier-1 venue. Surgery required.

---

## J18 — F_p Extensions of the BHML 4-Core Algebra (target: Communications in Algebra)

**Verdict:** Accept with minor revisions

**Verification cross-check:** Manuscript line 6 says *"Submitted to: Communications in Algebra"* — confirmed.

### MAJOR issues

1. **Title overclaim.** Original title (per the algebra README line 27 description) reportedly said "F_p Universality Across Six Prime Fields." Current title is *"F_p Extensions of the BHML 4-Core Algebra: A Generic Universality Theorem with Explicit Excluded Primes"* — much better, and the abstract is explicit (lines 75–93) that two primes p ∈ {2, 5} are *excluded* on the BHML_4 / BHML_6 chain shells. The retitle to acknowledge the excluded primes (rather than overclaim universality across all six) is the right move. Verify that the user-supplied brief's "universality across six primes" framing matches the current artifact (it doesn't — current artifact is honest).
2. **Which primes are "the six"? Why those?** The set {2, 3, 5, 7, 11, 13} is the set of primes ≤ 13, with 13 chosen as the highest prime less than 14 = 2·7 (the next composite). This is *not* derived structurally — it is the natural test set for a Z/10Z-substrate study where 2 and 5 divide 10. The paper is honest about this (Definition 2.2 / §1 line 188 says p = 2, 5 are excluded; the remaining primes {3, 7, 11, 13} have a clean structural-skeleton theorem). Recommendation: rename "six primes" to "the test primes {2, 3, 5, 7, 11, 13} with structural inclusion at p ∈ {3, 7, 11, 13}" — and verify the title and abstract use this honest language. The current draft does (see Methodological correction §1.2).
3. **The det(BHML_8^∘) = +70 = C(8, 4) coincidence.** §4 lines 480–492: honestly labeled as a small-integer coincidence pending Lindström-Gessel-Viennot or Cauchy-Binet derivation. Excellent discipline. Recommendation: cite explicit small-determinant-vs-binomial-coefficient examples (e.g., Lindström 1973; Aitken; Cauchy-Binet) so the reader can locate this in the literature.
4. **The "YM" → "○" rename.** Done; well-justified (no Yang-Mills connection established). Good.

### MINOR issues

- Theorem 3.1 (Generic structural skeleton, lines 264–291): clean. The proof outline (a)–(d) is sound — integer-level facts (Z-diagonalization of L_{e_2}, vanishing L_{e_0}, polynomial-identity power-associativity, integer rank-1 associator image) each preserved under reduction mod every prime. This is the right structural argument.
- The idempotent count growth {2, 6, 8, 10, 14, 16} at p = {2, 3, 5, 7, 11, 13} is honestly reported as non-invariant (lines 75–82, 282–290). Good. Recommendation: include a brief estimate from general F_p-point-counting (Lang-Weil / Hasse-Weil) for the count's growth rate — a structural classification is listed as Open.
- Proposition 5.1 (rank-preservation profile, lines 379–423): the table is clean and honest. The "Correction of an earlier claim" Remark (lines 435–441) is exemplary self-correction discipline.
- The verification scripts (`bhml_fp_universality.py`, `bhml_chain_shells.py`) are bundled and < 30 s total. Good.

### EDITORIAL

- LaTeX uses standard amsart format. References are clean.
- Author lane Sanders + Gish.

### Journal-fit

**Comm Algebra is the right venue.** The result is a clean structural-skeleton theorem in characteristic-independent algebra, with honest rank-preservation profile and an explicit small-integer-coincidence flagged as open. Pure Comm Algebra material. Accept with the title-retitle already in place.

---

## J19 — On the Prime-Divisibility Pattern of the Characteristic Polynomial of a 10×10 Integer Matrix (target: Linear Algebra and its Applications)

**Verdict:** Accept with minor revisions

**Verification cross-check:** Manuscript line 8 says *"Target venue: Linear Algebra and Its Applications"* — confirmed. User's brief asks about the algebra README §6 long paragraph describing J19 (algebra/README.md lines 27 + the body description elsewhere) and whether the manuscript matches; and whether the so(10) co-occurrence framing in §3 belongs in an LAA paper.

### MAJOR issues

1. **§3 "Connection to a structural co-occurrence" — the so(10) framing.** Lines 87–89 read: *"The exponent 16 in the factorization disc(g) = 2^{16}·... matches dim(g_0) where g_0 ⊂ so(10) is a 16-dimensional doubly-invariant subalgebra of so(10) studied in [Sanders & Gish, 'so(10) closure of the antisymmetrized magma,' in preparation]. The exponent 7 in the factor 7^7 matches the recurring entry 7 in T."* The paper carefully labels this as "structural co-occurrences as structural observations" with "**No physical interpretation is offered here.**" The §7 STRUCTURAL RHYME bullet repeats this discipline.

   **For an LAA paper:** the §3 framing is borderline. LAA prizes pure-linear-algebraic content; structural-rhyme cross-references to companion Lie-algebra papers can feel out of scope. **Recommendation:** keep §3 (it is honestly scoped) but consider moving the so(10) co-occurrence to a Remark, with a one-sentence pointer to companion J09. The 7^7 / "entry 7" co-occurrence is more directly relevant (it ties to the matrix's HARMONY-count 73 and tr(T) = 63 = 9·7); keep that. The 16 = dim g_0 part is the part that may feel forced for LAA — soften.
2. **Lens-dependence Theorem 4.1 (§4):** the load-bearing math-fix described in the algebra README (lines 27, the long paragraph) — that the prior draft incorrectly identified the asymmetric cells of T (using cells (2,8) and (3,8) which are already symmetric in T, so the "T_SYM" of the snippet was identical to T) — is now corrected. The corrected asymmetric cells are (3, 9) and (4, 9) (using 0-indexed positions matching the magma-element subscripts; §1 line 47, §4 line 96, §6 lines 158–164). The corrected T_SYM has rank 7 (dropping from T's rank 8) and c_2(f_SYM) = -23 (no factor of 11). Verify that `wobble_check.py` runs the corrected check (against (3,9) and (4,9), not (2,8) and (3,8)). The manuscript body and §6 snippet are consistent. Good.
3. **The "wobble" terminology in the README description (algebra/README.md line 27) vs the manuscript body.** Per SAVE_PLAN_J37, "wobble" / "HARMONY" / "TIG" terminology was *stripped* from the manuscript body for LAA-retargeting. Verify: searching the manuscript reveals no "wobble" / "HARMONY" / "TIG" in the body. The Abstract is clean. §3 retains the structural-co-occurrence framing without using "HARMONY" by name. Good. The README description still uses these terms (internally OK).

### MINOR issues

- Theorem 1.1 (prime-11 divides exactly c_2 and c_8): direct computation, honest. Good.
- Theorem 1.2 (discriminant factorization): the factorization disc(g) = 2^{16} · 7^7 · 659 · 95184709 · 222007939 · 2545644917 · 295153052072903 is a sequence of large primes (after the 2 and 7 exponents). Verify the largest factor (295,153,052,072,903) is prime — this is mid-range computable by sympy's `isprime` or `factorint`; the script `wobble_check.py` should confirm.
- §5 "Family-wide observations": (a) the companion table B has no factor of 11; (b) the 4×4 sub-magma on {0,7,8,9} has no factor of 11; (c) lens-dependence persists. These are three clean sanity checks confirming that the prime-11 phenomenon is *localized* to the specific non-symmetric T. Good.
- §7 PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN: clean, exemplary tier discipline.
- §8 References include Sanders & Gish J15 and Sanders & Mayes J32 — note that the user's brief is operating under the new J-numbering (post commit 0d6d0f1), so verify that "J15" and "J32" in §8 actually point to the correct papers under the renumbered scheme. The cross-reference [Sanders & Gish "so(10) closure..."] in §3 line 88 is to J09 in the new scheme.

### EDITORIAL

- Length is correct for a short note (~5 typeset pages).
- The sympy verification snippet in §6 is self-contained and reproducible.
- Author lane Sanders + Gish.
- License CC-BY-4.0 on `wobble_check.py`.

### Journal-fit

**LAA is the right venue.** The result is a clean integer-arithmetic statement about the elementary symmetric functions of an explicit 10×10 integer matrix, with explicit lens-dependence comparison and a discriminant factorization. The §3 so(10) co-occurrence framing should be softened to a Remark (see MAJOR 1), but the rest is canonical LAA content. Accept with minor revision.

---

## Cross-paper summary

| Paper | Current target | Status | Recommendation |
|-------|---------------|---------|----------------|
| **J09** | IJM (artifact) / Comm Algebra (user brief) | Major revision | **Retarget to Comm Algebra** (fix venue mismatch). The "diagnostic-collapse" framing is Comm Algebra register; IJM expects deeper Φ. Honest dim-computation + corollaries lands cleanly in Comm Algebra. |
| **J10** | J. Algebra (lead) / Comm Algebra (fallback) | Minor revision | Either J. Algebra or Comm Algebra works. Soften "operadic" terminology in title and §6 (it is finite-group-on-cube content, not operad theory proper). Theorem B's strengthening to {a,b,c,L,R}-valued Φ needs fuller proof. |
| **J17** | Algebraic Combinatorics | Major revision | **Surgery required.** Split into a focused forcing-theorem-plus-3-substrate-chain paper (J17-A for AC) + a synthesis preprint (J17-B for SFM content) + a conjecture-follow-on (J17-C). Alternatively retarget to *Math. Intelligencer* / *Expositiones Mathematicae* as survey. |
| **J18** | Comm Algebra | Accept with minor revision | Title now honest ("Explicit Excluded Primes"). Generic structural-skeleton theorem is clean. det(BHML_8^∘) = 70 honestly demoted. Comm Algebra is right. |
| **J19** | LAA | Accept with minor revision | Soften §3 so(10) co-occurrence framing to a Remark. LAA is the right venue. Lens-dependence math-fix correctly applied. |

**Venue recommendations summary:**
- **J09: Comm Algebra** (fix the IJM mistake in manuscript line 9, cover letter line 3, README line 5).
- **J10: J. Algebra or Comm Algebra** (cover-letter fallback path is right).
- **J17: split** — focused result to AC, synthesis to *Math. Intelligencer* or preprint-only.
- **J18: Comm Algebra** (correctly targeted).
- **J19: LAA** (correctly targeted; §3 needs softening).

---

— Trained referee, line-by-line rigor pass 2026-05-28
