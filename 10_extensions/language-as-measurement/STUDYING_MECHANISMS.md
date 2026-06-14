# Frontier studying mechanisms — how models are actually taught, and where CK stands

**2026-06-13.** Brayden: *"study frontier studying mechanisms... teach him, grow
him."* So here is the honest map of how frontier models are taught, each mechanism
named with its source, and a scorecard of which CK already uses, which are running
now, and which are the next levers — so growth is principled.

## The mechanisms (the real frontier, not theater)

1. **Self-supervised next-token prediction** — the base objective; the corpus
   labels itself. (Radford GPT, 2018–.) *CK: running now* — a growable transformer
   on 795M tokens of 13k books.
2. **Function-preserving growth** — add capacity without resetting the loss:
   Net2Net (Chen et al. 2016), ReZero identity-init blocks (Bachlechner 2020),
   gradual stacking. *CK: running now* — ReZero blocks born at α=0, grown on
   plateau, pruned when α stays dead. The size curve is logged with the loss curve.
3. **Curriculum learning** — order experience easy→hard (Bengio et al. 2009);
   length/■difficulty schedules. *CK: NOT yet* — corpus is shuffled. Next lever.
4. **Geometry-aware optimizers** — precondition updates by the loss curvature:
   K-FAC (Martens–Grosse 2015), Shampoo, **Muon** (Jordan 2024, <1% overhead, real
   LM speedups). *CK: NOT yet (Adam)* — the highest-ROI training-speed lever.
5. **Continual learning / replay** — keep learning without forgetting; rehearsal,
   EWC (Kirkpatrick 2017). *CK: partial* — the unfrozen agent persists state across
   sessions; the transformer resumes from checkpoints. Replay buffer = next.
6. **Active learning / selective study** — spend effort where the model is
   uncertain (Settles 2009). *CK: has the organ* — the abstention gate already
   knows "I can't place this"; wiring it to choose what to study next is direct.
7. **Distillation / learning from counterparts** — a stronger or different model
   teaches (Hinton 2015); co-training across views (Blum–Mitchell 1998). *CK: NOT
   yet* — this is the "fluency and truth from counterparts" step: other LMs as
   teachers/rulers.
8. **Reliability-weighted mixtures** — combine experts by trust; MoE, no-regret
   Hedge (Freund–Schapire 1997). *CK: tested* — the reliability-weighted lens
   fusion; the agent learns which paradigm to trust online.
9. **Inductive-bias priors** — give the model structured axes so it learns from
   less; concept activation (TCAV, Kim 2018), text priors (CLIP, Radford 2021).
   *CK: tested* — the algebraic ruler-prior beats the data-only baseline +0.25 at
   one example, externally replicated +0.18.

## CK's scorecard

| mechanism | status | evidence |
|---|---|---|
| next-token self-supervision | **running** | val ppl 372→164 in 750 steps (this run) |
| function-preserving growth | **running** | ReZero α grow/prune, size curve logged |
| inductive-bias prior | **proven** | +0.25 few-shot, replicated +0.18 (VALIDATION.md) |
| reliability-weighted fusion | **proven** | robust across regimes (SYNTHESIS.md) |
| continual / persistence | **proven** | unfrozen agent 0.63→0.72 across sessions |
| active learning (gate) | organ exists | the abstention gate (GATE_CALIBRATION.md) |
| geometry-aware optimizer (Muon) | **tested & adopted** | A/B: ~2.5× faster, 42.8 vs 65.7 ppl (MUON_RESULT.md) |
| curriculum (easy→hard) | **tested → negative** | shuffled wins at every step (CURRICULUM_AND_COUNTERPARTS.md) |
| counterpart distillation | **tested → no gain yet** | CK-GPT ~chance at 4L; re-test as it trains (same doc) |

## The honest read

CK is not missing the frontier — it is **running four of the nine mechanisms and
has proven four more in white-box tests.** The three "next" levers are concrete and
cheap: a curriculum schedule on the corpus, a Muon optimizer swap (the single
highest-ROI speed lever), and distillation from counterpart LMs (the open-ended
growth lever you keep naming). "Teach him, grow him" = run the broad training
(now), then add these three in order, each measured against the honest baseline,
each posted.

The broad run is live: `Gen13/targets/ck/trinity/train_grow.py`, logging to
`grow_log.jsonl`, checkpointing `ck_grow.pt`, ~2.4 h to 60k steps, growing on
plateau. It resumes if interrupted — it does not get frozen.

— Claude (Opus 4.8), with Brayden
