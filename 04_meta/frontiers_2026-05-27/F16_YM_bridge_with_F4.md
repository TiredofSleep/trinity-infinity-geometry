# F16 — Yang-Mills Clay Bridge Examined With F4's Closed Forms

**Frontier:** Does F4's `|Aut(V^BHML / F_p)| = (p − 1)²` and `|idem| = p + 3` give any
traction on the YM-mass-gap TIG bridge at `04_meta/clay/YM_TIG_BRIDGE.md`?

**Date:** 2026-05-29
**Status:** SCOPING. **Verdict: NO-TRACTION on the central YM gap problem; ONE marginally
suggestive structural rhyme (the rigidity of the e₂-e₃ subalgebra) identified, plus
ONE genuinely productive redirection — the F4 closed forms feed BSD substantially better
than YM.**
**Inputs:** `04_meta/clay/YM_TIG_BRIDGE.md`, `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md`,
`04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md`, `04_meta/clay/BSD_TIG_BRIDGE.md`,
`04_meta/clay/NS_TIG_BRIDGE.md`, `04_meta/clay/HODGE_TIG_BRIDGE.md`,
`05_papers/algebra/J11/manuscript/manuscript.md`.

---

## §1 — YM bridge current state

The TIG–YM bridge as stated in `YM_TIG_BRIDGE.md` rests on three PROVEN substrate
facts:

- **BHML_8 spectral data.** The 8×8 core BHML matrix has eigenvalues whose ordered
  magnitudes are `{47.69, 7.01, 4.45, 1.32, 0.75, 0.47, 0.34, 0.30}`, with an O(1)
  gap `1 - |λ₅|/|λ₄| = 0.434` and the ratio `|λ₇|/|λ₆| ≈ 0.7148` matching
  T* = 5/7 to 0.08%.
- **Identification (conjectural).** The BHML 8×8 plays the role of a discrete
  Wilsonian transfer matrix `T = e⁻ᵃᴴ`. Its persistent spectral gap is the candidate
  finite analog of an SU(N) mass gap.
- **Gauge-group correspondence (conjectural, YM.3).** "BHML's gauge group" is
  identified provisionally with the commutative non-associative magma structure
  on Z/10Z — and this is the load-bearing match-point: it is the place where the
  identification has to bind SU(N) (non-abelian, continuous) to a finite,
  commutative magma. The bridge document acknowledges this is open.

The continuum-limit conjecture (YM.2: the gap persists as `a → 0`) is the second
load-bearing piece. The cross-references in `YM_TIG_BRIDGE.md` note that "the
YM-bridge continuum-limit question … requires understanding how the BHML spectral
gap behaves under refinement, which has parallels to behavior under prime-base
extension" — i.e., the F_p chain-shell data was already flagged as potentially
relevant. F4 (and F4-extended) is exactly the closed-form refinement of that
flag.

---

## §2 — F4 closed forms recapped (CORRECTED)

After the F4-extended correction (`F4_extended_higher_primes.md`):

- **Idempotent count.** `|idem(V^BHML_{F_p})| = p + 3` for all odd primes
  3 ≤ p ≤ 97 (verified at 23 primes; clean closed form). At p = 2, the count
  collapses to 2.
- **Automorphism group.** `|Aut(V^BHML_{F_p})| = (p − 1)²` at all odd primes
  3 ≤ p ≤ 97. The group is `F_p* × F_p*` — Cartan-style abelian
  decomposition. The two `F_p*` factors are:
  - `F_p*` on `span(e₀)` — scalar action on the annihilator.
  - `F_p*` on `span(e₄)` — scalar action on the nilpotent direction.
  - The middle subalgebra `span(e₂, e₃)` (the "idempotent + square-root"
    block) is **rigid**: there is NO non-trivial automorphism, in any odd
    characteristic.
- **No characteristic-zero anomaly.** The F4-original p=5 "anomaly" was a
  cross-algebra confusion; the J18 T^BHML algebra has no anomaly at p=5.

Two clean integer-coefficient closed forms on the 4-core algebra. Both are
fully ABELIAN (F_p* × F_p* is the direct product of two cyclic groups).

---

## §3 — Three connection angles examined

### §3.1 Angle (a) — DIRECT: V^BHML automorphism structure → finite YM gauge structure?

**Claim under examination.** F4 says Aut(V^BHML / F_p) is `F_p* × F_p*`. Could
this be a finite-arithmetic analog of an SU(N) gauge group action?

**Examination.**

1. **Abelian vs non-abelian.** F_p* × F_p* is abelian; SU(N) for N ≥ 2 is
   non-abelian. YM's mass gap problem is fundamentally non-abelian: U(1) gauge
   theory (i.e., QED) has massless photons and NO mass gap. Mass gap conjecture
   is for non-abelian gauge theory specifically. So Aut(V^BHML / F_p) ≃ F_p* × F_p*
   cannot directly play the role of the YM gauge group, because abelian gauge
   theory does not exhibit confinement or a mass gap.

2. **Dimensionality mismatch.** SU(2) has 3 real parameters and is connected.
   SU(N) has N²−1 parameters. F_p* × F_p* has size (p−1)² as a finite set,
   not as a Lie group; the comparison "rank" or "dimension" doesn't naturally
   parse against SU(N).

3. **The σ-permutation/BHML lens IS the carrier of the non-abelian structure.**
   In the TIG substrate, non-abelian content lives in `σ` (the 5-cycle permutation
   of Z/10Z) and the lens-pair commutator `[TSML, BHML]`, NOT in the
   commutative algebra structure of V^BHML. J11 establishes the
   D₄-Wedderburn decomposition of `[T, B]` with the structural zero at sign₃ —
   that IS where finite non-abelian structure lives in TIG. F4 captures the
   FIBER (commutative algebra on the 4-core), not the BASE (the σ-symmetric
   permutation action).

4. **Verdict.** Angle (a) is a no. The (p−1)² automorphism group is the wrong
   algebraic object to feed into the YM identification. It is the commutant
   group of a commutative algebra; YM needs the non-abelian gauge group.

### §3.2 Angle (b) — INDIRECT: does F4 data feed σ_YM bound or continuum limit?

**Claim under examination.** Even if F4's Aut group is not the YM gauge group,
maybe its closed-form structure feeds into the σ_YM-bounded reformulation of
the mass-gap problem (via the chain-shell rank-preservation pattern noted in
the YM bridge's `Cross-references` table).

**Examination.**

1. **What the YM bridge specifically cited.** The YM bridge document cites
   the BHML chain-shell determinants `{5305, 2843, −2886, 2929, −7542, 7272, −7002}`
   and notes that the "natural primes" for the YM gap are {7, 11} — primes that
   rank-preserve across all chain shells. This was the original F4 motivation.

2. **What F4-extended resolved.** F4-extended showed the "{7, 11} are special"
   framing is an artifact of restricting to small primes. The rank-preserving
   set is `{all primes not dividing any chain-shell determinant} =
   {7, 11, 17, 19, 23, 31, 41, 43, 47, ...}` (39 primes < 200). There is NO
   inherent algebraic reason {7, 11} are special; the bad primes are the
   explicit factors {2, 3, 5, 13, 29, 37, 101, ...}.

3. **Consequence for YM.** The YM-bridge's appeal to {7, 11} as the "natural
   prime base" for the YM gap is therefore DEPRECATED by F4-extended. There
   is no "natural prime" for the YM gap from the chain-shell side; there is
   only the empirical-list-of-bad-primes structure. This DOES feed the YM
   bridge: it removes a speculative hook (the "prime 7 or 11 is the gauge-group
   characteristic") and replaces it with a more honest, more generic, less
   useful statement ("any prime not in the bad-list works").

4. **σ_YM bound.** The σ_YM bound mentioned in the task prompt isn't explicitly
   defined in YM_TIG_BRIDGE.md (which uses Δ for the gap and BHML eigenvalues
   for the discrete data). Across the four bridge docs, only NS_TIG_BRIDGE
   defines a substrate functional with a specific bound (`C_discrete ≤ 3.74`
   for the Breath observable). For YM, the "σ_YM" framing is implicit in
   "BHML eigenvalue gap" or "ratio T* = 5/7". F4's closed forms do NOT
   contribute new data to either: the eigenvalue gap lives at the integer
   level of T^BHML (not at the F_p-reduction level F4 catalogs), and T* = 5/7
   is a characteristic-zero fact (not p-dependent).

5. **Verdict.** Angle (b) is marginally productive only in the NEGATIVE
   direction: it deprecates the YM bridge's "natural prime {7, 11}" hint
   and forces a more honest "any non-bad prime" statement. No positive
   contribution to the gap proof.

### §3.3 Angle (c) — CRITICAL: forced or merely suggestive?

**Claim under examination.** Even if (a) and (b) fail directly, is there an
indirect/suggestive rhyme worth flagging — a structural pattern that
COULD be elevated to a YM connection with more work?

**Examination of three candidate rhymes.**

1. **Rigidity of span(e₂, e₃) ↔ "rigid Cartan" inside the BHML.** F4-extended
   §4.2 Step 4 shows that φ(e₃) = +e₃ is FORCED (the −1 branch collapses to
   a singular matrix in odd characteristic). This is a substantive rigidity
   result: the e₃-direction is structurally pinned by the relation `e₃² = e₂`
   combined with `e₃·e₄ = e₄`. Could this rigidity be the finite-arithmetic
   analog of how Cartan subalgebras inside `su(N)` are rigid?
   - WEAK rhyme. Cartan subalgebras in `su(N)` ARE rigid up to Weyl-group
     symmetries — but the symmetry doesn't match: in `su(N)`, the rigidity
     is up to permutation-of-roots; here it's an absolute fixing.
   - This is the most suggestive of the three rhymes, but it is still only
     suggestive: the analog requires a Lie-algebraic structure that V^BHML
     does NOT have (V^BHML is a non-associative commutative magma over Z, not
     a Lie algebra).

2. **(p-1)² scaling ↔ "two independent loop-correction directions".** YM
   1-loop running involves two coupling-direction independence (think
   `α_s` running at different scales). F4's (p-1)² has two independent F_p*
   factors. Coincidental.
   - VERY WEAK rhyme. There is no derivation that ties the (p-1)² structure
     to the YM beta-function. The two factors in F4 are pinned to specific
     algebra directions (`e₀` annihilator, `e₄` nilpotent); the YM running
     has no such pinning. This is pattern-matching at the level of "two
     things".

3. **p + 3 idempotents ↔ "vacuum + 2 excitations" or "Casimir count".** SU(N)
   has 2 Casimirs (rank of su(N) = N−1, and the Killing form). p + 3
   idempotents counts: 0, q₊, q₋, and p indexed orbits. The "3 base
   idempotents" (0, q₊, q₋) plus p "trivial" extras.
   - VERY WEAK. The "+3" comes from substrate-fixed elements (0, q₊, q₋) and
     the +p from a family of solutions parameterized by F_p. No YM analog
     forces "rank 2 + index-p multiplicities".

### §3.4 Honest assessment per angle

| Angle | Verdict | Strength |
|---|---|---|
| (a) Direct: F_p* × F_p* as YM gauge | NO | F_p* × F_p* is abelian; YM needs non-abelian. Structural blocker. |
| (b) Indirect: F4 → σ_YM or continuum limit | NO (with deprecation gain) | F4-extended deprecates the "{7, 11} natural prime" hint; no positive YM contribution. |
| (c) Suggestive: rigidity rhyme | MARGINALLY SUGGESTIVE | The e₂-e₃ rigidity is real and clean but not connected to YM mass gap. Would need Lie-algebra lift that V^BHML does not have. |

---

## §5 — Conclusion: **NO-TRACTION**

The F4 closed forms (`|Aut| = (p−1)²` and `|idem| = p + 3`) give **no positive
traction** on the YM mass-gap problem. The fundamental blocker is structural:
F4 catalogs the F_p-reduction of a commutative non-associative ALGEBRA, while
the YM mass gap is fundamentally a non-abelian gauge-theory phenomenon. The
two are not bridged by F4's data.

**The most that can be honestly said.** F4-extended DEPRECATES the YM-bridge
document's appeal to "{7, 11} as the natural prime base" (since the rank-preserving
set is open-ended). This is a small honest improvement to the YM bridge — the
{7, 11} hint should be REMOVED from `YM_TIG_BRIDGE.md` §"What the F_p merger
contributes" and replaced with a more generic statement.

**The most suggestive rhyme identified.** The rigidity of the e₂-e₃ subalgebra
(forced by F4-extended §4.2 Step 4) is a clean structural fact, but it does
not bind to SU(N) Cartan rigidity without a Lie-algebraic lift that V^BHML
does not possess.

**Verdict: NO-TRACTION** on the YM mass gap. F4 is the wrong tool for this Clay
problem.

---

## §6 — Whether to pursue alternative Clay bridges with F4

F4's `(p−1)²` automorphism group, with its `F_p* × F_p*` Cartan-style abelian
structure and explicit `F_p`-arithmetic, is exactly the kind of object that
parses well against L-function / arithmetic-geometry data. Compare:

| Clay bridge | Match-quality with F4 closed forms |
|---|---|
| **BSD** | **STRONGEST candidate.** BSD is about ranks of `E(Q)`, orders of vanishing of `L(E, s)`, and arithmetic-geometric data over F_p (Tate-Shafarevich, conductor, reduction type). The (p−1)² automorphism structure (two independent F_p* factors) and the p+3 idempotent count are p-explicit arithmetic invariants. The BSD bridge already calls for a curve-to-corridor map (Conjecture BSD.1) — F4's catalog of `(p−1)²` could conceivably be related to the discriminant or conductor of a candidate elliptic curve via the substrate. |
| Hodge | Wrong shape. Hodge is about algebraic cycles on smooth projective varieties over C; F4 is a finite-arithmetic catalog. Hodge's TIG bridge already targets `D₄`-isotypic structure, which is OUTSIDE F4's scope. |
| NS | Wrong shape. NS Breath Criterion is a continuous-PDE blowup characterization; F4's discrete arithmetic doesn't feed it. |
| RH | INDIRECT plausibility. F4's `|Aut| = (p−1)²` resembles the `(p−1)` that appears in the multiplicative group of F_p — a building block of Dirichlet characters and L-functions. But J62 (RH-rhyme) already targets a specific direction and F4 doesn't obviously feed it without an explicit Dirichlet-character lift. |
| P vs NP | Wrong shape. P vs NP is complexity-theoretic, not arithmetic. |
| Hodge / NS / P≠NP | All wrong shape. |

**Recommendation.** Open a follow-up frontier (provisionally F18 — "BSD bridge with
F4 closed forms") that examines whether the (p−1)² and p+3 forms feed BSD.1
(the curve-to-corridor map). Two specific tests worth running:

1. **Is there an elliptic curve E/Q whose mod-p torsion structure mirrors F_p* × F_p* at primes p of good reduction?** (i.e., is E(F_p)[p] ≃ Z/p × Z/p? — this happens for supersingular reduction.) If yes, the F4 closed form might catalog the supersingular-reduction prime locus.

2. **Is the "p + 3 idempotents" count related to any standard arithmetic
   invariant (component group, Tamagawa number, conductor exponent)?**

These are genuinely productive open questions. F4 → YM is closed (NO-TRACTION);
F4 → BSD is the recommended next examination.

---

## §7 — Provenance, files touched, and corrections to YM_TIG_BRIDGE

This document is a SCOPING report under the F-series frontier-push 2026-05-27;
NOT a YM proof attempt. F4 was honestly examined for YM traction and found
to give NONE on the central problem, with one DEPRECATION CONTRIBUTION
(remove {7, 11} natural-prime hint from YM bridge) and one PRODUCTIVE REDIRECTION
(F4 should be examined against BSD, not YM).

**Files read.**
- `04_meta/clay/YM_TIG_BRIDGE.md` (current state of YM bridge)
- `04_meta/clay/BSD_TIG_BRIDGE.md` (comparison)
- `04_meta/clay/NS_TIG_BRIDGE.md` (comparison)
- `04_meta/clay/HODGE_TIG_BRIDGE.md` (comparison)
- `04_meta/frontiers_2026-05-27/F4_Fp_variation_pattern.md` (F4 original)
- `04_meta/frontiers_2026-05-27/F4_extended_higher_primes.md` (F4 corrected)
- `05_papers/algebra/J11/manuscript/manuscript.md` (D₄ Wedderburn context)

**Files NOT touched.** No J-paper or Clay-bridge document was edited under F16;
the only deliverable is THIS scoping report. The recommended YM-bridge edit
(remove the {7, 11} natural-prime hint) is documented above but not executed —
it should be done in a separate hygiene pass with explicit user sign-off, since
it touches a Clay-bridge document.

---

*Status: F16 scoping complete. Verdict NO-TRACTION on YM; redirect to F18 (BSD bridge with F4) recommended.*
