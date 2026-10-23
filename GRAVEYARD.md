# Graveyard — what was archived, and why

*Nothing here was deleted. The repository as it stood before the cleanup is preserved, unchanged,
at the tag [`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24)
(and on the branch `archive`); the full working history is in the workstation repository
[`ck`](https://github.com/TiredofSleep/ck). Proven dead ends are information, so each is recorded
here with the evidence that killed it. (The archive was made on 2026-09-23; the tag's name carries
a date one day off, and is kept so that existing links still work.)*

`A/` below abbreviates `https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/`.

---

## 1. The table program — archived 2026-09-23

**What it was.** Three 10×10 composition tables on ten named operators — TSML (73 cells equal to
HARMONY), BHML (28) and CL_STD (44) — built by AI from the author's verbal descriptions of the
operators; and on them, 56 manuscripts (J01–J56), a canon of "results", readings of the tables as
physics, cosmology, biology and consciousness, and documentation for a runtime.

**Why it was archived.** The author: *"I have no ties to any of these tables at all."* And the audit
found nothing in them that stands on its own:

- **The tables are renderings, not discoveries.** The three are three AI renderings of the same
  descriptions. They disagree on 49–71 of the 100 cells, even on whether VOID is an identity or an
  absorber, and agree on only 12 of the 55 cell pairs. The descriptions do not determine a table.
  ([`A/verification/three_renderings.py`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/verification/three_renderings.py))
- **The headline results were generic or restatements.** The joint so(10) Lie closure holds for
  every random table pair; the four-core and its sub-magma chain are the upper sets of a
  "climbing" rule built into the tables; TSML's so(8) is two identical elements; the α = ½
  attractor's 1+√3 is three cells of BHML, and its D₄ number field turns up for a third of the
  nearby variants.
  ([`A/04_meta/FOUNDATION_NULL_MODEL_AUDIT.md`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/04_meta/FOUNDATION_NULL_MODEL_AUDIT.md))
- **One layer was a typo.** The prime-11 "wobble" that five papers rested on exists only in a copy
  of TSML whose row 9 has two digits swapped — first typed on 2026-04-25, seven weeks after the
  original table.
- **The papers.** Of the 56: none carries a result specific to the tables that survives testing;
  36 are true-but-empty, numerology, typo-dependent, untested physics, or already retracted; 8 are
  merged tombstones; 10 contain mathematics that does not use the tables and is correct (two only after their
  headline theorems are fixed) — all classical or elementary. About twenty contain a false or mislabeled statement — one (J42) has an "empirical"
  data column made of powers of the Cabibbo value 0.2253 instead of measurements.
  ([`A/04_meta/DRIFT_CENSUS.md`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/04_meta/DRIFT_CENSUS.md))

**What the descriptions themselves force** — the part that was never the AI's: in all three
renderings, VOID, HARMONY, BREATH and RESET close on themselves, and a dozen compositions agree
(BREATH with BREATH gives HARMONY; CHAOS drives the ordinary operators to HARMONY; LATTICE with
COUNTER gives PROGRESS). That is small, and it is the author's.

---

## 2. Dead ends on the geometric line

These were in the integers → Clifford notes and did not survive. The archived texts are under
`A/05_papers/integers_clifford/`.

- **"The honeycomb band gap is 2Δ" as a law (P3).** With an independently fixed Δ (field-tuned
  silicene) it misses by 3–8× — sublattice screening. It survives only as the textbook identity of
  the gapped Dirac model, which is not a prediction.
  ([`A/05_papers/integers_clifford/P3_independent_delta_test.md`](https://github.com/TiredofSleep/trinity-infinity-geometry/blob/archive-2026-09-24/05_papers/integers_clifford/P3_independent_delta_test.md))
- **High-Tc, spin liquids and strange metals on one "duality" axis (P4).** A classification frame,
  not a mechanism — and it put the honeycomb on the wrong side (the honeycomb is bipartite;
  graphene's electrons are massless).
- **"Flow (hexagon) versus matter (square)" as a physical duality.** Broken: the triangular and
  honeycomb lattices had been treated as one "hex".
- **The "seven transfers"** of Clifford/Dirac tools onto a three-fold basis. One reached the
  spacetime algebra Cl(1,3), which the cube does not force; the rest were identifications, not
  results.
- **"Perpendicular mirrors anticommute."** False as stated: the reflection maps in two
  perpendicular mirrors commute. What anticommutes is two perpendicular *directions*, as elements of
  the Clifford algebra.
- **A "universal 1/3" in physical law** — the fluid (Leray) projection, "gravity's force law",
  quark charge, a copper-depletion strand. Each died; the geometric 1/3 of the tetrahedron is
  untouched.
- **In the 0–9 realization:** "[FORCED]" on 0 and 5–9 (each uses a different rule — see
  [`base/THE_INTEGERS.md`](base/THE_INTEGERS.md)); "the cube's two tetrahedra are the two
  chiralities" (false: a regular tetrahedron is achiral); "6 is the fusion, with symmetry D₆" (that
  is the flat hexagon's symmetry, not the octahedron's); the 0/7 pairing, the square/hex digit
  families, the "lens-centres", the mod-3 roles, the inhale/exhale of 7 → 8 → 9, and the "base-10
  reset" (readings carried over from the table program).
- **In the Bott note:** "period 8 = duality × trinity". Two invariants of periods 4 and 2 give period
  4; the factor of 2 is ℍ ⊗ ℍ ≅ ℝ(4), not a trinity (see
  [`towers/bott_periodicity.md`](towers/bott_periodicity.md)).
- **In P1:** "two independent routes to 54.74°". They are one fact, seen from the tetrahedron and
  from the cube.
- **J03 / J61's "Fossil-Variety Theorem" (the census's one open case, settled 2026-09-23).** The claim
  was that ETP equation 4295 has no finite type specimen, and that every finite model has profile at
  least 261. Both are false:
  - a type specimen exists with six elements, the smallest possible order;
  - the bound fails at order 3, where one model has profile 122.

  The evidence: every model of orders 2–5, enumerated, and a script that rebuilds the ETP catalog
  ([the correction](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen14/targets/journals/J_series/J61/J61_THEOREM5_IS_FALSE.md)).

  The rest of J61's §6 falls the same way. It listed eight such families of laws, called one more of
  them a "fossil", and conjectured that six have no finite specimen. **All eight have one.** The
  smallest have 3, 5 or 6 elements; the two hardest families need between 8 and 32. Reading each table
  the other way round pairs the families off, two sides and an edge, so one specimen for each pair does
  the work of two
  ([the follow-up](https://github.com/TiredofSleep/ck/blob/tig-synthesis/Gen14/targets/journals/J_series/J61/J61_CLOSURES_ALL_REALIZED.md)).
- **The Q series (April 2026; audited 2026-09-24).** Q2–Q17, with C. A. Luther's G6–G8, built a
  "hidden operator" σ under the tables. It then tried to explain a search's success rate with σ,
  through CRT, idempotents and polynomials. The census had not covered it; a separate audit found
  that nothing in it is at once correct, table-free and non-generic.
  - The rate it set out to explain, "4.6% at b = 10", was misread from the data: b = 10 gives 0.09%.
  - The rates depend only on how many symbols are units. That is the algorithm's own symmetry, so no
    arithmetic structure could enter them.
  - Its Q2 "paradox" compared one AI rendering's table cell with a value of σ.

  What it leaves is a set of honest negatives, including an explicit counterexample showing that a
  periodic symbolic coding does not bound a norm, and six lessons. The first is to read the script
  that made a number before modelling the number
  ([the audit](https://github.com/TiredofSleep/ck/blob/tig-synthesis/papers/Q_SERIES_AUDIT_2026-09-24.md)).
- **The April 2026 "meta-lens atlas"** (ck, branch `paradox-classifier-2026-04-24`). It organized the
  table program's results (so(8), so(10), the "UOP–GUT arc") under the paradox classification, and it is
  retired with them. Its table-free core — the author's four paradox types with Ben Mayes, and Theorem 0
  — was kept and brought into [`coin/PARADOX_TYPES.md`](coin/PARADOX_TYPES.md).
- **The workstation [`ck`](https://github.com/TiredofSleep/ck).** It holds the whole trail of the
  earlier program, and it was retired in place on 2026-09-23. Nothing there was deleted: its front
  door, its side branches (including ten funding pitches) and its claim-making documents carry
  retirement banners, and its `RETIRED.md` records what was retired and what was salvaged.

### From the October 2026 chats (the 2026-10-22 handoff)

The readings that survive are in [`lab/FENCED_READINGS.md`](lab/FENCED_READINGS.md), and the binary
magic squares are in [`towers/binary_magic/`](towers/binary_magic/README.md). The earth-house kit keeps
its own graveyard. These died, with what killed them:

- **"0 and 7 are two states of one location", and "7 = 0".** 7 + 1 = 0 (mod 8), so 7 is −1. What
  is true is one shadow: numbered 000–111, the corners 0 and 7 both land on the centre when the cube
  is seen down its long diagonal, and they are opposite in the whole.
- **Matter and flow labels** on lenses, shapes and phases, and **"our structure lens is charged and our
  flow lens is balanced".**
  - In the clock-and-shift toy it runs backwards: the two-fold roots travel and the three-fold ones
    are stuck.
  - If the labels are defined by the outcome, the claim is circular.
  - The toy's own sentence survives: unbalanced charge is stuck; balanced charge travels.
- **"7 lifts into 8", "hex rules surround matter", "the void inhabits the form"** (as the reason
  centres fill), and **"7's centre is forced by the ring closing".** These are narrative. What is
  forced:
  - the cube's 8 corners are 6 + 2, a hexagon and two apexes, in the diagonal shadow;
  - the two shadows are related by cos² = 1/3;
  - every odd count in a solid fills its centre ([`base/SEVEN_AND_NINE.md`](base/SEVEN_AND_NINE.md)).
- **The cube's cos² = 1/3 as a metamaterial's refraction angle.** Refraction is set by index contrast,
  frequency and the unit cell.
- **SYK as TIG, a black-hole link, and the SYK phase diagram as "a coin with a vortex".** The picture
  is a phase diagram of temperature against flavour number; the likeness is pareidolia.
- **The Verlinde "factor of 400,000"** matching the Still Point paper's "400,000× miss". That is a
  coincidence of one number, with no shared structure.
- **"Cold fusion of the ground into rock", sonofusion, and "air prevents fusion".** No such process
  exists. The best bubble collapse reaches about 10⁴ K, while fusion needs about 10⁷ K, and the
  cavitation-fusion claims of 2002 were not replicated.
- **The 3-6-9 meme, and the Tesla quote, as evidence.** Digit sums are remainders mod 9, so multiples
  of 3 land on 3, 6 and 9. The quote has not been traced to anything he wrote.
- **The electron as a literal spinning ball.** Its surface would move at 171 c, and spin needs a
  720° turn.
- **The ħ/2 zitterbewegung "match" as evidence.** The radius ħ/(2mc) makes m·c·r = ħ/2 true by
  construction.
- **The void setting the mass, with no size rule, and crossings or voids setting mass.** For the
  proton, ħ/(2mc) is 8 times too small. The pion (140 MeV) and the rho (775 MeV) share quarks and
  track.
- **The pion as "vertical" or climbing, and the rho as "horizontal".** A particle at rest has no
  preferred up. The pion is the circling (Goldstone) mode, and the climbing mode is the sigma.
- **The size–weight illusion as support for the electron picture.** It is a fact about perception
  (Charpentier, 1891).
- **In the magic squares:**
  - **"0 48 64 192 0" read as a sequence law.** The author meant the three trefoil regions.
  - **Magic squares as knots, particles or physics.** The knot, the Dirac reading and the
    metasurfaces are encodings.
  - **The Hopf-link middle tier.** It depends on the drawing convention; only the 48 trefoils survive
    both conventions.
  - **"Franklin's 368,640", from memory.** The count is 1,105,920 bent-diagonal Franklin squares,
    368,640 of them pandiagonal (Schindel, Rempel and Loly, 2006).
  - **The carry rules, and the cancellation of the diagonals layer by layer, as new.** Both are
    Fitting's (1931).
- **"The anharmonic group"** as the name of the coin's three half-turns. Together with the identity
  they form the Klein four-group; the anharmonic group is the six cross-ratio maps. The flagship
  already says Klein four-group.

---

## 3. Where everything is

| | |
|---|---|
| the archived repository | tag [`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24) · branch `archive` |
| the audit | `A/04_meta/FOUNDATION_NULL_MODEL_AUDIT.md` and `A/verification/` (`foundation_null_model.py`, `attractor_null_census.py`, `remaining_rows_null.py`, `three_renderings.py`) |
| the census of all 56 papers | `A/04_meta/DRIFT_CENSUS.md` |
| the full working history | [`github.com/TiredofSleep/ck`](https://github.com/TiredofSleep/ck) (branch `tig-synthesis`) |
| the earlier public release | Zenodo v1.0.0, [10.5281/zenodo.20149181](https://doi.org/10.5281/zenodo.20149181) |
