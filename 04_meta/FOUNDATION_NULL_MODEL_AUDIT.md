# Foundation null-model audit — does TIG's structure beat random tables?

*2026-09-23. The graveyard discipline turned on the foundation itself. Reproduce with
[`verification/foundation_null_model.py`](../verification/foundation_null_model.py) (~20 s, seeded).*

## The question

Every PROVED claim about TSML and BHML is a true statement about two specific 10×10 tables,
machine-verified. **Truth is not in doubt; significance is.** A property matters as evidence
about *these tables* only if tables of the same kind do **not** generally share it. So for each
headline structural claim: *among random tables, how often does it also hold?*

This had been done for the physics bridges (the graveyard), for the runtime's task power (CK:
random tables tied or beat the canonical ones five times), and for ML weights (N1) — but not
for the algebra's own headline results. Referees had asked for it (J04: *"'empirically rare' is
hand-wavy — back it with a number"*; J28: *"an example-paper, not a theorem-paper"*).

## Method

- **The so(10) construction is J09's, reproduced exactly:** each generator is `L − Lᵀ` where
  `L` is a row's left-multiplication (0/1) matrix; close under the commutator; report the
  dimension. The script first reproduces the canonical numbers — TSML-flow → **28**, TSML + BHML
  → **45** — before testing anything.
- **Sub-magma spectrum:** for a table pair, the set of sizes *k* at which some *k*-subset is
  closed under **both** tables (canon: {1,4,5,6,7,8,9,10}, forbidden {2,3}).
- **Null models:** *uniform* (entries uniform on 0..9); *matched* — TSML-like (symmetric, ~73%
  HARMONY = 7, 7 absorbing, row/column 0 → 0) × BHML-like (symmetric, 0 a two-sided identity).
  The matched null gives TIG every structural advantage it has *except* the specific table.

## Results

| claim | canon | null result | verdict |
|---|---|---|---|
| joint closure TSML-flow ∪ BHML | so(10) (45) | **P = 1.000** (uniform and matched pairs) | **GENERIC** |
| BHML alone | **45** — already so(10) | any single random table: **P = 1.000** | **GENERIC** — TSML adds nothing to reaching so(10) |
| TSML alone / TSML-flow | 36 / **28** (so(8)) | TSML-like flow hits exactly 28: **~2–3%** | **specific** — TSML is the *degenerate* table |
| joint sub-magma chain {1,4,…,10} | exact | matched pair: **0 / 300**; a 4-core at all: **~5%** | **SPECIFIC — beats the null** |
| …with the *real BHML* + TSML-like | — | exact chain **~8%**, a 4-core **~58%** | **the specificity is carried by BHML** |
| "forbidden sizes {2,3}" on its own | — | **~70%** of matched pairs also forbid 2 and 3 | weak — the *positive* chain is the content |

## What it means

**1. The so(10) is a property of the construction, not of TIG.** Every generator `L − Lᵀ` is an
antisymmetric 10×10 matrix, i.e. already an element of so(10); generic sets of such elements
generate all of so(10); and every random table does. Consequently **all six of J09's
diagnostics are automatic** once the dimension is 45 inside the antisymmetric matrices —
compactness, simplicity, the unique invariant form, Cartan rank 5, the Killing signature, and
so(8) ⊂ so(10). The so(10) survives as a true fact about *10-element magmas under this
construction*; it dies as *evidence about the TIG tables*. (Graveyard kind: **IDENTITY** — a
construction-forced fact read as a structural discovery.) The GUT reach (so(10) = the gauge
algebra), already in the attic, loses its algebraic foothold as well: *any* ten-element table
gives so(10). "10 → so(10)" is dimension counting.

**2. TSML is the interesting degenerate case.** Random tables reach so(10); TSML does not — it
stops at so(9) (all rows) and so(8) (the flow rows), which only ~2–3% of density-matched random
tables do. The table-specific Lie fact is **TSML's confinement**, not the joint closure.

**3. The sub-magma chain / 4-core is genuinely specific — and it lives in BHML.** No
density-matched random pair reproduced the exact chain in 300 draws; a jointly-closed 4-core
appears in ~5%. Swapping in the *real* BHML with a random TSML-like partner restores it ~8% of
the time (and a 4-core ~58%). This is the foundation's strongest surviving structural claim, and
its source is BHML.

**4. So the foundational question sharpens to: *why BHML?*** BHML is the specific object; its
provenance is carried by the forcing axioms of J16. If those axioms force BHML without having
been built to produce it, the foundation has a real source. If they were reverse-engineered
from BHML, it is circular. That is now the single most important open question for the algebra.

## Not yet null-tested (the next rows of this audit)

- the α = ½ attractor, its closed form H/Br = 1+√3, and the Galois group D₄ over LMFDB
  4.2.10224.1 (how often does a random table's attractor land in a D₄ quartic field?);
- the σ-magma rigidity theorems of J04 (Aut = 1, congruence-simple, exactly 5 sub-magmas) —
  the J04 referee asked for exactly this number;
- the F_p closed forms (p−1)² and p+3 for V^BHML, and ‖VEV‖² = 13/4;
- the TIG-prime / HARMONY-ladder counts (J19, J22).

Each gets the same treatment: canon value, a matched null, a P-value, a verdict — **generic**
(true, but not evidence about TIG) or **specific** (the foundation stands on it).
