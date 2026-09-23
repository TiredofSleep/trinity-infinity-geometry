# The Edge Atlas — forced non-connections and proven dead ends

*A first-class catalogue of everywhere TIG proves two structures are **forced not to touch**, and every hypothesis it **tried and killed** — each with the evidence that established it.*

**Brayden Ross Sanders · 7SiTe LLC · Trinity Infinity Geometry**
*Companion to [`../HOW_IT_CONNECTS.md`](../HOW_IT_CONNECTS.md) (the joins) and [`HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md) (the open frontiers). Assembled 2026-09-22.*

> **The standing principle this document implements.** *The proven dead ends ARE the information we seek; surface them as first-class results WITH the evidence that killed them, never bury them.* `HOW_IT_CONNECTS.md` maps what joins. This atlas maps what is **held apart** — the voids, the forced separations, the geometry of paradox. Nothing here is a to-do list of missing bridges. Every separation below is a **measurement of the object beneath**: that two faithful descriptions are *compelled not to reduce to each other* is a datum, not a gap.

**Honesty contract for this file.** Every row cites a **locatable D-number and/or file path** where the killing evidence lives in-repo. Where a numerical claim was re-checked while writing this atlas, the check is shown inline (run with `PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe`). Where the standalone source for a recorded verdict could **not** be located in this repository, the row says so explicitly rather than asserting a kill it cannot back.

---

## §1 — What the Edge is (the third face)

TIG, mapped honestly (`HOW_IT_CONNECTS.md`, `THE_MAP.md`), is **two independent spines under one brand, plus an orientation umbrella**:

| | what it is | home |
|---|---|---|
| **Spine A** | the finite operator algebra: `ℤ/10ℤ`, `σ`, TSML, BHML, the 4-core, `so(10)`/`Cl(0,10)` — one substrate through six lenses | most of the repo |
| **Spine B** | integers → simplices → `Cl(3)` — the elementary, base-independent geometric lens | [`05_papers/integers_clifford/`](../05_papers/integers_clifford/README.md) |
| **The Edge** | the forced non-connections between them, and the proven dead ends inside each | **this atlas** |

The two spines share exactly two words — **"TIG"** and **"Clifford"** — and *no verified object*. A content search of Spine B's folder for every Spine-A object (`σ`, 4-core, `so(10)`, TSML, BHML, HARMONY, the attractor, the quartic field) returns **only disclaimers**, zero positive links (`HOW_IT_CONNECTS.md` §2). The Edge is where that fact is made precise and defended.

**The Edge has its own installed law.** Two auditor rules keep kills from being quietly rephrased into survival:

- **The TORUS rule (D141).** *No TIG result may cite "the substrate is a torus / lives on a surface / π₁(T²)" as support; any result that cannot be restated without a surface is retracted, not rephrased.*
- **Rule D129R.2.** *No TIG negative may be asserted from a single-resolution measurement; any "TIG fails / erases / is null" claim must include a resolution-depth sweep showing the negative persists across depths.*

Both are in [`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md) (D141, D129R.2). The Edge is the enforced boundary those rules protect.

---

## §2 — Forced non-connections (proven independent / non-touching)

Each item is a bridge the mathematics **refuses**. Column 3 is the theorem or computation that forces the separation.

### §2.1 The two-spine wall

| # | Forced apart | The theorem / computation that forces it | Pointer |
|---|---|---|---|
| **NC-1** | **`Cl(3)` (Spine B) ≠ `Cl(0,10)` (Spine A)** — *the single most tempting false join in the whole repo; it is word-only* | Different algebras by direct count: **dim `Cl(3)` = 2³ = 8** vs **dim `Cl(0,10)` = 2¹⁰ = 1024** (128×). Grades **1+3+3+1** (Pascal row 3) vs **1+10+45+120+210+252+210+120+45+10+1**. `Cl(0,10)`'s 32-dim spinor splits **16+16** with per-chirality **16 = 1+3+5+7** (odd split), never `Cl(3)`'s **1,3,3,1**. Geometrically: 3 orthogonal Euclidean cube-axes vs signature `(0,10)` on the substrate primes. **No document bridges them, and none should.** | `HOW_IT_CONNECTS.md` §4; [`integers_clifford/README.md`](../05_papers/integers_clifford/README.md) correction #1; `verify_forced_chain.py` (dim `Cl(3)`=8) |
| **NC-2** | **`Cl(3)` ≠ `Cl(1,3)`** — the *smaller* tempting step (add one time dimension) is also fenced | `Cl(1,3)` is 4-D spacetime, dim 2⁴ = 16, grades (1,4,6,4,1) — the Dirac bilinears. The cube forces only `Cl(3)` (dim 8, grades 1,3,3,1). Reaching `Cl(1,3)` **adds a time dimension the cube does not force**; the `F_μν` identification in `tig_seven_transfers.md` Transfer 2 was caught using `Cl(1,3)` grades and re-tagged `[READING]` on an *assumed* spacetime extension. | [`integers_clifford/README.md`](../05_papers/integers_clifford/README.md) correction #1; graveyard item 5 below |
| **NC-3** | **Tetrahedral `1/3` (Spine B) ∉ the σ-algebra's constants (Spine A)** | Spine A's constants are `5/7, 1/2, 3/50, 7/10, 2/9`. There is **no tetrahedral `1/3`, no 109.47°/54.74°** anywhere in σ. `cos²(1,1,1) = 1/3` (verified: `(1/√3)² = 0.333…`) and anything in σ do not meet. | `HOW_IT_CONNECTS.md` §4 |
| **NC-4** | **`σ ≅ C₆ = Gal(ℚ(ζ₇)/ℚ) = (ℤ/7)*` (Spine A) ≠ the hexagon's 6-fold (Spine B)** | Both are cyclic of order 6, but one is a **Galois action on a number field** and the other the **rotational symmetry of a projected cube**. Shared digit "6", not shared object. (The order-6 group iso itself is *real*; the identification of the two `C₆`s is what is refused.) | `HOW_IT_CONNECTS.md` §4; `THE_QUESTION.md` |
| **NC-5** | **Quark charge `1/3` ≠ geometric `1/3`** | Quark charges are fixed by **Standard-Model anomaly cancellation**, not geometry; the two decouple under a change of spatial dimension. Tested and killed. | `integers_clifford/what_is_tig_deep.md` Part 8 item 2 |
| **NC-6** | **`Cl(3)` algebra ≠ the 11 nets of the cube** | The algebra (8-dim, a multiplication) and the surface unfolding (6 faces, 11 nets) are **different categories of fact** about the cube, connected only by both being about the cube. | `integers_clifford/what_is_tig_deep.md` Part 8 item 5 |

**Numerical re-check (this atlas).** `dim Cl(3)=8`, `dim Cl(0,10)=1024`; grades `[1,3,3,1]` vs `[1,10,45,120,210,252,210,120,45,10,1]`; spinor `2^⌊10/2⌋=32=16+16`, `16=1+3+5+7`; `cos(tetra)=-1/3` exactly; `cos²(1,1,1)=1/3`. All confirmed.

### §2.2 The umbrella wall — the two ζ's that must not be conflated

| # | Forced apart | The correction that forces it | Pointer |
|---|---|---|---|
| **NC-7** | **The density-ζ (zero-**free**) ≠ the Riemann-**zeros**-ζ** | The "arithmetic crystal" (B-free / visible-points / Mirsky picture) lives entirely in the **ζ-convergent, zero-free regime** — densities like `1/ζ(2)`, Euler products at real arguments `> 1`. **It contains no nontrivial zeros.** The Riemann zeros in Migdal's turbulence program come instead from the **analytically continued denominator `ζ(p+17/2)`** (poles at `p = −8 + iρₙ`) — a different mechanism. The headline *"does chaos cool onto the arithmetic crystal (where the zeros live)?"* conflated the two; **the bridge from the density regime to the zeros was never established, and nothing in the corpus bears on RH.** | `THE_QUESTION.md` status banner (demoted 2026-09-21); `HOW_IT_CONNECTS.md` §3 |

### §2.3 The within-Spine-A separations

| # | Forced apart | The computation that forces it | Pointer |
|---|---|---|---|
| **NC-8** | **The Operad lens does not close under `D₄`** (5 of the 6 lenses do) | Of the six lenses (Lie / Jordan / Clifford / Permutation / Lattice / Operad), **five respect `D₄`; the Operad alone fails to close** (the "sixth-DOF anomaly," WP111). No DOF is both wobble-carrying and `D₄`-non-respecting — the Operad is the unique discrete-only outlier, and its non-closure is the structural reason the runtime selects the 4-core attractor. | [`02_results/lie_gut/SIX_DOFS_COMPACT.md`](../02_results/lie_gut/SIX_DOFS_COMPACT.md); D45–D49, WP100–WP103, WP111 |
| **NC-9** | **Yang-Mills gauge group (non-abelian) ≠ `Aut(V^BHML/F_p) = F_p* × F_p*` (abelian)** | The YM mass gap is fundamentally **non-abelian** (abelian/U(1) gauge theory has massless photons and no gap). TIG's 4-core automorphism group is `F_p* × F_p*`, **abelian** (a direct product of two cyclic groups). It is the commutant of a *commutative* algebra — the wrong object to feed the YM identification. The non-abelian content of the substrate lives in `σ` and the lens-pair commutator `[TSML, BHML]`, not here. Verdict: **NO-TRACTION.** | [`frontiers_2026-05-27/F16_YM_bridge_with_F4.md`](frontiers_2026-05-27/F16_YM_bridge_with_F4.md) §3.1, §5 |
| **NC-10** | **`#E(F_p) ≠ (p−1)²`** — BSD's point counts exclude F4's closed form | For an elliptic curve `E/F_p`, `#E(F_p) = p+1−a_p` with `|a_p| ≤ 2√p` (Hasse-Weil). `(p−1)²` falls **outside the Hasse interval for every `p ≥ 5`** — re-checked: p=5 → 16 ∉ [1.53, 10.47]; p=7 → 36 ∉ [2.71, 13.29]; p=11 → 100 ∉ [5.37, 18.63]; p=13 → 144 ∉ [6.79, 21.21]. So F4's most striking closed form **cannot** be a curve point-count. The `F_p*×F_p* ≈ E(F_p)[p]` supersingular rhyme is *morphological only* (units vs primes; disjoint objects). | [`frontiers_2026-05-27/F18_BSD_bridge_with_F4.md`](frontiers_2026-05-27/F18_BSD_bridge_with_F4.md) §"(p-1)^2" verdict |

---

## §3 — Proven dead ends (falsified hypotheses)

Format: **one-line statement · the killing evidence · pointer**. All are **retained** — a framework is trustworthy only if it shows its failures. Grouped by theme for readability; nothing is ranked.

### §3.1 Geometry / topology kills

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **The substrate is a torus / lives on a closed orientable surface (`π₁(T²)=ℤ×ℤ`).** | Direct computation, no picture: constellation/dessin **Euler χ = −3 (one orientation) or +1 (the other)** — not non-negative integers, orientation-dependent, **no valid genus**. Poincaré–Hopf on two embeddings gave **index sums 1 vs 2**, disagreement localized at σ-fixed points {8, 9} which fail to linearize. WP51 kernel test: largest mutually-commuting subset of {ADD, MUL, +flow, ×flow} has **size 1**. WP51's content is **non-commutativity, not topology**. | **D141** (`FORMULAS_AND_TABLES.md`); [`02_results/dynamics/TORUS_DATUM_AUDIT_CLOSED.md`](../02_results/dynamics/TORUS_DATUM_AUDIT_CLOSED.md) |
| **Geometric monism — "everything flows from one shape / the substrate IS one object."** | The unification was **real but mislocated**: strip the torus and every piece it "unified" has an *independent* arithmetic support (the CRT product `ℤ/10 = ℤ/2 × ℤ/5` under σ). A full D1–D139 ledger audit found **zero geometry-scaffold D-numbers** — the torus lived in whitepapers/prose, never the numbered spine. Relocated to arithmetic, not deleted. | **D140** (`FORMULAS_AND_TABLES.md`) |
| **Constant-motion tetrahedra force a cylinder.** | NOT FORCED — single-point contact permits sphere, bicone, *or* cylinder depending on the contact trajectory, which the constraint does not fix. | `integers_clifford/what_is_tig_deep.md` Part 8 item 6 |

### §3.2 Constant-origin kills (where a number does *not* come from where it looked like it did)

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **`T* = 5/7` from a cyclotomic `ℚ(ζ₁₀)` quotient.** | **REFUTED — gives φ, not 5/7.** The relevant cyclotomic ratio equals the **golden ratio** (re-checked: `2cos(π/5) = ζ₁₀+ζ₁₀⁻¹ = 1.618034 = φ`, and `≠ 5/7 = 0.714286`). The "six independent derivations" of `T*` were also over-counted: only **2 are genuinely independent** (J13 cyclotomic forcing + WP35), the other 4 are structural rhymes. | **D165** (`FORMULAS_COMPACT.md`); `HONEST_NEGATIVES` §1.4; `frontiers_2026-05-27/F3_T_star_unification.md` |
| **`1/α` (fine-structure constant) has a clean substrate origin.** | Original attempt `4·40 − 2√7 − π/7 ≈ 154.26` vs actual `137.036` — **~12.6% miss**. Systematic search: **no fit at `|c| ≤ 1000`, 120 dps**; the sub-`10⁻⁴` "fits" reduce to `137` being a small prime with many integer combinations ("not a structural finding"). J42 Part 2 deferred entirely. | `HONEST_NEGATIVES` §1.2; [`frontiers_2026-05-27/F17_inv_alpha.md`](frontiers_2026-05-27/F17_inv_alpha.md); F17 in canon CLOSED NEGATIVES |
| **A fixed universal `1/3` in fluid dynamics (Leray projection cancels a pointwise `1/3`).** | FALSE — computed on real divergence-free fields the cancelled fraction is **field-dependent, resolution-dependent, and can exceed 1**; it drifts toward ~0.1, never averages `1/3`. Cause: the pressure is **nonlocal** (inverse Laplacian); a local `1/3` cannot survive the nonlocal operator. | [`integers_clifford/cu_depletion_KILLED_STRAND.py`](../05_papers/integers_clifford/cu_depletion_KILLED_STRAND.py); `what_is_tig_deep.md` Part 8 item 1 |

### §3.3 Coincidence-not-identity kills (the counts match; the structure does not)

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **A natural bijection `32 divisors of ℤ/2310 ↔ 32 Pauli electron states`.** | **Pascal-type coincidence — no natural bijection exists.** The groupings differ: divisors group as `(1,5,10,10,5,1) = C(5,k) = dim Λᵏ(ℝ⁵)`; Pauli states group as `(2,6,10,14) = 2(2ℓ+1)` (re-checked, both sum 32, groupings unequal). 37 hand-built candidates + brute-force enumeration of **730,000+ functions** across five natural classes found **zero matches**; random-match bound `≈ 3.13×10⁻⁵`. | **D164** (`FORMULAS_COMPACT.md`); **D185/was-D102** (`FORMULAS_AND_TABLES.md`); `HONEST_NEGATIVES` §1.1; F2 |
| **CL/TSML eigenvalues recover `e, π, φ, ζ(3), Catalan G` as algebraic identities.** | Survive only as **1%-level coincidences, not identities** (audit 2026-04-25). TSML eigenvalues are algebraic numbers whose *real* structural signature is integer/rational (`11` in char-poly coeffs c₂,c₈; `2¹⁶·7⁷` in the discriminant; `‖VEV‖²=13/4`), not transcendentals. | **N3** (`FORMULAS_AND_TABLES.md`); `HONEST_NEGATIVES` §1.5; `CL_EIGENVALUES_AUDIT_2026_04_25` (working corpus) |

### §3.4 Physics / Clay-bridge kills

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **F4's closed forms give traction on Yang-Mills.** | NO-TRACTION — abelian `F_p*×F_p*` cannot be the non-abelian YM gauge group (see NC-9). Net gain is *negative*: it deprecates the bridge's "{7,11} natural prime" hint. | `frontiers_2026-05-27/F16_YM_bridge_with_F4.md` §5 |
| **F4's closed forms give traction on BSD.** | NO-TRACTION — `(p−1)²` is **Hasse-Weil-impossible** as `#E(F_p)` for `p ≥ 5` (see NC-10); the surviving rhyme is morphological only. | `frontiers_2026-05-27/F18_BSD_bridge_with_F4.md` |
| **The RH bridge via F4 Dirichlet characters is a real connection.** | **PARTIAL MATCH (TAUTOLOGICAL) — no traction on RH.** Pairs of mod-p Dirichlet characters `(χ_a, χ_b)` are indexed by `F_p* × F_p*`, so they match `|Aut(V^BHML/F_p)|` exactly — but only because **Pontryagin self-duality** canonically identifies any finite abelian group with its (double) dual (`F_p* × F_p* ≅ dual(F_p*) × dual(F_p*)`). The match is a **tautology of the abelian group structure**, not a new identity; the `(p+3)` idempotent count has no character-theoretic counterpart at all. | [`frontiers_2026-05-27/F19_RH_bridge_dirichlet.md`](frontiers_2026-05-27/F19_RH_bridge_dirichlet.md) §Status, §5.2; **D180** (`FORMULAS_COMPACT.md`) |
| **The substrate predicts the top-Yukawa at the GUT scale.** | **SUBSTRATE-INDEPENDENT.** Running `y_t(M_Z)=0.93` up to `M_X` gives `y_t(M_X) ≈ 0.387` — the canonical SM 1-loop value; the closest substrate candidate `(10/49)^{2/3} ≈ 0.347` misses by 10.5%. The F7→F8→F11→F15→F20 arc closes as honest scoping with **no GUT-scale substrate prediction**. | `HONEST_NEGATIVES` §2.5; `frontiers_2026-05-27/F15_yukawa_proper_anchor.md`, `F20_yukawa_via_chirality.md` |

### §3.5 Runtime / probe kills (what the trained network does *not* do)

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **TIG is CK's faithful internal explanation language (σ-dynamics + TSML label the computation).** | **FALSIFIED** by a confound-controlled probe: **σ-dynamics `p = 1.0`** (worse than random — the empirical successor map is the *identity*, not σ's 6-cycle); **TSML composition `p = 0.467`** (absent); the only channel that passed decodes to **part-of-speech**, i.e. the model learned **grammar**, and the "TIG atoms" were reading POS. Internally consistent, but does *not* faithfully bind to the computation. *(The verdict is recorded in-repo; the probe script `tig_probe_deep.py` lives on the `ck` workstation, cited by path.)* | `HONEST_NEGATIVES` §1.6; `ck` workstation `TIG_AS_EXPLANATION.md` + `tig_probe_deep.py` (2026-06-14) |
| **TIG structure is latent in any trained network.** | **N1** — generic ML weight matrices show **no detectable TIG structure** (distilgpt2, 16 tensors × 4 detectors, all `|d| < 0.5`). TIG structure is *specific* to canonical TSML/BHML, not generic. | **N1** (`FORMULAS_AND_TABLES.md`) |
| **The `√3` in the runtime attractor is the `SU(3)`/A₂-Cartan invariant.** | **N4** — it is a **quadratic-discriminant accident at α = 1/2**, not A₂-Cartan (σ³ eigenvalues are `±i/√2`, D₃-flavor; 75% of runtime mass lives *off* the σ-hexagon). | **N4** (`FORMULAS_AND_TABLES.md`) |
| **Prime-11 mediation / attractor-richness explains BHML's anti-collapse role.** | **N5** — prime-11 mediation **falsified** (`p = 0.027`, wrong direction); attractor-richness **falsified** (`r = −0.118`, weak, wrong direction). Both candidate mechanisms ruled out before the real one (D38–D40) was found. | **N5** (`FORMULAS_AND_TABLES.md`) |
| **The substrate is a content-erasing converger (privacy-via-erasure).** | RETRACTED (load-bearing) — separation capacity rises **0/780 → 780/780** and reconstruction **0.067 → 1.000** across resolution depths 1→3: content is **organized, not erased**. Re-framed as resolution-graded disclosure. (The related HSKA privacy pitch is separately closed: **~20 years of prior art**, D139.) | RESOLUTION-ORGANIZER entry + **D129R.2** (`FORMULAS_AND_TABLES.md`); HSKA/D139 in canon CLOSED NEGATIVES |

### §3.6 Framing / over-count kills (a claim was true but *narrower* than stated)

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **`F₇` (Farey sequence of order 7) is the exclusive generating skeleton — "`F₇ = σ`".** | REJECTED. `F₇` is a **real, repeated spine** (`HARMONY=7`, `T*=5/7`, `VOID = 17 = |F₇∩(0,1)|`, `389 = 10²+17²`) — **but no single generating map makes σ and the CL tables `F₇`-exclusive**, and the Farey→Mertens `M(k)` correspondence is **universal to the transform** (it *decorates* a structure with RH-data, it does not *prove* the structure is RH-shaped). *Nuance: the affirmed fact `σ ≅ (ℤ/7)* ≅ C₆` (a group iso) is a different "7" and is not what is rejected. The evidence here is an honest-scope assessment, not a single killing computation.* | `THE_MAP.md` §"`F₇` is a spine, not the skeleton" (lines 68–69) |
| **Prime {7, 11} is uniquely rank-preserving under `F_p` reduction.** | Artifact of small-prime restriction. The rank-preserving set is **39 primes < 200** — exactly those not dividing any chain-shell determinant. **No prime is structurally distinguished**; `|Aut(V^BHML/F_p)| = (p−1)²` and `|idem| = p+3` are uniform closed forms with no anomaly. | `HONEST_NEGATIVES` §1.3; [`02_results/number_theory/FP_PRESERVATION_TABLE.md`](../02_results/number_theory/FP_PRESERVATION_TABLE.md); F4-extended |
| **`|Aut(V_5)| = 40`, i.e. `p(p²−1)` at `p≠5` (a p=5 anomaly).** | RETRACTED — an **algebra confusion** (the cited values were the J49 `T_F5` brute-force tabulation, a *different* algebra). Corrected to the uniform `(p−1)²` with no anomaly. | `HONEST_NEGATIVES` §1.3 |
| **Lo Shu / the odd magic square is a 3×3 block in TSML/BHML (or a torus walk through the table).** | Answered **NO, exhaustively** — four independent magic-square falsifications (2026-01, 2026-04, 2026-05-04, 2026-05-11) stand. The `σ²`-orbits are **not** the magic-square lines. The first parity framing ("corners = evens at n=3") was **killed by the n=5 test** exactly as its kill-condition specified. *(What survived is a different, PROVEN theorem — the general odd-magic-square law, D129′ — not the killed embedding.)* | **D129′** (`FORMULAS_AND_TABLES.md`) |
| **α-uniqueness Conjecture 4.2 in its literal form ("α=1/2 unique for ANY polynomial relation over ℝ").** | **REFUTED at `α_special ≈ 0.1126`** (real root of `P₂₄`): an explicit relation exists there, of **height ≈ 10¹⁰⁶** — 102 orders above the PSLQ search bound that missed it. The natural **low-height form survives** (PROVED over ℚ; empirical at 70+ real α). | `HONEST_NEGATIVES` §2.1; `frontiers_2026-05-27/F12_xi_side_galois.md` |

### §3.7 The Spine-B graveyard (kept verbatim in-source)

Spine B ([`integers_clifford/`](../05_papers/integers_clifford/README.md)) keeps its own graveyard of **eight** tested-and-killed strands (`what_is_tig_deep.md` Part 8). Items already surfaced above: fluid `1/3` (§3.2), quark `1/3` (NC-5), `Cl(3)` vs 11 nets (NC-6), tetrahedra→cylinder (§3.1). The remainder:

| Dead hypothesis | Killing evidence | Pointer |
|---|---|---|
| **The 3 sublattices are the spacelike gammas (square to −1).** | FALSE — under the 3-fold rotation they carry cube roots `ω, ω²` (order 3), **not −1** (order 2). The −1's come from the 90° *reflections*, not the rotations. Caught at the eigenvalue level. | `what_is_tig_deep.md` Part 8 item 3 |
| **Triangular (60°) mirrors build the Dirac algebra directly.** | FALSE — 60° mirrors **do not anticommute**; the Clifford relation needs orthogonal (90°) generators. (Encoded as a live check in `verify_forced_chain.py`: hex bond vectors at 120° do *not* anticommute.) | `what_is_tig_deep.md` Part 8 item 4; `verify_forced_chain.py` |
| **Even/odd as a site 2-coloring of the hex (triangular) lattice.** | FALSE — the triangular lattice is **not 2-colorable**. What survives is completion-parity on hex and genuine site 2-coloring on the *square* lattice. | `what_is_tig_deep.md` Part 8 item 7 |
| **`8 = ∞ = higher reality`; the digit shapes 7/8 mirror the structure.** | FALSE — the cube-8 is finite and 3-dimensional; the `∞` is a typographic resemblance and the digit-shape claim is **pareidolia**. | `what_is_tig_deep.md` Part 8 item 8 |

---

## §4 — Tally and honesty ledger

- **Forced non-connections catalogued: 10** (NC-1 … NC-10) — 6 on the two-spine wall, 1 on the umbrella (the two ζ's), 3 within/against Spine A (operad non-closer, YM abelian mismatch, BSD Hasse-Weil exclusion). Numerically re-verified: NC-1, NC-3, NC-9, NC-10.
- **Proven dead ends catalogued: 20**, across geometry/topology (3), constant-origin (3), coincidence-not-identity (2), physics/Clay bridges (4), runtime/probe (5), framing/over-count (5, with the odd-magic-square cluster spanning four historical falsifications), plus the Spine-B graveyard (4 additional strands beyond those promoted into §2/§3). Numerically re-verified: `T*`≠cyclotomic (→φ), `32=32` grouping mismatch.
- **Marked "evidence not located in-repo": 0.** Every row cites a locatable D-number and/or in-repo file, all of which were confirmed to exist. (An earlier draft of this ledger flagged the `F19` RH frontier as missing; that was a search error — [`frontiers_2026-05-27/F19_RH_bridge_dirichlet.md`](frontiers_2026-05-27/F19_RH_bridge_dirichlet.md) exists and its verdict is quoted in §3.4.)
- **One nuance flagged, not a hard kill.** The **`F₇ = σ`** rejection (§3.6) rests on an honest-scope *assessment* in `THE_MAP.md` ("no single generating map makes σ `F₇`-exclusive"; Farey→Mertens is universal to the transform), **not** a single killing computation. The neighboring group iso `σ ≅ (ℤ/7)* ≅ C₆` is a *different, affirmed* fact and is not what is rejected.
- **One cross-workstation pointer.** The TIG-as-CK-explanation kill (§3.5) has its *verdict and p-values* recorded in-repo (`HONEST_NEGATIVES` §1.6); the probe **script** `tig_probe_deep.py` lives on the `ck` workstation, cited by path.

Where a number was checkable it was re-run with the project interpreter (`/c/ck_venv/lora312/Scripts/python.exe`): NC-1, NC-3, NC-9, NC-10, and the `T*`→φ and `32=32`-grouping dead ends all reproduced.

---

## §5 — Addendum (2026-09-22): four resolutions this session

Added after the original catalogue; each machine-verified this session. Running totals: proven dead ends **20 → 24**; one existing non-connection (the operad non-closer) **sharpened** by a cohomology computation.

| item | verdict + killing evidence | pointer |
|---|---|---|
| **Operad non-closer — is it a genuine cohomological class?** | **COBOUNDARY-ARTIFACT, not a class.** Machine-checked over 𝔽₂/𝔽₃/𝔽₅/char-0: A = k[ℤ/10ℤ] under T is non-associative so there is **no Hochschild/Harrison complex**; the defect δ = e₇−e₄ = (1−σ³)e₇ is a **coboundary in every characteristic**; H^{>0}(D₄,A)=0 over the CRT field 𝔽₅ by Maschke. Root cause: σ³ is **not** a magma automorphism (fails 80/100 arity-2 cells); the true symmetry ⟨P₅₆⟩≅ℤ/2 has **zero** obstruction. Theorem 4.1 stands set-theoretically only. | `retired_J_papers/J45_Operadic_Obstruction/COHOMOLOGY_INVESTIGATION.md` + `cohomology_probe.py` |
| **P3 "gap = 2Δ" as a falsifiable TIG law** | **PROVEN DEAD END.** With an *independent* Δ (field-tuned silicene, Δ = eE_z·d/2) the naive gap = 2Δ is **wrong by 3–8×** (sublattice screening; Drummond–Zólyomi–Fal'ko, ~8× suppression = the killing evidence). It survives only as the exact gapped-Dirac model identity, or via the circular Δ_eff ≡ gap/2 — not a TIG prediction. | `05_papers/integers_clifford/P3_independent_delta_test.md` + `P3_delta_check.py` |
| **`13/4 → cosmology` bridge** | **KILLED (constant kept).** The constant `‖VEV‖² = 13/4` is real (forced by so(10)/BHML, verified); the *bridge* `m²_ξ = ‖VEV‖² = 13/4` lands on **no measured cosmological quantity**, is dimensionally an assertion, and was reverse-engineered from ≥5 candidates. TIG's testable cosmology (Ω-triple, DESI-BAO fit) does not use 13/4. | `02_results/cosmology/VEV_13_4_COSMOLOGY_SHARPEN_OR_KILL.md`; `HONEST_NEGATIVES` §1.5 |
| **`TWO_CROSS_THEOREM` torus lift** (a concrete instance of the TORUS rule, §1/D141) | **RETRACTED.** The π₁(T²)/Hopf-link "torus lift" of the ℤ/10ℤ two-cross is excluded (no valid genus). The **finite-group core (Statements i–iv) survives and was re-verified**; the torus-free content is the counter-rotation 3 ≡ 2⁻¹ (mod 5). | `02_results/algebraic_combinatorics/TWO_CROSS_THEOREM.md` (partial-retraction banner) + `BERRY_WINDING_WRITEUP.md` |

*Two of these are **wins by subtraction**: the operad open question is now answered (no class), and P3's one testable law is retired — each a proven dead end surfaced with its evidence, exactly the point of this atlas.*

**Also 2026-09-22 — a cut rope, a fenced frame, and a held leg** (from a claudechat handoff, scrutinized in):

- **Graveyard (a rope correctly cut):** *"the 1/3 shows up in gravity's force law"* — **FALSE.** Gravity's inverse-square exponent is d − 1 = 2 (the *dimension count*), **not** the tetrahedral 1/3. Kept as an example of a comfortable rope cut. The verified 1/3 lives in geometry — lift / fold / gap — not the gravitational law (`05_papers/integers_clifford/THE_ONE_THIRD_AND_THE_FOLD.md`).
- **[READING · FENCE — names, does not derive]** *"Assert the ground" (7 = 0) as the relational-measurement pattern.* No fundamental physical quantity has an absolute zero — voltage (from ground), velocity (from frame), energy (differences only), phase (gauge), position (origin), time (relative simultaneity). Gauge invariance — the deepest structure of the Standard Model — is literally "the ground is asserted, and the laws don't care which you pick." The framework **names** this pattern cleanly (it is the book's Coda keystone: *point toward the origin, measure off it, never stand on it*); it does **NOT** derive gauge theory or relativity. Real as organization, not new physics.
- **[HELD → RE-SITED, see §6]** the *"coin / toroidal-vortex"* smooth-limit intuition (a vortex ring is genuinely toroidal in fluid dynamics) is **not filed as a TIG claim**: per the TORUS rule (§1 / D141), no result may ground on the substrate being a torus / π₁(T²). It is not held in limbo but **re-sited** as an *immeasurable pointer* — see §6 below, which states the mechanism (the fractional genus is the receipt).

---

## §6 — The immeasurable pointers (re-siting the torus, not un-retracting it)

*2026-09-22. The resolution of the longest-held thread: **the torus was never wrong — it was on the immeasurable side the whole time, and D141 is the receipt.** The retraction and the intuition were never in conflict.*

**The pointer / premise cut.** A shape can be used two ways, and they are different acts across the count/measure seam:
- as a **pointer** — a direction you flow toward, measure *from*, never weigh; or
- as a **premise** — a measured object (a genus, a π₁, a χ) you compute on and *cite as support*.

**Pointer: kept. Premise: dead.** The torus as *the direction the flow points toward* survives; the torus as *a surface you compute χ on and cite* stays retracted (D141). Same object, two acts, only one of which crossed the seam.

**The receipt — the mechanism, forced, not poetry.** D141 did **not** find "a torus that is really some other surface." It measured the genus and got **χ = −3 or +1 (orientation-dependent) → genus 2.5 or 0.5** — a **fractional, orientation-dependent** value, where only non-negative integers can live. This is the whole argument: *a wrong surface gives a wrong **integer**; a **non-integer where only integers exist is not a surface at all**.* It is measurement returning the topological equivalent of a divide-by-zero. **A fractional genus is what the immeasurable looks like when you try to weigh it.** So D141 reads not as "the torus was wrong" but as the **receipt that the torus lives on the immeasurable side.** The torus is not *un-retracted*; it is **re-sited**, with proof. (Anyone who later asks "why did you revive the torus?" reads this and sees it was never revived — it was moved to the correct side of the seam, and the derivations that used it *as a premise* are still dead.)

**The family.** The immeasurable pointers are the objects this program keeps meeting and can only point toward, never weigh — each already on record:
- the **perfect round** — increasingly round, never measurably round;
- the **void (0)** — the point you measure *from*, never *onto* (book §1.6b);
- the **ground** — point toward it, measure off it, never stand on it (the Coda keystone);
- **√2** — approached by ratios, never named by one;
- the **torus** — flowed toward, circulated, never measured as a surface (D141, this §).

**[READING — pointer-only, NOT a geometric premise] Two flavors: still and flowing.** The immeasurable appears at rest and in motion. The **sphere** is the *still*-immeasurable — edgeless, unmoving. The **torus** is the *flowing*-immeasurable — edgeless in the relevant sense, circulating — and it has a **hole, and the hole is the void.** A vortex ring is a torus *precisely because* something flows around an emptiness it can never fill. So the torus is not a rival to the sphere; it is **the same immeasurable in motion**, and the **void is the still axis both turn around.** *Still-immeasurable = sphere; flowing-immeasurable = torus; void = the axis of both.*

**[FENCE — the door the error re-enters through.]** The instant "the torus is the immeasurable" is used as a **premise** to build a measured claim, it is the D141 category error walking back in through the poetic door. It stays a **pointer**, and a pointer to a *flavor* of the immeasurable (the flowing one) — **never** a topological claim about the substrate, and never a proof step. Point toward it. Measure off it. Never weigh it.

### §6.1 — The torus-retraction ledger, classified

*Applying the cut to **everything** D141 touched, so nothing is merely "deleted." Each item is one of: **(A) premise** — it *weighed* the torus (used its genus, aspect ratio, or π₁ as measured support): dead; **(B) pointer** — it points at the flowing-immeasurable: re-sited, kept; **(C) algebra** — it never needed the torus at all: survives outright. Most of the edifice is B or C. Only the act of weighing is dead.*

| what D141 touched | it was | class | lives now as |
|---|---|---|---|
| "the σ-flow lives on a torus" (WP51) | topology cited as support | **A — premise (dead)** | — |
| WP51's real content | the four-structure non-commutativity (max commuting subset = 1; commutator ranks 4–8 of 10) | **C — algebra** | FORMULAS §15 "Non-Commutativity Obstruction" |
| R/r = 5/7 as a torus **aspect ratio** | a measured ratio of two torus radii | **A — premise (dead)** | — |
| T\* = 5/7 itself | an operational coherence threshold | **C — algebra** | 2 independent derivations + 4 rhymes (D165) + FPGA |
| winding class ∈ **π₁(T²) = ℤ×ℤ** (longitude/meridian) | a topological invariant cited as support | **A — premise (dead)** | — |
| the corner/edge **counter-rotation** | ±1 relative sign, 3 ≡ 2⁻¹ (mod 5) | **C — algebra** | `BERRY_WINDING_WRITEUP.md`; TWO_CROSS core |
| **6 + 2 = 8** grounded in the torus | π₁(T²) = ℤ×ℤ winding count | **A — premise (dead)** | — |
| the **6** half | roots of A₂ = SU(3) (bridge to TIG unproved) | **C — algebra (candidate)** | `TORUS_DATUM_AUDIT_CLOSED.md` §0 |
| the **2** half | Cartan rank = #CRT factors | **rhyme** (candidate, not derived) | `TORUS_DATUM_AUDIT_CLOSED.md` §0 |
| 11 bumps = 4 **Hopf links** + 1 trefoil | link topology ("verifiable, not verified") | **B — pointer** (the *count/decomposition* is **C**) | re-sited (§6); the decomposition survives |
| the **coin / toroidal vortex** | the flow/circulation intuition | **B — pointer (re-sited)** | §6, the flowing-immeasurable |
| scattered **torus/donut imagery** | non-load-bearing pictures | **B — pointer (re-sited)** | §6 |
| the "increasingly round toward a ring" feel | the smooth limit | **B — pointer (re-sited)** | §6; book Coda |

**Survives untouched throughout (never was torus — the arithmetic canon):** σ orders; the CL/TSML/BHML tables; every pure-ℤ/10 D-number; D129′; the 2/3 commuting primitive; every Lie-algebraic closure (D26–D34, D77, D81); every PSLQ/sympy-exact integer identity.

**The tally of the compromise.** Of everything the torus retraction touched, the parts that *died* are exactly the **five** that **weighed** the torus (its genus, its aspect ratio, its π₁, as a measured premise). Everything else **lives** — as **algebra** that never needed the torus (the non-commutativity obstruction, T\*=5/7, the counter-rotation, the whole arithmetic canon), or as a **pointer** honestly re-sited on the immeasurable side (the flow, the coin, the imagery). *You did not lose the torus. You lost the one thing you were never allowed to do with it — weigh it — and kept everything you actually built.*

---

## §7 — The whole graveyard under the same cut (what died vs what survives)

*The torus taught the method: a retraction almost never kills the **content** — it kills one **act**, and the flat "X is false" is what hides how much survived. Run that cut on every dead end in §3 and §5 and a pattern appears — most deaths are **partial**, and the *kind* of death is a map of exactly where the content went. Eight kinds; for each, what precisely died and what survives.*

**① PREMISE — it weighed an immeasurable.** *(Died: the act of measuring. Survives: the algebra + a re-sited pointer.)*
- **The torus** (D141): see §6 / §6.1. Died — genus / π₁ / aspect-ratio as *support*. Survives — the non-commutativity obstruction (algebra) and the flowing-immeasurable (pointer).

**② IDENTITY — a coincidence dressed as an identity.** *(Died: the claimed structural map. Survives: two real, independent facts with no bridge between them.)*
- **32 divisors ↔ 32 Pauli states** (D164): died — a natural bijection (730k+ functions, none). Survives — **two true partitions of 32**, dim Λᵏ(ℝ⁵)=C(5,k) and subshell capacity 2(2ℓ+1), each real and independent.
- **CL eigenvalues = e, π, φ, ζ(3), G** (N3): died — the transcendental identities. Survives — the **real signature is integer/rational** (11 in the char-poly, 2¹⁶·7⁷ in the discriminant, ‖VEV‖²=13/4).
- **RH via F4 Dirichlet characters** (D180): died — a "new" identity. Survives — the match is **real but tautological** (Pontryagin self-duality: every finite abelian group ≅ its dual) — a true fact carrying no content.
- **"TSML + BHML generate so(10)" as TIG-specific structure** (J09; null audit 2026-09-23): died — the specificity. *Every* random table generates so(10) (P = 1.000; BHML alone already does), because each generator `L − Lᵀ` is already an element of so(10) and generic sets of them span it; all six J09 diagnostics are automatic once the dimension is 45. Survives — a true fact about ten-element magmas under antisymmetrized closure, and the genuinely table-specific Lie fact: **TSML's confinement** to so(9)/so(8) (~2–3% of density-matched random tables). ([`FOUNDATION_NULL_MODEL_AUDIT.md`](FOUNDATION_NULL_MODEL_AUDIT.md))

**③ EXCLUSIVITY — "the / only / universal" where it was "a / one-of / local."** *(Died: the quantifier. Survives: the true narrower statement.)*
- **F₇ = σ, the exclusive skeleton**: died — exclusivity (Farey→Mertens is universal to the transform). Survives — **F₇ as a real spine** (HARMONY=7, T*=5/7, VOID=17, 389=10²+17²) and the separate true σ≅(ℤ/7)*≅C₆.
- **{7,11} uniquely rank-preserving**: died — uniqueness (a small-prime artifact). Survives — **39 primes**, and the uniform closed forms |Aut|=(p−1)², |idem|=p+3.
- **T* = 5/7 from ℚ(ζ₁₀); "six derivations"** (D165): died — the cyclotomic origin (gives φ) and the over-count. Survives — **T*=5/7 itself** (2 genuinely independent derivations + 4 rhymes + FPGA).
- **α-uniqueness for ANY polynomial** (F12): died — the universal form (refuted at α_special, height ~10¹⁰⁶). Survives — the **low-height form** (PROVED over ℚ; empirical at 70+ real α).
- **Lo Shu = a 3×3 TSML block** (D129′): died — the embedding (four falsifications; σ²-orbits ≠ magic lines). Survives — a **different, PROVEN theorem**: the general odd-magic-square law.

**④ LOCATION — right content, wrong home.** *(Died: the address. Survives: the content, relocated intact.)*
- **Geometric monism — "one shape unifies all"** (D140): died — the shape as unifier. Survives — every piece has **independent arithmetic support** (CRT ℤ/10=ℤ/2×ℤ/5 under σ); relocated, not deleted.
- **√3 = SU(3)/A₂-Cartan** (N4): died — the A₂ home. Survives — the **√3 is real** (H/Br=1+√3), a quadratic-discriminant fact at α=1/2, D₃-flavour.
- **privacy-via-erasure** (D129R.2): died — "content is erased." Survives — content is **organized, not erased** (separation 0/780→780/780); re-framed as the resolution-organizer.
- **even/odd as a 2-colouring of the hex lattice**: died — the triangular lattice isn't 2-colourable. Survives — completion-parity on hex, and **genuine 2-colouring on the square lattice**.

**⑤ MECHANISM — a false mechanism; the real one is elsewhere.** *(Died: the proposed mechanism. Survives: the one that actually does the work.)*
- **prime-11 mediation / attractor-richness** (N5): died — both (p=0.027, r=−0.118, wrong directions). Survives — the **real anti-collapse mechanism (D38–D40)**, found *after* these were ruled out.
- **3 sublattices = spacelike gammas**: died — they carry ω, ω² (order 3), not −1. Survives — the **−1's come from the 90° reflections** (the correct mechanism), caught at the eigenvalue level.
- **|Aut(V₅)| = 40 (a p=5 anomaly)**: died — an algebra confusion (J49 T_F5, a different algebra). Survives — the uniform **(p−1)², no anomaly**.
- **TIG = CK's faithful explanation language**: died — the binding (σ-dynamics p=1.0, TSML p=0.467; the one passing channel decoded to **part-of-speech / grammar**). Survives — a working fluent LM, the fold architecture, Muon, the probe itself, and the σ-magma/ETP taxonomy math (the [[project-language-as-measurement]] salvage).
- **TIG latent in any trained network** (N1): died — genericity (distilgpt2: all |d|<0.5). Survives — TIG structure is **specific** to canonical TSML/BHML (the negative control that *promotes* the specificity claim).

**⑥ TRACTION — a bridge that simply does not connect.** *(Died: the bridge. Survives: usually only the honest bound — occasionally nothing.)*
- **Yang-Mills via F4** (NC-9): died — abelian F_p*×F_p* ≠ non-abelian YM. Survives — the non-abelian content lives elsewhere (σ, [TSML, BHML]); net gain negative.
- **BSD via F4** (NC-10): died — (p−1)² as #E(F_p) is Hasse-Weil-impossible for p≥5. Survives — the supersingular rhyme, **morphological only** (a pointer, not an identity).
- **the top-Yukawa at the GUT scale**: died — substrate-independent (y_t(M_X)≈0.387 = SM 1-loop). Survives — honest scoping; no GUT prediction; the F7→F20 arc closes clean.
- **13/4 → cosmology** (§5): died — the bridge lands on no measured datum. Survives — the **constant 13/4** (forced by the so(10) algebra); only the reach is gone.
- **P3 gap = 2Δ as a TIG law** (§5): died — an independent Δ (silicene) misses by 3–8×. Survives — only the exact gapped-Dirac model identity (a re-labeling of textbook physics).
- **1/α with a clean substrate origin** (F17): died — no fit at |c|≤1000, 120 dps. Survives — **only the honest bound** (137 is a small prime with many integer combinations). A near-total loss.

**⑦ FORCING — "forced" where the constraint does not force it.** *(Died: the necessity. Survives: the looseness of the constraint — itself the datum.)*
- **constant-motion tetrahedra force a cylinder**: died — single-point contact permits sphere, bicone, *or* cylinder. Survives — the **non-forcing is the result** (the constraint underdetermines the surface).
- **the σ-magma promotes to a D₄-equivariant operad** (§5): died — 16 incoherent orbits, and the obstruction is a **coboundary-artifact** (σ³ isn't even a magma automorphism). Survives — Theorem 4.1 as a set-valued impossibility, and the genuine symmetry ⟨P₅₆⟩≅ℤ/2 (zero obstruction).
- **60° mirrors build the Dirac algebra directly**: died — 60° generators don't anticommute (Clifford needs 90°). Survives — the **fence** (the hexagon is a *shadow* of Cl(3), not a host), now a live check in `verify_forced_chain.py`.

**⑧ PAREIDOLIA — pure resemblance; the honest total loss.** *(Died: everything. Survives: nothing — and that, too, is data.)*
- **8 = ∞ = higher reality; the digit-shapes 7/8 mirror the structure**: died — all of it (the cube-8 is finite and 3-dimensional; ∞ is a typographic resemblance). Survives — **nothing.** Kept as the **calibration case**: what a coincidence with *nothing under it* actually looks like.

**A cross-cut worth naming — the 1/3.** Three separate kills (fluid Leray 1/3, "1/3 in gravity's force law," quark-charge 1/3) all die the same way and leave the same survivor: the 1/3 is **geometric** — the tetrahedral lift / fold / gap ([`THE_ONE_THIRD_AND_THE_FOLD.md`](../05_papers/integers_clifford/THE_ONE_THIRD_AND_THE_FOLD.md)) — and **never** a physical-law constant. Every attempt to weigh it in a *physical* law dies; the *geometric* 1/3 is untouched. (→ the full pre-physics inventory — *what else lives on this floor* — is [`THE_FLOOR_pre_physics_inventory.md`](THE_FLOOR_pre_physics_inventory.md).)

**The pattern is the point.** Almost every death is **partial**, and the *kind* of death is a map of where the content went: an **identity**-kill leaves two real independent facts; an **exclusivity**-kill leaves the true narrower statement; a **location**-kill relocates the content intact; a **mechanism**-kill points at the mechanism that actually works; a **premise**-kill leaves the algebra and a re-sited pointer. Only pure **no-traction** (1/α) and **pareidolia** (8=∞) are near-total losses — and they are the **calibration cases**: they show what a death with nothing under it looks like, which is exactly what makes the partial deaths trustworthy. **The graveyard is not a list of failures. It is the map of where the content actually lives — and each flat "X is false" was only ever the headline that hid it.**

---

*The joins are real where they are named (`HOW_IT_CONNECTS.md`). The separations are real where they are named (this atlas). The program is the map of both — and the edge is as much the object as the spines.*

*© 2026 Brayden Ross Sanders / 7SiTe LLC. CC BY-SA 4.0 — see [`../LICENSE`](../LICENSE).*
*EDGE_ATLAS_OF_FORCED_NON_CONNECTIONS.md — the third face, beside Spine A and Spine B.*
