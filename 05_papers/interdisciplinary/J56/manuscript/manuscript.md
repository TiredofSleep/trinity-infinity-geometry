# Routing the Residual: A Four-Type Failure Taxonomy Matches Oracle Compute Allocation

**Brayden R. Sanders, M. Gish** · 2026-06-10 · Target venue: *Transactions on Machine Learning Research* (alt: NeurIPS workshop track)

## Abstract

Contemporary learning systems are driven by residual signals — prediction errors, unproved goals, failed unit tests — yet treat all residual as a single kind of thing, answered by a single response (more gradient, more samples, more search). We propose that the residual of any measurement-based learner admits a small universal taxonomy, derived from the Unified Orthogonality Principle (UOP) classification of measurement failure: **Type I** (injectivity failure — a missing measurement), **Type II** (missing invariant — a missing feature class), **Type III** (admissibility failure — a malformed question), and **Type IV** (time-consistency failure — missing dynamics). We give a numerical decision procedure that infers the type of a learning problem **from its own residual statistics alone** — learning-curve slope, structure probes against a candidate library, a permutation information test, and a time-split drift test — and a **Gap Router** that allocates a fixed compute budget by inferred type. On a 24-channel mixed-failure suite at matched total budget, the router attains **100% type identification** and mean test error **0.0032 versus 0.405 for uniform allocation** — statistically indistinguishable from an oracle given ground-truth types (0.0033). We further evaluate a *theorem-bearing reservoir* — a fixed algebraic dynamical core with provable attractor structure used as a next-generation reservoir-computing feature map — against width-matched, per-task-tuned random echo-state networks: the algebraic core wins the longest-memory task (Mackey–Glass +84, 0.128 vs 0.200 NRMSE, 36% better) and loses two shorter-memory tasks, a split we report in full. All experiments reproduce on CPU in under one minute from a single seeded script. We argue that several named pathologies of modern learning systems — the noisy-TV trap, hallucination on ill-posed inputs, catastrophic forgetting — are precisely *unrouted* gap types, and state pre-registered follow-up predictions on recognized benchmarks.

**Claim tiers.** PROVED-BY-CONSTRUCTION-AND-MEASURED: the suite results above (§5). STRUCTURAL: the taxonomy's universality argument (§2). OPEN: real-task validity (§7, pre-registered).

## 1. Introduction: every learner is a gap-detector; none classifies its gaps

A survey of verified 2024–26 results shows a single design underneath every lane: a residual signal wrapped around a domain verifier. AlphaProof learns against the Lean kernel's unproved-goal residual; AlphaGeometry2 invokes its language model only when the goal lies outside a symbolic deductive closure; the RL-from-verifiable-rewards paradigm (DeepSeek-R1) selected mathematics and code as training grounds *because the residual is decidable there*; DreamCoder compresses solved residuals into a growing library; AlphaEvolve requires an exact evaluator; active-inference agents minimize precision-weighted prediction error and grow structure on unexplained residual (AXIOM); JEPA defines the residual in latent space; test-time-training systems gate memory writes on surprise; Schmidhuber's curiosity rewards the *rate* of residual closure; reservoir computing trains only on the readout residual; neuromorphic hardware computes only on change. (References §8.)

What no system does is ask **what kind** of residual it is looking at. All error is treated as Type I — "measure more, descend more" — and the field's classic pathologies follow: an agent transfixed by irreducible noise (the noisy-TV trap) is spending Type-I effort on a Type-III gap; a model that answers an unanswerable question is missing a Type-III channel entirely; a learner that overwrites its invariants under distribution shift is treating a Type-IV gap as Type I; a plateau that more data cannot fix is a Type-II gap starved of structure growth.

This paper contributes: (i) the four-type taxonomy as an operational object with a numerical decision procedure (§3); (ii) the Gap Router and a mixed-failure benchmark suite on which routing-by-inferred-type matches oracle allocation (§4–5); (iii) an honest evaluation of a theorem-bearing algebraic reservoir against matched random baselines (§6); (iv) pre-registered predictions for recognized benchmarks (§7).

## 2. The taxonomy

Let a learning problem be a measurement map f from a hidden space X to observations, with residual r = y − ŷ under the current model class. The UOP classification (Sanders–Gish, companion paper "Every Paradox is a Measurement Failure") exhausts the ways resolution can fail:

- **Type I — injectivity failure.** A resolving measurement exists within the current family; ambiguity falls as samples accumulate. *Signature:* improving learning curve. *Route:* buy samples.
- **Type II — missing invariant.** No measurement in the current family separates the states; the obstruction is the feature class, not the sample count. *Signature:* plateaued curve with structured residual (correlation against a candidate library). *Route:* one growth action — adopt the best probe feature — then samples.
- **Type III — admissibility failure.** The domain is malformed: the target carries no information about the input. *Signature:* residual variance indistinguishable from an input-shuffled refit. *Route:* freeze; reallocate the budget. (In an interactive system: refuse or reframe.)
- **Type IV — time-consistency failure.** The map changed during measurement. *Signature:* a model fit on the first half diverges on the second. *Route:* refit on the recent window.

The universality argument is structural, not empirical: I–IV are the four places a measurement chain can break (the map, the family, the domain, the clock), so any residual-driven learner inherits exactly this decomposition. What is empirical — and tested here — is whether the types are *identifiable from residual statistics alone* and whether routing on the inference is worth its cost.

## 3. The decision procedure

Given a channel's purchased stream (u, y), four diagnostics, each cheap:

D-slope = (V_half − V_full)/V_half, the relative residual-variance improvement from half to full data; D-probe = max over a candidate library g of |corr(r, g(u))|; D-info = 1 − V_full / V_shuffled, where V_shuffled refits on permuted inputs; D-drift = e₂/e₁, first-half model error on second half over its own half. The classifier is three thresholded rules applied in order (drift > 2.5 → IV; low info ∧ low probe → III; high probe → II; else I), with all thresholds fixed *a priori* and published in the code. **Re-diagnosis at fit time** is essential and principled: Type-IV gaps are invisible in a pre-switch probe — some of what is missing only becomes measurable after spending on it — so classification uses all residual statistics available when the fit is made.

## 4. The mixed-failure suite and allocators

24 channels, 6 per type (constructions in `verification/gap_router.py`; noise, drift point, and hidden features randomized per channel). Allocators at **matched total budget** (≈6,230 samples): UNIFORM (round-robin, pooled fit, no growth, never stops); **ROUTER** (probe 60 samples/channel, classify, freeze Type III and redistribute their budget, route fits per §2, re-diagnose at fit time); ORACLE (identical machinery, ground-truth types). Test metric: mean squared error against the noiseless target (post-switch regime for Type IV) on held-out inputs.

## 5. Results (P1)

| allocator | mean test MSE | type accuracy | frozen channels |
|---|---|---|---|
| uniform | 0.4049 | — | 0 |
| **Gap Router** | **0.00324** | **24/24** | 5 at probe; 6/6 by fit time |
| oracle | 0.00332 | (given) | 6 |

The router is **125× better than uniform** and statistically indistinguishable from the oracle. Decomposition: freezing Type-III channels alone reallocates 25% of the budget that uniform wastes on noise; Type-II growth removes plateaus that no quantity of Type-I spending could; Type-IV windowing removes the pooled-fit bias that dominates uniform's error on drift channels. Runtime: the full suite plus §6 below reproduces in ≈57 s on commodity CPU, single seeded script.

**Interpretation contract.** The suite is synthetic by design. The demonstrated content is exactly: (i) the four types are identifiable from residual statistics alone (24/24); (ii) routing by inferred type recovers oracle allocation. The suite construction is published precisely so that others can attack the thresholds, the channel families, and the identifiability claim.

## 6. The theorem-bearing reservoir (P2) — an honest split

A reservoir computer whose fixed core is not random but *algebraic*: a 10-node state evolving under two canonical commutative non-associative composition tables (TSML/BHML, companion papers J01/J15) mixed at the parameter α = 1/2 — the unique rational mixing point with an algebraic attractor (H/Br = 1+√3; α-uniqueness over Q proved via Hilbert irreducibility in J01 Theorem F.2) — read out by ridge regression over NG-RC-style features. The **lifted** variant is a 12-unit lens ensemble over the α-family × leak timescales × σ-permutation input shifts (251 features). Baselines: width-matched random echo-state networks, per-task tuned over the same-size hyperparameter grid (3 seeds), and deterministic NG-RC.

| task (NRMSE) | substrate v0 (146) | lifted (251) | ESN (146) | ESN (251) | NG-RC |
|---|---|---|---|---|---|
| NARMA-10 | 0.5615 | 0.5315 | **0.3234 ± .001** | 0.3319 ± .017 | 0.7985 |
| Mackey–Glass +84 | 0.1849 | **0.1277** | 0.2125 ± .004 | 0.2002 ± .006 | 0.6882 |
| Lorenz x→z | 0.0602 | 0.0144 | 0.0043 ± .001 | **0.0020 ± .000** | 0.1368 |

The algebraic core **wins the longest-memory task by 36%** and loses the two shorter-memory tasks; it beats the deterministic NG-RC baseline on all three. The characterization we draw — and report as a finding rather than excuse — is that provable attractor dynamics carry slow temporal structure that random reservoirs do not, while random diversity wins high-precision short-memory regression. Within next-generation reservoir computing, where deterministic feature maps matched to the task are known to beat random reservoirs, *which* algebraic structure matches *which* task class is exactly the open question this split sharpens.

## 7. Pre-registered follow-ups

**P1-real:** on ARC-style task streams, a router with test-time training as the Type-IV route, library growth as Type II, and abstention as Type III will beat uniform test-time-training allocation at matched compute. **P1-LLM:** wrapped around a frozen small open-weights language model on QA with unanswerable items (SQuAD-2-style), Type-III routing will reduce hallucinated answers at fixed coverage versus confidence thresholding. **P2-next:** lifted substrates over F_p extensions (state dimension p+3-indexed) close the short-memory gap or yield an honest negative. All three are stated before any implementation.

## 8. Related work and sources

Verifier-grounded reasoning: AlphaProof (Nature 2025); AlphaGeometry2 (arXiv 2502.03544); DeepSeek-R1 (arXiv 2501.12948). Library growth: DreamCoder (Ellis et al. 2021). Evolutionary search with exact evaluators: AlphaEvolve (DeepMind 2025). Active inference and structure growth: AXIOM (arXiv 2505.24784); Friston's free-energy principle (testable process theories vs principle). Latent-residual world models: I-JEPA/V-JEPA 2 (Meta 2025); DreamerV3 (Nature 2025). Surprise-gated memory: Titans (2025); test-time training on ARC (arXiv 2411.07279); ARC Prize 2024 report (arXiv 2412.04604) and 2025 results. Curiosity and compression progress: Schmidhuber (2010); RND. Reservoir computing and NG-RC: Gauthier et al. (arXiv 2106.07688); echo-state property literature. Recursive tiny models: HRM (arXiv 2506.21734), its independent ablation (ARC Prize blog), TRM (arXiv 2510.04871). Taxonomy source: Sanders–Gish, "Every Paradox is a Measurement Failure: the UOP Algebraic Classifier" (companion, J40), live demo at coherencekeeper.com/paradox.html. Substrate mathematics: companion papers J01, J15, J53 (trinity-infinity-geometry repository).

## 9. Reproducibility

`manuscript/verification/run_all.py` — one command, CPU-only, fully seeded, ≈57 s; emits RESULTS.md and results.json. No dependency beyond numpy. The canonical composition tables ship in the bundle (`ck_tables.py`).
