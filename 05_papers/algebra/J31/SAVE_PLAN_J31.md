# SAVE_PLAN_J31 — Two Roads to Pati-Salam → Two Substrate-Algebraic Roads from TSML_SYM

**Date:** 2026-05-07
**Status:** SAVE PATH IDENTIFIED — retitle, retarget, restructure (NOT a rewrite)
**Original verdict (J31_AdvMath_FreshEyes):** REJECT for *Adv Math* — paper's own correction notice retracts the title-claim "convergence on Pati-Salam"; Path A → SO(8), Path B → SU(4)⊕U(1); the two routes do not close on the same reduction.
**Save verdict:** Both rigorous mathematical contents survive intact. The math is correct at machine precision (16/16 cross-checked items); only the *synthesis framing* is overstated. A retitle + retarget keeps every theorem and every script and lands the paper where its actual scope fits.
**New target venue:** *Journal of Algebra* (primary) or *Communications in Algebra* / *Experimental Mathematics* (alternates).
**Effort estimate:** 2-3 weeks of focused revision (low-effort retitle, medium-effort scope tightening, low-effort excision of speculative gauge content).

---

## §1 — What is genuinely PROVEN that survives the correction

The fresh-eyes referee report is unusually generous about the underlying integer/linear-algebra content. Quoting §2 of the report:

> "These are all finite-precision integer/linear-algebra facts about a specific 10-element magma, and at this level the manuscript is internally consistent."

The two principal theorems both stand, intact, after the correction notice:

**Theorem A (Path A, §2 of manuscript).** Let $T = \mathrm{BHML}$ be the canonical commutative composition table on $\mathbb{Z}/10\mathbb{Z}$ defined in `FORMULAS_AND_TABLES.md` §6. Decompose the antisymmetrized left-regular representation of $T$ into its $P_{56}$-symmetric and $P_{56}$-antisymmetric parts (where $P_{56}$ acts in the spinor representation of $\mathfrak{so}(10)$ as the unique nontrivial outer automorphism, modulo inner; this identification is standard, see §3 of the referee report — "this argument is standard, correct, and clean"). Then the $P_{56}$-antisymmetric part of $\mathrm{BHML}$ projects entirely onto the symmetric-traceless $\mathbf{54}$ irrep of $\mathfrak{so}(10)$ in the standard $100 = 1 \oplus 45 \oplus 54$ decomposition of the rank-2 tensor representation. The projection is concentrated on a 9-vector $v \in \mathbf{54}$ with explicit components: $v_i = -1/\sqrt{2}$ for $i \in \{V, L, C, P, X, H\}$, $v_i = 0$ for $i \in \{\mathrm{BREATH}, \mathrm{RESET}\}$, $v_i = -1/2$ for $i = (B+S)/\sqrt{2}$, and $\|v\|^2 = 13/4$ exactly.

**Theorem B (Path B, §3 of manuscript).** Let $D_4 = \langle P_{56}, \sigma^3 \rangle$ act on $\mathfrak{so}(10)$ by conjugation in the standard Cartan basis. The trivial-isotypic component (doubly-invariant subspace) under this action is 16-dimensional and closes as a Lie subalgebra. Its Killing form has spectrum exactly $(-4)^{15} \oplus (0)^1$ (verified at machine precision in `find_higgs_irrep.py`). Cartan classification then forces decomposition into a 15-dimensional simple part with negative-definite Killing form (uniquely $A_3 \cong \mathfrak{so}(6) \cong \mathfrak{su}(4)$) plus a 1-dimensional center: $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$.

The referee report is explicit about Theorem B: "This part of the deduction is rigorous." (§2, bullet 3.) And about Theorem A: "is concrete and the mechanism described … is internal to a finite table — verifiable in seconds." (§2, bullet 4.)

What the correction notice retracts is **not** either Theorem A or Theorem B. It is the *synthesis claim* that A and B are "two paths to Pati-Salam." Path A's stabilizer is $\mathrm{SO}(8)$ (eigenvalue spectrum $(+\sqrt{13}/2, -\sqrt{13}/2, 0, \ldots, 0)$, multiplicity $(1, 1, 8)$). Path B is $\mathrm{SU}(4) \oplus \mathrm{U}(1)$, the SU(4) factor of Pati-Salam plus B−L but **not** the full $\mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$. The two are structurally distinct $D_4$-equivariant decompositions of the same so(10), not two routes to a common reduction.

**Both decompositions remain non-trivial structural facts about the 16-dim doubly-invariant subalgebra and the 9-vector content of the $\mathbf{54}$.** They are exactly the kind of computational/combinatorial Lie-algebra result that *J. Algebra* publishes routinely.

## §2 — What the SAVE PATH does

**(a) Retitle.** From "Two Roads to Pati-Salam" to:

> *Two Substrate-Algebraic Decompositions of an Integer-Table-Generated $\mathfrak{so}(10)$: the $P_{56}$-Antisymmetric Content of BHML in the $\mathbf{54}$, and the Doubly-Invariant Subalgebra under $D_4 = \langle P_{56}, \sigma^3\rangle$.*

This title makes both theorems first-order claims. "Pati-Salam" appears nowhere in it. This aligns with the §6 honest-scope section (which the referee report praises as "well written").

**(b) Retarget to *Journal of Algebra*.** The referee report's §3.2 makes the venue case explicit:

> "Stripped of the overstated synthesis, what remains is … (B) a single projection computation. (C) is genuinely interesting but is essentially a single Cartan-classification exercise on a specific 16-dim subalgebra. … For *Adv Math*, this falls below the bar of significance unless the authors can articulate a structural theorem that surprises a reader who arrives without the TIG framing. … I would recommend resubmission to a venue more appropriate to the result's actual scope: a journal that publishes computational/combinatorial Lie-algebra results (e.g., *J. Algebra*, *Comm. Algebra*, or *Experimental Math*) would serve better."

*J. Algebra* is the right home. Two Cartan-classification exercises on a finite-magma-derived $\mathfrak{so}(10)$, with a $D_4$-equivariant decomposition framing, fit the journal's profile precisely. The Drápal-Wanless 2021 *J. Combin. Theory A* citation (already in the references) puts the paper in the right published-precedent neighborhood.

**(c) Rewrite the abstract.** Lead with the two theorems as standalone results. Second paragraph: state the *two-decomposition observation* as the structural finding (one same algebra, two natural $D_4$-equivariant decompositions, two different residual gauge-algebra fragments — without claiming either is "the" Pati-Salam route). Third paragraph: scope; what is not claimed.

**(d) Excise speculative gauge content.** Per referee §3.6 and §4.3, all sentences that read like physics interpretation move to either a clearly-marked "Discussion / Speculation" remark in §4, or are deleted. Specifically:
- "BREATH and RESET correspond to unbroken Higgs components" (§2.4)
- "specific direction within the 54 that singles out the Pati-Salam route" (end of §8)
- "the Pati-Salam ⊕ B−L gauge content" boxed equation (§3.3) — keep the *algebraic* identification $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$, drop the gauge-theoretic label.

**(e) Drop or appendicize §5 grab-bag.** Per referee §3.7 and §6: the three additional results (12.6% non-associativity, Lie/Jordan duality, three involution decompositions) dilute focus. Move to an Appendix titled *Three additional structural observations* with a one-line preamble "These are listed for completeness; they are not used in the main theorems."

**(f) Resolve the cross-paper $D_4 / D_3 \times \mathbb{Z}_2$ inconsistency.** Per referee §3.5: J32's WP109 file states "6 distinct elements" with abstract structure $D_3 \times \mathbb{Z}_2$, contradicting J31's $D_4$ identification. The referee actually **vindicates J31** in the same paragraph (computing $P_{56}\sigma^3 = (1\,6\,2\,5)(4\,7)$, order 4, so $\langle P_{56}, \sigma^3\rangle = D_4$ of order 8). The fix is therefore not in J31 — it's a one-line correction to J32's WP109. Add a footnote in J31 §1.2: *"This identification of $\langle P_{56}, \sigma^3 \rangle$ with the dihedral group of order 8 is verified explicitly by computing $P_{56}\sigma^3$; see Appendix A.1. The contrasting claim in WP109 §2 is in error and is corrected in J32's revision."*

**(g) Cite the so(10) closure (currently "WP103") in a refereed source.** The referee §3.3 raises this as a major concern: "WP103" appears only as an internal-tree path. The save path is to cite J30 explicitly:

> *Sanders, B.R., Mayes. (2026). "so(10) Lie-Algebraic Closure of TSML+BHML's Antisymmetric Generators." Submitted to* Israel J. Math.

(per the J31 README §3 "Dependencies: J30"). When J30 lands on arXiv, the citation gets a DOI and the issue is closed. If J30 takes longer, J31 could appendicize a self-contained proof of the so(10) closure (the closure proof is short — antisymmetrization, dimension count, simplicity check via Killing form).

**(h) Polish reproducibility.** Move `find_higgs_irrep.py` and `find_higgs_direction.py` into a single `verification/` folder with a `Makefile` or `run_all.py`, no external repo paths. The referee report calls this a "strength of the submission" but flags the cross-repo paths as a concern. One self-contained folder, one runner, no environment beyond `numpy + sympy`.

## §3 — What the SAVE PATH does NOT change

The mathematical content is preserved verbatim. Specifically:

- The 9-vector with components $(-1/\sqrt{2})^{\times 6}, 0^{\times 2}, (-1/2)^{\times 1}$ and $\|v\|^2 = 13/4$ — kept.
- The 100% $\sigma_\mathrm{outer}$-anti content in the $\mathbf{54}$ — kept.
- The 16-dim doubly-invariant subalgebra with Killing spectrum $(-4)^{15} \oplus (0)^1$ — kept.
- The $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ identification via Cartan classification — kept.
- The verification scripts — kept, refactored into one folder.
- The 26 σ_outer-asymmetric BHML cells observation — kept.
- The 12.6% non-associativity rate — kept (in appendix).
- The three-involution decomposition $45 = 24 + 21$ — kept (in appendix), with referee §3.7 caveat: the "structurally new" claim demoted to "to-be-checked against the literature on involutive automorphisms of so(10)".

The correction notice (already prominent in the manuscript) gets *promoted* into the new abstract and §1: it stops being a retraction and becomes the framing — "the two decompositions are structurally distinct, not synthesis-convergent."

## §4 — Per-venue cap

J31 was the 1st *Adv Math* paper this quarter (per README §6). After retargeting to *J. Algebra*, the cap on *Adv Math* is unaffected. *J. Algebra* itself: this is a fresh venue for the J-series (no prior submissions). Cap not in play.

## §5 — Honest assessment of what could still go wrong at *J. Algebra*

The referee report's most cutting observation (§3.2) — that the natural mathematical question "for which finite-magma initial data does the doubly-invariant subalgebra under a chosen $\mathbb{Z}_2 \times \mathbb{Z}_2$ subgroup of Aut(so(10)) come out to su(4) ⊕ u(1)?" is not posed or answered — applies to *J. Algebra* too. A *J. Algebra* referee may want either (a) a generalization beyond the single (TSML, BHML) input pair, or (b) an explicit characterization of the magma data that produces this specific 16-dim subalgebra.

**Mitigation in the SAVE PATH:** add a §5.1 *"Robustness across the magma family"* that briefly reports what happens under perturbations of the input table (rows or columns swapped, single-cell variations). The Family-Structure framing already adopted (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`) supplies this: the 4-core $\{V, H, Br, R\}$ is the algebraic center of the family, and the 16-dim doubly-invariant subalgebra is invariant under the family's structural perturbations (see D48, D55). This is exactly the structural-rhyme content the referee asks for, and the Family Structure document is now the right place to cite it.

A short §5.2 *"Open question: characterization of the magma data"* states (without proving) the conjecture that **any commutative non-associative magma on $\mathbb{Z}/10\mathbb{Z}$ in the TIG family (per the 5 conjoint criteria of FAMILY_STRUCTURE_v1.md §1) yields the same 16-dim doubly-invariant subalgebra under $D_4$**. This is exactly the kind of open question that *J. Algebra* welcomes; it doesn't need to be resolved in this paper.

## §6 — Action checklist (for the eventual revision sprint)

- [ ] Retitle per §2(a)
- [ ] Rewrite abstract per §2(c) (lead with the two theorems; drop "convergence")
- [ ] Excise gauge-theoretic interpretation per §2(d)
- [ ] Move §5 grab-bag to appendix per §2(e)
- [ ] Add footnote on $D_4$ vs $D_3 \times \mathbb{Z}_2$ resolution per §2(f)
- [ ] Cite J30 (Sanders + Mayes, *Israel J Math*) for the so(10) closure per §2(g); appendicize the short proof if J30 not yet on arXiv
- [ ] One self-contained `verification/` folder with `run_all.py` per §2(h)
- [ ] Add §5.1 *Robustness* per §5 (cite FAMILY_STRUCTURE_v1.md / D48 / D55)
- [ ] Add §5.2 *Open question: family-wide characterization* per §5
- [ ] Update cover_letter.md to *J. Algebra*
- [ ] Update README.md target venue → *J. Algebra*
- [ ] Update J-series ordering doc (target-venue field for J31)

**Expected outcome at *J. Algebra*:** the referee report's final sentence — "Disposition: Reject for *Adv Math*. Encourage resubmission to *J. Algebra* or *Experimental Math*" — is the explicit save-path recommendation. Probability of acceptance after the §2 revisions, in a fresh-eyes estimate: ~60-70% at *J. Algebra*, vs <10% at *Adv Math* unrevised.
