# Status: closed for now (2026-10-25)

This page covers the binary-magic thread, which ran from 2026-10-20 to 10-25. A claude.ai chat proposed, Claude Code
checked, and the author steered. It was closed on 2026-10-25 by the author's decision, after a review found the
yield per round falling and the questions drifting from the book's purpose. Nothing is deleted. This page says
what stands, at what strength, and what is left.

## What stands
| result | strength | where |
|---|---|---|
| **Graph stars:** critical, genuine n-qubit magic sets with 3n + 1 observables for every odd n. At n = 5 that is 16 observables against 26 published, within the published observable-minimal class | proved; checked by three independent implementations | `magic_sets/THEOREM.md` |
| **16 is the exact minimum** for genuine *context-minimal* 5-qubit magic sets | computer-assisted. The last case rests on one implementation, calibrated against two others on the smaller cases | `magic_sets/LOWER_BOUND.md` |
| No genuine 4-qubit set with at most 6 contexts of 3–5 observables | computer-assisted | `magic_sets/LOWER_BOUND.md` |
| The published sets are not context-minimal: 16 of 18 must hide a smaller clash. In MS5-26, all 3,051 minimal hidden clashes fit on at most 4 qubits | proved from the published tables; exhaustive on MS5-26's printed data | `magic_sets/` |
| **Closed-form determinant of MATLAB's odd magic(n)**, so the squares are never singular, and n^(n−1) divides the determinant (OEIS A160523) | proved; exact to n = 101; probably new | `void_lens/` |
| **Prime-order cyclic-Latin squares are never singular, so all 28,800 pandiagonal 5×5 magic squares are invertible** | proved; exhaustive at p = 5; probably new, pending two unread sources | `void_lens/` |
| The void index: nullity ≥ \|(f_P + f_Q)/2 − 1\|. At order 4 it is exact, and Dudeney's two groups of 8 have index 0 | proved; small; Staab et al.'s Theorems 12–13 are its special cases | `void_lens/`; atlas v6 |
| The fold theorem; degree 3 ⟺ invertible; the 432 affine squares are 9 of Fitting's 11 quadruples; the magic Mermin square is unique | proved or enumerated; probably new, pending Conway–Norton–Ryba | `README.md`, `NOVELTY.md` |
| Pairwise bit-plane balance plus the 10 line sums force Nimm0 and a fold | computer-assisted; probably new | `code_lens/` |
| One kernel ledger across five domains | a synthesis of known theorems, plus measured residue shares at order 5 (71% concentric, 5% eccentric, 25% weighted) | `../kernel_ledger/` |

The author's synthesis essay, *A Ledger of Nothing*, is in `../kernel_ledger/A_LEDGER_OF_NOTHING.md`, with
verification notes. The live claude.ai doc is the master copy.

## Known: cite, don't claim
- Fitting 1931: the binary layers, carries, Nimm0 and the counts.
- Dudeney 1917 and Trigg 1948: singular ⟺ a complement symmetry, at order 4.
- Mattingly 2000 and Staab et al. 2010: the singular direction at every even order.
- Manjunath and Ambikasaran 2022: the doubly-even rank 3.
- Waegell's Star families: degree-2 sets that reduce to the square or the pentagram.
- Levels 0–2 of the kernel ledger: Maxwell–Calladine, Lieb, Edmonds, Chebotarev.

Details are in `NOVELTY.md`.

## Waiting on the author (outward-facing; nothing has been sent)
1. **The note to Trandafir, Lisoněk and Cabello.** The draft is kept privately and was updated 2026-10-24. Before
   sending, the (6, 15) case deserves one more independent implementation.
2. **Optional:** a comment on OEIS A160523. The closed form proves Robert Israel's 2015 observation.
3. **Optional:** `pip install pycryptodome`, so that `void_lens/applications` test A4 runs. It now reports SKIPPED.

## Open, parked (in priority order)
1. A hand proof that no complement symmetry ⟹ invertible at order 4. That covers 224 squares, and the proof has
   to mix bit planes.
2. Read before calling anything else new:
   - Conway, Norton and Ryba 2017;
   - Rosser and Walker 1938–39;
   - Loly, Cameron, Trump and Schindel 2009;
   - Delvaux and Van Barel 2008, where the Fourier certificate is probably a special case.
3. Do graph stars meet the conditions of Aasnæss's shallow-circuit construction (arXiv:2212.09382)?
4. The order-5 residue: predict the weighted quarter from the arithmetic, or leave it.
5. A hand proof that pairwise balance forces Nimm0.
6. Lower bounds beyond n = 5, and for the wider observable-minimal class.

## Dead ends, with evidence
See [`../../GRAVEYARD.md`](../../GRAVEYARD.md). Of the pre-registered real predictions, 44 of 71 held, by the
chat's tally. Broad structural predictions mostly held; narrow numerical thresholds mostly lost.

## Check everything
```
cd towers/binary_magic && python run_all.py               # 39 scripts, about 15 minutes
cd magic_sets && python run_all.py                        # 15 scripts
cd ../../kernel_ledger && python run_all.py               # 8 scripts, about 2 minutes
```
