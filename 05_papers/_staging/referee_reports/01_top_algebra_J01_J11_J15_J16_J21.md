# Referee report — top algebra targets (J01, J11, J15, J16, J21)

**Date:** 2026-05-27
**Reviewer brief:** Trained referee for *Journal of Algebra* and *Algebraic Combinatorics*.
**Scope:** line-by-line read of five Tier-1 manuscripts after the 0d6d0f1 renumbering.
**Sources read:** each `manuscript/manuscript.{md,tex}`, the bundled verification script(s), and each `README.md`.

---

## J01 — Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z

**Verdict:** Minor revision — the mathematics is sound and the demotion of F is largely consistent, but two presentation defects (mismatched "five vs six structural facts" count, stale README) and one substantive overclaim in Lemma 2.1 should be fixed before submission.

**Verification cross-check:** Yes — `manuscript/verification/4core_verification.py` has six checks mapped 1-to-1 with manuscript Theorems A–E plus Proposition F (see script header lines 9–18 and §11 of the manuscript). The script header at line 17 reads "alpha-sweep PSLQ (Theorem F partial uniqueness)" — the script still says **Theorem F**, even though the manuscript body has demoted it to Proposition F. This is a one-word inconsistency to fix in the script docstring.

### MAJOR issues

1. **[§0 line 50 vs §8 line 345] Internal "five vs six" count contradiction.** The abstract (line 14) and §0 (line 50) both say "six independent structural facts converge on C". §8 (line 345) says "five independent structural facts together establish C as the algebraic center" — the count was clearly demoted to 5 once F became a Proposition, but the abstract and §0 still say 6. Pick one. The natural choice is five Tier-A theorems (A–E) since Proposition F is finite-test only and not on the same footing.

2. **[§2 Lemma 2.1 / §2.2 proof, lines 142–151] "By direct enumeration" without showing the structural reason for size-2.** The proof writes 'For size-2 closure {i,j}, both B(i,i) and B(j,j) must lie in {i,j}, ruling out all but a few candidate pairs; direct check on the remaining candidates confirms none is also T-closed.' The candidates surviving the B-diagonal test should be displayed — this is what J. Algebra referees scrutinize. The companion paper J15 §3 Theorem 3.1 does this enumeration carefully (lines 502–551); J01 should either cite J15 explicitly here or import the few lines. As written, the "direct check" is opaque.

3. **[§5.1 proof, line 256] Gröbner basis step "we have also independently verified the Gröbner reduction in PARI/GP at lex order, with the identical second-elimination polynomial" — no log, no run-script.** For J. Algebra, the *exact* claim "Gröbner basis reduces the four-equation polynomial system to h² − 2h·br − 2br² = 0" should be backed by either: a PARI/GP script in `verification/` reproducing the reduction, or a hand proof. As it stands the proof relies on sympy's `solve`, which is not standard for J. Algebra referees.

### MINOR issues

1. **[§0.3 line 56 "STRUCTURAL RHYME"]** "The same field appears across multiple substrate invariants in the parent framework's catalogue (Volume D, Section 78)." The reference is to internal documentation that referees cannot access. Either rewrite without the citation, or cite a published artifact.

2. **[§5.3 lines 285–296] Closed-form coordinates.** The four ugly closed-forms are correct as displayed, but the contrast "complexity of the individual coordinates vs simplicity of the ratio" would be sharper if the splitting field is *named* (it is named in §5.2 line 280 but not at the point of display).

3. **[§9.3 line 365] Replicator-dynamics comparison.** The analogy is fair but the cited Hofbauer-Sigmund text is 1998. A more recent comparison (Sigmund 2010, or any 2010s replicator-on-finite-set paper) would strengthen the positioning.

4. **README §1 line 27 still calls F a "Theorem".** Update to "Proposition F". Also README line 19 says "Six theorems (renumbered to match `4core_verification.py`)" — adjust to "Five theorems + one proposition".

### EDITORIAL

1. The Galois proof in §5.2 is clean; lead with it more aggressively in the abstract.
2. The 4-core-as-U(1) framing in §0 is heavy on internal pseudonyms (TSML/BHML/CL_STD, "operator names VOID/LATTICE/..."). For J. Algebra, strip those down to "tables T, B, S" everywhere except a single naming remark.
3. Drápal–Wanless 2021 is cited as "closest published precedent" three times; one citation suffices.

### Journal-fit

Excellent fit for *Journal of Algebra*. The Galois D_4 quartic identification (Theorem D) and the polynomial-reduction normalizer identity (Theorem C) are exactly the kind of self-contained structural result the venue wants. Length (≈460 lines markdown, ≈25 pages typeset) is appropriate. The PSLQ Proposition F should remain demoted; J. Algebra referees will reject any "uniqueness" claim from PSLQ alone, and the current framing acknowledges this. Recommendation: **Minor revision then submit.**

---

## J11 — Decomposition of the Lens-Pair Commutator [TSML, BHML] under D_4 on Z/10Z

**Verdict:** Major revision — the central Wedderburn theorem (Theorem 2.1) is solid and the integer/rational shares are verifiable, but the §3.2 Killing-classification proof has a non-obvious step that needs more detail, the title is unreasonably long (a known referee red flag), and the manuscript repeatedly slides between "theorem" content and "structural rhyme" GUT labelling.

**Verification cross-check:** Three scripts in `manuscript/verification/`: `verify_d4_decomposition.py` (Theorem 2.1, Wedderburn isotypic decomposition); `find_higgs_irrep.py` (Theorem 4.1 rough); `find_higgs_direction.py` (Theorem 4.1 sharp). The first script header (lines 1–20) matches the manuscript's stated shares exactly: triv 3,075,027/2, sign1 9/2, sign2 288,164, sign3 0, std 19,608, total 1,845,290. Wedderburn orthogonality check is built in. **Verification matches manuscript.**

### MAJOR issues

1. **[Title, line 1]** "Wedderburn D₄-Isotypic Decomposition of the Lens-Pair Commutator [TSML,BHML] on Z/10Z: an Exact-Rational Identification of a Doubly-Invariant su(4)⊕u(1) Subalgebra of so(10) and a 9-Vector inside the 54 with ‖v‖²=13/4." This is 41 words. *J. Algebra* convention is ≤15. The README/cover-letter title at J11/README.md "Decomposition of the Lens-Pair Commutator [TSML, BHML] under D₄ on Z/10Z" is fine; cut the manuscript title to match.

2. **[§3.2 Theorem 3.2 proof, lines 200–208] "By Cartan's criterion the 1-dimensional 0-eigenspace is the center of g₀ and the 15-dimensional (−4)-eigenspace is the simple part. The unique compact simple Lie algebra of dimension 15 is so(6) ≅ su(4) ≅ A₃."** This step needs more detail. Cartan's criterion gives the semisimple-vs-abelian split, but the *identification* of the 15-dim simple part as A₃ (rather than some non-compact form, or a different 15-dim simple algebra over ℝ) requires either: (a) verifying that the 15-dim part embeds in the compact so(10), forcing the compact real form; or (b) a direct root-system computation. The compact-form argument is implicit ("compact simple Lie algebra of dimension 15") but should be stated. Also: dimension-15 compact simple is unique (A₃ ≅ D₃) — fine — but C₂ = sp(2) has dimension 10 not 15, B₂ has dim 10, G₂ has dim 14, so the statement is correct; just spell out the elimination.

3. **[§3.1 line 196] "verified numerically at residual ≤ 10⁻¹⁴"** — for J. Algebra the closure of g₀ under Lie bracket must be a symbolic check on the 16 basis elements, not numerical. The proof says "the centralizer of any subgroup of Aut(g) is a Lie subalgebra, then verified numerically" — that prose is confused: the centralizer-is-subalgebra argument is the *proof*; numerics is redundant. Cut the numerical residual and stand on the centralizer argument.

4. **[§5.1 Proposition 5.1, lines 257–263]** "The character χ_sign₃ is +1 on C₁∪C₂∪C₅ and −1 on C₃∪C₄. The eight terms of the projection sum split into two halves of four terms each, summing to zero." This proof says it splits and sums to zero "by direct verification by verify_d4_decomposition.py" — but the *structural reason* that the +-half and −-half exactly cancel is the load-bearing content. As written it's a computer-verified identity, not a theorem. The paper claims this is "a bilinear identity that does not hold for generic 10×10 integer table pairs" (line 261) — so the cancellation is special to (T,B), but no algebraic mechanism is given. J. Algebra referees will demand either (i) an algebraic identity in the entries of T,B that makes the cancellation visible, or (ii) explicit downgrade of Proposition 5.1 to "verified empirically for this pair".

### MINOR issues

1. **[§0.3 lines 31–37] Correction-notice paragraph reads as defensive.** The retraction of "two roads to Pati-Salam" is appropriate, but should be one sentence in the introduction, not a half-page §0.3. The decomposition stands on its own.

2. **[§4.2 Theorem 4.1 statement, lines 222–231]** The displayed 9-vector v is given case-by-case with one case ("-1/2 on the symmetric pair (B+S)/√2") that mixes coefficient form (-1/2) with basis-vector notation ((B+S)/√2). Restate as a single linear combination in a fixed basis of the **9** so referees can check the squared norm by inspection.

3. **[§4.2 proof, line 235]** "The integer 13 in ‖v‖² = 13/4 has a parallel direct enumeration: there are exactly 26 cells (i,j) where BHML[i,j] ≠ BHML[P₅₆(i), P₅₆(j)] ... ‖v‖² = 26/8 = 13/4. The 8 in the denominator is the standard normalization of the 9-vector projection within the 54." This is *structural rhyme*, not proof — restate as a Remark.

4. **[§7.2 Conjecture 7.2]** The family-wide invariance of sign₁ ≈ sign₃ ≈ 0 is interesting but only stated, never tested. The Q7 follow-up paper is referenced but not in the J-series; mention an empirical test on at least one other pair (T', B') in the same paper as evidence.

5. **[§9 Appendix]** The three appendix observations (non-associativity rate 0.126, Lie/Jordan duality, three involutions) are all interesting but read as offcuts. Either fold the τ₁/τ₂/τ₃ involution table into §3 (it cleanly shows g₀ is the intersection of τ₂- and τ₃-fixed parts), or remove.

### EDITORIAL

1. The "(TSML_SYM throughout this paper; the literal-bit-pattern variant TSML_RAW is used for prime-11 wobble-localization in companion work, not here)" parenthetical in §0.1 line 16 is symptomatic — the paper repeatedly opens parentheses to companion-paper internals. Trim aggressively for J. Algebra.

2. The single-emoji "🙏" at line 410 should be removed.

3. References §10 — Slansky 1981 (cited as structural rhyme) is the only physics reference; either commit to the GUT framing or remove (the algebra stands without it).

### Journal-fit

Strong fit for *Journal of Algebra* on the algebra alone: Wedderburn decomposition of a specific lens-pair commutator under a specific dihedral action, with exact rational shares and a clean structural-zero theorem. The paper would be stronger if it cut the GUT-style "structural rhyme" framing by 70%. With the title shortened, §3.2 proof tightened, and §5.1 either upgraded or downgraded honestly, this is a solid J. Algebra paper. **Major revision then resubmit.**

---

## J15 — Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z

**Verdict:** Accept with minor revision — the strongest of the five papers. Self-contained, rigorous, clearly written, with explicit proofs of the chain enumeration and the Galois identification. One redundant remark on the normalizer identity, a small Theorem 6 sketch in the dynamics section, and one citation cleanup are needed.

**Verification cross-check:** Four scripts (`4core_verification.py`, `04_bridge_attractor.py`, `06_attractor_closed_form.py`, `07_full_closed_form.py`, `alpha_pslq_sweep.py`) listed in §10 line 1346 onwards. Each maps to a specific theorem (Thm 3.1 ↔ `4core_verification.py`; Thm 7.1 ↔ `06_attractor_closed_form.py`; Thm 8.1 ↔ `07_full_closed_form.py`; Conj 9.1 ↔ `alpha_pslq_sweep.py`). I verified the script files exist (`manuscript/verification/`). **Matches manuscript claims.**

### MAJOR issues

1. **[§6 Theorem 6.2 (Interior existence), lines 963–978]** "By Lemma 4.1, no boundary fixed point exists for α∈(0,1) except e₀, which is a repellor; standard topological arguments (e.g., Lefschetz fixed-point theory or the index calculation for a repellor on the boundary of a contractible set) then place at least one fixed point in the interior." This is a sketch, not a proof. The Brouwer argument gives a fixed point *somewhere*; the boundary-only-repellor argument needs to give a Lefschetz/index calculation explicitly. For *Algebraic Combinatorics* this is borderline acceptable since the existence is independently confirmed by Thm 6.3 at α=1/2 (the load-bearing case); but the wording "standard topological arguments" should be replaced by either (i) the explicit Lefschetz computation, or (ii) "By Brouwer's theorem at least one fixed point exists in the closed simplex; by Lemma 4.1 it lies in the interior since e₀ is the unique boundary fixed point and is a repellor." (The repellor-vs-attractor index argument is then a 3-line afterthought.)

### MINOR issues

1. **[§2 Remark 2.6 line 434–447] Total-mass identity Z_T = Z_B = (Σpᵢ)².** This is honestly disclosed as following from bilinearity, *not* from joint closure (lines 437–442). Good. But Remark 2.6 is then largely redundant with §5 Remark 5.4 "the total-mass identity Z_T(p) = Z_B(p) is not the substantive structural observation". Pick one location.

2. **[§3 Theorem 3.1 proof, "Sizes 4–9 uniqueness within size class" line 553–600]** "Direct enumeration over the (10 choose k) candidates at each size (totalling 210+252+210+120+45+10=847 subsets across sizes 4–9, plus (10 choose 10) =1 at size 10) confirms that each non-listed candidate fails T- or B-closure on at least one cell, completing the uniqueness verification." This is OK but inefficient — most sizes have a structural reduction (e.g., {0,7,8,9}⊆S forces shells). Consider folding in: "*the structural reduction C₄⊆S* (just proved) eliminates all candidates that don't contain {0,7,8,9}, leaving exactly (6 choose k−4) candidates at each size k≥4, totalling 15+20+15+6+1+0=57 candidates to check at sizes 4–9 plus size 10. Inspection of these 58 candidates" — much cleaner.

3. **[§9 Conjecture 9.1]** The PSLQ Stern-Brocot scan over 57 rationals at q≤13 is honestly bounded. Good. But the "degree ≤ 8, coefficient ≤ 50" specifications should appear in the conjecture *statement* (line 1308), not just in the result section.

4. **[Remark 2.5 / Definition 2.4]** The lens-choice paragraph (T = upper-triangle symmetrization vs. T_raw bit-pattern) is a real subtle point. The current placement at Remark 2.5 (line 360–388) is good. Note: the chain length differs (8 vs 7); this is a real sensitivity. The remark currently says the closed-form attractor and Galois quartic do not depend on the symmetrization choice. **Confirm this in the verification script** (a 5-line check on T_raw would settle it definitively).

5. **[§7 Remark 7.2 "Numerical check", line 1075]** "h^*/β^* = 2.732050807568878 and 1+√3 = 2.732050807568877 (residual 4.4×10⁻¹⁶)." That residual is double-precision unit-rounding; presenting it as a "check" reads as overkill given Thm 7.1 is a symbolic identity. Either upgrade to mpmath 50-digit, or simply note "verified symbolically by `06_attractor_closed_form.py` (sympy)."

### EDITORIAL

1. The π-permutation in Remark 3.2 (renamed from σ to avoid name collision with the non-associativity rate function in the companion paper) is good practice. Confirm consistency: the script `4core_verification.py` should use the same notation if it uses one.

2. References [SandersClaudeChat2026BridgeSprint] (line 1522) cites "Sanders et al." — `et al.` suggests other authors. Confirm the author list and remove if it's still Sanders+Gish.

3. Reference [SandersGishFourCore] is cited as J01 but the bibitem (line 784 in J16, also referenced here) doesn't have a venue or arXiv id. Add one.

### Journal-fit

Excellent fit for *Algebraic Combinatorics*. Mixes finite-magma enumeration, simplex dynamics, and number-theoretic identification of the Galois closure as a catalogued LMFDB field. Length (≈1550 lines LaTeX, ≈35 pages typeset) is on the long side for *AlgComb* but defensible given the multiple independent results. Honesty about scope (§11 lines 1394–1444) is exemplary. **Accept with minor revisions.**

---

## J16 — The CL Forcing Axioms: S₁–S₇ Force the Canonical Composition Lattice

**Verdict:** Major revision — the structural-axiom rewrite is conceptually right, but (i) the README title still says "A1-A9" while the manuscript title and body say "S_1-S_7" (this is the precise inconsistency the task flagged), (ii) the §5 independence proofs read as sketches that explicitly acknowledge they can't construct strict witnesses for 5 of the 7 axioms, and (iii) the `cl_independence.py` script referenced in the manuscript is missing from `manuscript/`.

**Verification cross-check:** The manuscript references **`cl_independence.py`** at §4 line 526, §4 line 600, and §7 line 718. The actual script in `manuscript/` is **`cl_forcing.py`** only. There is no `cl_independence.py` in `manuscript/` or in `manuscript/verification/`. The §7 reproducibility paragraph (lines 716–731) says "the reference Python script `cl_forcing.py`" but then says "for each i ... constructs the witness magma M_i explicitly and verifies that M_i satisfies {S_j : j ≠ i} but fails S_i" — *this is the work the manuscript repeatedly punts to `cl_independence.py`*. Either consolidate `cl_forcing.py` to do both jobs, or ship `cl_independence.py`. As filed, the independence verification cannot be reproduced.

### MAJOR issues

1. **[README §1 line 1] Title mismatch:** README reads "J16 — The CL Forcing Axioms: A1-A9 Uniquely Force the Canonical Composition Lattice". Manuscript title (line 39–41) reads "Structural Axioms, Independence, and a 73-HARMONY Forcing Theorem". Abstract (line 61) says "seven structural axioms S₁–S₇". Fix the README title to match the rewritten content; the README abstract paragraph at line 16 still says "nine axioms A1-A9" — that paragraph is the original (pre-rewrite) abstract that was never updated. Update the README throughout.

2. **[§5 independence proofs, lines 480–658]** The proof of Theorem 5.1 explicitly admits that only M₂ and M₇ are "strict independence witnesses" (failing only the targeted axiom) and that M₁, M₃, M₄, M₅, M₆ "fail S_i together with one or two additional axioms due to the tight combinatorial interaction" (lines 663–668). This is **logical independence in a weakened sense, not the standard meaning.** Standard logical independence requires that S_i is not derivable from S_j (j≠i); the standard witness construction shows a model satisfying all S_j (j≠i) but violating S_i. The paper *cannot construct such a witness for 5 of 7 axioms* and openly says so. This either (i) needs the standard definition restated honestly: "no single S_i is a logical consequence of the conjunction of the other six, where independence is exhibited by the partial witnesses M_i below" — and the section title needs to drop the unqualified "Independence"; or (ii) the partial witnesses need to be replaced by strict ones, perhaps by relaxing S_5/S_6/S_2 in pairs (e.g., constructing M_3 that breaks only S_3 by violating the absorption at H but keeping all cell counts via a more elaborate substitution). The current text is the kind of thing that will land in a referee report verbatim.

3. **[§4 forcing proof, "Step 4" lines 418–432]** "Of the remaining 56 cells, S₆ identifies exactly 10 as exceptional ... the remaining 56 − 10 = 46 cells must be either HARMONY or VOID by exclusion (S₆ asserts that the exceptional cells are exactly those in E, so all other off-special cells are non-exceptional, i.e., have value in {0, 7}). Since no other VOID structure has been imposed (rows ≠ 0, columns ≠ 0 are not VOID-forcing by S₂), all 46 remaining cells must equal 7." The last step is **not justified by the axioms as stated**: nothing in S₁–S₇ says that non-exceptional off-special cells must be 7 rather than 0. The argument is implicitly using "the count S₅ = 73:17:10 has already accounted for 17 VOIDs (Step 1), so the remaining cells can't be VOID without exceeding the count" — but that's a count-elimination argument that should be explicit. Rewrite Step 4 to say: "By S₅ the total VOID count is exactly 17, already satisfied by Step 1; therefore the remaining 46 cells cannot be VOID. Since they are not exceptional (S₆) and not VOID (S₅), they must be HARMONY = 7."

### MINOR issues

1. **[§3 axiom statements, lines 297–338]** S₆ says "the set of exceptional positions is exactly E = {{1,2}, {2,4}, {2,9}, {3,9}, {4,8}}" and S₇ then names values. This makes S₆ + S₇ a **direct cell listing** in slight disguise: 10 cells are spelled out. The paper explicitly acknowledges this in §3 Remark 3.3 — "S₆ enumerates a 5-element set of positions; S₇ enumerates the values on those positions. The two listings S₆ and S₇ are minimal." Acceptable, but the abstract's framing "structural axioms rather than cell-listings" oversells the position-listing. Either tighten the framing or acknowledge S₆+S₇ as a "minimal cell-listing" honestly in the abstract.

2. **[§6 Conjecture 6.1]** Lens family enumeration is appropriately positioned as open. Good.

3. **[References §8 line 783] `SandersGishFourCore` citation:** "submitted to *Algebraic Combinatorics*, 2026." Is this J15 or a different paper? The Companion-J card in the cover letter should reconcile.

### EDITORIAL

1. Remove the README's outdated abstract (line 16 "We isolate nine axioms A1-A9..." — completely wrong after rewrite).

2. Title can be tightened: "The CL_TSML Composition Lattice on Z/10Z: Structural Axioms and Independence" loses nothing.

3. The cover letter (per task description) should not lean on the A1-A9 framing either; check.

### Journal-fit

*Algebraic Combinatorics* is acceptable; the result is a small-magma axiomatization with explicit independence statement. The work is honest about S₆/S₇ being position-and-value listings. With the major revisions above (especially the missing verification script, the README title, and the weakened-independence framing), the paper would be in shape. Without those it will be desk-rejected. **Major revision.**

---

## J21 — Two Crossing Decompositions of a −21 Invariant on Z/10Z with the σ²-Triadic Refinement

**Verdict:** Major revision — the core integer-arithmetic content is correct and easily verifiable (all six checks in `verify_J18.py` pass), but a **systematic terminological error** runs through the entire paper: σ is repeatedly called a "canonical involution" when its cycle structure (line 117 verbatim) shows it has order 6, not 2. This must be fixed before submission. Additional issues with the table-specific Fibonacci result and the structural significance argument.

**Verification cross-check:** `verify_J18.py` in `manuscript/`. Six checks (C1–C6) map 1-to-1 to the manuscript's load-bearing claims (script header lines 7–27). Stated values: Ψ_B table sums to −21 (C1); σ-orbit triangular −15/−6 (C2); role-Fibonacci −13/−8/−1/+1 (C3); σ²-orbit per-orbit −8/−7 (C4); crossing closure failure (C5); σ-orbit data (C6). The script docstring at line 24–26 itself contains a misstatement: "C6 sigma involution data: sigma is an involution on the cycle component in the order-2 sense (sigma^2 has order 3 on the 6-cycle, identity on fixed points)." σ has order 6 on the 6-cycle (it's a 6-cycle in cycle notation), not order 2. **Verification matches integer-arithmetic claims but inherits the involution misnomer.**

### MAJOR issues

1. **[Title, abstract, §0, §1, §2, keywords, verify script — pervasive]** σ is **not an involution**. The cycle structure σ = (0)(3)(8)(9)(1 7 6 5 4 2) is given verbatim at line 75–76: four fixed points and a 6-cycle. The order of σ on Z/10Z is lcm(1,1,1,1,6) = 6. The paper calls σ "the canonical involution" at lines 73 ("canonical involution σ"), 75 ("the canonical involution"), 117 ("canonical involution"), 173 ("specified involution σ"), 250 ("we fix the involution σ on Z/10Z given by the cycle structure"). The keywords (line 65) include "sigma involution". Both Theorem 3.2's name ("σ-orbit triangular decomposition") and the use of "σ-orbit" throughout (correct usage) are fine — σ does partition Z/10Z into orbits — but σ is **not** an involution. The natural fix: replace every "involution σ" with "permutation σ" (or "the canonical σ-permutation"). σ² (order 3 on the cycle) is also not an involution; only σ³ is an involution. This is the kind of error that gets flagged in the first paragraph of an AlgComb referee report.

2. **[§3 Theorem 3.1 / Proposition 4.1, lines 482–490] σ²-orbit per-orbit "TIG primes" framing.** Proposition 4.1 says the σ²-orbits O₁, O₂ contribute −8 and −7 respectively, "the negations of the canonical TIG primes {8, 7}." The integers 7 and 8 are *not* primes (8 = 2³). The phrase "canonical TIG primes" is parent-framework jargon that must be removed or defined precisely. If "prime" here means "primary indices in the operator alphabet" rename to operators-7-and-8 or the indices H and Br.

3. **[Definition 3.4 vs Theorems, lines 449–463]** The distinction "table-independent vs table-specific" is good in principle. But the empirical evidence cited for the table-specific Fibonacci result (Theorem 3.2 / Theorem thm:role-fib, lines 366–402) is "0/200 random commutative tables on Z/10Z in [SandersBridgeWP9, N8] reproduce the (13, 8) split" (Remark line 412). The 200-table sample size is too small to support the strong "table-specific" claim, and the citation is to an internal note. For *Algebraic Combinatorics* the table-specificity claim needs either (a) a larger random sample (10⁴+) shipped in the verification script, or (b) explicit demotion to "empirically not reproduced in a 200-table random sample."

### MINOR issues

1. **[§0 lines 152–161 STRUCTURAL RHYME tier]** Theorem 3.2's Fibonacci appearance is *table-specific*. Theorem 4.2 / Cor 4.3 "{−7, −8} TIG-prime split" is also table-specific. Both are honestly disclosed. But "structural rhyme" as a tier is a TIG-internal label; for AlgComb readability, replace with "empirical observation" or "table-dependent identity (Def 3.4)."

2. **[§2.3 Table 1, caption lines 273–283]** "These ten integer values are the input data of this paper. They originate as Ψ_B(n) = −(p(n) − 1) + δ_{n,0} + δ_{n,8} where p(n) is the per-element period under BHML in the substrate of [Sanders-Gish-FourCore]..." — this footnote-style origin story for the table values is fine but the formula isn't actually used in the paper. Either prove it (gives extra structural depth) or remove the formula (the table stands alone).

3. **[§1.2 line 199]** "We do not derive the Ψ_B values from a closed-form formula internal to this paper" — and §2.3 line 273 gives the formula. These two statements are mutually inconsistent. Clarify: the formula is *not* derived in this paper (it's input from a companion); the paper treats Ψ_B as data.

4. **[§4 Theorem 4.2 statement]** The "canonical σ²-triadic" framing should make explicit that "triadic" here refers to the 3-cycle structure of σ² on the 6-cycle (each σ²-orbit has 3 elements). The phrase is used 8+ times without definition.

5. **[Companion paper references]** `[SandersGishFourCore]` is J01 (clarified in earlier J16 review) but the bibitem doesn't say which J-number; readers can't track companion-versus-citation. Annotate each Sanders-Gish bibitem with its J-number.

### EDITORIAL

1. The title "Two Crossing Decompositions of a −21 Invariant on Z/10Z with the σ²-Triadic Refinement" is appropriately concise (compare J11). Keep.

2. §0 (Lens, substrate, claim tier) and §1 (Introduction) overlap substantially. Merge into a single introduction; AlgComb readers prefer a single entry point.

3. The Galois/representation-theoretic framing is explicitly disclaimed (§1.2 line 207). Good; don't reintroduce it later.

4. The phrase "canonical TIG primes {8, 7}" needs to go. Rewrite as "the indices 7 and 8" or "the canonical 4-core indices H, Br."

### Journal-fit

The core combinatorial content (two crossing decompositions of an integer-valued invariant on a small group, with a refinement using a sub-permutation) is appropriate for *Algebraic Combinatorics*. The integer arithmetic is verifiable by inspection. The paper is short and self-contained, which is a virtue. With the σ-as-involution misnomer fixed throughout, the "TIG primes" jargon excised, and the table-specific Fibonacci claim either properly tested or honestly downgraded, this is a publishable short paper for *AlgComb*. **Major revision (mainly terminological), then resubmit.**

---

## Summary of pressing issues across all five papers

1. **J21 — pervasive misuse of "involution" for an order-6 permutation σ** (Major). Title, abstract, introduction, §2.2, and the verify script all call σ an involution; σ has order 6 (one 6-cycle + four fixed points). The cleanest fix is replace "involution" with "permutation" throughout.

2. **J16 — title/README/manuscript inconsistency (A1-A9 vs S_1-S_7) plus a missing `cl_independence.py` script** the manuscript repeatedly relies on (Major). The §5 independence proofs also openly admit that only 2 of 7 witnesses are strict — the section title "Independence" should be qualified or the witnesses upgraded.

3. **J01 — "five vs six structural facts" count contradiction** between abstract/§0 (6) and §8 (5) following the Theorem→Proposition F demotion (Major presentation). README still calls F a "Theorem". The Lemma 2.1 "direct enumeration" elision for sizes 2/3 should import the J15 §3 proof.

4. **J11 — 41-word title, §3.2 Killing-classification missing the compact-form step, and §5.1 structural-zero proof is empirical-only** (Major). The "structural rhyme" GUT framing should be cut by 70% for J. Algebra.

5. **J15 — best of the five** but §6 Theorem 6.2 sketches "standard topological arguments" without an explicit index calculation (Minor); Conjecture 9.1 statement should include the (degree ≤ 8, |c| ≤ 50) bound; Remark 2.6 / Remark 5.4 duplicate the total-mass identity disclosure.

**Across-the-board:** "STRUCTURAL RHYME" tier, "TIG primes", "lens ownership paragraph", and internal companion-document citations are TIG-internal idioms that don't transport to J. Algebra / AlgComb referees. Strip systematically.
