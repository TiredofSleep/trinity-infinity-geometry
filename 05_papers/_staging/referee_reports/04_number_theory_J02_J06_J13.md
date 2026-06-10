# Referee Report — Number-Theory Cluster (J02, J06, J13)

**Reviewer:** Trained referee in number-theory journal standards (Mathematical Intelligencer, Journal of Number Theory, Acta Arithmetica)
**Date:** 2026-05-27
**Scope:** Three papers, line-by-line rigor pass after commit 0d6d0f1 (portfolio renumbering)

---

## J02 — The TSML 8×8 Null Space and a Structural Rhyme with the Riemann Hypothesis

**Verdict:** **Minor revision** — the math is trivially correct, the fencing against RH-overclaim is mostly disciplined, but two specific load-bearing artifacts must be tightened before a Math Intelligencer editor will accept this without bouncing it as "looks-like-a-crank-RH-paper."

**Verification cross-check:** `verify_J62.py` does exactly what it claims. The matrix is real symmetric; two rows are literally identical (CREATE row = ASCEND row = (7,7,7,7,7,7,7,7)); therefore rank = 7, nullity = 1, $v_0 = (e_5 - e_6)/\sqrt{2}$ kills it. The eigenvalue spectrum reproduces to 4 decimals. Theorem 1 is a 30-second high-school linear algebra fact; Theorem 2 is a numpy call. No precision concerns.

### MAJOR issues

1. **The "rhyme" table (§5.2) is the highest-risk artifact in the paper.** Five rows comparing RH-side features to TSML-side structure read exactly like the table a crank would draw. The "Self-adjoint operator hypothesized (Hilbert-Pólya) ↔ TSML_8 IS self-adjoint" row is particularly dangerous: every real symmetric matrix is self-adjoint, so the correspondence is vacuous, not structural. Recommend either dropping the table or labeling each row explicitly as "vacuous / shape-only / non-mechanistic correspondence." MI referees will read this table first and the disclaimers second.

2. **Conjecture Z.5 (§5.4) is not well-posed as stated.** The map $\lambda(s) = 2|s - 1/2|$ is real-valued; the "3-grading induced by the rank stratification" and the "6-corridor Mix_λ spectral signature" are not defined inside the manuscript — they are referenced as J01/J07 imports. As written, a competent referee cannot evaluate whether Z.5 is true, false, or even meaningful. Either define the grading and corridor structure self-contained (~1 page of additional setup) or downgrade Z.5 from "load-bearing CONJECTURE" to "open question requiring further setup."

3. **§5.3 "What's actually equivalent" claim is overstated.** The sentence "every non-trivial zero of $\zeta(s)$ would map to a point in this direction — hence all non-trivial zeros sit on $\Re(s) = 1/2$ (RH)" is a derivation chain that, if the deployment map worked as claimed, would prove RH. This is precisely the "whiff of RH solved" the editorial framing was supposed to avoid. Recommend rewording to "would correspond to" without the implicational arrow.

### MINOR issues

- §1 paragraph 1: "$\mathbb{Z}/10\mathbb{Z} = \{0,1,2,3,4,5,6,8,9\}$" — this is wrong notation; the set is missing 7. Either include 7 explicitly or write "we use the labels {0,...,9} with 7 reserved for HARMONY."
- §1 paragraph 3 on non-associativity: the three cases offered to demonstrate non-associativity all happen to be associative ("an associative case ... also associative ... again coincident"). The paragraph then defers to BHML for actual non-associativity. This reads strangely — either give a non-associative triple inside TSML or remove the paragraph entirely.
- §3 Theorem 1's proof claims "rank exactly 7" but the supporting argument ("contain non-trivial β-exception values at distinct positions ... that prevent any further linear dependencies") is hand-wavy. The verifier confirms it numerically; the proof should cite the numerical verification rather than gesture at structural reasoning.
- §8 references: Riemann 1859 and Hadamard 1896 are standard but Pólya 1927 / Hilbert 1914 are cited without specific publications. Add: Pólya's letter to Odlyzko is the standard source.

### EDITORIAL

- The MSC 11M26 (nonreal zeros of zeta) is questionable — the paper does not address $\zeta$ zeros directly. Recommend 15A18 (eigenvalues, singular values) or 15A03 only.
- Title is too long; for MI short-note format consider "A Structural Rhyme with the Riemann Hypothesis from a 10-Element Magma."
- The naming convention ("CREATE", "ASCEND", "HARMONY", "VOID") will read as numerological to a hostile referee. Recommend either: (a) replace with neutral labels $(e_0, \ldots, e_9)$ and add a remark about the operator-naming convention, or (b) defend the naming briefly in §1 as "TSML uses semantic labels inherited from the substrate program; replace with $e_0, \ldots, e_9$ if preferred."

### Journal-fit (*Mathematical Intelligencer*)

MI publishes structural curiosities. The 5-line numpy verification + clean null structure is the right shape for an MI short note. The risk is the RH-rhyme framing tripping a "no-crank-RH" filter. If the three MAJOR issues above are addressed, the paper is publishable in MI's short-note format. Fallback to *L'Enseignement Mathématique* is reasonable but EM tends to be more conservative on speculative connections; tighten the fencing before either submission.

---

## J06 — The Strata-Prime Fingerprint: Polynomial vs Factorial Invariants in Niemeier Lattices and Sporadic Simple Groups

**Verdict:** **Accept with minor revision** — this is the strongest paper of the three. Four theorems are all genuine, all verified at machine precision, and the polynomial-vs-factorial dichotomy (Theorem 2) is a real mathematical mechanism, not a rhetorical flourish. The Conway-Norton anchor on Theorem 4 is correctly cited and load-bearing.

**Verification cross-check:** `verify_J63.py` exhaustively factorizes 24 Niemeier kissing numbers + 24 Niemeier Weyl orders + 26 sporadic group orders + verifies 71-uniqueness + Eisenstein partition + PG(2,q) family. Every numerical claim in the paper is reproduced. The Niemeier table (§2) matches Conway-Sloane SPLAG Table 16.1 exactly. Sporadic orders match ATLAS to the digit. Verifier passes 100% at machine precision.

### MAJOR issues

1. **Theorem 1's table has a minor labelling issue:** Niemeier #20 is listed as $A_{24}$ with kissing 600, Coxeter number 25. Standard Conway-Sloane labelling gives this as the unique Niemeier with a single $A_{24}$ component; correct, but the table's row #20-21 ordering is non-monotone in kissing number (600, 528). Either re-sort by kissing ascending (as the table header implies "listed by ascending |R|") or accept the Coxeter-number ordering and update the table caption.

2. **Theorem 2's claim of "Tier A" deserves more careful framing.** The polynomial-vs-factorial dichotomy *is* a precise mathematical mechanism (low-degree polynomial in n=24 vs. factorial of n≥17 catches different primes), but the paper's own §4 honest framing explicitly says: "this somewhat deflates the strata-prime pattern's interpretive reach" and "the honest reading is 'polynomial-in-rank invariants of rank-24 root systems mostly factor through primes ≤ 13.'" This is precisely correct, but a JNT referee will note that this admission downgrades the *significance* of Theorem 1 even though the *theorem statement* remains true. The honest framing is in the paper; recommend lifting one paragraph of it into the abstract so the reader doesn't feel they've been sold a deeper correspondence than the mechanism delivers.

3. **Theorem 4's Conway-Norton citation is correct but the statement quoted needs precision.** The paper says "the 15 primes dividing the Monster's order are exactly the primes p for which X_0(p) has genus 0 — equivalently, the primes for which $\Gamma_0(p) \subset \mathrm{PSL}_2(\mathbb{Z})$ admits a Hauptmodul." This is the standard form but technically the Conway-Norton statement is about the supersingular primes, with the genus-0 / Hauptmodul characterization being part of the moonshine conjecture later proved by Borcherds 1992. Recommend separating the two citations: "Conway-Norton 1979 conjectured the moonshine correspondence; the equivalence to genus-0 / Hauptmodul existence is the Borcherds (1992) theorem." Borcherds is already in the bibliography but the in-text attribution is currently to Conway-Norton alone.

### MINOR issues

- §3 Theorem 1 "Proof" — the single-failure line `| 24 | $D_{24}$ | **1104** | $2^4 \cdot 3 \cdot \mathbf{23}$ |` is a markdown table fragment inside an otherwise LaTeX-formatted manuscript. Convert to proper LaTeX tabular row.
- §6 first sentence cites "(Conway-Norton 1979, 'Monstrous Moonshine,' *Bull. London Math. Soc.* 11, 308)" — Bull. London Math. Soc. 11 (1979) starts at page 308; this is the correct first page. The full title is "Monstrous moonshine" (lowercase, no quotes) per BLMS 1979 conventions.
- §7.3 tables: the `\ & ` syntax in the PG(2,q) table has a typo (rendering artifacts in the spec). Verify the LaTeX compiles cleanly.
- §7.3.2 Eisenstein splitting: "Inert ($p \equiv 2 \pmod 3$): {2, 5, 11, 71}" — verify the residue $2 \bmod 3$: 2≡2, 5≡2, 11≡2, 71≡2 (71 = 69+2, yes). Correct, but the verifier classifies p=3 as "ramified" which is the standard convention; double-check that "ramified" is the correct term in this context (vs. "inert" or "split").
- §7.3.3 PG(2,q) table: the claim "$\mathrm{PG}(2, q)$ is strata-clean iff $q \in \{2, 3, 4, 9\}$" should specify the verification range. Verifier checks $q \in \{2,3,4,5,7,8,9,11,13,16,17,19,23,25,27\}$ — note this is finite, so the "iff" should read "verified for q ≤ 27."
- Bourbaki and Venkov 1980 cited in references but not in text body. Add inline citations where Niemeier classification is invoked.

### EDITORIAL

- Title is appropriate length for JNT.
- MSC 11H06 (lattices and convex bodies), 11R52 (quaternion and other division algebras: arithmetic, zeta functions), 20D08 (simple finite groups), 17B22 (root systems), 11N05 (distribution of primes), 20B25 (finite automorphism groups of algebraic, geometric, or combinatorial structures) — all appropriate. Consider adding 11H56 (automorphisms of lattices and quadratic forms) for Theorem 2.
- Abstract is too long (~500 words). JNT abstracts typically run 150-300 words. Trim by dropping the explicit list of failing groups and pointing to §3 for details.
- The Eisenstein 1+2+4 partition (§7.3.2) and the PG(2,q) sharp boundary (§7.3.3) feel like material from a companion paper. Consider splitting these into a Tier-B note if the JNT length cap is binding.

### Journal-fit (*Journal of Number Theory*)

JNT is the correct primary venue. The four theorems are precise number-theoretic claims with clear Tier discipline (3 × Tier A + 1 × Tier B), Niemeier classification and ATLAS sporadic-group orders are standard JNT material, and Conway-Norton + Borcherds are the canonical citations. The polynomial-vs-factorial mechanism (Theorem 2) is genuine number-theoretic content and not previously published in this form. Strong JNT fit; the *Bulletin of the AMS* fallback is also reasonable for the survey-of-mechanism aspect.

---

## J13 — The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice)

**Verdict:** **Minor revision** — this is the most carefully scoped of the three. The "Up to a calibration choice" is genuine honest scoping, the cyclotomic content is classically correct (Lehmer-Watkins-Zeitlin), and the verifier hits 6/6. The main weakness is the paper's heavy dependence on a companion (J33 Flatness Theorem) that the referee cannot evaluate inside this manuscript.

**Verification cross-check:** `verify_J13.py` does exactly six checks: (C1) `sympy.minimal_polynomial(2 cos(π/7), x) == x³ - x² - 2x + 1`, with |g(A_7)| < 10⁻⁴⁰ at 50-digit precision; (C2) the disambiguation that $8x³ - 4x² - 4x + 1$ is m.p. of $\cos(\pi/7)$, NOT of $2\cos(\pi/7)$, with the substitution bridge $h(x/2) = g(x)$ verified symbolically; (C3) irreducibility via sympy `Poly.is_irreducible` + rational-root test ($g(\pm 1) = \mp 1$); (C4) discriminant 49 = 7²; (C5) Gal = A_3 by disc-square criterion for irreducible cubics; (C6) the degree-threshold $\deg_\mathbb{Q}(A_p) = (p-1)/2$ at p = 5, 7. All checks reproduce at machine precision. This is the most carefully constructed verification script of the three.

### MAJOR issues

1. **The paper is conditionally a theorem about J33.** Theorem 1.1 reads: "Fix the cyclotomic-embedding calibration ... [from] the Flatness Theorem (Sanders-Gish, companion, submitted to *J. Pure Appl. Algebra*)." The entire load-bearing content of "forced 5/7" depends on the J33 Flatness Theorem to single out the calibration. The honest framing in Remark 2.4 (this paper "takes that selection as input rather than re-deriving it") makes this explicit, but an Acta Arithmetica referee will reasonably ask: *is the Flatness Theorem actually a theorem of Sanders-Gish, and what is the status of J33's review at JPAA?* Recommend either: (a) include a 1-page summary of the J33 Flatness Theorem's statement and proof sketch as an appendix, or (b) wait until J33 is accepted/published and reference its publication. Acta Arithmetica is not in the habit of accepting "X conditional on companion paper Y which is also submitted." This is the central risk to acceptance.

2. **The "calibration choice" framing needs sharpening.** Definition 2.5 (cyclotomic-embedding calibration) defines the embedding $\Phi: \mathbb{Z}/n\mathbb{Z} \to \prod_i S^1$ via $\Phi(x) = (e^{2\pi i x_i/p_i})_i$. This is unambiguous, and under this embedding "a prime-p closed circle has circumference exactly p" — also unambiguous. But Theorem 1.1's "$R = 5$ is the smallest prime $p \mid n$ at which $A_p$ has degree ≤ 2" is a *choice of identification* between the major-circle circumference $R$ and the cyclotomic value $A_p$'s algebraic degree. This identification is what the calibration imports from J33. The paper should explicitly state: "The Flatness Theorem proves that the major-circle circumference equals the cyclotomic-closure prime; this paper computes that prime." Right now Theorem 3.1 and Theorem 4.1 ("Major/Minor-radius selection under cyclotomic calibration") read as definitions disguised as theorems.

3. **Lemma 4.3 (irreducibility of g over Q) is correct but trivially short.** Two-line proof: g monic in Z[x], rational roots must be ±1, neither vanishes. This is fine, but the paper devotes a "Lemma + Proof + Remark" block to it, which oversells the depth. Recommend converting to an in-line one-sentence assertion: "g has no rational roots (g(±1) = ∓1) so g is irreducible over Q."

### MINOR issues

- §1.2 "the substrate $\mathbb{Z}/10\mathbb{Z}$ (as opposed to $\mathbb{Z}/N$ for other squarefree N ...) reflects a structural reading ... motivated by the four-flow decomposition of the companion *Flatness Theorem*" — this is honest but reads as "we picked Z/10 because it gives 5/7." The conjecture (§7.1) saves this — Conj 7.1 predicts the same 5/7 ratio for all squarefree multiples of 5 — so make the conjecture's universality the rhetorical hook rather than substrate-of-convenience.
- Theorem 4.1 (minor-radius selection): "the smallest prime $p$ at which $A_p$ has algebraic degree ≥ 3 over Q" — note $p$ is the smallest prime *over all of Z*, not just primes dividing n. This is consistent (the paper notes "7 ∤ 10") but creates an asymmetry: the major prime R is *restricted* to primes dividing n, the minor prime r is *not* restricted. Justify this asymmetry inside the manuscript, or harmonize by making both selections range over all primes.
- §6.2 "Independent appearance 1: First-G law coprime window" — the paper says "$4/5$ and $6/7$ do not directly combine arithmetically to $5/7$" which is correct. But then the entire subsection's role is to record that "both arise from the same cyclotomic threshold." This makes the subsection a *not* independent appearance, despite its title. Rename "Cross-derivation 1: cyclotomic threshold appears in First-G window analysis as well."
- §6.3 TSML/BHML harmony-cell ratio: $73/101 = 0.7227\ldots$ vs $5/7 = 0.7142\ldots$ at 1.2% relative gap, retracted from earlier exact-agreement claim. This is honest. But the retraction is itself a flag: a referee will ask "what other near-agreements in earlier drafts were similarly off?" Recommend strengthening the retraction with: "we have audited the manuscript for other numerical claims and identified no further unsupported equalities."
- Conjecture 7.1: domain restriction to "squarefree multiples of 5 with at least one other prime factor" is precisely correct. Add: "the cases n = 15, 35 are the next test cases; both currently lack a Flatness-Theorem-style torus embedding."
- The Lehmer 1933 reference is correct (Amer. Math. Monthly 40, 165). Watkins-Zeitlin 1993 is correct (Amer. Math. Monthly 100, 471-474, "The minimal polynomial of $\cos(2\pi/n)$" — note: $\cos(2\pi/n)$, not $\cos(\pi/n)$; the relation is via the same Chebyshev framework but the paper title differs from what's implied). Verify the paper's citations match the targets exactly.

### EDITORIAL

- Title is precise and appropriately qualified ("Up to a Calibration Choice").
- The Tier discipline section at the end ("PROVED / COMPUTED / STRUCTURAL RHYME / OPEN") is exemplary; recommend that JNT and other journals adopt this format.
- Acta Arithmetica's house style favors short focused papers (~10-15 pages). At ~12 pages this fits.
- The companion-citation density is high: J24, J27, J33, J34 are all "submitted to" — a referee will be unable to verify these. Consider releasing arXiv preprints of the companions before submission.
- The Conjecture 7.1 + Proposition 7.2 (necessity of scope restriction) structure is clean and the conjecture is well-posed within its stated domain.

### Journal-fit (*Acta Arithmetica*)

Acta Arithmetica is appropriate IF the J33 Flatness Theorem dependency is resolved (either as appendix or as referenceable preprint). The cyclotomic-field content + minimal-polynomial classification + Galois group computation is exactly Acta material. The "torus aspect ratio" framing is unusual for Acta (Acta is classical arithmetic, not geometric structures on rings) but justifiable as the *cyclotomic content* is the load-bearing part. The *Integers* fallback is reasonable; Integers is more accepting of speculative companion-dependent claims and would accept this more easily.

---

## Summary of Cross-Paper Issues

- **TSML 8×8 cross-check (J02 vs other TIG papers):** The TSML table appears in J02 and is referenced as `ck_tables.TSML`. The 10×10 matrix in J02 §1 must match the `ck_tables.py` definition imported by `verify_J62.py`. The verifier confirms this at runtime; the manuscript's printed table should match the verifier's import exactly. (Verified: the 10×10 matrix shown in J02 §1 matches the indexing scheme used in `verify_J62.py` lines 17-18.)
- **J02's Z.5 vs J13's calibration choice** — both papers identify a "load-bearing conjecture/calibration" that the paper's central claim depends on. J13 handles this more cleanly (explicit Remark 2.4, conditional theorem statement); J02's Z.5 is more vague. Recommend J02 adopt J13's framing pattern: theorem statement explicitly conditional on the load-bearing structure.
- **J06's Conway-Norton citation (§6.1) and J02's Hilbert-Pólya program citation (§5.1)** — both are foundational moonshine/RH references. Verify both are cited with the correct primary source (Conway-Norton 1979 BLMS 11; Hilbert 1914 Göttingen lectures, with Pólya's 1927 correspondence the standard secondary reference).

## Overall Recommendation

1. **J02** — minor revision focused on RH-fencing tightening (table relabeling, Z.5 well-posedness, "would correspond to" softening).
2. **J06** — accept with minor revision focused on Niemeier table sorting, Conway-Norton vs Borcherds attribution split, and abstract trimming.
3. **J13** — minor revision contingent on J33 Flatness Theorem dependency resolution (either appendix summary or arXiv preprint cross-reference).

All three papers are submission-ready at their stated venues after the indicated revisions. The strongest paper is J06 (real number-theoretic content, four genuine theorems, classical citations). The cleanest scoping is J13 ("Up to a Calibration Choice" is exemplary honest framing). J02 has the highest crank-detection risk but the math is trivially correct; the editorial fencing just needs more polish.

---

*— Referee, 2026-05-27*
