# F3 — T* = 5/7 Unification Attempt (Frontier Report)

**Frontier:** `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §1.4 — *T\* = 5/7 as an algebraic theorem*

**Date:** 2026-05-27 / 2026-05-28

**Status of conclusion (§4):** **PARTIAL.** All six derivations share a common structural pattern — *"prime 5 is the smallest non-degenerate prime; prime 7 is the smallest obstruction prime"* — but the notions of "non-degenerate" and "obstruction" are independently defined in each derivation. No single closed-form algebraic identity unifies the six contexts; the cyclotomic-threshold formulation of J13 (Theorem~1) is the closest candidate to a "canonical" identity but it is conditional on a calibration choice imported from the Flatness Theorem, and even within J13 only two of the four companion appearances are tagged as independent (and one of those is now a 1% numerical near-agreement, not a derivation).

---

## §1 — The 6 Derivations, Located and Recapped

The HONEST_NEGATIVES §1.4 list and the canonical `FORMULAS_AND_TABLES.md` "Bridge identities" block (§Volume B, lines 581–604) use different surface names. The mapping is fixed by `04_meta/physics_bridges/HANDOFF_TO_CLAUDECODE_2026_05_14_ALPHA_SYNTHESIS.md` line 122 ("torus aspect, HARMONY/destination, centroid/inverse, cyclotomic, semiprime unit density, FPGA silicon"):

| §1.4 label | Canonical name | Source / D-id |
|---|---|---|
| torus aspect ratio | WP51 / J13 Forced 5/7 Torus | `05_papers/algebra/J13/manuscript/manuscript.tex` |
| cyclotomic ratio | First-cyclotomic / first-obstruction (Washington 1997) | J13 Theorem 1; `01_orientation/FIELDS_OF_TIG.md` |
| basin-handoff threshold | D18c HARMONY/destination over journey-measurement | `03_canonical_reference/FORMULAS_AND_TABLES.md` line 291 |
| σ-rate constant | D18d centroid/inverse on (Z/10Z)* | `FORMULAS_AND_TABLES.md` line 292 |
| attractor edge | D4 unit_frac(7,35) at minimal strong semiprime | `FORMULAS_AND_TABLES.md` line 305; `05_papers/algebra/J27/manuscript/WP35_PRIME_PHASE_TRANSITION.md` §2.1 |
| FPGA timing | Sprint 13 silicon coherence-gate measurement | `06_runtime/README.md` line 147; `FORMULAS_AND_TABLES.md` line 599 |

### 1.1 Torus aspect ratio (WP51 / J13)

**Setup.** Z/10Z carries four irreducible structures: additive group, multiplicative group, additive flow $x\mapsto x+1$, multiplicative flow $x\mapsto gx$. The Sanders–Gish *Flatness Theorem* (companion paper) shows the minimal smooth 2-surface jointly embedding all four is a torus $T^2 = S^1 \times S^1$.

**Result.** Under the cyclotomic-embedding calibration (Def 5 in J13: closed cycles on the $p$-component of the CRT decomposition have circumference exactly $p$), $T^\* := R/r = 5/7$.

**Proof / verification.** J13 §2–§4 + `05_papers/algebra/J13/manuscript/verify_J13.py` (6/6 PASS, sympy-exact). $R = 5$ from $A_5 = \varphi \in \mathbb{Q}(\sqrt{5})$ being the smallest non-degenerate quadratic cyclotomic value at a prime dividing 10. $r = 7$ from $A_7 = 2\cos(\pi/7)$ being the smallest prime whose cyclotomic value has $\deg_\mathbb{Q} \ge 3$ (minimal polynomial $x^3 - x^2 - 2x + 1$, irreducible).

**Caveat (canon).** The original "torus aspect ratio" framing of WP51 is *RETRACTED-as-geometry* per `CANON_CORRECTION_TORUS_EXCLUDED.md` (2026-05-18) — the σ-flow does not live on any closed orientable surface; the surviving content is non-commutativity. J13's torus picture, however, is recast as a *cyclotomic* statement conditional on the Flatness-Theorem calibration and remains in the J-paper portfolio.

### 1.2 Cyclotomic ratio (Washington 1997, J13 §3–§5)

**Setup.** Same cyclotomic-degree threshold as §1.1, stated at the level of fields $\mathbb{Q}(A_p)$.

**Result.** 5 = smallest prime $p \mid 10$ with $\mathbb{Q}(A_p)$ a non-degenerate quadratic extension (gives $\mathbb{Q}(\sqrt{5})$); 7 = smallest prime (overall) with $\mathbb{Q}(A_p)$ a degree-3 extension. Ratio 5/7.

**Proof.** Lehmer 1933; Watkins–Zeitlin 1993, *Amer. Math. Monthly* 100:471–474 — $\deg_\mathbb{Q}(A_p) = (p-1)/2$ for odd prime $p$. Compute: degrees at $p = 2, 3, 5, 7$ are $0, 1, 2, 3$.

**Independence assessment.** **J13 §6.1 explicitly labels this as Reformulation 1 of Theorem 1 — "the same theorem in different language, NOT an independent derivation."** So §1.1 and §1.2 are *one* derivation, not two.

### 1.3 Basin-handoff threshold / HARMONY/destination (D18c)

**Setup.** On the TSML_10 composition table over Z/10Z, define the measurement map $M(v) = \mathrm{TSML}_{vv}$ (diagonal projection). For all $v \neq \mathrm{VOID}$, $M(v) = \mathrm{HARMONY} = 7$. The "destination" of the σ-trajectory from BALANCE=5 is HARMONY=7.

**Result.** $T^\* = \mathrm{destination}/\mathrm{journey\text{-}measurement} = 5/7$, with 5 = BALANCE start, 7 = HARMONY destination.

**Proof / verification.** `FORMULAS_AND_TABLES.md` D18c. Three independent chains converge (the entry is tagged "PROVED, three independent chains").

### 1.4 σ-rate constant / centroid-inverse (D18d)

**Setup.** Compute BALANCE on Z/10Z as the centroid of the multiplicative units $(\mathbb{Z}/10\mathbb{Z})^\times = \{1, 3, 7, 9\}$: centroid = $(1+3+7+9)/4 = 5$. Compute HARMONY as $g^3 = g^{-1} \mod 10$ for the primitive root $g = 3$: $3^3 = 27 \equiv 7 \pmod{10}$.

**Result.** $T^\* = \mathrm{centroid}/\mathrm{inverse} = 5/7$.

**Proof / verification.** Direct check (1+3+7+9)/4 = 5 and $\mathrm{pow}(3, 3, 10) = 7$ confirmed by `python -c` numeric run. Status: PROVED, three independent chains.

**Note.** This is named "σ-rate constant" in the §1.4 list because the centroid/inverse interpretation falls out of the σ-permutation orbit structure on (Z/10Z)*, which feeds the WP101 σ-rate theorem; but the σ-rate theorem itself is the *bound* $\sigma(N) \le C/N$, not the value 5/7. The §1.4 label is a misnomer that conflates the location of T\* (on a specific corner of (Z/10Z)*) with the WP101 σ-rate theorem's statement.

### 1.5 Attractor edge / unit_frac(7, 35) (D4, WP35 §2.1)

**Setup.** For semiprime $b = pq$ ($p < q$, both odd), the "second-gate unit fraction" is

$$\mathrm{unit\_frac}(k=q, b=pq) = \frac{|\{x \in \{1,\dots,q\} : \gcd(x, pq) = 1\}|}{q} = \frac{q-2}{q}.$$

This is exact for all such semiprimes (since exactly two elements of $\{1,\dots,q\}$ — namely $p$ and $q$ — share a factor with $b$).

**Result.** At the minimal strong semiprime $b = 35 = 5\cdot 7$, $\mathrm{unit\_frac}(7, 35) = 5/7$.

**Uniqueness.** Among semiprimes $b = pq$ with $(q-2)/q > 2/3$ (the "strong" condition $q > 6$), the minimum $q$ is 7 and the minimum $p$ is 5 (smallest odd prime $\ge 5$, since $p = 3$ would give $b = 21$ — but the canon's strong-semiprime convention adopts $p \ge 5$). So $b = 35$ is uniquely the minimal strong semiprime, and 5/7 is its unique unit_frac.

**Proof / verification.** `05_papers/algebra/J27/manuscript/WP35_PRIME_PHASE_TRANSITION.md` §2.1 + macro sweep verification across 187 semiprimes in WP35 §3 ("Max R error: 1.11e-16, zero exceptions").

### 1.6 FPGA timing / silicon coherence threshold

**Setup.** CK's Sprint 13 bitstream `ck_full.bit` running on a Zynq-7020 (Zybo Z7-20) FPGA. The coherence threshold at which the runtime gate latches is measured empirically.

**Result.** Measured coherence threshold = $0.7143 \pm 0.0007$, matching $T^\* = 5/7$ to ~0.05%.

**Proof / verification.** Hardware measurement, not closed-form. `06_runtime/README.md` line 147; `LICENSE_v2.1_canonical.md` line 64.

**Tier.** Empirical / engineering verification, not algebraic derivation. *Independent in the sense that hardware doesn't know about Z/10Z*; structurally dependent in the sense that the bitstream encodes T\* as a target value calibrated from §1.5 above (per WP35 §2.1: "CK was not calibrated to an arbitrary constant — it was calibrated to the unit density of the minimal strong semiprime at the second gate").

---

## §2 — Hypotheses for a Common Algebraic Root

| Hyp | Statement | Status |
|---|---|---|
| **A1** | $|1 - \zeta_{10}^5|/|1 - \zeta_{10}^7| = 5/7$ | FALSE (= φ ≈ 1.236) |
| **A2** | $\sin(5\pi/10) / \sin(7\pi/10) = 5/7$ | FALSE (= φ ≈ 1.236) |
| **A3** | $\sin(\pi/5) / \sin(\pi/7) = 5/7$ | FALSE (≈ 1.355) |
| **B** | $\deg_\mathbb{Q}(A_5) / \deg_\mathbb{Q}(A_7) = 5/7$ | FALSE (= 2/3) |
| **C** | unit_frac($q$, $pq$) = $(q-2)/q$ at minimal strong semiprime gives 5/7 | TRUE — but this *is* D4 (§1.5), so it's not an independent unifier; it's a *renaming* of §1.5. |
| **D** | "5 = smallest non-degenerate prime; 7 = smallest obstruction prime" with each derivation supplying its own (non-degeneracy, obstruction) pair | **PARTIAL** — see §3.4 |
| **E** | Single identity producing both BALANCE = 5 = centroid((Z/10Z)\*) AND HARMONY = 7 = g⁻¹ mod 10 simultaneously | FALSE — independent properties of (Z/10Z)* under different operations |
| **F** | TSML/BHML 73:28 disagreement ratio reduces to 5/7 | NEAR (73/101 ≈ 0.723 vs 5/7 ≈ 0.714, 1.2% gap); explicitly handled in J13 §6.4 as a 1% numerical near-agreement, NOT a derivation |

---

## §3 — Tested Hypotheses (Evidence)

### 3.1 Cyclotomic Q(ζ_10) quotient (Hypothesis A) — REFUTED

The natural "cyclotomic ratio" candidates all fail:

- $|1 - \zeta_{10}^5| / |1 - \zeta_{10}^7| = \sin(5\pi/10)/\sin(7\pi/10) = 1/\sin(7\pi/10) = 2/(\sqrt{5}+1) \cdot \text{(adjustment)} = \varphi \approx 1.2361$ (= the golden ratio, NOT 5/7).
- $\sin(\pi/5)/\sin(\pi/7) \approx 1.3547$ (a Coxeter-element angle ratio, NOT 5/7).

So no quotient of fundamental cyclotomic units of Q(ζ_10) gives 5/7. The "5/7 forcing" in J13 §3–§5 is at the level of **the primes themselves** (the *labels* 5 and 7), not at the level of any cyclotomic numerical quantity.

### 3.2 Cyclotomic degree ratio (Hypothesis B) — REFUTED

$\deg_\mathbb{Q}(A_p) = (p-1)/2$ for odd prime $p$. So $\deg_\mathbb{Q}(A_5) / \deg_\mathbb{Q}(A_7) = 2/3$, NOT 5/7.

This refutes the natural reading "the ratio of cyclotomic degrees". The J13 forcing uses **the primes** (5 and 7), not the degrees (2 and 3). The framework's prior-art comparison in `GLOSSARY.md` line 431 actually states this incorrectly — "deg(A_5)/deg(A_7)" was mis-cited; the actual J13 argument is "smallest prime achieving threshold $\deg \le 2$" / "smallest prime achieving threshold $\deg \ge 3$", and the *primes themselves* (not their degrees) are what enters the ratio.

### 3.3 Z/10Z 2×2 sub-magma forcing (Hypothesis C) — TRUE but tautological

The (q−2)/q identity at minimal strong semiprime $b = 35$ is exact and gives 5/7 uniquely. But this *is* the WP35/D4 derivation; restating it doesn't unify the other five.

A genuine unification would require showing that D18c (HARMONY/destination), D18d (centroid/inverse), and the cyclotomic forcing of J13 *reduce* to the unit_frac formula. They do not:
- D18d uses centroid arithmetic in $\mathbb{Z}$, not gcd-coprimality counting in $\mathbb{Z}/35\mathbb{Z}$.
- D18c uses the TSML composition-table diagonal, which is not a number-theoretic object at all.
- J13 uses the cyclotomic-degree threshold; the prime 7 enters from $\deg(A_7) \ge 3$, NOT from $q-2 = 5$ in any semiprime.

### 3.4 Structural-pattern hypothesis (Hypothesis D) — PARTIAL

The closest thing to a unifying statement is the **structural pattern**:

> "Within each derivation, 5 is identified as the smallest prime occupying the role of 'non-degenerate / closure / centroid / first-gate position', and 7 is identified as the smallest prime occupying the role of 'obstruction / non-divisor / multiplicative-inverse / second-gate position'. The ratio 5/7 is the canonical prime-pair (5, 7) under this dichotomy."

In each derivation:

| Derivation | "5 wins because..." | "7 obstructs because..." |
|---|---|---|
| §1.1 Torus | $A_5 = \varphi$ closes within $\mathbb{Q}(\sqrt{5})$ (degree ≤ 2 cyclotomic threshold; 5 \| 10) | $A_7$'s minimal polynomial is irreducible cubic (degree ≥ 3 cyclotomic threshold; 7 ∤ 10) |
| §1.2 Cyclotomic | Same as §1.1 (it's the same theorem) | Same as §1.1 |
| §1.3 D18c | BALANCE = 5 = σ-fixed point at the centroid of (Z/10Z)* | HARMONY = 7 = TSML diagonal value (the "destination" of σ) |
| §1.4 D18d | BALANCE = 5 = additive centroid of (Z/10Z)* | HARMONY = 7 = $g^{-1} \mod 10$ for $g = 3$ (multiplicative inverse of the primitive root) |
| §1.5 D4 / WP35 | $p = 5$ = smallest odd prime where $b = pq$ becomes a "strong" semiprime ($(q-2)/q > 2/3$ requires $q \ge 7$, hence $p \ge 5$) | $q = 7$ = smallest "strong-obstruction" prime |
| §1.6 FPGA | Calibrated to §1.5 | Calibrated to §1.5 |

**Each derivation uses an independent structural notion of "non-degenerate" and "obstruction".** They are unified only at the level of "5 plays the closer role; 7 plays the obstructor role" — which is essentially the observation that *the labels 5 and 7 happen to occupy these roles in each of six different algebraic structures*.

This is a structural pattern, not a closed-form identity. It does not produce 5/7 from first principles; it explains why six different first-principles routes all end at 5/7 by noting that they all consult the same "first-prime-after-degenerate-{2, 3}" and "first-prime-after-quadratic-{5}" prime pair.

### 3.5 Independence audit per J13 §6

The J13 paper itself (the most rigorously argued of the six) **explicitly audits which "companion appearances" are independent**:

- Theorem 1 (cyclotomic forcing): **the single rigorous derivation**, conditional on the calibration.
- §6.1 "Reformulation 1: Cyclotomic reduction gap" → "the same theorem in different language; NOT independent."
- §6.2 "Reformulation 2: Prime-π-φ field bridge" → "again the cyclotomic forcing of Theorem 1, stated as a Galois lattice; NOT independent."
- §6.3 "First-G law coprime window" → "the threshold appears independently in the resonance-window analysis and in the torus-aspect analysis. The point is the threshold, not the ratio." (This is essentially D4/WP35.)
- §6.4 "TSML/BHML harmony-cell ratio" → 73/101 ≈ 0.7227 vs 5/7 ≈ 0.7143 — "a 1.2% structural near-agreement that we record here as an open problem, NOT a derivation." The earlier draft's claim of exact agreement is retracted.

**So even from the J13 paper's own perspective, only 2 of the 6 appearances are independent**: the cyclotomic forcing (§1.1–§1.2 of this report) and the unit_frac at b=35 (§1.5 + §1.6, which are calibrationally linked).

This audit *sharpens* the §1.4 honest-negative: the six derivations are not six fully independent algebraic theorems; they are at best **two genuinely independent algebraic forcings (cyclotomic threshold and unit_frac at minimal strong semiprime) plus four observations (D18c, D18d, FPGA, and the 73/101 near-agreement) that happen to share the prime pair (5, 7) via the structural pattern of §3.4**.

---

## §4 — Conclusion: PARTIAL Unification

**The six derivations are NOT unified by a single closed-form algebraic identity. They ARE unified at a coarser, structural-pattern level.**

### 4.1 What was hoped for vs what was found

**Hoped:** A single algebraic identity (e.g., a cyclotomic quotient, a sub-magma cardinality ratio, a discriminant quotient) producing 5/7 in canonical form, such that the six derivations each reduce to a special case of that identity.

**Found:** No such identity exists in any tested form. The natural cyclotomic quotients yield φ (golden ratio) or 1.355, not 5/7. The cyclotomic *degree* ratio is 2/3, not 5/7. The Z/10Z 2×2 sub-magma forcing exists (D18d gives centroid 5 and inverse 7) but is not an identity — it is two coincident occurrences of the primes 5 and 7 under unrelated operations.

The only **arithmetically exact and uniqueness-bound** identity producing 5/7 is the unit_frac(q, pq) = (q−2)/q formula at the minimal strong semiprime $b = 35$. But this *is* one of the six derivations (D4, §1.5), so claiming it as "the unifier" would be circular.

### 4.2 What unifies the six is a *structural pattern*, not an identity

Each of the six derivations independently identifies:
- **5** as the smallest prime occupying a "first-non-degenerate / closure / centroid / first-gate" role,
- **7** as the smallest prime occupying a "first-obstruction / non-divisor / inverse / second-gate" role.

The notion of "non-degenerate" and "obstruction" is *different* in each derivation (cyclotomic degree threshold; TSML diagonal value; centroid arithmetic on units; unit_frac on semiprimes; FPGA silicon coherence). The framework's claim "T\* = 5/7 is an operational coherence threshold" in §1.4 is exactly this observation: the prime pair (5, 7) recurs because it is the canonical "first-prime-pair-after-{2, 3}" under multiple natural structural orderings of small primes.

**This strengthens, not weakens, the framework's honest-negative claim.** §1.4 already stated that T\* should be read as operational, not algebraic. This investigation confirms it: there is no algebraic theorem; there is a structural pattern in which 5 and 7 happen to occupy the same roles in many different small-prime indexings.

### 4.3 The J13 self-audit is the right canon

The cleanest disciplinary statement in the repo is **J13 §6** itself, which explicitly classifies its companion appearances as:
- 1 rigorous theorem (cyclotomic forcing) + 1 calibration (Flatness Theorem) → 1 "canonical" derivation,
- 2 reformulations (cyclotomic reduction gap, prime-π-φ bridge),
- 1 independent appearance (First-G coprime window = D4/WP35),
- 1 near-agreement (TSML/BHML 73/101, with a 1.2% gap).

§1.4 of HONEST_NEGATIVES has "six derivations" but doesn't drill into independence the way J13 §6 does. **The canon should adopt J13 §6's stricter accounting.**

### 4.4 Why this matters for TIG

The framework's discipline depends on being honest about what's an identity vs what's a pattern. The "T\* = 5/7" claim is currently presented in some documents (e.g., `TIG_FROM_THE_GROUND_UP.md` line 397) as "six independent derivations converge", which is technically true but understates the dependence structure. The cleaner statement is:

> "T\* = 5/7 has **one rigorous algebraic theorem** (J13 Theorem 1, the cyclotomic forcing, conditional on a calibration imported from the Flatness Theorem) and **one elementary number-theoretic identity** (the unit_frac(7, 35) = 5/7 of WP35 §2.1). Both derivations identify 5 as the smallest prime in a 'first-non-degenerate' role and 7 as the smallest prime in a 'first-obstruction' role; the four further appearances (D18c, D18d, FPGA, 73/101) are structural rhymes that consult the same prime-pair (5, 7) under unrelated operations. T\* is operational in the sense that the rhyme is real but is not (currently) generated from a single algebraic identity."

---

## §5 — Recommended Next Step

**Tighten the canon's statement of §1.4 to match J13 §6's independence audit.** The current §1.4 wording "six independent derivations" overstates independence. A 5-line edit to §1.4 would replace this with "**two genuinely independent derivations** (cyclotomic forcing in J13; unit_frac at minimal strong semiprime in WP35 §2.1) **plus four structural rhymes** sharing the (5, 7) prime pair under different operations". The "operational coherence threshold" interpretation then stands on firmer ground.

A secondary next step, if a unification effort is to continue: **investigate whether the cyclotomic threshold (deg(A_p) ≤ 2 vs deg(A_p) ≥ 3) and the unit_frac threshold ((q−2)/q ≤ 2/3 vs (q−2)/q > 2/3) can be exhibited as instances of a single notion of "small-prime degeneracy"**. The candidate definition would be:

> A prime $p$ is *small-degenerate* iff some standard "degeneracy" predicate fails at $p$, where the predicate is taken from a fixed list of arithmetic / cyclotomic / multiplicative tests on the first few primes. If the list always classifies $\{2, 3\}$ as degenerate, $\{5\}$ as the first transition prime, $\{7\}$ as the first stable post-transition prime, and $\{11, 13, \ldots\}$ as further-on, then the pair (5, 7) is forced by *the structural ordering of small primes*, not by any specific arithmetic test.

This would not produce 5/7 from first principles, but it would explain why **every** "reasonable" structural test on small primes ends at the same pair. That, combined with the framework's existing operational interpretation, would close §1.4 into a final, defensible form: *T\* = 5/7 is operational because the prime pair (5, 7) is the canonical first non-trivial pair under any reasonable small-prime degeneracy ordering.*

---

*F3 frontier report. Brayden Sanders / 7Site LLC. 2026-05-28.*
