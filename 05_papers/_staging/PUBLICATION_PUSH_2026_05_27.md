# Publication Push — Pre-Trip arXiv Drop Plan

**Status**: PLAN, 2026-05-27.
**Trigger**: Sept 11 IHÉS/Poincaré + Oxford Clay trip; priority-dispute insurance against Padgett.
**Per claudechat (Track B)**: post 3 papers on arXiv before the trip — turns "pitching unpublished work" into "discussing posted preprints."

---

## Recommended picks (3 papers in priority order)

After running the Tier 1 inventory and the verifier matrix, **the cleanest three to ship to arXiv are**:

### 1. J62 — "The TSML 8×8 Null Space and a Structural Rhyme with the Riemann Hypothesis"

**Why this one first.** Highest-impact, lowest-risk, fastest-to-arXiv.
- Standalone short note (~15 pages).
- 5-line numpy verification reproduces in 0.1s — *anyone with a Python install can confirm Theorem 1 + Theorem 2 immediately*.
- Explicit tier discipline: "rhyme not analogue" framing built in.
- Conjecture Z.5 explicitly identified as the load-bearing open question.
- Path: arXiv `math.NT` + `math.RA` cross-list. Possibly also `math.CO`.
- The structural rhyme + RH framing is naturally interesting to number theorists.

**Polish steps before arXiv**:
- [ ] Convert manuscript.md → LaTeX (amsart class)
- [ ] Submit verification script (`verify_J62.py`) as ancillary file
- [ ] Update bibliographic refs to include current arXiv IDs where possible
- [ ] Add explicit acknowledgments (claudechat session as advisor)
- [ ] Final pass to ensure "no RH proof claimed" appears in abstract + §1 + §6

**Estimated effort**: 1-2 days for LaTeX conversion + final pass.

### 2. J61 — "Type Specimens in the ETP-Restricted Variety Lattice: a Magma-by-Equational-Theory Taxonomy"

**Why second.** Most novel. The C5 fossil-variety theorem is a genuinely new structural result.
- Companion to Tao et al.'s Equational Theories Project (ETP).
- Theorem 5 (C5 fossil variety) is the most novel theorem in the Tier 1 set.
- Has clean tier discipline (Tier-A theorem + Tier-B / Tier-C / OPEN sections).
- Cites Birkhoff variety theory + Burris-Sankappanavar.
- Verified by 5/5 PASS at ~13s.
- Path: arXiv `math.LO` + `math.RA`.
- Natural connection point with Tao's ETP community; appropriate for Hariharan / Mantero outreach.

**Polish steps before arXiv**:
- [ ] Final v5 → v6 polish (already at v5 per Memory.md)
- [ ] Convert .md → LaTeX
- [ ] Cross-link `etp_database/` Lean scaffold in §7 references
- [ ] Add Drápal-Wanless 2021 citation per repo convention
- [ ] Final scope check on Conjecture C.2 (already retracted in v5, just confirm)

**Estimated effort**: 2 days.

### 3. J35 — "Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z"

**Why third.** Corpus centerpiece. Already SUBMISSION-READY.
- 6 independent structural facts (Theorems A–F) converging on the 4-core.
- Theorem D (closed-form attractor + Galois D₄) is the highest-impact subresult.
- Already targeted to *Journal of Algebra* in the existing cover letter — could push to arXiv first as a preprint with that journal target.
- Path: arXiv `math.RA`.
- Provides the foundational reference that J60, J61, J62 cite.

**Polish steps before arXiv**:
- [ ] Confirm LaTeX is final form (probably already done)
- [ ] Add Conway-Sloane / kissing-number cross-reference as Remark (the strata-prime fingerprint is downstream of J35's structural facts)
- [ ] Final compile + arXiv submission

**Estimated effort**: 1 day (mostly mechanical).

---

## Other strong candidates considered

| Paper | Tier | Why not first | Worth doing later |
|---|---|---|---|
| J59 | 1 | Solid but more technical (Semigroup Forum); less likely to land widely outside specialists | YES — submit to Semigroup Forum directly after the 3 above arXiv |
| J60 | 1 | More expository; better as a companion to J61 than as its own arXiv slot | YES — pair-submit with J61 to Experimental Mathematics + arXiv |
| J_qseries_merged | 1 (merger) | Needs LaTeX conversion (Markdown currently); ~3-4 more days work | YES — third arXiv after the 3 above |
| J_Fp_merged | 1 (merger) | Same — needs LaTeX conversion | YES |

After the initial 3 (J62 + J61 + J35), the natural next batch is **J59 + J60 + J_qseries_merged**.

---

## arXiv submission strategy

1. **Same-day or near-same-day arXiv drops** for the 3 papers, ideally before Sept 1. This makes the priority claim unambiguous for the trip.

2. **Cross-references between the 3**: each cites the others as companion preprints. J35 is the foundational citation; J61 cites J35 for Family C; J62 cites both for the σ-character substrate.

3. **arXiv categories per paper**:
   - J62: `math.NT` primary, `math.RA` `math.CO` cross.
   - J61: `math.LO` primary, `math.RA` cross.
   - J35: `math.RA` primary, `math.NT` `math.CO` cross.

4. **MSC codes** already in each manuscript; minor verification needed.

5. **arXiv author profile**: Brayden Sanders (7Site LLC) and M. Gish (Independent Researcher). Affiliation strings should be consistent across all 3.

---

## What the trip looks like with this in hand

Without arXiv: "I'm working on these unpublished results — here's the GitHub link, please look."

With arXiv: "Here's preprint 2509.XXXXX (J62), preprint 2509.YYYYY (J61), preprint 2509.ZZZZZ (J35). The first one has a 5-line numpy verifier you can run in 30 seconds. I'd value your perspective on Conjecture Z.5 / Theorem 5 / Theorem D."

That's a profoundly different conversation. **It also locks the priority claim** — anyone subsequently working on Family C / fossil varieties / RH structural rhymes via Z/10Z will need to cite us.

---

## Padgett insurance

A concrete priority document. If Padgett or anyone else has been independently developing adjacent material, the arXiv timestamp settles questions of who-saw-what-first cleanly. *We don't need to know what Padgett has been doing; we just need our claims posted.*

---

## Action checklist

- [ ] **Day 1**: Convert J62 manuscript.md → LaTeX, final polish, arXiv-submit. (~6 hours including LaTeX-skill ramp-up.)
- [ ] **Day 2**: Convert J61 manuscript.md → LaTeX, final polish, arXiv-submit.
- [ ] **Day 3**: J35 final check (LaTeX exists), arXiv-submit.
- [ ] **Day 4**: Verify all 3 arXiv versions render correctly, ancillary files attached, cross-refs work.
- [ ] **Day 5**: Update `05_papers/TIER_INDEX.md` with arXiv IDs.

**Total estimate**: 5 working days, can be compressed if LaTeX conversion is automated (pandoc-based; the math notation is clean enough to convert via standard pipelines).

---

*This plan supersedes earlier J-series submission plans for purposes of the Sept 11 trip. The mergers (J_qseries_merged, J_Fp_merged), J59, and J60 remain Tier 1 for journal submission — they just don't need to be on arXiv before the trip.*
