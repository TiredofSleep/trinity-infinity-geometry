# Is the operadic non-closure obstruction a genuine cohomological class, or an artifact of the restricted value space?

**A computational attempt at manuscript OPEN(c) / NON_CLOSURE_QUESTION.md §4.1.**
**Date:** 2026-09-22. **Companion code:** `cohomology_probe.py` (runnable with the project venv python; all numbers below are its output, cross-validated against textbook cohomology).

---

## Verdict (up front)

**COBOUNDARY-ARTIFACT.** The obstruction is **not** a genuine cohomological class. It is an artifact of (i) demanding equivariance under a group element that is not a symmetry of the magma, and (ii) restricting the fuse value to the input-derived set. Three independent, machine-checked lines of evidence agree:

1. **Strict Hochschild cohomology does not exist for this algebra.** The magma algebra `A = k[Z/10Z]` (`e_a · e_b = e_{T(a,b)}`) is non-associative, so the Hochschild differential fails `d²∘d¹ = 0`: `rank(d²∘d¹) = 87` over F₂ and `89` over F₃/F₅/char-0 — **nonzero**. There is therefore no Hochschild complex and no `H²`, `H³` in which the obstruction could be a class. (Harrison cohomology inherits the same failure and is likewise undefined.)

2. **In the theory that IS well-defined — group cohomology of the value module** `H^*(⟨σ³⟩, A)` and `H^*(D₄, A)` — the defect cochain is a **coboundary in every characteristic**, hence the **trivial class**; and away from characteristic 2 the higher cohomology **vanishes entirely** (Maschke, since `char ∤ |D₄| = 8`). There is no nonzero class anywhere for the defect to be.

3. **Root cause:** `σ³` is **not a symmetry of the magma `T` at any arity**. Of the 8 elements of `D₄`, only the identity and `P₅₆` are magma automorphisms; `σ³` violates equivariance on **80 of 100** arity-2 cells. The arity-3 "operadic obstruction" is the foregone shadow of this arity-2 non-symmetry — not a new higher-operadic phenomenon. Under the **genuine** symmetry `⟨P₅₆⟩ ≅ Z/2`, there is **no obstruction at all** (0 of 98 orbits incoherent; Family H is `P₅₆`-equivariant).

**Confidence: high** for "not a genuine cohomological class" (points 1–2 are exact finite-field linear algebra, and the bar-cohomology engine is validated against four textbook values). **High** for the root-cause reframing (point 3 is a direct table computation). The one modeling caveat — that the obstruction *is* genuine as a **set-valued / combinatorial** statement (Theorem 4.1 remains a true impossibility theorem) — is discussed in §6; it does not survive passage to the linear (cohomological) category, which is what "cohomological class" asks about.

---

## 1. Setup and the honest framing problem

The substrate is the finite magma `(Z/10Z, T)` with the canonical **TSML_RAW** table (identical to the verifier). To ask a *cohomological* question we linearize: let

> **A = k[Z/10Z]**, the 10-dimensional `k`-vector space with basis `e₀,…,e₉` and bilinear product `e_a · e_b = e_{T(a,b)}`.

Cohomology is well-defined linear algebra **only over a field**, so we work over the two CRT factor fields of the ground ring `Z/10Z = Z/2 × Z/5`, namely **F₂** and **F₅**, plus **F₃** (a control: the label gap `7−4 = 3` vanishes there) and a **large prime P = 1000003** as a faithful char-0 proxy.

The immediate obstacle — and the first honest finding — is that **`A` is non-associative** (126 of 1000 triples fail associativity). This matters enormously, because:

- Hochschild's `d² = 0` **requires associativity**. For non-associative `A`, the "cochain complex" is not a complex.
- So `H²(A,A)` and `H³(A,A)` — the groups OPEN(c) asks about — **are not defined**. This is not a technicality to wave away; it is the first part of the answer.

We therefore compute *four* distinct things and report exactly what each can and cannot say.

## 2. The defect and its mechanism (probe §A, §A2)

| Fact | Value |
|---|---|
| non-associative locus `\|N\|` | 126 |
| HARMONY `= 7` as a sink | occupies **73 / 100** cells of `T` |
| `σ³` | `(1 5)(2 6)(4 7)`, fixes `{0,3,8,9}` |
| the localized triple `(3,9,9)` | `L = 3`, `R = 7`, `σ³`-fixed; `σ³(7) = 4` |
| bracketing pairs on `N` | `{0,7}:108, {3,7}:8, {4,7}:2, {7,8}:6, {7,9}:2` — **all contain 7** |

Every non-associative disagreement routes through the sink value **7**, and **7 is not `σ³`-fixed** (`σ³` swaps `7↔4`). That single fact is the entire mechanism.

**Root cause (the decisive computation).** Is `D₄` even a symmetry of `T`? Test each `g ∈ D₄` for the magma-automorphism property `T(g·a, g·b) = g·T(a,b)`:

| `g ∈ D₄` | magma automorphism of `T`? | arity-2 cells consistent |
|---|---|---|
| identity | yes | 100/100 |
| `P₅₆ = (5 6)` | **yes** | **100/100** |
| `σ³` | **no** | **20/100** (80 violations) |
| other 5 elements | no | — |

**Only `{id, P₅₆}` are automorphisms.** The genuine symmetry group of the raw table inside `D₄` is `⟨P₅₆⟩ ≅ Z/2`, **not** `D₄`. Of `σ³`'s 80 arity-2 violations, **62 are exactly** "`T` lands on the sink 7 where `σ³`-equivariance demands 4." Consequently `N` is `P₅₆`-invariant (0/126 escape) but **not** `σ³`-invariant (45/126 escape).

> The `D₄` of the manuscript is the symmetry of the **derived bilinear closure** (the antisymmetrized Lie/Jordan algebra `so(10)`), whose support avoids the wobble cells (manuscript §0.2). It is **not** a symmetry of the **raw magma `T`**, which is what the arity-3 fuse question is posed on. Asking for `σ³`-equivariance of a ternary lift of `T` asks a non-symmetry to become a symmetry one arity up. That cannot succeed, and its failure is not a characteristic class.

## 3. Strict Hochschild: not a complex (probe §B)

Cochains `Cⁿ = Hom(A^{⊗n}, A)`, `dim Cⁿ = 10^{n+1}`. Differentials built as explicit integer matrices from `T`:
`d¹: C¹(100) → C²(1000)` and `d²: C²(1000) → C³(10000)`.

**The fatal check** `d² ∘ d¹ =? 0` (holds **iff** `A` is associative):

| field | F₂ | F₃ | F₅ | char-0 (P) |
|---|---|---|---|---|
| `rank(d² ∘ d¹)` | **87** | **89** | **89** | **89** |

Nonzero in every characteristic ⇒ **strict Hochschild cohomology is NOT DEFINED for `A`.** For the record, the individual (non-cohomological) dimensions:

| field | rank `d¹` | dim ker `d¹` | rank `d²` | dim ker `d²` |
|---|---|---|---|---|
| F₂ | 95 | 5 | 971 | 29 |
| F₃/F₅/char-0 | 96 | 4 | 972 | 28 |

These do **not** assemble into `H²` or `H³`: `im d¹ ⊄ ker d²` (precisely `rank(d²∘d¹) = 87/89` dimensions of `im d¹` are pushed out of `ker d²`). Harrison cohomology (the symmetric/commutative summand) is the natural refinement OPEN(c) also names, but it is a sub-theory of the same complex and inherits the same `d²≠0` failure — also undefined here. **The obstruction cannot be a Hochschild or Harrison class because those groups do not exist for this algebra.**

## 4. The well-defined theory: group cohomology of the value module (probe §C)

The obstruction is really about **`D₄`-equivariance of a value**, so the theory that houses it cleanly is **group cohomology `H^*(G, A)`** with `A = k^{10}` the permutation module. This is honest linear algebra (explicit bar/periodic complexes), and the engine is **validated** against textbook values:

`H^*(Z/2, F₂-trivial) = [1,1,1,1]` ✓ `H^*(Z/2, F₂[Z/2]) = [1,0,0,0]` ✓ `H^*(D₄, F₂-triv) = [1,2,3]` ✓ `H^*(D₄, F₃-triv) = [1,0,0]` ✓.

### 4.1 `G = ⟨σ³⟩ ≅ Z/2` acting on `A`

`σ³` has cycle type `4 fixed + 3 transpositions` on the basis, so `A ≅ (trivial)⁴ ⊕ (regular Z/2-rep)³`.

| field | `H⁰` | `H¹` | `H²` |
|---|---|---|---|
| **F₂** | 7 | **4** | **4** |
| F₃ | 7 | 0 | 0 |
| **F₅** | 7 | 0 | 0 |
| char-0 | 7 | 0 | 0 |

The nonzero `H¹ = H² = 4` in characteristic 2 comes entirely from the **four fixed points** `{0,3,8,9}` (the trivial summands). The defect lives elsewhere:

> **The defect cochain** `δ = e₇ − e₄ = (1 − σ³)·e₇`. The probe confirms in **every** field (F₂, F₃, F₅, char-0): `δ ∈ Z¹` (cocycle) **and** `δ ∈ B¹ = im(1−σ³)` (coboundary) ⇒ **`[δ] = 0`, the trivial class.**

So the localized `σ³`-defect is a coboundary in all characteristics — it sits in the **free/induced** (`(4 7)`-transposition) summand where `H^*(Z/2, −) = 0` regardless of characteristic. It is cohomologically invisible.

### 4.2 `G = D₄` acting on `A` (bar resolution)

| field | `H⁰` | `H¹` | `H²` |
|---|---|---|---|
| **F₂** | 6 | 11 | 16 |
| F₃ | 6 | 0 | 0 |
| **F₅** | 6 | 0 | 0 |
| char-0 | 6 | 0 | 0 |

`|D₄| = 8 = 2³`, so **char 2 is the only prime dividing `|G|`**. By Maschke, `H^{>0}(D₄, A) = 0` over **F₅, F₃, and char 0**. Over the CRT factor field **F₅ that is native to `Z/10Z`, there is no nonzero cohomology at all** — the obstruction has nowhere to be a genuine class. The only characteristic with room is **2** (dividing `|D₄|`), and even there the defect (§4.1) is a coboundary.

## 5. The value-space question, made precise (probe §D)

- **Restricted (input-derived) value space.** The set-valued bracketing bundle `W(t) = {L(t), R(t)}` fails `D₄`-equivariance on exactly **16 of 67** restricted orbits — this **reproduces Theorem 4.1**. But under the **genuine** symmetry `⟨P₅₆⟩` alone: **98 orbits, 0 incoherent.** The 16 is a **pure `σ³` effect**; the genuine symmetry has no obstruction.

- **Enlarged value space (values in all of `A`).** For every restricted orbit the equivariant value must lie in `A^{Stab(base)}`, and `min_orbit dim A^{Stab} = 6 ≥ 1` over every field — so equivariant values into the full `A` **always exist**. At the sharp triple `(3,9,9)`, the stabilizer is *all of `D₄`* (both generators fix 3 and 9), so a value must lie in `A^{D₄}` (6-dimensional). That space **contains `e₃` and `e₉` — both already in the natural value set `{3,7,9}`** — and `e₄+e₇`. Only the *isolated Family-H choice* `e₇` fails to be fixed.

- **Explicit local resolution.** Replace `e₇` by its transfer average `½(e₇ + σ³·e₇) = ½(e₇+e₄)`, which is `σ³`-fixed; the correction is `½·δ`. This exists over any field where `2` is invertible (F₃, F₅, char 0). Over F₂ the average fails, but §4.1 already shows `δ` is a coboundary there too.

**Reading:** the obstruction is exactly what disappears when the value space is enlarged from the input-derived set to the full module and one averages over the group — the textbook signature of an **artifact of a restricted value space**, not a characteristic class.

## 6. Honest scope — what is genuine, and the one caveat

- **Genuine and untouched:** Theorem 4.1 as a **set-valued / combinatorial** statement ("no `D₄`-equivariant fuse valued in the input-derived *set* `{a,b,c,L,R}`") is a true impossibility theorem; nothing here refutes it. What this investigation shows is that this set-level obstruction **is not the shadow of a nonzero cohomology class** — it dissolves the moment one passes to the linear category (allow `A`-linear combinations, average over the group). "Genuine cohomological class" asks about the linear category, and there the answer is negative.
- **The task's own heuristic, reconciled (probe §E).** The suggested reading "`7 = σ³(7) = 4` ⟺ `7−4 = 3 = 0`" makes the defect *survive* mod 2 and mod 5 and *vanish* mod 3. That is the **values-as-scalars** model. But `σ³` acts on labels as the permutation `(1 5)(2 6)(4 7)` — it fixes `0` and `3` while swapping `4↔7`, which **cannot be any affine map `x ↦ ax+b`** on `k` (fixing 0 forces `b=0`; fixing 3 then forces `a=1` = identity). So the scalar reading does not define a linear `G`-action and carries **no cochain complex**; the char-3 coincidence is label numerology, not cohomology. The canonical **module** computation (§4) gives the opposite and correct verdict: the defect is a coboundary everywhere, and the *only* characteristic with any higher cohomology is 2 (dividing `|D₄|`), **not** the F₅ the heuristic suggested.
- **What would change the verdict.** A genuine class would require (a) an *associative* model in which Hochschild/Harrison is defined and the associator is a nonzero `H³` class — but `A` is not associative and the failure is not a small perturbation (86%+ associative is still not associative); or (b) a `D₄`-module structure in which `δ` is not a coboundary and `H^{>0} ≠ 0` — but the honest permutation module gives a coboundary in every characteristic. Neither exists. The route "the finite 16-orbit obstruction is a higher-operadic/(co)homological characteristic class" is therefore, on this computation, a **proven dead end**.

## 7. One-line summary

`A` is non-associative ⇒ no Hochschild/Harrison `H²,H³` exist to house a class; in the well-defined `H^*(D₄, A)` the defect `e₇−e₄ = (1−σ³)e₇` is a coboundary in every characteristic and `H^{>0}` vanishes over F₅ (Maschke); and the root cause is that `σ³` is not a magma automorphism at all (80/100 arity-2 violations) — so the obstruction is a **COBOUNDARY-ARTIFACT of the restricted value space and of a spurious symmetry demand**, resolved by `⟨P₅₆⟩` (the genuine `Z/2` symmetry) or by enlarging the value space and averaging (char ≠ 2).

---

### Reproduce

```
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe cohomology_probe.py
```

Pure `numpy`; all finite-field linear algebra by explicit Gaussian elimination mod `p` (`gf_rank`), char-0 by a large prime; the bar-cohomology engine validated against `H^*(Z/2,F₂)`, `H^*(Z/2,F₂[Z/2])`, `H^*(D₄,F₂)`, `H^*(D₄,F₃)`.
