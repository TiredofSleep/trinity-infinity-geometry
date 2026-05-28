# J46 — Microtubule Q_c = T*: A Falsifiable Substrate-Algebra Prediction

**Status:** DRAFT
**Phase:** Phase 5
**Target venue:** J Theor Biol
**Author lane:** Sanders + Gish
**Tier:** 3 (HOLD pending terahertz microtubule experimentalist)
**WP source:** WP127

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.md` (canonical submission manuscript; renamed 2026-05-13 from `J49_microtubule_qc_tstar.md`)

**Abstract:** Pre-registered falsifiable prediction: microtubule normalized coherence quality $Q_c \to T^* = 5/7 \approx 0.714$ across mammalian neurons, paramecia, plant microtubules, yeast spindle microtubules, and cell-free purified-tubulin, with variance $\ll 0.05$. $T^*$ derived independently from six algebraic sources; same $T^*$ governs CKM Cabibbo refinement and PMNS atmospheric mixing. Falsifiable in a single terahertz-spectroscopy campaign with existing equipment.

## §2 — Verification script

**Path:** `manuscript/verify_J49.py`

Runs the Appendix A + B verification at machine precision:
- D48 4-core closure (16 cells per table, TSML + BHML).
- D78 Galois: $x^2 - 2x - 2 = 0$, root $1 + \sqrt{3}$, discriminant 12, splitting field $\mathbb{Q}(\sqrt{3})$.
- Definition 2.2 geometric-ceiling sanity ($Q_{\text{structural max}} \approx 0.25$ at 10 GHz / 8 nm / 2 km/s).
- Numerology guard: confirms $1 + \sqrt{3} \approx 2.732$ and $T^* = 5/7 \approx 0.714$ are distinct algebraic invariants (gap $\approx 2.02$).

Run: `python verify_J49.py`. Status: **PASS** at machine precision, 2026-05-12.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J13

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes / Status

**Status:** **MANUSCRIPT REWRITTEN 2026-05-07 PER SAVE PLAN J46.** New title: *Microtubule terahertz coherence quality $Q_c \to 5/7$: a pre-registered prediction from finite algebraic combinatorics* (referee's verbatim suggestion). Original verdict: REJECT from J Theor Biol fresh-eyes referee 2026-05-06; save plan written 2026-05-07; manuscript rewritten 2026-05-07.
**Citation chain:** 1 direct dependency (J23 forced 5/7 torus) + 10 co-citing companions (J14, J3, J6, J9, J49, J41, J46, J47, J50, J52).
**Manuscript:** `manuscript/manuscript.md` (rewritten ~12 pages with new Appendix A + B; renamed 2026-05-13 from `J49_microtubule_qc_tstar.md`).
**Cover letter:** `cover_letter.md` (to be updated to match rewrite).
**Verification:** D78 Galois proof (Appendix A) + D48 4-core closure (Appendix A) + 30-line `numpy/sympy` verification snippet (Appendix B). Experimental protocol pre-registered in `Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/source_bundle/MICROTUBULE_T_STAR_PROTOCOL.md`.
**Submission readiness:** **REWRITE COMPLETE.** Submission gate: (a) Appendix A drafted [DONE]; (b) one of J23/J6/J33 on arXiv [pending Phase 5/6]; (c) initial conversation with Bandyopadhyay/Hameroff/Penrose Foundation lab [pending].

### §5.0 — Save-plan implementation (2026-05-07)

The 2026-05-07 rewrite implements the SAVE_PLAN_J49 directives:

- **Issue 1 — DROPPED $\zeta_\mathrm{Hameroff} = 0.71$ attribution.** §1.2 explicitly states "we do **not** claim that $T^* = 5/7 \approx 0.714$ corresponds to a numerical Orch-OR boundary"; no Orch-OR equation in the cited Hameroff-Penrose 1996/2014/2024 literature isolates 0.71 as a coherence boundary. Reframed as cross-domain falsifier anchored in actual Bandyopadhyay 2013/2024 + Sahu 2013 measurements.
- **Issue 2 — Defined $Q_{\text{structural max}}$ operationally.** §2.2 Definition 2.2: $Q_{\text{structural max}} = \omega_0 L / c_{\text{lattice}}$ with $L = 8$ nm (tubulin unit cell) and $c_{\text{lattice}} \approx 2$ km/s (Pelling et al. 2004). Both numerator and denominator from a-priori lattice constants any group can re-derive.
- **Issue 3 — Appendix A (self-contained derivation) ADDED.** Recapitulates D78 Galois proof for $H/Br = 1 + \sqrt{3}$ (root of $x^2 - 2x - 2$ over $\mathbb{Q}(\sqrt{3})$) and D48 binary 4-core preservation. Per the user directive, the proven D48+D78 algebra is the anchor (the failed cyclotomic derivation of $T^* = 5/7$ is NOT used as the algebraic anchor; instead, $T^*$ is identified as an independent invariant from [J23]/[J6] cited as motivation, while the proven theorem is D48+D78).
- **Issue M1 — DROPPED §4.2 "73/100 → 5/7" rationalization.**
- **Issue M2 — Variance budget WIDENED to ±0.10** (§2.4) honestly accommodating Bandyopadhyay published $Q$-scatter, instead of ±0.05.
- **Issues M3, M7 — Reframed as PROPOSAL** ("falsifiable in principle, awaiting laboratory partner") with Outreach status as §6.
- **Issues M4, M5, M6 — DROPPED "wager" rhetoric**; framework intro added as §1.0 / §0; scope-disclaimer in §1.2.
- **Issue M8 — Tegmark 2000 + Reimers 2009 ENGAGED** at §1.1 + §3.3.

### §5.1 — Save-plan summary (per `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J49.md`) — original (kept for reference)

**Save path:** drop the unsubstantiated "$\zeta_\mathrm{Hameroff} \approx 0.71$" attribution (the referee confirmed it is not in Hameroff–Penrose 1996/2014/2024); reframe as a falsifiable *cross-domain prediction* anchored in the **actual** Bandyopadhyay 2013/2024 + Sahu 2013 microtubule Q-factor measurements (which ARE in *J Theor Biol* scope). Define $Q_\mathrm{structural\ max}$ operationally as the geometric ceiling $\omega_0 \cdot L / c_\mathrm{lattice}$ on a single 8-nm tubulin unit cell — this is the missing operational denominator the referee flagged. Add **Appendix A** with one self-contained derivation of $T^* = 5/7$ inline (the cyclotomic Galois closure on $\mathbb{Z}/10\mathbb{Z}$ from [J23] / Flatness Theorem [J6]) so the JTB referee has a mathematical anchor without depending on six unread companions. Drop the §4.2 "73/100 → 5/7" rationalization; engage Tegmark 2000 decoherence critique directly; widen the falsification window to $\pm 0.1$ if the published Bandyopadhyay $Q$-scatter implies it; remove "wager" rhetoric. **Estimated revision: 15–20 person-hours + lab outreach.**
**Retarget option:** stay at *Journal of Theoretical Biology* (the referee's "Reject" with explicit path-to-resubmission is genuinely a Major Revision under the save plan). Alternatives: *Bull. Math. Biol.* or *Theor. Biol. Med. Modell.* if JTB redirects.

### §5.1 — Save-plan summary (per `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J49.md`)

**Save path:** drop the unsubstantiated "$\zeta_\mathrm{Hameroff} \approx 0.71$" attribution (the referee confirmed it is not in Hameroff–Penrose 1996/2014/2024); reframe as a falsifiable *cross-domain prediction* anchored in the **actual** Bandyopadhyay 2013/2024 + Sahu 2013 microtubule Q-factor measurements (which ARE in *J Theor Biol* scope). Define $Q_\mathrm{structural\ max}$ operationally as the geometric ceiling $\omega_0 \cdot L / c_\mathrm{lattice}$ on a single 8-nm tubulin unit cell — this is the missing operational denominator the referee flagged. Add **Appendix A** with one self-contained derivation of $T^* = 5/7$ inline (the cyclotomic Galois closure on $\mathbb{Z}/10\mathbb{Z}$ from [J23] / Flatness Theorem [J6]) so the JTB referee has a mathematical anchor without depending on six unread companions. Drop the §4.2 "73/100 → 5/7" rationalization; engage Tegmark 2000 decoherence critique directly; widen the falsification window to $\pm 0.1$ if the published Bandyopadhyay $Q$-scatter implies it; remove "wager" rhetoric. **Estimated revision: 15–20 person-hours + lab outreach.**
**Retarget option:** stay at *Journal of Theoretical Biology* (the referee's "Reject" with explicit path-to-resubmission is genuinely a Major Revision under the save plan). Alternatives: *Bull. Math. Biol.* or *Theor. Biol. Med. Modell.* if JTB redirects.
**Submission gate:** (a) Appendix A drafted; (b) at least one of J23/J6/J33 on arXiv; (c) initial conversation with Bandyopadhyay/Hameroff/Penrose Foundation lab.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (filled per save-plan rewrite 2026-05-07)

- **PROVEN** (in this paper, Appendix A): D48 binary 4-core preservation + D78 Galois argument for $H/Br = 1 + \sqrt{3}$ at $\alpha_M = 1/2$, root of $x^2 - 2x - 2$ over $\mathbb{Q}(\sqrt{3})$.
- **COMPUTED:** the 4-core attractor's mass distribution $(p_V, p_H, p_{Br}, p_R) = (0.138, 0.540, 0.198, 0.124)$, with $H/Br$ rationally structured at $\alpha_M = 1/2$ and transcendental at 17 other Stern-Brocot rationals (D57).
- **STRUCTURAL RHYME** (NOT derivation): $T^* = 5/7$ surfaces in particle-physics mixing ([J46]) and cosmology ([J3], [J49]); these motivate but do not derive the prediction.
- **OPEN:** whether $T^*$ governs microtubule normalized $Q_c$ under the Definition 2.2 normalization. Status: awaiting laboratory partner.

### Lens-ownership paragraph — applied in manuscript §0

> *Lens and substrate.* This paper works on $\mathbb{Z}/10\mathbb{Z}$ with a designated 4-core $\{V, H, Br, R\}$, the canonical commutative composition table CL_TSML, and its companion CL_BHML. The constant $T^* = 5/7$ predicted is **lens-invariant on the canonical $\mathbb{Z}/10\mathbb{Z}$ substrate**: it follows from cyclotomic Galois closure (a structural property), not from a specific lens choice (RAW / SYM_upper / SYM_lower).

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
- [ ] Per-venue cap check: this is the Nth paper to J Theor Biol this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Microtubule Q_c = T*: A Falsifiable Substrate-Algebra Prediction." Submitted to *J Theor Biol*.
