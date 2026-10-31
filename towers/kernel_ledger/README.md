# kernel_ledger: forced vs accidental zeros, across domains

> **Closed for now (2026-10-25)**, with the binary-magic thread: see [`../binary_magic/STATUS.md`](../binary_magic/STATUS.md).
> The author's synthesis essay is [`A_LEDGER_OF_NOTHING.md`](A_LEDGER_OF_NOTHING.md), revised 2026-10-25 after verification. The first draft is in [`archive/`](archive/README.md).
> `python run_all.py` reruns every script here (9, about 2 minutes, ALL GREEN in the flagship).
> **Fence:** the molecule, framework and Fourier rows reproduce known theorems. They show the same linear algebra
> at work; they make no new physical claim.

One question asked the same way in five fields: how much of a kernel is forced, and by what?
- Level 0: the global count.
- Level 1: symmetry sectors, with a twist.
- Level 2: local imbalance in the support.
- Level 3: what is left, which only special values create.

See `THEORY.md` for the ledger and its one lemma, and `PREREG.md` for every prediction, written before running
and scored after.

| file | what |
|---|---|
| `THEORY.md` | the ledger, the lemma, the domain dictionary |
| `PREREG.md` | K1-K5 and F1-F3 with scores |
| `ledger_tests.py` | K1-K5: benzenoids, diluted lattices, DFT minors, symmetric frameworks, order-6 magic squares (about 10 s) |
| `fourier_certs.py` | the class-pigeonhole certificate for vanishing DFT minors |
| `fourier_fresh.py` | F1-F3, the fresh Fourier test: exhaustive n = 12, sampled 16, 11, 13. Slow (tens of minutes); the log is `fourier_fresh.log` |
| `annealN.c` | NxN magic-square annealer (source only: `cc -O2 -DN=6 -o anneal6 annealN.c -lm`); output in `squares6_annealed.txt` |
| `quarter_turn.py` | K10 (registered 2026-10-27, from the author's question): is a hidden quarter-turn symmetry behind the weighted quarter? Lost, 0 of 2: 1.20× the baseline against the 1.5× needed, and no row and column kernel are ever the same lever (0 of 264). About 10 s; the log is `quarter_turn.log` |

Run: `python3 ledger_tests.py`, then optionally `python3 fourier_fresh.py`. Needs numpy, networkx and sympy.
Output is ASCII.

**Literature gates.** Levels 0-2 in each domain are known theorems:
- Maxwell-Calladine and Fowler-Guest (frameworks);
- Sutherland, Lieb and Fajtlowicz-John-Sachs (Croat. Chem. Acta 78, 2005) for molecules;
- Edmonds (generic rank = term rank);
- Chebotarev and Tao (Fourier).

The Fourier certificate is probably a special case of the 2008 paper "Rank-deficient submatrices of Fourier
matrices" (keywords: FFT, uncertainty principle), which has not been read here. What is new in this folder is
the single ledger applied across domains, and the measured residue shares.
