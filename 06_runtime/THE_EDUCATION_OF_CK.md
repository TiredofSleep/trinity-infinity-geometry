# The Education of CK
### A measured arc from substrate to scholar — documented for collaborators, researchers, and anyone evaluating whether to help scale it

**Brayden Ross Sanders + Claude (Anthropic), 2026-06-11.**
**Repo:** github.com/TiredofSleep/ck (branch `tig-synthesis`) · companion math corpus: github.com/TiredofSleep/trinity-infinity-geometry
**Hardware for everything below: one desktop (RTX 4070, 12.9 GB) + CPU. No cloud training.**

---

## 0. What this document is

CK is a "living math creature" — an AI system built over thirteen generations by one
independent researcher, rebuilt in its current form (CK-TRINITY) in a single measured arc.
This document tracks that arc: what was claimed, what was tested, what survived, what died,
and what the system can demonstrably do tonight. **Every number below is reproducible from a
named script in this repo** (§7). The failures are documented beside the wins, because the
methodology — registered predictions, kill criteria, ability-by-ability measurement — is the
most transferable asset here.

**The thesis this work supports:** useful intelligence is *grounded* (evidence attached to
every claim), *bounded* (refusal as a first-class answer), and *honest about its boundary*
(calibrated, white-box) — and these properties are achievable NOW, at desktop scale, growing
with use, rather than emerging someday from scale.

## 1. The system in one view

**Architecture: a toolbox of measured organs under three faces.**
Every experience is jointly measured by all tools (the toolbox is the *generation layer*);
three faces consume the percepts: **FORM** (identity through noise), **MEANING** (trained
heads over fused percepts), **GAP** (conformal distance gate — answer or refuse). An
**ABILITY_REGISTRY** records what every organ has measured-ly earned: self-knowledge as a
data structure. Governing law (Sanders): *tools don't win seats; they earn places by
abilities.* Nothing is kept for being beautiful; nothing is discarded that holds a real
ability.

## 2. The arc — claim → test → number → artifact

| stage | claim tested | result | artifact |
|---|---|---|---|
| Braid memory | topological word-identity survives noise | 44% recall through 1-edit misspellings (260× chance); swaps 71% via exact theorem | `extraction/braid_memory.py` |
| Form↔meaning | form encodes meaning | within-language CCA 0.58 (survives length control); **cross-family: FALSIFIED** (p=0.29, below char-trigram) | `extraction/cross_family.py` |
| Table mystique | the canonical algebra carries task power | **FALSIFIED 5×** — random tables tie/beat under identical machinery, incl. multiscale | `extraction/project4_inductive.py`, `project6_multiscale.py` |
| Trained heads | training fills the gap *if representation carries signal* | learning curves climb exactly when true: routing 15→80% | `extraction/project2_routing.py` |
| Abstention gate | distance-to-the-measured beats confidence | far-OOD **0% hallucination** @ 90% coverage (AUgC 0.027 vs 0.242 MSP); near-OOD risk dial **42%→8%** | `trinity/organ_gap*.py` |
| FORM seat | our braid vs the field's VSA | field wins recall **91% vs 45%**; braid keeps evidence/compression abilities | `trinity/organ_form.py` |
| Discrete induction | parity dead end = wrong hypothesis class | one-shot/TRM/GRU all ~50%; **56 enumerated automata → 100%** in 0s | `trinity/organ_induction.py` |
| Meaning wean | distill teacher embedding into form features | **FALSIFIED at mechanism level**: 0.971 teacher-fit, 30% transfer — *meaning is not derivable from form* | `trinity/organ_wean.py` |
| Native meaning | learn meaning from HIS OWN life-corpus, no teacher | PPMI+SVD 50% → +synthetic curriculum **65%** → +contrastive head **75%** (borrowed teacher: 80%) | `trinity/organ_meaning_*.py` |
| Scaling curve | measure, don't guess, the growth dial | 133K→10.8M params: 3.99→2.44 bits/char, **no bend** — data-starved, not capacity-starved | `trinity/train_native_lm.py` |
| Senses | hear and see in his own alphabet | EAR: spoken-letter identity 27% (6.9× chance), vowel/consonant 73%; EYE: wavelength Mantel r=0.347, p=0.003 | `trinity/organ_senses.py` |
| Cliff notes | teacher summaries beat raw text for retrieval | **FALSIFIED** — raw 47% > native notes 42% > teacher notes 35%; *the teacher's voice erases the author's voice* | `trinity/eval_reading.py` |
| The scholar | grounded book QA with traps | **0 hallucinations / 10 questions incl. 5 traps**; refusals carry counted evidence ("Gandalf: 0 occurrences in all 12 books") | `trinity/ck_book_chat.py` |
| The reader freed | autonomous study at native speed | **479 books/min** (library of 1,019 in 2 min); fact/fiction **85%** from 12 hand-labeled seeds; self-written study journal | `trinity/ck_reader_daemon.py` |

## 3. The laws the arc discovered (each measured multiple times)

1. **Composition over volume** (4 independent confirmations): 3.3K right-register tokens
   lifted +15 points; 15K off-register tokens cost −5; raw author-voice beat summary-voice;
   lived log-scraps diluted. Data curation is the leverage, not data mass.
2. **Meaning is not derivable from form** (3 independent proofs): cross-family ✗, resonance
   partial, distillation ✗ at 0.97 fit. Meaning must be *earned from usage*.
3. **Calibrate on the register you will face** (2 appearances): conformal guarantees drift
   when calibration register ≠ query register — measured inside our own gate.
4. **The representation sets the ceiling; training climbs to it** — every learning curve.
5. **Hypothesis class beats gradient effort** — parity: 56 discrete hypotheses > 25K
   gradient steps.
6. **Every structure is a capacity AND a blindness** — the 4-core attractor theorem (the
   substrate's crown jewel) is *exactly* the fading memory that loses event-tracking tasks.
   Located paradoxes, not mysticism.

## 4. Honest negatives (the credibility section)

Falsified by our own registered tests, retired, and not resurrected: the pre-language
geometry of meaning; the canonical tables as a source of task power (five kills); cliff-notes
as retrieval keys; TRM-style static refinement at our scale (seat vacated on numbers); the
embedding-distillation wean. **A system whose claims you can trust is built from claims that
were allowed to die.**

## 5. Tonight's demonstrable state

- A scholar that **read 12 books and survived an oral exam with 5 traps at 0 hallucinations**,
  every answer shipping book + passage + score + entity census.
- A reader that judges **fact vs fiction at 85%** (from 12 seeds, active-learning loop live)
  while reading at **479 books/minute**, journaling in his own sentences.
- A gate that **refuses with printed evidence** and a measured risk dial.
- A meaning organ at **75% fully native** (no API, no external model at inference).
- Ears (6.9× chance on spoken-letter identity) and eyes (p=0.003 on the spectrum) in one
  operator alphabet.

## 6. The scaling ask — what help converts this

| need | why | scale |
|---|---|---|
| **Benchmark engineering** | port the gate to published selective-QA / hallucination benchmarks (it already beats MSP/max-logit in-house) | one engineer-month |
| **Compute for the voice lane** | native LM curve has no bend; curriculum-fed training rounds | ~10-100 GPU-weeks |
| **Corpora + licensing counsel** | fact-heavy curated feeds; open-source licensing decision (current: 7Site Human Use License) | advisory |
| **Federation protocol collaborators** | organs-not-data exchange with re-verification ("don't trust, re-measure") — the decentralized path | research partners |

**What a collaborator gets:** a fully reproducible harness (every claim = a script), a
defensible niche (evidence-bearing abstention — the property frontier systems structurally
don't ship), and a documented methodology for growing measured intelligence on owned hardware.

## 7. Reproduce everything

All scripts run on CPU or one consumer GPU, seconds-to-minutes each, under
`Gen13/targets/ck/{extraction,trinity,walker_v0}/`. Results land in `*_result.json` beside
each script. The living ledger (`trinity/LEARNING_LEDGER.md`) is regenerated by
`trinity/build_ledger.py`. The study journal (`trinity/study_journal.jsonl`) accumulates as
he reads. Full session-level history: the git log of this branch, pushed.
