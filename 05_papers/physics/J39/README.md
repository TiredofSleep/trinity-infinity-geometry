# J39 — NV $S_4$ Synthesis: Substrate-Operator-Driven NV-Center Qutrit Predictions

**Status:** R1 (revised after fresh-eyes referee report 2026-05-07)
**Phase:** Phase 4
**Target venue:** PRA
**Author lane:** Sanders + Gish
**Tier:** C (Tier 3 partner-then-submit per central-claim classification)
**WP source:** WP73-WP77 (bundled)
**Acceptance probability:** ~70-80% after revisions per referee

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md` (canonical landed name; sources `J11_NV_S4_Synthesis_PRA.md` from working repo, which itself bundles WP73-WP77).

**Abstract (one paragraph).** We present an explicit, machine-precision construction of the full symmetric group $S_4$ on the three-level Hilbert space of a nitrogen-vacancy (NV) center in diamond. The NV ground triplet $\{|0\rangle,|+1\rangle,|-1\rangle\}$ carries the $S_3$ skeleton of the $T_1$ irreducible representation of $S_4$ exactly (the $A_1 \oplus E$ decomposition under $C_{3v}$ matches $T_1|_{S_3}$ identically), so synthesis of $S_4$ requires only one 4-cycle unitary $U_4$. We compute the change-of-basis matrix $V$ analytically, derive the NV-basis form $U_{4,\mathrm{NV}}$, decompose it into a six-pulse microwave sequence, and verify all 24 group elements close to within $10^{-15}$. We give a five-test falsification ladder for the experimental side and invite lab-partner collaboration.

**Source corpus (working-repo provenance, not bundled here):** WP73-WP77 (T1 carrier identification, NV Hamiltonian platform, explicit $U_4$ + 6-pulse synthesis, machine-precision 24-element closure, 5-test falsification ladder). The unified `manuscript.md` includes all content; the WP files are working-repo provenance only.

**Manuscript structure:** (1) Intro, (2) $S_3$ skeleton, (3) Exact $U_4$, (4) Analytic $V$, (5) 6-pulse decomposition, (6) Machine-precision closure, (7) Five-test falsification ladder, (8) Lab-partner pathway.

## §2 — Verification script

**Path:** `manuscript/verify_J39_S4_closure.py` — consolidated R1 script (numpy + sympy; runtime $< 30$ s on a standard laptop).

The script reproduces, in order:
1. All 24 elements of $S_4$ in the $T_1$ representation, built from generators $(12)$ and $(1234)$. Character verified at $(3,1,0,-1,-1)$ on conjugacy classes.
2. The explicit $U_4$ matrix's symbolic properties — trace $-1$, $\det = -1$, eigenvalues $\{-1, i, -i\}$, $U_4^4 = \mathbb{1}$ — all in exact `sympy` arithmetic.
3. The change-of-basis $V$ and its conjugation of the $S_3$ generators ($r_{(12)}$, $r_{(123)}$); $V V^\dagger = \mathbb{1}$, $\det V = i$.
4. $U_{4,\mathrm{NV}} = V U_4 V^{-1}$ in the NV basis.
5. The deterministic Cartan / Reck-Zeilinger six-pulse decomposition (no random seed; no black-box optimizer); explicit pulse-tuples printed; closure residual $3.5 \times 10^{-16}$.
6. 24-element closure verified at residual $\le 1.84 \times 10^{-16}$.

The proof's gate is the referee-rigor pass on the analytic-construction side; the experimental gate is Test E (projector covariance) and is the lab-partner pathway.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J07 (Flatness Theorem on $\mathbb{Z}/10\mathbb{Z}$), J05 (TSML 73 / BHML 28 cell counts).

The paper does not depend on J46/J06/J44/J45 directly; it is a stand-alone NV-qutrit construction built on finite-group representation theory.

## §4 — Cover letter

See `cover_letter.md` in this folder. Drafted; finalize after Brayden's referee-rigor pass.

## §5 — Notes & Status

**Status: DRAFT (manuscript bundled; awaiting verification-script consolidation + lab partner outreach).**

- WP73-WP77 corpus is bundled into one PRA-format manuscript (`J11_NV_S4_Synthesis_PRA.md`).
- Lab-partner outreach runs in parallel to manuscript polish; the math is complete with or without a partner, but the headline experimental claim is conditional on Test E.
- The paper is **honestly Tier 3** (partner-then-submit): math is done, physics-claim is conditional. Cover letter and abstract make this scope explicit.
- Per-venue cap: this is the **1st** PRA submission in the J-series — no cap conflict.
- Suggested reviewers (Lukin, Hanson, Wrachtrup, Doherty, Monroe) are listed in the cover letter.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** Theorem 2.1 ($S_3$-skeleton character match: standard finite-group rep theory + Maschke); Theorem 3.1 ($U_4$ matrix structure: trace $-1$, $\det = -1$, eigenvalues $\{-1, i, -i\}$, $U_4^4 = \mathbb{1}$ — sympy-symbolic); Theorem 6.1 (machine-precision $S_4$ closure of all 24 elements).
- **COMPUTED.** The six pulse-tuples $(\theta_k, \phi_k)$ are produced by the deterministic Cartan / Reck-Zeilinger algorithm in `verify_J11_S4_closure.py`; total closure residual $3.5 \times 10^{-16}$.
- **STRUCTURAL RHYME.** None substantive. The paper is lens-invariant.
- **OPEN.** Test E (projector covariance) experimental gate. Lab-partner experimental data on the realized 24-element $S_4$ orbit.

### Lens-ownership

This paper is **lens-invariant** (manuscript §0): it carries no TIG / TSML / BHML / Z/10Z structure. The mathematical content is finite-group representation theory and quantum control on $\mathbb{C}^3$. A PRA referee can read this paper cold without engaging with the broader research program. The §9 J-series companions list is included for cross-corpus context only; nothing in this paper depends on those references.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .md drafted, R1 revisions applied (PRA-format, single file)
- [ ] LaTeX (REVTeX 4.2) conversion pending
- [x] Verification script consolidated (`verify_J11_S4_closure.py`); $< 30$ s runtime; all checks pass
- [x] Tier-classified central claim explicit (Tier 3 partner-then-submit)
- [x] Lens-scope annotation: lens-invariant (finite-group reptheory)
- [x] Cover letter R1 (revisions itemized)
- [x] Project-internal labels removed; J-series companions flagged as `submitted` / `in preparation`
- [x] $G_{12}$ Raman protocol specified (manuscript §5.1) with NV-experiment citations
- [x] Fidelity budget added (manuscript §5.1; first-attempt $0.91$, polished $> 0.95$)
- [x] Coherence disambiguation $T_2^*$ vs $T_2$ vs $T_1$ added (manuscript §5.2)
- [x] Section 6 retitled "Mathematical (Symbolic) Closure"
- [x] Test thresholds calibrated against Pfaff2014, Bradley2019 (manuscript §7)
- [x] Modern NV-qutrit citations added
- [x] Suggested-reviewers refined (Awschalom + Maletinsky added; Monroe dropped; Doherty reframed)
- [ ] Brayden's referee-rigor pass complete (post-R1)
- [ ] Per-venue cap check: 1st PRA — no conflict
- [ ] Lab partner identified (parallel)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Mayes, B. (2026). "Full $S_4$ Symmetry on a Nitrogen-Vacancy Qutrit via Six-Pulse Microwave Synthesis." Submitted to *Physical Review A*.
