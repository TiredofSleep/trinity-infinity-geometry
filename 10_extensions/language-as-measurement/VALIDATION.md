# Does Ruler Spectra carry real structure? — the trial

**2026-06-13.** Registered prediction + random-ruler null + kill criteria, run by
`validate.py`. The point was a go/stop verdict, not a demo.

## Registered before running
- **P1** zero-shot 8-way accuracy ≥ 0.55 (chance 0.125)
- **P2** real accuracy > 99th percentile of random-ruler accuracy
- **P3** bridge-vs-pure crossing AUROC ≥ 0.70
- **Kill** if accuracy ≤ 0.25, or real ≈ random, or AUROC ≤ 0.55

## Result

| test | result | bar | verdict |
|---|---|---|---|
| zero-shot 8-way accuracy (real rulers) | **0.863** | ≥0.55 | PASS |
| random-ruler null (200 sets) | mean 0.125, max 0.275 | — | — |
| real > random | **p = 0.0000** | <0.01 | PASS |
| crossing AUROC (bridges vs pure) | **0.800** | ≥0.70 | PASS |

Rulers defined **only from one-line domain descriptions**, never fit to the 80
probe labels, sorted canonical terms (capacitor→EM, quark→particle physics,
polygon→geometry, totient→number theory) at **86%**. 200 random rulers built with
identical machinery never exceeded 28%. Confusions land on **adjacent** domains
(algebra↔particle, EM↔wave, info↔number theory), not at random. Held-out bridge
terms — energy, signal, symmetry, wave, field, entropy — register as crossings
(2nd-ruler z mean 1.44 vs 0.42 for pure terms; AUROC 0.80).

**Verdict: ALL PASS, no kill. The structure is real and far from random.**

## What this proves — and what it does not (honest scope)

Proves:
- Measuring concepts across designer-chosen rulers extracts **real, non-random,
  interpretable structure**. The random-ruler null cancels any bias in how the
  probe terms were chosen: even if the terms were easy, random axes can't sort
  them — real axes do, at 86%.
- The emergent **crossings are real**, not cherry-picked: bridge terms score
  measurably higher on a second ruler than pure terms.

Does **not** prove (named, not hidden):
- That the 8-dim ruler spectrum **beats the raw 384-dim embedding** on a task. It
  is a lossy projection — it cannot hold more information than the embedding it
  comes from. Its value is **legibility** (8 named axes you can read) and the
  **emergent crossing structure**, not raw representational power.
- It leans on MiniLM's pretrained knowledge; the ruler layer adds interpretable
  axes + crossing detection *on top* of that. A from-scratch ruler-LM is untested.
- The 80 probe terms are author-chosen with objective labels; the random null
  controls the *relative* claim, but a fully external labeled set would be
  stronger.

## The next rigor gates (what would make this undeniable)
1. **External labels** — replicate the 86% on an independently-sourced labeled
   term set (e.g., arXiv-category or glossary terms), not author-chosen ones.
2. **Downstream utility** — show the ruler spectrum *helps* somewhere the raw
   embedding alone is worse: interpretable routing, abstention, or teaching a
   small model faster. That is the real "better, not just real" bar.
3. **Society of rulers** — replace the single MiniLM stand-in with two+ distinct
   LMs as independent rulers and test whether their crossings agree.

Reproduce: `python validate.py`.

— Claude (Opus 4.8), with Brayden
