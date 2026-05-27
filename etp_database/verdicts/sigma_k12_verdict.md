# U-4: σ-magma K_12 lattice embedding — VERDICT: NO embedding

**Test date**: 2026-05-27.
**Script**: `extensions/sigma_k12_embedding.py`.
**Raw output**: `overnight_outputs/sigma_k12_embedding.txt`.

## Question

Does the order-10 σ-magma have a natural embedding into the automorphism
group Aut(K_12) of the Coxeter-Todd lattice K_12?

## Answer

**No**, with three independent structural obstructions:

### Obstruction 1 — Non-associativity

The σ-magma is non-associative: `(0 ⋄ 0) ⋄ 1 = σ(σ(0)+1) = σ(0+1) = 7`,
but `0 ⋄ (0 ⋄ 1) = 0 ⋄ 7 = σ(7) = 6`. So `(0⋄0)⋄1 ≠ 0⋄(0⋄1)`.

Any operation-preserving embedding ι: σ-magma → G into a group `G` would
have to satisfy `ι(x ⋄ y) = ι(x) · ι(y)` for some group product `·`.
But group products are associative, so the image of σ-magma would need
to be associative — contradicting the explicit non-associativity above.

**No σ-magma → group embedding exists, for ANY group G.** Not Aut(K_12);
not Aut(any lattice); not any group at all.

### Obstruction 2 — Trivial automorphism group

The σ-magma has |Aut(σ-magma)| = 1 (proved in J60 §6.2). It admits no
non-trivial group action on its element set. So there is no
"σ-magma-as-permutation-group-target" embedding to be found anywhere.

### Obstruction 3 — Left-regular representation not closed

For each `a ∈ {0..9}` the row permutation L_a (x ↦ a ⋄ x) is a permutation
of {0..9}. The 10 row permutations have varied cycle structures:

| Row | Order | Cycle structure |
|---:|---:|---|
| 0 | 6  | (6, 1, 1, 1, 1) |
| 1 | 4  | (4, 2, 1, 1, 1, 1) |
| 2 | **14** | (7, 2, 1) |
| 3 | 5  | (5, 5) |
| 4 | 6  | (6, 3, 1) |
| 5 | 8  | (8, 2) |
| 6 | 6  | (6, 2, 2) |
| 7 | **21** | (7, 3) |
| 8 | 10 | (10) |
| 9 | **21** | (7, 3) |

The set `{L_a : a ∈ Z_10}` is **NOT closed under composition** (since
σ-magma is non-associative). So even the natural quasigroup permutation
embedding fails.

### Curiosity worth noting

The presence of 7-cycles (rows 2, 7, 9) and orders 14, 21 in a 10-element
quasigroup is unusual. It signals an interaction between Z_10's additive
structure and σ's permutation structure that produces "phantom mod-7"
cycles — possibly related to σ's underlying 6-cycle action on
{1, 2, 4, 5, 6, 7}.

## What this means

The σ-magma is **algebraically isolated**. It is not a subobject of any
group, lattice automorphism group, or other associative structure. Its
mathematical content lies entirely in its own quasigroup structure and
the Family C equational profile.

This rules out the "σ-magma lives inside some known classical structure"
hypothesis. The σ-magma is genuinely *new* — not a re-skinning of a
familiar group-theoretic object.

## Where this leaves U-line investigation

**U-2** ruled out crypto use (algebraic minimality ≠ statistical
randomness).

**U-3** ruled out direct Steiner-system identification (Family C sits
strictly below the squag variety).

**U-4** (this) rules out group-embedding (algebraic non-associativity
+ trivial Aut + non-closed L_a).

What's left as a *positive* claim for σ-magma:
- It is the order-10 commutative quasigroup realizing Family C minimum.
- Its rigidity profile is structurally maximal (|Aut|=1, congruence-simple, 2-generated).
- It is the smallest known "fully rigid" Family C realizer.

The σ-magma's value is **internal to the magma taxonomy** — it serves as
an exemplar for equational minimality theorems (J60), not as a building
block for downstream structures. The U-line's positive U-tasks (U-5 Lean,
U-6 outreach) will be the path to actual usefulness.

---

*— Claude Code, 2026-05-27. End of U-4.*
