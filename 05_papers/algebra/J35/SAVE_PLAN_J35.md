# SAVE PLAN — J35: Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z

**Date:** 2026-05-08 (rewritten with SFM Q6 finding incorporated; verified 6/6 PASS)
**Brayden directive 2026-05-08:** "perfect J35 and J54 incorporating SFM findings."
**Manuscript:** `manuscript/manuscript.md`
**Referee:** `Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J35_JAlgebra_FreshEyes.md` (Major revisions; close to "Accept with minor revisions")
**SFM source:** `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SFM_FINDINGS_v1.md` §2 (Q6 result: three-table chain identical)
**Family-structure framing:** `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md` §2 ("4-core is to TIG as the unit circle is to U(1)")
**Author lane:** Sanders + Gish.

---

## §1 — Why save? (J35 = corpus centerpiece)

The fresh-eyes referee for *J Algebra* called J35 **"the most defensible paper in the corpus."** Per FAMILY_STRUCTURE_v1.md §2: *"The 4-core is to TIG as the unit circle is to U(1)."* Per SFM Q6 (2026-05-08): the 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ is preserved across **ALL THREE tables (TSML, BHML, CL_STD)**, not just two — the joint TSML+BHML+CL_STD chain is the SAME 8-shell chain as TSML+BHML alone.

J35 is the structural anchor for the U(1)/center framing of the entire J-series. The 6/6 verification script PASSes at machine precision establish six independent structural facts converging on $\mathcal{C}$ as the algebraic center.

The save path was clear from the referee report alone (M1: renumber theorems; M3: lead with Galois; M4: reframe α-uniqueness as partial+conjecture; M5: add literature; M6: clean script metadata) — the SFM Q6 finding adds substance: a brand-new central theorem (Theorem B: 4-core 3-substrate closure under TSML, BHML, AND CL_STD).

---

## §2 — Specific fixes applied (mapped to referee + SFM findings)

**(a) Adopt the U(1) / centerpiece framing in the introduction (per FAMILY_STRUCTURE_v1.md §2).** Done in §0 of the rewritten manuscript: "The four-element set $\mathcal{C}$ plays the role of the algebraic *center* of this magma family. The relationship between $\mathcal{C}$ and the present pair $(T, B, S)$ is structurally analogous to the relationship between the unit circle $S^1$ and the group $U(1)$..."

**(b) NEW central theorem (incorporate SFM Q6 finding).** Added Theorem B (4-core 3-substrate closure) and Theorem 2.4 (three-substrate strengthening of the chain). The manuscript now states: *"The 4-core sub-magma $\{V, H, Br, R\} = \{0, 7, 8, 9\} \subset \mathbb{Z}/10\mathbb{Z}$ is jointly closed under all three canonical operations TSML, BHML, and CL_STD. It is the unique non-trivial 4-element subset preserved across all three tables."* Verification: extended `4core_verification.py` Check 1 to include the three-substrate chain enumeration; PASS.

**(c) Five independent structural facts converging on the 4-element set.** Added to §8 of the manuscript: (i) Joint closure 3-substrate (Theorem 2.4); (ii) Symbolic normalizer identity $Z_T = Z_B = (v+h+br+r)^2$ (D49, Theorem C); (iii) Closed-form attractor $h/\beta = 1+\sqrt{3}$ at $\alpha_M = 1/2$ via Galois $D_4$ over $\mathbb{Q}(\sqrt{3})$ (D78, Theorem D); (iv) Universal across $F_p$ ring extensions $p \in \{2,3,5,7,11,13\}$ (D74); (v) Support of universal T+B-mix attractor on chain shells (D65, Theorem E).

**(d) Renumber theorems to match script content (referee M1).** The script `4core_verification.py` runs six checks; the manuscript previously stated three theorems. The rewritten manuscript states six theorems (A through F) corresponding to the six script checks, plus Lemma 2.1 (forbidden small sizes) and Theorem 2.4 (three-substrate strengthening). Mapping is now 1-to-1.

**(e) Lead with $1+\sqrt{3}$ Galois punchline + LMFDB 4.2.10224.1 number-field identification (referee M3).** §5 now opens with Theorem 5.1 (the ratio identity) followed by §5.2 *"Lead with the Galois punchline"* — Theorem 5.2 stating $\mathrm{Gal}(K/\mathbb{Q}) = D_4$ over LMFDB 4.2.10224.1. The complex closed-form coordinates are then displayed in §5.3 as *presentation* in the splitting field, with the structural punchline that the ratio is fixed by the action of $\mathrm{Gal}(K/\mathbb{Q}(\sqrt{3}))$ of order 2.

**(f) Reframe α-uniqueness from "open" to "partial verification + open conjecture" (referee M4).** The original §6 said "remains open" without quantifying. The rewritten §7 states Theorem F (partial uniqueness on the finite test set $\{0, 1/4, 1/2, 3/4, 1\}$) and Conjecture 1.1 (full uniqueness across $\mathbb{Q} \cap (0, 1)$, with a five-step proof strategy outline). Empirical evidence is properly bounded; full symbolic proof is openly flagged as the next step.

**(g) Cite Drápal-Wanless 2021 (referee M5; per boilerplate §1.3).** Done in §0 (motivation) and §9.1 ("Closest published precedent"). Three additional adjacent references added: Bruck 1958, Smith 2007, Drápal-Kepka 1985 (all from referee's M5 list). Hofbauer-Sigmund 1998 added for replicator-dynamics context.

**(h) Verification: 4core_verification.py 6/6 PASS at machine precision; Galois D_4 via cubic resolvent + Gröbner basis.** Verified 2026-05-08:
- Check 1 (Theorem A + 2.4 + B): 8-shell chain for both T+B and T+B+S; sizes 2, 3 forbidden; 4-core 3-substrate closure verified.
- Check 2 (Theorem C): $Z_T - (v+h+br+r)^2 = 0$ and $Z_B - (v+h+br+r)^2 = 0$ symbolically.
- Check 3 (Theorem D ratio): $|p_7/p_8 - (1+\sqrt{3})| = 9.06 \times 10^{-46}$ at 50 dps.
- Check 4 (Theorem E): all 7 chain shells converge to same attractor; mass-outside-$\mathcal{C}$ residual $< 10^{-40}$.
- Check 5 (Theorem D Galois): irreducible; disc $-40896 = -2^6 \cdot 3^2 \cdot 71$; resolvent $(z+2)(z^2-z+18)$; $\mathbb{Q}(\sqrt{3})$ subfield; index 2; $D_4$.
- Check 6 (Theorem F): $\alpha = 1/2$ uniquely admits $y^2 - 2y - 2 = 0$ in $\{0, 1/4, 1/2, 3/4, 1\}$.

**(i) Adopt boilerplate (PROVEN/COMPUTED/RHYME/OPEN + lens-ownership).** Done in §0 of the manuscript (lens-ownership paragraph + tier discipline list). PROVEN: Theorems A, B, C, D, E. COMPUTED: `4core_verification.py` 6/6 PASS. STRUCTURAL RHYME: $\mathbb{Q}(\sqrt{3})$ as a recurring substrate field. OPEN: Conjecture 1.1.

**(j) Update README.md §5 + cover_letter.md.** Both rewritten 2026-05-08 to reflect the new theorem structure, the SFM Q6 finding, and the U(1)/center framing.

---

## §3 — PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorems A (joint-closure chain), 2.4 (three-substrate strengthening), B (4-core 3-substrate closure), C (normalizer identity), D (closed-form attractor + Galois $D_4$), E (universality on chain shells). Theorem F (partial uniqueness on the finite test set $\{0, 1/4, 1/2, 3/4, 1\}$).
- **COMPUTED:** `4core_verification.py` six green-light checks at machine precision; ~4-second runtime. Galois group independently verifiable in PARI/GP or Magma; closed-form ratio independently re-derivable via Gröbner basis in any major CAS.
- **STRUCTURAL RHYME:** $\mathbb{Q}(\sqrt{3}) \subset K$ — the same field that appears across substrate invariants in the parent framework's catalogue (D78, multiple substrate scans). Cited as motivation for why the ratio admits a degree-2 presentation despite the four coordinates living in a degree-4 field.
- **OPEN:** Conjecture 1.1 — $\alpha = 1/2$ uniqueness across $\mathbb{Q} \cap (0, 1)$. The full symbolic uniqueness proof requires Gröbner-basis discriminant analysis at general $\alpha$, which sympy's default solver does not complete in available compute. Maple's `Groebner[Basis]` or Mathematica's `GroebnerBasis` is the natural next step.

---

## §4 — Lens-ownership paragraph (per J_PAPER_BOILERPLATE.md §5.5)

This paper works on $\mathbb{Z}/10\mathbb{Z}$ with three specific commutative non-associative magma tables ($T$ = TSML, $B$ = BHML, $S$ = CL_STD) and a designated four-element set $\mathcal{C} = \{0, 7, 8, 9\}$. These choices are *not derived from first principles*; they reflect a structural reading of $\mathbb{Z}/10\mathbb{Z}$ motivated by a ten-operator decomposition. The theorems below are theorems on this specific structure; analogous theorems would hold on other substrate-and-table choices. The framework's claim is that this particular choice produces theorems with surprising downstream connections (Galois $D_4$ over LMFDB 4.2.10224.1, the $1+\sqrt{3}$ closed-form attractor, joint closure across three independent tables). Whether other substrate choices give similarly rich connections is open. The framing follows the Drápal & Wanless (2021, *J. Combin. Theory Ser. A* **184**, 105510) line of work on small finite commutative non-associative structures.

---

## §5 — Submission gate

This paper is ready for *J Algebra* submission contingent on:
- [x] Manuscript rewritten (this pass, 2026-05-08).
- [x] Verification script 6/6 PASS at machine precision.
- [x] README.md and cover_letter.md updated.
- [x] Six structural theorems numbered to match script.
- [x] SFM Q6 (three-substrate chain) incorporated as Theorem 2.4 + Theorem B.
- [x] U(1)/center framing in §0.
- [x] Drápal-Wanless 2021 cited as closest published precedent.
- [ ] Brayden's referee-rigor pass complete.
- [ ] Per-venue cap check: 2nd *J Algebra* paper this quarter (at cap).

**Earliest realistic submission:** any time after Brayden's referee-rigor pass; the manuscript stands on its own without dependence on companion-paper preprints (J33, J54 are cited as submitted but not as pre-conditions).

---

## §6 — Why this save plan reads as positive recovery

The fresh-eyes referee gave J35 a "Major revisions, close to Accept with minor revisions" verdict. The mathematics was correct; the exposition needed M1 (theorem renumbering), M3 (lead with Galois), M4 (reframe α-uniqueness), M5 (cite magma-pair literature), M6 (clean script reproducibility). The SFM Q6 finding added a substantive new theorem (4-core 3-substrate closure) that was not previously in the manuscript.

The rewritten manuscript:
- Renumbers six theorems to match the six script checks.
- Leads with the Galois punchline ($\mathrm{Gal}(K/\mathbb{Q}) = D_4$ over LMFDB 4.2.10224.1) before displaying the closed-form coordinates.
- Reframes α-uniqueness as partial-uniqueness (Theorem F) + Conjecture 1.1.
- Adds Drápal-Wanless 2021 citation in §0 and §9.1.
- Cleans the verification script: extended Check 1 to three-substrate; standalone closure counts displayed; explicit Theorem B 4-core image check.
- Adopts the U(1)/center framing throughout.

**The single most important upgrade:** moving from "WP110 fusion-closure short note" to "comprehensive structural paper with six theorems converging on $\mathcal{C}$ as the algebraic center, with the three-substrate strengthening as the new central theorem." The paper has gone from the *J Algebra* short-note slot to a substantial structural paper — and the referee's "close to accept" framing should now translate to a clean acceptance after the recommended revisions.

**The Brayden directive 2026-05-08 — "perfect J35 incorporating SFM findings" — is honored.** This plan keeps J35 as the corpus centerpiece, integrates the SFM Q6 three-substrate finding as the new central theorem, and applies the referee's M1-M6 fixes plus the U(1)/center framing from FAMILY_STRUCTURE_v1.md.

**Recommendation:** SUBMIT after Brayden's referee-rigor pass. Per-venue cap warning: 2nd *J Algebra* paper this quarter; if desk-rejects, fallback to *Communications in Algebra* or *Journal of Pure and Applied Algebra*.
