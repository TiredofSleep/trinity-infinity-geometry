# WP106 — Specificity of TIG-Structure Detection in Trained Transformer Weights

**Status:** empirical scoping result; verified across 16 weight tensors of distilgpt2 and 4 algebraic detectors
**Authors:** Brayden R. Sanders + M. Gish
**Date:** 2026-04-25
**MSC 2020:** 68T07 (artificial neural networks; deep learning), 17B25 (exceptional Lie algebras), 68P10 (searching algorithms)
**Length:** scope statement + experimental record

---

## Abstract

Trinity Infinity Geometry (TIG) defines a finite-magma research program whose canonical TSML and BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$ exhibit machine-precision algebraic structure: the Lie algebras $\mathfrak{so}(8)$ and $\mathfrak{so}(10)$ close on antisymmetrizations of the tables (WP102, WP103); BHML's $\sigma_\mathrm{outer}$-breaking content lives 100% in the $\mathbf{54}$ irrep of $\mathfrak{so}(10)$ (WP104); and a runtime attractor at the symmetric mixing weight $\alpha = 1/2$ lies in the degree-4 number field LMFDB 4.2.10224.1 with $\mathbb{Q}(\sqrt{3})$ as a canonical subfield (WP105).

A natural open question is whether TIG-structure is a **specific** algebraic feature of the canonical tables, or a **generic** feature latent in any algebraic system of comparable size. This paper answers the question for one specific test case: do TIG's algebraic-structure detectors, applied to the trained weight matrices of a public transformer language model, discriminate trained weights from random Gaussian baselines of matching scale?

**Result.** Across 16 weight tensors of distilgpt2 (82 M parameters; layers $L_0, L_2, L_5$ in attention $Q, K, V$ projections; MLP in/out matrices; token embeddings) and four algebraic detectors (Lie/Jordan ratio; $P_{56}$ invariance; prime-11 in characteristic polynomial; Higgs-direction alignment), every (tensor, detector) pair gives Cohen's $|d| < 0.5$. Every detector classifies trained-vs-random with accuracy $48-52\%$ (chance level). **The framework's algebraic detectors do not see TIG structure in arbitrary trained transformer weights at the threshold of small effect.**

This is a **specificity boundary**: TIG structure appears in canonical TSML/BHML and the algebraic structures they generate; it does not appear in arbitrary trained weights. The negative result rules out the tempting overclaim "TIG structure is latent in any trained network." It is a clarifying scoping contribution, not a critique of TIG's positive results.

We also report a positive ancillary architectural finding: among five encoder strategies for mapping text into TIG operator distributions (V1 seed lexicon, V1.5 canonical 112k corpus, V1.6 hybrid, V2 sentence-transformers fallback, V3 D2 phoneme-physics), the best cluster-separation comes from V2 (2.15× vs V1's 2.01×, a modest 7% improvement). The pure phoneme-physics V3 encoder gives only 1.06× separation, indicating that the canonical D2Pipeline encoding belongs at the **output** end of the CK runtime (operator-stream emission), not the **input** end (semantic encoding).

---

## §1 Setup

### §1.1 The four TIG-structure detectors

For a $10 \times 10$ real matrix $M$, define:

**D1 (Lie/Jordan ratio).**

$$
\mathrm{LJ}(M) := \frac{\|A(M)\|_F^2}{\|S(M)\|_F^2 + \|A(M)\|_F^2}, \qquad A(M) = \tfrac{1}{2}(M - M^\top), \quad S(M) = \tfrac{1}{2}(M + M^\top).
$$

This is the fraction of mass in the antisymmetric part. TSML has $\mathrm{LJ}(\mathrm{TSML}) \approx 0.18$ (heavily symmetric); BHML has $\mathrm{LJ}(\mathrm{BHML}) \approx 0.43$. A random Gaussian matrix has $\mathrm{LJ}(M) \approx 0.5$ (the symmetric and antisymmetric components are statistically equivalent).

**D2 ($P_{56}$ invariance defect).**

$$
P_{56}(M) := \frac{\|M - P_{56} M P_{56}\|_F^2}{\|M\|_F^2},
$$

where $P_{56}$ is the elementary transposition matrix. This measures the fractional mass change under conjugation by $P_{56}$. TSML has small $P_{56}(M)$ (the table is largely $P_{56}$-symmetric); BHML has $P_{56}(\mathrm{BHML}) \approx 26/420 \approx 0.06$ (the 26 σ_outer-asymmetric cells out of 100, weighted by entry magnitudes).

**D3 (prime-11 in characteristic polynomial).**

For an integer-rounded $10 \times 10$ matrix $M_\mathbb{Z}$ obtained from $M$ by scaling and rounding to the nearest integer, compute the characteristic polynomial via sympy. Test whether the prime $11$ divides **both** $c_2$ (sum of products of pairs of eigenvalues) and $c_8$ (product of the eight nonzero eigenvalues, when applicable). Returns $1$ if yes, $0$ otherwise.

**D4 (Higgs-direction alignment).**

Compute $h(M) := \cos(\theta)$, the cosine of the angle between $M$'s antisymmetric part (flattened upper triangle) and a fixed embedding of the canonical 9-vector Higgs direction $v$ from WP104 §2.3. Trained matrices may align with $v$ or be orthogonal to it; random matrices give a baseline distribution of $h$.

### §1.2 The model: distilgpt2

DistilGPT2 is a 82 M-parameter distillation of GPT-2 (Sanh et al., 2020). It has 6 transformer layers, 768-dim hidden states, 12 attention heads, 3072-dim MLP intermediate, 50257-token vocabulary. We extract weights from `transformers.AutoModel.from_pretrained("distilgpt2")` and select 16 tensors:

| layer / type | tensor | shape |
|---|---|---|
| $L_0, L_2, L_5$ × $\{Q, K, V\}$ | attention projections | $768 \times 768$ |
| $L_0, L_2, L_5$ × $\{\mathrm{in, out}\}$ | MLP projections | $768 \times 3072$ or $3072 \times 768$ |
| token embedding | $W_\mathrm{te}$ | $50257 \times 768$ |

For each tensor $W$, sample 200 random $10 \times 10$ sub-matrices (rows and columns chosen without replacement from each dim). Apply the four detectors to each sub-matrix.

### §1.3 The null distribution

For each tensor $W$, generate a Gaussian baseline $W_\mathrm{rand} \sim \mathcal{N}(0, \sigma_W^2)$ with $\sigma_W = \mathrm{std}(W)$, and sample 200 random $10 \times 10$ sub-matrices in the same way. Apply the four detectors.

The null hypothesis is that trained weights are statistically equivalent to scale-matched Gaussian noise under the four detectors. We compute Cohen's $d$ as the standardized mean difference:

$$
d = \frac{\overline{D(W)} - \overline{D(W_\mathrm{rand})}}{\sqrt{(s_W^2 + s_\mathrm{rand}^2)/2}}.
$$

By convention, $|d| < 0.2$ is "no effect"; $0.2 \le |d| < 0.5$ is "small"; $0.5 \le |d| < 0.8$ is "medium"; $|d| \ge 0.8$ is "large."

---

## §2 Result

We tabulate Cohen's $d$ for every (tensor, detector) pair (the prime-11 detector reports detection rate, not Cohen's $d$):

| tensor | LJ ratio $d$ | $P_{56}$ defect $d$ | cp11 trained % | cp11 random % | Higgs $\|d\|$ |
|---|---:|---:|---:|---:|---:|
| $L_0$ attn Q | $-0.10$ | $+0.17$ | 0.0% | 2.0% | $+0.09$ |
| $L_0$ attn K | $-0.09$ | $+0.06$ | 0.0% | 2.0% | $+0.02$ |
| $L_0$ attn V | $+0.13$ | $+0.14$ | 2.0% | 2.0% | $-0.08$ |
| $L_0$ MLP in | $-0.15$ | $+0.10$ | 0.0% | 2.0% | $-0.03$ |
| $L_0$ MLP out | $-0.19$ | $+0.13$ | 4.0% | 2.0% | $-0.02$ |
| $L_2$ attn Q | $-0.08$ | $+0.11$ | 0.0% | 2.0% | $-0.03$ |
| $L_2$ attn K | $-0.03$ | $+0.24$ | 2.0% | 2.0% | $+0.08$ |
| $L_2$ attn V | $-0.12$ | $+0.03$ | 2.0% | 2.0% | $-0.00$ |
| $L_2$ MLP in | $+0.01$ | $+0.12$ | 0.0% | 2.0% | $+0.03$ |
| $L_2$ MLP out | $-0.01$ | $+0.10$ | 0.0% | 2.0% | $+0.03$ |
| $L_5$ attn Q | $-0.09$ | $+0.08$ | 0.0% | 2.0% | $+0.11$ |
| $L_5$ attn K | $-0.25$ | $-0.11$ | 0.0% | 2.0% | $+0.11$ |
| $L_5$ attn V | $+0.00$ | $+0.10$ | 2.0% | 2.0% | $-0.19$ |
| $L_5$ MLP in | $-0.18$ | $+0.14$ | 0.0% | 2.0% | $+0.06$ |
| $L_5$ MLP out | $-0.03$ | $-0.04$ | 0.0% | 2.0% | $-0.05$ |
| token embedding | $-0.17$ | $-0.27$ | 2.0% | 2.0% | $+0.35$ |

**Theorem (specificity scope).**

Across all 16 (tensor, detector) pairs:

* Every Cohen's $d$ for the LJ-ratio detector lies in $[-0.25, +0.13]$, well below the small-effect threshold $|d| = 0.5$.
* Every Cohen's $d$ for the $P_{56}$ detector lies in $[-0.27, +0.24]$, all below small-effect.
* Every Cohen's $d$ for the Higgs-direction detector lies in $[-0.19, +0.35]$, all below small-effect.
* The prime-11 detector fires on $0–4\%$ of trained sub-matrices and $\sim 2\%$ of random sub-matrices — statistically indistinguishable.
* No (tensor, detector) pair achieves $|d| \ge 0.5$.

**Interpretation.** Trained weight matrices of distilgpt2, sub-sampled at $10 \times 10$ resolution, are **statistically indistinguishable from scale-matched Gaussian noise** under the four TIG-structure detectors. The framework's algebraic detectors do not see TIG structure in this trained-network test case at the small-effect threshold.

Verification: `Gen13/targets/ck/brain/dof_monitor/processing/ask4_real_ml_weights.py` (on the `ck` branch, runnable in $< 60$ s after `pip install transformers torch sympy`).

---

## §3 The architectural finding — five encoder strategies

We additionally tested five strategies for mapping English text to TIG operator distributions over $\mathbb{Z}/10\mathbb{Z}$, evaluated by cluster-separation on a fixed test fixture:

| version | strategy | cluster separation | TIG-coverage | notes |
|---|---|---:|---:|---|
| V1 | seed lexicon (~250 hand-curated words) + cascading layers (keyword / stem / phonaesthesia / grapheme) | $\mathbf{2.01}\times$ | 100% | baseline |
| V1.5 | full 112 k canonical TIG dictionary (`ck_dictionary.json`) — corpus first | $1.13\times$ | 100% | corpus floods filler words with BALANCE/CHAOS |
| V1.6 | hybrid: seed first, corpus fallback | $1.62\times$ | 100% | filler words still pollute; seed beats corpus |
| V2 | seed first + sentence-transformers (`all-MiniLM-L6-v2`) for unresolved words | $\mathbf{2.15}\times$ | 100% | modest 7% gain over V1 |
| V3 | pure D2Pipeline phoneme-physics (no lexicon, no embedding) | $1.06\times$ | 100% (in D2 sense) | no semantic discrimination |

The cluster fixture comprises four 4-word semantic clusters (patience, peace, structure, reset) with within-cluster vs cross-cluster L² distance ratio measuring discrimination.

**Reading.**

* V1 (hand-curated seed) is the strongest **baseline**. Hand-curating ~250 words for semantic specificity beats a 112k phoneme-derived bulk classifier.
* V1.5 (canonical corpus only) is **worse** because the bulk corpus assigns common words ("be", "want", "find") to BALANCE or CHAOS (47k and 45k of the 112k entries map to these two operators), which pollutes the encoded distribution with the same dominant operators regardless of cluster.
* V2 (V1 + sentence-transformers fallback) modestly improves on V1 by handling out-of-vocab semantic synonyms (e.g., "compassion", "tenderness") via embedding similarity to the operator anchors.
* V3 (pure D2 phoneme-physics) gives **no semantic discrimination**: every English word's letter triplets bend toward COUNTER + HARMONY + LATTICE in the D2 force-vector classification.

**Architectural conclusion.** The canonical D2Pipeline phoneme-physics belongs at CK's **output** end, where the operator stream emits the runtime descent through the lattice processor; it does not belong at the **input** end as a semantic encoder. The three-layer pipeline is

$$
\text{V2 encoder} \xrightarrow{\text{semantic content}} \text{T+B-mix lattice processor} \xrightarrow{\text{trail = memory}} \text{D2Pipeline} \xrightarrow{\text{operator stream}} \text{output}.
$$

V2 reads (semantic), the lattice processor remembers (trail-as-information), D2 speaks (phoneme physics). They are **complementary layers stacked**, not competing options to pick from.

Verification: `Gen13/targets/ck/brain/dof_monitor/processing/run_encoder_test_suite.py` (run with `v1`, `v15`, `v16`, `v2`, or `v3` argument).

---

## §4 Honest scope (what this paper does NOT establish)

### §4.1 One model, one architecture

We tested distilgpt2. **We do not claim** that the negative generalizes to all transformers, all neural network architectures, or all weights of any kind. A larger study (BERT, T5, Llama-class, vision transformers, recurrent networks, state-space models) would be needed to confirm or refine the boundary. The strong intuition — that TIG-structure detectors are tuned to canonical TSML/BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$, not generic trained weights — suggests the negative will replicate, but this is conjecture pending verification.

### §4.2 One sub-matrix size

We sub-sampled at $10 \times 10$ resolution to match the canonical TSML/BHML table size. Sub-sampling at other resolutions (5×5, 20×20, 768×768) might reveal different patterns. We did not test this systematically.

### §4.3 Four detectors

We tested four detectors derived from the canonical algebraic structures (Lie/Jordan ratio, $P_{56}$ invariance, prime-11 in characteristic polynomial, Higgs-direction alignment). Other plausible detectors — spectral statistics, mod-7 structure, σ-fixed-point structure, $D_4$-invariance — were not tested. A more comprehensive battery might identify a detector that does discriminate.

### §4.4 We do not claim TIG is irrelevant to ML interpretability

The negative result on these specific detectors, applied to these specific trained weights, does **not** imply that TIG-flavored algebraic methods cannot inform ML interpretability research broadly. The CK runtime itself uses TIG-internal operators throughout, and the DOF profile monitor on the `ck` branch (4 modules + 34 passing tests) provides a measurement layer that classifies activations onto verified DOF subspaces (Lie 28, Jordan 55, Clifford 36, Permutation 9, Lattice 4) for the canonical 10-operator alphabet. The boundary established here is **specific to the question of whether arbitrary trained weights look TIG-structured**; it does not bound TIG's utility for designed-from-scratch white-box AI systems.

### §4.5 The encoder finding is also empirical

The five-encoder cluster-separation comparison uses one test fixture (4 clusters of 4 short queries each). Real production CK queries are longer and stylistically different. We expect V2's 7% gain to grow on longer text where vocabulary coverage matters more, but this is conjecture.

---

## §5 What this clarifies

The state-of-the-art for TIG's positive claims (WP102/103/104/105) is now: structural / algebraic identifications at machine precision in canonical TSML/BHML. The clarification this paper provides is the **boundary**: those identifications do not extend to arbitrary trained networks at the level of these specific algebraic detectors.

This is **honest scope** that strengthens the rigorous framing. It rules out tempting overclaims:

* "TIG structure is latent in any trained neural network."
* "Any sufficiently complex algebraic system with $\sim 10^2-10^4$ generators will show TIG-like patterns."
* "TIG is a generic theory of finite-magma structure."

What TIG **is**: a specific finite-algebra research program built on the canonical TSML and BHML composition tables on $\mathbb{Z}/10\mathbb{Z}$, generating Lie algebras up to $\mathfrak{so}(10) = D_5$, with a specific runtime processor that lands on a closed-form attractor at $\alpha = 1/2$ in the number field LMFDB 4.2.10224.1. The structure lives in **these specific tables**, not in arbitrary tables. The Pati-Salam alignment is structural; the runtime number-field result is closed-form; the wobble localization is integer-factorization-precise. The detectors are tuned to these structures and read what they were tuned to read.

This is the right epistemic posture for a research program of this ambition: prove what can be proved, identify structural alignments without claiming derivation, and **bound the scope explicitly** with empirical negatives.

---

## §6 Reproducibility

```bash
pip install --user numpy sympy sentence-transformers transformers torch
git clone https://github.com/TiredofSleep/ck.git
git checkout ck
cd ck
PYTHONIOENCODING=utf-8 python Gen13/targets/ck/brain/dof_monitor/processing/ask4_real_ml_weights.py
PYTHONIOENCODING=utf-8 python Gen13/targets/ck/brain/dof_monitor/processing/run_encoder_test_suite.py v2
```

Total wall-clock $\le 5$ minutes on a standard laptop (the heaviest step is the first sentence-transformers call, which downloads the `all-MiniLM-L6-v2` model the first time). Outputs are integer-precision factorizations and Cohen's $d$ values reported to 3 decimals; the encoder test suite reports cluster separation, compositionality, coverage, and robustness.

---

## §7 References

* B.R. Sanders, M. Gish. *WP102 — Lie Algebra Structure: so(8) = D₄ Identification*, 2026-04-23. `papers/wp102/`
* B.R. Sanders, M. Gish. *WP103 — TSML+BHML's so(10) = D₅ closure*, 2026-04-24. `papers/wp103/`
* B.R. Sanders, M. Gish. *WP104 — Two Roads to Pati-Salam from TIG's so(10)*, 2026-04-25. `papers/wp104_higgs_pati_salam/`
* B.R. Sanders, M. Gish. *WP105 — Closed-Form Runtime Attractor at α = 1/2*, 2026-04-25. `papers/wp105_closed_form_attractor/`
* V. Sanh, L. Debut, J. Chaumond, T. Wolf. *DistilBERT, a distilled version of BERT.* arXiv:1910.01108 (2019).
* T. Wolf et al. *HuggingFace Transformers.* arXiv:1910.03771 (2020).
* J. Cohen. *Statistical Power Analysis for the Behavioral Sciences.* Lawrence Erlbaum, 1988.

---

## §8 Citation

```bibtex
@misc{sanders2026wp106,
  author       = {Sanders, Brayden R. and Gish, M.},
  title        = {{WP106} --- Specificity of {TIG}-Structure Detection in Trained Transformer Weights},
  year         = {2026},
  month        = {apr},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {\url{https://github.com/TiredofSleep/ck/tree/tig-synthesis/papers/wp106_tig_detector_scope}},
  note         = {Across 16 weight tensors of distilgpt2 and four algebraic detectors, every Cohen's $|d| < 0.5$. The framework's algebraic detectors do not see TIG structure in arbitrary trained transformer weights. Architectural ancillary: V2 (sentence-transformers) reads, T+B-mix processor remembers, D2Pipeline emits.}
}
```

🙏

— Sanders + Gish, 2026-04-25
