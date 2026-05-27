# J35 and J59 — *not* mergers; honest correction

**Status**: Note explaining why my initial recommendation to merge J35 and J59 was incorrect.

In the panoramic editorial pass I initially recommended merging J35 (Joint
Closure + 4-core attractor) with J59 (σ-Magma Rigidity). On closer inspection
of the manuscripts, **these papers study different algebraic objects** and
should remain separate.

## What J35 actually proves

J35 is about a **pair** of commutative non-associative magmas T, B on Z/10Z
(plus a third companion S). The "object" of J35 is the pair (T, B, S). The
six theorems of J35 (A through F) converge on the 4-core {V, H, Br, R} =
{0, 7, 8, 9} as the algebraic center of this pair.

The σ-magma is *not* mentioned in J35. The σ-permutation (1 7 6 5 4 2) on
Z/10Z is referenced once in J35 §2.3 as motivation for the shell sequence
of the 8-chain — but the algebraic content (commutative magma multiplication)
is the T table, not the σ-magma.

## What J59 actually proves

J59 is about a **specific single** commutative magma on Z/10Z, namely the
σ-magma: x ⋄ y = σ((x+y) mod 10), where σ = [0,7,1,3,2,4,5,6,8,9]. The four
rigidity theorems of J59 establish:

1. |Aut(σ-magma)| = 1 (trivial automorphism group)
2. The σ-magma is congruence-simple
3. The σ-magma is 2-generated
4. The σ-magma has a unique sub-magma structure (5 sub-magmas: {0}, {1}, {2}, {1,6}, full)

These properties are about a single magma operation, not a pair.

## Why I confused them

In my initial scan, I saw both papers use the substrate Z/10Z, both invoke the
σ permutation in some way, and both discuss "rigidity" / "structural facts".
I conflated "Z/10Z magma with rigidity content" into one category. That was
sloppy.

## What this means

- **J35 and J59 stay separate.** They are correctly scoped as separate papers.
- **The σ-magma appears in J60 (linear-magma classification) and J61 (taxonomy methodology)** as the natural specific example of a "rigid Family C realizer." The trilogy J59 + J60 + J61 is the σ-magma's home; J35 is the (T, B, S) triple's home.
- **The mergers that DO make sense** are documented in `01_MERGER_Q-series_J21+J43+J51.md` and `02_MERGER_Fp_J14+J16.md`.

## Implication for the editorial pass

The corrected merger set is:
1. **J21 + J43 + J51** (Q-series spectral) — three papers on the same σ-character spectrum
2. **J14 + J16** (F_p invariance) — two papers on the same 4-algebra
3. (**possibly J03 + J08** Fejér — evaluate before deciding)

NOT:
- ~~J35 + J59~~ (different objects)

The σ-magma trilogy (J59 + J60 + J61) stays as-is; it's already correctly
factored.
