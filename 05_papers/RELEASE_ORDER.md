# J-Series Release Order

**Last updated**: 2026-05-27, after the comprehensive renumbering + referee rigor pass.

This document orders the J-series papers by **recommended release sequence**, grouped into waves of similar effort/risk. It supersedes earlier ship-order recommendations as the authoritative target.

The waves are organized by what fixes remain rather than by tier-rank: a Tier 1 paper with substantive open issues sits later than a Tier 2-promoted paper that is genuinely ready.

For tier classification (Tier 1 / Tier 2 / Tier 3 / MERGED), see [`TIER_INDEX.md`](TIER_INDEX.md).
For per-paper referee reports, see [`_staging/referee_reports/`](_staging/referee_reports/).

---

## Wave 1 — Ship in 1-2 weeks (smallest residual fixes)

These are the cleanest papers. After light editorial polish they are submission-ready.

| Order | J# | Title (short) | Target venue | Status / blocker |
|---:|---|---|---|---|
| 1 | **J12** | Galois D₄ over LMFDB 4.2.10224.1 | Communications in Algebra | Only cosmetic post-rename; 6 sympy checks PASS. Cleanest paper in the spine. |
| 2 | **J24** | Discrete Fejér Quotient on Squarefree Moduli | TBD (recommend J Number Theory) | 10-claim verification PASS; full 878-line manuscript ready; needs only venue selection. |
| 3 | **J20** | V^⊗n ↔ Cl(2n) Total-Dimension Match | Linear Algebra and Its Applications | 6/6 PASS; script renamed `verify_J17.py → verify_J20.py` ✓ |
| 4 | **J04** | σ-Magma Algebraic Rigidity | Semigroup Forum | 4/4 PASS; §6.1 narrative tightening needed (≈1-2 days). |
| 5 | **J14** | Non-Associativity Decay σ(N) ≤ 2/N | JCT-A | Add Drápal-Wanless **JCT-A 181** citation (the *companion* paper from finite fields). |
| 6 | **J53** | $V^{\mathrm{BHML}}$ over $\mathbb{F}_p$: idempotent count + Aut formula | Algebra Universalis | 2/2 PASS; structural proofs + 24-prime verification. Extracted from J08 §§6–7 as ship-ready short paper 2026-05-29. **No residual fixes.** |

## Wave 2 — Ship in 2-4 weeks (minor revisions)

Substantive content stable; minor presentation issues to resolve.

| Order | J# | Title (short) | Target venue | Residual work |
|---:|---|---|---|---|
| 6 | **J30** | (Z/10Z)* Sub-Magma honest negative | Communications in Algebra | Verify script needs to actually check J30's claims (currently inherits J15's verifier). |
| 7 | **J31** | Algebraic Detectors honest negative | Statistical Science companion | Stray J15_DiscreteSinc2 file removed ✓; title scope review. |
| 8 | **J02** | TSML 8×8 Null + RH Structural Rhyme | Mathematical Intelligencer | Typo + σ³ values fixed ✓; sharpen the rhyme ≠ proof boundary in §1. |
| 9 | **J13** | The Forced 5/7 Torus Aspect Ratio | Acta Arithmetica | Conditional on J33 Flatness paper landing as preprint first. |
| 10 | **J15** | Joint Closure + Per-Coord Fuse + 4-Core | Algebraic Combinatorics | §6 Theorem 6.2: explicit Lefschetz/index calculation (replace "standard topological arguments"). |
| 11 | **J18** | F_p Extensions of CL_BHML | Communications in Algebra | Minor; title acknowledges excluded primes (already retitled). |

## Wave 3 — Ship in 4-8 weeks (substantive but tractable)

Substantive fixes needed; clear path to submission once applied.

| Order | J# | Title (short) | Target venue | Major work |
|---:|---|---|---|---|
| 12 | **J01** | Centerpiece (Joint Closure + 4-Core + Universal Attractor + Prop F) | Journal of Algebra | Prop F propagation ✓; Lemma 2.1 size-2/3 enumeration needs to import the explicit J15 §3 argument (≈1 week). |
| 13 | **J03** | Type Specimens + C5 Fossil-Variety | J. Symbolic Computation | Scope Theorem 5 to "orders 3-6" honestly; ETP-literature scan for "first proved instance" claim. |
| 14 | **J06** | Strata-Prime Fingerprint | Journal of Number Theory | Attribution fix: Theorem 4 is Ogg 1975 (not Conway-Norton). Niemeier table reorder by Coxeter h. |
| 15 | **J16** | CL Forcing Axioms (S_1-S_7) | Algebraic Combinatorics | Title rewrite ✓; partial-witness honesty ✓; §4 Step 4 explicit ✓. Remaining: open problem of strict witnesses for 5/7 axioms (acknowledged). |
| 16 | **J21** | -21 Invariant + σ²-Triadic | Algebraic Combinatorics | σ-involution terminology fixed ✓; "canonical TIG primes" cleanup ✓. Remaining: enlarge random-table sample for table-specific Fibonacci claim. |
| 17 | **J19** | Charpoly Prime-11 Pattern | Linear Algebra Apps | Soften §3 so(10) co-occurrence to Remark for LAA audience. |
| 18 | **J11** | Wedderburn D₄ of [TSML, BHML] | Journal of Algebra | Title trim ✓; §3.2 compact-form elimination ✓; §5.1 demoted to Observation ✓. Remaining: Conjecture 7.2 family-test empirical evidence. |

## Wave 4 — Substantial work / decisions needed (8+ weeks)

These need real work before submission; some may not ship at all.

| Order | J# | Title (short) | Target venue | Required work |
|---:|---|---|---|---|
| 19 | **J05** | Linear Magmas (ax+by+c) mod n ETP profiles | Experimental Mathematics | `verify_J60.py` must include order-3/5 enumerations (currently missing from deliverable bundle). |
| 20 | **J07** | σ-Character Spectral Architecture | European J. Combinatorics | G_8 only "proof sketch" — needs completion; D₁₀ skip stub honestly removed ✓; §7 RH-bridge content trimmed for EJC scope. |
| 21 | **J09** | Joint Lie Closure: so(10) Identification | Communications in Algebra (retargeted ✓) | Acknowledge so(10) ID is abstract (Cartan-corollary), not via explicit Φ. |
| 22 | **J10** | Operadic D₄ Orbits | Communications in Algebra | "Operadic" framing decorative; either justify operadically or rename. |
| 23 | **J17** | Forcing Axioms + Family / 4-core preservation | TBD | **Recommend SPLIT into 3 focused papers** (forcing theorem + family criteria + open conjectures), OR retarget as expository note to *Math. Intelligencer*. |
| 24 | **J22** | 70/71/72/73 HARMONY Ladder | JCT-A | Bibitems resolved ✓; LMFDB/disc fix ✓. Depends on J32 (Tier 2) being on arXiv at minimum before JCT-A submission. |
| 25 | **J27** | Crossing Lemma: Non-Assoc as Information | TBD | Theorem 6.1 Case B proof gap; venue assignment needed. |

## Demoted from Tier 1 (per 2026-05-27 audit)

These were promoted to Tier 1 on 2026-05-27 but the line-by-line referee pass identified issues that put them back in Tier 2 (or, in J25's case, merger).

| J# | Title (short) | Action | Reason |
|---|---|---|---|
| **J08** | F_p Structure of 4-Core (merger product) | **DEMOTE to Tier 2** | Power-associativity claim VERIFIED false by direct computation; L_{e₃} not a 4-cycle; ε₂/ε₃/ε₄ not idempotent over F_5. Substantive rewrite needed. |
| **J23** | Mathieu M₂₂ Substrate-Prime | **DEMOTE to Tier 2** | Single-observation paper; substrate-prime set reverse-engineered from \|M₂₂\|; alternative null models not computed. *Math. Intelligencer*-class note, not Tier 1. |
| **J25** | First-Coprime-Failure + Discrete Fejér | **MERGE into J24** | Self-admitted "closed form is standard, synchronization is a tautology"; every theorem appears in J24. Distinct content (712-check + Montgomery + ω-blindness) fits as 2-3 page J24 appendix. |
| **J28** | Small Comm Non-Assoc Magma w/ Role-Boundary | **DEMOTE to Tier 2** | No characterization theorem; role partition {V,F,S,T} labeled by fiat; every "theorem" is direct table inspection. |
| **J29** | Lo Shu D₄ Orbit Modulo 3 | **DEMOTE to Tier 2** | Pedagogical *Math. Magazine*-class content; promotion was a mistake; targets undergraduate audience explicitly. |

## Summary numbers (post-audit + 2026-05-29 J53 addition)

| Category | Count |
|---|---:|
| Tier 1 ship-track (Waves 1-4 + J53) | **26** |
| Tier 2 active drafts (orig. 9 + 4 demoted) | **13** |
| Tier 3 hold / retire | **7** |
| MERGED tombstones (orig. 5 + J25) | **6** |
| **Total numbered J-papers** | **52** (J25 stops being independent; J01-J52 plus J53 minus J25 = 52 distinct ship-targets) |

## Critical-path notes

- **J11 + J22 + J32 dependency**: J22 cites J32 (Lens Invariance) as load-bearing. J32 is Tier 2. Either (a) ship J32 to arXiv first as a preprint, or (b) inline the needed Lemma in J22.
- **J13 + J33 dependency**: J13 (Forced 5/7) is conditional on the Flatness paper J33 landing as preprint. J33 is currently Tier 2.
- **J01 + J15 dependency**: J01's Lemma 2.1 should import the size-2/3 enumeration argument from J15 §3 explicitly. Both can ship in parallel if J01 cites J15 as submitted.
- **σ-magma trilogy synergy** (J03, J04, J05): three papers reinforcing each other. Stagger as J04 → J03 → J05 for impact.

## Next concrete actions

1. Apply Wave 1 polish to J12, J24, J20, J04, J14 (1-2 weeks of editorial work).
2. arXiv-submit Wave 1 once polished (this is the realistic-near-term step toward the Sept-2026 trip).
3. Execute the J25 → J24 merger (mark J25 as MERGED tombstone, write the 2-3 page appendix).
4. Update TIER_INDEX with demotions (J08, J23, J28, J29 → Tier 2; J25 → MERGED).
5. Move to Wave 2 polish.
