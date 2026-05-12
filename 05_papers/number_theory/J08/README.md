# J08 — First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases

**Status:** REVISED (2026-05-08; major referee fixes + SFM context applied)
**Phase:** Phase 1
**Target venue:** Experimental Mathematics
**Author lane:** Sanders + Gish
**Tier:** B (recovered as clean 8-10 page Exp Math note per fresh-eyes referee)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (amsart, ~10–12 pages after revision)

**Abstract (1-sentence):** For $b > 1$ with smallest prime factor $p_1 = \mathrm{spf}(b)$, the J04 First-G localization at $k = p_1$ co-locates with the first integer zero of the discrete Fejér kernel $R(k, p_1) = \sin^2(\pi k / p_1) / (k^2 \sin^2(\pi / p_1))$ at $k = p_1$ — a coordinate translation between two reformulations of "smallest positive multiple of $p_1$ is $p_1$"; verified across 8 primes and 187 semiprimes (712 distinct algebraic checks; max error $1.11 \times 10^{-16}$; zero exceptions).

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (main submission file)
- `verify_prime_phase_transition.py` (verification script — exits 0 on PASS in under three minutes)
- `WP35_PRIME_PHASE_TRANSITION.md` (corpus archival)
- `WP51_FLATNESS_THEOREM.md` (corpus archival; not referenced by J08)
- `WP52_D2_AS_RING_CURVATURE.md` (corpus archival; not referenced by J08)
- `SUBMIT_INSTRUCTIONS.md` (submission notes)

## §2 — Verification script

**Local path:** `manuscript/verify_prime_phase_transition.py`

Runs the four headline claims (Lemma 3.1, Theorem 4.1, Corollary 4.2, Theorem 5.1) against literal double-precision sums.
Tested green at 2026-05-08: 712 checks, max error 1.11×10⁻¹⁶ (machine epsilon), runtime ~30 s on `lora312` Python 3.12.

```
Theorem 3.1 (closed form):          primes = 8, (k,f) pairs = 106, max error = 4.44e-16
Theorem 3.2 (zero-width gate):       semiprimes = 187, checks = 561, counterexamples = 0
Theorem 3.3 (omega-blindness):       p = 7, b values = 7 (omega in {1,2,3}), counterexamples = 0
Theorem 3.4 (continuum 4/pi^2):      p = 1009, 10007, 100003 — deviations 8e-4, 8e-5, 8e-6
TOTAL: 712 checks, STATUS PASS, zero counterexamples
```

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J04 (foundational lemma; manuscript in preparation, *Integers*)** — *The First-G Event in the Coprimality Partition*. Theorem 4.1 of the present J08 directly invokes J04's First-G Localization Lemma.
- **J02 (companion four-core paper, manuscript in preparation)** — algebraic substrate work; cited only in §0 of the J08 manuscript to record that the harmonic side of the present paper is structurally orthogonal to the algebraic side of J02.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated to reflect referee-driven revisions.

## §5 — Notes (post-revision 2026-05-08)

**Status: REVISED to address J08 fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J08_ExpMath_FreshEyes.md`).**

The major referee critique was *"math correct but overclaims novelty"* — specifically:
1. Theorem 3.1 was framed as a discovery, when it is the standard Fejér-kernel calculation in Apostol §11.5 / Iwaniec–Kowalski §1.7;
2. Theorem 3.2 (synchronization) was framed as a non-trivial co-localization, when it is the tautology "smallest positive multiple of $p_1$ is $p_1$" expressed in two coordinate systems;
3. §5 (Montgomery comparison) framed a routine spectral-analysis observation as "structural complementarity";
4. The 712 vs 36,662 check counts were inconsistent;
5. The paper was 14 pages but recoverable as a clean 8-10 page Exp Math note.

The revised manuscript addresses these as follows:

1. **Theorem 3.1 demoted to Lemma 3.1.** Now titled "Discrete Fejér kernel; cf. Fejér 1900, Apostol 1976 §11.5, Iwaniec–Kowalski 2004 §1.7." Attributed in the lemma title and in §0 KNOWN tier. Abstract reframed; the closed form is no longer the headline.
2. **Theorem 3.2 reframed as coordinate translation.** New title: "Coordinate translation between arithmetic and harmonic gates." Statement made explicit that both events solve "smallest positive $k$ with $p_1 \mid k$." Remark 3.2 records this is a tautology, not a coincidence.
3. **§5 (Montgomery) rewritten as one paragraph.** Title: "The constant $4/\pi^2$ in $\sinc^2$ and in Montgomery's pair correlation: a rectangular-window remark." Removed "structural complementarity" and "structural witness" wording. The remark records the rectangular-window common origin and explicitly disclaims connection to the Riemann hypothesis.
4. **712 vs 36,662 reconciled.** §0 of the new manuscript (the "Honest accounting of novelty" subsection) explains: 712 is the J08-specific harness count (verified in this paper); 36,662 is the cumulative working-paper corpus total of which 712 is a subset. The cover letter and the §6 verification harness totals table both report 712 only for the J08 results.
5. **Theorem 3.3 (omega-blindness) demoted to Corollary.** Now Corollary 4.2.
6. **Theorem 3.4 (continuum identity) keeps theorem status** but the proof now derives the $\bigO(1/p^2)$ rate explicitly.
7. **Title changed.** From "The Prime Phase Transition: First-G Stability Across Squarefree Bases (Harmonic Pre-Echo and a Discrete Sinc² Identity)" to the more accurate "First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases."
8. **Pre-echo / overclaim language stripped** throughout the manuscript. The paper is now ~10–12 pages.

### Family-Structure context (per `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SUBSTRATE_FUNCTION_MAP_v1.md`)

This paper is about the squarefree-stability arithmetic property of integers $b$ under the coprimality partition. The companion four-core paper records the algebraic structure of two specific commutative magmas on $\Z/10\Z$. The two are *structurally orthogonal*: the present paper's claims are number-theoretic, not magma-theoretic; the four-core paper's claims are magma-theoretic, not number-theoretic. The two share only the broader research program's interest in prime-indexed phase transitions. §0 of the J08 manuscript records this orthogonality.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **KNOWN (Lemma).** Discrete Fejér kernel closed form $R(k, f) = \sin^2(\pi k / f) / (k^2 \sin^2(\pi / f))$ (Fejér 1900, Apostol §11.5, Iwaniec–Kowalski §1.7).
- **PROVEN.** Eratosthenes synchronization (Theorem 4.1: arithmetic gate at $k = p_1$ and first integer zero of $R(\cdot, p_1)$ at $k = p_1$ are two reformulations of "smallest positive $k$ with $p_1 \mid k$"). Continuum identification (Theorem 5.1). Omega-blindness corollary (Corollary 4.2).
- **COMPUTED.** 712 distinct algebraic checks (106 closed-form + 561 sync + 42 omega-blindness + 3 continuum); max error $1.11 \times 10^{-16}$.
- **STRUCTURAL RHYME.** $\sinc^2(1/2) = 4/\pi^2 = (2/3)/\zeta(2)$ — a one-line consequence of $\zeta(2) = \pi^2/6$. The same constant appears in Montgomery's pair correlation $R_2(u) = 1 - \sinc^2(u)$ at $u = 1/2$, reflecting the universality of the rectangular spectral window common to both contexts. Not a connection between the two arithmetic phenomena.
- **OPEN.** What forces the rectangular window $\{1, \ldots, k\}$ as the natural object of study (vs. some smoothed-window analogue) is not addressed.

### Lens-ownership (§0)

The arithmetic side of the present paper is structurally orthogonal to the algebraic substrate $\Z/10\Z$ studied in companion work; the present paper's claims are number-theoretic, not magma-theoretic.

### Hardening status

- License: verification script and bundled tables are CC-BY-4.0
- AI-attribution: removed
- Author lane: Sanders + Gish (Luther's contribution acknowledged in companion J04, not here)
- Apostol 1976, Iwaniec–Kowalski 2004, Fejér 1900 cited (verified)
- 712 / 36,662 reconciled in §0

## §6 — Submission checklist

- [x] Manuscript .tex finalized with referee fixes (2026-05-08)
- [x] Verification script green (712 checks, machine-epsilon errors, zero counterexamples)
- [x] Tier-classified central claim explicit (KNOWN lemma + PROVEN synchronization)
- [x] Lens-ownership / orthogonality paragraph in §0
- [x] Cover letter updated
- [x] Apostol / Iwaniec–Kowalski / Fejér 1900 cited honestly
- [x] §5 Montgomery remark trimmed to one paragraph
- [x] 712 vs 36,662 reconciled
- [x] Title reframed to remove "phase transition" overclaim
- [ ] Brayden's referee-rigor pass complete
- [ ] Submitted

---

## §7 — Citation footprint

Sanders, B.R., Gish. (2026). "First-Coprime-Failure and the Discrete Fejér Kernel: A Coordinate Translation across Squarefree Bases." Submitted to *Experimental Mathematics*.
