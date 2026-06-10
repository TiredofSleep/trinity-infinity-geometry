# Promotions Audit — J17 & J23 (post-renumbering, commit 0d6d0f1)

**Auditor:** portfolio-quality reviewer
**Date:** 2026-05-27
**Scope:** ship-readiness audit for two papers placed in Tier 1 (J01–J31) range after renumbering; both were originally Tier 2.
**Method:** read manuscripts + READMEs + cover letters; ran verification scripts; cross-checked novelty framing against named precedents (Drápal-Wanless 2021, Conway-Norton 1979, ATLAS 1985, Eguchi-Ooguri-Tachikawa 2011).

---

## J17 — Forcing Axioms and the Family of Commutative Non-Associative Magmas on Z/10Z Preserving a Designated 4-Core

**Audit verdict:** **Ready for rigor pass** (with one structural caveat — see Novelty)
**Estimated work to submission:** 1–2 weeks (Brayden's referee-rigor pass + venue-formatting + bibliography polish)
**Recommended venue:** *Algebraic Combinatorics* (currently targeted) is plausible. *J. Combin. Theory Ser. A* is a stretch but defensible given the Drápal-Wanless 2021 lineage. *Algebra Universalis* is a safer fallback.

### Content completeness
Complete manuscript at 666 lines covering all standard sections: abstract / front matter (§0), three displayed 10×10 tables and the 9-axiom forcing theorem (§1), conjecture 2.1 (§2), substrate-to-function map (§3, 17-row table), family-membership criteria + 6 boundaries (§4), the 4-core attractor structural argument (§5), eight selected structural findings on (T,B) (§6), three-substrate chain theorems (§7), open questions (§8), references + bibtex (§9–§10). No skeleton-paper concerns.

### Theorem strength / Tier breakdown
**Tier-A (PROVEN):** 6 — Theorem 1.2 (forcing), Theorem 5.1 (closed-form attractor), Theorem 7.1 (3-substrate joint chain), Theorem 7.2 (4-core 3-substrate closure), Theorem 7.3 (bridge to J-companions), Proposition 4.5 (family-membership).
**Tier-B (COMPUTED-only):** the 17-function substrate-to-function map (§3.1) — well-organized but heuristic.
**STRUCTURAL RHYME (acknowledged as non-derivational):** "4-core is to family as unit circle is to U(1)" (§5.3); LMFDB 4.2.10224.1 convergence.
**OPEN:** Conjecture 2.1 (σ²-triadic three-BHML), Conjecture 8.1 (bimodal α_A gap), Q2/Q5/Q7/Q8/Q9.
Tier discipline is explicit and consistently applied.

### Verification status
**PASS.** `foundation_verification.py` ran in ~3 seconds; all 6 checks green (forcing reconstruction, chain enumeration over 1023 subsets, 4-core 3-substrate closure, C2/C3/C4 membership). Numerical results match manuscript verbatim: T+B+S joint closures = 8, chain sizes {1,4,5,6,7,8,9,10}, α_A(T)=0.8720, α_A(B)=0.5020, α_A(S)=0.8080.

### Novelty assessment
**The concern:** the forcing theorem (Theorem 1.2) takes the substrate-specific data (𝒟, BUMP, BUMPvalues, J_B7) as **input axioms**, not as derived structure. Remark 1.3 acknowledges this honestly. A skeptical referee will read Theorem 1.2 as "given these per-table cell specifications, the cell-filling procedure reproduces the table" — which is structurally a definition, not a theorem. The paper's defense (Remark 1.4: each substrate-data tuple corresponds to a "structural role" of DC/AC/encoding) is interpretive, not algebraic.
**The honest novelty:** Theorem 7.1 + 7.2 (the 3-substrate joint chain identical to the 2-substrate (T,B) chain) is a genuine, computationally-verified, non-trivial finding. Theorem 5.1 (the 1+√3 attractor) is real but cited as derivative of J01 Theorem D — load-bearing rests on companion paper.
**vs Drápal-Wanless 2021:** complementary not competing — DW treat maximally non-associative quasigroups; J17 treats intermediate α_A magmas with prescribed sub-structure. The Drápal-Wanless framing is well-cited.

### Key gaps to address before submission
1. **Tighten Theorem 1.2 framing.** Either explicitly call it a "characterization" / "uniqueness given substrate data" rather than a "forcing theorem," or add a meta-axiom (entropy-extremum, minimal-BUMP, etc.) that selects the three substrate-data tuples. Currently a referee can object that "9-axiom forcing" overstates the constraint when 4 of the 9 axioms encode per-table cell data.
2. **J01 dependency.** Theorem 5.1's proof is "adopt [J01] Theorem D verbatim." If J01 has not yet appeared in print, this paper risks a citation-cycle reject. Either inline J01's Galois argument, or hold J17 submission until J01 is at least on arXiv.
3. **§3 substrate-function map** is a discursive 17-row table with citations to internal Atlas documents (META_PLAN_2026-05-06, SUBSTRATE_FUNCTION_MAP_v1.md). External readers cannot resolve these. Either inline the necessary content or excise §3.
4. **TIG-framework language in §1.4 + §9.1.** The disclaimer is present ("the acronym's etymology is internal... not load-bearing") but the manuscript still names "TIG family." A *Algebraic Combinatorics* referee will likely ask for a neutral name (e.g., "the 4-core preserving family on Z/10Z").
5. **The bibliography is good** (Drápal-Wanless, McKay-Wanless, Bruck, Smith, Drápal-Kepka, Burris-Sankappanavar, Hobby-McKenzie, LMFDB) — no obvious missing comparator papers in finite commutative non-associative magma literature.

**Verdict: legitimately Tier 1 with caveats.** This is real algebraic combinatorics with verified theorems; it is not vapor. The rigor pass should focus on tightening the forcing-vs-characterization framing and resolving the J01 citation dependency.

---

## J23 — Mathieu M_22 Substrate-Prime: Order-Factorization Coincidences

**Audit verdict:** **Ready for rigor pass** — but venue mismatch and a deeper novelty question must be addressed
**Estimated work to submission:** 1 week (single critical numerical error already fixed 2026-05-07; current state is post-revision draft)
**Recommended venue:** *American Mathematical Monthly* is the targeted venue and is feasible for this format. **Caveat:** the paper's stated open question (#1: "structural origin vs deep coincidence") may be a flag to AMM's editor that this is a "look at these coincidences" paper. Consider *Mathematical Intelligencer* or *Amer. Math. Monthly* "Notes" track as alternatives if AMM full-article track rejects.

### Content completeness
Complete 623-line LaTeX manuscript with abstract, introduction, M_22+Steiner background (§2), substrate definition with intrinsic-prime origin (§3), main theorem section (§4), Steiner-parameter backdrop (§5), computational verification section (§6), 6 open questions (§7), acknowledgments, 10-entry bibliography. Well-structured for AMM.

### Theorem strength / Tier breakdown
**Tier-A (PROVEN):** 1 — Theorem 4.1 (non-genericity): 10 of 12 M_22 irrep dimensions lie in the substrate-prime band B = {m : prime factors in {2,3,5,7,11}, ν_2(m) ≤ 1}; binomial null gives p ≈ 1.19 × 10⁻⁶ under uniform null on [1, 385]. The four numerical sub-claims (1)–(4) are all verified computationally.
**Tier-B (Backdrop):** §5 Steiner-parameter table is textbook (Conway-Sloane, Cameron); the paper honestly labels this as backdrop, not novel content.
**STRUCTURAL RHYME (acknowledged):** the σ-orbit-size = hexad-size = 6 coincidence (§5 Remark) is explicitly NOT claimed as a structural map.
**OPEN:** 6 questions in §7 — structural origin, M_22 action on substrate, Steiner-class selection, moonshine connection, other sporadic groups, tighter null model. Question #1 is honestly the central question of the paper.

### Verification status
**PASS.** `m22_decomposition.py` ran in <1 second; all numerical claims verify exactly: |M_22|=443520 sum-of-squares check, classification table reproduces with strict count = 8/12 (7 non-trivial), B-band count = 10/12, |B_385|=67 density 0.1740, p-value Bin(12, 0.1740) ≥ 10 = 1.191859 × 10⁻⁶, strict p-value 2.136594 × 10⁻⁵. Numbers in the manuscript match.

### Novelty assessment
**The honest framing in the title ("Coincidences"):** correctly signals the paper's epistemic status. §1.2 explicitly disclaims "derivation of M_22 from substrate" / "action of M_22 on substrate" / "moonshine-type theorem." This is unusually disciplined.
**But:** the entire paper rests on whether the choice of null model (uniform on [1, 385]) is the natural one. Reasonable alternatives — conditioning on Σd_i² = 443520, or restricting to divisors of |M_22|, or conditioning on the number of irreducibles being 12 — would yield substantially different p-values. The paper acknowledges this (§7 Q6) but does not compute alternative nulls. **A skeptical referee will ask: why this null and not another?**
**vs Conway-Norton 1979 / ATLAS / Eguchi-Ooguri-Tachikawa 2011 (M_24 moonshine):** the paper carefully distinguishes itself ("present non-genericity is arithmetic, not analytic"). It is not in direct competition with moonshine literature. **But:** order-factorization "coincidences" in sporadic groups are a well-explored space; the AMM/MAA tradition of "elegant numerical coincidence" papers is large. The paper needs to clarify what its contribution is *over* this tradition.
**Deeper concern (honesty check):** §3 defines the substrate primes "from intrinsic substrate data," but the role of prime 11 (the wobble fraction's 11-prolongation, W·11/11 = 33/550) is genuinely strained. The paper acknowledges this ("the case for 11's substrate-distinguishedness is weakest of the five"). This is honest, but it does mean the substrate-prime distinction was partly reverse-engineered from |M_22|. A careful referee may flag this.

### Key gaps to address before submission
1. **Compute one or two alternative null models.** §7 Q6 acknowledges the uniform-null choice; commit to computing at least the sum-of-squares-conditioned null and reporting it. This will either strengthen the theorem (if the concentration persists) or qualify it appropriately (if it weakens substantially). Without this, the referee report writes itself.
2. **Tighten §3.1 prime-by-prime origin.** The cases for 2, 3, 5, 7 are clean (CRT factors, σ²-cycle order, σ-orbit characteristics, HARMONY index / T* denominator). The case for 11 is weak. Either find a cleaner substrate-internal origin for 11 (e.g., the smallest prime above 7 with a substrate role) or restrict the theorem to {2, 3, 5, 7} and report 11 separately.
3. **J15 (= J01-equivalent) dependency.** The paper cites SandersGishFourCore for the substrate definition. Same situation as J17/J01: J15 should at least be on arXiv before submitting J23.
4. **Reference §3 in §6.5** of J06 (the extension paper covering all 24 Niemeier lattices + 26 sporadics) — per the README header note, J06 is now the full extension. The relationship needs one clarifying sentence in J23's introduction: "this paper is the focused short note on M_22; the full extension across 26 sporadics is J06."
5. **AMM-style adjustments.** Currently the manuscript is amsart-formatted with author affiliations. AMM uses a specific style; convert to AMM's template before submission. Acknowledgments paragraph mentions "Trinity Infinity Geometry framework" + a GitHub URL — this kind of personal-project framing is unusual for AMM and may attract editor pushback. Consider neutralizing.
6. **Honest title revision.** "Order-Factorization Coincidences" is fine for the *Monthly*. If submitting to *Mathematical Intelligencer*, the same title works. If pivoting to *J. Algebra* or similar venue, "Coincidences" in the title will be a reject signal — rename to "A Non-Generic Concentration of M_22 Irrep Dimensions" or similar.

**Verdict on Tier 1 placement:** **borderline.** Mathematically the paper is tight and verifies. The contribution is a small, clean, well-disclaimed observation. It is *not* a tier-1 *structural* contribution (Mathieu groups, Steiner systems, and sporadic-group arithmetic are textbook); the paper's value is in the substrate→prime-mapping connection, which is novel only if the substrate itself is published and accepted. **The Tier 1 placement is reasonable if AMM-type venue is the target;** a refereed-research-journal venue would not accept this without substantially more structure.

---

## Cross-paper summary

Both papers PASS their verification scripts and have complete manuscripts. Both honestly disclose their substrate-dependence on companion papers (J01 / J15) and on internal TIG-framework definitions. Both apply the PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN tier discipline.

**J17** is mathematically the stronger paper (six PROVEN theorems with verified scripts, one of which — the 3-substrate joint chain — is a genuinely non-trivial enumeration result). Its main risk is referee pushback on the "forcing" framing of Theorem 1.2.

**J23** is the weaker paper (one theorem, narrow scope) but it is honestly scoped and explicitly disclaims overreach. Its main risk is null-model robustness and the reverse-engineered prime-11 case.

**Recommendation: keep both in Tier 1 with the rigor pass.** J17 belongs there on theorem strength; J23 belongs there on writing discipline and verification cleanliness, but should target a *Monthly*-style venue rather than a structural-research venue.
