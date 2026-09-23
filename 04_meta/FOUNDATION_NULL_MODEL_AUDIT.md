# Foundation null-model audit — does TIG's structure beat random tables?

*2026-09-23. The graveyard discipline turned on the foundation itself. Reproduce with
[`verification/foundation_null_model.py`](../verification/foundation_null_model.py) (~25 s, seeded) and
[`verification/attractor_null_census.py`](../verification/attractor_null_census.py) (a few minutes, exhaustive).*

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

## Not yet run (the next rows)

- the σ-magma rigidity theorems of J04 (Aut = 1, congruence-simple, exactly 5 sub-magmas) — the
  J04 referee asked for exactly this number;
- the F_p closed forms (p−1)² and p+3 for V^BHML, and ‖VEV‖² = 13/4 (canon traces the 13 to
  BHML's 26 = 2·13 σ-asymmetric cells — a cell count, so a readout candidate);
- the TIG-prime / HARMONY-ladder counts (J19, J22);
- **the forcing question** — a stated principle for Rule 89 and S₆/S₇, and the count of every
  table that satisfies it.

Each gets the same three gates: **true → specific → not a readout.**
