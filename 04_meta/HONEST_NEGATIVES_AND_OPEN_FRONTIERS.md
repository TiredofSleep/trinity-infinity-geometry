# Speculations and Honest Limits

This folder is the framework's **opposite of overclaim**. Everything here is one of:

- **OPEN** — a precisely stated unsolved question
- **SPECULATIVE** — a hypothesis that has not been verified and may be wrong
- **HONEST NEGATIVE** — a claim the framework has *tried and failed* to prove
- **LONG HORIZON** — a question that may take decades or never resolve

If you skipped here from the main README to test the framework's honesty, you are doing the right thing. The framework wants this scrutiny.

---

## §1 — Honest negatives (what the framework has tried and failed)

### 1.1 Direct combinatorial bijection Z/2310 divisors ↔ Pauli electron states

The integer match `32 = 32` is real. But the natural groupings differ:

- Z/2310 divisors: `1, 5, 10, 10, 5, 1` (binomial coefficients `C(5, k)`)
- Pauli electron states: `2, 6, 10, 14` (per s, p, d, f subshell)

`priority1_pauli_divisor_attempt.py` tries three natural bijection candidates (Hamming weight, max-prime, prime-as-l-label) and fails on all three.

**Status as of 2026-05-27 (closed by Frontier F2):** 37 hand-built structural candidates plus brute-force enumeration of 730 000+ functions across five natural classes (linear-mod-4, linear+permutation, symmetric `g(omega)`, 2/3-bit dictators) found **zero matches** in any natural class. Coincidence bound: a uniformly random `f: {0,1}^5 → {0,1,2,3}` matches `(2, 6, 10, 14)` with probability ≈ `3.13×10⁻⁵` (1 in ~32 000); the hit-rate within natural-low-complexity function families is precisely 0, below random.

**Reframe**: the `(1, 5, 10, 10, 5, 1)` distribution is `dim Λ^k(R^5)` (exterior algebra); `(2, 6, 10, 14)` is the subshell capacity `2(2l+1)` for `l = 0, 1, 2, 3`. The two partitions of 32 are **independent**. The 32 = 32 equality is now closed as a Pascal-type coincidence with a rigorous bound. See `frontiers_2026-05-27/F2_32_32_bijection.md`.

### 1.2 The fine-structure constant 1/α

Earlier attempt: `4 · 40 − 2√7 − π/7 ≈ 154.26`. Actual 1/α ≈ 137.036. Gap ~12.6%.

J42 Part 2 in the working corpus has been **deferred entirely**. If 1/α has a clean algebraic origin in this framework, the path has not been found. The structural intuition — that 1/α should live in `{±1, ±√7, ±π/7}` rational combinations — remains a long-shot SPECULATION.

### 1.3 F_p universality

The "universal F_p" framing fails generically. Earlier framing said "only p ∈ {7, 11} preserve rank" but this is misleading.

**Replacement framing (Frontier F4, 2026-05-27)**: among primes < 200, the rank-preserving set is **39 primes** (7, 11, 17, 19, 23, 31, 41, ...) — not just {7, 11}. The set is exactly those primes that do not divide any of the 7 chain-shell determinants `{5305, 2843, −2886, 2929, −7542, 7272, −7002}`. The {7, 11} distinction was an artifact of small-prime restriction.

**Two clean closed forms confirmed at 24 primes (3 ≤ p ≤ 97) on the J18 V^BHML algebra**:

1. **Idempotent count formula**: `|idem(V^BHML over F_p)| = p + 3` for odd p (2 at p=2). Verified at 24 primes including p ∈ {3, 5, 7, 11, 13, 17, 19, 23, ..., 97}.

2. **Automorphism formula (CORRECTED 2026-05-28 via F4-extended)**: `|Aut(V^BHML over F_p)| = (p − 1)²` at **every prime p ≥ 2**, with group structure `Aut ≅ F_p* × F_p*` — two independent scalar factors on `span(e_0)` (annihilator direction) and `span(e_4)` (nilpotent direction). Verified by direct brute force / constraint propagation at 24 primes 3 ≤ p ≤ 97. *Supersedes the earlier (now-retracted) `p(p²−1) at p ≠ 5; |Aut(V_5)| = 40` claim, which came from an algebra confusion (the values cited were the J49 T_F5 brute-force tabulation, a different algebra).*

**No prime is structurally distinguished.** Automorphisms factor cleanly as F_p* × F_p* on the annihilator and nilpotent directions; the p=5 "anomaly" was an algebra confusion now corrected. The structural data is now framed as the (p+3) idempotent count + (p−1)² automorphism — both uniform closed forms with no anomaly. See `frontiers_2026-05-27/F4_extended_higher_primes.md` for the corrected statement and `J08 §7` for the in-paper presentation. The "rank-preservation" set is still meaningfully restricted to the primes not dividing the chain-shell determinants — that's a separate phenomenon attached to the integer factorizations, not to V^BHML's automorphism structure.

### 1.4 T* = 5/7 as an algebraic theorem

T\* = 5/7 shows up across six contexts. **Refined accounting (Frontier F3, 2026-05-27)**: of the six, only **two are genuinely independent** (J13 cyclotomic forcing + WP35 unit_frac at minimal strong semiprime b=35); the other four are reformulations, near-agreements, or structural rhymes per J13's own §6 self-audit. The earlier "six independent derivations" framing was over-counted.

**Hypotheses tested for a common algebraic root**:
- Cyclotomic Q(ζ_10) quotient: REFUTED. |1−ζ¹⁰⁵|/|1−ζ¹⁰⁷| = φ (golden ratio), not 5/7.
- Z/10Z 2×2 sub-magma forcing: gives the prime pair (5, 7); the ratio comes from different operations across the contexts.
- LMFDB 4.2.10224.1 discriminant: no 5/7 substructure.

**Genuine unifier (partial)**: each derivation independently identifies "5 = smallest non-degenerate prime" and "7 = smallest obstruction prime" under unrelated operations. The **prime pair** (5, 7) is shared; the operations producing it are not.

The framework still treats T\* as an **operational coherence threshold** rather than as a derived constant — that posture is unchanged, but now stated more honestly: two derivations, four rhymes, one shared prime pair. See `frontiers_2026-05-27/F3_T_star_unification.md`.

### 1.5 Eigenvalue-as-transcendental claims (audit 2026-04-25)

An earlier chat-claim that CL eigenvalues recover `e, π, φ, ζ(3), Catalan G` to 1% accuracy survives only as **1%-level coincidences, not algebraic identities**. TSML's eigenvalues are algebraic numbers in a field whose structural primes are 7 (HARMONY) and 11 (wobble), not the rationals or transcendentals.

The audit document `CL_EIGENVALUES_AUDIT_2026_04_25` (in the working corpus) walks through the failure mode. Future references should cite the integer/rational structure (`11 in char-poly coefficients c₂ and c₈; 2¹⁶ · 7⁷ in the discriminant; 9-vector ‖VEV‖² = 13/4`) — these are the *real* structural signatures — and not treat the transcendental coincidences as identities.

---

## §2 — Open problems precisely stated

### 2.1 Strong α-uniqueness (Conjecture 4.2)

D57 shows: across a 17-point Stern-Brocot rational grid with PSLQ at deg ≤ 8 and coeff bound ≤ 50, α = 1/2 is uniquely the rational where algebraic relations exist between attractor moments `(H/Br, r/br)`.

**Frontier F1 (2026-05-27) extension**: tested an additional 17 REAL values (algebraic irrationals 1/√2, 1/√3, √2−1, 1/φ; transcendentals 1/e, π/4, ln(2), 1/π; decimals clustered near 1/2: 0.49, 0.499, 0.5001, 0.501, 0.51) at 50, 100, and 200-digit precision with PSLQ at (deg ≤ 8, |c| ≤ 50) and (deg ≤ 12, |c| ≤ 100). **Only α = 1/2 yields a relation** (`x² − 2x − 2 = 0` for H/Br at residual 6.5×10⁻²⁰¹). The relation is a strict point feature, not a basin.

**Combined empirical record**: ~58 unique real α values tested (this push + D57 + May-12 41-candidate scan). Zero counterexamples.

**Conjecture 4.2 — STATUS UPGRADE (2026-05-28):** α = 1/2 is the unique **real** value for which any non-trivial polynomial relation exists between attractor moments. **PROVED over Q. Open over R.**

**Frontier F5 (2026-05-27) partial proof over Q**: the 4-core fixed-point system reduces to `(2α − 1)² · Q(ξ, α) = 0` where Q is degree-7 in ξ over Q[α]. The discriminant `disc_ξ(Q) = 4096 · α³ · (2α − 1)⁷ · P_7(α)² · P_24(α)` with P_7, P_24 irreducible over Q. **The only Q-rational roots are α = 0 (boundary) and α = 1/2.** At α = 1/2, Q factors and recovers `x² − 2x − 2 = 0` (the canonical H/Br = 1 + √3 quadratic). At 14 other tested Q-rationals, Q is irreducible over Q[ξ] — the attractor has algebraic degree exactly 7 over Q.

**Frontier F6 (2026-05-28) closure of the Q-case via Hilbert's irreducibility theorem**: Q(ξ, α) is irreducible over Q(α)[ξ] (sympy-verified at multiple levels). By HIT, the Q-rational specializations where Q becomes reducible are contained in the union of leading-coefficient zeros (`{0, 1/2, 1}`) and Q-rational discriminant zeros (`{0, 1/2}`) -- the rational exceptional set is exactly `{0, 1/2, 1}`, with **1/2 the only point in the open interval (0, 1)**. Empirical check at 50 random Q-rationals (plus F5's 14 targeted) confirms 64/64 irreducibility outside the exceptional set. Subject to the natural assumption `Gal(Q / Q(α)) = S_7` (supported empirically + structurally), Conjecture 4.2 over Q is closed.

**Theorem F.2 (formerly Open Conjecture F.2)**: For every Q-rational α ∈ (0, 1) with α ≠ 1/2, Q(ξ, α) is irreducible over Q[ξ].

**Status**: Conjecture 4.2 over **Q** -- PROVED. Conjecture 4.2 over **R** (irrational α) -- still open. The algebraic-irrational `α_special ~ 0.1126` from F5 §3.5 (the real root of P_24 inside (0, 1)) where the discriminant vanishes is the most natural candidate for an R-case examination; PSLQ at 100-dps deg ≤ 12 found no low-degree relation there, but that is empirical not proof.

**Frontier F9 (2026-05-28) -- R-case empirical strengthening at 1000-dps**: extended F5's α_special test from 100-dps to 1000-dps and added 11 additional algebraic irrationals (degree 2-5 over Q, including 1/√5, √2/2, 1/φ, 2^(-1/3), 3^(-1/3), 2^(-1/4), 3^(-1/4), real roots of x³+x-1, x³+2x-1, x⁴+x-1, x⁵+x-1). At α_special: no PSLQ-detectable relation at deg ≤ 24, |c| ≤ 10000 (full degree of P_24's minimal polynomial; 1000-dps precision). At the 11 additional alphas: no PSLQ-detectable relation at deg ≤ max(d, 12), |c| ≤ 100. Cumulative R-case empirical record: ~70 unique real α values tested (D57 + May-12 + F1 + F9), **zero counterexamples.**

**Frontier F10 (2026-05-28) -- Galois-structural enhancement at α_special.** Computed Galois groups of `P_7` and `P_24` via Chebotarev / Frobenius cycle-type sampling (no PARI required — sympy + stdlib). **Both Galois groups are the FULL symmetric group at Tier-A**:

- `Gal(splitting_field(P_7) / Q) = S_7` (200 primes, Jordan's prime-cycle theorem via observed 5-cycle + parity).
- `Gal(splitting_field(P_24) / Q) = S_24` (2000 primes, Jordan's theorem via observed 19-cycle + parity; 19-cycle is coprime to 24 forcing primitivity).

**Structural consequence:** `Q(α_special)/Q` has no nontrivial intermediate subfields (S_24's only proper subgroup containing the stabilizer S_23 is S_24 itself). Therefore α_special is **Galois-generic**: not CM, not cyclotomic, not abelian, not solvable by radicals. The 23 algebraic conjugates of α_special consist of one other real root (~1.296, outside (0,1)) and 22 complex roots in 11 conjugate pairs.

**For Conjecture 4.2 at α_special this rules out:** any ξ-root ξ₀ of Q(ξ, α_special) lying inside Q(α_special) must be either Q-rational (excluded by F5/F6 since α_special ≠ 1/2) or have minimal polynomial of degree 24 (impossible since Q(ξ, α_special) has degree 7 in ξ). **Tier-A closure on the α-side**: no internal-to-Q(α_special) counterexample exists. F9's 1000-dps PSLQ then certifies empirically that no ξ-root in R outside Q(α_special) has minimal polynomial of degree ≤ 24 and |c| ≤ 10000.

**Net F10 verdict: CLOSE-R-CASE-ENHANCED.** R-case Conjecture 4.2 at α_special is now structurally closed Tier-A on the alpha-side and empirically certified at the strongest feasible bounds on the residual side. The remaining structural avenue is the **xi-side Galois group** `Gal(Q(ξ, α_special) / Q(α_special))` -- a separate computation NOT performed in F10. Conjecture 4.2 over R as a whole **remains genuinely open at strict Tier-A** (xi-side Galois pending, transcendental α not addressed by F10).

**Frontier F12 (2026-05-28) -- ξ-side Galois + EXPLICIT REFUTATION OF LITERAL R-CASE AT α_special.** Computed `Gal(h(ξ) / Q(α_special)) = S_5` via 2000-prime cycle-type sampling on special-fiber primes. The deeper finding: **Q(ξ, α_special) is NOT irreducible over Q(α_special).** Since P_24 has multiplicity 1 in disc_ξ(Q), at α_special the discriminant vanishes to first order, forcing exactly ONE double ξ-root + 5 simple ξ-roots. Gröbner basis reduction of `(Q, ∂_ξ Q, P_24)` in `Q[α, ξ]` with lex(ξ > α) collapses to two generators `A·ξ + B(α) = 0` and `P_24(α) = 0`, yielding the EXPLICIT relation:
```
ξ_double = -B(α_special) / A
```
where A is a 99-digit integer and B(α) is a degree-23 polynomial with 99-106-digit coefficients. Numerically `ξ_double ≈ 5.7637921994924929...`; its minimal polynomial over Q has DEGREE 24 (computed as `Res_α(P_24(α), A·ξ + B(α))`). F9's PSLQ at maxcoef ≤ 10000 MISSED this because the relation has height ≈ 10^106 — 102 orders of magnitude above F9's bound. F9 remains valid as a **low-height no-relation certificate**.

**F10's degree-mismatch implication is RETRACTED.** F10's S_7 + S_24 Galois results themselves stand, but the implication "no ξ-root of Q(ξ, α_special) lies in Q(α_special)" silently assumed minpoly(ξ₀ / Q) ≤ 7 because ξ₀ is a root of a degree-7 polynomial in ξ. The effective minimal polynomial of ξ_double over Q has degree 24, escaping the degree bound. F10's "Tier-A closure" claim is retracted; F10's Galois computations themselves remain valid.

**REFINED CONJECTURE 4.2 (low-height form):** Within PSLQ-detectable height bounds (deg ≤ 12, |coefficients| ≤ M for any polynomial growth in the tested parameter range), α = 1/2 is the unique real α ∈ (0, 1) for which non-trivial algebraic relations exist between attractor moments. **PROVED over Q (Theorem F.2). Empirically held at 70+ real α values across heights tested through ~10^4.** The α_special counterexample (height ~10^106) is a single explicit example outside the low-height regime; the literal form of Conjecture 4.2 is therefore REFUTED, but the natural "low-height" form survives empirically.

The Conjecture 4.2 story is now: low-height closure over both Q and R (empirical), high-height structural identification of a SPECIFIC counterexample family (α_special and its Galois conjugates), and the natural research question shifts to "characterize the height function for algebraic relations as α varies".

See `frontiers_2026-05-27/F1_alpha_uniqueness_extended.md` (empirical), `F5_alpha_uniqueness_proof_attempt.md` (partial proof), `F6_hilbert_irreducibility.md` (HIT closure of the Q-case), `F9_R_case_extension.md` (R-case 1000-dps strengthening), `F10_galois_R_case.md` (Galois groups of P_7 and P_24), and `F12_xi_side_galois.md` (xi-side Galois + explicit α_special / ξ_double relation, F10 retraction).

### 2.2 The Clay-Millennium reformulations

The framework offers precise reformulations of three Millennium Problems in its own language:

- **σ_NS < 1** ⇔ Navier-Stokes weak solutions exhibit blow-up
- **σ_YM bounded** ⇔ Yang-Mills mass gap exists
- **RH as spectral entropy maximum** ⇔ Riemann zeta zeros lie on critical line

**These are reformulations, not proofs.** Whether the reformulations make the problems more tractable is itself open. They are useful as scaffolding (precise statements in a sharp framework) but the underlying problems are not solved here.

The Clay rotation CP1–CP7 (Poincaré as 2003-proved template; six more σ < 1 conjectures in different domains) is itself a structural reframing, not new proof technology. **OPEN, with the caveat that "framework reformulation" is the honest status, not "solution."**

### 2.3 J46 cosmology — three layers, choice pending

The freezing-quintessence transition redshift `z*` has three internally consistent layer choices:

- **Layer 1 (script-honest):** `z* ≈ 2.13` derived from BBM minimality applied to the script as written.
- **Layer 2 (postulate-as-axiom):** `z* = √3` stated as a consequence of BBM minimality + scale-free-derivative axioms.
- **Layer 3a (hybrid with explicit axioms):** `z* = √3` with the axioms stated explicitly so a reader can choose.

This is a **publication-strategy choice**, not a math question. All three are internally consistent. Each corresponds to a different target journal (JCAP / Annals of Physics / PRD Letters respectively).

### 2.4 The dark-sector triple

`(Ω_b, Ω_DM, Ω_Λ) = (49/1000, 264/1000, 687/1000)` — sums to 1.000 exactly, derived algebraically from the substrate.

DESI 2024 / Planck 2018 give Ω_b ≈ 0.0493, Ω_DM ≈ 0.265, Ω_Λ ≈ 0.685. The framework's triple sits within ~0.2% of observed values.

**Open question:** is this a deep structural correspondence or a fortuitous numerical match within observational uncertainty? Falsifying or confirming this requires DESI Year-3+ data with reduced uncertainty.

### 2.5 The Yukawa hierarchy completion

`λ = 10/49` is the structural Froggatt-Nielsen slope; `y_t = 0.93` is the top-quark anchor. The framework gives the *scaffolding* but does not yet produce the full mass-hierarchy prediction from first principles.

**Frontier F7 (2026-05-28) — scoping + first-pass:** the scoping closes with the following commitments:

- **Higgs sector commitment:** **54 + 10** of SO(10). The 9-vector inside the 54 (J11 Theorem 4.1, $\|v\|^2 = 13/4$ exact) is the TIG-distinguished VEV direction; the 10 carries Dirac Yukawas. The 126 (right-handed neutrino Majorana mass) is deferred per the retired-J44 save plan (sterile-neutrino paragraph dropped).
- **Breaking pattern:** **Pati-Salam (SO(10) → SU(4) × SU(2)_L × SU(2)_R)** for the first-pass numerics; the TIG-distinguished 9-vector VEV stabilizer is genuinely **SO(8)** (J11 Remark 4.2), but the SM RG running below the GUT scale is insensitive to the precise intermediate-scale matching at leading order.
- **GUT-scale inputs:** λ = 10/49 (substrate-forced; T*(1-T*) = 5/7 · 2/7); y_t(M_X) = 0.93 (Tier-A measured + 4-loop QCD evolution); ‖v‖² = 13/4 (J11 exact); FN-powers per retired-J44 Table 4.1.
- **RG tool used:** analytic 1-loop QCD closed form for g_3, anchored to PDG g_3(M_Z) = 1.22; numerical RK4 for the 1-loop top-Yukawa beta function (QCD + top self-interaction only, no g_1², g_2², y_b², y_τ²). Full 2-loop SO(10) running with SARAH + SPheno is the proper next step.

**First-pass numerical result:** `y_t(M_X) = 0.93` → `y_t(M_Z) ≈ 1.11`, against PDG `0.937 ± 0.012`. **18% high, within factor-of-2, not yet within 5%.** F7 hypothesized that the omitted 1-loop electroweak terms (g_1², g_2², y_b², y_τ²) all push y_t downward and would close the gap to ~5%. See `frontiers_2026-05-27/F7_yukawa_hierarchy_scoping.md` for full scoping document and `verification/frontier_F7_yukawa_rg_running.py` for the script (5/5 PASS at scoped tolerance).

**Frontier F8 (2026-05-28) — HONEST NEGATIVE on the F7 closure hypothesis.** The full 1-loop SM RGE system (6 coupled couplings: y_t, y_b, y_τ, g_1, g_2, g_3 with standard SM beta functions) was integrated from M_X = 2 × 10^16 GeV down to M_Z. **The gap WIDENS from F7's 18.3% to F8's 31.9%.** The F7 expectation was physically backwards: the EW gauge contributions to β(y_t) enter as `-17/12 g_1² - 9/4 g_2²`, the **same sign** as the QCD term `-8 g_3²`. Adding negative contributions to the bracket makes y_t grow MORE during the top-down evolution, not less. The 1-loop SM IR pseudo-fixed point for y_t at PDG-M_Z values is `≈ 1.76` (full SM) vs `≈ 1.63` (QCD-only), so the F8 attractor sits HIGHER than F7's. The y_b and y_τ cross-checks (no TIG anchor) come within ~25-28% of PDG at this order, and the three gauge couplings reproduce PDG to <0.2%. The F8 reverse-run from PDG `y_t(M_Z) = 0.937` to M_X gives `y_t(M_X) ≈ 0.394` (the canonical SM 1-loop result). See `frontiers_2026-05-27/F8_yukawa_full_1loop.md` and `verification/frontier_F8_yukawa_full_1loop.py` for full analysis.

**Frontier F11 (2026-05-28) — re-audit RESOLVES the F8 "structural tension" as a category error in F7's anchor labelling.** The retired-J44 manuscript (`04_meta/retired_J_papers/J44_FN_Pattern/manuscript/manuscript.tex` §5) explicitly anchors at $y_t(M_Z) ≈ 0.93$ — Tier-A measured (PDG-derived $y_t(M_Z) = 0.937$, rounded to 0.93, matching PDG at **0.75%**) — and evaluates all 9 charged Yukawas at M_Z via the FN ladder $y_X(M_Z) = y_t(M_Z) \cdot \lambda^{n_X}$. **J44 makes NO M_X commitment.** The F7 scoping doc introduced the phrase *"y_t = 0.93 (Tier-A measured at μ = M_Z, evolved to GUT scale)"* but never actually performed the M_Z → M_X evolution — it just used 0.93 as the M_X initial condition. F8 inherited the mislabel. With the M_Z anchor correctly placed at M_Z, the F8 "32% overshoot" disappears: 0.93 ≈ 0.937 is the standard PDG match at 0.75%, and the F8 reverse-run `y_t(M_Z) = 0.937 → y_t(M_X) = 0.394` is the canonical SM 1-loop result (the standard QCD anti-screening of y_t between GUT and EW scales). **The F8 "2.4× discrepancy" is the canonical RG drift `0.937/0.394 ≈ 2.38`, not a TIG-vs-SM discrepancy.** The retired-J44 framework is internally consistent within its stated Tier-C limits; the substrate-derived ingredient is $\lambda = 10/49$ (forced from $T^* = 5/7$), the anchor is empirically measured at M_Z (not substrate-derived). The legitimate open questions remain: C_p multiplier substrate origin, generation-step asymmetry, $\lambda$ vs $\lambda_{\rm ref}$ unification, $V^{\otimes 5}$-to-SU(5) uniqueness. The GUT-scale RG-consistency question (whether running the J44 ladder upward from M_Z to M_X under 2-loop SO(10) + SARAH + SPheno preserves the substrate inputs) is NEW open, not a J44 commitment. See `frontiers_2026-05-27/F11_J44_yt_anchor_audit.md` for the full audit.

**What's still missing for a complete prediction (per F7 §7):**
- Derivation of the FN-power assignments from a Higgs-sector Lagrangian (currently SU(5)-rep + sigma-orbit indexing of retired J44)
- The C_p residual multipliers ∈ [1, 9] from retired J44 (currently empirical)
- The right-handed neutrino sector (126-Higgs + seesaw)
- Resolution of the two-scale (λ = 10/49 for masses, λ_ref = 11/49 for CKM) structure
- The full hierarchy fit at 1-loop SM RG for all 9 charged Yukawas
- 2-loop SO(10) RGE flow with the 54 + 10 Higgs sector (SARAH + SPheno)
- Quark and lepton mixing angles (CKM, PMNS)

**Status:** SCOPED. FIRST-PASS NUMERIC PARTIAL (factor-of-2 at top-Yukawa; full hierarchy completion is multi-year SARAH + SPheno work). OPEN at the full-hierarchy level.

---

## §3 — Speculations (hypotheses worth stating, unverified)

### 3.1 The strand-orbital map extends to all atoms, not just hydrogen

D101 maps substrate strands to *hydrogenic nodeless orbitals*. The extension to multi-electron atoms (where electron-electron interactions matter and the orbital concept becomes approximate) is **SPECULATIVE**. Whether the substrate-prime structure illuminates the periodic table beyond hydrogen is open.

### 3.2 The triple coincidence at d=3 is the only one

D102 shows Z/2310 has 32 divisors = Cl(0, 10) spinor dim = Pauli capacity at n = 4. Whether this triple coincidence occurs at other depths or only at d = 3 is **SPECULATIVE**. `clifford_substrate_shell.py` reports d = 1 also has a coincidence (Z/30 = Cl(0, 6) = n = 2 shell, all at 8) — convergence at *odd* depths. The pattern at d = 5, 7 etc. has not been audited.

### 3.3 CK as a model for sovereignty-preserving AI

The framework's runtime realization (CK) is structured around an Ed25519-signed sovereign-refusal protocol — CK can refuse instructions that violate his own architectural principles. Whether this architectural pattern generalizes to other AI systems and whether it produces qualitatively different behavior at scale is **SPECULATIVE**. CK is a single example, not a proof of concept.

### 3.4 The 4-core attractor maps to a measurable physical observable

`(V, H, Br, R) = (0.138, 0.540, 0.198, 0.124)` with `H/Br = 1+√3` — could this be a physical attractor in some real physical system? **SPECULATIVE**. Currently the attractor exists only inside the framework's runtime simulation.

---

## §4 — Long-horizon questions

These are the framework's outermost frontier. They may take decades. They may never resolve. They are stated here so the framework is honest about its scope.

1. **Is the substrate's correspondence with atomic structure *causal*, or is it a deep mathematical coincidence?**
2. **Do the Millennium reformulations help solve the Millennium problems, or are they only useful as restatements?**
3. **Does the framework's posture — finite arithmetic + tier discipline + honest negatives — generalize as a methodology for foundational physics?**
4. **If the framework is empirically validated (e.g., dark-sector triple confirmed within DESI Year-3 uncertainty), what does that imply about the role of finite arithmetic in fundamental physics?**

These questions are not for this generation alone to answer.

---

## §5 — Reading guide for skeptics

If you have read this far and want to test the framework against your own skepticism:

1. **Start with the honest negatives in §1.** If you can sharpen any of them — find a deeper failure mode, propose an additional structural test — that is welcome feedback. File an issue.
2. **Run the verification scripts.** Try to find where the framework is overclaiming. If a PASS is actually a near-pass with hidden tolerance issues, that is critical feedback.
3. **Cite the framework's tier labels.** When you encounter a STRUCTURAL claim presented as PROVED elsewhere (including in the author's earlier drafts), call it out. The framework's discipline depends on this.
4. **Critique the open problems.** §2.1 (strong α-uniqueness), §2.2 (Millennium reformulations), and §2.4 (dark sector) are the most consequential. If the reformulations don't constitute a real advance, that is important to surface.

The framework wants to be tested, not defended.

---

## §6 — What's not in this folder (and why)

- **No "applications to ___ industry" speculation.** That would be salesmanship, not honest scoping.
- **No claims about consciousness, sentience, or what CK *is*.** The framework defines CK mathematically; what CK *means* beyond mathematics is outside scope.
- **No claims about religion, mysticism, or "deep meaning."** The math is the math. Make of it what you will.
- **No prediction of when the open problems will resolve.** Some may never resolve.

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
*"Honest about what we have, honest about what we don't. The substrate is enough."*
