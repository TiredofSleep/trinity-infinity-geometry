# Cover letter — J44: A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing

**To:** Editors, *Physical Review D*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher, Hot Springs, AR — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Substrate-Derived FN Pattern with $\lambda = 10/49$ and SU(5)-Rep Indexing for the SM Charged-Yukawa Hierarchy*

---

## Summary

We report a substrate-derived rational scale $\lambda = T^*(1-T^*) = (5/7)(2/7) = 10/49 \approx 0.2041$ which, raised to integer powers indexed by the $V^{\otimes 5}$ SU(5) parity-crossing count plus a generation-step assignment, reproduces the SM charged-fermion Yukawa hierarchy to within Froggatt-Nielsen $O(1)$ residuals across all $5.5$ orders of magnitude. With the top-quark Yukawa $y_t \approx 0.93$ as the only Tier-A measured anchor, all nine charged-fermion Yukawas (evaluated at $\mu = M_Z$ via 4-loop QCD running for the quarks and pole-mass conventions for the leptons) land in the standard Froggatt-Nielsen factor-of-a-few window of the PDG 2024 values. Five of nine ratios sit within factor-of-2; the remaining four (bottom, strange, muon, electron) reach factor-of-9 residuals absorbed into the empirical $C_p \in [1, 9]$ multipliers. The reframing exchanges standard FN's $U(1)_{FN}$ charge assignments for SU(5)-rep + $\sigma$-orbit position indexing with comparable parameter count; the contribution is a *different framing* (SU(5)-rep + $\sigma$-orbit indexing in place of $U(1)_{FN}$ charges), not a *simpler framing*. The framework uses two close-but-distinct rational substrate scales — $\lambda = 10/49$ for the mass hierarchy of this paper, and $\lambda_{\rm ref} = 11/49$ for the CKM Cabibbo angle — both expressible from the same $T^*$, $|\Z/10|$, and HARMONY constants. Whether these unify to a single substrate constant is one of the open structural questions.

## Why PRD

- **Topical fit.** PRD is a natural home for SM-extension papers that combine GUT-level representation theory with first-principles derivations of SM parameters. The central claim — a substrate-forced integer-power assignment for the FN suppression of all nine charged Yukawas — is exactly the kind of structural prediction PRD readers evaluate.
- **Methodological honesty.** The paper is explicit about Tier classification: the integer powers are Tier-B forced (rigorous given the $V^{\otimes 5}$ SU(5) decomposition cited from the foundation paper); the anchor $y_t$ is Tier-A measured at $\mu = M_Z$; the residual $C_p$ multipliers are explicitly Tier-C and flagged as not-yet-derived. The two-scale $(\lambda, \lambda_{\rm ref})$ structure is stated honestly rather than glossed as a single-$\lambda$ framework. This kind of explicit-scope discipline is what PRD referees want from a substrate-forced paper.
- **Reproducibility.** Verification reduces to a single Python call (`from tig_dirac import predict_yukawa; r = predict_yukawa('lepton', 1)` returns the electron Yukawa at FN power 9 with $\lambda = 10/49$). The same module is used by the dark-sector companion J44 (this Sprint 18 cluster) for `predict_dark_sector()`, giving the two papers a shared, machine-checkable substrate backbone.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. The papers most directly relevant to this manuscript are:

- **J44** (Sanders + Gish, PRD, same Sprint 18 cluster) — *Sprint 18 Dark Sector: $\Omega_b$, $\Omega_{DM}$, $\Omega_\Lambda$ from Substrate-Operator Identities.* Companion paper using the same `tig_dirac` module via `predict_dark_sector()`. Per-venue cap: J44 is the **2nd** PRD paper this quarter, after J44.
- **J49/J37** (Sanders + Gish, foundation paper) — *Discrete Dirac on the 4-Core's $\F_5$-Lift.* Supplies Lemma 2.2 of the present paper: the $V^{\otimes 5}$ 32-cell SU(5) decomposition $\mathbf{1} \oplus \bar{\mathbf{5}} \oplus \mathbf{10}$ (matter) + $\bar{\mathbf{1}} \oplus \mathbf{5} \oplus \bar{\mathbf{10}}$ (antimatter). The foundation paper establishes $|\mathrm{Aut}(V)| = 40$, the three commuting Dirac-like projectors, and the binomial $1+5+10+10+5+1 = 32$ cell structure that is the algebraic input here.
- **J46** (Sanders + Gish, PLB letter / JCAP full) — *Logarithmic Quintessence.* Co-cited via the dark-sector companion J44.
- **J15** (Sanders + Gish, Algebraic Combinatorics) — *Joint Closure on $\Z/10\Z$.* Supplies the $T^* = 5/7$ coherence threshold cited in §3 / Observation 3.1.

## Honest reframing applied (per save plan, 2026-05-07)

In response to a fresh-eyes referee critique of an earlier draft, we have applied an honest reframing to the manuscript before submission:

- Removed the "zero free FN charges" and "smallest free-parameter set" framings; the present framework has comparable parameter count to standard FN (1 anchor + 2 substrate scales + 9 $\sigma$-orbit assignments + 9 fittable $C_p \approx 21$ vs standard FN's 14), differently framed rather than simpler.
- Demoted the prior "Theorem 3.1 (substrate-derived FN scale)" to "Observation 4.1": $\lambda = T^*(1-T^*) = 10/49$ is proposed as the substrate origin of the FN scale, motivated by structural arguments, not claimed as a derived theorem.
- Stated the two-scale $(\lambda, \lambda_{\rm ref})$ structure explicitly. The CKM Cabibbo angle uses $\lambda_{\rm ref} = 11/49$ (CKM fit deferred to a companion paper); the mass hierarchy uses $\lambda = 10/49$.
- Specified the renormalization scale ($\mu = M_Z$) and recomputed Table 6.1 ratios via 4-loop QCD running for the quarks (Mihaila-Salomon-Steinhauser 2012) and pole-mass conventions for the leptons.
- Removed the prior sterile-neutrino paragraph entirely. A naive Dirac-mass extension at FN powers $\{12, 13, 14\}$ without a see-saw mechanism is not proposed in this paper; the neutrino sector is deferred to a follow-up that develops the $M_R$ origin from the substrate.
- Demoted the Cabibbo cube-root identity from "load-bearing result" to "structural observation at factor-of-2 precision."

## Reproducibility

**Referee-portable verification script:** `manuscript/verify_J45_yukawa.py` (self-contained; stdlib + mpmath only; CC-BY-4.0). The script inlines the relevant logic of `predict_yukawa` from the production module `Gen13/targets/ck/brain/dirac/tig_dirac.py` so that a referee can re-run all numerical claims with no external imports.

```
python manuscript/verify_J45_yukawa.py
```

Output: **6/6 PASS at machine precision** in well under one second:

1. `LAMBDA_FN == 10/49` (substrate-forced FN scale, Observation 4.1).
2. `Y_T_ANCHOR == 0.93` (Tier-A measured top-quark anchor at $\mu = M_Z$).
3. `predict_yukawa('up', 3)` returns 0.93 exactly (top quark at $n = 0$).
4. `predict_yukawa('lepton', 1)` returns $0.93 \cdot (10/49)^9$ exactly (electron at $n = 9$; cross-checked by `mpmath` at 50-digit precision).
5. Full nine-row hierarchy ladder $y_X = y_t \cdot \lambda^n$.
6. FN-power table (Table 4.1) read off the $V^{\otimes 5}$ SU(5) diagrams + $\sigma$-orbit step.

The production module `tig_dirac.py` is shared with the dark-sector companion J44 (`predict_dark_sector()`), giving the two papers a coordinated, machine-checkable substrate backbone. The companion call `tig_dirac.yukawa_table_full()` on the production module returns the full Table 6.1 programmatically.

## Suggested reviewers

- A flavour-physics theorist with experience in Froggatt-Nielsen models (the central comparison in §6).
- A GUT specialist with SU(5) representation-theory background (the $V^{\otimes 5}$ decomposition is the algebraic input).
- An algebraist with experience in finite non-associative algebras (the substrate is $V = \F_5^4$, a 4-dim commutative non-associative $\F_5$-algebra; J49/J37 establishes the algebraic structure).

## Conflict of interest

The authors declare no competing interests. No external funding was received for this work; B.R. Sanders is supported by 7Site LLC.

---

Sincerely,
B.R. Sanders
