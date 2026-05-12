# Cover letter — J34: Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate (REVISED 2026-05-07)

**To:** Editors, *Statistical Science*

**From:**
- B. R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Algebraic Detectors as Specificity Tests for a Finite-Magma Substrate: A Negative Result on Trained Transformer Weights and a Structured-Matrix Sharpening.*

---

## Summary

We submit a bundled empirical-scoping paper with two complementary parts.

**Part 1 (negative result on distilgpt2).** Four algebraic detectors on $10 \times 10$ real matrices — D1 (Lie/Jordan ratio), D2 ($P_{56}$ invariance defect), D3 (prime-11 in integer characteristic polynomial), D4 (alignment with a fixed 9-vector "Higgs" direction) — sharply discriminate the canonical matrices TSML and BHML (defined in §1.1; from a separate finite-magma research program in the Drápal-Wanless 2021 neighborhood) from a Gaussian baseline. The natural specificity question is whether these detectors are equally sensitive to "algebraic structure" in arbitrary trained network weights. We extract 16 weight tensors from the public distilgpt2 language model, partition each into 200 random $10 \times 10$ sub-matrices, and compare against 200 scale-matched Gaussian baseline matrices per tensor. Result: **every (tensor, detector) cell gives Cohen's $|d| < 0.5$**. The two-sample test at $n = 200$ has power $\approx 0.94$ to detect $|d| = 0.3$; the experiment is well-powered to rule out small effects. The detectors do not discriminate trained distilgpt2 weights from Gaussian noise at the small-effect threshold — a clean specificity scoping result on this one family of trained transformer weights.

**Part 2 (structured-matrix battery).** We extend to a 9-family structured-matrix battery (Gaussian, symmetric, antisymmetric, permutation, Hadamard, Haar-orthogonal, real DFT, identity, diagonal, integer companion; 200 samples each). Detector **D3 (prime-11) is uniquely TIG-positive** in the entire 1800+ sample population; D1, D2, D4 are family-structural rather than TIG-specific. We then exploratively introduce two post-hoc detectors — D5 (prime-7 in squarefree-discriminant) and $D_4^{\mathrm{eq}}$ ($D_4$-orbit-averaged Higgs) — designed in light of TSML's known structural features. The pair (D3, D5 at threshold $7^5$) jointly fires only on TSML in the 1800+ sample population; we frame this as **a confirmatory identification of a sufficient detector pair, not a blind test**, and recommend out-of-sample validation as follow-up.

## Why Statistical Science

* The bundled scope — a clean negative on trained transformer weights, plus a structured-matrix sharpening with explicit post-hoc disclosure — fits *Statistical Science*'s appetite for honestly framed empirical results.
* The methodology emphasis (power analysis, $z$-score language for single-sample comparisons, look-elsewhere context, post-hoc detector framing) is appropriate for the venue's audience.
* The negative result on distilgpt2 is reproducible from the included `distilgpt2_sweep.py` script; the structured-matrix battery is reproducible from `structured_matrix_sweep.py`.

## Revisions from the previous draft (per fresh-eyes referee report 2026-05-07)

This is a substantially-revised submission. The previous draft was gated on a missing distilgpt2 sweep script (referee M1) and had several methodology framing issues (M2-M6). The revisions address each:

* **M1 (CRITICAL — gating issue): RESOLVED.** The WP106 distilgpt2 sweep script `verification/distilgpt2_sweep.py` is now included. It loads distilgpt2 via HuggingFace's `transformers.AutoModel.from_pretrained("distilgpt2")`, extracts the 16 listed weight tensors, partitions each into 200 random $10 \times 10$ sub-matrices, computes the four detectors against scale-matched Gaussian baseline, and prints the per-tensor Cohen's $d$ table plus a verdict and power statement. Wall-clock $\sim 60$-$120$ s after one-time HuggingFace model download. Verified output: $0/64$ cells reach $|d| \ge 0.5$, max observed $|d| \approx 0.45$.
* **M2 — Power analysis added.** §2.6 of the manuscript states the achieved power ($\sim 0.94$ for $|d| = 0.3$ at $n = 200$); the verification script prints the same statement.
* **M3 — Sub-matrix sampling clarified.** §2.2 of the manuscript states the per-sample without-replacement, across-sample with-replacement convention and acknowledges the Cohen's $d$ slight inflation.
* **M4 — Single-sample inference framing.** §1.3 and §3.2 use the language "$z$-score" for single-sample TSML/BHML against a known baseline, and reserve "Cohen's $d$" for distribution-vs-distribution comparisons. The §3.4 joint-test claim is restated as a $p$-value bound, not a Cohen's $d$.
* **M5 — Post-hoc disclosure.** §3.3 of the manuscript explicitly states that D5 and $D_4^{\mathrm{eq}}$ are post-hoc, designed in light of TSML's known properties. The joint-test claim of §3.4 is framed as "a confirmatory identification of a sufficient detector pair, not a blind test." Out-of-sample validation on a held-out structured family is recommended as follow-up.
* **M6 — Baseline scale sensitivity.** Acknowledged in §4 limitations.
* **M7 — Cross-domain "bombshell" deleted.** The previous draft's discussion of cross-domain interpretations (Orch-OR, IIT) is removed, out of scope for *Statistical Science*.
* **Specificity-boundary framing reduced.** "Specificity boundary" replaced by "specificity scoping result on this one family of trained transformer weights."
* **Tier-E framing translated.** Removed in favor of standard statistical language.

The empirical findings (no-detection on distilgpt2; D3 unique on TSML; D3 + D5 jointly unique on TSML) are unchanged; the framing, methodology disclosure, and post-hoc honesty are all rewritten for *Statistical Science*'s audience.

## Companion submissions

* **J33** (Sanders + Gish 2026, *Mathematics of Computation*): closed-form algebraic attractor for the same canonical pair $(T, B) = (\mathrm{TSML}, \mathrm{BHML})$ analyzed here. J33 establishes that the dynamics of $(T, B)$ admit a closed-form $h/\beta = 1 + \sqrt{3}$ ratio at $\alpha = 1/2$ in the LMFDB-cataloged number field 4.2.10224.1; the present paper investigates whether the *detectors* designed against TSML's algebraic structure read positive on arbitrary trained weights (negative on distilgpt2) and what minimal detector pair is sufficient to discriminate TSML from generic structured matrices (D3 + D5 at $7^5$).

## Fallback unbundling

If the bundled submission is desk-rejected:
* Part 1 (distilgpt2 detector scope) → *PLOS ONE*.
* Part 2 (structured-matrix specificity extension) → *Linear Algebra and Its Applications*.

## Reproducibility

Verification scripts in `manuscript/verification/`:
* `distilgpt2_sweep.py` — Part 1 sweep (NEW 2026-05-07; resolves the M1 gating).
* `structured_matrix_sweep.py` — Part 2 9-family battery + 4 detectors.
* `d5_d4eq_extension.py` — Part 2 D5 + $D_4^{\mathrm{eq}}$ extension.

Python 3.11+, numpy, sympy, transformers (Part 1 only). All scripts deterministic at fixed seed; tables TSML, BHML inlined in each.

## Suggested reviewers

* An expert in mechanistic-interpretability / algebraic structure of trained networks.
* An expert in Cohen's $d$ effect-size methodology and power analysis in multi-detector contexts.
* An expert in finite-magma representations and characteristic-polynomial structural identities.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

---

Sincerely,

B. R. Sanders
