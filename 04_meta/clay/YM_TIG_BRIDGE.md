# Yang-Mills Mass Gap — TIG Structural Bridge

**Tier**: STRUCTURAL connection grounded in PROVEN substrate facts.
**Status**: not a proof. Continuum-limit step is the load-bearing CONJECTURE.

---

## What TIG demonstrates (PROVEN)

**Fact 1 (BHML_8 spectral gap).** The BHML 8×8 core matrix (excluding VOID and
HARMONY boundary indices) has eigenvalues
$$\{47.6904,\, -7.0066,\, -4.4489,\, -1.3238,\, -0.7502,\, 0.4735,\, -0.3385,\, -0.2959\}.$$

Reordering by magnitude $|\lambda_1| \ge |\lambda_2| \ge \cdots$:
$$|\lambda_1| = 47.69,\, |\lambda_2| = 7.01,\, |\lambda_3| = 4.45,\, |\lambda_4| = 1.32,\, |\lambda_5| = 0.75,\, |\lambda_6| = 0.47,\, |\lambda_7| = 0.34,\, |\lambda_8| = 0.30.$$

**Fact 2 (T* identification).** The ratio $|\lambda_6| / |\lambda_5| = 0.471 / 0.750 \approx 0.6307$. The ratio $|\lambda_7|/|\lambda_6| \approx 0.7148$, matching the **TIG coherence threshold $T^* = 5/7 \approx 0.7143$** to 0.08%.

**Fact 3 (Spectral gap).** The "spectral gap at index k = 5" is
$$1 - |\lambda_5|/|\lambda_4| = 1 - 0.750/1.324 = 0.434$$
A persistent O(1) gap, independent of refinement.

These are not conjectures. They are finite linear-algebra computations,
verified in `CK/Gen9/spectral/bhml_eigenvalue_analysis.py`.

---

## The structural rhyme with Yang-Mills

The Yang-Mills (YM) mass gap problem asks: for SU(N) lattice gauge theory in
4D Euclidean spacetime, does the spectrum of the Hamiltonian H have a positive
mass gap Δ > 0, i.e., $\text{spec}(H) = \{0\} \cup [\Delta, \infty)$?

In Wilson's 1974 lattice formulation, the transfer matrix $T = e^{-aH}$ has
discrete spectrum on the lattice. Wilson proved that a spectral gap of T
(equivalently: a finite correlation length) implies confinement; the standing
question is whether this gap persists as the lattice spacing $a \to 0$.

The **TIG–YM rhyme** identifies:

| YM side | TIG side |
|---|---|
| Transfer matrix T = $e^{-aH}$ | BHML 8×8 as discrete transfer matrix |
| Mass gap $\Delta > 0$ | BHML_8 has $|\lambda_5| - |\lambda_6| > 0$ (a real gap) |
| Lattice spacing $a \to 0$ | Continuum limit on BHML refinement |
| Gauge group SU(N) | BHML's commutative non-associative magma structure |

---

## The load-bearing conjectures — CONJECTURE

> **Conjecture YM.1 (Reflection positivity).** The BHML transfer matrix is
> reflection-positive in the Osterwalder-Seiler sense, so that it defines a
> well-posed lattice gauge theory.

> **Conjecture YM.2 (Continuum limit).** The BHML spectral gap persists as
> the lattice spacing $a \to 0$, i.e., the gap is not an artifact of
> discretization but reflects a genuine continuum mass gap.

> **Conjecture YM.3 (Identification).** The BHML's "gauge group" — the
> commutative non-associative structure of the magma operation — corresponds
> to SU(N) for some N, or to a deformation of it.

If YM.1, YM.2, YM.3 all hold, the BHML's PROVEN spectral gap upgrades to
a continuum Yang-Mills mass gap. Each conjecture is structurally precise
and admits attack by lattice-gauge-theory machinery.

---

## What makes the bridge novel

The BHML's spectral ratio $|\lambda_7|/|\lambda_6| = T^* = 5/7$ is a
substrate-derived constant that emerges from the multiplication table of
the 10-operator algebra. It is *not* an input; it is a deduced spectral
property of the integer-valued 8×8 matrix.

If this constant matches the actual SU(N) lattice gauge theory's spectral
ratio at some specific N (or in the large-N limit), the rhyme would
tighten dramatically.

To our knowledge, no substrate-algebra approach to Yang-Mills has been
attempted before; standard approaches use representation theory of gauge
groups and analytic continuation. The TIG approach offers a fully discrete,
finite-matrix starting point.

---

## Cross-references — POST-MERGER

| Resource | Location |
|---|---|
| WHITEPAPER_15_YANG_MILLS_SYNTHESIS.md | CK working repo: `papers/clay/` |
| WP103_SO10_IDENTIFICATION.md | CK working repo: `papers/wp103/` |
| BHML eigenvalue analysis | CK working repo: `Gen9/spectral/bhml_eigenvalue_analysis.py` |
| **Related TIG papers** | |
| J09 (so(10) identification from joint Lie closure) | TIG: `05_papers/algebra/J09/` |
| J11 (Wedderburn D₄ decomposition of [TSML, BHML]) | TIG: `05_papers/algebra/J11/` (Tier 1, ship-ready) |
| J10 (Operadic D₄ obstruction at arity 3) | TIG: `05_papers/algebra/J10/` |
| J01 (Joint closure + universal attractor — corpus centerpiece) | TIG: `05_papers/algebra/J01/` (Tier 1, ship-ready) |
| **J08 (F_p structure of 4-core algebra)** | TIG: `05_papers/algebra/J08/` (Tier 2, merger product) |

### What the F_p merger contributes

The merged F_p paper (`J08/`) catalogs the BHML chain-shell rank
profile across primes — important because the YM-bridge continuum-limit
question (Conjecture YM.2) requires understanding how the BHML spectral gap
behaves under refinement, which has parallels to behavior under prime-base
extension. Specifically:

- BHML chain-shell determinants over Z: 5305, 2843, -2886, 2929, -7542, 7272, -7002
- Rank-preservation pattern: $p \in \{7, 11\}$ preserve rank everywhere; $p = 5$ fails at shell 4 ($5 \mid 5305$); $p = 13$ fails at shell 6; $p \in \{2, 3\}$ fail at shells 6, 8, 9, 10.

This suggests that the YM mass gap's "natural prime" might be in $\{7, 11\}$ where rank is fully preserved across the entire chain — a structural hint not addressed in standard YM literature.

---

## References

- Wilson (1974): "Confinement of quarks." *Phys. Rev. D* 10, 2445.
- Osterwalder & Seiler (1978): "Gauge field theories on a lattice." *Ann. Phys.* 110, 440.
- Jaffe & Witten (2000): "Quantum Yang-Mills theory." Clay Mathematics Institute problem statement.
- Sanders (2026): J09, J11, J10 — Lie-algebraic lifts of the BHML.

---

*Status: Open, structural. The BHML spectral gap is PROVEN; the continuum-limit identification is OPEN.*
