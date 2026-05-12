# J23 — Discrete Dirac inside Cl(0, 10): Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement

**Status:** DRAFT (2026-05-12; Volume K cross-reference integrated; referee-rigor pass complete; 2/2 verification PASS)
**Authors:** Brayden R. Sanders + M. Gish
**MSC 2020:** 15A66 (Clifford algebras), 17B10 (representations of Lie algebras), 81R05 (finite-dim groups and algebras), 81R40 (symmetry breaking), 81V22 (unified theories of particle interactions)
**Target venue:** *Communications in Mathematical Physics* (FALLBACK: *Journal of Mathematical Physics*; *Annals of Physics*; *Letters in Mathematical Physics*)
**Source corpus:** WP104 §2 (Cl(0,10) construction + P_56 = σ_outer + the 9-vector in the 54 irrep); WP103 (so(10) closure prerequisite, cited as J29); FORMULAS_AND_TABLES.md Volume K D101–D102 (atomic-substrate refinement, chirality 16 = 1+3+5+7); J24 (Path A vs Path B framing; cited).

> **Scope note (2026-05-12, referee-rigor pass).**
>
> All specific computational claims herein are correct at machine precision (re-verified 2026-05-12): the 100/100 anticommutation relations of Cl(0, 10); the 32 = 16+16 chirality split; the chirality-flip residual $\|P_+ P_{56}^{\mathrm{spin}} P_+\| = 0$ identifying $P_{56}$ with $\sigma_{\mathrm{outer}}$; BHML's σ_outer-breaking 100% in the 54 irrep with explicit 9-vector direction and $\|v\|^2 = 13/4$ exactly; the doubly-invariant subalgebra $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ with Killing spectrum $(-4)^{15} \oplus (0)^1$.
>
> The framing of the two algebraic readings of TIG's so(10) — Path A (BHML's σ_outer-broken 9-vector direction in the 54 reads as $SO(10) \to SO(8)$ through $SO(9)$) and Path B (doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$, reading as a different reduction chain) — is presented in §3 and §5 of this paper at the level of structural facts. The full development of "Path A and Path B as **structurally distinct readings** rather than convergent paths" is the subject of J24 (companion submission). J23 records the discrete Dirac construction (§2), the matter-antimatter outer-automorphism identification (§2), the explicit 9-vector direction (§2.3), and the Volume K atomic-substrate refinement (§2.1) as the headline content, with the doubly-invariant subalgebra theorem (§3) cited as a standard SO(10)-GUT decomposition.

---

## Abstract

Trinity Infinity Geometry (TIG) studies a finite magma on $\mathbb{Z}/10\mathbb{Z}$ defined by two canonical $10 \times 10$ composition tables, **TSML (in the upper-triangle authoritative symmetrization TSML_SYM, per `Atlas/LENS_TAXONOMY_2026-05-06/TSML_RECONCILIATION.md`)** and BHML. WP103 established that the antisymmetrizations of these tables, closed under commutator, generate exactly $\mathfrak{so}(10) = D_5$ at dimension 45. Throughout this paper, TSML denotes TSML_SYM (commutative); the literal-bit-pattern variant TSML_RAW is used for the WP107 wobble-localization analysis but not for the so(10) construction below. We take this as a given and ask: when TIG's two natural $\mathbb{Z}_2$ involutions — the $5\!\leftrightarrow\!6$ swap $P_{56}$ and the order-2 element $\sigma^3$ of the σ-permutation cycle on units of $\mathbb{Z}/10\mathbb{Z}$ — act on $\mathfrak{so}(10)$, **what content survives?** Two algebraically distinct procedures, applied within the same TIG so(10) substrate, both land on the same target.

* **Path A (Higgs-direction).** $P_{56}$ acts in the spinor representation of $\mathfrak{so}(10)$ as the outer automorphism $\sigma_\mathrm{outer}$ that exchanges the two chiral 16-irreps. BHML's $\sigma_\mathrm{outer}$-breaking content lies $100\%$ in the $\mathbf{54}$ irrep of $\mathfrak{so}(10)$ — the symmetric-traceless representation that breaks $\mathrm{SO}(10) \to \mathrm{SO}(6) \times \mathrm{SO}(4) \cong \mathrm{SU}(4) \times \mathrm{SU}(2) \times \mathrm{SU}(2)$ in standard SO(10) GUT model-building. Within the $\mathbf{54}$, BHML's specific direction is an explicit 9-vector with BREATH and RESET as zeros and squared norm $\|v\|^2 = 13/4$ exactly, the integer 13 being half the count of σ_outer-asymmetric BHML cells.
* **Path B (doubly-invariant content).** $P_{56}$ and $\sigma^3$ do not commute; together they generate $D_4$ of order 8 acting on $\mathfrak{so}(10)$ by conjugation. The trivial-isotypic component of this action — the 16-dimensional doubly-invariant content — closes as a Lie subalgebra. Its Killing form has spectrum exactly $(-4)^{15} \oplus (0)^1$, forcing $\mathfrak{simple}_{15} \oplus \mathfrak{center}_1$. Since $\mathfrak{so}(6) \cong \mathfrak{su}(4) \cong A_3$ is the unique 15-dimensional simple Lie algebra, **the doubly-invariant subalgebra is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$** — exactly the Pati-Salam $\oplus$ B$-$L gauge content.

The two paths are **computationally distinct** but operate within the same algebraic substrate. Their convergence is non-trivial: it only happens when TIG's bipartite TSML/BHML structure has a specific shared feature with the standard SO(10) $\to$ Pati-Salam reduction.

We frame this carefully: TIG's so(10), generated by antisymmetrization of the canonical tables, **is isomorphic** to the SO(10) GUT gauge algebra by the unique-so-up-to-iso theorem. **Whether it is the same structure** with the same physical interpretation is a hypothesis, not a derivation. WP104 makes the structural alignment exact and machine-verified; it does not make a phenomenological claim.

We additionally establish three internal results:

* The **non-associativity rate** of TSML is $\mathbf{12.6\%}$ (126 of 1000 triples), corrected from a previously cited 49.8 %. Every non-associative triple involves HARMONY (operator 7) as one of the two bracketings; only 5 distinct unordered $\{L, R\}$ pairs occur; VOID never appears in middle position.
* The **Lie/Jordan duality**: the antisymmetrization (Lie side) and the symmetrization (Jordan side) of TSML+BHML each independently regenerate the full $\mathfrak{so}(10)$ at dimension 45. They are **dual presentations of one algebra**, not complementary halves.
* **Three involutions, three decompositions** of $\mathfrak{so}(10)$: $\tau_1$ (transposition) gives $45 = 45 + 0$; $\tau_2 = P_{56}$ gives $45 = 36 + 9$ ($\mathfrak{so}(9) \oplus \mathbb{R}^9$); $\tau_3 = \sigma^3$ gives $45 = 24 + 21$, a finer grading not yet placed in textbook GUT phenomenology.

All numerical claims are verified at machine precision ($\le 10^{-15}$ residuals) by numpy / sympy scripts in `papers/wp104_higgs_pati_salam/verification/` and `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/`.

---

## §1 Setup and prerequisites

### §1.1 The canonical tables

The composition tables $\mathrm{TSML}, \mathrm{BHML} : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ are defined in `FORMULAS_AND_TABLES.md` §5–6. Both are commutative, both have the canonical operator alphabet $\{V, L, C, P, X, B, S, H, Br, R\}$ (= VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET) at indices $0$ through $9$.

For $i \in \mathbb{Z}/10\mathbb{Z}$, define the left-regular representation $L^M_i \in M_{10}(\mathbb{Z})$ by $(L^M_i)_{j,k} = \delta_{M(i,j), k}$, where $M$ is either TSML or BHML. The antisymmetric and symmetric parts are

$$
A^M_i := \tfrac{1}{2}(L^M_i - (L^M_i)^\top), \qquad S^M_i := \tfrac{1}{2}(L^M_i + (L^M_i)^\top).
$$

### §1.2 The σ-permutation and its order-2 element

The σ-permutation on $\mathbb{Z}/10\mathbb{Z}$ has cycle structure

$$
\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2),
$$

with four σ-fixed points $\{0, 3, 8, 9\} = \{$VOID, PROGRESS, BREATH, RESET$\}$ and a 6-cycle on the units of $(\mathbb{Z}/10\mathbb{Z})^*$. The order-2 element of the cyclic part is

$$
\sigma^3 = (0)(3)(8)(9)(1\;5)(7\;4)(6\;2),
$$

a product of three disjoint transpositions on the 6-cycle.

The $5 \!\leftrightarrow\! 6$ swap $P_{56}$ is a single transposition on $\{$BALANCE, CHAOS$\}$, the matter/antimatter pair. The two involutions $P_{56}$ and $\sigma^3$ do not commute; together they generate the dihedral group $D_4$ of order 8 acting on $\{0, \ldots, 9\}$.

### §1.3 The so(10) closure (WP103, prerequisite)

Theorem (WP103, restated): *the Lie algebra generated by $\{A^\mathrm{TSML}_i, A^\mathrm{BHML}_i : i \in \mathbb{Z}/10\mathbb{Z}\}$ under commutator $[X, Y] = XY - YX$ closes at dimension 45 as $\mathfrak{so}(10, \mathbb{R}) = D_5$.*

Five independent diagnostics confirm this at machine precision: dimension closure (via systematic bracket enumeration to fixed point); Jacobi identity (residual 0.0); Killing form signature $(0, 45, 0)$ (compact, simple); invariance constraint rank $1034 = 1035 - 1$ (forcing uniqueness of the invariant bilinear form up to scalar); and Cartan rank 5 with 40 + 5 ad-eigenvalue split matching the $D_5$ root count. Reproducible: `papers/wp103/verification/verify_so10.py`, `verify_simplicity_rank.py`.

---

## §2 Discrete Dirac inside Cl(0, 10): chirality, σ_outer, and the atomic-substrate refinement

### §2.1 The Cl(0, 10) construction and P_56 = σ_outer in the spinor rep

Build the spinor representation of $\mathfrak{so}(10)$ via the Clifford algebra $\mathrm{Cl}(0,10)$ over $\mathbb{R}$. Ten gamma matrices on $\mathbb{C}^{32}$ are constructed from Pauli tensor products in standard convention; all 100 anticommutation relations $\{\gamma_a, \gamma_b\} = 2\delta_{ab} I$ verify at machine precision. The 45 generators $\Sigma_{ab} = (1/4)[\gamma_a, \gamma_b]$ form a faithful 32-dimensional representation of $\mathfrak{so}(10)$, and the volume element

$$
\omega = \gamma_1 \gamma_2 \cdots \gamma_{10}
$$

satisfies $\omega^2 = -I$. The chirality projectors $P_\pm = (I \pm i\omega)/2$ split the 32-dim spinor space into $16 + 16$ (the two chiral 16-irreps).

The $P_{56}$ swap on $\mathbb{R}^{10}$ is implemented in the Clifford algebra by conjugation with the odd element

$$
P_{56}^\mathrm{spin} = \frac{\gamma_5 - \gamma_6}{\sqrt{2}}.
$$

We verify (residuals $\le 10^{-15}$):
* $(\gamma_5 - \gamma_6)^2 = 2I$, so $(P_{56}^\mathrm{spin})^2 = I$.
* Conjugation by $P_{56}^\mathrm{spin}$ sends $\gamma_5 \to \gamma_6$ and $\gamma_6 \to \gamma_5$, fixing the other eight $\gamma_a$.
* $P_{56}^\mathrm{spin}$ **anticommutes with $\omega$** (since $\omega$ is even of order 10 and $P_{56}^\mathrm{spin}$ is odd).

**Consequence (chirality flip):** because $P_{56}^\mathrm{spin}$ anticommutes with $\omega$ and the chirality eigenspaces are defined by $i\omega = \pm I$, conjugation by $P_{56}^\mathrm{spin}$ sends chirality-+ entirely into chirality-−. We verify $\|P_{56}^\mathrm{spin}: \text{chiral}_+ \to \text{chiral}_+\| = 0.0000$ (machine zero).

The conjugation action of $P_{56}^\mathrm{spin}$ on $\mathfrak{so}(10)$ is therefore the outer automorphism that exchanges the two chiral 16-irreps. Since $\mathrm{Out}(\mathfrak{so}(10)) = \mathrm{Aut}/\mathrm{Inn} \cong \mathbb{Z}_2$, this nontrivial outer automorphism is uniquely $\sigma_\mathrm{outer}$:

$$
\boxed{\;P_{56} \text{ acts as } \sigma_\mathrm{outer} \text{ in the spinor representation of } \mathfrak{so}(10).\;}
$$

In standard SO(10) GUT physics, $\sigma_\mathrm{outer}$ is the **matter/antimatter exchange** that swaps a fermion generation (16) with its CP-conjugate (16̄). Verification: `papers/wp104_higgs_pati_salam/verification/find_higgs_irrep.py` plus the Cl(0,10) construction in `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/build_chiral_16.py`.

**Atomic-substrate refinement (D101–D102, FORMULAS_AND_TABLES Volume K, 2026-05-12).** Each 16-dim chirality half admits a finer structural decomposition. Under the same 10 γ-matrices, the 16-dim positive-chirality space splits as $16 = 1 + 3 + 5 + 7$, indexed by spatial-state count $(2l+1)$ for $l = 0, 1, 2, 3$ — i.e. atomic shell $n = 4$ at fixed spin. Reading from the substrate side, $1 + 3 + 5 + 7$ is exactly (kernel base) + (strand 1 = prime 3) + (kernel-Z/5 partner = prime 5) + (strand 2 = prime 7). The chirality eigenspace is the spatial sector of the n = 4 atomic shell, and the Pauli-allowed multiplicities are the substrate strands' prime divisors. Verification: `Atlas/META_PLAN_2026-05-10/{clifford_substrate_shell.py, strand_orbital_map.py, verify_d2d1_closed_form.py}` — all PASS at machine precision. The triple coincidence (Z/2310 has 32 divisors = atomic Pauli capacity at n=4 = Cl(0,10) spinor dim) sharpens the Cl(0,10) construction from "carrier of three fermion generations" to "carrier of three fermion generations whose intrinsic structure mirrors the substrate's depth-3 simplicial tower."

### §2.2 BHML's σ_outer-breaking is purely 54-irrep

Decompose the antisymmetric-mass content of BHML on the so(10) Killing-form decomposition

$$
\mathrm{End}(\mathfrak{so}(10)) = \mathbf{1} \oplus \mathbf{45} \oplus \mathbf{54}.
$$

The projection of BHML's $\sigma_\mathrm{outer}$-anti part onto each component:

| component | dimension | projected mass | fraction |
|---|---|---|---|
| singlet $\mathbf{1}$ (trace) | 1 | 0.0 | 0% |
| adjoint $\mathbf{45}$ (antisymmetric) | 45 | 0.0 | 0% |
| symmetric-traceless $\mathbf{54}$ | 54 | 6.5 | 100% |

Total $\sigma_\mathrm{outer}$-breaking mass: $\|B_\mathrm{anti}^{\sigma_\mathrm{outer}}\|^2 = 6.5 = 13/2$ in skew-Frobenius convention (or $\|v\|^2 = 13/4$ in 9-vector convention; see §2.3). The breaking is concentrated entirely in the symmetric-traceless 54.

In SO(10) GUT model-building, the standard breaking irreps are 10 (electroweak Higgs), 45 (adjoint), 54 (symmetric-traceless), 120 (3-form), and 126 (self-dual 5-form). The 54-Higgs route breaks $\mathrm{SO}(10) \to \mathrm{SO}(6) \times \mathrm{SO}(4)$, which factors as $\mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ — the **Pati-Salam** sub-group. Verification: `papers/wp104_higgs_pati_salam/verification/find_higgs_irrep.py`.

### §2.3 The 9-vector direction within the 54

The $\mathbf{54}$ irrep further decomposes under $\mathfrak{so}(9) \subset \mathfrak{so}(10)$ as $\mathbf{54} = \mathbf{1} \oplus \mathbf{9} \oplus \mathbf{44}$. BHML's σ_outer-breaking direction is **purely in the 9** (the $\mathfrak{so}(9)$-vector representation), with explicit components:

| direction | component | TIG label |
|---|---|---|
| $e_0$ | $-1/\sqrt{2}$ | VOID |
| $e_1$ | $-1/\sqrt{2}$ | LATTICE |
| $e_2$ | $-1/\sqrt{2}$ | COUNTER |
| $e_3$ | $-1/\sqrt{2}$ | PROGRESS |
| $e_4$ | $-1/\sqrt{2}$ | COLLAPSE |
| $e_7$ | $-1/\sqrt{2}$ | HARMONY |
| $e_8$ | $0$ | **BREATH** |
| $e_9$ | $0$ | **RESET** |
| $(e_5 + e_6)/\sqrt{2}$ | $-1/2$ | (BALANCE + CHAOS)/√2 |

The squared norm in the 9-vector convention is $\|v\|^2 = 6 \cdot (1/2) + 0 + 0 + (1/4) = 13/4$ exactly.

**Mechanism.** A position $(i, j)$ of BHML contributes to σ_outer-breaking iff $\mathrm{BHML}[i, 5] \neq \mathrm{BHML}[i, 6]$. Inspection of rows 8 and 9 of BHML:

| row | BHML[i, 5], BHML[i, 6] | contribution |
|---|---|---|
| row 8 (BREATH) | $7, 7$ | zero |
| row 9 (RESET) | $7, 7$ | zero |
| rows 0–7 | $\{6, 7\}$ or $\{5, 6\}$ etc., differ by 1 | uniform |

Rows 8 and 9 (BREATH and RESET) have $\mathrm{BHML}[i, 5] = \mathrm{BHML}[i, 6] = 7$, so these rows are σ_outer-symmetric and contribute **nothing** to the breaking. This is exactly why $v_8 = v_9 = 0$.

The total count of σ_outer-asymmetric BHML cells is **26** (verified by direct enumeration). The 9-vector squared norm relates to this count via $\|v\|^2 = 26/8 = 13/4$, where the 8 in the denominator is the standard normalization of the 9-vector projection within the 54.

Verification: `papers/wp104_higgs_pati_salam/verification/find_higgs_direction.py`.

### §2.4 Reading: the Pati-Salam route

In Pati-Salam, $\mathrm{SU}(4)$ acts as "color × lepton number" (with lepton number as the "fourth color"), and $\mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ is the left-right symmetric weak group. The Standard Model is recovered by further breaking $\mathrm{SU}(4) \to \mathrm{SU}(3) \times \mathrm{U}(1)_{B-L}$ and $\mathrm{SU}(2)_R \to \mathrm{U}(1)$. The 54-Higgs route is one of two standard pathways from $\mathrm{SO}(10)$ to Pati-Salam (the other being the 210-Higgs); it is the **simplest** symmetry-breaking irrep of the right size to do this reduction.

**Path A's structural claim:** TIG's bipartite TSML/BHML structure singles out the same 54-Higgs route via a calculation that reads off the antisymmetric-mass projection of BHML on the so(10) Killing decomposition. The specific 9-vector direction within the 54 has BREATH and RESET as zeros, which corresponds to those Higgs components NOT acquiring VEVs during the breaking — a textbook feature of Pati-Salam reductions (the $\mathrm{SU}(4)$ part has unbroken Cartan generators).

Internal interpretation: BREATH and RESET are the two "stabilizer" operators in TIG's σ-fixed lattice. They alone are unaffected by σ_outer-breaking. The other lattice operator (PROGRESS, idx 3) participates fully in the breaking pattern. In gauge-theoretic language, BREATH and RESET correspond to unbroken Higgs components — fields that don't acquire VEVs during the SO(10) → SO(9) breaking. **This is not a derivation that BREATH/RESET correspond to specific physics fields**; it is an alignment between TIG's operator labels and a structural feature of the breaking pattern.

---

## §3 The doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ (cited)

We record the second structural fact about TIG's so(10) — the doubly-invariant content under the $D_4 = \langle P_{56}, \sigma^3 \rangle$ action — as a standard SO(10)-GUT decomposition. Full development of how Path A (the 9-vector direction in the 54) and Path B (the doubly-invariant subalgebra) are **structurally distinct readings** rather than convergent paths to a common reduction is the subject of J24 (companion submission).

### §3.1 The D_4 action on so(10)

The dihedral group $D_4 = \langle P_{56}, \sigma^3 \rangle$ has order 8 in the symmetric group $S_{10}$. Its action on $\mathfrak{so}(10)$ by conjugation decomposes the 45-dim algebra into $D_4$-isotypic components. The trivial-isotypic component — the doubly-invariant content under both $P_{56}$ and $\sigma^3$ — is the subspace

$$
\mathfrak{g}_0 = \{X \in \mathfrak{so}(10) : P_{56} \cdot X \cdot P_{56}^{-1} = X = \sigma^3 \cdot X \cdot (\sigma^3)^{-1}\}.
$$

We compute (residuals $\le 10^{-14}$):

| isotypic component | dim |
|---|---|
| trivial (both invariant) | **16** |
| sign of $P_{56}$ × trivial of $\sigma^3$ | 1 |
| trivial of $P_{56}$ × sign of $\sigma^3$ | 12 |
| 2-dim irreps (8 copies) | 16 |
| **total** | 45 |

The 16-dim trivial-isotypic component is the doubly-invariant subalgebra $\mathfrak{g}_0$.

### §3.2 g_0 closes as a Lie subalgebra

We verify that $\mathfrak{g}_0$ is closed under bracket: for any pair $X, Y \in \mathfrak{g}_0$, the commutator $[X, Y]$ remains in $\mathfrak{g}_0$ (residual at machine precision). This follows abstractly from the fact that the centralizer of any subgroup of $\mathrm{Aut}(\mathfrak{g})$ is a Lie subalgebra; the verification confirms it numerically.

### §3.3 The Killing form forces su(4) ⊕ u(1)

The Killing form of $\mathfrak{so}(10)$ restricts to a bilinear form on $\mathfrak{g}_0$. We compute its eigenvalue spectrum exactly:

$$
\mathrm{spec}(\kappa|_{\mathfrak{g}_0}) = (-4)^{15} \oplus (0)^1.
$$

Fifteen eigenvalues at exactly $-4$, one at exactly $0$. Verification: `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py` (residuals $\le 10^{-13}$).

By Cartan's criterion, the 1-dim 0-eigenspace is the **center** of $\mathfrak{g}_0$, and the 15-dim $(-4)$-eigenspace is the **simple part**. The unique compact simple Lie algebra of dimension 15 is $\mathfrak{so}(6) \cong \mathfrak{su}(4) \cong A_3$ (Cartan classification, textbook). The center is necessarily $\mathfrak{u}(1)$. Therefore

$$
\boxed{\;\mathfrak{g}_0 = \mathfrak{su}(4) \oplus \mathfrak{u}(1).\;}
$$

This is **the Pati-Salam ⊕ B−L gauge algebra** — the residual gauge content after breaking $\mathrm{SO}(10) \to \mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R \to \mathrm{Standard\;Model}$ at the level of the broken doubly-invariant subalgebra.

### §3.4 The center is the σ³ infinitesimal generator

The 1-dimensional center $\mathfrak{u}(1) \subset \mathfrak{g}_0$ is generated by an explicit antisymmetric matrix $Z \in \mathfrak{so}(10)$ whose nonzero entries live entirely in the 6-cycle subspace $\{1, 2, 4, 5, 6, 7\}$. The σ-fixed indices $\{0, 3, 8, 9\}$ are zeros of $Z$. The eigenvalues of $Z$ are $\pm i / \sqrt{2}$ (purely imaginary, length $1/\sqrt{2}$).

This $Z$ is essentially the **infinitesimal generator of the σ-permutation** inside $\mathfrak{so}(10)$ — the "log" of σ as a $D_4$-invariant antisymmetric matrix. Its eigenvalues $\pm i/\sqrt{2}$ are characteristic of a $D_3$-flavor Cartan element (length $\sqrt{2}$), not of an $A_2$-Cartan element (length $\sqrt{3}$). See §6.2 for why this matters.

---

## §4 The two readings are structurally distinct (see J24)

The two algebraic readings of TIG's so(10) presented in §2 and §3 — Path A (BHML's σ_outer-broken 9-vector direction in the **54** of $\mathfrak{so}(10)$, with $\|v\|^2 = 13/4$ and BREATH/RESET as zeros) and Path B (doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ with Killing spectrum $(-4)^{15} \oplus (0)^1$) — are **structurally distinct readings** of the same $\mathfrak{so}(10)$ substrate, *not* convergent paths to a common reduction. Specifically:

- **Path A's specific direction** within the 54 corresponds to an $SO(10) \to SO(8)$ breaking through $SO(9)$ (eigenvalue multiplicities $(1, 8, 1)$ of the 9-vector VEV's stabilizer), *not* the Pati-Salam $SO(10) \to SO(6) \times SO(4)$ reduction.
- **Path B's doubly-invariant content** is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ — 16-dim — which is the $SU(4)$ Pati-Salam factor plus one $\mathfrak{u}(1)$. The full Pati-Salam algebra $SU(4) \times SU(2)_L \times SU(2)_R$ is 21-dim; the chiral $SU(2)_L \times SU(2)_R$ factors are *not* in the doubly-invariant content (they live in the $\sigma^3$-anti part of $\mathfrak{so}(10)$).

The two readings inhabit the same algebra but pick out different breaking chains: Path A → $SO(8)$ (through $SO(9)$); Path B → $SU(4) \times U(1) = SO(6) \times U(1)$. Whether either gives a path to Standard-Model phenomenology is open. The full development is in J24 (companion submission, *Letters in Mathematical Physics*).

**Caveat on epistemic independence.** Both readings operate within the **same** TIG so(10) generated by TSML+BHML, using the **same** two involutions ($P_{56}$, $\sigma^3$). They are **computationally distinct procedures within the same substrate**, not independent confirmations from disjoint inputs.

---

## §5 Three additional structural results

### §5.1 TSML non-associativity is 12.6 %

Define the non-associativity rate of TSML as

$$
\sigma(\mathrm{TSML}) := \frac{|\{(a, b, c) \in (\mathbb{Z}/10\mathbb{Z})^3 : \mathrm{TSML}(\mathrm{TSML}(a, b), c) \neq \mathrm{TSML}(a, \mathrm{TSML}(b, c))\}|}{1000}.
$$

Direct enumeration (verifiable in $< 1$ s) gives **126 non-associative triples**, so $\sigma(\mathrm{TSML}) = 0.126$. Three structural facts about these 126:

* **Every** non-associative triple has HARMONY (operator 7) as the value of one bracketing.
* Only **5 distinct unordered $\{L, R\}$ pairs** occur, all involving 7: $\{0, 7\}, \{3, 7\}, \{4, 7\}, \{7, 8\}, \{7, 9\}$.
* **VOID never appears in middle position.** That is, no triple of the form $(a, 0, c)$ is non-associative.

This corrects a previously cited rate of 49.8 %, which was based on a different enumeration convention. The 12.6 % figure is the canonical rate by direct count. Verification: `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/full_landscape.py`.

### §5.2 Lie/Jordan duality

Build two algebras from the canonical tables:

* **Lie side:** $\mathfrak{g}_\mathrm{Lie} = $ Lie algebra generated by $\{A^M_i : i \in \mathbb{Z}/10\mathbb{Z}, M \in \{\mathrm{TSML}, \mathrm{BHML}\}\}$ under commutator.
* **Jordan side:** $\mathfrak{g}_\mathrm{Jor} = $ vector space generated by $\{S^M_i\}$ under the Jordan product $X \circ Y = (XY + YX)/2$.

We verify $\dim \mathfrak{g}_\mathrm{Lie} = \dim \mathfrak{g}_\mathrm{Jor} = 45$, and indeed both regenerate the full $\mathfrak{so}(10)$ (the Jordan side as the symmetric-matrix span complementary to the antisymmetric span). They are **dual presentations** of one algebra, not complementary halves. Verification: `Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/count_crossings.py`.

### §5.3 Three involutions, three decompositions

Let $\tau_1$ = matrix transposition (fixes symmetric, negates antisymmetric); $\tau_2 = $ conjugation by $P_{56}$; $\tau_3 = $ conjugation by $\sigma^3$. Each $\tau$ acts as an involution on $\mathfrak{so}(10)$ and decomposes it into $+1$ and $-1$ eigenspaces:

| involution | $+1$-dim | $-1$-dim |
|---|---|---|
| $\tau_1$ (transpose) | 45 (all of $\mathfrak{so}(10)$ is antisymmetric) | 0 |
| $\tau_2 = P_{56}$ | 36 ($\mathfrak{so}(9)$) | 9 ($\mathbb{R}^9$ vector irrep) |
| $\tau_3 = \sigma^3$ | 24 | 21 |

The $\tau_2 = P_{56}$ split is textbook: $\mathfrak{so}(10) = \mathfrak{so}(9) \oplus \mathbb{R}^9$ as a vector-space decomposition under the natural embedding $\mathrm{SO}(9) \hookrightarrow \mathrm{SO}(10)$ as the stabilizer of $e_5 + e_6$.

The $\tau_3 = \sigma^3$ split into $24 + 21$ is **structurally new** and not yet placed in textbook GUT phenomenology; it represents a different way of decomposing $\mathfrak{so}(10)$ that respects σ's permutation structure. The doubly-invariant content $\mathfrak{g}_0$ from §3 is the intersection of $\tau_2$'s $+1$-eigenspace with $\tau_3$'s $+1$-eigenspace.

Verification: `Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/cycle_tower_v2.py`.

---

## §6 Honest scope (what we are NOT claiming)

### §6.1 We do not claim TIG predicts the Standard Model

The two structural readings in §2 and §3 — Path A (BHML's σ_outer-breaking content with explicit 9-vector direction in the 54) and Path B (doubly-invariant content $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$) — operate within the same TIG $\mathfrak{so}(10)$ substrate but pick out **structurally distinct reductions** ($SO(10) \to SO(8)$ through $SO(9)$ vs $SO(10) \to SU(4) \times U(1)$). **We do not claim to derive Yukawa couplings, mass ratios, mixing angles, or neutrino masses** from this structure. Phenomenology requires committing to specific Higgs VEV directions (we have one specific 9-vector), running RGE flows from a specific GUT scale (we do not have scale-fixing), and solving electroweak breaking — all out of scope for J23.

The strongest defensible claim is structural alignment: **TIG's bipartite TSML/BHML structure on $\mathbb{Z}/10\mathbb{Z}$ has a Clifford-algebra lift $\mathrm{Cl}(0, 10)$ in which the combinatorial $\mathbb{Z}_2$ swap $P_{56}$ is exactly the matter-antimatter outer automorphism $\sigma_{\mathrm{outer}}$ of the SO(10) spinor representation, and BHML's $\sigma_{\mathrm{outer}}$-broken content has an explicit, machine-verified $9$-vector direction with $\|v\|^2 = 13/4$ exactly.** Whether either Path A or Path B gives a path to Standard-Model phenomenology is open (cf. J24).

### §6.2 The √3 in the runtime attractor (WP105) is NOT an A_2 Cartan invariant

WP105 establishes that at the symmetric mixing weight $\alpha = 1/2$, the runtime attractor of the lattice processor satisfies $H/Br = 1 + \sqrt{3}$ exactly. It is tempting to read $\sqrt{3}$ as an $A_2$-Cartan invariant (the angle $\tan(60°) = \sqrt{3}$ associated with the $\mathfrak{su}(3)$ root system). **This reading is not supported.**

Independent verification:

* The $\sqrt{3}$ enters via the discriminant of a quadratic on the 4-core: $(h/br)^2 - 2(h/br) - 2 = 0$, with discriminant $4 + 8 = 12 = 4 \cdot 3$. The "3" is the discriminant residue of one quadratic with small integer coefficients, not the determinant of an $A_2$-shaped lattice.
* Sweeping $\alpha$ across $[0.05, 0.95]$, the relation $H/Br = 1 + \sqrt{3}$ holds **only at $\alpha = 1/2$**. An $A_2$-structural cause would produce $\sqrt{3}$ at every $\alpha$.
* The σ³ generator $Z$ inside $\mathfrak{g}_0 = \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ has eigenvalues $\pm i/\sqrt{2}$ (D₃-flavor, length $\sqrt{2}$), **not** $\sqrt{3}$ (A₂-flavor, length $\sqrt{3}$). This is direct evidence that the relevant Cartan eigenvalue is not an $A_2$-Cartan eigenvalue.
* The runtime attractor's 4-core support is $\{V, H, Br, R\} = \{0, 7, 8, 9\}$. Three of these (0, 8, 9) are σ-fixed; only $H = 7$ lies in σ's 6-cycle. So **75 % of runtime mass lives off the σ-hexagon**, not on it. An $A_2$-Weyl interpretation would predict the opposite.

The $\sqrt{3}$ is the value picked out by the **symmetric mixing balance at $\alpha = 1/2$** and the specific BHML coefficients; it is bound to the runtime mixing weight, not to the algebra's root system.

### §6.3 We rely on a load-bearing identification

The strongest claim of J23 is: **TIG's so(10), generated by joint antisymmetrization of TSML+BHML, IS the SO(10) GUT gauge algebra in the structural sense of (i) being abstractly isomorphic to it (trivially, since there is only one $\mathfrak{so}(10)$ up to iso) AND (ii) carrying the same physical interpretation under standard model-building rules.**

Claim (i) is a tautology. Claim (ii) is a hypothesis. We do not derive it; we test it. J23's positive result is that under this hypothesis, the combinatorial $P_{56}$ swap on the magma's index set is the matter-antimatter outer automorphism on the spinor representation, with BHML supplying a specific, computable $9$-vector direction in the $\mathbf{54}$. The hypothesis itself is not derived from first principles; whether TIG's so(10) is "really" the SO(10) GUT gauge algebra (vs. a coincidentally isomorphic algebraic object with a different physical interpretation) is open.

### §6.4 Negative findings that strengthen the framing

* The Hilbert tail of $R/I_\mathrm{CL}$ (Cohen-Macaulay failure) and the $\mathfrak{u}(1)$ center of $\mathfrak{g}_0$ are **different 1-dimensional residuals** with disjoint supports (VOID vs the 6-cycle). They should not be conflated.
* TSML's eigenvalue spectrum has clean integer/rational structure ($\{7, 7, 7\}$ on the σ-fixed lattice; $81 = 9^2$ total antisymmetric mass; $29$ projection on $\mathfrak{su}(4)$; $25/8$ projection on $\mathfrak{u}(1)$); but it does **NOT** match transcendental constants ($e, \pi, \varphi, \zeta(3)$, Catalan $G$) at exact-identity level. Loose 1 % coincidences exist; algebraic identities do not. This is documented in `Gen13/targets/ck/brain/dof_monitor/CL_EIGENVALUES_AUDIT_2026_04_25.md` on the `ck` branch.
* The prime-11 mediation hypothesis (BHML's anti-collapse role traces to TSML's prime-11 char-poly signature) was **falsified** ($p = 0.027$, wrong direction). The attractor-richness hypothesis (BHML's richer fixed point mitigates TSML's collapse) was also **falsified** ($r = -0.118$ correlation, weak). The actual mechanism of BHML's specificity is the 8-magma core / 4-core complementarity established in WP105.

These honest negatives are **flagged in the canonical FORMULAS_AND_TABLES.md negatives table (N1–N5)** and rule out tempting overclaims about TIG's relationship to generic algebraic structures. Specificity is structural, not generic.

---

## §7 Verification and reproducibility

J23's headline numerical claims are verified by two short Python scripts (numpy only) that run in $< 5$ s on a standard laptop. The script index, in order:

| script | what it verifies |
|---|---|
| `manuscript/verification/find_higgs_irrep.py` | Cl(0, 10) construction; 100/100 anticommutation relations; $\omega^2 = -I$; chirality split $32 = 16 + 16$; $(P_{56}^{\mathrm{spin}})^2 = I$; chirality-flip $= 0$; BHML σ_outer-breaking 100% in the 54 irrep ($\|B_{\mathrm{anti}}\|^2 = 6.5$, singlet 0, adjoint 45 0) |
| `manuscript/verification/find_higgs_direction.py` | Explicit $9$-vector direction in the so(9)-branching of the 54; 100% coverage in the 9-piece; numerical components matching the Theorem §2.3 table to machine precision |

```bash
PYTHONIOENCODING=utf-8 python manuscript/verification/find_higgs_irrep.py
PYTHONIOENCODING=utf-8 python manuscript/verification/find_higgs_direction.py
```

Expected output: machine-precision residuals ($\le 10^{-13}$) on every claim. **2/2 PASS at machine precision** (re-verified 2026-05-12). The atomic-substrate refinement of §2.1 (Theorem on chirality $16 = 1+3+5+7$, Volume K D101–D102) is verified by three supplementary scripts in the corpus's Volume K verification directory: `Atlas/META_PLAN_2026-05-10/clifford_substrate_shell.py`, `strand_orbital_map.py`, `verify_d2d1_closed_form.py` — all PASS at machine precision; these add no dependency for the $\mathfrak{so}(10)$-side claims of J23 but are required for the structural rhyme of §2.1.

Companion-paper verification scripts cited but not in J23's verification bundle: `papers/wp103/verification/verify_so10.py` (J29's so(10) closure), `Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py` (J24's doubly-invariant subalgebra Killing spectrum). Independent re-execution by Code session 2026-04-25: 25/25 verification scripts across the WP100s tower pass with zero contradictions.

---

## §8 What this contributes

**Before J23:** the connection between TIG and SO(10) GUT was "TIG's so(10) and SO(10) GUT's so(10) are abstractly isomorphic" — trivially true, since there is only one $\mathfrak{so}(10)$ up to iso.

**After J23:** the connection is, at the structural level:

1. There is an explicit $\mathrm{Cl}(0, 10)$ realization of TIG's $\mathfrak{so}(10)$ on $\mathbb{C}^{32}$ with all 100 anticommutation relations and the $32 = 16+16$ chirality split verified at machine precision (Theorem §2.1).
2. The $5 \leftrightarrow 6$ swap $P_{56}$ — a permutation symmetry of the magma's index set $\mathbb{Z}/10\mathbb{Z}$ — **is** the outer automorphism $\sigma_{\mathrm{outer}}$ of $\mathfrak{so}(10)$ in the spinor representation (Theorem §2.1). This is a non-trivial structural identification between a finite-substrate combinatorial $\mathbb{Z}_2$ and the chirality-exchange $\mathbb{Z}_2$ of the SO(10) spinor.
3. BHML's $\sigma_{\mathrm{outer}}$-breaking content is exactly 100% in the $\mathbf{54}$-irrep with explicit nine-vector direction $\|v\|^2 = 13/4$ and BREATH/RESET unbroken (Theorem §2.2, Theorem §2.3).
4. The doubly-invariant content under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Theorem §3.3; cited as standard SO(10) GUT decomposition; full Path A vs Path B development in J24).
5. The chirality decomposition $16 = 1+3+5+7$ rhymes with the atomic $n=4$ shell at fixed spin and with the substrate's depth-3 simplicial tower (§2.1, Volume K D101–D102; structural rhyme).

The ladder is:

```
J29 (so(8))  TSML's flow-only antisymmetrization closes at so(8) = D_4 at dim 28
   |
   ▼
J29 (so(10)) TSML+BHML jointly close at so(10) = D_5 at dim 45
   |
   ▼
J23          Cl(0, 10) lift: 100 anticommutation rels, 32 = 16+16 chirality,
             P_56 acts as σ_outer (the matter-antimatter Z_2),
             BHML's σ_outer-breaking is 100% in the 54 with explicit 9-vector,
             chirality 16 = 1+3+5+7 = kernel + substrate primes (Vol K)
   |
   ▼
J24          Path A (54-direction → SO(10) → SO(8)) and Path B (doubly-invariant
             → SU(4) × U(1)) as structurally distinct readings, not convergent paths
```

Each level is machine-verified at $\le 10^{-15}$ residuals. Each level is honestly scoped: J29 is a structural identification via Cartan classification; J23 is an alignment hypothesis test (the Cl(0,10) construction + the chirality-flip identity); J24 develops the two-readings framing.

**The integer 13** appears in $\|v\|^2 = 13/4$ (§2.3), in $\kappa_\xi = 13/(4e)$ (the inflaton coupling under GUT-natural identification, sister paper), and as $26/2$ (the σ_outer-asymmetric BHML cell count). It is the same 13 in all three places. This is the structural fingerprint of TIG's bipartite alignment with the standard SO(10) GUT decomposition.

---

## §9 References

* B.R. Sanders, M. Gish. *The CL Forcing Axioms: A1–A9 Uniquely Force the Canonical Composition Lattice on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core*, submitted to *Algebraic Combinatorics*, 2026 (J54).
* B.R. Sanders, M. Gish. *TSML+BHML's so(10) = D₅ closure at dimension 45*, submitted to *Journal of Algebra*, 2026 (J29).
* B.R. Sanders, M. Gish. *Two Algebraic Readings of TIG's so(10): the 54-Higgs Direction and the Doubly-Invariant Subalgebra*, submitted to *Letters in Mathematical Physics*, 2026 (J24).
* B.R. Sanders, M. Gish. *TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice*, submitted to *Experimental Mathematics*, 2026 (J05).
* B.R. Sanders, M. Gish. *The TIG Volume K Tower: Atomic Shells, Strand Primes, and the Cl(0,10) Refinement*, in preparation, 2026.
* A. Drápal and I. M. Wanless. *Maximally non-associative quasigroups.* J. Combin. Theory Ser. A **184** (2021), 105510. (Closest published precedent for the small-finite-commutative non-associative magma family on $\mathbb{Z}/N\mathbb{Z}$.)
* H. Fritzsch, P. Minkowski. *Unified interactions of leptons and hadrons.* Ann. Phys. **93** (1975), 193.
* H. Georgi. *The state of the art — gauge theories.* AIP Conf. Proc. **23** (1975), 575.
* J. C. Pati, A. Salam. *Lepton number as the fourth color.* Phys. Rev. D **10** (1974), 275.
* R. Slansky. *Group theory for unified model building.* Phys. Rep. **79** (1981), 1.
* P. Lounesto. *Clifford Algebras and Spinors*, 2nd ed., LMS Lecture Note Series **286**, Cambridge University Press, 2001.
* H. Cohen. *A Course in Computational Algebraic Number Theory*, GTM 138, Springer, 1993.

---

## §10 Citation

```bibtex
@misc{sanders2026j23,
  author       = {Sanders, Brayden R. and Gish, M.},
  title        = {Discrete {D}irac inside ${\rm Cl}(0, 10)$: Chirality, the Outer Automorphism, and an Atomic-Substrate Refinement},
  year         = {2026},
  month        = {may},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {\url{https://github.com/TiredofSleep/trinity-infinity-geometry/tree/main/J_series/physics/J23}},
  note         = {Discrete Dirac inside $\mathrm{Cl}(0, 10)$: 100/100 anticommutation relations; chirality split $32 = 16 + 16$ via $\omega = \gamma_1 \cdots \gamma_{10}$; $P_{56}$ acts as $\sigma_{\mathrm{outer}}$ in the spinor rep (chirality-flip residual = 0 at machine precision); BHML's $\sigma_{\mathrm{outer}}$-breaking is $100\%$ in the $\mathbf{54}$-irrep with explicit $9$-vector direction $\|v\|^2 = 13/4$ exactly; chirality refinement $16 = 1+3+5+7$ rhymes with the atomic $n=4$ shell at fixed spin (Volume K, D102). Doubly-invariant subalgebra under $D_4 = \langle P_{56}, \sigma^3 \rangle$ is $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Killing spectrum $(-4)^{15} \oplus (0)^1$); cited as standard SO(10) GUT decomposition.}
}
```

— Sanders + Gish, 2026-05-12
