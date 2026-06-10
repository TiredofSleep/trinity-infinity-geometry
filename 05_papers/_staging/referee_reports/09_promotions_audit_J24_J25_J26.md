# Ship-Readiness Audit — Tier-1 Promotions J24, J25, J26

**Papers reviewed:** J24 (Integers), J25 (Experimental Mathematics), J26 (LMP / JMP)
**Reviewer perspective:** portfolio-quality auditor; submission-readiness gate, not full per-line referee
**Date:** 2026-05-27
**Source commit:** post-renumbering (0d6d0f1); papers promoted from Tier 2 to Tier 1 (J01–J31 slot)
**Common substrate:** the discrete Fejer quotient $R(k,f) = \sin^2(\pi k/f) / (k^2 \sin^2(\pi/f))$

---

## J24 — The Discrete Fejer Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average

**Audit verdict:** Ready for rigor pass (strongest of the three; absorbing J41 was the right move).
**Estimated work to submission:** 4–8 hours (Brayden's referee-rigor pass + Integers style file). No fundamental gaps.
**Recommended venue:** *Integers — Electronic J. Combinatorial Number Theory* (correct fit). Backup: *Acta Arithmetica* or *Math. Magazine* (note-length).

### Content completeness
Full manuscript: 878 lines, 9 numbered sections, 7 theorems + 4 corollaries + 4 remarks + verification table. amsart format, complete bibliography (11 entries), §0 lens preamble, §1 tier-discipline paragraph, §9 explicit "what is not claimed" scope. All theorems carry full proofs (not sketches). No skeleton sections.

### Theorem strength
PROVEN: 7 theorems — closed form (Thm 3.1), full-period cancellation (Thm 3.2), First-G localization (Thm 4.1), obstruction-zero correspondence (Thm 5.1, central new contribution), synchronization (Thm 5.2), squarefree layered-divisor structure (Thm 6.1, $2^j-1$ count), continuum limit (Thm 7.1), corridor average $\to \mathrm{Si}(2\pi)/\pi$ (Thm 7.2). The substantive contributions (per the paper's own §1 self-positioning) are the obstruction-zero correspondence + Boolean-lattice $2^j - 1$ count + closed-form corridor average. Two corollaries (inclusion-exclusion identity, Euler-product asymptotic density) follow cleanly.

### Verification status
Two scripts (602-line `verify_J03.py` + 151-line `proof_first_g_event.py`), reported 10/10 PASS, max deviation $4.44 \times 10^{-16}$ for closed form, 22,367 (b,k) pairs zero counterexamples for First-G, 900/900 cell matches for obstruction-zero, corridor-average deviation $4.8 \times 10^{-5}$ at $f = 1000$. Convergence rates consistent with Riemann-sum theory.

### Novelty
Mixed but honest. Closed form (Thm 3.1) and continuum limit (Thm 7.1) are explicitly classical Fejer-kernel material; §1 calls them "included to make the paper self-contained." Full-period cancellation (Thm 3.2) and First-G localization (Thm 4.1) are one-line gcd consequences. The genuinely new content is (i) the spectral-product $f_b(k) = \prod_j R(k, p_j)$ as a continuous-in-$k$ indicator for $\gcd(k,b) > 1$, (ii) the $2^j-1$ Boolean-lattice count, (iii) the explicit $\mathrm{Si}(2\pi)/\pi$ evaluation of the corridor average via integration by parts. These are competent but elementary results — appropriate for *Integers*, which welcomes such notes.

### Coherence with sister papers (J24/J25 Fejer overlap)
This is the dominant J24 paper. J25 is the lighter "coordinate translation" cousin (see below).

### Key gaps
- Bibliography includes 11 entries but the Pomerance 1985 reference has a bibtex mismatch (entry says "Proc. Int. Congr. Math. 1995" — actually his 1985 ICM lecture vs 1995 Birkhauser printing). Fix bibitem.
- §1 still self-flags ~60% of the seven theorems as "elementary" or "classical." Integers is okay with this, but the cover letter must lead with the genuinely new spectral-product / Boolean-lattice / corridor-average package, not the closed form.
- The §9 OPEN questions (corridor-midpoint substrate question, Ramanujan-sum form of $f_b$) are honest but unmotivated for the Integers audience — consider tightening to one OPEN.

---

## J25 — First-Coprime-Failure and the Discrete Fejer Kernel: A Coordinate Translation across Squarefree Bases

**Audit verdict:** Needs substantive revision OR merger into J24. The honest accounting in §0 admits the paper is "packaging plus verification harness"; this is a transparent but borderline-publishable framing.
**Estimated work to submission:** As-is: 2–4 hours rigor pass. **Strong recommendation: merge with J24** — see below.
**Recommended venue (if kept separate):** *Experimental Mathematics* (correct fit for "verification harness as object of study"). Backup: *Math. Intelligencer* expository note.

### Content completeness
Full manuscript: 865 lines, 8 sections, 1 lemma + 2 theorems + 1 corollary. amsart, 12 bibliography entries, §0 tier discipline + lens, §7 scope. Proofs present and short (the synchronization is a 6-line proof; the closed form is 5 lines; the continuum limit is 8 lines). The §0 "Honest accounting of novelty" paragraph self-admits "The contribution of the present paper is the packaging plus the verification harness."

### Theorem strength
KNOWN (Lemma 3.1): closed form for $R(k,f)$ — explicitly attributed to Fejer 1900 / Apostol §11.5 / Iwaniec-Kowalski §1.7 / Oppenheim-Schafer §3.8 in §0. PROVEN: Thm 4.1 (Eratosthenes synchronization — Remark 4.2 self-labels it "a tautology, recorded for clarity"), Thm 5.1 (continuum identification — standard discrete-to-continuum Fejer-kernel limit), Cor 4.3 ($\omega$-blindness — one-line consequence of closed form). Net new mathematical content: essentially the verification harness count (712 checks) + the structural-rhyme remark on Montgomery pair correlation.

### Verification status
207-line script `verify_prime_phase_transition.py`, reported PASS: 712 algebraic checks (106 closed form + 561 sync + 42 omega + 3 continuum), max deviation $1.11 \times 10^{-16}$, runtime ~30s. Clean.

### Novelty
This is the weakest of the three on novelty. The paper itself classifies its central claims as one KNOWN lemma + one synchronization theorem (Remark 4.2: "a re-coordinatization, not a non-trivial coincidence") + one omega-blindness one-liner + one standard continuum limit. The §6 Montgomery-pair-correlation remark is correctly disclaimed ("a coincidence reflecting the universality of the rectangular spectral window common to both contexts").

### Coherence with sister papers (J24/J25 Fejer overlap)
**STRONG overlap with J24.** Compare:
- J24 Thm 3.1 closed form = J25 Lemma 3.1 closed form (identical proof, identical statement).
- J24 Thm 4.1 First-G localization = J25 Thm 4.1 Eratosthenes synchronization (J25 is the coordinate-translation reading of the same fact).
- J24 Thm 7.1 continuum limit = J25 Thm 5.1 continuum identification (identical claim, identical proof up to notational variants).
- J24 Cor 5.3 inclusion-exclusion + Cor 5.4 asymptotic density partially subsumes J25 Cor 4.3 omega-blindness.

J25's distinct content: (i) the Montgomery pair-correlation remark in §6, (ii) the verification-harness framing (712 vs J24's 22,367 numerical claim), (iii) Cor 4.3 $\omega$-blindness as a stand-alone statement, (iv) Remark 4.5 ring-structure-detection consequence.

### Key gaps
- The paper's existence is essentially predicated on the J25 ≠ J24 distinction. After J24 absorbed J41, J25 is now a ~10-page note whose three theorems are all either explicitly KNOWN (Lemma 3.1) or "coordinate translations" of J24's results (Thms 4.1 / 5.1).
- Bibliography references `J04Sanders` as the "First-G Localization Lemma" companion — but post-merger that companion is J24 itself, not J41. Citation needs update.
- The 712-vs-36,662 reconciliation paragraph (§0) is honest but signals to a referee that the verification corpus has been disaggregated for paper count.

### MERGER RECOMMENDATION
**Strong recommendation: roll the J25-distinct content (Montgomery remark + omega-blindness corollary + ring-structure-detection remark) into J24 as a single appendix section (~3 pages); retire J25.** Rationale:
1. J24's §5 (spectral characterization, obstruction-zero correspondence, Cor 5.3 inclusion-exclusion, Cor 5.4 asymptotic density) already provides the structurally stronger framework that J25's "coordinate translation" reads off as a special case.
2. The Montgomery-pair-correlation remark is a 1-paragraph item, not a paper-justifying contribution.
3. *Experimental Mathematics* has a high bar; a "packaging + verification harness" paper whose three theorems are all elementary will struggle to clear it, while *Integers* will happily host the merged J24 with an explicit "harmonic side" subsection.
4. The post-merger J24 already has 7 theorems + verification on ~25 pages — adding 3 more pages keeps it within Integers length range.

**If retained separately:** rewrite the cover letter to lead with the Montgomery rectangular-window remark (the only genuinely-distinct contribution), and acknowledge J24 as the "spectral-side companion" with J25 as the "arithmetic-coordinate companion."

---

## J26 — A Discrete sinc² Identity in Finite-Dimensional Quantum Mechanics

**Audit verdict:** Needs substantive revision (QM framing is thin; mathematical content overlaps J24).
**Estimated work to submission:** 6–10 hours (rebuild QM motivation; clarify what's distinct from J24's continuum limit). Tier 1 promotion is defensible if the QM application is hardened.
**Recommended venue:** *Letters in Mathematical Physics* (per the README — JMP per-venue cap reached). Backup: *J. Phys. A: Math. Theor.* Concerns about CMP / JMP standards if positioning isn't sharpened.

### Content completeness
Full manuscript: 496 lines (shortest of the three), 7 sections, 2 theorems + 2 propositions + 1 corollary + 1 lemma. amsart, 12 bibliography entries (better-curated than J25 — includes Schwinger 1960, Wootters 1987, Vourdas 2004/2017 as finite-QM foundations). §0 lens, §7 tier discipline. Proofs all present and short (1–8 lines each). Markdown version `J15_DiscreteSinc2_QM_JMathPhys.md` is the source.

### Theorem strength
PROVEN: Thm 3.1 (closed form = J24's Thm 3.1, identical proof), Prop 4.1 (squared overlap — the QM-specific reading), Cor 4.2 (first zero at $k = f$ for every $f \ge 2$ — slightly stronger than J24's Thm 3.2 statement in that the "every $f$" framing is preserved without squarefree restriction), Thm 4.3 (continuum limit = J24's Thm 7.1), Prop 5.1 (synchronization with First-G — restates J24 Thm 4.1 + Cor 4.2 = J25 Thm 4.1).

### Verification status
85-line script `verify_J42_sinc2.py` (smallest of the three). Reported PASS at machine precision (max deviation $3.33 \times 10^{-16}$), $\sinc^2(1/10)$ closed form $25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675$ correctly verified (decimal error in earlier draft is documented in acknowledgments — credit to honest revision discipline).

### Novelty
**The only genuinely-new content vs J24/J25 is the QM-on-$\mathbb{Z}/N\mathbb{Z}$ framing** in §2 (position/momentum bases on cyclic group, normalized window state $|w_k\rangle$, squared overlap $|\langle \hat p | w_k\rangle|^2 = (k/N) R(k,f)$) and the interpretive paragraph in §4.1 ("Note on interpretation") fixing a misreading in an earlier draft (the overlap is fidelity, not the position-marginal probability $k/N$). The mathematical engine — closed form, first-zero theorem, continuum limit, First-G synchronization — is the J24/J25 engine.

This is borderline. The QM reading is a legitimate application but it's a 1-section application (§2 + §4) of an identity that is otherwise classical Fejer + J24's spectral content. The Schwinger-1960 / Wootters-1987 / Vourdas finite-QM literature has Fourier-on-cyclic-group machinery; the present "discrete sinc² in finite QM" framing is reasonable but is a re-presentation of standard finite-QM Fourier analysis with the arithmetic synchronization bolted on. **LMP referees will ask: what is the QM consequence beyond the kinematic identity?**

### Coherence with sister papers (J24/J25 Fejer overlap)
- Thm 3.1 closed form = J24 Thm 3.1 = J25 Lemma 3.1 (identical).
- Thm 4.3 continuum limit = J24 Thm 7.1 = J25 Thm 5.1 (identical proof).
- Prop 5.1 First-G synchronization = J24 Thm 4.1 + Cor 4.2 = J25 Thm 4.1 (essentially the same statement).
- Cor 4.2 (first zero at $k = f$, no primality) is the "every $f \ge 2$" reading of J24 Thm 3.2.

The genuinely J26-specific content: §2 (QM Hilbert-space setup), Prop 4.1 (squared overlap with normalized window), the §4.1 "Note on interpretation" disambiguating fidelity vs position marginal, the §4.3 $\sinc^2(1/10)$ Ptolemy-pentagon exact-value remark. Roughly 4–6 pages of distinct content.

### Key gaps
- The QM framing needs strengthening. Currently §2 + §4 set up the finite-QM kinematic identity but do not derive a QM-application consequence (scattering, measurement statistics, time evolution). For LMP, a one-paragraph "this is a useful identity in finite-QM scattering problems" should become a worked example with a specific Hamiltonian.
- §5 (First-G synchronization) is essentially a citation of J24 / J25; it could be reduced to a one-paragraph "Remark — arithmetic side" referencing the companion paper.
- The Schwinger / Wootters / Vourdas citations are not engaged in the body of the paper; they appear only in the bibliography. Either engage them (where in Vourdas 2017 does this overlap appear, and why is the present statement new?) or drop them.
- Acknowledgments still mention "Anthropic Claude sessions in 2026" — the AI-attribution removal directive (per J24/J25 hardening) was not applied here. Should be stripped before submission.

---

## Cross-paper summary and merger recommendation

All three papers have the same closed-form identity $R(k,f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ — the discrete Fejer kernel — as their mathematical engine. They differ in framing:
- **J24:** spectral product $f_b(k)$, Boolean-lattice $2^j - 1$ count, $\mathrm{Si}(2\pi)/\pi$ corridor average. Number-theoretic.
- **J25:** "coordinate translation" reading + verification harness + Montgomery rectangular-window remark. Experimental.
- **J26:** finite-QM on $\mathbb{Z}/N\mathbb{Z}$ overlap interpretation + Ptolemy-pentagon exact value. Mathematical physics.

J24 is the strongest and stands as a clean *Integers* submission. J25's distinct content (Montgomery remark, $\omega$-blindness corollary) is best folded into J24 as a 3-page appendix. J26 stands as a separate submission only if the QM framing is hardened with a concrete application (scattering / measurement / Hamiltonian example).

**Recommended portfolio configuration:**
- **J24:** ship to *Integers* after rigor pass + bibliography fix + cover letter rewrite to lead with the spectral product / Boolean lattice / corridor average. **Tier 1 confirmed.**
- **J25:** merge into J24 as appendix; retire as a standalone paper. **Demote from Tier 1.**
- **J26:** keep separate, but rebuild §4 + §5 to lead with the squared-overlap QM application (Prop 4.1 is the central novel claim) and de-emphasize the J24-overlapping closed form. **Tier 1 conditional on QM hardening.**
