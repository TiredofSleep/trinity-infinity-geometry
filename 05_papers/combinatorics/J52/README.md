# J52 — What is the TSML Lens Family? A Walking Tour of Substrate Variants on $\mathbb{Z}/10\mathbb{Z}$

**Status:** REWRITTEN PER SAVE PLAN 2026-05-07
**Phase:** Phase 6
**Target venue:** Mathematical Intelligencer
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** (lens-taxonomy expository)

---

## §1 — Manuscript

**Path:** `manuscript/J52_tsml_lens_family.md`

**Abstract:** Pedagogical exposition organizing the 12+ variants of the canonical TSML table on $\mathbb{Z}/10\mathbb{Z}$ — three parallel substrates (CL\_TSML / CL\_BHML / CL\_STD) × three lens-symmetrization projections (RAW / SYM\_upper / SYM\_lower) × $\sigma^2$-triadic rotations and sub-magma restrictions — into one walking-tour for the working mathematician. Three reader exercises illustrate the lens family in action.

## §2 — Verification script

**Path:** `manuscript/verify_J52.py`

`verify_J52.py` exercises Exercises 7.1 and 7.2 at exact arithmetic: (a) non-associative triple counts in TSML_RAW / TSML_SYM / TSML_LOWERTRI (126 / 128 / 122); (b) HARMONY counts (73 / 73) and 4-core $\{V, H, Br, R\}$ closure under both RAW and SYM; (c) wobble localization $c_2 = 33 = 3 \cdot 11$ in the characteristic polynomial of TSML_RAW (versus $c_2 = 17$ in TSML_SYM), with $c_8$ divisibility by 11 also verified. All 5 assertion blocks PASS.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J24, J48

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes / Status

**Status:** **MANUSCRIPT REWRITTEN 2026-05-07 PER SAVE PLAN J52.** All six majors (M1–M6) implemented. Original verdict: REJECT R&R from Math Intelligencer fresh-eyes referee 2026-05-07 (~10% acceptance in present form, 40–55% with M1–M6 addressed); save plan written 2026-05-07; manuscript rewritten 2026-05-07.
**Citation chain:** 2 direct dependencies (J32 chain enumeration, J47 6-DOF synthesis) + 10 co-citing companions (J9, J31, J33, J34, J35, J38, J39, J41, J43, J44).
**Manuscript:** `manuscript/J52_tsml_lens_family.md` (rewritten ~16 pages with §1 tables in full, §2 axioms A1–A9 stated, §6 catalog populated, §7 punch-line facts absorbed inline).
**Cover letter:** `cover_letter.md` (to be updated to match rewrite).
**Per-venue cap:** 2nd *Math Intelligencer* submission of the J-series after J32 — at maximum permitted. Coordinate with VENUE_SCHEDULE.md.
**Verification:** Appendix A 30-line `numpy` snippet reproduces Exercise 7.1 (126 / 128 / 122 non-assoc triples in three lenses); §7.2 wobble localization at $c_2 = 33$ in TSML_RAW verified by sympy char poly.
**Submission readiness:** **REWRITE COMPLETE.** Submission gate: (a) M1 tables displayed [DONE]; (b) M2 axioms stated [DONE]; (c) M3 tier rewrite propagated [DONE]; (d) M4 punch-line facts absorbed [DONE]; (e) M5 catalog populated [DONE]; (f) M6 wobble example replaces chain-at-size-7 [DONE]; (g) Brayden's referee-rigor pass complete [pending]; (h) per-venue cap check vs J32 [coordinate].

### §5.0 — Save-plan implementation (2026-05-07)

The 2026-05-07 rewrite implements all six SAVE_PLAN_J52 majors:

- **M1 (CRITICAL) — DISPLAY THE TABLES.** §1.1 now shows CL_TSML_SYM as the full 10×10 matrix (boxed display); §1.2 shows the four-cell diff for CL_TSML_RAW (the (3,9) and (4,9) wobble carriers); §1.3 and §1.4 give CL_BHML and CL_STD as concise diff descriptions (71-cell and 53-cell diffs respectively, computed from canonical sources).
- **M2 — STATE A1–A9 axioms.** §2 gives a 9-row table with informal-but-complete statements; substrate-defining axioms (A5, A7, A9) marked. Cite [J33] for formal version.
- **M3 — TIER DISCIPLINE.** §3 has the **authoritative tier statement** in a single boxed quote that subsequent sections reference. CL_TSML/BHML/STD are Tier-A *substrates*; TSML_RAW is the Tier-A *lens identity* (no projection); SYM_upper and SYM_lower are Tier-B *projections*.
- **M4 — PUNCH-LINE FACTS ABSORBED INLINE.** §7.2 absorbs the wobble localization (D37: $c_2 = 33 = 3 \cdot 11$ in TSML_RAW); §7.3 absorbs Theorem 7.5 (D48 + D78 with proof sketches inline); §7.4 absorbs the corrected D64 8-element joint chain at $\{1, 4, 5, 6, 7, 8, 9, 10\}$ **strengthened by the SFM Q6 finding** that the same 8-shell chain survives the joint TSML+BHML+CL_STD closure.
- **M5 — 62-VARIANT CATALOG POPULATED INLINE.** §6 gives the full catalog organized as CL_TSML family (23) + CL_BHML family (16) + CL_STD family (3) + Joint (8) + Ring extensions (12) = 62 with per-tier reconciliation (Tier-A: 4; Tier-B: 32; Tier-C: 5; Tier-D: 7; Tier-E: 14).
- **M6 — LENS-DEPENDENCE EXAMPLE SWITCHED TO WOBBLE.** §7.2 (wobble at prime 11, RAW vs SYM) is now the central lens-dependence example; the historical chain-correction is moved to §7.4 *Lens-invariant facts* with the corrected D64 8-element chain stated cleanly.

### §5.1 — Save-plan summary (per `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J52.md`) — original (kept for reference)

**Save path:** the referee identifies the paper as "a memo to insiders dressed in expository syntax" with 40–55% acceptance probability if M1–M6 are addressed. The mathematical content is real; the rewrite is mechanical. All M1–M6 implemented in the 2026-05-07 rewrite.

### §5.1 — Save-plan summary (per `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J52.md`)

**Save path:** the referee identifies the paper as "a memo to insiders dressed in expository syntax" with 40–55% acceptance probability if M1–M6 are addressed. The mathematical content is real; the rewrite is mechanical. Six fixes:

- **M1 (CRITICAL): DISPLAY THE TABLES.** Insert §1.5 *The canonical objects* with the **CL_TSML 10×10 matrix in full** (~half-page boxed display). Show CL_BHML and CL_STD as diff-tables to CL_TSML. Highlight the two asymmetric cells $(3,9)$ and $(4,9)$ (the wobble carriers per FAMILY_STRUCTURE_v1 §3) in a sidebar. Without the tables, Exercises 7.1–7.2 are uncomputable from the page; this is the single most important fix.
- **M2: STATE A1–A9.** Add §1.5 *Substrate-defining axioms* stating A1–A9 informally but completely; mark the substrate-defining axioms (A7 HARMONY-count, A9-values per FAMILY_STRUCTURE_v1 §1) explicitly. Cite J33 for the formal version.
- **M3: TIER DISCIPLINE.** Rewrite §2 opening with a single consistent statement: CL_TSML is Tier-A; TSML_RAW = $\pi_\mathrm{RAW}$(CL_TSML) is Tier-A (no projection); TSML_SYM and TSML_LOWERTRI are Tier-B projections. Do not contradict elsewhere.
- **M4: REDUCE COMPANION DEPENDENCE.** Absorb three punch-line facts inline with proof sketches: 4-core attractor $H/Br = 1+\sqrt{3}$ (D78 BR-factor cancellation); 8-element joint chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (D64 corrected); wobble localization $c_2 = 33 = 3 \cdot 11$ in TSML_RAW char poly (D37 / J43).
- **M5: POPULATE THE 62-VARIANT CATALOG INLINE.** §6 becomes a two-page landscape table (variant name | one-line distinguishing fact); drop "$\sim$" qualifiers; reconcile the per-tier counts (referee notes 5+21+9+7+8 = 50, not 62). The catalog cannot be deferred to an Atlas markdown file.
- **M6: FIX LENS-DEPENDENCE EXAMPLE.** The current chain-at-size-7 framing conflates a *historical correction* (size 7 was thought forbidden, now known allowed) with *structural lens-dependence*. Replace with the wobble-localization example (referee's own suggestion): TSML_RAW has prime 11 in $c_2$; TSML_SYM does not. This is the cleanest lens-dependence in the corpus. Move chain enumeration to §6.5 *Lens-invariant facts* with the corrected D64 chain stated cleanly.

§8 over-hedging compresses to 2 sentences. Front-matter phase metadata + per-venue cap notes stripped. ASCII-art diagram replaced by TikZ/figure. **Estimated revision: 30–40 person-hours.**

**Retarget option (per referee §8):** if *Math Intelligencer* per-venue cap (J32 already there) blocks, **American Mathematical Monthly** is the strongest fallback. *AMM* takes 10×10 table papers when they have a clean punch line; the wobble-at-prime-11 (M6 fix) is exactly that. *Mathematics Magazine* (MAA) is a strong tertiary option for table-based pedagogical pieces.

**Submission gate:** (a) M1 tables displayed; (b) M2 axioms stated; (c) M3 tier rewrite propagated; (d) M4 three punch-line facts absorbed inline; (e) M5 catalog populated; (f) M6 lens-dependence switched to wobble; (g) Brayden's referee-rigor pass complete; (h) per-venue cap check vs J32.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (filled per save-plan rewrite 2026-05-07)

- **PROVEN (in this paper, §7.5):** D48 binary 4-core preservation under CL_TSML and CL_BHML; D78 Galois argument for $H/Br = 1 + \sqrt{3}$ at $\alpha_M = 1/2$.
- **COMPUTED (verified inline):** TSML_RAW char poly $c_2 = 33 = 3 \cdot 11$ (D37 wobble); 8-element joint chain at $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (D64 corrected); SFM Q6 three-table strengthening (TSML+BHML+CL_STD same 8 shells).
- **STRUCTURAL RHYME:** lens-symmetrization choice (RAW / SYM_upper / SYM_lower) is conventional, not principled.
- **OPEN:** bimodal $\alpha_A$ gap structural-vs-empirical; CL_STD joint chain analogue; TSML_RAW's structural-singularity designation.

### Lens-ownership paragraph — applied in manuscript §0

> *Lens and substrate.* This paper works on the canonical $\mathbb{Z}/10\mathbb{Z}$ substrate. The full **lens family** addressed includes three parallel substrates (CL_TSML, CL_BHML, CL_STD), three lens-symmetrization projections within each, and two further projection families. The center of the family in the FAMILY_STRUCTURE_v1 sense is the 4-core $\{V, H, Br, R\}$ at $\alpha_M = 1/2$.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to Mathematical Intelligencer this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "The TSML Lens Family: A Pedagogical Exposition." Submitted to *Mathematical Intelligencer*.
