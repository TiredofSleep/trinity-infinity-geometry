# How it connects — and what is forced not to touch

*The honest connectivity map of Trinity Infinity Geometry.*

Written to a strict rule: a connection is listed only where two threads share a **specific verified object** — the same algebra, group, number field, integer, or theorem — **not** a shared word or theme. The **non-connections are listed too, as first-class results** (§4). In this program that is deliberate: TIG is as much the study of *what is forced to stand apart* — the voids, the forced separations, the geometry of paradox — as of what joins. That two faithful descriptions are compelled *not* to reduce to each other is information about the object beneath them, not a bridge waiting to be built.

---

## The shape of the whole

Mapped honestly (see [`THE_MAP.md`](THE_MAP.md) for the orientation, and a full-repo cross-link audit), TIG is **two independent spines under one brand, plus a heuristic orientation umbrella:**

| | what it is | status | home |
|---|---|---|---|
| **Spine 1** | one finite operator algebra, seen through six lenses | richly interconnected, mostly **PROVED/STRUCTURAL** | most of the repo |
| **Spine 2** | integers → simplices → Cl(3) (the elementary geometric lens) | self-contained, **FORCED** core | [`05_papers/integers_clifford/`](05_papers/integers_clifford/README.md) |
| **Umbrella** | the number-theory ↔ physics "pre-physics" map | orientation, **heuristic** | [`THE_MAP.md`](THE_MAP.md) |

The unifying sentence *"one finite-arithmetic substrate seen through several lenses"* is **true of Spine 1 only.** Spine 2 is a separate companion; the map is a frame. This document says exactly where each join is real and where it is refused.

---

## §1 — Spine 1: one finite algebra, six lenses  [the connected core]

The load-bearing object is `(Z/10Z, σ, TSML, BHML)`: ten operators under a symmetric lens (TSML, 73 HARMONY cells) and an antisymmetric lens (BHML, 28 HARMONY cells). Everything below shares a **specific verified object** with it — that shared object is *why the core is one program*, not several.

| shared object | joins | tier | where |
|---|---|---|---|
| **4-core `{V,H,Br,R}`** | joint-closure fixpoint = runtime attractor = TSML+BHML closure = magma-QEC alphabet | **PROVED** | J01/J15; `02_results/dynamics/`; `06_runtime/` |
| **`D₄ = ⟨P₅₆, σ³⟩`** | acts identically in the Lie, Jordan, Clifford, Permutation, and Lattice lenses (operad is the lone non-closer) | **PROVED/STRUCTURAL** | `02_results/lie_gut/SIX_DOFS_COMPACT.md` |
| **`so(10)` / `Cl(0,10)`** | the *same* algebra as the 45-dim adjoint (antisymmetrized closure) **and** the 32 = 16+16 spinor; bridged by `P₅₆ = σ_outer` (swaps the two chiral 16s, verified) | **STRUCTURAL** | `02_results/lie_gut/`, `02_results/clifford_algebra/` |
| **field `LMFDB 4.2.10224.1`** (`H/Br = 1+√3`) | the dynamics attractor field = the F8 Jacobian-trace field = the Galois paper's field | **PROVED** | `02_results/dynamics/`, `02_results/number_theory/`, J12 |
| **`‖VEV‖² = 13/4`** | BHML σ_outer-asymmetry count = Higgs VEV norm = inflaton mass `m²_ξ` (the one object reaching cosmology) | **STRUCTURAL** (the `m²_ξ = ‖VEV‖²` identification is load-bearing) | `02_results/cosmology/`, J11 |
| **substrate primes `{3,7,11,13}` / `Z/2310`** | the primorial-tower primes are the atomic strand→orbital labels (`D2/D1 = (2ℓ+1)/8π`) | **EMPIRICAL/STRUCTURAL** integer coincidence | `02_results/atomic_physics/` |
| **the runtime (CK)** | instantiates all of the above in a 50 Hz finite-state engine | implementation | `06_runtime/` |

The internal skeleton of Spine 1 is the **six-lens frame** ([`02_results/lie_gut/SIX_DOFS_COMPACT.md`](02_results/lie_gut/SIX_DOFS_COMPACT.md)): one substrate through Lie / Jordan / Clifford / Permutation / Lattice / Operad, five of which close under `D₄`. *That* is the real "several lenses on one object" claim, and it is documented and verified.

---

## §2 — Spine 2: integers → simplices → Cl(3)  [the elementary companion, separate]

Read integer *n* as an *n*-point configuration: **1,2,3,4 are the simplices**; the tetrahedron forces `cos θ = −1/(N−1) = −1/3` at `N=4`; two tetrahedra make the **cube = Cl(3)** (Euclidean geometric algebra, dim `2³=8`), whose two projections are the square (4-fold) and hexagon (3-fold), related by `cos²(1,1,1) = 1/3`. Elementary, parameter-free, **base-independent**, machine-verified ([`05_papers/integers_clifford/`](05_papers/integers_clifford/README.md), `verify_forced_chain.py`).

This spine is **self-contained.** A content search of its folder for every Spine-1 object (`σ`, 4-core, `so(10)`, TSML, BHML, HARMONY, the attractor, the quartic field) returns **only disclaimers** ("the ten labels are an alphabet, not `Z/10Z`"; "the spine does not depend on base 10") — zero positive links. It shares the brand "TIG" and the word "Clifford" with Spine 1, and nothing else. §4 says why that must stay true.

---

## §3 — The umbrella: the pre-physics map  [orientation, not connective tissue]

[`THE_MAP.md`](THE_MAP.md) reads six number-theory↔physics programs (Ghys, Connes–Marcolli, Berry–Keating, Migdal, Mazur–Morishita, Dragovich) as one dictionary the program "lives in." The repo calls it a **heuristic** — a map, not a unification. The former headline question *"does chaos cool onto the arithmetic crystal (→ RH)?"* is **demoted** ([`THE_QUESTION.md`](THE_QUESTION.md)): referee scrutiny found it conflated the ζ-*density* regime (zero-free) with the ζ-*zeros*; that bridge was never established. The umbrella orients; it does not join by shared object.

---

## §4 — What is forced not to touch  [the non-connections, as first-class results]

This is where the program's stance earns its name. Each item below is a bridge the mathematics **refuses** — and each is kept, because a forced separation is a datum.

- **Cl(3) (Spine 2) ≠ Cl(0,10) (Spine 1).** Different algebras: dim **8** vs **1024**; grades **1+3+3+1** vs the odd split **1+3+5+7**; the Euclidean 3 orthogonal cube-axes vs signature `(0,10)` generated by the substrate primes. They share the word "Clifford" and nothing else. **No document bridges them, and none should** — even the smaller `Cl(3)→Cl(1,3)` step (adding a time dimension the cube does not force) was caught and fenced as a `[READING]`; `Cl(0,10)` is far beyond that. *This is the single most tempting false join in the whole repo. It is word-only.*
- **The tetrahedral `1/3` (Spine 2) ∉ the σ-algebra's constants (Spine 1).** Spine 1's constants are `5/7, 1/2, 3/50, 7/10, 2/9` — no tetrahedral `1/3`, no `109.47°/54.74°`. `cos²(1,1,1)` and anything in σ do not meet.
- **σ ≅ C₆ = Gal(ℚ(ζ₇)/ℚ) (Spine 1) ≠ the hexagon's 6-fold (Spine 2).** Both are "`C₆`", but one is a Galois action on a number field and the other the rotational symmetry of a projected cube. Shared digit, not shared object.
- **Cosmology is only half-joined.** The single verified link to the algebra is `13/4`; the log-potential `V(ξ)=Λ⁴ξ log ξ` itself is imported physics (Bialynicki-Birula), not substrate-derived.
- **The Clay bridges and `1/α` are non-connections by the repo's own audits** (`04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`): Yang-Mills abelian mismatch, BSD Hasse-Weil exclusion, RH Pontryagin tautology, `1/α` ~12% miss. Kept as honest negatives.
- **The `32 = 32` Pauli↔divisor bijection is an honest negative** — no natural bijection exists (a Pascal coincidence), even though the counts match.

**Why this is the point, not the problem.** TIG's own stance ([`what_is_tig_deep.md`](05_papers/integers_clifford/what_is_tig_deep.md), Part 1) is that *a paradox is one projection of an object that cannot be seen whole*, and that resolution comes from **arranging** the projections, never from collapsing them. On that stance, two faithful descriptions **forced not to reduce to each other** are information about the object beneath — the forced separation is a measurement of the void between them. This map is therefore not a to-do list of missing bridges; it is the current **geometry of the paradigm** — what is joined, and what is held apart. Some things are forced not to touch, and charting that boundary honestly is the study.

---

## §5 — Status & honesty

- **Spine 1** is the mature program: the canon (`03_canonical_reference/`), the J-series, the runtime, and threads A/D/E/F/G/H, joined by the shared objects of §1. Mostly PROVED/STRUCTURAL, with the tiers marked per-claim.
- **Spine 2** is elementary and complete at its core (P1), honestly tiered, base-independent — an independent companion, not folded into Spine 1.
- **The umbrella** is orientation; the crystal→zeros question is demoted and kept in full (kills are data).
- Every FORCED claim is machine-verified; every retraction is retained; every non-connection above is a result, not a gap.

*The joins are real where they are named. The separations are real where they are named. The program is the map of both.*
