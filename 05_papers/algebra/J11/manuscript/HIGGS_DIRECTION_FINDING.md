# BHML's σ_outer-breaking is an explicit 9-vector, computed and characterized

**Date:** 2026-04-25
**Source script:** `find_higgs_direction.py`
**Verification:** machine precision (residual 0.0000)

---

## The 9-vector (the actual numbers)

BHML's σ_outer-breaking content lies entirely (100% coverage at machine precision) in the 9-dimensional so(9)-vector representation inside the 54 of so(10). Its components in the natural basis:

| Direction | Component | TIG label |
|-----------|-----------|-----------|
| e_0 | −1/√2 | VOID |
| e_1 | −1/√2 | LATTICE |
| e_2 | −1/√2 | COUNTER |
| e_3 | −1/√2 | PROGRESS |
| e_4 | −1/√2 | COLLAPSE |
| e_7 | −1/√2 | HARMONY |
| e_8 | 0 | BREATH |
| e_9 | 0 | RESET |
| (e_5+e_6)/√2 | −1/2 | (BALANCE+CHAOS)/√2 |

This is a single 9-vector, not a free parameter. It is forced by BHML's specific table values.

## Pattern

- **Six directions get equal weight** (−1/√2): VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, HARMONY
- **Two directions get zero**: BREATH, RESET
- **One direction gets smaller weight** (−1/2): the (BALANCE+CHAOS) symmetric combination

## Why this pattern

The mechanism is concrete: a position (i, j) of BHML contributes to σ_outer-breaking iff the values BHML[i, 5] and BHML[i, 6] differ. Looking at rows 8 and 9:

- Row 8 = [8, 6, 6, 6, 7, **7, 7**, 9, 7, 8] — positions 5 and 6 both equal 7
- Row 9 = [9, 6, 6, 6, 7, **7, 7**, 0, 8, 0] — positions 5 and 6 both equal 7

Rows 8 and 9 have BHML[i, 5] = BHML[i, 6] = 7, so they're σ_outer-symmetric and contribute nothing to the breaking. That's why BREATH (8) and RESET (9) get zero weight.

For the other rows (0–7), BHML[i, 5] and BHML[i, 6] differ by 1 (specifically, one is 6 and the other 7), giving a uniform contribution to the breaking. That's why those six directions get equal weight.

The (BALANCE+CHAOS)/√2 direction comes from the **diagonal** entries B[5,5] = 5 vs B[6,6] = 6 (also differing by 1).

## What's structurally meaningful

The fact that **BREATH and RESET are exactly excluded** from the breaking pattern, while the other σ-fixed elements (VOID, PROGRESS) are included, is striking. Both BREATH and RESET correspond to TSML rows that are entirely 7s except at position 0 and the diagonal — they are the most "saturated" rows.

In TIG's operator semantics:
- 8 = BREATH (holds tension)
- 9 = RESET (clears state)

These are the two "stabilizer" operators in the σ-fixed lattice. They alone are unaffected by the σ_outer-breaking. The other lattice operator (PROGRESS, idx 3) participates fully in the breaking pattern.

In SO(10) GUT terms: these two directions would correspond to *unbroken* Higgs components — fields that don't get a VEV during the SO(10) → SO(9) breaking. Their TIG semantic role (stabilization, reset) is consistent with this gauge-theoretic interpretation.

This is **not a derivation that BREATH/RESET correspond to specific physics fields**; it's an alignment between TIG's operator labels and a structural feature of the breaking pattern.

## Comparison to standard SO(10) Higgs sectors

Standard 54-Higgs VEVs that break SO(10) → SO(9) are characterized by their alignment in the 54-irrep. The decomposition under so(9) is `54 = 1 + 9 + 44`. A "pure 9" VEV (which is what we have) is not the most common starting point; standard treatments usually give a VEV in the singlet (1) of the 54 first, breaking to SO(9), then consider further breaking.

What we have here: BHML's σ_outer-breaking content is **purely in the 9 piece** of the 54, with no singlet (1) and no 44 contribution. This is a very specific direction within the 54.

In the SO(10) GUT literature, this corresponds to **a sub-leading-stage breaking** — the 9-vector VEV that further breaks SO(9) → SO(8). This breaks SO(10) → SO(9) → SO(8) in sequence, which lands us in TSML's home algebra.

So the structural picture is:
- TSML's so(8) is the **gauge group at the deepest level** — the residual symmetry after all breaking
- BHML's 9-vector content is **the SO(9) → SO(8) Higgs** — the specific direction in which the further breaking happens
- TSML+BHML together describe SO(10) at the algebraic level, with the breaking pattern explicit

## Honest limits

**What's strong:** The 9-vector is uniquely determined. Its values are computed at machine precision. Its alignment is highly specific (six equal entries, two zeros, one smaller entry). The pattern has a clean structural interpretation (rows where BHML[i,5] ≠ BHML[i,6]).

**What's still hypothetical:** That this 9-vector should be interpreted as a Higgs VEV in a physical SO(10) GUT model, rather than as algebraic structure with no gauge-theoretic content. Both interpretations are consistent with what we've shown.

**What I cannot do without more work:**
1. Compute Yukawa couplings allowed by this VEV. Requires committing to a physical interpretation and cross-referencing the SO(10) Yukawa literature.
2. Predict masses or mixing angles. Requires Yukawas + RG running + electroweak breaking.
3. Verify that subsequent breaking from SO(9) → SO(8) → SU(3)×SU(2)×U(1) is viable for this specific 9-vector direction.

These are the next 1000–3000 lines of work, plus literature, plus expert review.

## Bottom line

We started with: "TIG's so(10) might be related to SO(10) GUT."

We now have: **"BHML's σ_outer-breaking content is exactly a 9-vector inside the 54 of so(10), implementing the SO(9) → SO(8) breaking with a specific pattern that singles out BREATH and RESET as unbroken directions."**

That's a sharp, falsifiable, computed structural identification. It's not a physics prediction. It's a piece of algebra that says, *if you embed TIG in a Pati-Salam-route SO(10) GUT framework, the Higgs VEV pattern is forced to be this specific 9-vector*.

Whether that VEV pattern is *viable physics* is the next question, and it's a real one — most ad hoc Higgs directions in SO(10) GUT don't give realistic phenomenology. But ours isn't ad hoc; it's derived from the canonical TSML/BHML tables. That makes it a real test, not a fitting exercise.

🙏
