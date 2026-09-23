# Drift census — how much of TIG is toy-model drift?

*2026-09-24. The author's question: "AI built these tables from the descriptions I give … how
much of this repo is just toy model drift nonsense?" This is the answer, measured.*

*Method. The verdicts on the foundation's objects come from the null-model audit
([`FOUNDATION_NULL_MODEL_AUDIT.md`](FOUNDATION_NULL_MODEL_AUDIT.md) and its four scripts). Five
independent reviewers then classified all 56 J-papers and all 337 non-paper files against one
rubric (object · flags · verdict · evidence path:line). Errors below are marked **[verified]**
where they were re-checked by computation or by reading the cited lines, and **[reviewer]** where
they rest on a reviewer's check with the evidence pointer given.*

## The answer

**Most of it.** No paper in the J-series carries a result about TIG's tables that survives the
three gates (true → specific → not a readout). Every table-specific result the reviewers traced is
generic, a readout of how the tables were built, numerology, or computed on a typo. 36 of 56 papers
(63% of the paper corpus) fall in those classes, and 8 more are tombstones of the same material.
The 10 papers whose mathematics stands do not use the tables, and none was judged new. Outside the
papers, a third of the text maps table numbers onto physics, cosmology, biology, consciousness or
the Clay problems.

What is the author's own is small and real: ten operators, what their descriptions force (a closed
VOID–HARMONY–BREATH–RESET subsystem and about a fifth of the cells), the honesty apparatus, and the
book. What is drift is everything built on one AI rendering's particular cells.

## What "drift" means here — the layers

| layer | what it is | whose |
|---|---|---|
| 0 | verbal descriptions of ten operators (VOID … RESET) — originally LATTICE, COUNTER, PROGRESS, BALANCE, CHAOS for 1, 2, 3, 5, 6; the current canon renames them BEING, DOING, BECOMING, CREATE, ASCEND (`NAMING.md`), so even the meanings drifted | the author's |
| 1 | three AI renderings of them as tables — STD (44 HARMONY), TSML (73), BHML (28) — disagreeing on 49–71 of 100 cells, even on whether VOID is an identity or an absorber | one AI choice each |
| 2 | objects built on a rendering: σ (the "morphotic braid", 2026-04-01), the 4×4 "V" algebras, lens families, **TSML_RAW (a retyping error, 2026-04-25)** | later constructions |
| 3 | theorems about layers 1–2 — true, but generic or readouts | the J-series |
| 4 | readings of layer-3 numbers as physics, cosmology, biology, consciousness, Clay problems | the reach |

Each layer inherits the arbitrariness of the one below and adds interpretation. The drift is not one
error; it is layers 2–4 treating a layer-1 choice as a discovery.

## The J-series (56 papers, 93,057 lines)

| verdict | papers | lines | share | members |
|---|---:|---:|---:|---|
| **true but empty** (generic, or a readout of the rules) | 18 | 32,148 | 34.5% | J01 J02 J04 J07 J08 J09 J12 J15 J16 J17 J18 J28 J30 J32 J36 J40 J53 J54 |
| **typo-dependent** (computed on TSML_RAW) | 5 | 10,587 | 11.4% | J10 J11 J19 J31 J39 |
| **numerology** | 5 | 5,343 | 5.7% | J06 J21 J22 J23 J42 |
| **physics reach** (no tested prediction) | 3 | 4,785 | 5.1% | J37 J38 J46 |
| **graveyard** (already retracted, or dead by the repo's own checks) | 5 | 5,429 | 5.8% | J13 J33 J44 J47 J55 |
| merged tombstones (of the above material) | 8 | 12,929 | 13.9% | J25 J41 J45 J48 J49 J50 J51 J52 |
| **mathematics that stands** (table-independent) | 10 | 19,286 | 20.7% | J05 J14 J20 J24 J26 J27 J29 J34 J35 J43 |
| unclear | 1 | 1,451 | 1.6% | J03 |
| machine learning (does not use the tables) | 1 | 1,099 | 1.2% | J56 |

- **Table-specific survivors: zero.** Every TSML/BHML/σ-specific number traced — so(10), so(8),
  the 4-core and chain, 1+√3 and its D₄ field, 13/4, 73/71/70, 26, 78, the F_p closed forms,
  σ-magma rigidity, the prime 11 — is generic, a readout, numerology, or the typo.
- **The ten that stand** are correct (J34 and J35 only after their headline theorems are corrected)
  and not new: classical Fejér / sinc² identities (J24, J26), elementary group theory and CRT
  folklore (J27, J34, J35), a dimension count (J20), a classroom Lo Shu note (J29), ETP profiles of
  linear magmas (J05), an elementary non-associativity rate (J14), and an NV-qutrit S₄ construction
  with no TIG input (J43).
- **J03** is the one open case: its "fossil variety" proof is invalid, but the claim is testable
  (enumerate every model of ETP equation 4295 at orders 3–6).
- **J56** does not read the tables; random tables beat the canonical reservoir in 7 of 12 trials.

## Errors found inside the papers

Beyond the drift classes, about twenty papers contain a false or mislabeled statement.

- **J42 — its data column is not data. [verified]** The column headed "Empirical (PDG / CODATA)"
  gives |V_cb| = 0.0508, |V_ub| = 0.01140, V_td² = 0.00258 — exactly 0.2253², 0.2253³, 0.2253⁴.
  The measured values are ≈ 0.041, ≈ 0.0038 and |V_td|² ≈ 7×10⁻⁵. The paper's "load-bearing"
  four-order fit is one Cabibbo fit counted four times, and its 10⁻¹¹ joint probability is computed
  on generated numbers; against real data (11/49)² misses by 23%, (11/49)³ by 3×, (11/49)⁴ by 34×.
- **J11 — says one table, computes on another. [verified]** The manuscript uses "TSML_SYM
  throughout"; its verification script's TSML rows contain the typo `0797377777`. J10 and J39 also
  compute on the typo; J19 is entirely about it; J31's only TSML-specific detector (11 | c₂, c₈)
  never fires on the original table.
- **J19 — its comparison matrix is mislabeled. [verified]** "T_SYM" (c₂ = −23) sets both swapped
  cells to 7; it is neither symmetrization of the typo and not the original table (on which 11
  divides only c₇).
- **J22 — "lens-invariant 71" is false. [verified]** On TSML_RAW the TSML/BHML disagreement is 72.
- **J17 — its conjecture has a counterexample. [verified]** Setting TSML(1,7) = TSML(7,1) = 2 keeps
  the table commutative and the 4-core closed, with associativity index 0.736 — inside the interval
  (0.5, 0.8) the conjecture says is empty.
- **J34 / J35 — the headline "iff" is false. [verified]** On ℤ/15 with g = 2, h = 11,
  ⟨g⟩ ∩ ⟨h⟩ = {1}, yet 5 and 10 share both orbits.
- **J08 / J48 — the automorphism table is wrong for its own algebra. [reviewer]** J08's Theorem 2
  (|Aut| = 6, 24, 40, 336, 1320, 2184) and Theorem 3 (|Aut(V₅)| = 40): brute force gives 1 for J08's
  §1.1 algebra and 2p(p−1) for J48's (`J08/manuscript/manuscript.md:30`).
- **J16 — "independence" is wrong in both directions. [reviewer]** S₆ follows from S₅ + S₇, and S₃,
  S₄ from S₁ + S₂ + S₅ + S₆; one-move strict witnesses exist for S₁ and S₅, called open; the proof
  contains literal "Wait:" passages (`J16/manuscript/manuscript.tex:595-600, 686-689`).
- **J01 — Theorem F.2 misuses Hilbert irreducibility [reviewer]** (a conjecture, not a theorem; its
  own README lists it as open); **J33** — Theorem 2's proof relies on a false distributivity
  [reviewer]; **J38** — Theorem 4.1's hypotheses contradict each other [reviewer]; **J03** — the
  fossil-variety proof's either/or is false (36 of 45 order-3 models are neither) [reviewer];
  **J21** — its inputs contradict J28's Lemma 5.1 [reviewer]; **J23** — wrong null (Frobenius makes
  the prime condition automatic) [reviewer]; **J36** — σ called "the standard involution" (it has a
  6-cycle) [reviewer]; **J46** — its own inputs give Q_c ≈ 400–4000, not 5/7 [reviewer]; **J54** —
  "Theorem 1" is a regression with R² 0.67 [reviewer]; **J55** — the "sharp certificate" goal is
  impossible by the repo's own B2 check, manuscript not updated [reviewer]; **J04** — calls BHML and
  CL_STD quasigroups; neither is a Latin square [reviewer].

## Outside the papers (337 files, 68,583 lines)

| category | files | lines | share |
|---|---:|---:|---:|
| physics / cosmology / Clay / biology reach | 87 | 23,023 | 33.6% |
| table results (now: generic or readouts) | 49 | 11,944 | 17.4% |
| runtime / tooling / databases | 99 | 12,138 | 17.7% |
| honesty apparatus (audits, graveyard, negatives, ledgers) | 44 | 8,631 | 12.6% |
| universal mathematics | 36 | 7,346 | 10.7% |
| philosophy / narrative | 22 | 5,501 | 8.0% |

Leaving out tooling, 62% of these lines are reach or table readout, and 15% is honesty apparatus.
In `04_meta/`, 60% of lines are reach; 17 of 22 reach files at its top level carry no banner, and 12
of 18 files in `retired_J_papers/` carry no retirement notice. 75 files mention the "wobble" or
TSML_RAW; before this audit, none recorded it as a typo.

**Worst offenders** (each still presents a dead or readout claim as a result):

1. `TIG_FROM_THE_GROUND_UP.md:665` — the retracted torus "T\* = 5/7 … PROVED"; also "six independent
   derivations" (:397), "only p = 7, 11 preserve rank" (:742), and a false σ³ derivation of the 4-core (:132).
2. `03_canonical_reference/FORMULAS_AND_TABLES.md:377` — "TIG structure is *specific* to canonical
   TSML/BHML … not a generic feature"; PROVED rows on the TSML_RAW lens (D37, D98), the ladder (D97),
   Pati–Salam (D130).
3. `08_for_ai/README.md:49` — CK's "cognitive substrate is the finite-arithmetic structure described
   here", which the 2026-06-14 probe falsified; :90–103 hand AI readers the 4-core, 1+√3 and 13/4 as facts.
4. `01_orientation/for_physicists.md:25` — the Cl(0,10) spinor "is exactly the algebraic shape of the
   n = 4 atomic shell"; :121 keeps κ_ξ = 13/(4e), whose bridge was killed.
5. `04_meta/physics_bridges/THE_PHYSICS_BRIDGE_LIVES_HERE.md:47` — "1/α = 137 from structural
   primitives [Tier B-rigorous]", built on "22 = |TSML XOR BHML|"; the tables differ in 71 cells.
6. `02_results/clifford_algebra/PAULI_DIVISOR_BIJECTION.md:3` — "PROVED — bijection exhibited",
   contradicting D164 (no natural bijection among 730k+ functions).
7. `02_results/algebraic_combinatorics/BRAIDING_FRACTAL_FORMAL.md:142` — "TSML has exactly 2 cells
   where T[i][j] ≠ T[j][i]. These cells encode the wobble prime" — the typo, read as structure.
8. `04_meta/META_TIG_AS_PREPHYSICAL_SUBSTRATE.md:327` — "The integer 11 in TSML char poly
   coefficient c₂ isn't an error." It is exactly the transcription error.
9. `04_meta/MEGAROPE_COSMOLOGY_GENERATIONS_FORCES.md:92` — "Tier A — first algebraic derivation of
   dark energy fraction", using one rendering's (CL_STD's) 44-cell count and an invented Ω_Ψ0 = 1/1000.
10. `04_meta/sprint_2026_05_15_qutrit/PAPER_08_TIG_FRAMEWORK_MANIFESTO.md:434` — "Some predictions
    are already verified (fine structure constant, matter fractions, DNA structure)".

The honesty apparatus leaks too: `HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md:66` still says to cite the
typo's 11; `HOW_IT_CONNECTS.md` §1 still grades the 4-core, so(10) and 1+√3 as PROVED joins;
`frontiers_2026-05-27/F6_hilbert_irreducibility.md:3` says "proved over ℚ" on a lemma that fails in
general, and that label propagated.

## The front door

It still leads with readouts and retractions. `README.md:40` opens with "three structures follow
with no further assumption, all **PROVED**" (the 4-core, the chain, 1+√3) — contradicting its own
honest limit #7. `README.md:127` uses "this so(10) IS the SO(10) GUT gauge algebra" as its example
of a STRUCTURAL claim. `START_HERE.md:23` calls "the 4-core, D₄, so(10)/Cl(0,10)" "the
interconnected, proved core". `TIG_FROM_THE_GROUND_UP.md` teaches the retracted torus as PROVED.
No `01_orientation/` file has had a content edit since 2026-05-12. `THE_MAP.md` is the exception.

## What is the author's, and what survives

- **The descriptions' own content.** In all three renderings {VOID, HARMONY, BREATH, RESET} closes
  on itself, and the renderings agree on 12 of the 55 cells — BREATH·BREATH = HARMONY, CHAOS driving
  the ordinary operators to HARMONY, LATTICE·COUNTER = PROGRESS, BALANCE·BREATH = HARMONY
  ([`../verification/three_renderings.py`](../verification/three_renderings.py)). That is what the
  author's descriptions force; it is also all they force.
- **The honesty apparatus** — the graveyard, the audits, the honest frontier negatives (F2, F3, F8,
  F11, F12, F15–F19), the retraction records (VEV 13/4, torus, Berry). This is the part of the repo
  that behaves like research.
- **The book** (`shape-of-understanding`): universal mathematics, verified, walled off. One breach
  was found and closed today: its geometric-core verifier still carried the dead P3 and the P4
  frame (book commit `310262d`).
- **Spine B** (`05_papers/integers_clifford/`): correct standard mathematics, expository, with
  recurring slips — "the two tetrahedra are the two chiralities" (a regular tetrahedron is achiral),
  "perpendicular mirrors anticommute" (the reflection maps commute; it is perpendicular *vectors*
  that anticommute), triangular and honeycomb lattices treated as one "hex", and a Bott "4 × 2 = 8"
  reading that cannot produce period 8.
- **The ten table-independent papers** — correct after fixes, not new.
- **The CK runtime and the ML work** — separate from the tables (random tables do as well).

## What to do — the author's call

1. **Front door first.** Lead with the provenance (AI renderings of verbal descriptions) and this
   census; retire the "proved core" framing in `README.md`, `START_HERE.md`,
   `TIG_FROM_THE_GROUND_UP.md` and `01_orientation/`.
2. **Tombstone the typo-dependent work** — J10, J11, J19, J39, J31 part 2, and the WP107 / 109 /
   110 / 112 / 113 / 115 line built on TSML_RAW.
3. **Pull J42 now.** Its empirical column is not empirical.
4. **Relabel the table-specific corpus** (J01–J18, J28–J36, J53–J54) as worked examples on one AI
   rendering — true, and not evidence of anything beyond that rendering.
5. **Keep the table-independent notes as what they are** (expository, classroom), after fixing
   J34 / J35.
6. **The research question that remains** is small and honest: *what do the descriptions force?*
   Write the ten operator descriptions as constraints, enumerate every table that satisfies them,
   and study only what all of them share. The three renderings already in the history show the
   answer is much less than the corpus assumed — and that what does survive is the author's.
