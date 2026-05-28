# J25 → J24 Merger Plan

**Date:** 2026-05-28
**Status:** Plan only; merger NOT yet executed.
**Predicate audit:** `09_promotions_audit_J24_J25_J26.md` (2026-05-27)
**Decision:** J25 demoted from Tier 1; distinct content folded into J24 as a small appendix; J25 standalone manuscript tombstoned in place (README already marked MERGED at `05_papers/number_theory/J25/README.md`).

This plan inventories the J25 manuscript content, identifies where each piece lands in J24, lists what J24 already covers and what should be discarded, gives a five-step migration sequence, cross-references the J25 README tombstone, and lists residual risks.

---

## §1. Inventory of J25 content

Source: `05_papers/number_theory/J25/manuscript/manuscript.tex` (865 lines, amsart, 12 bib entries).

| J25 element | Line refs | Statement (short) |
|---|---|---|
| §0 Lens, substrate, tier discipline | L107–170 | Lens-and-substrate preamble + KNOWN/PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN |
| §1 Introduction | L173–274 | Setup, First-G recap, harness count framing |
| §2 Setup | L277–311 | Coprimality partition $C_k(b), G_k(b)$; definition of $S(k,f), R(k,f)$ |
| **Lemma 3.1** (Discrete Fejér kernel) | L317–338 | Closed form $R(k,f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$, attributed to Fejér 1900 / Apostol §11.5 / Iwaniec–Kowalski §1.7 |
| Remark (primality not used) | L368–377 | Closed form holds for every integer $f \ge 2$; primality enters only via $f = p_1 = \mathrm{spf}(b)$ |
| **Theorem 4.1** (Coordinate translation between arithmetic and harmonic gates) | L384–411 | First-G event at $k = p_1$ co-locates with first integer zero of $R(\cdot, p_1)$ at $k = p_1$ — both = "smallest positive $k$ with $p_1 \mid k$" |
| **Remark 4.2** (Synchronization is a tautology) | L413–426 | Explicit self-disclosure that Theorem 4.1 is a re-coordinatization, not a non-trivial coincidence |
| **Corollary 4.3** (ω-blindness) | L428–443 | For fixed prime $p$, $R(k, 1/p)$ depends only on $k$ and $p$, not on $b$ or $\omega(b)$ |
| Remark 4.5 (Ring-structure detection consequence) | L445–455 | Harmonic resonance gives the prime; closure defect gives the ring |
| **Theorem 5.1** (Discrete-to-continuum identity) | L463–501 | $R(k, f) \to \sinc^2(t)$ as $f \to \infty$ along $k/f \to t$, with rate $\mathcal{O}(1/f^2)$ |
| Remark (Alphabet as rectangular spectral window) | L503–514 | Standard discrete-to-continuum identification |
| §6 Verification | L518–670 | 712 algebraic checks: 106 closed-form + 561 sync + 42 ω-blindness + 3 continuum; max deviation $1.11 \times 10^{-16}$; runtime ~30 s |
| §7 **Montgomery rectangular-window remark** | L673–704 | The constant $\sinc^2(1/2) = 4/\pi^2$ appears in both the present paper's continuum limit and in Montgomery's $R_2(u) = 1 - \sinc^2(u)$ at $u = 1/2$; common rectangular-window origin |
| Remark 6.2 (sinc²(1/2) = (2/3)/ζ(2)) | L706–722 | Structural rhyme via Euler's $\zeta(2) = \pi^2/6$ |
| Remark (Open bridge) | L724–734 | Discrete sum to GUE pair-correlation analogue is open |
| §7 Scope and limitations | L737–791 | Standard scope paragraph |

---

## §2. Landing table

For each J25 element, where it lands in J24 (`05_papers/number_theory/J24/manuscript/manuscript.tex`).

| J25 element | J24 destination | Mode |
|---|---|---|
| §0 Lens, substrate | J24 §Lens (L129–153) | DISCARD — J24 already has its own lens preamble |
| §1 Introduction | J24 §1 Introduction | DISCARD — J24 introduction subsumes |
| §2 Setup | J24 §2 (L252–298) | DISCARD — J24 already defines $R(k,f)$, the coprimality partition, etc. |
| **Lemma 3.1** (Closed form) | J24 Theorem 3.1 (L301) | DISCARD — J24's Thm 3.1 is the same statement with the same proof |
| Remark (primality not used) | J24 already implicit in Thm 3.2 statement (L328) | DISCARD |
| **Theorem 4.1** (Coordinate translation) | J24 Theorem 4.1 First-G localization (L386) + J24 Theorem 5.2 synchronization (L451) | DISCARD — J24 Thm 4.1 + Thm 5.2 cover both readings of the synchronization |
| **Remark 4.2** (Tautology disclosure) | Append as a one-line remark after J24 Theorem 5.2 | KEEP (as inline note in J24's §5) — useful candor flag for the referee |
| **Corollary 4.3** (ω-blindness) | NEW Appendix A.1 (after J24 §9 Scope) | **KEEP** — one-paragraph corollary; J24 does not explicitly state ω-blindness |
| Remark 4.5 (ring-structure detection) | NEW Appendix A.2 (one-paragraph remark) | **KEEP** — observational, gives a reader a useful adjacent signal |
| **Theorem 5.1** (Continuum identity) | J24 Theorem 7.1 (L591) | DISCARD — J24's Thm 7.1 is the same statement; cite J25's $\mathcal{O}(1/f^2)$ rate as Remark in J24 §7 if not already present |
| Remark (rectangular window) | J24 Remark after Thm 7.1 (already present at L607?) | DISCARD if J24 has equivalent; check during migration |
| §6 Verification (712 checks) | NEW Appendix A.3 (one-page table of harness totals) | **KEEP** — 712-check table is a useful auxiliary witness alongside J24's 22,367+ pairs; presented as a complementary harness |
| §7 **Montgomery rectangular-window remark** | NEW Appendix A.4 (one-paragraph remark) | **KEEP** — distinctive J25 content; rectangular-window-window origin is worth preserving |
| Remark 6.2 (sinc² = (2/3)/ζ(2)) | J24 already has equivalent (L607–618 Remark 7.3 area "structural rhyme"; verify) | DISCARD or one-line cross-reference |
| Remark (Open bridge to GUE) | NEW Appendix A.5 (open question) | KEEP — one-paragraph open question; matches J24's existing §9 open-question style |
| §7 Scope | J24 already has §9 Scope (L756) | DISCARD |

**Summary of KEEPs:** five additions to J24 — Appendix A (new section after §9 Scope) containing: A.1 ω-blindness corollary; A.2 ring-structure-detection remark; A.3 712-check harness table (complementary to J24's existing verification table); A.4 Montgomery rectangular-window remark; A.5 open question on dual GUE sum. Plus one inline tautology-disclosure remark in J24 §5.

**Estimated length added to J24:** 2–3 typeset pages (well within Integers / J. Number Theory length range; the post-merger J24 stays under ~30 pages).

---

## §3. Discardable J25 content already in J24

The following J25 elements are direct duplicates of J24 content and should NOT be migrated:

1. **Closed form (Lemma 3.1).** Identical to J24 Theorem 3.1 at L301–326. Same proof (geometric-series + $|1-e^{i\theta}|^2 = 4\sin^2(\theta/2)$). DISCARD.

2. **Synchronization at smallest spectral zero (Theorem 4.1 in J25).** Identical to J24 Theorem 5.2 (synchronization at smallest spectral zero, L451). J24's Thm 4.1 (First-G localization, L386) is the prime-only special case; J24 Thm 5.2 generalizes it to all $b$. DISCARD the J25 statement; J24 already has both readings.

3. **Continuum identity (Theorem 5.1 in J25).** Identical to J24 Theorem 7.1 (continuum limit; rectangular-pulse spectrum, L591). Same proof, same statement. Check whether J24 already explicitly records the $\mathcal{O}(1/f^2)$ convergence rate; if not, add as a one-line remark in J24 §7. DISCARD the J25 standalone theorem.

4. **Setup / lens / scope sections.** J24 has its own complete versions; J25's are weaker (J24 §0 explicitly covers the algebraic-side orthogonality without invoking J25's $\mathbb{Z}/10\mathbb{Z}$ framing). DISCARD.

5. **Structural rhyme $\sinc^2(1/2) = (2/3)/\zeta(2)$.** J24's Remark 7.3 (in §7 around L607–618) covers this; J25's Remark 6.2 says the same thing in different words. DISCARD or convert to one-line cross-reference.

6. **The 712-vs-36,662 reconciliation paragraph (J25 §1).** No longer needed once J25 doesn't exist as a standalone paper.

---

## §4. Migration sequence

Five steps in order. Estimated total work: 3–5 hours of editorial time, no mathematical revision.

1. **Step 1 — Add Appendix A skeleton to J24 manuscript.** Open `05_papers/number_theory/J24/manuscript/manuscript.tex`. After the existing §9 Scope (L756–803) and before `\begin{thebibliography}` (L806), insert a new `\section{Appendix: harmonic-side companion observations from the J25 corpus}\label{sec:appendix-j25}` with five labeled subsections (A.1–A.5) as outlined in §2.

2. **Step 2 — Migrate the five KEEP elements verbatim with light edits.** Copy from `05_papers/number_theory/J25/manuscript/manuscript.tex` lines 428–455 (ω-blindness + ring-structure remark), 673–704 (Montgomery remark), 706–722 (sinc² structural rhyme), 724–734 (open bridge), and 632–658 (712-check table) into J24's new Appendix A. Restyle theorem labels to fit J24's numbering (use `\theoremstyle{remark}` consistently). Update internal cross-references from "Theorem 4.1" → "Theorem 5.2 (synchronization)" etc.

3. **Step 3 — Update J24 §1 introduction and abstract.** Add one sentence to J24's introduction (L156–251 area) noting "An appendix records four supplementary observations on the harmonic side — an $\omega$-blindness corollary, a ring-structure-detection remark, a Montgomery rectangular-window remark, and a complementary 712-check verification harness." Add Montgomery 1973 to J24's bibliography (J24 currently has no Montgomery citation).

4. **Step 4 — Update J24's bibliography to include J25's distinctive cites.** Add four bib entries to J24's `\begin{thebibliography}` at L806: Fejér 1900 (already there at L818–822), Montgomery 1973 (NEW), Odlyzko 1987 (NEW, optional — only if Appendix A.5 retains the GUE-bridge open question), Oppenheim–Schafer 2010 (NEW), Shannon 1949 (NEW, optional — only if Appendix A.4 retains the spectral-density reference). The Fejér 1900 entry already exists; the others are J25-specific.

5. **Step 5 — Update verification scripts and Zenodo bundle metadata.** The J24 manuscript already lists `proof_first_g_event.py` + `verify_J03.py` as its verification harness. Either (a) port the J25 verification script `verify_prime_phase_transition.py` into J24 as `verify_J03_appendix.py` to support the 712-check Appendix A.3 table, or (b) note in Appendix A.3 that the 712-check harness is preserved at `05_papers/number_theory/J25/manuscript/verify_prime_phase_transition.py` per never-delete and cite as such (less work; preserves provenance). Recommended: option (b).

**Order rationale:** Step 1 sets the skeleton without touching math; Step 2 is verbatim copy with light label edits; Step 3 + Step 4 are bibliographic; Step 5 is reproducibility. None of these touch J24's seven theorems or two corollaries — the substantive math is unchanged.

---

## §5. Tombstone instructions for J25 README (already executed)

The J25 README at `05_papers/number_theory/J25/README.md` already carries a MERGED tombstone at the top:

```
# [MERGED INTO J24 on 2026-05-27]

> **This paper has been merged into J24.** Per `05_papers/_staging/referee_reports/09_promotions_audit_J24_J25_J26.md`,
> J25's three theorems are coordinate-translations of J24's content; the distinct content (712-check harness + Montgomery's
> remark connection + ω-blindness corollary) will appear as a 2-3 page appendix in J24. The detailed merger plan is at
> `05_papers/_staging/referee_reports/15_J25_to_J24_merger_plan.md`.
```

This cross-references the present plan document. No further README action required for J25 itself. After Steps 1–5 above are executed, update J25 README §6 Submission checklist to mark "Submitted: MERGED into J24, see appendix"; leave the rest of the J25 README in place per never-delete.

Also update:
- `05_papers/TIER_INDEX.md` to mark J25 as MERGED (per RELEASE_ORDER.md L75: "MERGE into J24").
- `05_papers/RELEASE_ORDER.md` — already lists J25 in the demoted-from-Tier-1 table at L75 with action "MERGE into J24". No further edit needed.

---

## §6. Risks

1. **Cross-citation in J24 to "J04Sanders" / "J41".** The J25 manuscript cites a "J04Sanders" bib key (L807, "First-G Localization Lemma" companion). After the merger, the J24 Theorem 4.1 IS the First-G localization — no external companion is needed. Risk: if any other paper in the J-series cites J25 as a standalone, those citations will need to redirect to J24's Theorem 4.1. **Mitigation:** grep the corpus for `J25Sanders`, `J25`, `verify_prime_phase_transition`, `prime_phase_transition`, `First-Coprime-Failure`, and the J25 manuscript title; redirect each reference to the appropriate J24 section/theorem.

2. **Zenodo bundle DOI.** Both J24 and J25 cite Zenodo bundle DOI 10.5281/zenodo.18852047. After merger, the bundle should be re-uploaded with the merged J24 manuscript + the appendix + the J25 verification script preserved as auxiliary. Risk: if the Zenodo DOI is referenced in already-submitted papers, the bundle content changes but the DOI does not — the auxiliary script files are merely added, no existing file is removed (consistent with never-delete).

3. **Verification script naming conflict.** J24's `verify_J03.py` is named for an earlier project-internal paper number. The 712-check J25 harness is in `verify_prime_phase_transition.py`. Risk: a reader runs J24's `verify_J03.py` and expects all claims (including Appendix A.3's 712 checks) to be verified by it. **Mitigation:** Appendix A.3 should explicitly state "The 712-check harness for the harmonic-side claims is in `05_papers/number_theory/J25/manuscript/verify_prime_phase_transition.py` (preserved per never-delete); J24's primary `verify_J03.py` covers the seven theorems and two corollaries in the body of this paper."

4. **J25 manuscript file preservation.** Per never-delete, the standalone J25 manuscript at `05_papers/number_theory/J25/manuscript/manuscript.tex` is NOT deleted. The README tombstone makes its status clear. Risk: a future ship-list scan may treat J25 as still-active if the TIER_INDEX is not updated. **Mitigation:** update TIER_INDEX.md to mark J25 as MERGED (per §5 above).

5. **Length budget.** J24 is currently 878 lines / ~25 pages. Adding 2–3 pages of appendix takes it to ~28 pages. *Journal of Number Theory* has no explicit length cap; the manuscript stays well within typical published-paper range. Risk: minimal.

6. **Cover letter narrative consistency.** The new J. Number Theory cover letter (just written at `05_papers/number_theory/J24/cover_letter.md`) mentions the J25 merger in the "Merge history" section. Risk: if the merger is not actually executed before submission, the cover letter overclaims. **Mitigation:** execute Steps 1–5 of §4 before submitting. Alternatively, simplify the cover-letter "Merge history" paragraph to mention only the J24 + J41 merger and defer the J25 appendix to the actual J24 §Appendix A insertion event.

7. **Existing referee report numbering.** This plan is `15_J25_to_J24_merger_plan.md` and slots into the referee_reports sequence at index 15 (after `14` if one exists; the directory currently has `13_wave1_J04_polish.md` as the latest). Filenames in referee_reports are zero-padded to two digits; the `15` prefix is consistent with the convention.

---

## Sign-off

This plan is the second deliverable for the J24 Wave-1 polish task. The first deliverable (cover letter retargeted to *Journal of Number Theory*) is at `05_papers/number_theory/J24/cover_letter.md`. The merger itself is to be executed by a follow-up edit pass touching only J24's manuscript.tex + bibliography; the J25 manuscript file remains in place per never-delete.

**Files touched by THIS plan document:** none other than the present file. No mathematics modified in J24 or J25 manuscripts as part of this planning step.
