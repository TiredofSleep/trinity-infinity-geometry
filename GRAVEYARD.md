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
  - WP34's "Luther dispersion conjecture" (March 2026), that the gate rate is a function of |G| × dispersion,
    died by the same symmetry: the dispersion cannot enter the rate. The dispersion itself stands, exactly, in
    `towers/THE_STAIRCASE.md` §9 (2026-11-14).

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
  - **A hidden quarter-turn symmetry behind the weighted quarter** (K10, 2026-10-27, from the author's question; 0
    of 2). Quarter-turn complements are 1.20× as common as in nonsingular squares, against 1.5× needed, and a
    square's row kernel and column kernel are never the same lever (0 of 264) (`towers/kernel_ledger/quarter_turn.py`).
- **From the generation loop (2026-10-30; `lab/generation_loop/PREREG.md`)**, fenced physics, tested against the cube:
  - **Small sums of cube rotations give Koide's 2/3** (G1a): 0 of 17,344.
  - **The quark families carry the leptons' angle 2/9** (G7, G9: −214 to −255σ, in every mass convention tried),
    **or the published cross-family triplets are exactly Koide** (G8: +6.3σ and −3.4σ in the fixed convention).
  - **A correction term that fills the gap between exact Koide and an exact 2/9 can be found by search** (G10): hits
    come only at the chance rate, under the registered calibration and under two more
    (`lab/generation_loop/g10_calibration_check.py`).
- **From the seven levels (2026-11-07; `towers/seven_levels/PREREG.md`):**
  - **"No seven-level state has more Wigner negativity than the Legendre state"** (Q7, a registered guess). A
    search found 0.7325 against the Legendre state's 0.7283, at a state that is not even odd under the half turn
    (`towers/seven_levels/verify_seven_levels.log` gives it to 8 decimals).
  - **"The Legendre state is still the deepest odd state at eleven levels"** (T8, a registered guess,
    2026-11-08). A million climbs among the odd states found 1.029707, against the Legendre state's 0.787711, at a
    state with 24 symmetries: the binary tetrahedral group, the strange state's group at three
    (`towers/seven_levels/round3.log`; `verify_seven_levels.py` checks it). The Legendre state is the deepest odd
    state at 3 and at 7, the second by an exhaustive count, but not at 11.
  - **"At thirteen the two sides end within 0.01"** (U9, a registered guess, 2026-11-08). Three million climbs
    on each side found the even side ahead by 0.017 (`towers/seven_levels/round4_thirteen.log`). The size reading
    that made the guess is half dead: from 7 on no winner is fixed by its symmetries, as it said, but the margin
    is wider when p is 1 more than a multiple of 4.
  - **Round 5's guesses from the pattern at 3 to 13** (2026-11-08; `towers/seven_levels/round5_*.log`):
    - "The even side wins at 19" (V2), and with it "the best state found at 19 is even about one point" (V5b):
      the odd side wins at 19, 1.507862 against 1.484879, and a second even search with a fresh seed found the
      same even best.
    - "The margins shrink" (V4a, V4b): the even side's lead at 17 is 0.031, wider than 13's 0.017, and at 19
      there is no even lead at all.
    - "A highly symmetric state wins the odd side at 19" (V6): the odd winner has 4 symmetries; the tetrahedral
      state, with 24, comes below it.
  - **Round 6's two readings** (2026-11-08; `towers/seven_levels/round6_*.log`):
    - The author's prediction, "even only wins the lows, the odd wins the rest" (W1): the even side wins at 23,
      by 0.0036, and a recheck with a fresh seed confirmed it. At 29 the odd side wins, as the author said.
    - "The Legendre state's side wins" (W2): the even side wins at 23 and the odd side at 29, the opposite of both
      its calls.
  - **"The best turning-symmetric state beats the best multiplying-symmetric one at every prime"** (round 8's Y1,
    2026-11-08; `towers/seven_levels/two_wheels_*.log`). At 13 the multiplying wheel's order-4 family reaches 1.167364
    against the turning wheel's 1.105229, which is exact: the verifier counts every sign choice in the turning wheel's
    order-7 family. The test was confounded by family size: at 13 the turning wheel offers only orders 7 and 14.
  - **The author's 7-wheel: "the even side wins exactly when the powers of 7 modulo p pass through the half turn"**
    (round 7's X1, 2026-11-10; `towers/seven_levels/round7_*.log`). At 31 the 7-wheel has period 15 and never reaches
    the half turn, so the rule called the odd side, but the even side wins, 2.045297 against 2.031473. A recheck with a fresh seed, two million more odd climbs and kicks from the highest odd tops, found the same odd best and nothing higher.
    The rule had fitted the eight primes it was read from. With 31, no number wheel of any base from 2 to 30 fits
    every decided prime.
  - **Round 10's guesses on the larger arrays** (2026-11-10; `towers/seven_levels/larger_arrays_*.log`):
    - "On three wheels of 5 nothing beats the best norm-type state, and it beats both sides' bests" (round 10's V1
      and V2 there; both held on three wheels of 7). A climb from a kicked norm-type state reached 4.301387, and both
      sides' bests, 4.293476 (even) and 4.291598 (odd), beat the norm-type states' 4.252724. The Kloosterman closed
      form, derived during the run, shows why: at 5 the norm state reaches only 83.5% of the ceiling, below the
      product of the smaller arrays' bests. The winner found is still on neither face, a reshaped norm-type state.
    - "Every new array's best beats every product of smaller arrays' bests" (V4). On five wheels of 3 the best climb
      reached 6.082020, below 517/81 = 6.382716, the four-wheel best times a one-wheel best. That product is itself a
      state of the array, so the death is the search's: 4 000 climbs on each side ended 0.30 below it
      (`towers/seven_levels/product_climbs.log`).
    - "With an odd number of wheels the odd side wins" (V5, Claude's reading, registered as resting on one array). The
      even side won on three wheels of 5, by 0.0019, and on five of 3, where both sides fell short of a known product.
    - "Every array's best reaches 88% of its ceiling" (V6): 84.5% on three wheels of 5, and 83.4% on five of 3, where
      the best known state, the product, reaches 87.5%.
  - **Round 13's guesses on cubic magic** (2026-11-14; `towers/seven_levels/cubic_magic_*.log`):
    - "The most negative two-qudit states are cubic-phase states" (K2): the best two-wheel cubics fall short,
      (9 + 3√5)/10 against 1.766937 at 5 and 2.567775 against 2.719253 at 7.
    - "Some cubic beats the norm form on three wheels of 5" (K4): none of the 9 765 625 forms does, though elliptic
      curves with 8 points tie it.
  - **Round 14's guesses** (2026-11-14; `towers/seven_levels/planes_*.log`):
    - "The triangle unfolds again at 11 and not at 7 or 13" (T1), and "the tying curves have p + 3 points" (T2): no
      curve but the norm class ties the norm value at 7, 11 or 13.
    - "The Fano cubic beats random cubics" (F1) and "exceeds Sato–Tate's share" (F2): it reaches 0.642, 0.558 and 0.560
      of √q at 3, 5 and 7, against about 0.80 for random cubics.
    - "The affine-plane cubic beats random cubics" (F3): 0.779 and 0.788 at 3 and 5, against 0.811 and 0.798.
    - Not a registered prediction, but a reading the run falsified: round 13's "the norm state is the most magic
      three-qudit cubic" holds only at 3, 5 and 7. At 11 and 13 smooth curves beat it (15.013610 against 14.900798;
      19.498692 against 18.887726).
- **From the genetic-code study (2026-11-08; `lab/genetic_code/PREREG.md`, fenced):**
  - **"The vertebrate mitochondrial code is less optimized than the standard code"** (G1, a registered guess).
    51 of a million random codes with its own blocks beat it, against 98 for the standard code.
  - **"With transition bias, the best code found keeps the third-letter symmetry"** (G2). The best code found
    costs exactly what the best symmetric code costs, but it breaks the third-letter pairing. The prediction was
    worded too narrowly for its own model: the model weighs the three letters alike, and the polar-requirement
    scale ties threonine with proline and leucine with isoleucine. With the ties merged, the code is symmetric at
    its second letter (`lab/genetic_code/verify_code_symmetry.py`).
  - **"With Freeland and Hurst's weights, the standard code is more optimized than the mitochondrial code"**
    (part 2's H2, a guess from the literature). None of a million random codes with its own blocks beat the
    mitochondrial code, against 3 of a million for the standard code.
- **From the fifth moments (2026-11-14; `towers/seven_levels/TORUS_MOMENTS.md` §8):**
  - **"The level-15 form is not in our fifth moments"** (round 16's search, repeated in `HOW_WE_WORK.md`). It is in
    J5, through Kloosterman's fifth moment, beside an elliptic curve of conductor 150 that the search's library lacked.
    The search tried the form with characters, never together with a curve. A correct form missing from the list
    looks exactly like no form at all (`towers/seven_levels/verify_fifth_moment.py`, step 10).
  - **The Q(√−11) family as I5's form.** Split by the class of w, the part of I5's count with w on the circle holds a
    surface sum. That sum carries the weight-3 CM form of Q(√−11) and a weight-1 form of the cubic field of
    discriminant −44, exactly, at every prime tried. Neither is in I5: they cancel against the rest. Kept for its
    lesson: a piece of a count can carry motives the whole does not (step 13 of the same script).
- **From the coin at 5 (2026-11-14; `towers/seven_levels/COIN_AT_FIVE.md` §2, round 19's C1):**
  - **"At the edge prime, every formula holds with the symbol's 0, the average of its two sides."** That held for the
    moment without the parity flip, I5, at p = 5 (3504) and at p = 3 (368), and Theorem 5's J4 holds at 3. It died for
    the parity-weighted moments. The operators give J3 = 24 at 3 (registered −12 or 0), J5 = 240 at 3 (registered
    −84 or −192) and J5 = −1680 at 5 (registered −930) (`towers/seven_levels/coin_at_five_test.log`).
  - Theorems 6 and 7 were written for p ≥ 7, so no stated theorem fell. What died is the reading that the edge
    averages the sides for every moment. At its edge J3 is +2p(p + 1), the mirror of its (−3|p) = −1 side.
- **From the coin's edge and eleven (2026-11-14; `towers/seven_levels/COIN_AT_FIVE.md` §5 and §7, rounds 21 and 22):**
  - **"At the edge, a moment is minus its −1 side."** This was read off J3 at 3. It fits J5 at 3 for no integer
    a_E(3): 240 would need a_E(3) = −5/3. Round 19's log killed it before round 21 registered the rule in its
    surviving form.
  - **"The mirror rule for J5 at 5,"** as the drafter asked it on 2026-11-14, is ill-posed: no symbol of J5's formula
    has its edge at 5. J5's deviation at 5 is the bad reduction of its elliptic curve. Its phase-0 count keeps only
    the six pentagons (v, −v, v, −v, v) (`towers/seven_levels/edge_rule_test.log`).
  - **Q(√−385) as the field at 11**, the alternative to round 22's Q3′, with 2 ramified in place of 3. The field is
    Q(√−1155) (`towers/seven_levels/edge_rule_test22.log`).
- **From thirteen (2026-11-14; `towers/seven_levels/COIN_AT_FIVE.md` §8, round 23):**
  - **"The piece at 13 splits into a twisted Tate class and a weight-5 CM form"** (S2). p divides T13/p⁵ at none of
    the 73 primes from 17 to 401, and a CM part would vanish at about half of them
    (`towers/seven_levels/edge_rule_test23.log`).
    - S3 to S7 named the parts of that split and are void with it. That includes the two guesses, (5|p) with
      Q(√−3003), the icosahedron's √5, and (13|p) with Q(√−1155).
    - The piece is a twisted symmetric square instead, held blind in round 24.
  - **"The signed roots' product is a CM field at 13."** Q(√−15015) has class number 96 and exponent 12. A rational
    weight-5 CM form needs exponent dividing 4, so this was ruled out before the test. The product lives on as the
    determinant's character.
- **From seventeen (2026-11-15; `towers/seven_levels/COIN_AT_FIVE.md` §10, round 25):**
  - **"A piece keeps a line exactly when the base's n points keep an axis"** (Z3). This was the drafter's exact version
    of the reading at 13 that the author took up. Klein's finite rotation groups either keep an axis (the polygons'
    groups) or keep none (the icosahedron's).
    - The base gives the regular 17-gon at 17, which keeps its axis, so the dictionary predicted that 17's piece splits.
    - p divides T17/p⁷ at only 2 of the 72 primes from 19 to 401, and no CM field fits. 17's piece keeps no line: it
      is a twisted symmetric square, like 13's (`towers/seven_levels/edge_rule_test25.log`).
    - The guess that named the split's parts, (17|p) with Q(√−3003), is void with it.
    - What survives is the observation, not the link: the three-dimensional pieces at 13, 17 and 21 are all unsplit.
  - **Not held, not dead: twenty-one's sign test** (D2). Only 3 primes to 113 had |T21/p⁹| > p², and the test asked
    for 5. All three signs agree with (−138567|p), and an unregistered test supports it at all 22 primes. Round 26 read
    the determinant at every prime (Y4), and it held.
- **From twenty-seven (2026-11-15; `towers/seven_levels/COIN_AT_FIVE.md` §11, round 26):** nothing died.
  - **Not held, not dead:** two sign tests saw too few signs. Y2′ saw 8 large traces of V27 where it asked for 10. W1
    saw 1 large trace of V25 where it asked for 5. None of their signs disagreed
    (`towers/seven_levels/edge_rule_test26.log`).
  - **The rivals that lost:** "3 enters at 27" and "5 enters at 25", as readings of V27's determinant. They fit 13 and
    14 of the 27 primes, at chance level, where the thin rule fits all 27.
- **From eighty-one and twenty-five (2026-11-15; `towers/seven_levels/COIN_AT_FIVE.md` §12, round 27):** nothing
  died. Five of five held.
  - **The rival that lost again:** "5 enters at 25", now as a reading of V25's own determinant, (15935205|p). Read at
    every prime from the fields of p, p² and p³ elements, it fits 14 of 27 primes. It is wrong at all 13 where it
    differs from (3187041|p), which fits all 27 (`towers/seven_levels/edge_rule_test27.log`).
  - **Ruled out before the count:** "3 does not enter at 81". It would leave V81's determinant odd, and V81's Hodge
    types require it even (`towers/seven_levels/edge_rule_verify27.log`, F14).
- **From Theorem 8 and round 28 (2026-11-16; `towers/seven_levels/DETERMINANTS.md`, PREREG round 28):** nothing
  died. Five of five held.
  - **The rival that lost:** Yun's symbol without the cube's 3, (p/k!!), as a reading of the Airy determinants.
    At 29, 31 and 39, where it differs from (p/A_k), it fits 11 of 24 primes each, at chance level
    (`towers/seven_levels/edge_rule_test28.log`). Complex conjugation had already ruled it out there by sign.
- **From the edge at 137 (2026-11-14; `lab/alpha_137/PREREG.md`, fenced):**
  - **"The prime gradient at 137 makes the inverse fine-structure constant"** (A1 and A2, the author's reading).
    Of 630 registered expressions built from the compression, the taper, the staircase and the qudit floor at 137,
    the nearest is 137 + ln 137/137 = 137.035912, which misses 137.035999177 by 8.7 × 10⁻⁵, 4 100 times the
    measurement's uncertainty (A1). A grammar this size comes that close to a random target 2.2% of the time,
    against the registered bar of 1% (A2). The decoys were ordinary (`lab/alpha_137/alpha_test_run.log`).
  - **An earlier attempt, WP124 (May 2026),** wrote 1/α ≈ 4·|Aut(V)| − 2√7 − π/7 − … from the retired tables and
    claimed 10⁻⁵. Its leading terms give 154.26, not 137.036 (the ck repository's
    `Atlas/META_PLAN_2026-05-06/STATUS_REPORT_2026-05-07.md`).
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
