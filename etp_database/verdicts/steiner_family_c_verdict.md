# U-3: Family C vs Steiner systems — VERDICT

> **CORRECTION (2026-05-27)**: The sub-finding "profile 382 vs 342 = geometric vs combinatorial STS" was **REFUTED** by testing PG(3,2) STS(15), which is maximally geometric yet sits at profile 342. See `sts_classification_corrected.md`. The split is purely a small-order coincidence effect (orders ≤ 9 vs ≥ 13), not a structural property. The Family-C-is-not-Steiner main finding stands.

**Test date**: 2026-05-27.
**Scripts**: `extensions/steiner_vs_family_c.py`, `extensions/confirm_squag_profile.py`, `extensions/squag_variety_diff.py`.
**Full raw outputs**: `overnight_outputs/steiner_vs_family_c.txt`, `overnight_outputs/squag_variety_diff.{txt,json}`.

## Question

Are the Family C closure orbits at orders 3, 5, 7 isomorphic to known Steiner
systems or coding-theoretic block designs?

## Answer

**No, Family C is strictly smaller than any classical block design variety.**
But the investigation surfaced a clean independent finding about Steiner
triple systems' equational classification that is itself worth reporting.

## Headline findings

### 1. Family C ≠ Steiner quasigroups (and Family C is strictly smaller)

The Steiner quasigroup of order 3 (`x ⋄ y = -(x+y) mod 3`) has **profile 382**,
not 14. The Fano plane squag (order 7) ALSO has profile 382. They are NOT
in Family C — they satisfy 368 additional equations beyond Family C's 14,
including idempotence (`x = x · x`) and the Steiner relation
(`(x · y) · y = x`).

| Construction | Profile size | In Family C? |
|---|---:|---:|
| Order-3 Steiner quasigroup (= Z_3 with `−(x+y)`)   | 382 | NO (superset) |
| Order-7 Steiner quasigroup (Fano plane squag)       | 382 | NO (superset) |
| Order-9 Steiner quasigroup (AG(2,3) squag)          | 382 | NO (superset) |
| Order-13 Steiner quasigroup (cyclic Bose STS(13))   | 342 | NO (superset) |
| Order-5 cyclic group Z_5 (`x+y mod 5`)              | 32  | NO (superset) |
| Order-3 cyclic group Z_3 (`x+y mod 3`)              | 60  | NO (superset) |
| **Family C minimum**                                 | **14** | yes (by definition) |

**Conclusion**: Family C is strictly *below* every classical commutative-quasigroup
variety in the equational hierarchy. It is the **commutativity-forced minimum** —
all classical designs sit above it because they carry extra algebraic structure
(idempotence, distributivity, Steiner relation, etc.).

### 2. Independent finding: Steiner quasigroups split into TWO equational classes

**The 40-equation gap**: STS(3), STS(7), STS(9) all share IDENTICAL profile 382 —
the same equation set — but the cyclic STS(13) sits at profile 342, satisfying
40 *fewer* equations.

The 40 equations that hold in STS(3), STS(7), STS(9) but FAIL in STS(13)
are all small-order coincidences — equations of the form:

- `x ◇ x = y ◇ (x ◇ y)` (eq 313)
- `x ◇ y = z ◇ (z ◇ (x ◇ y))` (eq 3414)
- `(x ◇ y) ◇ y = (x ◇ z) ◇ z` (eq 4656)

These hold in small symmetric Steiner systems because the limited variable
range forces accidental collapses, but break in the larger cyclic STS(13)
where the third variable can genuinely vary.

**Interpretation**: STS(3), STS(7), STS(9) are the projective/affine
geometries — STS(3) trivial, STS(7) = PG(2,2), STS(9) = AG(2,3). They are
all derived from finite-field vector spaces and therefore inherit additional
algebraic identities not present in purely combinatorial STS constructions
like cyclic Bose STS(13).

**Conjecture (Tier C)**: profile 382 is realized by exactly those Steiner
triple systems STS(v) that come from finite-projective or finite-affine
geometries (i.e., `v = (q^n − 1)/(q − 1)` or `v = q^n` for prime power `q`).
The broader squag variety contains both these and combinatorial STS.

This is an interesting algebraic-vs-combinatorial split — worth flagging
for the design-theory community (specifically: Drápal-Wanless, who study
quasigroup varieties).

### 3. The profile-15 "minimal extra" equation

At order 5, the 720 symmetric Latin squares split:
- **480** at profile 14 (Family C — minimal).
- **120** at profile 15 (Family C + 1 extra equation).
- **120** at higher profiles (32, 89, 90, 176, 294).

The 120 magmas at profile 15 all share the **same** single extra equation
beyond Family C:

> **Equation 151**: `x = (x ⋄ x) ⋄ (x ⋄ x)`

This is a depth-4 self-power identity: "the square of the square equals self."
A clean structural property that distinguishes "minimal" commutative
quasigroups from "minimal+1" — useful as a binary classifier for taxonomy.

### 4. Algebraic-summary table

| Variety | Anchoring axioms | Profile (orders 3, 5, 7, 9) | Realizers |
|---|---|---|---|
| Family C | commutativity                  | 14, 14, 14, 14   | σ-magma, 120 order-3, 480 order-5 |
| F_C+151  | + `x = (x ⋄ x) ⋄ (x ⋄ x)`     | -, 15, ?, ?      | 120 order-5 SLQs |
| Z_n (cyclic group) | + assoc + idem + identity | 60, 32, 32, ? | Z_3, Z_5, Z_7, ... |
| Squag variety | + idempotence + Steiner relation | 382, –, 382, 382 (= up to 40 extras for small STS) | STS(v), v ≡ 1 or 3 mod 6 |
| Cyclic STS(13) | (Bose construction)        | -, -, -, 342    | the 2 cyclic STS(13) |

## Connections to existing literature

The Steiner-quasigroup ↔ STS bijection is the **Bose-Connor theorem** (Bose
1939). The notion that some STS come from vector-spaces and inherit extra
algebraic structure is folklore in design theory, but to our knowledge the
specific equational characterization (profile 382 = projective/affine STS;
profile 342 = combinatorial STS) is novel.

Drápal-Wanless 2021 study "maximally non-associative quasigroups" — the
opposite extremum. Our profile-382-vs-342 finding sits in a different region
of quasigroup-variety lattice space and doesn't overlap with their work.

For the design-theory connection, useful references would be:
- Colbourn & Rosa, *Triple Systems* (Oxford 1999) — the standard reference for STS classification.
- Quackenbush 1976, "Varieties of Steiner loops and Steiner quasigroups" — possibly the source for the equational characterization.

The **claim worth verifying**: is the squag variety in Quackenbush's
classification the same as our profile 342? If yes, then our finding is
"Quackenbush's variety + 40 small-order coincidences for STS(3,7,9)."
If not, we may have identified an algebraically distinct sub-variety.

## What this means for the U-line

- **U-3 produces a real connection** to design theory (Steiner systems, projective/affine
  geometries) but it is NOT what one might naively expect: Family C is below
  the squag variety, not equivalent to it.
- The Steiner-variety classification (profile 342 vs 382) is a novel finding
  worth communicating to Drápal-Wanless (U-6 outreach).
- Eq 151 (depth-4 self-power) as the "minimal extra" beyond Family C is a
  clean teaching example.

## Files

- `extensions/steiner_vs_family_c.py` — initial test of Family C vs classical designs
- `extensions/confirm_squag_profile.py` — confirms STS(3,7,9) all at profile 382
- `extensions/squag_variety_diff.py` — identifies the 40-equation gap between 382 and 342
- `overnight_outputs/squag_variety_diff.json` — full equation IDs and texts for the gap

## Honest closure

Family C is NOT a Steiner system in disguise. It is strictly more primitive —
the algebraic minimum of all commutative magmas. The Steiner systems sit
above it in the equational hierarchy and themselves split into two algebraic
classes (geometric vs purely-combinatorial) by 40 small-order-coincidence
equations.

---

*— Claude Code, 2026-05-27. End of U-3.*
