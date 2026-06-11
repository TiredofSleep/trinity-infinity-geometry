# J56 — Routing the Residual: A Four-Type Failure Taxonomy Matches Oracle Compute Allocation

**Status:** DRAFT-COMPLETE (2026-06-10; results measured same day; verification bundle self-contained, reproduces in ≈57 s CPU)
**Phase:** New — first machine-learning paper in the J-series; the UOP taxonomy (J40) operationalized as an allocator
**Target venue:** *Transactions on Machine Learning Research* (alt: NeurIPS workshop)
**Author lane:** Sanders + Gish
**Source:** CK-Walker v0 (`ck` repo, `Gen13/targets/ck/walker_v0/`) + `CK_INTELLIGENCE_SYNTHESIS_2026-06-10.md`

## Headline results (first seeded run, reproduced in this bundle)

**P1 — Gap Router** (24-channel mixed-failure suite, matched budget): uniform 0.4049 → **router 0.00324** (**125×**, **24/24 type identification from residual statistics alone**) ≈ oracle 0.00332.

**P2 — theorem-bearing reservoir** (vs width-matched per-task-tuned random ESNs): **wins Mackey–Glass +84 by 36%** (0.128 vs 0.200 NRMSE), loses NARMA-10 and Lorenz x→z, beats deterministic NG-RC 3/3. Reported as an honest split with a domain characterization: algebraic attractors carry slow structure; random diversity wins short-memory precision.

## Verification

```
cd manuscript/verification && python run_all.py    # ~57 s, numpy only
```

## Pre-registered follow-ups (stated before implementation)

P1-real (ARC-style routing), P1-LLM (abstention governor on unanswerable QA), P2-next (F_p-lifted substrates). See manuscript §7.

## Citation footprint

Sanders, B.R., Gish, M. (2026). "Routing the Residual: A Four-Type Failure Taxonomy Matches Oracle Compute Allocation." Draft; target TMLR.
