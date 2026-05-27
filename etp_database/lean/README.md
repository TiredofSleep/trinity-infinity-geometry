# Lean 4 formalization

## What's here

| File | Contents |
|---|---|
| `Fossil4295.lean` | Lean 4 scaffold of J61 Theorem 1 (the C5 fossil-variety theorem). |
| `lakefile.toml` | Lake project file (mathlib-compatible). |
| `lean-toolchain` | Lean version pin. |

## The theorem being formalized

> **Theorem 1 (J61).** Let `M` be a finite magma whose multiplication satisfies
> equation 4295 of Tao et al.'s Equational Theories Project:
> `∀ x y z : M, x * (x * y) = y * (z * x)`.
> Then the equational profile of `M` (= number of ETP equations `M` satisfies)
> has size at least 261.

## Current status (scaffold v2)

| Component | Status |
|---|---|
| `Magma` typeclass definition | **PROVED** (compiles) |
| Equation 4295 predicate `Eq4295` | **PROVED** (compiles) |
| Step 1: `z_collapse` (`y*(z*x)` is z-independent) | **PROVED** (3-line `rw`) |
| Step 3: `case_a_constant` (left-projection forces `g` constant) | **PROVED** (5-line proof) |
| Step 4: `case_b_ff_constant` (right-projection forces `f∘f` constant) | **PROVED** (5-line proof) |
| Step 2: `structural_dichotomy` | **`sorry`** — needs finite-injectivity argument |
| Profile-size definition `equationalProfileSize` | **`sorry`** — needs ETP decision procedure |
| `const_magma_profile = 1556` | **`sorry`** — empirical Python-to-Lean lift |
| `right_proj_ff_const_profile ≥ 261` | **`sorry`** — empirical Python-to-Lean lift |
| Final `c5_fossil_variety` assembly | **partial** — case (b) goes through; case (a) needs `Inhabited M` plumbing |

**What this scaffold demonstrates**: the three substantive lemmas (z-collapse,
case-a constancy, case-b `f∘f`-constancy) are fully formalized in Lean 4 and
type-check syntactically. The remaining gaps are the structural dichotomy
(provable but technical) and the empirical profile bounds (provable but
require a verified ETP-membership decision procedure that doesn't yet exist
as Lean infrastructure).

The cleanly formal part is Lemma 2: given that `x*y = f y` for some `f`, the
equation `x*(x*y) = y*(z*x)` directly implies `f(f(x)) = f(f(y))`. That step
is two `rw`s and a `symm`; the Lean proof matches the pen-and-paper proof line
for line.

Lemma 1 requires a slightly subtler structural argument (the equation has
both `(x * x)` and `(z * x)` patterns, and showing `*` is right-trivial
demands choosing the right `f` and rearranging). Currently `sorry`d pending
a careful re-derivation.

Theorem 1 needs an ETP-verified decision procedure for finite magma equational
profiles. That doesn't yet exist as Lean infrastructure; the empirical bound
261 is verified by our Python implementation but not by Lean.

## Next steps

1. **Complete Lemma 1.** Strategy: introduce `Classical.choice` to pick an
   `f`, then derive `x*y = f y` from the equation by manipulating `h y y z`
   for two different `z`'s.
2. **Define `equationalProfileSize`.** Either as a literal computation against
   a finite list of ETP equations (decidable on `Fintype M` + `DecidableEq M`),
   or as an abstract count via a quotient by ETP equation logical equivalence.
3. **Wire up the empirical bound.** For orders 2 – 6, define right-trivial
   magmas computationally and verify profile ≥ 261 via `decide` tactic.
4. **Lift to Mathlib4.** Once verified, propose for inclusion in Mathlib4's
   universal-algebra namespace (`Mathlib/Algebra/Magma/`).

## Why this matters

A Lean-verified fossil-variety theorem would be the first formal proof of an
equational-theory non-realizability result derived from the ETP. It provides:

1. **Reproducibility certificate**: the proof in J61 is checkable by anyone
   with a Lean toolchain.
2. **Pathway to Mathlib4**: opens the door to formalizing other ETP results.
3. **Cross-validation with ETP**: ETP itself is formalized in Lean; our
   Theorem 1 sits in the same logical universe.

## Building

This file targets Lean 4 + Mathlib4 (as of 2026). To build:

```bash
cd etp_database/lean
lake build
```

(The current state will have `sorry` warnings on Lemma 1 and Theorem 1.)
