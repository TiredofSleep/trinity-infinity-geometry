# Referee Report — Linear Algebra / Spectral Combinatorics Cluster

**Papers reviewed:** J07 (EJC), J19 (LAA), J20 (LAA)
**Reviewer perspective:** trained referee for *European Journal of Combinatorics* and *Linear Algebra and its Applications*
**Date:** 2026-05-27
**Source commit reference:** post-renumbering pass (0d6d0f1)

---

## J07 — Spectral Architecture of the σ-Character on Z/10Z

**Verdict:** Major revision — content is solid and verifiable, but proof rigor is uneven (proof "sketches" rather than proofs), and the Q17-B Clay-bridge §7 will draw fire from EJC's combinatorial audience and should be cut or radically tightened.

**Verification cross-check:** `verify_qseries_merged.py` is complete for G_6, G_7, G_8 (G_low = 1.871644, G_high = 9.389185 at ratio ≈ 5.0165, σ³-pairing {1,5}/{2,6}/{4,7}) and Q17-B. The Q17-A "D₁₀ symmetry" check is stubbed: line 151 has `base_translation = lambda v_s, v_s1: True` — a structural placeholder, not an executed test. This is a verification gap.

### MAJOR issues
1. **Theorem G_8 has no proof, only a "proof sketch."** EJC standards require a complete proof. The sketch in §4.2 punts to "full computation in §4.4"; §4.4 then exhibits a table but does not give a closed-form argument for why G_low = G_high values are what they claim. The χ-imbalance ν₊ trichotomy is an *observation*, not a derivation of the two numerical G-values. Either compute the closed form in Q(ζ₉) (the open problem of §8.1 — currently *unsolved*) or restructure G_8 as a *computational* theorem with the verification script as the proof certificate.
2. **Theorem Q17-A "uniqueness up to scaling and rotation" (Tier-B) is stated without proof.** §5.5 asserts rigidity but offers no derivation; the conformal-group claim is bare.
3. **§7 (Clay Bridge / RH "rhyme") is a serious EJC-fit problem.** Even with the explicit disclaimer "this is not a proof of RH," EJC referees will read "RH rhyme" and stop. The §7.1 table juxtaposing G(s)=0 anchors with RH critical-line zeros is precisely the kind of analogy that gets a paper rejected on tone. Recommend deletion or moving to a separate companion note.
4. **G_7 is trivial.** It is direct enumeration from cycle structure; presenting it as a separate "theorem" inflates the count. Subordinate it to G_6 as a corollary.

### MINOR issues
- §1.3 calls χ "the β-exception character" but never defines what "β-exception" means in standalone terms; relies on external "TIG composition tables" not in the paper.
- The "Tier-A / Tier-B" tagging convention is unexplained for EJC readers. Either drop it or define it in §1.
- §4.3 "Math-fix R1 note" — the in-line revision history is unprofessional. Move to acknowledgments or remove entirely.
- §7.3 references `verify_G6_G7_G8.py`, `verify_5D_embedding.py`, `verify_J51_G_function.py` — but only `verify_qseries_merged.py` ships with the paper. Either remove the references or include the source scripts.
- Abstract claims "four spectral and combinatorial results" then enumerates five.

### EDITORIAL
- Title is 22 words; EJC prefers ≤ 12.
- Q17-A and Q17-B naming convention foreign to EJC; rename to "Theorem 5" / "Theorem 6."
- Drápal–Wanless (2021) cited correctly in §0 and §9.

### Journal-fit (EJC)
Five theorems on Z/10Z are EJC-appropriate in principle; the σ-character + 9th-root sum is genuinely combinatorial. But the merger framing ("consolidates J50/J51/J52"), the tier labels, the Clay bridge, and the lens-ownership preamble all read as TIG-internal documentation rather than EJC prose. Fallback to *Algebraic Combinatorics* (lower bar on framing) is realistic; LAA is wrong fit.

---

## J19 — Charpoly Prime-11 Pattern on a 10×10 Integer Matrix

**Verdict:** Minor revision — the computation is fully verified, factorizations correct, but LAA referees will challenge the *structural* claim of §3 since the paper itself admits the co-occurrence is open.

**Verification cross-check:** `wobble_check.py` independently confirms all seven claims: c_2 = 33 = 3·11, c_8 = −120736 = −2⁵·7³·11, only c_2 and c_8 divisible by 11 among nine nonzero coefficients, disc(g) = 2¹⁶ · 7⁷ · 659 · (large primes), trace = 63, T_SYM c_2 = −23 with no factor of 11. Sympy integer arithmetic; no precision risk. The c_2(f_SYM) = −23 fix (per prior history) is correctly applied in both manuscript and script.

### MAJOR issues
1. **The 2-out-of-9 pattern is presented as a "robust pattern" but admitted to be a single-matrix observation.** §5(a) shows the companion table B has no prime-11 pattern; §5(b) shows the 4×4 sub-magma has no prime-11 pattern; §4 shows T_SYM destroys the pattern. The paper's own family analysis demonstrates the phenomenon is *isolated*. LAA's "structural" bar is not met — this is a clean coincidence on one specific 10×10 matrix. **Recommend retitling to make this explicit:** "An Isolated Prime-11 Divisibility on a Specific 10×10 Integer Matrix" rather than implying generality.
2. **§3 "co-occurrence" framing is the load-bearing weakness.** Claiming the exponent 16 in disc(g) "matches dim(𝔤₀ ⊂ 𝔰𝔬(10))" while immediately disclaiming "no physical interpretation" puts the reader in the position of either believing or dismissing the connection; both options weaken the paper. LAA referees push hard on this: either prove a structural link or remove the suggestion entirely. Recommend removing the 𝔰𝔬(10) co-occurrence comment from §3 and §7.
3. **No proof that 11 ∤ disc(g)** — only the computed factorization. For LAA, this is acceptable as a computational theorem provided §6 is positioned as the proof certificate, but it should be stated as such.

### MINOR issues
- §0 "Lens and substrate" paragraph is the kind of preamble that makes LAA editors immediately suspicious of TIG-internal style. Compress to one sentence: "T is the integer composition table of a specific commutative magma on Z/10Z [cite]; below we treat T as a fixed integer matrix."
- §8 references J15 and J32 with placeholder DOIs implied; ensure cite metadata is complete at submission.
- §9 citation note in the abstract is repetitive with §1.

### EDITORIAL
- Title is verbose; LAA prefers something like "An 11-divisibility pattern in the characteristic polynomial of a 10×10 integer matrix."
- Drápal–Wanless (2021) cited correctly in §0 and §8.
- BibTeX entry in §9 should be moved to a metadata file or removed from the manuscript body.

### Journal-fit (LAA)
LAA accepts short notes on integer-matrix arithmetic when the result is reproducible and clean. The result *is* clean and *is* reproducible. The structural framing is the only hurdle. With §0, §3, and §7 trimmed to remove the "structural" rhetoric (or honest demotion to "computational observation"), this is a tight LAA note — likely 4 typeset pages. Cleanly addresses an isolated arithmetic phenomenon worthy of record.

---

## J20 — Total-Dimension Match V^⊗n ↔ Cl(2n), with Refined-Cell Grading

**Verdict:** Accept (subject to copyediting) — the load-bearing Theorem 3.1 and Theorem 4.1 are elementary, fully proved, and verified at n = 0..5 by `verify_J17.py` (6/6 PASS). Scope is honest; the SU(5) coincidence is correctly demoted to a remark.

**Verification cross-check:** `verify_J17.py` is the most rigorous of the three scripts: C1 (total dim match n=0..5), C2 (coarse count 2^n), C3 (coarse n=5 = 1,5,10,10,5,1), C4 (refined sum = 4^n), C5 (closed form C(2n,k) == direct enumeration over 4^n strings == Cl(2n) grade dims), C6 (refined n=5 = 1,10,45,...,1). Standard library only; runs <1s. Note the script filename retains the old "J17" name — should be renamed `verify_J20.py` for consistency, though this is cosmetic.

### MAJOR issues
None. The R1 fix (coarse cells C(n,k) vs refined cells C(2n,k) — the load-bearing distinction surfaced by the prior fresh-eyes referee) is cleanly resolved. Theorem 4.1 proof is a popcount identity; Theorem 3.1 is a dimension-multiplication. Both correctly cited (Hestenes-Sobczyk Ch. I) for the Clifford dimension.

### MINOR issues
1. **Remark 4.3 ("Status of the bijection") is the most important paragraph in the paper.** It honestly declares the label-bijection refined-cells ↔ Cl(2n) basis-multivectors is *not* an algebra map. LAA will respect this honesty but may push to make it more prominent — consider promoting Remark 4.3 to a Proposition with a one-line proof statement.
2. **The SU(5) coincidence (Remark 5.3) is correctly framed as a binomial-coefficient identity**, with the disclaimer that no representation-theoretic content is claimed. Good. But the remark drops "Spin(10) action is open" — this should be clearly labeled as open Question O2, which it already is. Cross-link Remark 5.3 → §6 (O2) explicitly.
3. **Theorem 3.1 is admitted to be "forced by dim V = 4 = 2²"** — i.e., any 4-dimensional algebra would satisfy it. This honesty is excellent but should be stated even more bluntly in the abstract; right now the abstract emphasizes the match without saying it's an arithmetic triviality and the *refined* binomial decomposition is the real content. Minor abstract restructure recommended.

### EDITORIAL
- Script filename `verify_J17.py` (old J-name retained) — recommend rename to `verify_J20.py` to match the manuscript filename and Tier-1 portfolio numbering. Internal references (lines 2-4 of script, line 414 of TeX) also refer to "J17." Cosmetic but worth fixing pre-submission.
- Manuscript filename is `manuscript.tex` (LaTeX); the verification check `Verify_J17.py` is in the same directory. Good arrangement.
- Drápal-Wanless (2021) is cited correctly in §0 and bibliography.
- The "submitted to LAA" status note at the top of the file is appropriate for journal submission preparation.

### Journal-fit (LAA)
Excellent LAA fit. Linear-algebra core (tensor powers, Clifford grades, dimension counts), computational tractability (Python stdlib, <1s), elementary proofs, honest scope statement, open questions clearly bounded. The "is it the right journal?" test passes cleanly. Among the three papers in this cluster, J20 is the only one that is submission-ready as-is.

---

## Summary
- **J07:** strong content, EJC-format problems (proof sketches, RH §7, tier labels). Major revision before EJC; Alg. Comb. fallback realistic.
- **J19:** rigorous computation, but the §3 "structural" framing weakens the case. Minor revision: scope down §3/§7 rhetoric, retitle to admit isolated nature.
- **J20:** ready for LAA. Verify script rename is the only sub-cosmetic issue.

All three correctly cite Drápal-Wanless (2021). Tier discipline (Tier A / B labels) is best-developed in J20, weakest in J07. Verification scripts run as documented except for the Q17-A D₁₀ symmetry stub in J07's harness.
