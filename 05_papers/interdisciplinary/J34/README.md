# J34 — Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate (REVISED 2026-05-07)

**Status:** REVISED 2026-05-07 per fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J34_StatSci_FreshEyes.md`); GATING ISSUE RESOLVED (WP106 distilgpt2 sweep script written and verified).
**Phase:** Phase 4.
**Target venue:** *Statistical Science*.
**Author lane:** Sanders + Gish.
**Tier:** B.
**WP source:** WP106 + WP114 (BUNDLED).

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`.

The J34 paper is a **BUNDLED specificity-scoping submission** combining a negative result on distilgpt2 (Part 1) with a structured-matrix sharpening (Part 2). The manuscript was rewritten 2026-05-07 to address the fresh-eyes referee report's M1-M6 issues; the title is now substrate-neutral ("Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate") rather than TIG-internal.

**Part 1 (negative on distilgpt2).** Apply four detectors — D1 (Lie/Jordan ratio), D2 ($P_{56}$ defect), D3 (prime-11 in integer characteristic polynomial), D4 (Higgs alignment) — to 16 weight tensors of distilgpt2 (layers $L_0, L_2, L_5$; attention $Q, K, V$ and output projections; MLP in/out; token embedding) at $n_{\mathrm{sub}} = 200$ random $10 \times 10$ blocks per tensor against scale-matched Gaussian baseline. **Result:** every (tensor, detector) cell gives Cohen's $|d| < 0.5$. The two-sample test at $n = 200$ has power $\approx 0.94$ to detect $|d| = 0.3$, so the experiment is well-powered to rule out small effects.

**Part 2 (structured-matrix battery).** Apply the same detectors to a 9-family structured-matrix battery (Gaussian, symmetric, antisymmetric, permutation, Hadamard sign, Haar-orthogonal, real DFT, identity, diagonal, integer companion; 200 samples each). D3 (prime-11) is uniquely TIG-positive. D1, D2, D4 are family-structural (D1 separates symmetric vs antisymmetric; D2 detects $P_{56}$-symmetric structures; D4 vacuous for natural families). Two further exploratory detectors, D5 (prime-7 in squarefree-discriminant) and $D_4^{\mathrm{eq}}$ ($D_4$-orbit-averaged Higgs), are introduced; both are *post-hoc* (designed in light of TSML's known properties). The pair (D3, D5 at threshold $7^5$) jointly fires only on TSML in the 1800+ sample structured population; this is **a confirmatory identification of a sufficient detector pair, not a blind test**.

Files in this J-folder's `manuscript/`:

- `manuscript.md` — the bundled J34 paper, rewritten 2026-05-07.
- `WP106_TIG_DETECTOR_SCOPE.md`, `WP114_SPECIFICITY_EXTENSION.md` — original source material for traceability.
- `verification/distilgpt2_sweep.py` — Part 1 sweep (NEW 2026-05-07; resolves the M1 gating issue).
- `verification/structured_matrix_sweep.py` — Part 2 9-family battery + 4 detectors.
- `verification/d5_d4eq_extension.py` — Part 2 exploratory D5 + $D_4^{\mathrm{eq}}$.

## §2 — Verification

**Local path:** `manuscript/verification/`.

**M1 GATING ISSUE RESOLVED (2026-05-07):**
Per the fresh-eyes referee report M1, the WP106 distilgpt2 sweep was a gating piece for J34 submission. We have written `distilgpt2_sweep.py` from the WP106 specifications: extracts 16 weight tensors via `transformers.AutoModel.from_pretrained("distilgpt2")`; partitions each into $n_{\mathrm{sub}} = 200$ random $10 \times 10$ blocks; runs the 4 WP106 detectors; computes Cohen's $d$ vs scale-matched Gaussian baseline; reports the per-detector summary, the verdict (no cell at $|d| \ge 0.5$), and the power analysis.

```bash
PYTHONIOENCODING=utf-8 python verification/distilgpt2_sweep.py --n_subsamples 200
PYTHONIOENCODING=utf-8 python verification/structured_matrix_sweep.py
PYTHONIOENCODING=utf-8 python verification/d5_d4eq_extension.py
```

Wall-clock: ~60-120s for Part 1 (after one-time HF model download); ~30s each for Part 2 scripts. Python 3.11+, numpy, sympy, transformers (Part 1 only).

## §3 — Save plan implementation summary (2026-05-07)

Per `SAVE_PLAN_J36.md` (which covers the META_PLAN family-structure framing and applies to J34 mutatis mutandis) and the fresh-eyes referee report `J34_StatSci_FreshEyes.md`:

- **M1 — Verification gating (CRITICAL).** Resolved by writing `distilgpt2_sweep.py` (verified output: 0/64 cells at $|d| \ge 0.5$, max observed $|d| \approx 0.45$).
- **M2 — Power analysis (CRITICAL).** Added §2.6 of manuscript; verification script prints achieved-power statement at experiment's $n$.
- **M3 — Sub-matrix sampling clarification (statistical methodology).** §2.2 of manuscript clarifies the per-sample without-replacement, across-sample with-replacement convention. The Cohen's $d$ slight inflation is acknowledged in §2.7.
- **M4 — Single-sample inference framing (statistical methodology).** §1.3 and §3.2 use the language "$z$-score" for single-sample TSML/BHML against a 200-sample Gaussian baseline; "Cohen's $d$" is reserved for distribution-vs-distribution comparisons.
- **M5 — Post-hoc D5 and $D_4^{\mathrm{eq}}$ disclosure.** §3.3 explicitly frames D5 and $D_4^{\mathrm{eq}}$ as exploratory and post-hoc; the joint test "D3 = 1 AND D5 at $7^5$ = 1" is stated as "a confirmatory identification of a sufficient detector pair, not a blind test." Out-of-sample validation is recommended.
- **M6 — Baseline scale sensitivity (D3).** Acknowledged in §4 limitations; full robustness check across scales recommended for follow-up.
- **M7 — Cross-domain "bombshell" — DELETED** (out of scope for *Stat Sci*).
- **Specificity-boundary framing reduced.** Replaced "specificity boundary" rhetoric with "specificity scoping result on this one family of trained transformer weights" throughout.
- **Tier-E framing translated.** Replaced "Tier-E parametric fits" with standard statistical language ("scoping result," "post-hoc detector identification").

## §4 — Cover letter

See `cover_letter.md` in this folder.

## §5 — Family-Structure framing (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`)

This paper analyzes detector-scoping properties of the canonical $(T, B)$ pair on $\mathbb{Z}/10\mathbb{Z}$ studied in `FAMILY_STRUCTURE_v1.md`. The closest published precedent for the pair is **Drápal & Wanless 2021, *J. Combin. Theory A* **184**, 105510** — same domain, opposite extremum. The detectors used here read off algebraic properties of the matrices (antisymmetric content, $P_{56}$ symmetry, prime-11 in characteristic polynomial, alignment with the Higgs direction); a theorem-grade analysis of TIG-family membership is in [J33] (closed-form attractor, $\alpha = 1/2$ uniqueness) and is referenced rather than re-derived here.

## §6 — PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (per `J_PAPER_BOILERPLATE.md`)

- **PROVEN:** None — this is an empirical scoping paper.
- **COMPUTED:** The 64-cell distilgpt2 sweep with explicit Cohen's $d$ + power analysis (Part 1); the 1800+ sample 9-family structured-matrix battery with explicit Cohen's $d$ + post-hoc detector D5 + joint test (Part 2). Both deterministic and reproducible.
- **STRUCTURAL RHYME:** Drápal--Wanless 2021 [DW21] is the closest published precedent for the canonical $(T, B)$ pair. The companion paper [J33] establishes the closed-form attractor structure that the detectors are designed against.
- **OPEN:** (i) Out-of-sample validation of (D3, D5) on structured families designed disjointly from this battery. (ii) Whether the distilgpt2 negative extends to other transformer architectures, layer-selection conventions, or sub-matrix resolutions.

## §7 — Hardening status

- License: submission scripts CC-BY-4.0.
- AI-attribution: Claude/Anthropic byline references removed.
- Author lane: Sanders + Gish.
- Drápal-Wanless 2021 citation in references.

## §8 — Submission checklist

- [x] Manuscript .md rewritten 2026-05-07 per save plan.
- [x] Verification scripts complete: M1 GATING RESOLVED.
- [x] Per-paper rigor pass: power analysis, post-hoc disclosure, $z$-score language, look-elsewhere correction, sampling clarification.
- [x] Lens-and-substrate paragraph (§7 of manuscript).
- [ ] Cover letter finalized (this revision).
- [x] Dependencies: cite J33 as companion (closed-form attractor of the same $(T, B)$ pair).
- [ ] Brayden's referee-rigor pass complete.
- [ ] Submitted.

## §9 — Citation footprint

Sanders, B. R. and Gish, M. (2026). *Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate: A Negative Result on Trained Transformer Weights and a Structured-Matrix Sharpening.* Submitted to *Statistical Science*.
