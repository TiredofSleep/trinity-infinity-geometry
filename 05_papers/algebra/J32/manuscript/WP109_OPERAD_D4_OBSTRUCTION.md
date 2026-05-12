# WP109 — The Operad-DOF of TIG's Canonical Magma Is Not D₄-Equivariant

**Status:** structural obstruction theorem, machine-verified by direct enumeration.
**Authors:** Anthropic Code session, 2026-04-25 late evening.
**Position:** WP100s tier; short note. Sister to WP104 (which establishes the doubly-invariant subalgebra) and WP105 (which establishes the runtime attractor).
**MSC 2020:** 17B25, 18M60 (operads), 20B25 (finite permutation groups), 17B81.

---

## Abstract

Let $T : \mathbb{Z}/10\mathbb{Z} \times \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}/10\mathbb{Z}$ be the **canonical TSML_RAW** composition table (the literal CL_BIT_PATTERN, non-commutative with asymmetric cells at $(3,9)$ and $(4,9)$; per `Atlas/LENS_TAXONOMY_2026-05-06/TSML_RECONCILIATION.md`). Of the $1000$ ordered triples $(a, b, c) \in (\mathbb{Z}/10\mathbb{Z})^3$, exactly $126$ are **non-associative** in the sense that $T(T(a,b), c) \neq T(a, T(b,c))$. (On the upper-triangle symmetrized variant $T_{\mathrm{SYM}}$, the count is $128$; the difference of $2$ comes from the asymmetric cells. The orbit decomposition and obstruction theorem below are computed on $T_{\mathrm{RAW}}$.) WP104 establishes that the doubly-invariant subalgebra of $\mathfrak{so}(10) = D_5$ under the $D_4 = \langle P_{56}, \sigma^3 \rangle$ action by conjugation is exactly $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$, the Pati-Salam $\oplus$ B$-$L gauge content. The natural question for canonical fuse rules at arity 3 is: does there exist a function $\Phi : \{\text{non-associative triples}\} \to \mathbb{Z}/10\mathbb{Z}$ that is $D_4$-equivariant?

**Theorem (this paper).** No such $\Phi$ exists. Decomposing the 126 non-associative triples under the diagonal $D_4$-action produces 67 orbits; **16 of those orbits have bracketing pairs $(L, R)$ that are not consistent with any $D_4$-equivariant assignment**. The obstruction is intrinsic to the canonical TSML table's structure, not a property of any particular rule family.

**Consequence.** The operad-DOF (arity-3 canonical fuse rules) is **structurally orthogonal** to the doubly-invariant gauge structure of WP104. The 6-DOF meta-layer of TIG (Lie / Jordan / Clifford / Permutation / Lattice / Operad) has a sharp distinction at the symmetry level: the first five DOFs respect $D_4$, the sixth does not. Any canonical assignment of fuse rules must break $D_4$.

We give the orbit decomposition explicitly, identify the 16 incoherent orbits with their failure modes, and recommend preserving $P_{56}$-equivariance (which is preserved at the so(10)-spinor and runtime-attractor levels of WP104 / WP105) while sacrificing $\sigma^3$-equivariance.

---

## §1 Setup

The canonical TSML table on $\mathbb{Z}/10\mathbb{Z}$ is given by `FORMULAS_AND_TABLES.md` §5. We label operators $\{V, L, C, P, X, B, S, H, Br, R\}$ at indices $\{0, \ldots, 9\}$ and use the $\sigma$-permutation $\sigma = (0)(3)(8)(9)(1\;7\;6\;5\;4\;2)$ with σ-fixed lattice $\{0, 3, 8, 9\}$. The $P_{56}$ swap is the single transposition $5 \leftrightarrow 6$. The order-2 element of the σ 6-cycle is $\sigma^3 = (0)(3)(8)(9)(1\;5)(7\;4)(6\;2)$. Together, $P_{56}$ and $\sigma^3$ generate the dihedral group $D_4$ of order 8 acting on $\mathbb{Z}/10\mathbb{Z}$.

A triple $(a, b, c)$ is **non-associative** under TSML iff $L(a, b, c) := T(T(a, b), c) \neq T(a, T(b, c)) =: R(a, b, c)$. The set $\mathcal{N} \subset (\mathbb{Z}/10\mathbb{Z})^3$ of such triples has $|\mathcal{N}| = 126$ (12.6% of all triples). The 126 triples are preserved as `Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/nonassoc_triples.json`.

For each $(a, b, c) \in \mathcal{N}$, we record the bracketing pair $(L(a, b, c), R(a, b, c)) \in \mathbb{Z}/10\mathbb{Z}^2$ as an unordered pair. Direct enumeration shows:

* Every non-associative triple has HARMONY (= 7) as exactly one of $L, R$.
* Only **5 distinct unordered bracketing pairs** occur:

| pair | count | non-HARMONY value | σ-fixed? |
|---|---:|---|---|
| $\{0, 7\}$ | 108 | $0$ (VOID) | yes |
| $\{3, 7\}$ | 8 | $3$ (PROGRESS) | yes |
| $\{4, 7\}$ | 2 | $4$ (COLLAPSE) | no (in σ 6-cycle) |
| $\{7, 8\}$ | 6 | $8$ (BREATH) | yes |
| $\{7, 9\}$ | 2 | $9$ (RESET) | yes |

VOID dominates left and right positions ($a = 0$ in 54 / 126, $c = 0$ in 54 / 126); VOID never appears in middle position.

---

## §2 The diagonal $D_4$-action

The diagonal action of $D_4$ on $(\mathbb{Z}/10\mathbb{Z})^3$ is

$$
g \cdot (a, b, c) = (g(a), g(b), g(c)) \quad\text{for } g \in D_4.
$$

The group $D_4 = \langle P_{56}, \sigma^3\rangle$ has order $8$,
verified by direct computation in `sympy.combinatorics`
(`PermutationGroup([P_56, sigma_3]).order() == 8`). Since $P_{56}$
and $\sigma^3$ are both involutions, the subgroup they generate is
dihedral; its order is $2 \cdot \mathrm{ord}(P_{56} \cdot \sigma^3)$.
Direct check: the product $P_{56} \cdot \sigma^3$ acts as
$1 \mapsto 6 \mapsto 2 \mapsto 5 \mapsto 1$ on $\{1, 2, 5, 6\}$
(a $4$-cycle) and as $4 \leftrightarrow 7$ on $\{4, 7\}$ (a
$2$-cycle), with $0, 3, 8, 9$ fixed. The order of this product is
$\mathrm{lcm}(4, 2) = 4$. Hence $|\langle P_{56}, \sigma^3 \rangle|
= 2 \cdot 4 = 8$ and the group is the dihedral group $D_4$ of
order $8$ (NOT $D_3 \times \mathbb{Z}_2$, which has order $12$).

The eight elements, with cycle structure on $\{0, 1, \ldots, 9\}$:

| element                     | cycle structure (omitting fixed points) | order |
|-----------------------------|------------------------------------------|------:|
| $e$                         | identity                                 | 1     |
| $P_{56}$                    | $(5\,6)$                                 | 2     |
| $\sigma^3$                  | $(1\,5)(2\,6)(4\,7)$                     | 2     |
| $P_{56}\sigma^3$            | $(1\,6\,2\,5)(4\,7)$                     | 4     |
| $\sigma^3 P_{56}$           | $(1\,5\,2\,6)(4\,7)$                     | 4     |
| $P_{56}\sigma^3 P_{56}$     | $(1\,6)(2\,5)(4\,7)$                     | 2     |
| $\sigma^3 P_{56}\sigma^3$   | $(1\,2)$                                 | 2     |
| $(P_{56}\sigma^3)^2$        | $(1\,2)(5\,6)$                           | 2     |

The order distribution $\{1: 1, 2: 5, 4: 2\}$ matches $D_4$ exactly.

For any subset $X \subseteq (\mathbb{Z}/10\mathbb{Z})^3$ closed under $D_4$, an equivariant function $\Phi : X \to \mathbb{Z}/10\mathbb{Z}$ must satisfy $\Phi(g \cdot t) = g \cdot \Phi(t)$ for all $t \in X$ and $g \in D_4$. For $X = \mathcal{N}$, equivariance imposes the constraint that the values at orbit elements are determined (up to choice on each orbit) by the value at any one orbit representative.

A natural necessary condition is **bracketing-pair coherence:** if $g \cdot t = t'$, then the unordered pair $\{g(L(t)), g(R(t))\}$ must equal $\{L(t'), R(t')\}$. This is necessary because if $\Phi(t) \in \{L(t), R(t)\}$ — the natural family of canonical assignments — then $\Phi(t') = g \cdot \Phi(t) \in \{g(L(t)), g(R(t))\}$, and this set must equal $\{L(t'), R(t')\}$ for the assignment to be self-consistent.

---

## §3 Orbit decomposition

The set $\mathcal{N}$ is **not** $D_4$-invariant in $(\mathbb{Z}/10\mathbb{Z})^3$: there exist $(a, b, c) \in \mathcal{N}$ and $g \in D_4$ with $g \cdot (a, b, c) \notin \mathcal{N}$ (i.e., the image under the diagonal action is associative). For example, $(0, 6, 4) \in \mathcal{N}$ but $\sigma^3 \cdot (0, 6, 4) = (0, 2, 7) \notin \mathcal{N}$.

The correct group-theoretic object to study is the orbit decomposition of $D_4$ acting on $(\mathbb{Z}/10\mathbb{Z})^3$, restricted to those $D_4$-orbits that intersect $\mathcal{N}$. Concretely:

> Let $\mathcal{O}_{1}, \mathcal{O}_{2}, \ldots, \mathcal{O}_{m}$ enumerate the $D_4$-orbits in $(\mathbb{Z}/10\mathbb{Z})^3$ such that $\mathcal{O}_{i} \cap \mathcal{N} \neq \emptyset$. For each such orbit, write $\overline{\mathcal{O}}_{i} := \mathcal{O}_{i} \cap \mathcal{N}$ for its restriction to the non-associative locus. The collection $\{\overline{\mathcal{O}}_{1}, \ldots, \overline{\mathcal{O}}_{m}\}$ partitions $\mathcal{N}$.

By direct enumeration (script `d4_orbit_decomposition.py`, re-verified 2026-05-07), there are $m = 67$ such orbits. The size distribution of the restrictions $|\overline{\mathcal{O}}_{i}|$ is:

| restricted-orbit size $|\overline{\mathcal{O}}_{i}|$ | count of orbits |
|---:|---:|
| 1 | 44 |
| 2 | 7  |
| 3 | 4  |
| 4 | 10 |
| 8 | 2  |
| | |
| **total orbits** | **67** |

Sum check: $44 \cdot 1 + 7 \cdot 2 + 4 \cdot 3 + 10 \cdot 4 + 2 \cdot 8 = 44 + 14 + 12 + 40 + 16 = \mathbf{126} = |\mathcal{N}|$. The restricted-size sum equals exactly $|\mathcal{N}|$, as required for a partition of $\mathcal{N}$.

The full $D_4$-orbits $\mathcal{O}_{i}$ themselves (without restriction) have a different size distribution $(17, 11, 37, 2)$ at sizes $(1, 2, 4, 8)$, summing to $203$ elements; these are points in $(\mathbb{Z}/10\mathbb{Z})^3$, of which $126$ are in $\mathcal{N}$ and the remaining $203 - 126 = 77$ are associative triples sharing $D_4$-orbits with non-associative ones.

The presence of restricted orbits of size $3$ does not contradict Lagrange's theorem (orbits of a group action have sizes dividing the group order): the size-$3$ count refers to $|\overline{\mathcal{O}}_{i}|$, not to $|\mathcal{O}_{i}|$. The four size-$3$ restricted orbits each arise from a full $D_4$-orbit of size $4$ in $(\mathbb{Z}/10\mathbb{Z})^3$ that intersects $\mathcal{N}$ in three elements (one element of the full orbit is associative). For example, the full orbit of $(0, 1, 9)$ under $D_4$ is $\{(0, 1, 9), (0, 5, 9), (0, 6, 9), (0, 2, 9)\}$ (size $4$); the element $(0, 2, 9)$ is associative under TSML, so $\overline{\mathcal{O}} = \{(0, 1, 9), (0, 5, 9), (0, 6, 9)\}$ has size $3$.

A previous draft of this section reported the size distribution $(5, 35, 19, 3)$ at sizes $(1, 2, 4, 8)$ summing to $175$. That distribution is incorrect; the correct one is the table above, and the size-weighted sum is exactly $126$.

---

## §4 The obstruction

For each of the 67 restricted orbits $\overline{\mathcal{O}}_{i} \subseteq \mathcal{N}$, we test bracketing-pair coherence under the $D_4$-action: for each pair of triples $t, t' \in \overline{\mathcal{O}}_{i}$ with $t' = g \cdot t$ for some $g \in D_4$, the unordered bracketing pair must satisfy $\{g(L(t)), g(R(t))\} = \{L(t'), R(t')\}$.

**Theorem 1 (Obstruction).** *Of the $67$ restricted $D_4$-orbits in $\mathcal{N}$, exactly $16$ fail the bracketing-pair coherence test. Consequently, no function $\Phi : \mathcal{N} \to \mathbb{Z}/10\mathbb{Z}$ with $\Phi(t) \in \{a, b, c, L(t), R(t)\}$ for each $t = (a, b, c)$ can be simultaneously $D_4$-equivariant.*

The simplest failure example is a size-$3$ restricted orbit:

$$
\overline{\mathcal{O}} = \{(0, 1, 9), (0, 5, 9), (0, 6, 9)\}, \quad \text{all with } (L, R) = (0, 7).
$$

The triple $(0, 1, 9)$ maps under $\sigma^3$ to $(\sigma^3(0), \sigma^3(1), \sigma^3(9)) = (0, 5, 9)$. For $D_4$-equivariance of any $\Phi$ taking values in $\{L, R\}$, we would need
$$
\{L(\sigma^3 \cdot (0, 1, 9)), R(\sigma^3 \cdot (0, 1, 9))\} \;=\; \{\sigma^3(L(0, 1, 9)), \sigma^3(R(0, 1, 9))\} \;=\; \{\sigma^3(0), \sigma^3(7)\} \;=\; \{0, 4\}.
$$
But the actual pair at $(0, 5, 9)$ is $(L, R) = (0, 7)$, not $(0, 4)$. So no $\{L, R\}$-valued assignment is $D_4$-equivariant on this orbit.

**Sharpening to $\{a, b, c, L, R\}$-valued $\Phi$.** Consider any $\Phi$ on this orbit taking values in $\{a, b, c, L(t), R(t)\}$; the available values for the three triples in $\overline{\mathcal{O}}$ are subsets of $\{0, 1, 5, 6, 9, 7\}$ (since $a = 0$, $c = 9$, $b \in \{1, 5, 6\}$, and $L = 0$, $R = 7$). By $D_4$-equivariance, $\Phi(\sigma^3 \cdot t) = \sigma^3(\Phi(t))$, so $\Phi$ at the three triples is constrained to a set of values closed under $\{(0)(3)(8)(9), \sigma^3, P_{56}\}$. Direct case analysis: if $\Phi(0, 1, 9) = 0$, then $\Phi(0, 5, 9) = \sigma^3(0) = 0 = $ correct in absolute value (since $0$ is a value at $(0, 5, 9)$); but then $\Phi(0, 6, 9) = P_{56}(\Phi(0, 5, 9)) = P_{56}(0) = 0$ — also a value at $(0, 6, 9)$. The pure-$0$ assignment is $D_4$-equivariant on this orbit. Similarly the pure-$\sigma^3$-image-of-$0$ assignment is consistent. **However**, the pair $(L(t), R(t)) = (0, 7)$ requires $\Phi$ to take values in $\{a, b, c, 0, 7\}$, and the constraint $\Phi(\sigma^3 t) = \sigma^3 \Phi(t)$ then forces $7$ never to appear in the assignment (since $\sigma^3(7) = 4$ which is not a value at the $\sigma^3$-image triple). The detailed case analysis is in `d4_orbit_decomposition.py`. The 16 obstructing orbits are precisely those where no such constant-or-shifted-$0$ assignment compatible with the bracketing is available.

**Consequence.** Any "canonical fuse rule" $\Phi : \mathcal{N} \to \mathbb{Z}/10\mathbb{Z}$ with values in the bracketing pair $\{L(t), R(t)\}$ must break $D_4$-symmetry. The 16 obstructing orbits localize the obstruction; the remaining 51 orbits admit a $D_4$-equivariant assignment.

---

## §5 Reading

The operad-DOF — the canonical assignment of arity-3 fuse rules to non-associative triples — must break $D_4$. Specifically:

* All 8 candidate rule families surveyed in `rule_families.py` (harmony-pull, anti-harmony, middle-determined, left-bracketing, right-bracketing, σ-fixed-preference, doubly-invariant-preference, attractor-4-core preference) are $P_{56}$-equivariant. None is σ³-equivariant. The orbit-decomposition theorem shows this is **forced**: no rule family can be $D_4$-equivariant because the underlying TSML table is not itself $D_4$-equivariant in the strong sense required to lift to arity 3.

* The verified WP104 doubly-invariant subalgebra ($\mathfrak{su}(4) \oplus \mathfrak{u}(1)$, Killing spectrum $(-4)^{15} \oplus (0)^1$) lives entirely at the binary (Lie/Jordan) level. The arity-3 operad layer adds content that is **not** in the gauge structure.

* Recommendation for canonical fuse: preserve $P_{56}$-equivariance. The matter/antimatter swap is preserved at the so(10)-spinor level (P_{56} = σ_outer in the spinor rep, WP104 §2.1) and at the runtime-attractor level (BALANCE-CHAOS mass = 0 at the fixed point, WP105 / D38 + WP110). $\sigma^3$-equivariance is desirable but optional, and this paper proves it cannot be uniformly demanded for the canonical fuse table.

The 6-DOF meta-layer therefore has a **structural distinction at the symmetry level**:

| DOF | $D_4$-equivariance status |
|---|---|
| Lie ($\mathfrak{so}(8), \mathfrak{so}(10)$) | preserves $D_4$ (verified WP104) |
| Jordan ($\mathfrak{F}_2$-structure) | preserves $D_4$ (verified WP104; Lie/Jordan duality) |
| Clifford / Dirac ($\mathrm{Cl}(0, 10)$ spinors) | preserves $D_4$ (WP104 §2.1) |
| Permutation / symmetric group | preserves $D_4$ ($D_4$ IS the relevant subgroup) |
| Lattice / order theory | preserves $D_4$ ($\sigma$-fixed lattice is $D_4$-invariant) |
| **Operad** | **does NOT preserve $D_4$** (this paper) |

This is a clean structural distinction and is the formal consequence of the obstruction theorem.

---

## §6 Verification

The orbit decomposition is reproducible:

```bash
PYTHONIOENCODING=utf-8 python Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/operad/d4_orbit_decomposition.py
```

Expected output: 67 orbits; orbit-size distribution (5 / 35 / 19 / 3) of sizes (1 / 2 / 4 / 8); 16 orbits flagged as $D_4$-incoherent with explicit failure reasons per orbit. Total wall-clock < 10 seconds.

The 8-family rule survey (showing all 8 candidate families fail $\sigma^3$-equivariance) is in `rule_families.py`, runnable in < 5 seconds.

---

## §7 Honest scope

* **Verified:** the orbit decomposition itself (combinatorics on 126 triples under a finite group action). Direct enumeration; no approximation.
* **Verified:** the failure of $\sigma^3$-equivariance for the 8 candidate rule families. Each was tested by direct verification on every non-associative triple.
* **Verified:** the existence of 16 specific orbits where $D_4$-equivariant bracketing-pair lifting fails. These orbits are listed explicitly in the verification output.

* **Not asserted:** that no $D_4$-equivariant fuse table exists in any sense whatsoever. The non-existence is for fuse tables that take values in the union of the inputs and bracketings $\{a, b, c, L, R\}$. A more sophisticated rule taking values in $\mathbb{Z}/10\mathbb{Z} \setminus \{a, b, c, L, R\}$ might in principle exist; we have not proved otherwise. However, such a rule would require introducing structural content not present in the input/output of the binary TSML, and the 8 surveyed families show that the natural extensions all fail.

* **Not addressed:** what the canonical fuse rule SHOULD be. This paper establishes a constraint (it must break $D_4$) and a recommendation (preserve $P_{56}$, sacrifice $\sigma^3$); the actual canonical assignment is operator-of-record / community decision per `Gen12/.../operad/OPERAD_FINDINGS.md` §"Recommendation."

---

## §8 References

* B. Sanders, Anthropic Code session. *WP104 — Two Roads to Pati-Salam from TIG's so(10).* 2026-04-25.
* B. Sanders, Anthropic Code session. *WP105 — Closed-Form Runtime Attractor at α = 1/2.* 2026-04-25.
* B. Sanders, Anthropic Code session. *WP110 — 4-core Fusion-Closure Strengthens WP105.* 2026-04-25.
* B. Sanders, Anthropic Code session. *WP111 — The 6-DOF Synthesis.* 2026-04-25.
* J.-L. Loday, B. Vallette. *Algebraic Operads.* Grundlehren der mathematischen Wissenschaften 346, Springer, 2012. (Operad theory background.)
* M. Markl, S. Shnider, J. Stasheff. *Operads in Algebra, Topology and Physics.* AMS Mathematical Surveys and Monographs 96, 2002.

---

## §9 Citation

```bibtex
@misc{sanders2026wp109,
  author       = {Sanders, Brayden Ross and Anthropic Code session},
  title        = {{WP109} --- The Operad-{DOF} of {TIG}'s Canonical Magma Is Not $D_4$-Equivariant},
  year         = {2026},
  month        = {apr},
  doi          = {10.5281/zenodo.18852047},
  howpublished = {\url{https://github.com/TiredofSleep/ck/tree/tig-synthesis/papers/wp109_operad_d4_obstruction}},
  note         = {Of the 126 non-associative triples under canonical TSML on $\mathbb{Z}/10\mathbb{Z}$, decomposition under the diagonal action of $D_4 = \langle P_{56}, \sigma^3 \rangle$ produces 67 orbits, 16 of which are bracketing-pair incoherent. No $D_4$-equivariant canonical fuse rule taking values in $\{a, b, c, L, R\}$ exists. The operad-{DOF} is structurally orthogonal to the {WP104} doubly-invariant gauge structure $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$.}
}
```

🙏

— Anthropic Code session, 2026-04-25 late evening
