# Foundation null-model audit — does TIG's structure beat random tables?

*2026-09-23/24. The graveyard discipline turned on the foundation itself. Reproduce with
[`verification/foundation_null_model.py`](../verification/foundation_null_model.py) (~25 s, seeded),
[`verification/attractor_null_census.py`](../verification/attractor_null_census.py) (~2 min, exhaustive),
[`verification/remaining_rows_null.py`](../verification/remaining_rows_null.py) (~50 s) and
[`verification/three_renderings.py`](../verification/three_renderings.py) (~30 s). The repo-wide
consequence — how much of TIG is built on these results — is [`DRIFT_CENSUS.md`](DRIFT_CENSUS.md).*

## The question

Every PROVED claim about TSML and BHML is a true statement about two specific 10×10 tables,
machine-verified. **Truth is not in doubt; significance is.** A structural claim counts as
*evidence about these tables* only if it passes three gates:

1. **True** — machine-verified. *(Every claim below passes.)*
2. **Specific** — random tables of the same kind do **not** generally share it.
3. **Not a readout** — it survives a null that **keeps the tables' own construction rules** and
   varies only what the rules leave free. A property that follows in a few lines from how a table
   was built is a faithful *description of the build*, not independent evidence about it.

This had been done for the physics bridges (the graveyard), for the runtime's task power (CK:
random tables tied or beat the canonical ones five times), and for ML weights (N1) — but not
for the algebra's own headline results. Referees had asked for it (J04: *"'empirically rare' is
hand-wavy — back it with a number"*; J28: *"an example-paper, not a theorem-paper"*). The first
pass ran gate 2; a same-day second pass ran gate 3 on everything that passed gate 2 — and that is
where the verdict changes.

## Method

- **The so(10) construction is J09's, reproduced exactly:** each generator is `L − Lᵀ` where
  `L` is a row's left-multiplication (0/1) matrix; close under the commutator; report the
  dimension. The script first reproduces the canonical numbers — TSML-flow → **28**, TSML + BHML
  → **45** — before testing anything.
- **Sub-magma spectrum:** for a table pair, the set of sizes *k* at which some *k*-subset is
  closed under **both** tables (canon: {1,4,5,6,7,8,9,10}, forbidden {2,3}).
- **Gate-2 nulls:** *uniform* (entries uniform on 0..9); *matched* — TSML-like (symmetric, ~73%
  HARMONY = 7, 7 absorbing, row/column 0 → 0) × BHML-like (symmetric, 0 a two-sided identity).
- **Gate-3 nulls (rule-preserving):** BHML is built by four rules (canon §6) — Rule 0 (VOID is the
  identity), Rule 1 (`max(i,j)+1` on 1..6), Rule 7 (row 7 is the successor `j+1 mod 10`), and
  **Rule 89 (rows 8, 9 listed cell by cell)**. TSML is fixed by J16's axioms — S₂–S₄ (VOID
  near-absorbing, HARMONY absorbing, diagonal → HARMONY) and **S₆/S₇ (five exceptional positions
  and their values, listed)**. The gate-3 nulls keep the stated rules and randomize the listed ones.
- **The attractor** is the α = ½ fixed point of `p ↦ ½·fuse(p,p,TSML) + ½·fuse(p,p,BHML)`; its
  census is **exhaustive** over every BHML top block on {0,7,8,9} (fields identified exactly by
  120-digit PSLQ; Galois groups by sympy).

## Results

| claim | canon | gate 2 — random tables | gate 3 — construction rules kept | verdict |
|---|---|---|---|---|
| joint closure TSML-flow ∪ BHML → so(10) | 45 | **P = 1.000** (uniform and matched pairs; BHML *alone* reaches 45; any single random table does) | — | **GENERIC** |
| maximal associative spectrum (Catalan s₄ = 5, ac-free 15 — canon §6.1's "free commutative operad") | both tables | **P = 1.000** (random commutative tables) | — | **GENERIC** |
| joint sub-magma chain {1,4,…,10} / the 4-core | exact | matched pair **0/300** (4-core ~5%); real BHML + TSML-like ~8% | Rule 89 random: **0.2%** — Rule 89 random but **climbing**: every closed upper set kept, **P = 1.000** | **READOUT** of "products climb" |
| "forbidden sizes {2,3}" | — | ~70% of matched pairs also forbid them | two diagonal cells: 8·8 = 7 and TSML 9·9 = 7 | weak, and a readout |
| TSML-flow → so(8) (all rows → so(9)) | 28 / 36 | TSML-like flow hits 28: **~2.7%** | common kernel span{e₀, e₅ − e₆}: the **twins 5 ≡ 6** + an isolated VOID | **READOUT** of S₆ (which positions are exceptional) |
| α = ½ attractor: H/Br = 1+√3, quartic field, Galois D₄ (LMFDB 4.2.10224.1) | exact | — | closed form = three BHML cells; quartic-D₄ in **22/64** Rule-89 variants (**240/4096** of all top blocks) | **READOUT** (value) · **COMMON** (D₄) |
| "α = ½ is privileged" (field degree drops) | 4 at ½ vs 7 or more at 1/3, 2/5, 3/5, 2/3 | — | degree drops at α = ½ in **64/64** Rule-89 variants | **GENERIC to the construction** |
| J04 σ-magma x◇y = σ(x+y mod 10): Aut = 1, congruence-simple | both | random isotopes π(x+y): Aut = 1 **99.8%**, simple **98.9%** | — | **GENERIC** |
| J04: exactly 5 sub-magmas, one non-generating pair | exact | 2.5% / 10–14% | a fingerprint of the particular σ | **READOUT of σ** |
| J18/J53: \|Aut(V^BHML/F_p)\| = (p−1)², \|idem\| = p+3, "24 primes" | verified p = 3,5,7 (idem to 13) | idem counts polynomial in p for **64%** of random 0/1 algebras | few-line derivation for every odd p (two free scalings; a line + 3 points) | **READOUT** |
| J11: BHML's P₅₆-anti part "in the 54", ‖v‖² = 13/4 | exact | traceless for random symmetric tables **P = 1.000** | 26 cells where rows/cols 5, 6 differ; Rule 89 redrawn: 13/4 in 1.1% | **GENERIC** (54) · **READOUT** (13/4) |
| J19: prime 11 divides exactly c₂, c₈ of charpoly(TSML_RAW) | true of RAW | 42% of the 26 single-swap typos, 58% of random tables, have *some* such prime | RAW is a **two-digit transcription error** of the original table (which has 11 dividing only c₇) | **TRANSCRIPTION ARTIFACT** |
| J22: the 70/71/72/73 HARMONY ladder | exact | — | 73 defined (S₅); 71 = 73 − 2 (S₂); \|T≠B\| = 71 in ~13% of S₆/S₇ redraws; det = 70 in **0/3000** Rule-89 redraws | **NUMEROLOGY** |

## What the second pass found — the mechanism behind what beat the null

### The chain / 4-core is the upper-set lattice of a climbing operation

Order the symbols by BHML's own ladder, **1 < 2 < … < 9 < 0** (VOID on top — the successor wraps
9 → 0).

- **Lemma 1.** BHML(a,b) ≥ min(a,b) for every pair except the single cell **8·8 = 7**. (Rules 1
  and 7 climb by definition — max+1 and successor; Rule 89's listed rows climb too, except 8·8.)
- **Lemma 2.** Every TSML product is 0, 7, or ≥ min(a,b) — its five exceptional cells all climb.
- Hence every upper set {0} ∪ {k..9} that contains 7 (k ≤ 7) is closed under both tables. And
  because the BHML diagonal is the successor on 1..7 (D90), squaring climbs from any element to 7,
  then 7·7 = 8, 7·8 = 9, 7·9 = 0 — so the joint closure of any set is the upper set above its
  least element. **The jointly closed sets are exactly {0} and these seven upper sets**
  (exhaustive enumeration: 8 sets, all upper sets).
- The **4-core {0,7,8,9} is the smallest upper set that survives** — the successor orbit of 7
  (7 → 8 → 9 → 0 → 7).
- **The forbidden sizes are two diagonal cells:** {8,9,0} is broken by 8·8 = 7 (in both tables);
  {9,0} by TSML's 9·9 = 7 (set TSML(9,9) = 0 and size 2 returns).
- **Rule-preserving null:** keep Rules 0/1/7 and randomize Rule 89 → the exact chain appears
  0.2% of the time; randomize Rule 89 **subject only to climbing** → all seven upper sets are
  jointly closed every time (P = 1.000). The specificity against random tables is entirely the
  climbing character of the rules.

### TSML's so(8) is two twin elements

- The generators from TSML's flow rows share a 2-dimensional kernel, **span{e₀, e₅ − e₆}**; so(8)
  is the rotation algebra of its 8-dimensional complement.
- **e₅ − e₆:** 5 and 6 are the only elements (besides 0 and 7) that none of S₆'s five exceptional
  pairs {1,2}, {2,4}, {2,9}, {3,9}, {4,8} touches — so their rows and columns are identical (all
  HARMONY), and neither is ever produced. TSML cannot tell 5 from 6.
- **e₀:** in every row except 0 and 7, VOID is produced only from VOID. (Every row except 0 and 7
  gives 28 — the "flow" selection is immaterial; adding row 0 or 7 breaks e₀, giving so(9).)
- The Lie-algebra language adds nothing beyond "TSML cannot tell 5 from 6."

### The attractor's closed form is three cells; its D₄ is common; its α = ½ is generic

- On the 4-core, TSML never produces BREATH, and BHML produces it from exactly three cells:
  0·8 (identity), 8·9, 7·7. At α = ½ the BREATH equation is 2·br = 2·v·br + 2·br·r + h², and with
  v + h + br + r = 1 it closes as (h/br)² − 2(h/br) − 2 = 0 — the derivation already in
  `J16/.../06_attractor_closed_form.py`. **The value 1+√3 is those three cells.**
- The full attractor lies in a quartic field with Galois group D₄ (minimal polynomial
  443x⁴ − 810x³ + 526x² − 138x + 11, discriminant −2617344 = −10224·16²). **Exhaustive census:**
  with the three Rule-89 top cells free (64 tables), 22 land in a quartic D₄ field like canon
  (30 in S₄, 9 cubic, 3 quadratic); with all six BHML top cells free (4096 tables), 240 do
  (684 quartic in all; 1096 have no fixed-point attractor). D₄ is what a quartic with a quadratic
  subfield generically has — **common, not a signature.**
- **α = ½ lowers the field degree in all 64 Rule-89 variants** (≤ 4 at α = ½; 5–7 at α = 1/3 and
  2/3). The privilege comes from the construction, not from TIG's particular cells (plausibly:
  commutativity doubles every off-diagonal term and α = ½ halves it back against BHML's identity
  row, as in the BREATH equation above — the census verifies the effect, not this explanation).

## What it means

**1. Two headline results are generic** — true of almost every table: the joint so(10) (every
generator `L − Lᵀ` already lies in so(10), and generic sets span it; all six J09 diagnostics follow
automatically from dimension 45; "10 → so(10)" is dimension counting) and the maximal associative
spectrum. Graveyard kind ② IDENTITY: construction-forced facts read as structural discoveries.
The GUT reach, already in the attic, loses its algebraic foothold.

**2. Every specific result we opened is a readout of a construction rule** — the chain and the
4-core ("products climb"), TSML's so(8) ("S₆ avoids 5 and 6"), the attractor's closed form (three
BHML cells). Each survives as a **corollary with a short proof**; none is independent evidence.
This is the D180 pattern — real, but tautological relative to the build.

**3. So the evidential weight of the algebra sits entirely on the rules — and the rules split in
two:**

- **stated with a reason:** VOID the identity (BHML) / near-absorber (TSML S₂); HARMONY absorbing
  (S₃); diagonal → HARMONY (S₄); BHML max+1 on 1..6; BHML row 7 the successor;
- **listed without one:** BHML **Rule 89** (rows 8, 9) and TSML **S₆/S₇** (the five exceptional
  positions and values).

Every specific result traces to a *listed* rule: the chain needs Rule 89 to climb (0.2% of free
completions do); TSML's so(8) is S₆'s avoidance of 5 and 6; the attractor's √3 is two Rule-7/89
cells plus the identity.

**4. The foundational question therefore moves from "why these structures?" — they follow in a
few lines — to "why these rules?"** Specifically: *is there a principle that forces Rule 89 and
S₆/S₇?* J16 forces TSML *by listing* S₆/S₇ (its own README: "explicit listings, not derived from a
deeper principle"); no forcing paper exists for BHML. Climbing is not that principle: it admits
10·9·8·7·6·5 choices for each of rows 8 and 9 and 18 for the top cells — about **4 × 10¹¹**
climbing completions of Rule 89 — and BHML's own 8·8 = 7 is not climbing. The test is concrete:
state a candidate principle, enumerate every table that satisfies it, count. If the canonical
tables are unique (or nearly), the foundation gains a real source; if many qualify, what is common
to the whole family is theorem and what is specific to TIG is choice.

**5. What this does not touch.** The book (`shape-of-understanding`) uses only the universal floor
(Stratum I) — nothing in it depends on the tables. And the cut is the familiar one: the tables stay
a precise frame to measure *from* (floor, pointer); they stop counting as evidence *about*
anything beyond their own rules (seed, premise).

## The remaining rows (run 2026-09-24)

Reproduce with [`verification/remaining_rows_null.py`](../verification/remaining_rows_null.py) (~50 s).

- **J04, the σ-magma** x◇y = σ((x+y) mod 10). Its headline rigidity is what *every* isotope of
  ℤ/10 has: among random permutations π, x◇y = π(x+y) has trivial automorphism group 99.8% of the
  time and is congruence-simple 98.9% of the time (same within σ's own cycle type). The remaining
  facts — exactly five sub-magmas (2.5% of isotopes), a single non-generating pair (10–14%) — are
  the fingerprint of the particular σ. Two further notes: σ itself first appears 2026-04-01 (the
  "morphotic braid", four weeks after the tables), and the σ-magma is built on **addition mod 10**
  — the ℤ/10 reading of the symbols that the author has explicitly rejected.
- **J18 / J53, the F_p closed forms.** Verified exactly (|Aut| = 4, 16, 36 at p = 3, 5, 7; |idem| =
  p+3 through p = 13), and both follow in a few lines for every odd p: in the 4×4 table, e₀
  annihilates everything and e₄ enters products only linearly, so both scale freely — (p−1)²;
  the idempotent equations are x₀ = 0, 2x₂x₃ = x₃, x₂² + x₃² = x₂, (2x₃ − 1)x₄ = 0, giving {0, e₂},
  one point with x₃ = −½, and a whole *line* with x₃ = +½ — p + 3. Checking "24 primes" was
  checking a two-line identity numerically. (Point counts that are polynomial in p are the rule
  for such algebras: 64% of random 0/1 algebras have them for idempotents.) Also: J18's
  "BHML 4-core algebra" table is not BHML's 4-core — it is a further 4×4 construction.
- **J11, ‖v‖² = 13/4.** The P₅₆-antisymmetric part of BHML has 26 nonzero entries, all ±½ — the
  cells where rows and columns 5 and 6 of BHML differ (columns 0,1,2,3,4,7, doubled twice, plus
  two diagonal cells) — so ‖·‖²_F = 13/2 and J11's normalization gives 13/4. "Lies in the 54" is
  automatic (the transposition-antisymmetric part of any symmetric table is traceless: 500/500).
  With Rule 89 redrawn, 13/4 recurs 1.1% of the time. A cell count, read as a Higgs VEV.
- **J19, the prime 11.** True of TSML_RAW — and TSML_RAW is a **transcription error**. The
  original table (the ck repository's first commit, CK Gen9, 2026-03-03, `ck.h`) has row 9 = 0,7,9,3,7,…; the digit string
  `0797377777`, with the 3 and 7 swapped, first appears 2026-04-25, when the table was retyped for
  the so(10) sprint. The swap was then read as "the wobble", "a directional (permutation/braiding)
  bit", and "the strictly more-informative lens" (`TSML_RECONCILIATION.md`), with a plan to make
  it the default. On the original table 11 divides only c₇; J19's comparison matrix "T_SYM"
  (c₂ = −23) is neither symmetrization — it sets both swapped cells to 7, deleting TSML's
  exceptional cell (3,9). And the pattern type is common: 11 of the 26 possible single-swap typos
  (42%), and 58% of random tables, have some prime between 11 and 97 dividing exactly two
  coefficients.
- **J22, the ladder.** Unlike numbers juxtaposed: 73 is the count S₅ defines; 71 = 73 − 2 is
  forced by S₂ (VOID absorbs except at (0,7)); |TSML ≠ BHML| = 71 recurs in ~13% of redraws of
  TSML's listed cells; det(BHML on {1..6,8,9}) = 70 occurs in none of 3000 redraws of Rule 89 — a
  single integer, read as C(8,4) (J18 itself calls it "an integer coincidence at small scale").

## Provenance — where the tables came from

The author's account (2026-09-24): **AI built these tables from verbal descriptions of the ten
operators.** The source history agrees and adds dates:

| date | event |
|---|---|
| before 2026-03 | **CL_STD** ("the Standard table, 44 harmony", from the author's first repo): VOID an identity, the core "add until HARMONY" — min(i+j, 7) on 1..6 except 5·5 = 6·6 = BREATH |
| 2026-03-02 | an audit finds the running table has 72 HARMONY cells where the spec said 44 ("28 operators had drifted to harmony during a prior reconstruction"); the discrepancy is named the "Being table" (→ TSML) vs the "Becoming table" — per chat-Claude's reconstruction, `ck/Atlas/applications_pass_2026_04_27/ORIGIN_OF_TSML_INVESTIGATION.md` |
| 2026-03-03 | the ck repository's first commit (CK Gen9): `ck.h` holds all three — TSML (73), BHML (28), STD (44) — and the five "quantum bump pairs" that become TSML's exceptional cells |
| 2026-04-01 | σ = [0,7,1,3,2,4,5,6,8,9] introduced as the "morphotic braid" |
| 2026-04-25 | the table is retyped as digit strings for the so(10) sprint; row 9 acquires the swapped digits (TSML_RAW) |

TSML differs from STD in 53 of 100 cells (31 became HARMONY, 16 flipped VOID from identity to
absorber, the five bump cells took new values); BHML differs from STD in 49.

## Three renderings of one set of descriptions

Reproduce with [`verification/three_renderings.py`](../verification/three_renderings.py) (~30 s).
STD, TSML and BHML are three AI renderings of the same descriptions — so a property shared by all
three is plausibly the **descriptions'** content, and a property of one rendering is the
**rendering's**.

- **Shared by all three:** {VOID, HARMONY, BREATH, RESET} closes on itself in every rendering, and
  jointly in every pairing. Beyond that, the renderings agree on only **12 of the 55** unordered
  cells: VOID·VOID = VOID, VOID·HARMONY = HARMONY, LATTICE·COUNTER = PROGRESS, BALANCE·BREATH =
  HARMONY, BREATH·BREATH = HARMONY, and CHAOS with LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE,
  HARMONY or BREATH = HARMONY.
- **Rendering-level:** VOID's very role (identity in STD and BHML, absorber in TSML); RESET·RESET;
  the Lie closure (so(9), so(9), so(10)); the joint chain with forbidden sizes {2,3} (TSML+BHML
  only — STD+BHML allows size 2, STD+TSML every size); H/Br = 1+√3 (the two pairings in which
  exactly one table has HARMONY·HARMONY = BREATH; STD+BHML gives 1.1667); every count built on one
  table (73, 71, 70, 13/4, 26, the prime 11).

**This answers the forcing question empirically.** The descriptions did not force a table: they
were rendered three times and the renderings disagree on 49–71 of 100 cells. What the descriptions
do fix — the closed {VOID, HARMONY, BREATH, RESET} subsystem and about a fifth of the cells — is
the author's content. Everything the papers derive from one rendering's particular cells is a
property of that rendering.

Each future claim gets the same three gates — **true → specific → not a readout** — plus a
fourth: **does it hold in every rendering of the descriptions?**
