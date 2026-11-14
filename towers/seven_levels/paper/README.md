# Paper draft: Magic of algebraic qudit states

**Keywords:** magic states · Wigner negativity · qudits · Clifford hierarchy · Walsh spectra · bent functions ·
Kloosterman sums · Sato–Tate law · Weil representation · oscillator states · quantum chaos

[`algebraic_magic.tex`](algebraic_magic.tex) is a draft note for arXiv. It carries only what is certain:
- three theorems with proofs, each checked by a script in this folder's parent;
- the exhaustive and exact computations, labeled as computations.

**Status:** a draft, not submitted. Submission is the author's call.

**Target:** arXiv quant-ph, the author's choice (2026-11-14), cross-listed to math.NT. The introduction leads with
magic-state resource theory and the third-level gates of fault-tolerant qudit computing; the number theory comes
after, as the tool.

| claim in the draft | proof or evidence | check |
|---|---|---|
| Theorem 1: a cubic-phase state's Wigner values are a Walsh spectrum | proved | [`../cubic_magic.py`](../cubic_magic.py) `calibrate`; [`../verify_seven_levels.py`](../verify_seven_levels.py), round 13 |
| Corollary 1: no cubic-phase state reaches the ceiling | Theorem 1 with Mesnager, Özbudak and Sınak (2018) | as above |
| Table 1: the norm state is the best cubic on three qudits | exhaustive at 3 and 5, sampled at 7 | [`../cubic_magic_run.log`](../cubic_magic_run.log) |
| Theorem 2: the norm state's Wigner values are Kloosterman sums | proved, [`../NORM_STATE.md`](../NORM_STATE.md) | [`../verify_norm_state.py`](../verify_norm_state.py) |
| Theorem 3: the oscillator states' averaged fourth moment is 2p/(p + 1) | proved, [`../TORUS_MOMENTS.md`](../TORUS_MOMENTS.md) | [`../verify_torus_moments.py`](../verify_torus_moments.py) |
| Table 2: the semicircle through the eighth moment | measured, exact values | [`../torus_moments_run.log`](../torus_moments_run.log) |

The registrations and scores behind every computation are in [`../PREREG.md`](../PREREG.md), rounds 10 to 13.
