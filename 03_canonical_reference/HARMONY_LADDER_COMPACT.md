# HARMONY_LADDER_COMPACT — The 28–73 Integer Sequence

## Every HARMONY count integer in TIG, with structural decomposition and cross-DOF identities

**Brayden Sanders · 7Site LLC · Trinity Infinity Geometry**
*Sources: canon D26, D27, D34, §6.7, D97; this session*
*Companion to: PRIMES_OF_TIG, SIX_DOFS_COMPACT, THREE_TABLES_COMPACT*
*Locked v1 · 2026-05-08*

---

## §1. The Ladder

Every HARMONY-relevant integer that appears in canon, ascending:

| n | Source | Decomposition | DOF |
|:---:|---|:---:|:---:|
| **28** | BHML_10 HARMONY count | $T_7 = 2^2 \cdot 7 = C(8,2) = C(8,6)$ | Lie (= dim so(8) = D₄) |
| **36** | TSML_7 HARMONY count | $T_8 = 2^2 \cdot 3^2 = C(9,2) = C(9,7)$ | TSML chain rung 7 |
| **44** | CL_STD HARMONY count (variant) | $4 \cdot 11$ (wobble interpolation) | encoding |
| 45 | dim so(10) = D₅ | $T_9 = 3^2 \cdot 5 = C(10,2) = C(10,8)$ | Lie (NOT a H count) |
| **70** | det(BHML_8) | $2 \cdot 5 \cdot 7 = C(8,4) = \varphi(71)$ | Lie/Yang-Mills core |
| **71** | TSML_9 H = lens disagreement = LMFDB prime | prime | Lattice (3 roles per D97) |
| **72** | TSML_10 minus apex | $8 \cdot 9 = 2^3 \cdot 3^2$ | TSML structure |
| **73** | TSML_10 HARMONY count | prime | full TSML lens |

---

## §2. The Triangular Sub-Spine

Three sequential triangular numbers with TIG roles:

$$T_7 = 28, \quad T_8 = 36, \quad T_9 = 45.$$

| Triangular | Identity | TIG meaning |
|:---:|---|---|
| $T_7 = 28$ | $\dim \mathfrak{so}(8) = D_4$ | BHML_10 HARMONY count |
| $T_8 = 36$ | — | TSML_7 HARMONY count |
| $T_9 = 45$ | $\dim \mathfrak{so}(10) = D_5$ | (Lie dim, not H count) |

**Reading.** Sequential triangulars $T_7, T_8, T_9$ tile the **bottom** of the ladder. Two are HARMONY counts; the middle one is just a HARMONY count; the third is the next Lie algebra dimension.

**The wobble interpolation.** CL_STD's HARMONY count $44 = 4 \cdot 11$ sits between $T_8 = 36$ and $T_9 = 45$ but is **not triangular**. It uses the wobble prime 11. CL_STD therefore sits **off the triangular sub-spine** — this is consistent with CL_STD being the "papers freeze" encoding (D95) rather than a clean algebraic structure.

---

## §3. The 70–73 Quartet

Four consecutive integers, each with a distinct TIG role:

| n | Role | Decomposition |
|:---:|---|---|
| **70** | $\det(\mathrm{BHML}_8)$, Yang-Mills core | $2 \cdot 5 \cdot 7 = C(8,4) = \varphi(71)$ |
| **71** | Lattice prime; TSML_9 H; lens disagreement | prime |
| **72** | TSML_10 minus apex (drop $(7,7)$) | $8 \cdot 9$ |
| **73** | TSML_10 H (full canonical lens) | prime |

**Reading.** Consecutive integers in canon are rare. This quartet shows TIG's "final ascent" of the ladder: from the Yang-Mills core at 70, through the lattice prime at 71, the structurally-reduced TSML at 72, to the canonical full TSML at 73. **One step per role.**

**Three of four are arithmetically special:**
- 70 = $\varphi(71)$ (totient relation)
- 71 prime; THREE structural roles in canon (D97)
- 72 = $T_8 \cdot 2$ = product of two consecutive integers
- 73 prime

---

## §4. Cross-DOF Identities Through the Ladder (this session, new)

The ladder integers participate in **non-trivial cross-DOF arithmetic identities**:

### Identity I — Lie ⊕ Lie = TSML
$$\dim \mathfrak{so}(8) + \dim \mathfrak{so}(10) \;=\; 28 + 45 \;=\; 73 \;=\; \mathrm{TSML}_{10}\, H.$$

The two canonical Lie algebra dimensions sum to the TSML_10 HARMONY count.

Algebraic form: $T_7 + T_9 = T_{n=7}^2/3 + 3\cdot 7 + 3 = 49 + 21 + 3 = 73$. (Special to $n = 7$.)

### Identity II — CL_STD − BHML = Jordan
$$44 - 28 \;=\; 16 \;=\; \dim(\mathfrak{su}(4) \oplus \mathfrak{u}(1)) \;=\; \dim D_4\text{-inv}\, \mathfrak{so}(10).$$

CL_STD's HARMONY count minus BHML_10's HARMONY count equals the **Jordan DOF dimension** = the doubly-invariant Higgs sector dimension (D34).

### Identity III — TSML_7 doubled = TSML_10 reduced
$$2 \cdot 36 \;=\; 72 \;=\; \mathrm{TSML}_{10} - \text{apex}.$$

Doubling the TSML_7 HARMONY count gives the TSML_10 HARMONY count minus the apex cell.

### Identity IV — BHML + CL_STD = TSML reduced
$$28 + 44 \;=\; 72 \;=\; \mathrm{TSML}_{10} - \text{apex}.$$

Sum of BHML_10 H and CL_STD H also lands at 72.

**Reading.** Identities I, II, III, IV all relate ladder integers to one another or to DOF dimensions. They form a **dense web of integer relations** — small integers in TIG don't sit isolated; they tile through addition and subtraction.

---

## §5. The Step Pattern

Differences along the ladder:
$$28 \xrightarrow{+8} 36 \xrightarrow{+8} 44 \xrightarrow{+1} 45 \xrightarrow{+25} 70 \xrightarrow{+1} 71 \xrightarrow{+1} 72 \xrightarrow{+1} 73.$$

Two structural regions:
- **Low ladder (28–45):** double-step of 8, then unit step of 1. The +8 increments correspond to the triangular increment $T_{n+1} - T_n = n+1$ at $n = 8$ ($T_8 - T_7 = 8$). The CL_STD interpolation 44 sits at the same +8 from 36 (one wobble step ≈ one triangular step).
- **High ladder (70–73):** four consecutive integers, one step each. Maximum density of TIG roles.

**Big gap (45 → 70):** $\Delta = 25 = 5^2$. This empty stretch contains:
- $T_{10} = 55$ — does not appear as HARMONY count
- $T_{11} = 66 = e_2$ idempotent of $\mathbb{Z}/143$ — does not appear as H count
- 50 — wobble cycle ratio denominator (W = 3/50) — appears here but not as H count

**Reading.** The HARMONY count ladder is **bimodal** — clustered at the bottom (sequential triangulars + wobble interpolation) and at the top (four consecutive integers covering det, prime, structure-reduced, and full-canonical). The middle gap reflects the structural separation between Lie-dim regime (low) and Yang-Mills/lattice regime (high).

---

## §6. The Prime 70 — Three Distinct Identities

$$70 = 2 \cdot 5 \cdot 7 = C(8, 4) = \varphi(71).$$

This is one integer with three independent structural readings:

1. **Substrate × Attractor:** $2 \cdot 5 \cdot 7 = $ smallest substrate prime × BALANCE × HARMONY. Pure prime-stratum decomposition.
2. **Combinatorial:** $C(8, 4) = $ number of 4-element subsets of an 8-set = the Yang-Mills self-dual sector count (mainstream Lie theory).
3. **Number-theoretic:** $\varphi(71) = $ Euler totient of the lattice prime = number of integers $\leq 71$ coprime to 71.

That a single integer has all three readings AND is the determinant of the canonical Yang-Mills core $\mathrm{BHML}_8$ is a strong structural anchor. Per §6.7 / WP15, $\det(\mathrm{BHML}_8) = +70$ is the load-bearing identity for the Yang-Mills emergence.

---

## §7. The Prime 71 — Three Roles per D97 (PRIMES_OF_TIG)

$$71 = \text{TSML}_9\text{ HARMONY count} = |\text{TSML XOR BHML}| = \text{LMFDB Galois prime}.$$

Three independent structural roles in a single prime (canon D97). Plus three textbook returns:

1. $\varphi(71) = 70$ (returns to BHML_8 det)
2. $h(\mathbb{Q}(\sqrt{-71})) = 7$ (returns to HARMONY)
3. $2 \cdot 71 + 1 = 143 = 11 \cdot 13$ (Sophie Germain bridge to wobble pair)

**Six total structural anchors of the prime 71.** It is the densest connector in TIG's prime spectrum (per ARITHMETIC_BRIDGES).

---

## §8. The Prime 73 — TSML_10 Full Lens

$$73 \text{ is prime}; \quad 73 = T_7 + T_9 = \dim\mathfrak{so}(8) + \dim\mathfrak{so}(10).$$

The full canonical TSML_10 HARMONY count is prime, and equals the sum of the two canonical Lie dimensions. **The TSML_10 lens captures both Lie algebras additively.**

Other 73-residues:
- $73 \bmod 11 = 7 = $ HARMONY
- $73 \bmod 13 = 8 = $ BREATH
- $73 \bmod 7 = 3 = $ PROGRESS

Note: 73's residue mod the **HARMONY prime 7** is **3 = PROGRESS** (the Galois generator). In the sense of σ-fixed vs 4-core (SIGMA_PERMUTATION_COMPACT), 73 lives in the "static" residue class.

---

## §9. Compact Take-Home

```
HARMONY count ladder (every appearance in canon):

   28 = T_7 = dim so(8) = D_4             [BHML_10 H, Lie DOF]
   36 = T_8                               [TSML_7 H]
   44 = 4·11 (wobble interpolation)       [CL_STD H]
   45 = T_9 = dim so(10) = D_5            [Lie dim, not H count]
   ──────────── gap of 25 = 5² ────────────
   70 = 2·5·7 = C(8,4) = φ(71)            [det BHML_8, Yang-Mills core]
   71 = lattice prime (3 roles, D97)      [TSML_9 H, lens, Galois]
   72 = 8·9                               [TSML_10 - apex]
   73 = T_7 + T_9 (prime)                 [TSML_10 H, full canonical]

Cross-DOF identities through the ladder:

   I.  dim so(8) + dim so(10) = TSML_10 H
       28 + 45 = 73
   
   II. CL_STD H - BHML_10 H = Jordan DOF dim
       44 - 28 = 16 = dim(su(4)⊕u(1))
   
   III. 2·TSML_7 H = TSML_10 - apex
        2·36 = 72
   
   IV. BHML_10 H + CL_STD H = TSML_10 - apex
       28 + 44 = 72

The integer 70 has THREE independent identities:
   2·5·7  (substrate × BALANCE × HARMONY)
   C(8,4) (combinatorial, Yang-Mills self-dual)
   φ(71)  (number-theoretic, totient of lattice prime)

The integer 71 has SIX structural anchors (PRIMES_OF_TIG):
   3 in canon D97 + 3 textbook returns
```

---

## §10. Status

- **[CANON]** Triangular T_n values, dim so(n) values, det BHML_8, all H counts.
- **[THM]** All cross-DOF identities (I-IV), arithmetic-trivial verification.
- **[STRUCTURAL]** The triangular sub-spine reading; the bimodal ladder structure.
- **[STRUCTURAL]** The 70-71-72-73 consecutive-integer quartet as TIG's "final ascent."
- **[REFINED]** CL_STD's 44 = 4·11 sits OFF the triangular sub-spine — wobble interpolation. Consistent with CL_STD being a coding-level encoding rather than a clean algebraic object.
- **[OPEN]** Whether the gap 45 → 70 ($\Delta = 25 = 5^2$) has a structural meaning — the only gap in the ladder where no canon integer appears.

---

*© 2026 Brayden Sanders / 7Site LLC*
*Trinity Infinity Geometry · HARMONY ladder compact · Locked v1*
