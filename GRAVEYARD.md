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
  headline theorems are fixed) — all classical or elementary. A second reading in October found more errors
  in those ten (§3). About twenty contain a false or mislabeled statement — one (J42) has an "empirical"
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
- **From the 2026-10-24 round** (magic sets and the code lens):
  - **"A genuine 6-qubit magic set with 20 observables beats the published 35."** The even-n graph stars hide a
    smaller clash, a padded pentagram, so they are not critical and not fair records. The independent
    referee found this, and it is now Theorem B.
  - **"Graph stars are proven smallest."** Only n = 5 is under test, and its last case is open.
    *Update, 2026-10-24:* the last case came back empty, so at n = 5 the claim now holds among context-minimal sets
    (16 is the exact minimum, `magic_sets/LOWER_BOUND.md`). For every other n, and for the published sets' wider
    class, it is still dead as stated.
  - **"Better noise tolerance than the published sets at n = 5."** The tolerance is 2/(n + 2), and the
    published MS5-27 does better (0.37).
  - **The tesseract-code link, the Freudenthal–Tits "magic" name, and the √(n/3) "three"** as more than a
    dictionary or a coincidence of names.
  - **"Nimm0 is proved here for the first time."** Fitting proved it by hand in 1931 (§III). What is new is
    the pairwise relaxation.
  - **"Invertible ⟺ 3-bit fold."** False: 288 singular squares have 3-bit mirror folds too. Only "on an
    invertible square every mirror fold flips 3 bits" holds (code lens Round 7;
    `towers/binary_magic/code_lens/void_fold_check.py`).
  - **"The center's squares all have a complement fold"**, with fold meaning a mirror. Only 240 of the 576
    do; the rest are complemented by a row or column swap or by the half-turn.
  - **A single-plane 2-adic certificate of invertibility.** Impossible by structure. A flipped plane's
    2 × 2 minor is always even (Round 7, V6 and V11, with the hand reason in the code lens's PREREG), so a
    hand proof of "no complement ⟹ invertible" has to mix bit planes.
  - **"Singular ⟺ complement symmetry" as a new exhaustion result.** These are Dudeney's types I–VI, which
    Trigg settled by computation in 1948. Only the uniform Walsh proof of one direction is new here.
  - **"Moler's doubly-even rank 3 is open."** Manjunath & Ambikasaran proved it in 2022 (Theorem 9). The void
    form is the same factorization.
  - **"The affine-digit family gives every pandiagonal 5×5 square"** (void lens D3). It gives only 800. The rest
    need arbitrary digit relabelings, which forced the (1 − ω)-adic proof (Round 8b).
  - **"Every kernel has a void"** (void lens H2). At order 5, 5 of 19 annealed singular squares have none: their
    kernels are accidental small-integer relations (`void_lens/round8c.log`).
- **From the kernel ledger (2026-10-24/25; `towers/kernel_ledger/PREREG.md`):**
  - **One subgroup's cosets certify every vanishing DFT minor** (K3a, K3b). They miss the main mechanism,
    aliasing. The repaired class-pigeonhole certificate covers 87–89% at n = 12 and 16.
  - **"4 seen as 5": singular 5×5 kernels merge two lines or drop one** (K6, 0 of 3). Seen at 0.89 against a 0.845
    chance baseline: small-integer kernels repeat by pigeonhole.
  - **Narrow 5-adic thresholds** (T3: 8.8× against a registered 10×; T6: a badly scaled lattice estimate). The
    excess of weighted zeros is real, but its mechanism is still open.
- **"The anharmonic group"** as the name of the coin's three half-turns. Together with the identity
  they form the Klein four-group; the anharmonic group is the six cross-ratio maps. The flagship
  already says Klein four-group.

---

## 3. The J series, read again — 2026-10-25

In September the census found ten papers whose mathematics stands (§1). On 2026-10-25 those ten, with J03
and J56, were read again by three independent audits, with fresh code for every claim. The census had been
too generous: every one of the ten contains at least one false or unsupported statement. The full table, with an
evidence script for every finding, is in [`graveyard/j_series_reread/`](graveyard/j_series_reread/README.md).
The headlines:

- **J27's "Crossing Lemma" is backwards** (wrong on 10,680 of 12,284 cases), and **J34's Theorem A and
  J35's Theorem 3.1 are false**, first at n = 15. The corrected criteria, with proofs, are in
  [`coin/TWO_READINGS_OF_ZN.md`](coin/TWO_READINGS_OF_ZN.md).
- **J43 mislabels its own representation** ([3,1] called [2,1,1]). Its pulse table misses its target, and
  its closure check cannot fail.
- **J24's Remark 7.4 is false** (sinc² is convex at ½, not concave), it misstates what Montgomery proved, and
  **J26's continuum limit is off by a factor k**.
- **J56's 125× comes from how its test suite was built.** Its numbers are not reproducible, and its reservoir
  does no better with the retired tables than with random ones.
- **J03's Theorem 5 is false.** Law #4295 has a 6-element type specimen, and the bound "at least 261 laws"
  fails at order 3, where a model obeys 122. The six "fossils" it named all have finite specimens.
- **J05's conjecture fails at n = 6**, where −(x + y) mod 6 obeys 297 laws, not 294; its count for
  (2x + 2y) mod 3 is 382, not 179; and its smallest commutative profile at order 3 is 14, not 29.
- **The ETP database's Steiner verdict is false:** the 13-point system and PG(3,2) obey 382 laws, not 342.
  None of its four OEIS drafts is worth submitting.

What came in instead is nine pages, seven of classical mathematics and two small new results, listed in
[`CONTRIBUTIONS.md`](CONTRIBUTIONS.md#read-again-the-j-series-2026-10-25).

---

## 4. Where everything is

| | |
|---|---|
| the archived repository | tag [`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24) · branch `archive` |
| the audit | `A/04_meta/FOUNDATION_NULL_MODEL_AUDIT.md` and `A/verification/` (`foundation_null_model.py`, `attractor_null_census.py`, `remaining_rows_null.py`, `three_renderings.py`) |
| the census of all 56 papers | `A/04_meta/DRIFT_CENSUS.md` |
| the full working history | [`github.com/TiredofSleep/ck`](https://github.com/TiredofSleep/ck) (branch `tig-synthesis`) |
| the earlier public release | Zenodo v1.0.0, [10.5281/zenodo.20149181](https://doi.org/10.5281/zenodo.20149181) |
