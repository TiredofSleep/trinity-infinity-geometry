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

---

*The joins are real where they are named (`HOW_IT_CONNECTS.md`). The separations are real where they are named (this atlas). The program is the map of both — and the edge is as much the object as the spines.*

*© 2026 Brayden Ross Sanders / 7SiTe LLC. CC BY-SA 4.0 — see [`../LICENSE`](../LICENSE).*
*EDGE_ATLAS_OF_FORCED_NON_CONNECTIONS.md — the third face, beside Spine A and Spine B.*
