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

---

## 3. Where everything is

| | |
|---|---|
| the archived repository | tag [`archive-2026-09-24`](https://github.com/TiredofSleep/trinity-infinity-geometry/tree/archive-2026-09-24) · branch `archive` |
| the audit | `A/04_meta/FOUNDATION_NULL_MODEL_AUDIT.md` and `A/verification/` (`foundation_null_model.py`, `attractor_null_census.py`, `remaining_rows_null.py`, `three_renderings.py`) |
| the census of all 56 papers | `A/04_meta/DRIFT_CENSUS.md` |
| the full working history | [`github.com/TiredofSleep/ck`](https://github.com/TiredofSleep/ck) (branch `tig-synthesis`) |
| the earlier public release | Zenodo v1.0.0, [10.5281/zenodo.20149181](https://doi.org/10.5281/zenodo.20149181) |
