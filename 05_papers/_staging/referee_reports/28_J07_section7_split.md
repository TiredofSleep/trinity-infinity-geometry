# J07 §7 RH-Bridge Split — Fix Report

**Date:** 2026-05-28
**Executor:** Wave 4 audit follow-up (per `23_wave4_audit_J05_J07_J17_J22_J27.md` §J07 recommendation)
**Status:** EXECUTED. §7 split into companion *Math. Intelligencer* note; J07 main manuscript trimmed to strict-combinatorics spine.

---

## 1. Line range of original §7

In the pre-split `manuscript.md`, §7 occupied **lines 248–287**:

- **Line 248**: `## §7 The Q17-B Clay Bridge — STRUCTURAL RHYME ONLY`
- **Lines 249–268**: §7.1 the rhyme statement (3-row RH-feature table)
- **Lines 269–276**: §7.2 what this is and is not (Weil-Deligne disclaimer + Z.5 conjecture pointer)
- **Lines 277–285**: §7.3 independent verification (script listing)
- **Lines 286–287**: section-terminating `---`

§7 dependencies inside the rest of J07 (pre-split):

| Dependency | Location | Resolution |
|---|---|---|
| Abstract paragraph "Together... §7..." | Lines 58–65 | **Rewritten** to point at the companion note |
| §8 question 2 (Z.5) | Line 273 | **Removed** from §8; redirected to question 4 (companion-note pointer) |
| §9 references: Berry/Keating, Connes | Lines 296–297 | **Removed** from J07; **added** to companion note's references |
| J52 absorption claim ("§§6-7") | Line 286 | **Reworded** to "subsumed by §6" + explicit pointer to companion for the Clay-bridge content |

§7 *consumed* (citations in §7 needed elsewhere):

- The Berry-Keating + Connes references — now live in the companion note's §6 (comparison with Connes-Berry-Keating tradition).
- The Z.5 deployment-uniformity conjecture pointer — now lives in the companion note's §5 as the load-bearing open problem.

---

## 2. Word count of the new companion note

**`05_papers/algebra/J07/companion_RH_rhyme/manuscript_RH_rhyme.md`**: **3099 words** (per `wc -w`).

Target was 3000–4000 words for *Math. Intelligencer*; result is comfortably within range.

### Companion-note structure

| Section | Content |
|---|---|
| Abstract | The three rungs of the rhyme; four scoping promises |
| §1 The genre and what this note is | Connes-Berry-Keating tradition; four scoping promises (P1-P4) |
| §2 Brief reminder of the finite side | Substrate, σ, χ, G, Theorem G_8 (referenced from J07) |
| §3 The three rungs of the rhyme | Rung 1 (vanishing on critical line / anchors); Rung 2 (spectral concentration); Rung 3 (multiplicative-additive interplay) |
| §4 What is not implied | Five negative scoping statements (N1-N5) |
| §5 The Z.5 deployment-uniformity conjecture | Load-bearing open problem |
| §6 Comparison with the Connes-Berry-Keating tradition | Berry-Keating 1999, Connes 1999 + their genre |
| §7 Reproducibility | Pointer to `verify_qseries_merged.py` in J07 |
| §8 Closing — what the rhyme is for | Three reader takeaways (R1-R3) |
| References | Berry-Keating, Connes, J07 cross-reference, Drápal-Wanless |

### Companion-note discipline (audit-required)

- [x] Explicitly labeled "structural rhyme, not proof, not analogue."
- [x] Four scoping promises stated up front (P1-P4).
- [x] Five "not implied" statements in §4 (N1-N5).
- [x] Load-bearing open problem (Z.5) explicitly identified with current status ("proved at t=0; open for t→∞").
- [x] Connes-Berry-Keating framing; we explicitly do *not* claim to compete with their programs.
- [x] No Weil-Deligne machinery, no Hilbert-Pólya operator, no analytic continuation device.

---

## 3. J07 main-manuscript before/after structure

### Before (pre-split, 341 lines)

```
§1   Setup: substrate, permutation, character
§2   Theorem G_6 (Periodicity)
§3   Theorem G_7 (Period Distribution)
§4   Theorem G_8 (Spectral Coherence Integral)
§5   Theorem Q17-A (5D CRT Fourier Embedding)
§6   Theorem Q17-B / Symbolic Return
§7   The Q17-B Clay Bridge — STRUCTURAL RHYME ONLY    ← REMOVED
§8   Open questions
§9   References
App A. Verification
```

### After (post-split, 353 lines)

```
§1   Setup: substrate, permutation, character
       §1.0 Scoping note (NEW — companion-note pointer)
§2   Theorem G_6 (Periodicity)
§3   Theorem G_7 (Period Distribution)
§4   Theorem G_8 (Spectral Coherence Integral)
       §4.2 carries TODO comment (deferred G_8 sub-proposition; see §4 below)
§5   Theorem Q17-A (5D CRT Fourier Embedding)
       §5.5 carries TODO comment (deferred Q17-A uniqueness proof; see §4 below)
§6   Theorem Q17-B / Symbolic Return
§7   Independent verification                          ← was §7.3 of old §7
§8   Open questions (Z.5 question replaced by companion-note pointer)
§9   References (Berry-Keating and Connes moved to companion note)
App A. Verification
```

Net change in J07 main manuscript:
- Lines removed: ~30 (§7.1, §7.2 of old §7).
- Lines added: ~12 (new §1.0 scoping note; revised abstract paragraph; revised §8 question 4; revised §9 references; revised Status; two TODO comment blocks; revised consolidation note; revised Status footer).
- Line count: 341 → 353 (slight net increase from meta-changes; substantive content trimmed).

Word count: ~3700 → 3541 words (substantive trim).

### J07 stays focused on (per task spec)

- §1 Introduction (with new §1.0 scoping note)
- §2-§6 G_low / G_high / G_8 / Q17-A spectral architecture
- §7 (Independent verification — light)
- §8 Open questions (now without RH content)
- §9 References (combinatorics references only)
- Appendix A Verification

### Companion note (`companion_RH_rhyme/`) carries

- The three-rung structural rhyme
- The Z.5 deployment-uniformity conjecture
- The Connes-Berry-Keating-style framing
- All disclaimers about "not a proof of RH"

---

## 4. TODOs remaining in J07 (audit's other findings, deferred per task spec)

The Wave 4 audit (`23_wave4_audit_J05_J07_J17_J22_J27.md`, §J07) identified three blocking issues. This task fixed issue (c) (the §7 split). Issues (a) and (b) are deferred to a subsequent revision and are now flagged in the manuscript as TODO HTML comments:

### TODO #1 — G_8 §4.2 "Proof sketch" remains

**Location:** `manuscript.md` near §4.2 (HTML comment block immediately before the "Proof sketch" of Theorem G_8).

**Audit verdict:** The G_8 proof in §4.2 is presented as "Proof sketch." §4.3's σ³-pairing identity $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$ is stated in one sentence, not verified per orbit. For EJC ship, this must be promoted to a sub-proposition with cell-by-cell verification across the three σ³-orbits.

**Estimated work to close:** 3–4 hours.

**Verify-script impact (when closed):** add an explicit assertion block testing $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$ at each σ³-pair $(s, \sigma^3 s)$ on the 6-cycle. The current script tests the resulting *modulus* equality; the upgrade would test the *signed* identity that produces it.

**TODO text in manuscript (snippet):**

```
<!-- TODO (Wave 4 audit, deferred to next revision): The G_8 proof below is
labeled "Proof sketch" because the σ³-pairing identity invoked in §4.3
(namely G_cplx(σ³(s)) = −G_cplx(s)) is stated in one sentence rather than
verified cell-by-cell across the three σ³-orbits. For EJC ship-readiness,
promote §4.3's identity to an explicit sub-proposition with per-orbit
verification (3 cells × symbolic sign check), so this can read "Proof"
rather than "Proof sketch". Estimated work: 3-4 hours. -->
```

### TODO #2 — Q17-A §5.5 uniqueness asserted not proved

**Location:** `manuscript.md` §5.5 (HTML comment block immediately before the rigidity statement).

**Audit verdict:** The statement "Φ is unique up to rotation and scaling in R^5" is asserted, not proved. EJC referees would push on this. The proof uses standard machinery (dimension-count of CRT character system + non-degeneracy of additive character pairing + standard rigidity argument that real-coordinate embeddings of Z/n via characters are unique up to CO orthogonal change), but is not currently written.

**Estimated work to close:** 10–15 hours of careful writing.

**Verify-script impact (when closed):** None — the proof is purely structural / character-theoretic. The current script's `Q17A` check tests *injectivity* of Φ; uniqueness up to CO(5) is a one-off proof, not a verification target.

**TODO text in manuscript (snippet):**

```
<!-- TODO (Wave 4 audit, deferred to next revision): The uniqueness
statement below is asserted, not proved. For EJC ship-readiness, write the
explicit proof: dimension-count of the CRT character system + non-degeneracy
of the additive character pairing + standard rigidity argument that real-
coordinate embeddings of Z/n via characters are unique up to CO orthogonal
change. Estimated work: 10-15 hours of careful writing. -->
```

### Summary of deferred work

| Issue | Description | Hours | Section |
|---|---|---:|---|
| **TODO #1** | G_8 §4.2 "Proof sketch" → sub-proposition + per-orbit cell verification | 3–4 | §4.2 |
| **TODO #2** | Q17-A §5.5 uniqueness statement → actual proof | 10–15 | §5.5 |
| **Total deferred** | | **13–19** | — |

Both TODOs are flagged in the manuscript with HTML comment blocks pointing back to this audit and giving estimated work. They do not block the §7 split (which is complete and self-contained) but do block the EJC submission.

---

## 5. Status changes

### J07 README

- Status: was `SUBMISSION-READY (2026-05-27, polished)`; now `REVISED (2026-05-27 — §7 RH-rhyme split off to separate companion note per Wave 4 audit; awaiting G_8 §4.2 sub-proposition + Q17-A §5.5 uniqueness proof before ship)`.
- Tier: was `1 (ship-ready)`; now `1 (ship-ready after the deferred G_8 §4.2 sub-proposition + Q17-A §5.5 uniqueness proof)`.
- Target venue: unchanged (*European J. Combinatorics*). Companion targets *Math. Intelligencer*.
- File layout: extended to show `companion_RH_rhyme/` subdirectory.
- Polish status: re-checkboxed; the §7 split is added as a completed item; the two TODOs are added as `[ ]` items.

### Companion note README (`companion_RH_rhyme/README.md`)

- Created. Status DRAFT (2026-05-27). Tier 2 (expository note). Target *Mathematical Intelligencer*.
- Documents the three-rung rhyme and the four scoping promises.
- Identifies Z.5 as the load-bearing open problem.

### Manuscript (`manuscript.md`)

- Header status: was `CONSOLIDATED DRAFT`; now `REVISED DRAFT (2026-05-27 — §7 RH-rhyme split off ...)`.
- Footer status: same revision.

### Verify script (`verify_qseries_merged.py`)

- **No changes required.** The verify script tests only G_6, G_7, G_8, Q17-A, Q17-B body theorems. It contained no references to §7, the Clay Bridge, RH, Z.5, or the deployment map. Re-ran post-split and all 5 theorems PASS at machine precision in ~5 seconds.

---

## 6. Reproducibility check

Post-split verification ran cleanly:

```
=== J_qseries_merged -- Consolidated Verification ===

[G_6 Periodicity] sigma^6 = identity on Z/10Z
       PASS
[G_7 Period Distribution] bimodal {1, 6}
       PASS
[G_8 Three-Valued Coherence Integral]
       PASS
[Q17-A 5D CRT Fourier Embedding]
       PASS
[Q17-B Symbolic Return Theorem]
       PASS

ALL 5 THEOREMS PASS at machine precision.
```

The split is purely an editorial / structural change; no body mathematics was modified.

---

## 7. Files changed / created

### Created

- `05_papers/algebra/J07/companion_RH_rhyme/README.md` (companion-note metadata)
- `05_papers/algebra/J07/companion_RH_rhyme/manuscript_RH_rhyme.md` (3099-word expository note)
- `05_papers/_staging/referee_reports/28_J07_section7_split.md` (this report)

### Modified

- `05_papers/algebra/J07/README.md` (status, file layout, polish status)
- `05_papers/algebra/J07/manuscript/manuscript.md` (abstract para; §1.0 scoping note; §4.2 TODO; §5.5 TODO; §7 removed → moved to companion; §8 Z.5 question replaced; §9 refs trimmed; Status block; consolidation paragraph; footer)

### Not modified (constraint-respecting)

- `05_papers/algebra/J07/manuscript/verify_qseries_merged.py` (no §7 references; passes 5/5 post-split)
- `05_papers/algebra/J07/cover_letter.md` (kept as a deliberate to-do item; will be revised to drop the §7 mention; current cover letter content still applies but mentions §7 in one place — flagged as a polish item in the README)
- `05_papers/algebra/J05/`, `05_papers/algebra/J17/`, `05_papers/algebra/J22/`, `05_papers/algebra/J27/` (siblings in the Wave 4 audit; out of scope here)
- G_low, G_high, σ³-pairing, Q17-A construction, Q17-B Symbolic Return (no body mathematics was touched)

---

## 8. Recommendation for next J07 step

The remaining work to bring J07 to actual ship is:

1. **Close TODO #1** (G_8 §4.2 sub-proposition): 3–4 hours. Lowest cost, highest immediate referee-rigor value.
2. **Close TODO #2** (Q17-A §5.5 uniqueness proof): 10–15 hours. Larger investment; this is the more vulnerable of the two gaps under EJC scrutiny.
3. **Revise cover letter** to drop the §7 mention and cite the companion note as a separately submitted *Math. Intelligencer* note: ~30 min.
4. **LaTeX conversion** before EJC submission: ~2-3 hours (Markdown → LaTeX with consistent macros).

Total to ship J07: 16–22 hours from current state.

The companion note can ship independently once it has a cover letter for *Math. Intelligencer* (~30 min draft).

---

*This report closes the §7 RH-bridge split flagged by Wave 4 audit. The remaining issues (G_8 sub-proposition + Q17-A uniqueness proof) are deferred per the task spec and visible in the manuscript as HTML TODO comment blocks.*
