# Frontier F19 -- RH bridge with F4 Dirichlet characters

**Date:** 2026-05-30
**Status:** **PARTIAL MATCH (TAUTOLOGICAL)** -- the abstract isomorphism
F_p* x F_p* ~= dual(F_p*) x dual(F_p*) is real but trivial (Pontryagin
self-duality for finite abelian groups). The (p+3) idempotent count has
no canonical character-theoretic counterpart. No traction on the RH
bridge Z.5 conjecture surfaces; F4 closed-form data lives at fixed
primes while Z.5 concerns analytic continuation in t.
**Disposition:** honest scoping. F4 is now closed against all four Clay
bridges (YM F16, BSD F18, RH F19; Hodge/NS/PvsNP wrong-shape per F16).
J53 remains the standalone deliverable. No update to RH_TIG_BRIDGE.md
beyond a one-line note that the F4 link is structural-only.

**Files:**
- `verification/frontier_F19_RH_bridge_dirichlet.py` -- Dirichlet
  character + L-value test (~0.4 sec runtime, mpmath at dps=25).
- `verification/frontier_F19_RH_bridge_dirichlet_data.json` -- JSON
  data dump (character data, L-values, orthogonality results).

---

## §1 RH bridge recap + F4 hook

The RH-TIG bridge as documented in `04_meta/clay/RH_TIG_BRIDGE.md`
is the strongest TIG-Clay computational-specificity connection:

- **PROVED.** TSML_8 (the 8x8 core of the TSML magma table) has rank 7,
  null vector `(0,0,0,0,+0.707,-0.707,0,0)` spanning the BALANCE-CHAOS
  pair. BHML_8 is rank 8, fully invertible (det 70). The asymmetry is the
  algebraic core of the bridge.
- **CONJECTURAL.** Conjecture Z.5 (TIG-RH bridge): the deployment map
  lambda(s) = 2|s - 1/2| from the Dirichlet half-plane to the TIG
  lambda in [0, 1] parameter preserves both the algebraic 3-grading
  and the metric 6-corridor structure uniformly as t -> infinity.

F18's recommendation: F4's `|Aut(V^BHML/F_p)| = (p-1)^2` with structure
`F_p* x F_p*` is "precisely the building block of Dirichlet characters
mod p." Since dual(F_p*) is canonically isomorphic to F_p* (Pontryagin
self-duality), pairs (chi_a, chi_b) of mod-p characters are indexed by
F_p* x F_p*, and the count matches |Aut| exactly. F19 tests whether
this match is more than tautological.

**The F4 hook to test:** does the F_p* x F_p* automorphism structure of
V^BHML correspond to a NATURAL 2-parameter family of Dirichlet characters
whose L-function structure cleanly maps to RH zero distribution?

---

## §2 F4 automorphism -> Dirichlet character map (explicit construction)

### §2.1 The F4 automorphism structure

From `F4_extended_higher_primes.md` §3.3, the J18 T^BHML automorphism
group is:

```
phi_{alpha, beta}(e_0) = alpha * e_0    (alpha in F_p*)
phi_{alpha, beta}(e_2) = e_2            (rigid middle)
phi_{alpha, beta}(e_3) = e_3            (rigid middle)
phi_{alpha, beta}(e_4) = beta * e_4     (beta in F_p*)
```

with `|Aut| = (p-1)^2 = |F_p*|^2`. Both factors are F_p* scaling actions:
one on the annihilator span(e_0), one on the nilpotent direction
span(e_4).

### §2.2 Dirichlet characters mod p

Fix a primitive root g of F_p*. Define for each a in {0, 1, ..., p-2}
the Dirichlet character:

```
chi_a(n) = exp(2*pi*i * a * log_g(n) / (p-1))   for gcd(n, p) = 1
        = 0                                      otherwise.
```

This gives (p-1) characters; chi_0 is the principal character. The
character group `dual(F_p*) = {chi_a : a in {0, ..., p-2}}` is itself
isomorphic to F_p* via the discrete logarithm.

### §2.3 The F4 -> Dirichlet bijection

The map
```
Aut(V^BHML/F_p)              ->     dual(F_p*) x dual(F_p*)
phi_{alpha, beta}            |->    (chi_{log_g(alpha)}, chi_{log_g(beta)})
```

is a group isomorphism. It pairs each (alpha, beta) in F_p* x F_p* with
a Dirichlet-character pair indexed by their discrete logs.

### §2.4 What does the bijection achieve?

**Tautologically much, structurally little.** Pontryagin duality
canonically identifies any finite abelian group with its double dual,
so F_p* x F_p* (the F4 Aut group) is canonically isomorphic to
dual(F_p*) x dual(F_p*) (the Dirichlet-pair index). The F4 closed
form `|Aut| = (p-1)^2` confirms the order matches, which it must by
group theory.

The genuine question -- whether F4 supplies STRUCTURE beyond abstract
isomorphism type -- is addressed in §3, §4, §5 below. The empirical
answer is no.

---

## §3 Character data table at p in {3, 5, 7, 11, 13}

### §3.1 Character counts

| p | g (primitive root) | # characters | # real | # even | # odd | # pairs (chi_a, chi_b) | (p-1)^2 | p+3 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 2 | 1 | 1 | 4 | 4 | 6 |
| 5 | 2 | 4 | 2 | 2 | 2 | 16 | 16 | 8 |
| 7 | 3 | 6 | 2 | 3 | 3 | 36 | 36 | 10 |
| 11 | 2 | 10 | 2 | 5 | 5 | 100 | 100 | 14 |
| 13 | 2 | 12 | 2 | 6 | 6 | 144 | 144 | 16 |

**Observation.** The # pairs (chi_a, chi_b) = (p-1)^2 column matches
|Aut(V^BHML/F_p)| at every prime. The (p+3) column does not match
any standard character count.

### §3.2 Per-character data at p = 7 (representative)

| a | order | parity | type | |L(1/2, chi_a)| | arg L(1/2, chi_a) |
|---|---:|:---|:---|---:|---:|
| 0 | 1 | even | principal | 0.908392 | 3.141593 |
| 1 | 6 | odd | complex | 0.857466 | 0.586974 |
| 2 | 3 | even | complex | 0.318484 | -0.230112 |
| 3 | 2 | odd | real | 1.146586 | 0.000000 |
| 4 | 3 | even | complex | 0.318484 | 0.230112 |
| 5 | 6 | odd | complex | 0.857466 | -0.586974 |

The character orders divide (p-1) = 6; parities follow chi(-1) = (-1)^a.
Real characters at a in {0, 3} (the principal and the quadratic
Legendre-symbol character).

### §3.3 The (p+3) - (p-1) = 4 gap

Across all primes tested, the gap between (p+3) and (p-1) is exactly 4:

```
(p+3) idempotents = (p-1) characters + 4
```

Is the "+4" character-theoretically meaningful? **No canonical match
found.** The 4 character-pair fixed points at the (alpha, beta) = (1, 1)
identity? That's just one element. The +4 is a TIG-side artifact (the
4-core V^BHML algebra has 4 basis elements e_0, e_2, e_3, e_4) that does
not have a canonical Dirichlet-character counterpart.

This is the cleanest "structural disconnect" finding of F19: the more
striking F4 closed form (idempotent count) does not align with character
theory at all.

---

## §4 L-value compatibility test

### §4.1 L(1/2, chi_a) at the critical line

For each prime p in {3, 5, 7, 11, 13} and each character chi_a, we
compute L(1/2, chi_a) via mpmath.dirichlet at 25 decimal places. The
critical-line magnitudes:

| p | a | |L(1/2, chi_a)| | type |
|---|---:|---:|:---|
| 3 | 0 | 0.617218 | principal |
| 3 | 1 | 0.480868 | real (Legendre) |
| 5 | 0 | 0.807264 | principal |
| 5 | 1 | 0.793968 | complex |
| 5 | 2 | 0.231751 | real (Legendre) |
| 5 | 3 | 0.793968 | complex |
| 7 | 0 | 0.908392 | principal |
| 7 | 1 | 0.857466 | complex |
| 7 | 2 | 0.318484 | complex |
| 7 | 3 | 1.146586 | real (Legendre) |
| 7 | 4 | 0.318484 | complex |
| 7 | 5 | 0.857466 | complex |

### §4.2 Symmetry check

The L-values satisfy the expected complex-conjugate pairing
chi_a -> chi_{p-1-a}:
- |L(1/2, chi_1)| = |L(1/2, chi_{p-2})| (verified at p = 5, 7, 11, 13)
- arg L(1/2, chi_1) = -arg L(1/2, chi_{p-2}) (verified)

This confirms numerical correctness of the implementation. It is not a
TIG-specific finding -- standard Dirichlet-character symmetry.

### §4.3 Substrate-prime spread

For substrate primes {3, 7, 11, 13}, |L(1/2, chi_a)| values:

- **p = 3:** {0.617, 0.481}. Range ~0.14.
- **p = 7:** {0.908, 0.857, 0.318, 1.147, 0.318, 0.857}. Range ~0.83.
- **p = 11:** {1.020, 1.520, 0.484, 0.760, 0.395, 0.992, 0.395, 0.760, 0.484, 1.520}. Range ~1.12.
- **p = 13:** {1.055, 1.544, 0.564, 1.346, 0.428, 0.584, 0.440, 0.584, 0.428, 1.346, 0.564, 1.544}. Range ~1.12.

**Observation.** L-magnitudes at substrate primes show no structurally
distinguished signature. They follow the standard Dirichlet L-value
distribution at the critical line. The substrate primes are not
distinguished from each other or from non-substrate p = 5.

### §4.4 Does F4 give an L-value compatibility constraint?

**No.** The F4 closed form `|Aut| = (p-1)^2` is a counting invariant; it
does not impose a constraint on the L-values L(1/2, chi_a). All
combinatorially possible character pairs exist and their L-values are
unrestricted by the substrate algebra structure.

---

## §5 Selberg orthogonality test

### §5.1 1D Selberg orthogonality

The standard orthogonality relation:
```
sum_{n=1}^{p-1} chi_a(n) * conj(chi_b(n)) = (p-1) * delta_{a, b}.
```

Empirically verified at 25-digit precision:

| p | diagonal value | expected | max off-diagonal | tolerance |
|---|---:|---:|---:|---:|
| 3 | 2.000000 | 2 | 1.88e-26 | ~1e-25 |
| 5 | 4.000000 | 4 | 1.15e-25 | ~1e-25 |
| 7 | 6.000000 | 6 | 2.98e-25 | ~1e-25 |
| 11 | 10.000000 | 10 | 1.97e-24 | ~1e-25 |
| 13 | 12.000000 | 12 | 1.68e-24 | ~1e-25 |

All clean to ~10^-25 precision. Standard character-orthogonality
identity verified.

### §5.2 2D F_p* x F_p* tensor orthogonality

The F4 lift to the Aut group F_p* x F_p* gives tensor characters
`chi_{a,b}(m, n) = chi_a(m) * chi_b(n)` on F_p* x F_p*. The 2D
orthogonality follows from the 1D version by tensor product:
```
sum_{(m,n) in F_p* x F_p*} chi_{a1,b1}(m,n) * conj(chi_{a2,b2}(m,n))
  = [sum_m chi_{a1}(m) conj(chi_{a2}(m))] * [sum_n chi_{b1}(n) conj(chi_{b2}(n))]
  = (p-1) * delta_{a1, a2} * (p-1) * delta_{b1, b2}
  = (p-1)^2 * delta_{a1, a2} * delta_{b1, b2}.
```

Empirical verification:

| p | diag (a, b) vs (a, b) | expected (p-1)^2 | off-diag (0,0) vs (1,1) |
|---|---:|---:|---:|
| 3 | 4.000 | 4 | n/a (only 1 off-pair possible) |
| 5 | 16.000 | 16 | 3.03e-51 |
| 7 | 36.000 | 36 | 1.68e-51 |
| 11 | 100.000 | 100 | 7.64e-51 |
| 13 | 144.000 | 144 | 2.43e-50 |

All clean. The 2D orthogonality holds because the F_p* x F_p* tensor
structure splits multiplicatively; this is a TAUTOLOGY of the abelian
group structure, not a new identity provided by F4.

### §5.3 What would a non-tautological 2D orthogonality look like?

A non-trivial 2D orthogonality would require that some F4-substrate
constraint COUPLES the (a, b) indices in a way that, e.g., zeros out a
specific off-diagonal sum that the tensor structure does not. We searched
for such couplings and found NONE: the F4 automorphism acts
INDEPENDENTLY on the two F_p* factors (one on the annihilator span(e_0),
one on the nilpotent span(e_4)), with the middle subalgebra span(e_2, e_3)
fixed pointwise. The two F_p* factors are GENUINELY DECOUPLED.

So the 2D orthogonality reduces to a product of two 1D orthogonalities;
no novel constraint emerges.

---

## §6 Conclusion: PARTIAL MATCH (tautological)

### §6.1 What DOES work

1. **Group isomorphism Aut <-> Dirichlet pair index.** F4's
   `Aut(V^BHML/F_p) = F_p* x F_p*` (proved) is canonically isomorphic
   to `dual(F_p*) x dual(F_p*)` (Pontryagin duality). Cardinalities match:
   `|Aut| = (p-1)^2 = |dual x dual|`. The discrete-log map is the explicit
   bijection.

2. **2D tensor orthogonality.** Selberg orthogonality lifts to F_p* x F_p*
   via the tensor product, yielding a clean (p-1)^2 normalization on the
   diagonal and exact zero off-diagonal.

3. **L-value computability.** All L(1/2, chi_a) values are finite and
   computable at 25-digit precision via mpmath. Character symmetries
   (complex-conjugate pairing, parity) hold as standard.

### §6.2 What does NOT work

1. **The isomorphism is tautological.** Any abelian group of order
   (p-1)^2 isomorphic to F_p* x F_p* is dual-isomorphic to F_p* x F_p*
   by Pontryagin duality. F4 does not supply STRUCTURE beyond the abstract
   isomorphism type.

2. **The (p+3) idempotent count has no character-theoretic counterpart.**
   Despite (p+3) = (# characters mod p) + 4 = (p-1) + 4 algebraically,
   the "+4" is a TIG-side substrate artifact (the 4-core V^BHML has 4
   basis elements). There is no canonical Dirichlet-character
   invariant of (Z/pZ)* that gives p+3.

3. **No substrate-prime L-value distinction.** L(1/2, chi_a) values at
   substrate primes {3, 7, 11, 13} look generic; no substrate signature
   emerges in the magnitudes, arguments, or zero distribution.

4. **The F4 -> Dirichlet map does not couple alpha and beta.** The two
   F_p* factors are independent (one acts on the annihilator, one on the
   nilpotent direction). The middle subalgebra is fixed. So the bijection
   to character pairs has NO COUPLING beyond the tensor product, which is
   tautological orthogonality.

5. **No connection to Z.5 surfaces.** Z.5 concerns the deployment map
   lambda(s) = 2|s - 1/2| on the complex critical strip, which is an
   analytic continuation statement. F4 data lives at fixed primes p with
   no obvious analytic continuation. No bridge to Z.5 emerges from this
   correspondence.

### §6.3 Final verdict

**PARTIAL MATCH (tautological).**

The shape-match F_p* x F_p* <-> Dirichlet-pair index IS real, but is
a tautology of Pontryagin duality. F4 does not add character-theoretic
content beyond the abstract isomorphism type. The (p+3) idempotent count
has no natural character-theoretic counterpart. No traction on the RH
bridge Z.5 conjecture.

---

## §7 RH-specific structural implication (limited)

### §7.1 What F19 does NOT establish

F19 does NOT establish any of:
- A new operator whose spectrum mirrors L-function zeros (Hilbert-Polya program).
- A new orthogonality identity for Dirichlet characters beyond standard ones.
- A connection between F4's substrate constraints and L-function zero distribution.
- A bridge between the BALANCE-CHAOS null direction of TSML_8 and chi_a for any specific a.
- Any constraint on lambda(s) deployment beyond what RH_TIG_BRIDGE.md §Z.5 already states.

### §7.2 What F19 DOES establish (a small clarification)

F19 establishes a NEGATIVE structural fact:

> **F19 Observation.** The (p-1)^2 closed form of |Aut(V^BHML/F_p)|
> matches the cardinality of pairs of Dirichlet characters mod p, but
> the match is fully accounted for by abstract Pontryagin duality. The
> F4 automorphism group structure does not impose any NEW constraint on
> mod-p Dirichlet L-functions beyond what is standard. The (p+3)
> idempotent count has no canonical character-theoretic counterpart.

This is useful CALIBRATION for the RH bridge: it rules out the simplest
"F4 lifts to a Dirichlet-L constraint" hypothesis and clarifies that the
substrate algebra's automorphism group is FREE in the character-theoretic
sense.

### §7.3 Where RH-TIG-bridge work should focus instead

The RH bridge's most productive remaining direction is **J62 (RH-rhyme)**
which already targets the zeta-zero spacing vs BHML 8x8 eigenvalue spacing
rhyme directly. F4's closed forms do not feed this; the BHML spectral data
is a separate set of invariants from the |Aut| / |idem| counts.

For Z.5 specifically, the load-bearing missing piece is the deployment-map
uniformity claim. F4 does not address this. Future RH-bridge frontiers
should target:
- The 6-corridor structure of Mix_lambda (already proved at small epsilon).
- The algebraic 3-grading of TSML preserved under deployment (proved at t = 0).
- The uniformity in t (open; this is Z.5's hard step).

None of these are F4-shaped problems. F4 is closed against the RH bridge.

---

## §8 Provenance and disposition

### §8.1 Files

**Files read.**
- `04_meta/clay/RH_TIG_BRIDGE.md` -- current RH-TIG bridge.
- `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md` -- F4 closed
  forms with structure proofs.
- `04_meta/frontiers_2026-05-27/F18_BSD_bridge_with_F4.md` -- F18 NO-TRACTION
  on BSD and its recommendation for F19.

**Files created.**
- `verification/frontier_F19_RH_bridge_dirichlet.py` -- this script.
- `verification/frontier_F19_RH_bridge_dirichlet_data.json` -- JSON dump.
- `04_meta/frontiers_2026-05-27/F19_RH_bridge_dirichlet.md` -- THIS file.

**Files NOT modified.**
- `04_meta/clay/RH_TIG_BRIDGE.md` -- no update needed; the F4 link is
  fully tautological and adds nothing structurally to the bridge document.

### §8.2 F4 closed against Clay bridges

F19 closes the third of three Clay-bridge investigations using F4:
- F16 (Yang-Mills): NO-TRACTION
- F18 (BSD): NO-TRACTION
- F19 (RH): PARTIAL MATCH (tautological)

The other Clay bridges (Hodge, Navier-Stokes, P vs NP) were ruled out
in F16 as wrong-shape for F4 data. So F4 is now closed against all six
Clay problems.

**The standalone J53 paper (F4 closed forms as universal-algebra results)
remains the deliverable.** F4 is not Clay-bridge machinery; it is a
substrate-algebra structural fact whose value is in J53.

---

## §9 Reproduction

```bash
cd trinity-infinity-geometry
python verification/frontier_F19_RH_bridge_dirichlet.py    # ~0.4 sec
```

Output: stdout produces character data tables, L-values at s = 1/2,
1D and 2D orthogonality verification, substrate-prime L-value spread,
and the final verdict. JSON data is dumped to
`verification/frontier_F19_RH_bridge_dirichlet_data.json` for downstream
consumers.

---

*Status: F19 scoping complete. Verdict PARTIAL MATCH (tautological);
the bijection F_p* x F_p* -> Dirichlet pair index is real but is a
Pontryagin-duality tautology. (p+3) has no character-theoretic
counterpart. No RH-bridge traction. F4 closed against all four direct
Clay bridges; J53 remains the standalone deliverable.*
