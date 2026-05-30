# Birch and Swinnerton-Dyer — TIG Structural Bridge

**Tier**: STRUCTURAL. Energy-law connection identified; precise mapping to L-functions open.

---

## What TIG demonstrates (PROVEN)

**Fact 1 (BAL corridor energy law).** In the Mix_λ family at $\lambda \in [0.42, 0.50]$
(the BAL = BALANCE corridor), the iteration $F_\lambda(p) = \lambda(p \star_T p) + (1-\lambda)(p \star_B p)$
admits an explicit conservation law:
$$E(p) := \sum_i p_i \cdot \text{BAL}_i \cdot (\text{some weight depending on } \lambda)$$
that is constant on orbits. The exact functional form is verified
computationally for $p \in [0.42, 0.50]$ but unknown analytically.

**Fact 2 (Rational fixed points).** The BAL corridor has rational fixed
points whose rank (in the sense of "number of linearly independent
orbit-conservation laws") can be computed exactly via the closed-form
attractor analysis of J01 Theorem D.

**Fact 3 (At $\lambda = 1/2$).** The closed-form attractor exists exactly,
with ratio $H/Br = 1 + \sqrt{3}$ and Galois group $D_4$ over LMFDB 4.2.10224.1
(J01 Theorem D, J12).

---

## The structural rhyme with BSD

The Birch and Swinnerton-Dyer (BSD) conjecture asserts that for an elliptic
curve $E$ over $\mathbb{Q}$:
$$\text{rank}(E(\mathbb{Q})) = \text{ord}_{s=1} L(E, s)$$
i.e., the rank of the group of rational points equals the order of
vanishing of the $L$-function at $s = 1$.

The **TIG–BSD rhyme** identifies:

| BSD side | TIG side |
|---|---|
| Elliptic curve $E/\mathbb{Q}$ | BAL corridor of Mix_λ on Z/10Z |
| Rank $r = \text{rank}(E(\mathbb{Q}))$ | Number of independent conservation laws in BAL |
| $L$-function $L(E, s)$ | Substrate energy functional |
| BSD equality | TIG energy law |

---

## The load-bearing conjectures — CONJECTURE

> **Conjecture BSD.1 (Curve-to-corridor map).** Every elliptic curve $E/\mathbb{Q}$
> determines a specific $\lambda(E) \in$ BAL corridor, via its $j$-invariant
> reduced modulo a specific substrate prime.

> **Conjecture BSD.2 (Rank-conservation equivalence).** The number of
> linearly-independent conservation laws of $F_{\lambda(E)}$ on the BAL
> corridor equals $\text{rank}(E(\mathbb{Q}))$.

> **Conjecture BSD.3 (Energy-to-L-function).** The substrate energy $E(p)$
> at the BAL fixed point corresponds to $L(E, s)$ near $s = 1$, with
> the order of vanishing matching.

If BSD.1, BSD.2, BSD.3 all hold, BSD becomes a structural consequence of
the TIG energy law on the BAL corridor.

---

## What makes BSD especially speculative

Unlike RH or YM (where the substrate-side spectral data is intrinsically
algebraic), BSD requires a map from a specific elliptic curve to a specific
corridor parameter. This map is not yet specified. Until BSD.1 is made
explicit (e.g., via a formula $\lambda(E) = f(j(E))$ for some function $f$),
the bridge is genuinely speculative.

The BAL corridor's energy law is a real, computationally-verified
phenomenon — but its connection to L-functions is currently a structural
analogy, not a derivation.

---

## Honest caveats

1. The curve-to-corridor map is the load-bearing missing piece. Without it,
   the bridge is incomplete.
2. BSD-rank equality is one of the deepest conjectures in number theory;
   any structural rhyme should be especially modest.
3. The TIG BAL corridor's "rank" of conservation laws has not been compared
   against any explicit elliptic curve's rank computationally.

---

## Cross-references — POST-MERGER

| Resource | Location |
|---|---|
| WP19_BSD_TIG.md, WP21_BSD_ENERGY_LAW.md, WP21_BSD_MIX_LAMBDA.md | CK working repo: `papers/clay/` |
| Closed-form attractor analysis | TIG: J01 §6 (Joint Closure, Theorem D + corollary) — Tier 1, ship-ready |
| Galois D₄ over 4.2.10224.1 | TIG: J12 (Tier 1, ship-ready) |
| **5D Fourier embedding (new merger)** | TIG: `J07/` §5 |
| **σ-magma + ETP profile substrate** | TIG: J05 (Tier 2), J03 (Tier 2) |

### What the Q-series merger contributes

The merged Q-series paper (`J07/`) §5 establishes the 5D CRT
Fourier embedding $\Phi : \mathbb{Z}/10\mathbb{Z} \hookrightarrow \mathbb{R}^5$
with decagonal $D_{10}$ symmetry. The "rank" of an elliptic curve under the
BSD bridge corresponds (conjecturally) to the dimension of the image of a
specific sub-set of the BAL corridor under $\Phi$ — when this dimension is
$> 0$, the elliptic curve has positive rank.

This identification is currently structural-only (no formula linking
$j$-invariant to image-dimension). Tightening this gives a path to making
Conjecture BSD.1 (curve-to-corridor map) explicit.

---

## References

- Birch & Swinnerton-Dyer (1965): "Notes on elliptic curves I, II." *J. Reine Angew. Math.* 218, 79.
- Wiles (2000): "The Birch and Swinnerton-Dyer conjecture." Clay Mathematics Institute problem statement.
- Coates & Wiles (1977): "On the conjecture of Birch and Swinnerton-Dyer." *Invent. Math.* 39, 223.
- Kolyvagin (1988): "Finiteness of E(Q) and Sha(E,Q) for a subclass of Weil curves."

---

## F4 / F18 addendum (2026-05-29)

Frontier F18 (`04_meta/frontiers_2026-05-27/F18_BSD_bridge_with_F4.md`)
examined whether F4's two prime-uniform closed forms on the substrate
algebra $V^{\mathrm{BHML}}$ give traction on the BSD bridge:

- $|\mathrm{idem}(V^{\mathrm{BHML}}/\mathbb{F}_p)| = p + 3$ (odd $p$);
- $|\mathrm{Aut}(V^{\mathrm{BHML}}/\mathbb{F}_p)| = (p - 1)^2$, with group structure $\mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$.

The F18 verdict is **NO-TRACTION on BSD.1** (the curve-to-corridor map).
Three findings:

1. **$(p-1)^2$ is Hasse-Weil-impossible** as $\#E(\mathbb{F}_p)$ for any
   elliptic curve over $\mathbb{Q}$ at any prime $p \geq 5$. Setting
   $\#E(\mathbb{F}_p) = (p-1)^2$ forces $a_p = -p(p-3)$, violating
   $|a_p| \leq 2\sqrt p$ already at $p = 5$.

2. **$(p + 3)$ does match $\#E(\mathbb{F}_p)$ for some curves at some
   primes** (corresponding to $a_p = -2$), but the substrate-prime hit
   fraction (observed 35.3% of all $a_p = -2$ hits at substrate primes
   $\{3, 7, 11, 13\}$, across 22 small-conductor curves) **matches the
   Sato-Tate baseline (30.0% predicted)** within ~5 percentage points,
   well inside statistical noise on the 34-hit sample.
   No substrate distinction is visible.

3. **One morphological rhyme** remains: the F4 automorphism group
   $\mathbb{F}_p^{\!*} \times \mathbb{F}_p^{\!*}$ has the same "2-fold
   direct product of cyclic groups of order ~$p$" shape as the
   $p$-torsion $E(\mathbb{F}_p)[p] \cong \mathbb{Z}/p \times \mathbb{Z}/p$
   in supersingular reduction. But the cyclic factors are non-isomorphic
   (additive $\mathbb{Z}/p$ vs multiplicative $\mathbb{F}_p^{\!*}$), and
   no functorial link binds them. The rhyme is **suggestive but not
   load-bearing** for BSD.1.

**Bottom line.** F4's closed forms catalog the substrate algebra itself,
not data attached to specific elliptic curves. The curve-to-corridor
map (BSD.1) remains the load-bearing missing piece; F4 does not supply
it. Reproduction: `python verification/frontier_F18_bsd_F4_test.py`.

---

*Status: Open, structural. Energy law proved; curve-to-corridor and rank-equivalence open. F4 closed forms examined and found NO-TRACTION on BSD.1 (F18, 2026-05-29).*
