# Referee Report — Honest-Negative Cluster

**Papers reviewed:** J30 (Communications in Algebra), J31 (Statistical Science companion)
**Reviewer perspective:** trained referee for *Communications in Algebra* and *Statistical Science*; honest-negative-paper discipline (PROVEN / STRUCTURAL / EMPIRICAL / OPEN tier hygiene, scope-of-claim discipline, post-hoc disclosure)
**Date:** 2026-05-28
**Source commit reference:** post-renumbering pass (0d6d0f1)

---

## J30 — The Multiplicative-Unit Sub-Magma C = (Z/10Z)* in the TSML Composition Lattice, and Its Contrast with the Joint 4-Core {0, 7, 8, 9} (target: Communications in Algebra)

**Verdict:** Minor revision — content is sharp, the retraction is correctly cordoned, the contrast is structured. Only blocker is a verification-script mismatch: the script `4core_verification.py` shipped with the manuscript is the *joint-4-core* paper's verification harness (J15/J01), not J30's. None of the J30-specific computational claims (78 TSML-closed 4-subsets; the 16-cell BHML cell-distribution on C×C; generator-selection mod-10 arithmetic) is checked by the included script. Fixable in an afternoon; required before submission.

**Verification cross-check:** `manuscript/verification/4core_verification.py` is the 6-check joint-4-core script (chain enumeration, normalizer identity, attractor h/br = 1+√3 at α=1/2, universality across shells, Galois D₄ on x⁴+4x³−x²+2x−2, α-sweep PSLQ). It does NOT contain (a) the 16-cell enumeration of CL_TSML|_{C×C} producing image {3,7} with the 14/2 distribution; (b) the 16-cell enumeration of CL_BHML|_{C×C} producing image {0,2,4,6,8} with the 3/3/5/4/1 distribution; (c) the exhaustive enumeration of size-4 subsets giving 78 TSML-closed / 1 BHML-closed; (d) the elementary 3³≡7, 7³≡3 mod 10 generator-selection. The README §2 claims these run "inline" — they do not appear in the shipped script.

**Manuscript file status:** Both `manuscript.md` and `manuscript.tex` are present, well-titled, and consistent with the README abstract. The author block is correctly de-duplicated (per R1 fix). PROVED/COMPUTED/STRUCTURAL RHYME/HONEST NEGATIVE/OPEN tier discipline is explicit in §0. No file-naming issues.

### MAJOR issues
1. **Verification gap — required fix.** The shipped script verifies the *companion paper's* claims, not this paper's. Add (preferably to the same file, gated by an `if __name__ == "__main__"` extension) a `check_J30()` function that explicitly performs the four J30-specific computations listed above. Without it, the §7 "Reproducibility" paragraph is inaccurate. (The required checks are <30 lines of Python total; this is hygiene, not a content gap.)
2. **§5 Theorem 5.1 vs §5 Remark 5.2 — citation circularity.** The cover letter says the generator-selection argument is "self-contained inline" (no reliance on unwritten companion). Theorem 5.1's proof IS self-contained (3³≡7 vs 7³≡3 mod 10 and the elementary inequality). But Remark 5.2 then cites J33 for "the full TIG flatness theorem T*=5/7 derives this ratio from several independent algebraic chains." Comm Algebra referees will (correctly) ask: if the wider theorem is in J33, then T*=5/7 should be stated as a *consequence* of Theorem 5.1 here, not the other way around. Recommend rewording Remark 5.2 to "Theorem 5.1 gives one of several independent derivations of T*=5/7 that J33 collates."

### MINOR issues
- §2 Remark 2.3 talks about "CREATION orbit" and "DISSOLUTION orbit" (TIG-internal names LATTICE/PROGRESS/RESET/HARMONY/COUNTER/CHAOS/BREATH/COLLAPSE/BALANCE/VOID). Comm Algebra readers will not parse these. Either drop the names and present 1→3→9→7→1 and 2→6→8→4→2 as orbits of ×3 on (Z/10Z)* and (Z/10Z)\{0,5} respectively, or add a one-line glossary footnote on first use.
- §4.2 Theorem 4.3 statement (3) says "there is exactly one subset of size 4 that is jointly CL_TSML- and CL_BHML-closed." This is genuinely the new structural point — make it the headline of the section heading rather than burying it.
- The 73-HARMONY rate (73/100) is used in §1 and §3.2 without definition; Comm Algebra readers don't know it. State once in §1: "CL_TSML has 73 entries equal to 7 out of 100; we call this the *HARMONY saturation rate*."
- §6.1 says shells at sizes {1, 4, 5, 6, 7, 8, 9, 10} are in J15/J01 — the J15 dependency is `Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor`. Confirm cross-reference resolves under the new J-numbering.
- Bibliography lists J33 *twice* under two different titles ("The CL Forcing Axioms" and "The Flatness Theorem T* = 5/7"). These appear to be the same paper described differently, or two papers both J-numbered J33. Disambiguate or merge.

### EDITORIAL
- Title is 25 words; Comm Algebra prefers shorter. Suggest: "Multiplicative-Unit Sub-Magma of (Z/10Z) in the TSML Composition Lattice, and the Joint 4-Core Contrast."
- Drápal–Wanless (2021) cited correctly in §6.2 and §9.
- Per-venue cap note (3rd Comm Algebra after J12, J18) — flag for the editorial board; the README already lists JPAA / J. Alg. Appl. / Semigroup Forum as fallbacks.

### Journal-fit (honest-negative discipline)
The honest-negative discipline is exemplary on this paper. The retracted claim is explicitly named (Remark 4.2: "the lens-invariance assertion is formally retracted in this revision"), the 16-cell counterexample is exhibited in full, the surviving positive content (Theorem 3.1, Proposition 4.1, Theorem 4.3, Theorem 5.1) is precisely stated, the tier discipline at the top of the manuscript labels each item correctly. The "contrast" structure of §4 — many TSML-closed 4-subsets vs unique joint-closed 4-subset — does exactly what a contrast paper should: point-by-point distinction with both quantitative counts and structural-meaning interpretation. Comm Algebra accepts honest-negative scope when the substrate is mature; the J30 substrate (Z/10Z with two named 10×10 tables) is anchored to companion papers J33 and J15/J01, which is enough.

The only thing keeping this from a clean Accept is the verification-script mismatch (MAJOR-1). Once that is patched, this is a legitimate Comm Algebra note.

---

## J31 — Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate (target: Statistical Science)

**Verdict:** Minor revision — well-disciplined methodology paper, post-hoc disclosure correctly handled, gating verification script now present, but file housekeeping is broken: the manuscript folder still contains the leftover file `J15_DiscreteSinc2_QM_JMathPhys.md` which is a completely unrelated paper (a discrete-sinc² identity in finite QM, target *J. Math. Phys.*, by Sanders + Mayes). This MUST be removed or relocated before submission, or a *Statistical Science* editor opening the submission folder will be confused about which manuscript is being submitted.

**Verification cross-check:** Three scripts in `manuscript/verification/`: `distilgpt2_sweep.py` (Part 1; resolves the M1 gating issue identified in the prior fresh-eyes referee report — extracts 16 distilgpt2 tensors via HuggingFace, partitions into 200 random 10×10 blocks each, runs D1/D2/D3/D4, computes Cohen's d vs scale-matched Gaussian baseline); `structured_matrix_sweep.py` (Part 2 9-family battery + 4 detectors); `d5_d4eq_extension.py` (Part 2 post-hoc D5 prime-7 and D4_eq D₄-orbit-averaged Higgs). All three scripts have inlined TSML/BHML tables matching the manuscript §1.1 (row-by-row spot-check confirms TSML row 1 = `0737777777`, BHML row 1 = `1234567266`). Detector definitions in `distilgpt2_sweep.py` match those in `structured_matrix_sweep.py` (D1 = ||A||²/(||A||²+||S||²); D2 = ||M − P₅₆MP₅₆||²/||M||²; D3 = `1` iff 11 | c₂ and 11 | c₈ on the scale-10 integer-rounded charpoly; D4 = cosine alignment with the 45-vector tile of the 9-vector Higgs direction). Reproducibility claim in §6 of the manuscript is sound.

**Manuscript file status:** The correct manuscript is `manuscript/manuscript.md` (titled "Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate: A Negative Result on Trained Transformer Weights and a Structured-Matrix Sharpening"). **The file `manuscript/J15_DiscreteSinc2_QM_JMathPhys.md` is a completely different paper** — a mathematical-physics short note on the closed-form identity R(k,f) = sin²(πk/f)/(k² sin²(π/f)) and its discrete-sinc² implications for finite QM on Z/NZ, authored by Sanders + Mayes (not Sanders + Gish), targeting *Journal of Mathematical Physics*. This is the J15-numbered leftover flagged in the review brief; it has nothing to do with detectors or transformer weights. It is a stale file that needs to be either deleted from J31's `manuscript/` folder or moved to its proper J-folder under the new numbering. Submitting J31 with this file in the manuscript folder is a desk-rejection risk on grounds of "what is the editor supposed to read?"

### MAJOR issues
1. **File housekeeping — required fix.** Remove `manuscript/J15_DiscreteSinc2_QM_JMathPhys.md` from J31's manuscript folder, or move it to the correct J-folder for the discrete-sinc² paper. Also worth confirming under the new numbering whether the discrete-sinc² paper has its own home (it appears to be a Sanders+Mayes paper, distinct from the Sanders+Gish J-series, possibly orphaned by the renumber).
2. **Title vs scope tension.** The title says "Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate." But Part 1 is a *negative* result on distilgpt2 (the detectors do NOT specifically discriminate trained weights from Gaussian noise), and Part 2 introduces *post-hoc* detectors (D5, D4_eq) tuned to TSML's known properties to identify a sufficient pair. The paper title implies a test of TIG-substrate specificity in general, but what's actually delivered is (i) a scoping negative on one transformer family, and (ii) a confirmatory identification of a sufficient detector pair on a hand-designed battery. *Statistical Science* referees will push hard on this gap. Recommend retitling to something like: "Specificity Scoping of Algebraic Detectors: a Negative on distilgpt2 Weights and a Post-Hoc Sufficient Pair on Structured Matrices." The current title overpromises.
3. **§3.4 joint-test p-value bound.** The bound `p ≤ 0.01 × ε` with Laplace-smoothed `ε = 1/202` giving ~5×10⁻⁵ is correct as a *bound*, not a *p-value* (the post-hoc design defeats nominal-α interpretation). The manuscript correctly states "the post-hoc-design caveat is the load-bearing constraint on this p-value, not the numerical bound." Excellent. But the §3.4 paragraph ends with "a sufficient detector pair (D3, D5 at 7⁵) for TSML in the 1800+ sample structured population, designed in light of TSML's known properties." A *Stat Sci* referee will ask: what would constitute a falsification of the sufficient-pair claim? Answer requires (a) holdout-family verification, (b) blind-design protocol. §3.3 names this as recommended follow-up; recommend promoting that paragraph to a numbered "Future work" §3.5.

### MINOR issues
- §1.3 D3 single-sample Cohen's d for TSML against the Gaussian baseline is correctly relabeled as a z-score. But D3 is *binary* (output ∈ {0, 1}), so the z-score language is also imperfect — a Bernoulli single-success against a baseline rate ≈ 0.01 is better stated as exact binomial p ≤ 0.01, which the manuscript does state. Could be slightly clearer that the z-score is for D1/D2/D4 only.
- §2.5 "Max |d| ≈ 0.45" — borders on the conventional small-effect threshold (|d|=0.5) and §2.7 acknowledges it's "barely above" Bonferroni-corrected significance. Worth a sentence in the abstract acknowledging this proximity (currently just "|d| < 0.5"); it makes the negative more honest.
- §3.3 "D5 was designed in light of TSML's known characteristic-polynomial discriminant structure (7⁷ as a factor of the squarefree part)" — confirm this is true (the verification scripts compute the discriminant of TSML's integer charpoly; the manuscript should briefly cite J33 or J19 where the 7⁷ fact lives so the reader can verify).
- §6 references the verification scripts but doesn't say a fixed seed produces deterministic output. The scripts do support seeding (e.g., `--seed 0` in `distilgpt2_sweep.py`). State this in §6.
- "Higgs direction" terminology is a TIG-internal name that *Stat Sci* readers won't parse. Either gloss it as "a fixed 9-component reference direction" or pick a substrate-neutral name.
- The 4-detector table summary in §2.5 should include the per-detector mean over the 16 tensors, not just the max — a *Stat Sci* referee wants the full distribution.

### EDITORIAL
- Per-paper rigor pass already done (per the README §3, M1–M7 resolved); the cover letter explicitly lists which issues were addressed. This is excellent submission discipline.
- Drápal–Wanless (2021) cited correctly as [DW21] in §1.1, §5, and §8.
- Cover letter's "Fallback unbundling" section (Part 1 → PLOS ONE, Part 2 → Linear Algebra and Its Applications) is a smart fallback structure.
- README §8 submission checklist still has unchecked boxes: cover-letter finalization and Brayden's referee-rigor pass. Confirm these are closed before submission.

### Journal-fit (honest-negative discipline)
The honest-negative discipline is genuinely good. Specifically:
1. The "specificity boundary" rhetoric is correctly reduced to the more conservative "specificity scoping result on this one family of trained transformer weights" (per §2.8 of the manuscript and the cover letter "Revisions" §5).
2. The post-hoc design of D5 and D4_eq is named in §3.3, in the abstract, in §4 limitations, and in the cover letter — four-way disclosure is exemplary.
3. The §4 "Not asserted" subsection is the most important paragraph of the paper, and is correctly placed (after the positive results, before the boilerplate).
4. The "PROVEN: None — this is an empirical-scoping paper, not a theorem paper" line in §5 is the right tone for *Stat Sci*: empirical work labeled as empirical work.
5. Tier-E framing has been translated out (per README §3 bullet "Tier-E framing translated"); the manuscript reads as standard statistical methodology now, not TIG-internal taxonomy.

The blockers are the J15-leftover file (MAJOR-1) and the title-scope tension (MAJOR-2). Once those are addressed, this is a defensible *Stat Sci* companion paper — the kind of negative scoping result the venue actively wants, framed with the post-hoc honesty its referees expect.

---

## Cross-paper summary

Both papers are credibility-builders done right: explicit retraction (J30), explicit post-hoc disclosure (J31), explicit limitations sections in both. The PROVEN/STRUCTURAL/EMPIRICAL/OPEN tier discipline is applied correctly in both manuscripts. Major issues are mechanical — verification-script mismatch (J30) and stray file (J31) — not content. Minor revision is appropriate for both. Once the mechanical issues are fixed, both are ship-ready for their respective venues, and both contribute to the J-series' credibility by demonstrating that the TIG corpus knows the difference between what it can prove, what it can compute, what it can rhyme, and what it has gotten wrong.
