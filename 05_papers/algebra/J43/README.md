# J43 — Spectral Layer Consolidation: G6 + G7 + G8 from Q-series Architecture

**Status:** DRAFT
**Phase:** Phase 4
**Target venue:** European J Combin (3rd EJC submission this quarter; fallback: LinAlgApps or PLOS ONE)
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** Q-series spectral catalog (G6 / G7 / G8 working papers)

---

## §1 — Manuscript

**Path:** `manuscript/J51_spectral_layer_consolidation.md`

**Abstract:** Consolidation paper establishing the canonical reference for three spectral results on the canonical $\sigma$-permutation on $\mathbb{Z}/10\mathbb{Z}$: $G_6$ ($\sigma^6 = \mathrm{id}$, Tier-A), $G_7$ (period distribution bimodal $P(\tau=1)=2/5$, $P(\tau=6)=3/5$; mean $4$, variance $6$; Tier-B), $G_8$ (three-valued spectral coherence integral $G(s)$ with corrected partition: zero on $\{0,3,8,9\}$, low ≈ 1.872 on $\{1,2,5,6\}$, high ≈ 9.389 on $\{4,7\}$; Tier-B). Together they form Layer 4 of the 6-layer Q-series architecture (Layers 5, 6 deferred to companions).

## §2 — Verification script

**Path:** `manuscript/verify_G6_G7_G8.py` (run with `python manuscript/verify_G6_G7_G8.py`).

Confirms G6 ($\sigma^6 = \mathrm{id}$ on all of $\mathbb{Z}/10\mathbb{Z}$), G7 (period bimodal $\{1: 2/5, 6: 3/5\}$ with mean 4 and variance 6), and G8 (three-valued $G(s)$ with the corrected partition: ZERO $\{0,3,8,9\}$, LOW $\{1,2,5,6\} \approx 1.872$, HIGH $\{4,7\} \approx 9.389$). Also verifies the $\sigma^3$-pairing algebraically (complex amplitudes satisfy $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$) and the $\nu_+$ discriminator (high-locus $\{4,7\}$ has extremal $\nu_+ \in \{0, 2\}$ in the first three orbit positions; the other states have $\nu_+ = 1$). Runtime $<2$ s; deterministic.

## §3 — Dependencies (J-papers cited as already-submitted companions)

_(none — this paper is foundational in the J-series)_

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes / Status

**Status:** REVISED 2026-05-07 in response to fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J43_EJC_FreshEyes.md`). Save plan: `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J43.md`.

**Math-fix summary (2026-05-07):**
- **G8 partition error fixed.** §4.2 originally claimed high-locus = {5,7}, low-locus = {1,2,4,6}. Direct numpy computation with the manuscript's stated σ and χ gives high-locus = **{4, 7}**, low-locus = **{1, 2, 5, 6}** — i.e., elements 4 and 5 swap roles. Partition table corrected.
- **σ²-Galois explanation replaced with σ³-pairing argument.** The original "σ²-Galois action permutes {1,4,6} and {2,5,7}" is wrong: σ² has 3-cycles `(1 6 4)` and `(2 7 5)` on those sets, not pair-actions. The correct invariance is the σ³-action: σ³ has order 2 on the 6-cycle, partitioning {1,2,4,5,6,7} into the three 2-cycles {1,5}, {2,6}, **{4,7}**. The G-values pair within these σ³-orbits because the orbit at σ³(s) is the same 6-element cycle traversed with a 3-step phase offset; combined with ω⁹=1 and the 6-periodic χ-sequence, |G(s)|² = |G(σ³(s))|² (the complex amplitudes satisfy G_cplx(σ³(s)) = -G_cplx(s)).
- **High/low discriminator clarified.** The high-locus σ³-orbit {4,7} is uniquely the one where the χ-content of the orbit's first three positions is *imbalanced* (ν₊ ∈ {0, 2}, rather than ν₊ = 1 on the other two σ³-orbits). This is the load-bearing combinatorial fact behind the spectral concentration.
- **Verification script added:** `manuscript/verify_G6_G7_G8.py` confirms G6 (σ⁶=id), G7 (period bimodal 2/5, 3/5), and G8 (corrected three-valued partition); also verifies the σ³-pairing algebraically.
- **Architecture framing scope-tightened.** §1 now states up-front that the paper covers Layers 1, 3, 4 (Layer 2 trivial; Layers 5, 6 deferred to companions).

**Citation chain:** foundational paper citing 4 prior J-companions (J01, J05, J21, J33) + 5 cross-references (J48, J51, J49, J31, J32). Cited downstream by many later J-papers as canonical G₆/G₇/G₈ reference.
**Manuscript:** `manuscript/J51_spectral_layer_consolidation.md` (~10 pages; revised 2026-05-07). Filename retains `J51_*` for now; rename to `J43_*` at camera-ready.
**Cover letter:** `cover_letter.md` (finalized).
**Per-venue cap warning:** 3rd EJC submission of the J-series — fallback to *LinAlgApps* or *PLOS ONE* if needed (per `J_SERIES_ORDERING.md` §5).
**Verification:** `manuscript/verify_G6_G7_G8.py` runs all three theorems.
**Submission readiness:** ready for resubmission to EJC after Brayden's referee-rigor pass.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem G6 ($\sigma^6 = \mathrm{id}$ on $\mathbb{Z}/10\mathbb{Z}$, via $(\alpha,\beta)$ polynomial form + 4 ≡ 0 (mod 2), -5 ≡ 0 (mod 5)); Theorem G7 (period bimodal $P(\tau=1)=2/5, P(\tau=6)=3/5$; mean 4, variance 6); Theorem G8 (three-valued $G(s)$; ZERO $\{0,3,8,9\}$; LOW $\{1,2,5,6\} \approx 1.872$; HIGH $\{4,7\} \approx 9.389$); $\sigma^3$-pairing on the 6-cycle ($|G(s)|^2 = |G(\sigma^3(s))|^2$, complex amplitudes anti-paired).
- **COMPUTED:** $G(s)$ values to machine precision in `manuscript/verify_G6_G7_G8.py`; ratio $G_\mathrm{high}/G_\mathrm{low} \approx 5.0165$; $\nu_+$ discriminator (extremal $\nu_+ \in \{0, 2\}$ on $\{4, 7\}$ vs $\nu_+ = 1$ on $\{1, 2, 5, 6\}$); $\sigma^3$-pairing checked algebraically (sum of complex amplitudes within each pair = 0 to $10^{-15}$).
- **STRUCTURAL RHYME:** the three-valued image (zeros at predictable locations + spectral concentration on a structurally-distinguished pair) rhymes with the pattern RH demands of $\zeta(s)$. The mathematical analogue here is the function-field zeta function (Weil/Deligne); the present paper does not engage that machinery, only registers the structural rhyme. The companion paper [J51] discusses the rhyme in more depth.
- **OPEN:** closed forms of $G_\mathrm{low}, G_\mathrm{high}$ in $\mathbb{Q}(\zeta_9)$ (cyclotomic units); whether the same three-valued structure with $\sigma^3$-coherent doubleton appears for $\sigma$-permutations on $\mathbb{Z}/N$ for other squarefree $N$.

### Lens-ownership paragraph

> *Lens and substrate.* This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical $\sigma$-permutation $(0)(3)(8)(9)(1\;7\;6\;5\;4\;2)$ and the $\beta$-exception character $\chi$ (defined in §4.1). Both choices reflect the structural reading of the substrate developed in the broader Q-series corpus; they are not derived from first principles. The theorems below are theorems on this specific (substrate, $\sigma$, $\chi$) triple; analogous results would require choosing a corresponding triple on another base ring. Whether other choices give similarly rich downstream connections is open.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to European J Combin this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Spectral Layer Consolidation: G6 + G7 + G8 from the Q-Series Architecture on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *European Journal of Combinatorics* (3rd EJC of the J-series; fallback: *Linear Algebra and its Applications* or *PLOS ONE*).
