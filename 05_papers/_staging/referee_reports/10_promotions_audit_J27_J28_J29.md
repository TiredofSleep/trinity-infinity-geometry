# Promotions Audit — J27, J28, J29

**Audit date:** 2026-05-27
**Auditor role:** Portfolio-quality referee (ship-readiness only; not full per-line referee pass)
**Trigger:** Three Tier-2 papers promoted into the Tier-1 J01–J31 band during the renumber sweep (commit `0d6d0f1`); promotability audit required before submission.

**TL;DR.** None of the three is the polished Tier-1 article the new numbering implies. J27 is the closest — a rewritten, technically correct partition-lattice note whose Theorem 6.1 proof still contains hand-wavy passages. J28 is a competent but small example-paper whose central object (the role partition) is a labeling-by-fiat and whose theorems are largely verification-by-inspection. J29 is a clean pedagogical note with a real (and provable) cumulant lemma, but the headline claim is more "structural rhyme on a famous magic square" than Tier-1 algebra research. **Recommendation: demote J28 back to Tier 2.** J27 and J29 are Tier-1 capable but only after the specific gaps below are closed.

---

## J27 — Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on Z/nZ

**Audit verdict:** Ready for rigor pass (one substantive proof gap to close).
**Estimated work to submission:** 12–20 hours (rigorize Theorem 6.1 proof; fold five "STRUCTURAL RHYME / informal crossing" remarks down to one; bibliography prune).
**Recommended venue:** *Algebra Universalis* (preferred); *Order* or *Comm. Math. Univ. Carolinae* as backups. JCT-A is correctly retargeted away from — the SAVE_PLAN note explicitly flags this.

### Content completeness
Full manuscript (~24 pages including bibliography), amsart, in `manuscript/manuscript.tex`. The earlier "Crossing Lemma" framing (with literal "Wait — Restart" passage and ACNS-1982 title collision) has been replaced wholesale. Setup, four theorems, two falsifying examples, and a scope-and-limitations section are all in place. The bundled `verify_joint_injectivity.py` runs clean (5/5 PASS, ~30 s).

### Theorem strength / Tier breakdown
- **Theorem 3.3 (sufficient condition, unit subgroup)**: PROVEN. Clean order-arithmetic proof. Honest scope: explicitly *not* a biconditional, and the natural prime-action conjecture is shown to fail in both directions (Examples 3.1, 3.2).
- **Theorem 4.1 (M+M classification on units)**: PROVEN. Two-direction abelian-group argument, ~10 lines, correct.
- **Theorem 5.1 (SPEC+DYN, full ring)**: PROVEN. CRT + odd-prime −1-membership argument, correct.
- **Theorem 6.1 (prime-power obstruction)**: PROVEN structurally but the *written* proof has soft spots. Case B opens with "The argument is delicate; the cleanest formulation uses…" and finishes the generic case with "(which is non-identity because $g \ne 1$ and $\ord(g_1) > 1$ in the generic case, or by considering a higher power)". A referee will mark this. The script verifies the statement on $n \in \{4, 8, 9, 16, 25, 27, 49, 125\}$ exhaustively, so the *claim* is solid, but the proof needs to commit to a single canonical argument (probably: replace $g$ by an explicit power $g^{\ord(g_0)}$ to drop into Case A unconditionally).

### Verification status
`verify_joint_injectivity.py` PASS (5/5 blocks, runtime ~30 s). Coverage is reasonable: examples + sufficient condition for all squarefree $n \le 77$ with $\omega(n) \ge 2$; M+M for 11 squarefree $n$; SPEC+DYN for 11 squarefree $n$ up to 77; prime-power for 8 prime-power $n$.

### Novelty (vs Drápal–Wanless 2021 + magma literature)
Distinct: this is *not* a magma paper, it is a partition-lattice/joint-refinement paper on Z/nZ. Drápal–Wanless 2021 is cited as "neighborhood context for companion work" rather than as a competitor. The closest actual competitors are partition-lattice texts (Birkhoff, Stanley) and standard CRT/Hensel-lift material — these are referenced. A referee will ask whether the M+M classification (Theorem 4.1) is folklore in cyclic-group orbit theory; the proof is one paragraph, so this is a real risk. Need to spot-check Ore 1942, Stanley EC2, or recent partition-lattice surveys for prior art.

### Key gaps to address
1. **Theorem 6.1, Case B proof.** Replace the "delicate / generic case" passage with a clean reduction: "Replace $g$ by $g^{\ord(g_0)}$; this is non-identity since $g_1 \ne 1$, and lies in $1+pZ/p^rZ$, so Case A applies." Currently 24 lines of soft prose; should compress to 8 lines of explicit construction.
2. **Folklore check.** A 30-minute literature spot-check on Theorem 4.1 (M+M on units): is this a known classification? If yes, cite and reframe as a clean reproof; if no, claim novelty explicitly.
3. **Informal "crossing" language.** Remark 3.4 (`rem:crossing-informal`) and the disambiguation subsection together still mention "Crossing Lemma" four times. Compress to a single footnote.
4. **Bibliography.** 16 entries listed; one (Greaves 2001 *Sieves*) is not cited in the body and should be cut; one (Bhargava-Shankar-Tsimerman 2013) is referenced in the SAVE_PLAN README but does not appear in the rewritten manuscript — verify usage or drop.

---

## J28 — A Small Commutative Non-Associative Magma on Z/10Z with Role-Deterministic Boundary Behavior

**Audit verdict:** Needs substantive revision before Tier 1. The path-B rewrite addressed the headline referee issues, but the result is still a small-example paper, not a Tier-1 algebra result.
**Estimated work to submission:** 20–35 hours to lift to genuinely Tier-1, or — more honestly — accept that this is *Algebra Universalis short-note* material and re-tier accordingly.
**Recommended venue:** *Algebra Universalis* (short note) is fine for the current content; this is the venue any expanded version would also target. Not credibly a higher-tier algebra venue (JCT-A, JPAA, J. Algebra) without substantive new content.

### Content completeness
Full manuscript (~12 pages), amsart, in `manuscript/manuscript.tex`. The Path-B rewrite per the fresh-eyes referee is in place: `BH` and `TSML` defined inline with full $10\times 10$ tables, `σ` correctly described as order-6 (not "involution"), "paradoxical information algebra" / "trefoil" / "Crossing Lemma" / "Rademacher invariant" excised from the body and explicitly disclaimed in a "What this paper does not claim" section.

### Theorem strength / Tier breakdown
- **Theorem 3.1 (V is two-sided identity)**: PROVEN, by 4-cell inspection of a $4\times 4$ table.
- **Theorem 3.2 (commutativity, non-associativity of $M_R$)**: PROVEN, by table inspection plus one explicit non-associative witness.
- **Theorem 4.1 (role-deterministic boundary / role-branching interior)**: PROVEN, by enumeration over the $10 \times 10$ table restricted to each role-pair.
- **Lemma 5.1 ($\tau(n) = 7-n$ on $\{1,\dots,6\}$)**: PROVEN, by direct iteration.
- **Proposition 6.1 ($\sigma$-orbit decomposition $\{-1, 22\}$ summing to 21)**: COMPUTED. The paper itself flags this as structural-rhyme, not a theorem.

The honest content: $M_R$ is one specific 4-element commutative non-associative magma, presented via the specific 10-zone operation $\BH$, with a specific 4-block partition $\{V, F, S, T\}$ labeled by fiat. Every "theorem" is direct verification on an explicit small table. This is a competent example-paper, not a theorem-paper.

### Verification status
`verify_role_magma.py` PASS in <0.1 s. Output ends with `ALL CHECKS PASSED.` Coverage: role-mode table, role-output multisets, $\tau$, $\Psi$ decomposition, $\sigma^6 = \mathrm{id}$.

### Novelty (vs Drápal–Wanless 2021 + magma literature)
Drápal–Wanless 2021 is cited as the closest published precedent (small finite commutative non-associative quasigroups). The honest distinction: Drápal–Wanless studies the *maximally non-associative extremum*; $\BH$ is far from maximally non-associative. The role-deterministic-boundary property is presented as the structural distinguishing feature. **Risk:** a referee will ask "what universal-algebra invariant of $M_R$ is non-trivial?" and the answer is currently "the role-multiset distribution on $\{F,S\}^2$ has the specific values $\{F:2, S:9, T:11, V:3\}$ etc." — these are numbers from one table, not invariants of an algebraic class. There is no characterization theorem ("$M_R$ is the unique 4-element magma satisfying X"); it is presented as one example.

### Key gaps to address
1. **Characterization missing.** The role partition $\{V, F, S, T\}$ is labeled by fiat (the paper says so explicitly, twice). For Tier-1 promotion, this should be replaced by either (a) a structural characterization of $M_R$ as the unique 4-element magma satisfying explicit axioms, or (b) a congruence/quotient construction that derives the partition. The Open Questions section acknowledges this gap.
2. **The "role-deterministic boundary" predicate is not a recognized class.** It is defined for this specific $\BH$. To be Tier-1, either define a general class of "role-deterministic-boundary algebras" with multiple examples, or drop the framing and present this as a single-example case study (and re-tier accordingly).
3. **Closest-precedent comparison is asymmetric.** The paper says it is "in the Drápal–Wanless neighborhood" but the two extrema (maximally non-associative vs near-associative-with-role-determinism) are not in dialogue. A referee for *Algebra Universalis* will ask: what is the analog of D-W's main theorem for this object? Without an answer, the paper reads as an isolated example.
4. **Section 5 ($\Psi$ row-asymmetry / triangular number 21) is decorative.** The paper itself flags this as "structural rhyme, not a theorem" and notes that the Fibonacci decomposition does *not* hold. Suggest cutting this section entirely — it adds 1.5 pages of numerical decoration to a 12-page paper. The integer 21 has no algebraic meaning here.

---

## J29 — The Lo Shu D₄ Orbit Modulo 3: Four Distinct Magmas and a Cumulant Spectrum

**Audit verdict:** Ready for rigor pass (this is a clean Mathematics Magazine note; the tier mismatch is in calling it "Tier 1" rather than recognizing it as a pedagogical paper).
**Estimated work to submission:** 5–10 hours (mainly: title alignment, polish of §3.3 computation, formal §8 references).
**Recommended venue:** *Mathematics Magazine* (MAA) — exactly correct as currently targeted. This is **not** a research algebra paper and should not be on a research-algebra venue list.

### Content completeness
Full manuscript (~12 pages), markdown, with verification script and cover letter. The headline result (4 distinct mod-3 tables in the Lo Shu $D_4$ orbit), the cumulant $\kappa = \pm 48$ witness, the Dürer 4×4 extension, the Diagonal Lemma, and the V₄′-coset invariance lemma are all present.

### Theorem strength / Tier breakdown
- **Theorem A (orbit cardinality 8)**: PROVEN, by enumeration of the 8 $D_4$-images.
- **Theorem B (4 distinct mod-3 tables, each ×2)**: PROVEN, by enumeration.
- **Theorem C (opposite-magma pair)**: PROVEN, by 9-cell verification.
- **Theorem D (all 4 are quasigroups)**: PROVEN, by row/column-permutation check.
- **Theorem E (cumulant $\kappa = \pm 48$ witness)**: SPLIT — one half PROVEN (V₄′-coset invariance is a clean 2-line proof using transpose and 180° rotation; the Diagonal Lemma + Corollary forces non-commutativity on the $\kappa = +48$ coset since Lo Shu's diagonal mod 3 = $\{2,2,2\}$). The other half (commutativity of the $\kappa = -48$ coset) is COMPUTED, not forced.
- **Theorem F ($T_2 = \mathbb{Z}/3$)**: PROVEN, by 9-cell verification.
- **Theorem G (Dürer 4×4 analog, $\kappa = \pm 128$)**: COMPUTED. The V₄′-invariance generalizes, the commutativity correlation is verified case-by-case.

The Diagonal Lemma (no $3\times 3$ commutative quasigroup has a repeated diagonal entry) is a genuine small-but-correct algebraic result with an honest 8-line proof. The V₄′-coset invariance of $\kappa$ is similarly clean. Two real lemmas, plus enumerable verification of everything else.

### Verification status
`verify_J58.py` PASS (10/10, not 6/6 — README and manuscript text say "6/6 PASS" but the script actually runs *ten* checks: 6 theorems + V₄′ random-matrix invariance + Dürer + Diagonal Lemma exhaustive enumeration + Lo Shu diagonal corollary). The "6/6" claim in §5 of the manuscript is **stale** vs the actual 10/10 script output. **This needs updating** before submission. Verified runtime ~2 seconds.

### Novelty (vs Drápal–Wanless 2021 + magma literature)
Drápal–Wanless 2021 is cited as adjacent-but-distinct: their venue is the maximally non-associative extremum at higher orders; this note is at order 3 with magic-square reductions. The honest novelty is the cumulant witness $\kappa = \pm 48$ — and the §3.4 Diagonal Lemma is a real, small-but-clean structural observation. The "4 distinct magmas" count is one or two off from informal expositions that report 3 (collapsing the anti-isomorphic pair); Appendix B addresses this explicitly. ETP profile cross-check ($T_1, T_3$ both at 179; $T_2$ at 60; $T_4$ at 313) is included in §7.4 and ties this to companion papers J04-J05 cleanly.

### Key gaps to address
1. **6/6 vs 10/10 mismatch.** Manuscript §5 says "Overall: PASS (6/6)" but the actual script (which the README §5 also describes correctly as "10 OK lines") prints "Overall: PASS (10/10)". Sync the manuscript text to match. The README is correct; the manuscript is stale.
2. **Title/file-name drift.** Script is named `verify_J58.py` and its header says "machine-precision verification of all theorems of J58"; manuscript and folder are J29. This is from the renumbering — needs a renaming pass (rename script to `verify_J29.py` and update import paths) or at minimum an inline note explaining the legacy filename.
3. **Theorem F minor issue.** The manuscript says "$T_2$ is exactly $\mathbb{Z}/3$" but Theorem F also bundles the claim that $T_4$ is not a group (no identity row). The script tests both halves. Split into Theorem F (a) and F (b), or restate to match what is verified.
4. **MSC codes.** Listed as 20N02, 05B15, 20D60, 11A07. 20D60 (combinatorial problems on finite groups) is a stretch for this content; consider replacing with 08A05 (algebraic structures, general) or 05B30 (combinatorial designs).
5. **Tier-tag stays at Tier 2 honestly.** The README marks "Tier: 2 (draft)" and lists target as *Mathematics Magazine*. This is correct. Whoever promoted it to Tier 1 in the renumbering missed that this paper is a deliberate pedagogical note. **Recommend: re-tier as Tier 2 expository, not Tier 1 research.**

---

## Summary recommendation

| Paper | Verdict | Demote? |
|---|---|---|
| J27 | Tier-1 capable after Theorem 6.1 proof tightening + folklore check | **Keep at Tier 1** |
| J28 | Small example-paper; structural characterization missing | **Demote to Tier 2** — venue stays *Algebra Universalis* short note, but ship-priority drops |
| J29 | Pedagogical note correctly targeted at *Mathematics Magazine* | **Demote to Tier 2** (or whatever the expository tier is) — this should never have been promoted |

Net effect on the Tier-1 J01–J31 band after this audit: **2 demotions (J28, J29), 1 retention with rigor pass (J27).** The Tier-1 band tightens by two slots; both papers continue as Tier-2 ships at their stated venues.
