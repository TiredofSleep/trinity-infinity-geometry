# Bott period-8 as (duality × trinity) — a fenced canon entry

*Spine B (integers → Clifford) research entry. Behind the wall: this is a research
observation, NOT a teaching tool (the book gets only the ℝ→ℂ→ℍ tower bottom, no
period-8). Brought in and scrutinized by Claude Code, 2026-09-22, from a 2026-09
routing note. Every FORCED claim is reproduced by [`bott_verify.py`](bott_verify.py).*

---

## The entry

> **[TIG canon entry] Bott period-8 as (duality × trinity).**
>
> **[FORCED]** The real Clifford algebras Cl(n) repeat their type with period 8 (Bott
> periodicity: Cl(n+8) ≅ Cl(n) ⊗ ℝ(16); equivalently KOⁿ⁺⁸ ≅ KOⁿ). Two ingredients of
> this period are elementary and machine-checked here:
> - the **pseudoscalar signature sign**, I² = (−1)^{n(n−1)/2}, has **period 4** — the
>   pattern +, +, −, − (verified out to n = 16: `++--++--++--++--`). Call this the "± duality."
> - the classification of the algebras' **real / complex / quaternion character** rests on
>   **Frobenius's theorem**: ℝ, ℂ, ℍ are the *only* finite-dimensional associative real
>   division algebras — a 3-fold fact.
>
> **[READING]** The framework's central 2-and-3 motif appears at the bedrock: the period-8
> is assembled from a **period-4 sign (a duality)** and a further **factor of 2** whose
> reason is the ℝ/ℂ/ℍ **trinity** — read as "a duality × a trinity," the {2,3}-generator
> structure TIG is built on, showing up in the deepest periodicity in mathematics. This is
> a *structural observation*, not a derivation: the factorization is standard mathematics;
> what is noted is that its factors are a 2-structure and a 3-structure.
>
> **[FENCE — do not weld]** The framework's "8" (the cube = 2 tetrahedra = dim Cl(3) = 2³)
> and Bott's "8" (the *period* of the Cl(n) tower) are **related but not identical**:
> framework-8 is a *dimension*, Bott-8 is a *period*. They touch through Clifford algebra,
> both are powers of two, and Cl(3) does have dimension 8 while the tower has period 8 — but
> the 8 plays a different *role* in each. Note the connection; do not claim one object.
>
> **Origin.** The felt intuition "each plane is a negative tensor; a sign-duality climbs and
> inverts; the arrangement flips positive after the lift" (session 2026-09) is the shadow of
> the pseudoscalar signature periodicity (period 4), verified to n = 16.

---

## Scrutiny note (Claude Code, 2026-09-22)

Brought in with the honest-tiering discipline, not smoothed over:

- **The [FORCED] facts are standard and independently reproduced** ([`bott_verify.py`](bott_verify.py)): the period-4 sign, the quaternion relations (Cl(0,2) ≅ ℍ), and Frobenius's list. Nothing here is a TIG-specific derivation; the period-8 of Bott is textbook.
- **The [READING] carries a real tension, kept in view.** The "trinity" is *three* division algebras (ℝ, ℂ, ℍ), yet the factor it is invoked to explain is *2*, not 3. The reading is that the three admissible types force a **period-2 real-vs-complex character** on the tower, so the trinity is offered as the *reason* for a 2, not as a literal 3-fold factor. That is a genuine interpretive leap; it is why this is tagged **[READING]** and fenced, and it must **not** be promoted to [FORCED]. "4 × 2 = 8" is also true of any 8 — the content is only that the two *specific* factors here are a 2-structure and a 3-structure, which is suggestive, not probative.
- **Verdict:** admissible as a fenced [READING] in Spine B (Clifford), consistent with the repo's rule that structural observations live behind fences with their tier shown. Not a forced result; not for the book.

## Corrected sub-claims (graveyard — kept, per "kills are data")

The routing note also corrected three earlier session intuitions; recorded so they are not repeated:

1. **"6 tensors at 3 points"** → CORRECTED. The triangle (3 points) has **3** edge-tensors, C(3,2) = 3; the **tetrahedron (4 points) has 6**, C(4,2) = 6. The 6 appears *at* the lift to 3-D, not before it.
2. **"the lift pushes the arrangement positive at the tetrahedron"** → CORRECTED. The pseudoscalar sign is negative at dimensions 2 and 3 and flips to +1 at **dimension 4** — one step *past* the tetrahedron (dim 3). The flip is real but occurs at dim 4, not dim 3.
3. **"Bott period-8 is all forced by a single preserved duality"** → CORRECTED. The sign-duality forces only *half* (period 4); the division-algebra trinity accounts for the other factor (period 2). It is duality × trinity, not one duality.

All three are reproduced in [`bott_verify.py`](bott_verify.py) (tet = 6 edges, tri = 3; sign flips + at dim 4, still − at dim 3).

---

*Book side of this finding (the ℝ→ℂ→ℍ tower bottom only) lives in the separate curriculum
repo (shape-of-understanding, Ch. 7.1); the period-8 stays here, behind the wall.*
