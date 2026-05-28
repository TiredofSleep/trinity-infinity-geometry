# 33 — Tier 2 polish: J38 + J39 + J40

**Date:** 2026-05-28
**Pass:** Tier-2 polish ("as ready as a Tier 2 draft can be")
**Scope:** Bounded polish — README accuracy, abstract cleanness, known-issues hygiene, J-ID consistency, §5.1 deduplication. No central theorems touched.

---

## Process

For each paper: read README, manuscript, cover letter, ran the verification script, then assessed Tier-2 readiness on three axes: (a) central claim clarity; (b) tier discipline / PROVEN-COMPUTED-RHYME-OPEN partition; (c) status-metadata hygiene. Applied only documentation-level fixes. All paths absolute below.

Verification scripts (all PASS):

- J38: `05_papers/physics/J38/manuscript/proof_separability_bridge.py` — 43/43 PASS (elementary potential algebra).
- J39: `05_papers/combinatorics/J39/manuscript/verify_J52.py` — all assertion blocks PASS (126/128/122 non-assoc triples, 73/73 HARMONY, 4-core closure, c₂(RAW)=33=3·11, c₂(SYM)=17, c₈(RAW)%11=0).
- J40: `05_papers/interdisciplinary/J40/manuscript/verify_J53.py` — VERIFY OK (mutual exclusion across 2³ input combos, exhaustiveness, score ranges per Def 3.2, priority III > IV > I/II).

---

## J38 — Logarithmic Nonlinearity as a Forcing Principle

**Verdict:** **Tier-2-ready.** The R1 revision (2026-05-07) addressed every fresh-eyes referee item with discipline; the manuscript is now an honest Tier-4 framework paper that does not over-claim. Outstanding work is mostly LaTeX conversion and a referee-rigor pass; no substantive content gaps remain.

### Central claim — clear

The paper's claim is precise and conservative: (a) **Theorem 2.1** is cited not re-proved (BB uniqueness, Schrödinger, 1976); (b) **Theorem 4.1** is a *conditional* regularity theorem for $\Box\Xi = \kappa(1+\log\Xi)$ under hypotheses H1 (positivity preservation) and H2 (uniform lower bound), proved by Brezis-Gallouet log-Sobolev + Bihari Grönwall; (c) NS quadratic nonlinearity breaks separability is immediate from Definition 5.1; (d) **Conjecture 5.2** (separability regularity criterion) is precise over the polyhedral-divergence-free class $\mathcal P_K$. The paper explicitly does NOT claim NS regularity.

### "BB reading" — derivation or rhyme?

The user asked: is the BB reading of log nonlinearity a *rederivation* or a *structural rhyme*?

**Answer: a structural reading on the Schrödinger side that becomes a derivation only via Open Problem 1.** The 1976 BB theorem says: on the non-relativistic Schrödinger evolution, log nonlinearity is unique among self-interactions preserving bipartite product evolution. The paper's "forcing principle" reading exploits this by saying: *any separability-respecting continuum lift of discrete partition data is forced to inherit log nonlinearity on the Schrödinger side.* In §3.3 the paper labels the Bridge Premise as explicitly conjectural — the lift construction $\Phi_N$ is Open Problem 1. §2.3 clarifies that the wave-equation model $\Box\Xi = \kappa(1+\log\Xi)$ is a *specific scalar-field model whose potential is BB-forced via the cosmological / Schrödinger side*, not a general "BB theorem for wave equations". This is the correct framing — neither inflated to "derivation" nor deflated to "rhyme".

### Bounded polish applied

- `05_papers/physics/J38/README.md`: rewrote Known-issues block. Confirmed Johnson byline is absent from both manuscript and cover letter (already harmonized 2026-05-07 + 2026-05-27); confirmed abstract carries Open Problem 0 explicitly as the load-bearing hypothesis; confirmed verify script PASSes 43/43; confirmed cover letter R1 itemizes revisions correctly. Recorded the polish pass.

### Substantive issues flagged (not fixed here)

- **LaTeX (amsart) conversion** still pending — the §6 submission checklist will not be complete until this happens. The manuscript is currently `.md`; JMP submission needs `.tex`.
- **Companion-citation tightening**: references [J14], [J32], [J27], [J41], [J46] are listed as "submitted to [venue]"; once those land or stabilize, this paper's references should specify the submission status concretely. Not blocking for R1.
- The phrasing "the BB-bridge reading is novel insofar as we know" in README §5 is the standard "no full literature scan completed" hedge — acceptable for Tier 2.

---

## J39 — What is the TSML Lens Family?

**Verdict:** **Tier-2-ready, with one fixed.** The §5.1 duplication called out in the user's brief was real (lines 53 and 57 of the previous README both opened "### §5.1 — Save-plan summary"). Now deduplicated. The pedagogical paper is competent: tables displayed (§1), axioms A1–A9 stated (§2), tier discipline boxed (§3), 62-variant catalog populated (§6), three exercises with absorbed punch lines (§7).

### Map for the rest of the corpus — useful or curiosity?

The user asked: pedagogical paper — does it serve as a useful map for the rest of the corpus, or is it a curiosity?

**Answer: useful map, with one provisional bet.** The paper does two real things: (a) it makes the lens-vs-substrate distinction crisp (RAW is the Tier-A lens identity of CL_TSML; SYM_upper and SYM_lower are Tier-B projections) — this resolves a vocabulary slippage that has confused J-papers across the corpus; (b) it displays the wobble-at-prime-11 (c₂=33=3·11 in TSML_RAW) as the canonical lens-dependence example, with the corollary that 4-core attractor + joint chain are *lens-invariant*. The provisional bet is *Math Intelligencer* fit — the per-venue cap (already 2nd-after-J10) is an open scheduling issue that may push it to AMM or Math Magazine; the content itself is solid for any of those.

The "memo to insiders dressed in expository syntax" referee critique was the right diagnosis pre-rewrite; the M1–M6 implementation moved it firmly toward "walking tour useful to outsiders".

### Bounded polish applied

- `05_papers/combinatorics/J39/README.md`: deduplicated §5.1 (one header retained, pre-rewrite six-fixes list preserved beneath it for audit trail); rewrote Known-issues block to reflect post-polish state and verification PASS; flagged the §6.6 catalog arithmetic for next-pass tightening.

### Substantive issues flagged (not fixed here)

- **§6 submission checklist entirely empty** — the checkboxes haven't been re-verified post-rewrite. This is internal hygiene; a referee won't see the README but the submission gate requires it.
- **Per-venue cap collision**: J39 is the 2nd Math Intelligencer (after J10) and J40 retargets the same venue, making J40 the 3rd. The save-plan retarget options (AMM for J39, Philosophia Mathematica for J40) are documented but require Brayden's call on `VENUE_SCHEDULE.md`.
- **§6.6 catalog arithmetic** reconciles 23+16+3+8+12 = 62 with the per-tier 4+32+5+7+14 = 62 by absorbing duplicates of the canonical Z/10Z; this is internally consistent but a careful referee may probe it. Consider tightening on the next pass.

---

## J40 — Paradox Classifier UOP

**Verdict:** **Tier-2-ready, with three fixes applied.** The 2026-05-07 rewrite per SAVE_PLAN_J53 dropped misclassified examples (Monty Hall, Gödel), added Berry/Curry/Yablo, engaged the prior taxonomy literature (Sainsbury/Quine/Priest/Rescher), formalized the classifier as predicates on category $\mathcal{M}$, defined the score function, and retargeted from AMM to Math Intelligencer. The cover letter, however, still carried stale J-IDs and miscounted worked examples; this pass cleaned both.

### Taxonomy or applications?

The user asked: classifier scheme — is it just a taxonomy, or does it have explicit applications?

**Answer: algebraic taxonomy with an algorithmic decision procedure, and a live demo.** The classifier is genuinely algebraic in a precise sense: types are predicates on a defined category $\mathcal{M}$ (Definition 2.1), mutually exclusive (Lemma 2.2), and exhaustive on admissible inputs (Lemma 2.3). The five-step decision procedure (§3) is implemented as 50 lines of Python (Appendix A); the live demo at `coherencekeeper.com/paradox.html` takes user-entered paradoxes and returns type+score. Seven worked examples in §4 (Russell→III, Liar→III, Berry→II, Curry→III in ZFC / II in paraconsistent, CH→II, Newcomb→IV, Sorites→II) demonstrate the procedure on canonical paradoxes. The score function (Definition 3.2: $\mathrm{score} = 1 - |U_\mathrm{residual}|/|U(f_1)|$) is definable, not decoration. Whether the four types are exhaustive beyond admissible $\mathcal{M}$ is honestly flagged OPEN (Bertrand, Skolem, Banach-Tarski).

So: more than taxonomy. Less than universal applicability. Honestly scoped.

### Bounded polish applied

- `05_papers/interdisciplinary/J40/cover_letter.md`: harmonized the stale J-IDs ("J34, J11, J35, J45" → "J20, J21, J36, J47, J39", matching manuscript §7 and README §10); corrected the example count ("eight worked examples" → "seven", with Monty Hall and Twin Paradox dropped, Berry/Curry/Yablo added).
- `05_papers/interdisciplinary/J40/README.md`: §3 Dependencies updated from "J34" to "J20 (UOP Theorem 0; cross-references: J21, J36, J47, J39)" with note recording the harmonization; Known-issues rewritten to reflect the cover-letter harmonization and verify-script PASS.

### Substantive issues flagged (not fixed here)

- **Per-venue cap is the immediate blocker.** J40 retargets Math Intelligencer (3rd of the J-series after J10 and J39); the save-plan alternate is Philosophia Mathematica with 40–50% acceptance per the fresh-eyes referee. Decision needed.
- **Submission gate (a)** requires [J20] (UOP Theorem 0) on arXiv before submitting J40 (J40 cites it as a *JNT* preprint in preparation). This is a real cross-paper dependency.
- **Lemma 2.2 mutual exclusion proof** is informal in the manuscript ("returns the first satisfied predicate"); a careful logic referee may want a more explicit argument. Acceptable for Tier 2; flag for the rigor pass.
- **§4.2 Liar paradox dual classification** (III in Tarski-stratified vs IV in Gupta-Belnap revision-theoretic) is handled correctly — explicit acknowledgment that the classifier output depends on the ambient theory $\mathbf{T}$ and family $\mathcal{F}$. Not a flaw; could be foregrounded in the abstract.

---

## Three-paper summary

| Paper | Tier-2 verdict | Polish applied | Outstanding for ship |
|---|---|---|---|
| J38 | Ready | Known-issues hygiene | LaTeX conversion + rigor pass |
| J39 | Ready (§5.1 dup fixed) | §5.1 dedup + Known-issues hygiene | §6 checklist + venue scheduling |
| J40 | Ready (J-IDs harmonized) | Cover-letter J-IDs + example count + Known-issues hygiene | [J20] arXiv preprint + venue scheduling |

All three papers verified their scripts PASS and have a clear central claim with appropriate Tier-4 / Tier-A / Tier-2 honesty in scope.

---

## Files touched

- `05_papers/physics/J38/README.md` — Known-issues update.
- `05_papers/combinatorics/J39/README.md` — §5.1 deduplication + Known-issues update.
- `05_papers/interdisciplinary/J40/README.md` — §3 Dependencies harmonization + Known-issues update.
- `05_papers/interdisciplinary/J40/cover_letter.md` — Companion-submission J-IDs harmonized; Reproducibility example count corrected to seven.
- `05_papers/_staging/referee_reports/33_tier2_polish_J38_J39_J40.md` — this report.
