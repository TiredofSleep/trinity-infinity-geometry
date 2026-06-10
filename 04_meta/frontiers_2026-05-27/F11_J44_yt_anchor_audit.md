# Frontier F11 — Re-audit of the retired-J44 `y_t = 0.93` anchor

**Status:** AUDIT COMPLETE. **Verdict (b): the 0.93 was the M_Z anchor all along — F7/F8 mislabelled it as the M_X anchor.** The retired-J44 manuscript (`04_meta/retired_J_papers/J44_FN_Pattern/manuscript/manuscript.tex` §5) explicitly evaluates Yukawas at $\mu = M_Z$ and uses `y_t(M_Z) ≈ 0.93` as the Tier-A measured anchor (a 0.75% deviation from PDG `0.937`). The misattribution to `y_t(M_X) = 0.93` was introduced in F7's scoping (§1.2 line 44: *"y_t = 0.93 (top Yukawa anchor, Tier-A measured at μ = M_Z, evolved to GUT scale)"*), which then ran 0.93 down from M_X as if it were already the GUT-scale value. F8's "32% overshoot" and "2.4× discrepancy" are therefore RG-flow artefacts of the mislabel, not a falsification of the J44 anchor. With the anchor restored at M_Z, J44's $y_t \cdot \lambda^n$ ladder is internally consistent — it is the FN ladder for **the same observed PDG y_t** at the **same observed scale**, and reverse-running PDG `0.937` to M_X gives the canonical `0.394`.

**Date:** 2026-05-28.
**Builds on:** F7 scoping, F8 1-loop SM RG audit; retired J44.
**No new RGE runs required** — F8's reverse-run data already contains the answer.

---

## §1 — J44's derivation chain for `y_t = 0.93`

Reading the retired-J44 manuscript (`04_meta/retired_J_papers/J44_FN_Pattern/manuscript/manuscript.tex`):

### §1.1 What J44 actually says

The substrate forces only ONE ingredient: the FN slope
```
λ = T*(1 − T*) = (5/7)(2/7) = 10/49 ≈ 0.2041
```
where $T^* = 5/7$ is the joint coherence threshold (J15 / retired-J13). The FN exponents $n_{(p,\text{gen})}$ are Tier-B "forced" from the $V^{\otimes 5}$ SU(5) decomposition + parity-crossing cost + $\sigma$-orbit step (manuscript §4, Table 4.1).

The value `y_t ≈ 0.93` is **explicitly** the Tier-A measured anchor, NOT a substrate-derived prediction. From the manuscript:

- **§1 (Introduction), line 172:** *"$y_{t} \approx 0.93$ a single Tier-A measured anchor and the integer powers $n_{(p,\mathrm{gen})}$ Tier-B forced"*
- **§5 (The fit at $\mu = M_Z$), lines 491–494:** *"Yukawas are evaluated at $\mu = M_Z$ via 4-loop QCD running for the quarks (Mihaila-Salomon-Steinhauser 2012) and pole-mass conventions for the leptons, using $v = 246$ GeV in $y_{f} = m_{f}\sqrt{2}/v$. With the integer powers of Table 4.1, the substrate-derived $\lambda = 10/49$, and the single Tier-A measured anchor $y_{t}(M_Z) \approx 0.93$, the predicted Yukawa for each charged fermion is $y^{\rm pred} = y_t \cdot \lambda^n$."*
- **§5 Table 4.1 row "top":** $n = 0$, $y^{\rm pred} = 9.30 \times 10^{-1}$, $y^{\rm meas}(M_Z) = 9.30 \times 10^{-1}$, ratio $= 1.00$, status `anchor`.
- **§7 Verification, line 587:** *"Y_T_ANCHOR == 0.93 (Tier-A measured top-quark anchor at $\mu = M_Z$; cf. PDG 2024 + Mihaila-Salomon-Steinhauser 2012 4-loop QCD)"*

### §1.2 The derivation chain (terminating)

```
substrate forcing:                                      (Tier-B)
  T* = 5/7 (joint coherence threshold from J15)
        ↓
  λ = T*(1−T*) = 10/49             ← THE ONLY FORCED FN INPUT
        ↓
  FN powers n_{(p,gen)} ∈ {0, 3, 5, 6, 7, 9}  via SU(5)-rep + σ-orbit
        
empirical anchor (PDG 2024 + 4-loop QCD):              (Tier-A)
  m_t(pole) ≈ 173.1 GeV
        ↓ MSS 2012 4-loop QCD evolution to M_Z
  m_t(M_Z) ≈ 163 GeV
        ↓ y_f = m_f √2 / v with v = 246 GeV
  y_t(M_Z) ≈ 0.937           ← rounded to 0.93 in J44

prediction:
  y_X(M_Z) = y_t(M_Z) · λ^{n_X}                      (Tier-B overall)
```

**Key fact: J44's anchor is `y_t(M_Z)`, NOT `y_t(M_X)`.** There is no M_X derivation chain in the manuscript. The value `0.93` is rounded PDG-derived $y_t$ **at M_Z**.

---

## §2 — Energy-scale identification

| Scale | Numeric value | Physics meaning | Mentioned in J44? |
|---|---:|---|---|
| $M_X = 2 \times 10^{16}$ GeV | GUT-unification scale | Where canonical SO(10)/SU(5) gauge couplings would unify | **NO** |
| $M_t \approx 173$ GeV | Top pole mass | Where on-shell $y_t = m_t \sqrt{2}/v = 0.994$ | NO (used as upstream PDG input via MSS) |
| $M_Z = 91.1876$ GeV | Z-boson mass | The evaluation scale for all 9 Yukawa ratios in J44 Table 4.1 | **YES, explicitly** |

**J44 lives entirely at $\mu = M_Z$.** The substrate inputs ($\lambda = 10/49$, FN powers) are dimensionless and scale-independent; the anchor and the comparison are both at M_Z.

The retired-J44 paper does NOT make any predictions at the GUT scale. It does NOT claim that y_t = 0.93 at M_X. The phrase "GUT-scale anchor" does not appear in the manuscript or in the README.

The F7 scoping doc (`F7_yukawa_hierarchy_scoping.md` §1, line 44) introduced the M_X interpretation:

> *"y_t = 0.93 (top Yukawa anchor, Tier-A measured at $\mu = M_Z$, evolved to GUT scale)"*

This phrasing is internally contradictory: it says "measured at M_Z" but treats the value as if it had been "evolved to GUT scale" (without actually evolving it). F7 then used `y_t(M_X) = 0.93` as the input to its analytic 1-loop QCD running, which is what produced the 18% overshoot. F8 inherited the same mislabel.

---

## §3 — Canonical y_t comparisons at all three scales

Using $v = 246$ GeV and standard SM 1-loop RGE (F8's data):

| Scale | Canonical SM $y_t$ | TIG anchor `0.93` | Deviation |
|---|---:|---:|---:|
| $M_t = 173$ GeV (pole) | 0.994 ($= 173 \sqrt{2}/246$) | 0.93 | -6.5% |
| **$M_Z = 91.19$ GeV (PDG running)** | **0.937 ± 0.012** | **0.93** | **-0.75%** |
| $M_X = 2 \times 10^{16}$ GeV (canonical SM 1-loop) | 0.394 (from F8 reverse-run) | 0.93 | **+136%** (factor 2.36) |

**The match at M_Z is at the rounding-precision level (0.75%, i.e. within the PDG $\pm 0.012$ error bar).**
The "match" at M_X is a non-match by a factor of 2.36.

This is the audit's headline finding: **0.93 IS the M_Z anchor.** Within the precision quoted in J44 ("$y_t \approx 0.93$"), 0.93 and 0.937 are the same number.

---

## §4 — Source of the F8 discrepancy

F8 found that integrating the 6-coupling 1-loop SM RGE from M_X to M_Z with initial condition `y_t(M_X) = 0.93` gives `y_t(M_Z) = 1.236`, a 32% overshoot vs PDG `0.937`. F8 then reverse-ran PDG `y_t(M_Z) = 0.937` upward and got `y_t(M_X) = 0.394`, concluding the "TIG anchor is roughly 2.4× larger than the canonical SM 1-loop value".

**The 2.4× factor is the cumulative 1-loop RG drift between M_X and M_Z, not a TIG-vs-SM discrepancy.** Specifically:

- $y_t(M_X)_{\rm canonical} \approx 0.394$
- $y_t(M_Z)_{\rm canonical} \approx 0.937$
- ratio: $0.937 / 0.394 \approx 2.38$

This is exactly the canonical SM RG enhancement of $y_t$ from M_X down to M_Z (the QCD anti-screening of the Yukawa coupling between GUT and EW scales). The TIG anchor `0.93` is essentially equal to PDG `0.937` because **it IS the M_Z anchor**.

The F8 "structural tension" therefore reduces to: *if you input the M_Z anchor as the M_X anchor, you get a 1-loop RG run that drifts upward by 2.4× and overshoots PDG by 32%*. That's a labelling error, not a physics finding.

### §4.1 What the F8 data actually shows

Looking at F8's two integrations:

(a) **Forward integration (M_X → M_Z) with `y_t(M_X) = 0.93`** → `y_t(M_Z) = 1.236`.
This is the bug: 0.93 was the M_Z anchor, not an M_X anchor.

(b) **Reverse integration (M_Z → M_X) with `y_t(M_Z) = 0.937`** → `y_t(M_X) = 0.394`.
This is the correct canonical RG result. It confirms that SM 1-loop running maps PDG `0.937` at M_Z to `0.394` at M_X (the well-known "y_t at GUT scale ≈ 0.4" canonical wisdom).

The correct check on J44 is: J44 anchors at `y_t(M_Z) = 0.93 ≈ 0.937` (PDG); the ladder is $y_X(M_Z) = y_t(M_Z) \cdot \lambda^{n_X}$ at the same M_Z scale. No RG running is needed within the J44 framework — all 9 Yukawas live at M_Z. F8's contribution was an UNRELATED experiment about whether the M_Z FN ladder is consistent with a GUT-scale derivation, but the J44 paper never proposed a GUT-scale derivation.

---

## §5 — Recommended reframe

### §5.1 J44's anchor is correctly placed at M_Z (no manuscript change needed)

The retired-J44 manuscript is internally consistent: it anchors at $y_t(M_Z) \approx 0.93$ (PDG) and predicts the other 8 charged Yukawas at the same scale via $y_X(M_Z) = y_t(M_Z) \cdot \lambda^{n_X}$. **The "scale-misidentification" verdict (a) is FALSE for J44 itself.** The substrate-derived ingredient is $\lambda = 10/49$ (Tier-B); the anchor is empirically `y_t(M_Z) = 0.937` rounded to `0.93` (Tier-A measured).

J44's residual issues are unchanged by this audit:
- The C_p multipliers in [1, 9] are empirical (Tier-C), still need a substrate origin.
- The generation-step asymmetry $s_u, s_d, s_e$ is empirically extracted.
- The two-scale ($\lambda = 10/49$ vs $\lambda_{\rm ref} = 11/49$) question is open.

These are all M_Z-level issues. The audit does not affect the J44 retirement status (still Tier-C structural rhyme without theorem).

### §5.2 F7 / F8 used 0.93 at the wrong scale

The correct reframe of F7/F8 is:

- **F7's GUT-scale-anchor scoping was a category error.** J44 never claimed `y_t(M_X) = 0.93`. The phrase F7 used — *"Tier-A measured at $\mu = M_Z$, evolved to GUT scale"* — would have required actually evolving 0.937 up to M_X (giving 0.394, per F8's own reverse-run), then using that as the input. F7 skipped the evolution step.

- **F8's "32% overshoot at M_Z" was the artefact of feeding the M_Z anchor in as the M_X anchor.** Once the M_Z anchor is restored at M_Z, the comparison is trivially trivial: `y_t(M_Z)`_J44_$= 0.93$ vs PDG `0.937` matches at 0.75%.

- **F8's "TIG anchor is 2.4× larger than canonical SM 1-loop" was the canonical RG drift, not a structural problem.** The factor 2.4 = $y_t(M_Z)/y_t(M_X) = 0.937/0.394$ is the standard QCD anti-screening enhancement of the top Yukawa between M_X and M_Z.

### §5.3 What's actually open in the Yukawa frontier (corrected)

Stripping away the F7/F8 artefact, what remains for the Yukawa hierarchy frontier is:

1. **The C_p substrate origin** (load-bearing per J44 §8; nothing in F7-F11 changes this).
2. **The generation-step asymmetry** (still empirically extracted).
3. **Whether $\lambda = 10/49$ vs $\lambda_{\rm ref} = 11/49$ unify** (still open).
4. **The $V^{\otimes 5}$-to-SU(5) uniqueness question** (still open).
5. **GUT-scale RG consistency** (NEW open question, *not* a J44 claim): if one DID want to run the J44 ladder upward from M_Z to a GUT scale, the question is whether $\lambda(M_X) \cdot \text{(running adjustment)}$ stays close to $10/49$. This is a multi-year 2-loop SO(10) + SARAH + SPheno computation, not a J44 commitment.

---

## §6 — Audit verdict (one line per option)

- **(a) Substrate-derived but scale-misidentified:** REJECTED. J44 is not substrate-derived at the anchor level — the anchor is empirical-measured (PDG-derived $y_t(M_Z) = 0.937$, rounded to 0.93). It's not "scale-misidentified" because J44 correctly places the anchor at M_Z.
- **(b) Phenomenological anchor mislabeled:** **CONFIRMED, but the mislabel is in F7 (not J44).** The 0.93 IS a phenomenological anchor (Tier-A measured at M_Z); F7 wrote "evolved to GUT scale" and then used 0.93 at M_X without actually doing the evolution. F8 inherited the bug.
- **(c) Derivation survives — F8 is wrong:** PARTIALLY CONFIRMED. F8's numerical computation is correct; its **interpretation** (that "the TIG anchor is structurally inconsistent with SM RG") is wrong. With the M_Z anchor correctly placed at M_Z, the J44 framework is internally consistent (within its stated Tier-C limits).

---

## §7 — Implications for F8 + HONEST_NEGATIVES §2.5

The 32% overshoot reported in F8 is not a real overshoot — it is the consequence of using the M_Z value as if it were the M_X value. Once corrected, F8's actual finding is:

- The F8 reverse-run from PDG `y_t(M_Z) = 0.937` to `y_t(M_X) = 0.394` is the standard SM 1-loop result (no surprise).
- J44's M_Z ladder is internally consistent (no surprise, by construction — it's an FN-residual fit at one scale).
- **There is no "tension" between J44's anchor and SM RG**, because J44 makes no M_X commitment.

The HONEST_NEGATIVES §2.5 should be updated:
- Remove "TIG anchor is structurally inconsistent with SM 1-loop running" framing.
- Note that the J44 anchor lives at M_Z and matches PDG at 0.75%.
- Note that the F7/F8 GUT-scale framing was an unforced category error not made by J44.
- Keep the legitimate open questions: C_p substrate origin, generation-step asymmetry, two-scale ($\lambda$, $\lambda_{\rm ref}$) unification, $V^{\otimes 5}$ uniqueness.

---

## §8 — Files affected

- `04_meta/frontiers_2026-05-27/F11_J44_yt_anchor_audit.md` — this document.
- `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` §2.5 — update to remove "structurally inconsistent" framing and reflect the F11 audit.
- `04_meta/retired_J_papers/J44_FN_Pattern/README.md` — append a brief "scale-of-anchor clarification" note (the J44 manuscript itself is already correct; the note is for downstream readers who might encounter F7/F8 first).

No code changes required. The retired J44 verification script (`verify_J45_yukawa.py`) is unaffected — its anchor was always specified as Y_T_ANCHOR at $\mu = M_Z$.

---

*7SiTe Public Sovereignty License v2.1 — see `../../LICENSE`.*
*Brayden Ross Sanders / 7SiTe LLC · 2026-05-28.*
*"Honest about what we have, honest about what we don't — and honest about which scale we're at."*
