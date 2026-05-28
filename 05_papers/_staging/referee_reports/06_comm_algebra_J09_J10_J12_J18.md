# Referee Report 06 — Communications in Algebra Bundle (J09 / J10 / J12 / J18)

**Referee:** trained reader, *Communications in Algebra* standards
**Date:** 2026-05-27 (post-renumbering commit 0d6d0f1)
**Scope:** rigor pass on four candidates targeting Comm Algebra. Manuscripts read line-by-line; verification scripts spot-checked for structural consistency with manuscript claims.

Comm Algebra fit profile applied here: focused technical algebraic results, typically 10–20 pages, theorems precisely stated with full proofs, computational content cleanly separated from theoretical claims, exact references (LMFDB IDs, etc.), and Lie-algebra identifications shown to be *canonical*, not merely abstract isomorphisms.

---

## J09 — Joint Lie Closure of a Pair of Z/10Z Magmas: an so(10) Identification

**Verdict:** **Major revision (or re-route).** The substantive result (dim g = 45 = dim so(R^10)) is correct and verification-backed, but the *cover letter targets Israel J Math while the brief routes this paper to Comm Algebra* — Comm Algebra readers will read the title as promising a canonical so(10) identification, which the paper does not deliver and explicitly disclaims.

**Verification cross-check:** `verify_so10.py` performs the closure dim → 45 computation honestly (the sampled simplicity test is properly demoted to "development-time sanity check"); `verify_simplicity_rank.py` exists and is referenced as canonical for the full 91,125-equation enumeration of D4 and the rank-5 Cartan construction. Killing-form residual 1.73e-8 acknowledged. Scripts match the manuscript's tier discipline.

### MAJOR issues

1. **The "so(10) identification" is not canonical, it is an abstract isomorphism.** The manuscript is admirably honest that diagnostics D2–D5 are *corollaries* of D1 (dim = 45) plus the Cartan classification (Corollary 4.2; §4.6). A Comm Algebra Lie-algebra referee will push exactly on this: an abstract iso to so(10, R) of any 45-dim Lie subalgebra of so(V) for V = R^10 is *automatic*, since g ⊆ so(V) and dim g = dim so(V) forces g = so(V). The substantive content reduces to "dim g = 45", i.e. that the joint closure saturates so(V). Calling the result an "so(10) identification" in the title overstates this — the standard inclusion so(8) ⊂ so(10) ⊂ so(V) is the *substrate* inclusion, not a canonical realization of a specific so(10) action.
2. **Comm Algebra has tougher referees on Lie-algebra titles than J. Algebra.** Recommend either: retitle as *"Two Z/10Z magmas whose antisymmetrized Lie closure saturates so(R^10)"* (honest scope), or route to *Linear Algebra and its Applications* / *Algebras and Representation Theory* where the dim-saturation framing reads naturally.
3. **Cover-letter / target mismatch.** Cover letter is addressed to Israel J Math; the present brief routes it to Comm Algebra. Either reconcile or accept that the cover letter needs to be rewritten for Comm Algebra. The "diagnostic-collapse" framing is well-suited to IJM but reads as defensive in Comm Algebra.

### MINOR issues

1. §1.3 "Family-Structure context" and §5.3 lean on internal references (`Atlas/META_PLAN_2026-05-06`, `FoundationsModule`, `SFM_Q6`) that a Comm Algebra referee cannot follow. Strip to load-bearing facts or move to companion paper.
2. (B5) appeals to [SandersGishFourCore, J01] for the 8-shell chain — fine for IJM, awkward for Comm Algebra. Re-prove the size-4 closure of {0,7,8,9} inline (one line).
3. Remark 6.1 (SO(10) GUT) is unnecessary in Comm Algebra; cut.
4. Diagnostic-5 wording ("greedy-Cartan returns smaller rank... is expected") reads apologetic; replace with one sentence: "The standard J_1,…,J_5 of §4.5 generate a 5-dim abelian subalgebra in g, so rk(g) ≥ 5; by g = so(V) ≅ so(10) the equality holds."
5. Citation style: [SandersGishSO8, J29] etc. — convert J-numbers to journal-style refs before submission. Drápal-Wanless 2021 IS cited (§1.1, references list).

### EDITORIAL

- Title length 70+ chars; Comm Algebra prefers short.
- "Substrate ceiling" terminology is internal jargon — gloss once or replace with "dim so(V) = 45."
- Eight open questions in §8 is a lot for a 10–20 page Comm Algebra paper; cut to two or three.

### Journal-fit (Comm Algebra specific)

Comm Algebra accepts focused dim-saturation results, but the *title* must match the proven content. Either retitle to remove "so(10) identification" (since the result is dim-saturation + classification), or re-route to *Linear Algebra and its Applications* (better fit for the matrix-Lie-closure-to-skew-symmetric-algebra framing), *Israel J Math* (as the cover letter already targets), or *Algebras and Representation Theory*.

---

## J10 — Operadic D₄ Orbits on the Non-Associative Locus

**Verdict:** **Minor revision.** Clean combinatorial-on-a-finite-group-action result with crisp theorems (A–D), explicit obstruction count (16/67), and a self-contained verifier under 1 second. Mathematically honest. Comm Algebra fits as the cover letter's first-choice fallback.

**Verification cross-check:** `verify_J32_d4_orbits.py` is exemplary — pure stdlib, deterministic, checks all six claims (|N|=126, |D_4|=8 with order spectrum {1,2,2,2,2,2,4,4}, 67 orbits with (44,7,4,10,2) distribution, 16 incoherent, 98 P_56-orbits 70+28 all coherent, 4-core arity-3 closure 64/0/8). Order-2 correction noted in Remark 2.7 (previously mis-stated as order 12) is documented honestly.

### MAJOR issues

1. **"Operad" in the title is overpromising.** The paper does not define an operad in the Loday–Vallette sense, does not exhibit a free-magma operad structure, and the "arity-3" content is just the two bracketings (T(T(a,b),c), T(a,T(b,c))) of a binary operation. A genuine operadic framing would include the symmetric-group action, the composition maps γ, and a Koszul-dual or quadratic-relations discussion. Recommend retitling as *"Dihedral D₄ orbits on the non-associative locus..."* — the result is honest as a combinatorial-on-a-group-action theorem.
2. **Theorem B's proof has a logical gap.** The strengthening from "{L,R}-valued Φ" to "{a,b,c,L,R}-valued Φ" is asserted at the end of the proof but the case analysis is hand-waved ("at every incoherent orbit there is a generator g ∈ {σ³, σ³P₅₆, P₅₆σ³P₅₆} for which g(7)=4..."). For Comm Algebra, this needs the full 16-orbit table verifying the extended-value-set obstruction, or a structural lemma. As written, the conclusion for {a,b,c,L,R}-valued Φ is conjectural.

### MINOR issues

1. D₄-vs-D₈ convention is acknowledged in Prop 2.6 — good. Stick with the order-8 convention throughout.
2. The phrase "spinorial outer automorphism of so(10)" (§6) is a structural-rhyme claim and should be tagged as such; verifying it requires the Wedderburn analysis of J11, which is not in this paper.
3. References to companion papers J45, J11, J12 are appropriate. Drápal-Wanless 2021 cited (§0, §8). Loday-Vallette 2012 cited but unused in proof.
4. Section §6 ("Structural interpretation") is interpretive rather than theorem-proof; in Comm Algebra this can be ¼ page max. Tighten.
5. Appendix B referenced ("64 triples listed in full") but not present in the manuscript. Either include or drop the reference.

### EDITORIAL

- Reduce companion-paper citations in §1 — the "structurally distinct from J01/J12/J11" paragraph reads as defensive boilerplate. One sentence suffices.
- Inline the table from Lemma 2.4 (bracketing-pair multiplicities) — already done.
- Acknowledgments section currently reveals internal WP-numbering (WP109, WP112). Reword.

### Journal-fit (Comm Algebra specific)

Strong fit *if retitled*. The result is a clean structural-combinatorial theorem with a sharp obstruction count and a complete verifier. Length is good (manuscript reads to ~12 pages). The "operadic" framing should be downgraded — Comm Algebra readers will judge the result on its combinatorial merit, which is solid.

---

## J12 — Galois D₄ over LMFDB 4.2.10224.1

**Verdict:** **Accept (with minor polish).** This is the strongest of the four, and the natural Comm Algebra submission. Self-contained, six independent sympy checks, exact discriminant identifications, explicit Tschirnhaus reduction to LMFDB's canonical defining polynomial.

**Verification cross-check:** Discriminants verified by hand: |Δ_f| = 40896 = 2^6·3^2·71 ✓; |d_K| = 10224 = 2^4·3^2·71 ✓; index² = 40896/10224 = 4 ✓. The script `verify_J15_galois.py` runs six sympy checks: irreducibility (case + mod 7, with mod 5 noted as the reducible counterexample — good methodological transparency), discriminant, resolvent cubic g(y) = (y+2)(y² − y + 18), Galois D₄ via sympy.factor(f, extension=[sqrt(-71)]), Q(√3) explicit factorization, LMFDB cross-check via Tschirnhaus x → −x − 1 to the canonical h(x) = x⁴ − 7x² − 12x − 8. All passes are believable from the script structure.

**LMFDB identifier 4.2.10224.1:** The four-part LMFDB convention is (degree).(real_embeddings).(|d_K|).(class_index). For degree 4, signature (2,1) gives 2 real embeddings, |d_K|=10224, class index 1. This matches the manuscript's claim. Confirmed catalogued.

### MAJOR issues

None substantive.

### MINOR issues

1. **The "novelty" claim should be tightened.** The Remark in §5 ("Novelty of the route, not the field") is correctly framed, but the language "we have not located it as a defining polynomial in a published context tied to a finite-magma fuse iteration" is hedged. Strengthen to: "We are not aware of f(x) = x⁴ + 4x³ − x² + 2x − 2 appearing in the literature as the defining polynomial of LMFDB 4.2.10224.1; standard databases (LMFDB, OEIS coefficient sequence search) return no prior occurrence."
2. The Galois group identification uses sympy.factor with sqrt(-71) extension to distinguish C_4 from D_4. PARI/GP polgalois(f) is mentioned as cross-check — actually run it and report the output in the verification log, or drop the mention.
3. Class number h_L = 14 for the degree-8 Galois closure is stated without verification — this comes from LMFDB; cite the LMFDB record explicitly here. (The reference is in the bibliography but the in-text claim h_L = 14 should be annotated as LMFDB data.)
4. The "structural rhyme" Q(√3) ⊕ Q(√−71) language in the tier-discipline section is fine; the explicit Q(√3) factorization in Theorem 1.1 is a genuine proof element, properly displayed.
5. References: Drápal-Wanless 2021 cited (§Acknowledgments). Cohen 1993 cited for the quartic-Galois classification.

### EDITORIAL

- The dependence on companion paper SandersGishFourCore [J15] for the structural input (the fuse iteration, the 4-core, the h/β = 1+√3 closed form) is unavoidable; the manuscript handles this cleanly by recalling the necessary data in §2 (Setup) and proceeding self-contained from there. Good.
- Title "Galois D_4 over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor" is appropriately precise.
- Length looks about right for Comm Algebra (~12 pages).
- The §6 verification description (six bullet items) duplicates the script's docstring; one can be cut.

### Journal-fit (Comm Algebra specific)

Textbook Comm Algebra fit: clean Galois identification, explicit number-field reference, full proof of irreducibility (not just sympy assertion), resolvent-cubic computation, Tschirnhaus cross-check, exact-arithmetic verification. The MSC 11R32 / 11R20 classification is appropriate. Recommend accept-as-is or with the minor tightening above.

---

## J18 — F_p Extensions of CL_BHML: Universality Across Six Prime Fields

**Verdict:** **Minor revision.** Honest paper after the 2026-05-07 fresh-eyes correction (which converted "per-prime verification of universality" to "generic structural skeleton" and corrected the false rank-preservation claim at p ∈ {3, 13}). The remaining issues are framing and the binomial-coincidence claim.

**Verification cross-check:** `bhml_fp_universality.py` (referenced) and `bhml_chain_shells.py` (referenced) — I read the universality script. It computes idempotent counts {2, 6, 8, 10, 14, 16} for p ∈ {2,3,5,7,11,13}, eigenspace dimensions of L_e2 and L_e0, power-associativity, and associator image dimension. The chain-shells script is referenced for the determinant-factorization profile.

### MAJOR issues

1. **The title is misleading after the correction.** The title still says "Universality Across Six Prime Fields" but the abstract honestly admits universality is *structural-skeleton invariance* (eigenspace signatures, power-associativity, 1-dim associator image), NOT a stronger claim about the algebra being the "same" across F_p. Retitle to *"F_p reductions of the BHML 4-core algebra: characteristic-independent structural invariants and a rank-preservation profile"* or similar. The current title will draw a reviewer expecting strong universality (Morita-equivalence, isomorphism classes, etc.).
2. **Which six primes, and why those?** The abstract chooses {2, 3, 5, 7, 11, 13} but the §1 Methodological Correction notes that p ∈ {2, 5} are excluded due to Z/10Z = 2·5 residue characteristic collisions. So Theorem 3.1 is stated as holding "for every prime p" but the chain-shell profile (Prop. 3.2) gives failures at p ∈ {2, 3, 5, 13}. The honest scope is: Theorem 3.1 holds for *all* primes (the structural skeleton is characteristic-independent because it follows from integer-level facts), but the chain-shell profile fails outside p ∈ {7, 11}. State this distinction prominently in §1: "structural skeleton: universal; chain-shell rank: only universal at p ∈ {7, 11}."
3. **The binomial-coincidence claim (det BHML_8° = 70 = C(8,4)) is honestly tagged "small-integer coincidence pending further investigation" — good.** But the whole §4 reads as a side-quest unrelated to the universality theorem. For a 10–20 page Comm Algebra paper, recommend either dropping §4 or moving it to an appendix.

### MINOR issues

1. The "previously circulated draft" / "fresh-eyes correction" disclosure (§1, Remark 3.3) is unusual for a journal manuscript. Convert to a single footnote, or remove the meta-narrative entirely. The corrected statement should stand on its own.
2. Theorem 3.1 proof is by polynomial-identity verification (power-associativity), integer diagonalization (L_e2), and rank-1 associator image. Each step is invoked as "the script verifies" — for Comm Algebra, give the matrix L_e2 explicitly (done) and write the rank-1 generator (e_4 − e_3, per Lemma 5.2) directly in the proof of Theorem 3.1. Don't punt to a script reference.
3. References: Drápal-Wanless 2021 is in the bibliography (item 1). Schafer 1966, Albert 1942, Wedderburn 1907 cited — appropriate.
4. The §0 "Scope and tier discipline" PROVEN/COMPUTED/RHYME/OPEN structure is internal corpus convention; for Comm Algebra, reformat as a standard "Main results" subsection.
5. §6 "Power-associativity, associator image, and conjectures" — there are no conjectures in §6 as listed (only restatements of Lemmas 5.1 and 5.2). Rename to "Power-associativity and associator image" or add the conjectures stated in the abstract.

### EDITORIAL

- The "YM subscript renamed to ° " explanation in §4 reads as internal-history. Either drop the YM mention entirely, or footnote.
- The reference to "TIG synthesis 2026" with a Zenodo DOI is unusual for a focused algebra paper — keep if it carries the code, drop if redundant.
- BHML notation: write out the multiplication table T^BHML once (Definition 2.1 does — good) and never call it "the BHML table" without referent.

### Journal-fit (Comm Algebra specific)

After retitle and §4 demotion, this is a fine Comm Algebra paper: a focused structural theorem about characteristic-independent invariants of a small commutative non-associative algebra, with explicit computational data for six primes and an honest rank-preservation profile. The methodology-correction transparency is admirable but should be muted in the final manuscript. MSC 17A30 / 11T55 is appropriate.

---

## Cross-paper summary

| Paper | Verdict | Comm Algebra fit | Drápal-Wanless cited? | Verification |
|---|---|---|---|---|
| J09 | Major revision / consider re-routing | Weak (title overpromises canonicality) | Yes | scripts honest, sampled-test demoted properly |
| J10 | Minor revision (retitle, fix Thm B gap) | Strong with retitle | Yes | exemplary self-contained verifier |
| J12 | Accept (minor polish) | Textbook fit | Yes | exact arithmetic, six independent sympy checks, LMFDB cross-check |
| J18 | Minor revision (retitle, §4 demotion) | Strong after retitle | Yes | scripts run; correction history needs muting |

**Bundle recommendation:** J12 is the strongest Comm Algebra submission (Accept). J10 and J18 are strong with minor revision (retitle + small gaps). J09 needs to be either retitled honestly or re-routed to IJM / LAA / Algebras and Representation Theory; the "so(10) identification" framing won't survive a Comm Algebra Lie-algebra referee.

The four papers together show a coherent program (Z/10Z magma substrate → Lie/Galois/operad/F_p reductions); each is technically honest once the title overpromise (J09, J10, J18) is corrected. The verification infrastructure is excellent across all four.
