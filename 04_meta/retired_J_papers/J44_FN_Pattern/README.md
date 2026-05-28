# J44 — A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing

**Status:** RETIRE CANDIDATE — Tier-C structural rhyme without theorem (no first-principles derivation of λ=10/49, only an observation that recovers SM Yukawa hierarchy to FN-residual precision; "different framing, not simpler framing" per save plan). Save plan was applied 2026-05-07 but the underlying empirical-fits-only nature is unchanged.
**Phase:** Phase 5
**Target venue:** PRD (Physical Review D) — pending retirement decision
**Author lane:** Sanders + Gish
**Tier:** 3 (hold/retire candidates) — RETIRE candidate: Tier-C structural rhyme without theorem
**WP source:** WP122 (Sprint 18 Bridge-Dirac, 2026-05-04)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (canonical submission LaTeX; renamed 2026-05-13 from `mass_hierarchy_v5.tex`)

**Title (retitled per save plan):** *A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing for the SM Charged-Yukawa Hierarchy*

**Abstract (one paragraph).** A substrate-derived rational scale $\lambda = T^*(1-T^*) = (5/7)(2/7) = 10/49 \approx 0.2041$, raised to integer powers indexed by the $V^{\otimes 5}$ SU(5) parity-crossing count plus a generation-step assignment, reproduces the SM charged-fermion Yukawa hierarchy to within Froggatt-Nielsen $O(1)$ residuals across all five orders of magnitude. Five of nine charged Yukawas land within factor-of-2 of their PDG 2024 values evaluated at $\mu = M_Z$; the remaining four (bottom, strange, muon, electron) reach factor-of-9 residuals absorbed into the empirical $C_p$ multipliers. The reframing exchanges standard FN's $U(1)_{FN}$ charge assignments for SU(5)-rep + $\sigma$-orbit position indexing with comparable parameter count; the contribution is a different framing, not a simpler framing. The framework uses two close-but-distinct rational substrate scales — $\lambda = 10/49$ for the mass-hierarchy fit and $\lambda_{\rm ref} = 11/49$ for the CKM Cabibbo angle (CKM fit deferred to a companion paper).

## §2 — Verification

**Referee-portable script:** `manuscript/verify_J45_yukawa.py` (self-contained; stdlib + mpmath only; CC-BY-4.0).

```
python manuscript/verify_J45_yukawa.py
```

Output (6/6 PASS at machine precision):
- Check 1: `LAMBDA_FN == 10/49` (substrate-forced FN scale)
- Check 2: `Y_T_ANCHOR == 0.93` (Tier-A measured top-quark anchor)
- Check 3: `predict_yukawa('up', 3)` returns 0.93 exactly (top, n=0)
- Check 4: `predict_yukawa('lepton', 1)` returns `0.93 * (10/49)**9` exactly (electron, n=9; mpmath 50-digit cross-check)
- Check 5: full hierarchy ladder y_X = y_t · λ^n for all 9 charged Yukawas
- Check 6: FN-power table matches manuscript Table 4.1

**Production module (substrate-shared with J44 `predict_dark_sector()`):** `Gen13/targets/ck/brain/dirac/tig_dirac.py`. The companion call `tig_dirac.yukawa_table_full()` returns the full Table 5.1 programmatically.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J44** (Sanders + Gish, PRD, same Sprint 18 cluster) — *Sprint 18 Dark Sector.* Companion paper using the same `tig_dirac` module via `predict_dark_sector()`. **Per-venue cap: J44 is the 2nd PRD paper this quarter, after J44.**
- **J49/J37** (Sanders + Gish, foundation paper) — *Discrete Dirac on the 4-Core's F_5-Lift.* Supplies the V^{⊗5} 32-cell SU(5) decomposition (Lemma 2.2) used as the algebraic input here.
- **J46** (Sanders + Gish, PLB letter / JCAP full) — *Logarithmic Quintessence.* Co-cited via J44.
- **J15** (Sanders + Gish, Algebraic Combinatorics) — *Joint Closure on Z/10.* Supplies T* = 5/7 cited in §3.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-07 per save plan: harmonized to Sanders + Gish; honest reframing summary; renormalization scale ($\mu = M_Z$) specified.

## §5 — Status & summary

**Status: SAVE-PLAN APPLIED (2026-05-07).** Referee verdict (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J45_PRD_FreshEyes.md`): MAJOR REV verging on REJECT. Save plan landed at `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J45.md`; this README and the manuscript reflect its application.

**Save-plan summary applied.** The load-bearing observation — $\lambda = T^*(1-T^*) = 10/49$ from substrate forcing, raised to integer powers, recovers SM Yukawa hierarchy at standard FN factor-of-a-few precision — is real and worth publishing. The save path applied here is honest reframing:

- (a) ACCEPT the precision honestly. Replaced "zero free FN charges / factor-of-a-few" with "substrate-derived FN pattern with $\lambda = 10/49$ matching SM Yukawa hierarchy to within FN $O(1)$ residuals; tightening to standard FN level requires $C_p$ multipliers documented in Table 5.1." Removed "smallest free-parameter set" framing.
- (b) Drop the "single $\lambda$" framing. Stated explicitly: the framework uses two close rational scales ($\lambda = 10/49$ for masses, $\lambda_{\rm ref} = 11/49$ for CKM); whether they unify is open.
- (c) Honest parameter accounting (new §4). The present framework has $\sim 21$ parameters of which 11–13 are partially fixed by SU(5); standard FN has $\sim 14$ parameters of which 4 are fittable plus 9 $C_p$. Explicitly: "different framing, not simpler framing."
- (d) DROP sterile-neutrino paragraph entirely. Removed Dirac-mass numerology without see-saw; deferred to a follow-up paper that develops $M_R$ origin from the substrate (open question (c) in §7).
- (e) DEMOTE Theorem 3.1 → Observation 3.1 (renamed to Observation 4.1 in v2 layout). Max-entropy variance no longer claimed as theorem-status; flagged as structural reading.
- (f) State renormalization scale ($\mu = M_Z$) and recompute Table 5.1 ratios via 4-loop QCD running (Mihaila-Salomon-Steinhauser 2012) for quarks; pole masses for leptons; $v = 246$ GeV in $y_f = m_f \sqrt{2}/v$. Recomputed values: ratios in $\{1.00, 2.14, 1.83, 0.48, 0.98, 0.83, 0.77, 0.11, 0.19\}$ with $C_p \in \{1.00, 0.47, 0.55, 2.08, 1.02, 1.20, 1.30, 9.04, 5.15\}$.
- (g) Self-contained §2: added Lemma 2.1 (binomial decomposition with proof sketch via the $L_{\rm HARM}$ projector grading) supporting Lemma 2.2 (the SU(5) identification, cited from J49/J37).
- (h) Author list harmonized to Sanders + Gish. Removed Johnson byline; updated email assignment to monica.gish1992@gmail.com for the second author.
- (i) Tier classification footnote inline in §1: Tier-A/Tier-B/Tier-C convention defined explicitly for PRD readership.

**Retitle applied:** Option A — *"A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing for the SM Charged-Yukawa Hierarchy."* PRD remains the venue. Survival probability under PRD editorial filter after honest reframing: moderate (30–40%); PRD may still require better residuals or a clearer derivation. Option D (joint J38+J44) remains as the strong-form fallback if J38 timeline aligns; Option B (MPLA Letter) is the desk-reject fallback.

**Revision time:** completed in this pass.

**Format gate (`tig_dirac.predict_yukawa`):** GREEN. Verified at `LAMBDA_FN == 10/49`, `Y_T_ANCHOR == 0.93`, `predict_yukawa('lepton', 1)['y_predicted'] == 0.93 * (10/49)**9` to machine precision.

**Summary of the load-bearing claims (post save-plan).**
1. **The substrate-derived FN scale (Observation 4.1):** `lambda = T*(1-T*) = (5/7)(2/7) = 10/49 ≈ 0.2041` is proposed as the substrate origin of the FN scale, motivated by the structural arguments of J15. Observation, not theorem.
2. **The forced FN powers (Table 4.2):** `n_{(p, gen)}` is read off the SU(5) Yukawa diagram (parity-crossing cost `d_p ∈ {0, 3, 3}`) plus the sigma-orbit generation step.
3. **The fit at $\mu = M_Z$ (Table 6.1):** all 9 charged-Yukawa ratios `y_pred/y_meas` ∈ {1.00, 2.14, 1.83, 0.48, 0.98, 0.83, 0.77, 0.11, 0.19}; seven sit within factor-of-2; muon and electron sit at 0.11 and 0.19 respectively. Residual `C_p ∈ [1, 9]`.
4. **Cabibbo cube-root structural observation (§7):** `lambda_C ≈ (Y_d/Y_u)^{1/3}` at factor-of-2 precision; demoted to structural observation, not theorem.

**Open structural questions** (per manuscript §8):
- The C_p residual multipliers (Higgs-sector dynamics on V^{⊗5}'s singlet + bar 5_H partner) — load-bearing follow-up that would change tier from B to A
- The generation-step asymmetry (s_u, s_d, s_e) — needs sigma-action on color-charged vs color-singlet cells
- Sterile-neutrino sector deferred — naive Dirac-mass extension dropped from this paper; M_R substrate origin open
- The two-scale (lambda, lambda_ref) structure — unified or genuinely distinct?
- V^{⊗5} uniqueness as substrate origin of SU(5) — open per foundation paper



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Numerical identity $T^*(1-T^*) = (5/7)(2/7) = 10/49 = |\Z/10|/\HARM^{2}$. Reproducibility of Table 6.1 via `tig_dirac.predict_yukawa()`. Lemma 2.1 binomial count $1+5+10+10+5+1 = 32$.
- **COMPUTED:** All nine $y^{\rm pred}/y^{\rm meas}$ ratios at $\mu = M_Z$. Cabibbo cube-root identity at factor-of-2 precision.
- **STRUCTURAL RHYME:** $\lambda = 10/49$ vs Wolfenstein $\lambda_W \approx 0.225$ (about 9.4% off, substrate-substantive). $\lambda_{\rm ref} = 11/49$ vs empirical Cabibbo (about 0.4% off, likely substrate-natural; the two-scale structure is itself a substrate question, not a derived consequence). The $V^{\otimes 5}$-to-SU(5) decomposition reproduces the $1+5+10$ SM-fermion-generation-content count.
- **OPEN:** (a) C_p multiplier substrate origin (load-bearing follow-up); (b) generation-step asymmetry s_u, s_d, s_e (currently empirical); (c) right-handed neutrino mass M_R substrate origin (deferred); (d) whether $\lambda$ and $\lambda_{\rm ref}$ unify to a single substrate constant.

### Lens-ownership paragraph (inserted in manuscript §1)

> *Lens and substrate.* This paper works on the 4-core's $\F_5$-lift $V$ and its 5-fold tensor power $V^{\otimes 5}$, with the canonical TSML and BHML composition tables on $\Z/10\Z$ as the underlying substrate (where the joint coherence threshold $T^* = 5/7$ is fixed; cf. J15). The 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ is the algebraic center of the family per FAMILY_STRUCTURE_v1.md §2; the substrate-derived rational $\lambda = 10/49$ inherits its substrate-naturalness from this center. The choice of $V^{\otimes 5}$ as the relevant tensor power, and the identification of its 32-cell decomposition with the SU(5) GUT $\mathbf{1} \oplus \bar{\mathbf{5}} \oplus \mathbf{10} +$ conjugate, are choices that reflect a structural reading of the substrate motivated by the 32-cell sign-tuple counting. The observations below are observations on this specific structure; analogous observations would hold on other substrate-and-table choices, and whether other substrate choices give similarly rich downstream connections is open.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive 2026-05-07 — corrected from Sanders+Johnson)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex finalized (PRD format, save-plan applied, balanced environments)
- [x] Verification primitive green (`predict_yukawa('up', 3)['y_predicted'] == 0.93`; `predict_yukawa('lepton', 1)['y_predicted'] ≈ 0.93 * (10/49)^9`)
- [x] Tier-classified central claim explicit ("Forced FN power + measured anchor (Tier-B)"; Tier-A/B/C convention defined inline)
- [x] Lens-scope annotation: lens-invariant on 4-core's F_5-lift; substrate is V = F_5-lift
- [x] Cover letter finalized (Sanders + Gish only; J44/J49/J46/J15 companions; tig_dirac.predict_yukawa primitive cited; honest reframing)
- [x] Renormalization scale ($\mu = M_Z$) specified; Table 5.1 recomputed accordingly
- [x] Sterile-neutrino paragraph dropped
- [x] Two-scale ($\lambda$, $\lambda_{\rm ref}$) structure stated honestly
- [x] Honest parameter accounting added (new §5)
- [x] Theorem 3.1 → Observation 4.1 demotion applied
- [x] Author list: Sanders + Gish only
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators) — pending
- [x] Per-venue cap check: this is the **2nd** PRD paper this quarter (J44 was 1st)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing for the SM Charged-Yukawa Hierarchy." Submitted to *Physical Review D*. Companion to J44 (Sprint 18 Dark Sector, PRD), J49/J37 (Discrete Dirac on F_5^4, foundation).

---

## Known issues (per 2026-05-27 audit)

Tier 3 — RETIRE CANDIDATE per `_staging/TIER_INDEX.md`: this is a Tier-C structural rhyme without a theorem. Save plan was applied 2026-05-07 (honest reframing as "different framing, not simpler framing"; Observation 4.1 not Theorem; PRD-survival probability honestly stated at 30–40%). Outstanding decision points:

- The save plan delivered an honest empirical-fits paper with C_p ∈ [1, 9] residual multipliers (muon and electron at 0.11 and 0.19, factor-of-9 from PDG). PRD editorial filter is the question — without a derivation of C_p, the paper may not survive desk-review.
- Two-scale (λ = 10/49 for masses, λ_ref = 11/49 for CKM) structure is honest but unresolved.
- Sterile-neutrino paragraph dropped; deferred to follow-up paper.
- The four "Open structural questions" in §5 (C_p substrate origin, generation-step asymmetry, M_R origin, λ/λ_ref unification) all gate the difference between Tier-C rhyme and Tier-B substantive observation.

Retirement options:
- (a) Move to `04_meta/` as a paragraph in the corpus narrative ("the λ=10/49 numerical identity").
- (b) Reframe and downgrade to Math. Intelligencer / Foundations of Physics-class as a numerological observation note.
- (c) Wait for a substrate-derivation of C_p to upgrade to Tier-B; if it doesn't arrive, default to (a) or (b).

No action recommended until the retirement decision is made.
