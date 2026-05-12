# PREDICTIONS_FEASIBILITY_MAP

## Which physics predictions are computable NOW vs blocked vs external

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Question: Can we chase these calculations or are we blocked or missing something?*
*Sources: this session's computation; META_TIG_AS_PREPHYSICAL_SUBSTRATE §10*
*Locked v1 · 2026-05-08*

---

## §1. Status of Each Prediction

| Prediction | Status | Blocker / Path |
|---|---|---|
| **A** — Cosmological constants from rung structure | EXTERNAL | needs Friedmann fits / cosmology engagement |
| **B** — α⁻¹ analog at higher rungs | PARTIAL ★ | disc tower computed; needs normalization recipe |
| **C** — Yang-Mills emerges at Z/210 | **BLOCKED** | needs composition-table recipe at Z/n |
| **D** — DM/VM/DE as projection ratios | **BLOCKED²** | needs (a) memory traceback (b) recipe |
| **E** — 71 in fundamental ratios | PARTIAL | direct test fails; needs refined formulation |

★ = partially computable now
**bold** = blocked

---

## §2. What Computed Successfully (Prediction B)

The cyclotomic discriminant tower is computable in closed form:

| Rung | $\varphi(n)$ | $|\mathrm{disc}\,\mathbb{Q}(\zeta_n)|$ | Factored |
|:---:|:---:|---|---|
| Z/10 | 4 | 125 | $5^3$ |
| Z/30 | 8 | 1,265,625 | $3^4 \cdot 5^6$ |
| Z/210 | 48 | $\approx 2.6 \cdot 10^{67}$ | $3^{24} \cdot 5^{36} \cdot 7^{40}$ |
| Z/2310 | 480 | $\approx 10^{577}$ | $3^{240} \cdot 5^{360} \cdot 7^{400} \cdot 11^{432}$ |

The Z/10 recipe **137 = disc(Q(ζ₁₀)) + #lines(AG(2, missing_prime))** = 125 + 12 doesn't scale naively:

| Rung | disc | missing prime | #lines AG(2,p) | sum |
|---|---|:---:|---|---|
| Z/10 | 125 | 3 | 12 | **137** ≈ α⁻¹ ✓ |
| Z/30 | 1,265,625 | 7 | 56 | 1,265,681 |
| Z/210 | $\sim 10^{67}$ | 11 | 132 | $\sim 10^{67}$ |

**Scaling problem**: discriminants grow superexponentially, physical constants are $\mathcal{O}(1)$ to $\mathcal{O}(10^4)$. The Z/10 case is "lucky" — small enough discriminant to land in the right magnitude. At higher rungs we'd need a **normalization recipe** (e.g., a logarithm, a quotient by some other tower-quantity, a ratio). Without it, B is computable but the analogs aren't physical.

**This is the open structural question**: is 137's appearance a coincidence at Z/10, or is there a general formula that produces physically meaningful constants at every rung after appropriate normalization?

---

## §3. What Computed Successfully (Prediction E refined)

Direct "71 divides the integer part" test fails for every major fundamental constant:

| Constant | Value | Integer | Mod 71 | Prime factors of int |
|---|---|:---:|:---:|---|
| α⁻¹ | 137.036 | 137 | 66 | 137 (prime) |
| m_p/m_e | 1836.153 | 1836 | 61 | $2^2 \cdot 3^3 \cdot 17$ |
| m_μ/m_e | 206.768 | 206 | 64 | $2 \cdot 103$ |
| m_W (GeV) | 80.379 | 80 | 9 | $2^4 \cdot 5$ |
| **m_Z (GeV)** | 91.188 | **91** | 20 | **7 · 13** ★ |
| **m_H (GeV)** | 125.25 | **125** | 54 | **$5^3$** ★ |
| m_top | 172.69 | 172 | 30 | $2^2 \cdot 43$ |

**Two unexpected pattern-matches surfaced:**

★ **m_H ≈ 125 = 5³ = disc(Q(ζ₁₀))** — the Higgs mass integer part equals the cyclotomic discriminant at Z/10. The Higgs is the field whose VEV breaks electroweak symmetry; canon's $\|\mathrm{VEV}\|^2 = 13/4$ (D33). The numerical match $m_H \to 125 \to 5^3$ is suggestive — the Higgs at the energy of TIG's substrate's algebraic complexity.

★ **m_Z ≈ 91 = 7 · 13 = HARMONY · (wobble prime)** — Z boson mass integer part is the product of TIG's Stratum II prime (7 = HARMONY, attractor) and Stratum III wobble prime (13). The Z is the neutral mediator of weak interactions; its mass involves both attractor and wobble.

**Both are dimensional (depend on choice of GeV as unit)**, so they're not unit-independent. But the *integer-part coincidence in GeV* is striking enough to warrant follow-up. If the same pattern held in MeV, eV, Planck, or other natural units, it would be coincidence; the GeV-specificity suggests *some* scale-setting is involved that happens to land on these substrate-natural integers.

→ **Prediction E should be reformulated**: not "71 divides constants," but "TIG primes (Stratum I-IV) appear in the prime factorization of integer parts of fundamental constants in natural units."

---

## §4. What's Blocked — The Keystone

**Predictions C and D are blocked by ONE missing piece**: the composition-table recipe at arbitrary modulus n.

Currently:
- TSML, BHML, CL_STD are defined ONLY at Z/10 (canon §5, §6, §6.7)
- The 4-bit operator encoding is Z/10-specific (10 ≤ 16 = 2⁴)
- σ-fixed and σ-cycle decompositions are defined at any Z/n (substrate-independent)
- 4-core attractor analog at Z/n is unknown
- Runtime number field at Z/n is unknown (LMFDB 4.2.10224.1 was identified empirically at Z/10)

**Without the recipe, TIG-on-Z/210 doesn't exist as a computable object.** We can't compute "det(BHML at Z/210)" because there's no BHML at Z/210.

### What the recipe needs to specify

1. **Encoding** of n elements as some canonical form (bit-tuples? polynomial residues? CRT components?)
2. **TSML-analog**: commutative magma respecting the CRT structure of Z/n
3. **BHML-analog**: the "becoming" counterpart with non-trivial associativity defect
4. **σ-action**: the Galois-generator-derived permutation (well-defined at any n)
5. **Core attractor**: the σ-fixed set or some derived stable subset
6. **Runtime number field**: the algebraic-geometry analog of LMFDB 4.2.10224.1

Items 1-5 are **combinatorial / algebraic** — tractable in 1-2 weeks of focused work. Item 6 is **harder** — requires algebraic-geometry insight to identify the natural number field associated with a substrate, possibly via Iwasawa / class-field-theoretic methods.

### Why this is the keystone

With the recipe:
- Prediction C unlocks: compute det(BHML_n) at Z/210, check for SU(3)×SU(2)×U(1)
- Prediction D becomes formulatable: define projection from Z/n to Z/10, compute coefficients
- Prediction B gets structural backbone: relate disc-tower terms to recipe-derived quantities
- Prediction E gets refined: TIG primes appear at every rung's recipe output

Without the recipe:
- Only B (disc tower) and a refined E (factor pattern) are computable in isolation
- C and D are entirely blocked
- The "framework" claim is weakened: TIG doesn't actually exist at any rung other than Z/10

---

## §5. What's Blocked by Memory Traceback (Prediction D)

The DM/VM/DE values from prior memory:
- DM (dark matter) = 264/1000 ≈ 26.4%
- VM (visible matter) = 49/1000 = 4.9%
- DE (dark energy) = 687/1000 ≈ 68.7%

Match observation reasonably well (Planck 2018: DM ≈ 26.8%, VM ≈ 4.9%, DE ≈ 68.3%).

**Per BUNDLE_CROSSWALK, these need traceback** — they are memory-grounded, not in canon D1-D99.

The numerator 264 = 8 · 33 = $2^3 \cdot 3 \cdot 11$. Contains wobble prime 11. Contains 8 = $|D_4|$ = TIG runtime symmetry order. Suggestive but not derivative.

**Action**: search prior WPs and canon for the source of 264/1000, 49/1000, 687/1000. Without traceback, D's claim that "these come from substrate projection" can't be tested.

---

## §6. What's External (Prediction A)

Cosmological constants prediction requires:
- Identifying which Friedmann-equation parameters are TIG-derivable
- Solving the cosmological evolution with κ_ξ = 13/(4e) as inflaton coupling
- Comparing predictions to PLANCK / CMB data

This is **outside TIG's algebraic core** — it requires cosmology expertise and observational data engagement. Not blocked by anything internal to TIG; just needs external work or a cosmologist collaborator.

---

## §7. Recommended Sequence (Concrete Plan)

### Quick wins (1-3 days each)

1. **Memory traceback for DM/VM/DE values** — search prior WPs for the derivation of 264/1000, 49/1000, 687/1000. If found, D is half-unblocked. If not found, D needs a derivation from scratch.

2. **Reformulate Prediction E** — define precisely what "TIG primes appear in fundamental constants" means. Test: do constants in natural units (Planck, eV, MeV, GeV) decompose into substrate primes more than chance? Run statistical comparison against random nearby integers.

3. **Investigate m_H = 5³ and m_Z = 7·13 coincidences** — are these unit-independent in any natural framing? Compute m_H, m_Z in eV, Planck, multiple units; check whether the substrate-prime decomposition persists.

### Medium move (1-2 weeks)

4. **Build the composition-table recipe at arbitrary n** — this is the keystone. Specify TSML/BHML construction at Z/30 first (smallest non-trivial primorial), verify properties (commutative, non-associative defect, etc.), then extend to Z/210. This unblocks C and D structurally.

### Larger move (weeks-months)

5. **Identify the runtime number field at Z/30 and Z/210** — likely the hardest piece. Requires algebraic-geometry insight. May involve searching LMFDB for natural extensions of $\mathbb{Q}(\zeta_n)$ with appropriate Galois group.

6. **Friedmann fit for Prediction A** — requires cosmology collaborator.

### Order of operations

For the Sept 11 / Oxford timeline, the right priority is:
- **Quick wins (1-3) first** — give immediate progress and refinement
- **Recipe (4) as the major sprint** — the highest-leverage research move
- **Items (5) and (6) post-Sept 11** — these are full research programs, not pre-deployment items

---

## §8. Compact Take-Home

```
ANSWER: Two computable now, two blocked by ONE keystone, one external.

  COMPUTABLE NOW (with refinement):
    B — disc(Q(ζ_n)) tower in closed form. Needs normalization recipe.
    E — TIG-prime decomposition of constants. Needs refined formulation.
        ★ Surfaced: m_H ≈ 125 = 5³ = disc(Q(ζ_10))
        ★ Surfaced: m_Z ≈ 91 = 7·13 = HARMONY · wobble

  BLOCKED BY KEYSTONE:
    C — Yang-Mills at Z/210
    D — DM/VM/DE projection
    
    Keystone = composition-table recipe at arbitrary n.
    Items 1-5 of recipe are tractable (1-2 weeks).
    Item 6 (runtime number field) is harder.

  EXTERNAL:
    A — cosmological constants. Needs Friedmann fit.

THE KEYSTONE INSIGHT:
  TIG currently exists ONLY at Z/10.
  TSML, BHML, CL_STD are not defined at any other modulus.
  The 'framework' claim hinges on building this recipe.
  WITHOUT it: TIG is one substrate's theory, not a tower's framework.
  WITH it: TIG-on-Z/30, TIG-on-Z/210 become computable; physics
           predictions become testable.

QUICK WINS (immediate):
  1. Memory traceback for DM/VM/DE numbers (1 day)
  2. Reformulate E with statistical test (1-2 days)
  3. Investigate m_H/m_Z coincidences in unit-independent form (1-2 days)

MAJOR MOVE (1-2 weeks):
  4. Build composition-table recipe at Z/30 first, then Z/210.
     This is the highest-leverage research move available.

POST-SEPT-11:
  5. Runtime number field at higher substrates (algebraic geometry)
  6. Friedmann fit for cosmology (collaborator-required)

PRACTICAL: the recipe is the key. Build it, three predictions unblock.
```

---

## §9. Status

- **[CLOSED]** Discriminant tower computed in closed form for Z/10, Z/30, Z/210, Z/2310.
- **[CLOSED]** Direct test of "71 divides fundamental constants" — fails universally.
- **[NEW]** $m_H \approx 125 = 5^3 = \mathrm{disc}(\mathbb{Q}(\zeta_{10}))$ — pattern match worth investigation.
- **[NEW]** $m_Z \approx 91 = 7 \cdot 13$ = HARMONY × wobble — pattern match worth investigation.
- **[OPEN]** Normalization recipe scaling discriminants to physical constants at higher rungs.
- **[BLOCKED]** Composition-table recipe at arbitrary n — the keystone for predictions C and D.
- **[NEEDS TRACEBACK]** DM/VM/DE values 264/1000, 49/1000, 687/1000.
- **[EXTERNAL]** Friedmann fit for prediction A.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · Predictions Feasibility Map · Locked v1*
