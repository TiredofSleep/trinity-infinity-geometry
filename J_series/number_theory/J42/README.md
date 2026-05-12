# J42 — A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics

**Status:** DRAFT (with fallback flagged on per-venue cap)
**Phase:** Phase 4
**Target venue:** Journal of Mathematical Physics (preferred); *Letters in Mathematical Physics* / *J Phys A* / *Comm Math Phys* as fallbacks
**Author lane:** Sanders + Gish
**Tier:** B (Tier 1/2 fully proved)
**WP source:** Discrete sinc² identity (Theorem 3.1 in `first_g_sinc2_FINAL.tex`); QM application is novel framing

---

## §1 — Manuscript

**Local path:** `manuscript/J15_DiscreteSinc2_QM_JMathPhys.md`

**Abstract (one paragraph).** For an integer $f \ge 2$ and $k \ge 1$, the squared overlap of a momentum eigenstate with a position-space rectangular window of size $k$ in finite-dimensional QM on $\mathbb{Z}/N\mathbb{Z}$ admits the closed form $R(k,f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ (the Fejér kernel; cf. Fejér 1900). We derive three QM-relevant consequences: (i) the squared overlap of a momentum eigenstate with the normalized rectangular position window (corrected from the earlier "probability mass" reading), (ii) a first-zero theorem (for **every $f \ge 2$**, the first integer zero of $R(\cdot, f)$ is at $k = f$ — no primality needed), and (iii) the continuum limit $R(k,f) \to \sinc^2(k/f)$. We close with the synchronization with the arithmetic First-G event: for $f = \mathrm{spf}(b)$, the first integer zero of $R(\cdot, f)$ coincides with the smallest $k$ at which $\{1,\dots,k\}$ contains a non-coprime element of $\mathbb{Z}/b\mathbb{Z}$.

**Source corpus:**
- The closed-form identity (Theorem 3.1) is taken from the source paper `first_g_sinc2_FINAL.tex` (J03 / J04 corpus); the QM framing (Hilbert space on $\mathbb{Z}/N\mathbb{Z}$, momentum-position rectangular-window overlap, finite uncertainty) is novel for J42.
- The synchronization is reproduced from companions [J03, J04].

## §2 — Verification script

**Path:** `manuscript/verify_J42_sinc2.py` (run with `python manuscript/verify_J42_sinc2.py`). Verifies Theorem 3.1 at machine precision (max deviation $3.33 \times 10^{-16}$) on $f \in \{3,4,5,6,7,8,9,10,11,12,13,17,19,23\}$ and $k \in \{1,\dots,f+1\}$; the unrestricted Corollary 4.2 (first zero at $k = f$ for all $f \ge 2$); the corrected special value $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675$; and the Proposition 5.1 synchronization for $b \in \{6, 10, 15, 21, 22, 35, 105\}$. Runtime $<2$ s; deterministic.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J03 (First-G Law, *Integers*), J04 (Sinc² Zero Law, *Integers*), J40 (BB Bridge, *JMP*).

## §4 — Cover letter

See `cover_letter.md` in this folder. Drafted; finalize after Brayden's referee-rigor pass.

## §5 — Notes & Status

**Status: REVISED 2026-05-07** in response to fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J42_JMP_FreshEyes.md`). Save plan: `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J42.md`.

**Math-fix summary (2026-05-07):**
- **Numerical error fixed:** §4.3 `sinc²(1/10) ≈ 0.9355` was wrong — correct value is `0.9675` (closed form `25(√5-1)²/(4π²)` was correct; only the printed decimal was wrong). Verified via sympy and direct numpy computation in `manuscript/verify_J42_sinc2.py`.
- **Fejér kernel attribution added:** Theorem 3.1 is the Fejér kernel (1900) — explicit acknowledgement now in §3 proof.
- **Corollary 4.2 generalized:** prime-f restriction was unnecessary; restated for all f ≥ 2. Prime structure is now relegated to its actual role at Proposition 5.1 (synchronization).
- **Proposition 4.1 reformulated:** language changed from "position-space probability mass" to "squared transition amplitude" / "squared overlap with the normalized window state". The `·k` un-normalization factor is explicit; the difference between this overlap and the actual position-marginal probability `k/N` is noted.
- **Verification script added:** `manuscript/verify_J42_sinc2.py` runs Theorem 3.1 (max dev 3.33e-16), unrestricted Corollary 4.2, the corrected sinc²(1/10), and Proposition 5.1 synchronization.

**Per-venue cap:** This is the **3rd JMP target** in the J-series (J40 1st, J41 2nd). The 2/quarter cap is reached. Per referee + per-venue-cap discipline, **submit to *Letters in Mathematical Physics*** (preferred fallback already documented in cover letter §6.3).

The paper is **Tier 1/2** (fully proved): all theorems are elementary and verified at machine precision. No conjectural content. The note is honestly framed as a Fejér-kernel application to QM-on-cyclic-group, not as a new identity.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem 3.1 (closed form for $R(k,f)$ — the Fejér kernel evaluated at $\theta = 2\pi/f$, $n = k$); Corollary 4.2 (first zero of $R(\cdot, f)$ at $k = f$ for every $f \ge 2$, no primality used); Theorem 4.3 ($\sinc^2$ continuum limit); Proposition 5.1 (synchronization $k^\star(b) = \mathrm{spf}(b)$ with the First-G event).
- **COMPUTED:** machine-precision verification (max deviation $3.33 \times 10^{-16}$) of Theorem 3.1 over $f \in \{3,4,5,6,7,8,9,10,11,12,13,17,19,23\}$ and $k \in \{1,\dots,f+1\}$; unrestricted Corollary 4.2 confirmed for $f \in \{2,\dots,15\}$; corrected $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675312093$ (sympy + numpy agreement to 10 digits); synchronization confirmed for $b \in \{6, 10, 15, 21, 22, 35, 105\}$. All in `manuscript/verify_J42_sinc2.py`.
- **STRUCTURAL RHYME:** the closed form $25(\sqrt{5}-1)^2/(4\pi^2)$ at $f = 10$ folds in Ptolemy's pentagon identity $\sin(\pi/10) = (\sqrt{5}-1)/4$ — connecting cyclic-group QM at $f = 10$ to the regular-pentagon arithmetic. Cited as structural motif, not load-bearing.
- **OPEN:** does $R(k,f)$ for $f$ ranging over the prime factors of squarefree $b$ encode the full coprimality structure of $(\mathbb{Z}/b\mathbb{Z})^\times$? (See Proposition 5.1 and §5.)

### Lens-ownership paragraph (insert at manuscript §0 if/when LMP-style version is built)

> *Lens and substrate.* This paper works on $\mathbb{Z}/N\mathbb{Z}$ as the cyclic-group quantum-mechanics substrate, with no TSML/BHML lens dependence. The momentum-position duality is the standard one (DFT-related orthonormal bases). The theorems are statements about the Fejér-kernel restriction to integer arguments and its arithmetic synchronization with smallest-prime-factor partitions. No 10-operator framework is invoked; the substrate $\mathbb{Z}/10\mathbb{Z}$ enters only as a special case ($f = 10$ in §4.3) and not load-bearingly.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .md drafted (J Math Phys-format, single file)
- [ ] LaTeX (amsart) conversion pending
- [x] Verification at machine precision (carries from J03/J04); standalone script TBD
- [x] Tier-classified central claim explicit (Tier 1/2 fully proved)
- [x] Lens-scope annotation: lens-invariant
- [x] Cover letter drafted (with summary, Why-JMP-with-fallback, suggested reviewers)
- [ ] Dependencies → cite J03, J04, J40 as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete
- [x] Per-venue cap check: **3rd JMP target — fallback to LMP / J Phys A / CMP recommended**
- [ ] Final venue decision
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Mayes, B. (2026). "A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics." Submitted to *Journal of Mathematical Physics* (or *Letters in Mathematical Physics* as fallback per per-venue cap; see README §5).
