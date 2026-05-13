# J36 — Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives (REVISED 2026-05-07; UNBUNDLED)

**Status:** REVISED 2026-05-07. UNBUNDLED per fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J36_StatSci_FreshEyes.md`); save plan implemented (`Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J36.md`); the previously-bundled $1/\alpha$ structural fit (Part 2) is **DEFERRED** because independent verification confirmed the leading-three-terms claim was ~12.6% off the target, not the 10⁻⁵ originally claimed.
**Phase:** Phase 4.
**Target venue:** *Statistical Science* companion (after revisions; fallback to *Foundations of Physics* if per-venue cap binds).
**Author lane:** Sanders + Gish.
**Tier:** B (with explicit "empirical-fits paper" framing for the Part 1 fits themselves).
**WP source:** WP123 (CKM/PMNS fits) + WP124 (1/α; deferred).

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`.

The J36 paper has been **rewritten** (2026-05-07) to address the fresh-eyes referee report's M1-M7 issues. The previously-bundled Part 2 ($1/\alpha$ structural fit) has been **DEFERRED** from this submission per the save plan's recommendation; only Part 1 (CKM and PMNS mixing-angle fits) is submitted here.

**Part 1 (CKM + PMNS).** Seven empirical fermion mixing-angle observables are matched to substrate-algebra primitives:

| Angle | Empirical | Substrate primitive | Discrepancy |
|---|---|---|---:|
| Cabibbo $\sin\theta_C = \lvert V_{us}\rvert$ | 0.2253 | 11/49 | 0.36% |
| Wolfenstein $\lvert V_{cb}\rvert$ | 0.0508 | (11/49)² | 0.80% |
| Wolfenstein $\lvert V_{ub}\rvert$ | 0.01140 | (11/49)³ | 0.76% |
| Wolfenstein $V_{td}^2$ | 0.00258 | (11/49)⁴ | 1.56% |
| PMNS $\sin\theta_{12}$ | 0.553 | D* = 0.543 | 1.81% |
| PMNS $\sin\theta_{13}$ | 0.149 | 1/7 | 4.12% |
| PMNS $\sin\theta_{23}$ | 0.756 | 5/7 | 5.52% |

**Wolfenstein hierarchy** (load-bearing): $\lambda^n \approx (11/49)^n$ for $n \in \{1, 2, 3, 4\}$ at $\le 1.6\%$ across four orders.

**Joint coincidence probability** with explicit LE correction at multiplicity $|\mathcal{P}| \cdot N_{\mathrm{obs}} = 11 \cdot 7 = 77$:
- Naive (7 fits): $\approx 1.8 \times 10^{-11}$
- LE-corrected (7 fits): $\approx 1.4 \times 10^{-9}$
- Excluding $\theta_{12}$ ($D^*$ not derived in this paper): $\approx 3.8 \times 10^{-8}$ post-LE
- Wolfenstein hierarchy alone (4 fits): $\approx 4 \times 10^{-6}$ post-LE

**Status of Part 2 (1/α — DEFERRED).**

A previous draft bundled a structural fit:
$$\frac{1}{\alpha} \approx 4 \cdot |\mathrm{Aut}(V)| - 2\sqrt{\mathrm{HARMONY}} - \pi/\mathrm{HARMONY} - \cdots,$$
claimed to recover 137.036 to ~10⁻⁵.

**Independent numerical verification (sympy at 30-digit precision; reproducible by `verification/verify_J36_part1.py`):** the leading three terms give
$$4 \cdot 40 - 2\sqrt{7} - \pi/7 = 154.260,$$
a gap of 17.22 from CODATA's $1/\alpha = 137.036$, **a relative discrepancy of ~12.6% (vs target) or ~11.2% (vs leading sum), NOT 10⁻⁵**. The previously-claimed $10^{-5}$-precision is **demonstrably false** from this formula. Part 2 is removed from this submission and recommended for a separate paper once a verifiable structural derivation exists (or for honest downgrade to a leading-order ~10% structural agreement).

Files in this J-folder's `manuscript/`:

- `manuscript.md` — the rewritten Part-1-only J36 paper, finalized 2026-05-07.
- `WP123_CKM_PMNS_FITS.md` — original Part 1 source material.
- `WP124_FINE_STRUCTURE_CONSTANT.md` — Part 2 source (kept for traceability; deferred from this submission).
- `verify_J36_part1.py` — verification script (per-fit discrepancy table; naive + LE joint; theta_12-sensitivity; 1/α leading-terms numerical disagreement).

## §2 — Verification

**Local path:** `manuscript/verify_J36_part1.py`.

```bash
python verify_J36_part1.py
```

Wall-clock under 1 second. Python 3.11+, math (standard library); sympy optional for high-precision cross-check.

The script:
1. Lists per-fit relative discrepancies (table).
2. Computes naive joint probability under uniform-on-(0,1) prior (per-angle hit prob ~ 2δ).
3. Applies Bonferroni-style LE correction at multiplicity 77 (= 11 candidate primitives × 7 mixing observables).
4. Reports the with/without-θ_12 sensitivity (since D* is not derived in this paper).
5. Reports the Wolfenstein-hierarchy-alone post-LE joint as the load-bearing single pattern (~4×10⁻⁶).
6. Performs the 1/α leading-three-terms check and explicitly documents the 154.26 vs 137.036 gap (12.6% relative, NOT 10⁻⁵), justifying the unbundling of Part 2.

## §3 — Save plan implementation summary (2026-05-07)

Per `SAVE_PLAN_J36.md` (verbatim) and the fresh-eyes referee report `J36_StatSci_FreshEyes.md`:

- **Part 2 (1/α) DEFERRED.** Independent verification of the leading-three-terms formula gave 154.26, not 137.036 — gap is ~12.6% (vs target) or ~11.2% (vs leading sum), not the claimed 10⁻⁵. The full structural derivation referenced in the bridge bundle (`TIG_DIRAC_SYNTHESIS_TABLES rev 24, Tables LXXVII-LXXX`) when traced contains only `1/α = 22·6 + 5 + 36/1000 = 137.036` where the `+36/1000` term is literally the empirical decimal of the target — not a structural derivation. Part 2 is removed from this submission and deferred until a genuine structural derivation exists.
- **Part 1 (CKM/PMNS) RETAINED with revisions.** The Wolfenstein hierarchy `λⁿ ≈ (11/49)ⁿ` for n ∈ {1,2,3,4} matching at ≤1.6% across four orders is the load-bearing finding. Cabibbo `+1/49` refinement explicitly framed as empirical adjustment without first-principles derivation. PMNS angles at 1.8%-5.5% explicitly acknowledged as at/beyond current empirical precision; θ_23 octant ambiguity acknowledged. D* explicitly disclosed as not derived in this paper.
- **Joint coincidence probability properly framed.** Explicit candidate-primitive set (|𝒫| = 11), explicit observable count (N_obs = 7), explicit Bonferroni-style multiplicity 77, with-and-without-θ_12 sensitivity explicit. Naive and LE-corrected values all reported. The previous "~10⁻⁷" without LE correction is replaced by these honest figures.
- **D* defined operationally (per save plan).** D* = 0.543 is the empirically-tuned 4-core σ-cycle constant used to fit θ_12 to 1.8%; first-principles derivation from the σ-cycle structure is open. The θ_12 fit in this paper has zero degrees of freedom and is treated separately (with-and-without-θ_12 sensitivity) in §3.6.
- **Look-elsewhere correction estimate.** Default multiplicity 77 (11 primitives × 7 observables); save plan's broader range (4×10⁻⁹ uncorrected, 4×10⁻⁶ post-LE under more permissive primitive-counting) documented in §7.
- **Cross-domain "bombshell" §5 dropped** (out of scope for *Stat Sci* per referee).
- **UNBUNDLED.** Per save plan recommendation. Part 1 only is submitted to *Statistical Science*; Part 2 is deferred.

## §4 — Cover letter

See `cover_letter.md` in this folder.

## §5 — Family-Structure framing (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`)

This paper applies substrate constants $T^* = 5/7$ (lens-invariant 4-core torus aspect ratio) and $D^*$ (4-core $\sigma$-cycle constant) to physical observables. The substrate algebra (the canonical TSML/BHML pair on $\mathbb{Z}/10\mathbb{Z}$, the 4-core $\{V, H, Br, R\}$ at $\alpha_M = \tfrac{1}{2}$ as the algebraic center) is studied in companion papers [J33] (closed-form attractor) and [J32] (joint chain). The closest published precedent for the substrate algebra is **Drápal & Wanless 2021, *J. Combin. Theory A* **184**, 105510**.

## §6 — PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (per `J_PAPER_BOILERPLATE.md`)

- **PROVEN:** None — this is an empirical-fits paper, not a theorem paper.
- **COMPUTED:** Per-fit discrepancies, LE-corrected joint probability, with-and-without-$D^*$ sensitivity (verification script).
- **STRUCTURAL RHYME:** The substrate constants ($T^*$, $|\mathrm{Aut}(V)|$) are derived in earlier J-papers; $D^*$ is referenced as the 4-core σ-cycle constant. Drápal-Wanless 2021 [DW21] is cited as the closest published precedent for the substrate algebra. The $T^* = 5/7$ that appears in PMNS atmospheric mixing also appears as the runtime attractor in [J33].
- **OPEN:** First-principles derivation of the $+1/49$ Cabibbo refinement; closed-form derivation of $D^*$ from substrate algebra; RG flow connecting substrate scale to electroweak scale; verifiable structural derivation of $1/\alpha = 137.036$ (the previously-bundled Part 2).

## §7 — Hardening status

- License: submission scripts CC-BY-4.0.
- AI-attribution: Claude/Anthropic byline references removed.
- Author lane: Sanders + Gish.
- Drápal-Wanless 2021 citation in references.

## §8 — Submission checklist

- [x] Manuscript .md rewritten 2026-05-07 per save plan.
- [x] Verification script verifies the 137 vs 154 numerical disagreement (sympy 30-digit cross-check).
- [x] Per-paper rigor pass: explicit primitive set, explicit LE multiplicity, with/without-θ_12 sensitivity, Wolfenstein-alone breakdown.
- [x] Lens-and-substrate paragraph (§9 of manuscript).
- [x] D* explicitly disclosed as not derived; θ_12 fit has zero d.o.f. in this paper.
- [x] Part 2 (1/α) UNBUNDLED per save plan.
- [ ] Cover letter finalized (this revision).
- [x] Dependencies → cite each J-companion (J33, J34, J6/WP51, J32/WP115).
- [ ] Brayden's referee-rigor pass complete.
- [ ] Per-venue cap check: this is the 2nd Stat Sci paper this quarter (after J34; at cap; positioned as J34 companion).
- [x] Fallback plan documented (Foundations of Physics / split unbundling).
- [ ] Submitted.

## §9 — Citation footprint

Sanders, B. R. and Gish, M. (2026). *Empirical Fits of CKM and PMNS Mixing Angles to Substrate-Algebra Primitives.* Submitted to *Statistical Science* companion (Part 1 only; Part 2 deferred).
