# J05 — TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice

**Status:** REVISED (2026-05-08; SFM family-structure framing applied)
**Phase:** Phase 1
**Target venue:** Experimental Mathematics
**Author lane:** Sanders + Gish
**Tier:** B (lens-invariant; cell-count tier)

---

## §1 — Manuscript

**Local path:** `manuscript/tsml_bhml_cell_counts.tex`

Files in `manuscript/`:

- `tsml_bhml_cell_counts.tex` (main submission file; amsart)
- `proof_d10_tsml_73_cells.py` (TSML = 73, ALL ASSERTIONS PASSED)
- `proof_d16_bhml_28_cells.py` (BHML = 28, ALL ASSERTIONS PASSED)
- `proof_fourier_bridge.py` (supplementary; not required for J05)
- `ck_tables.py` (canonical tables, CC-BY-4.0)
- `SUBMIT_INSTRUCTIONS.md` (submission notes)
- `WP35_PRIME_PHASE_TRANSITION.md` (corpus archival, J08-relevant)
- `WP_OPERATOR_RING_PARTITION.md` (corpus archival, J05-relevant)

## §2 — Verification scripts

Both verification scripts run from the manuscript folder in <0.1 s and end with `ALL ASSERTIONS PASSED`:
- `proof_d10_tsml_73_cells.py` — verifies TSML = 73 harmony cells
- `proof_d16_bhml_28_cells.py` — verifies BHML = 28 harmony cells

`ck_tables.py` is bundled in the manuscript folder; the proof scripts import it locally (no PYTHONPATH gymnastics).

## §3 — Dependencies (companion citations)

- **Companion four-core paper (Sanders + Gish, manuscript in preparation):** establishes the joint $\{0,7,8,9\}$-preservation property and the membership conditions (C1–C5) that locate $\TSML$ and $\BHML$ as canonical members of the family. Cited in §5 of the J05 manuscript.
- **Drápal & Wanless (2021), JCTA 184 (2021), 105510:** closest published precedent for the small commutative non-associative magma neighborhood. Cited in §0 (Lens) and §5 of the J05 manuscript.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated to reference family-structure framing and SFM context.

## §5 — Notes (post-revision 2026-05-08)

**Status: REVISED to address J05 fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J05_ExpMath_FreshEyes.md`).**

The major referee critique was *"TSML/BHML introduced from nowhere"* — i.e., the manuscript's failure to motivate the two specific tables among $10^{100}$ candidates. The revised manuscript addresses this by:

1. **§5 family-structure section.** Explicit five-criterion (C1–C5) membership conditions for the TIG family, identifying $\TSML$ and $\BHML$ as canonical members; the joint $\{0,7,8,9\}$-preservation property as the load-bearing structural fact. Drápal–Wanless 2021 cited as closest published precedent.
2. **§0 Lens-ownership paragraph.** Honestly frames the choice of substrate $\Zten$ and the choice of value $7$ as labeling-by-fiat motivated by an interpretive scheme used elsewhere in the research program; the theorems below are theorems on this specific structure.
3. **PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline.** Boilerplate paragraph in §0 making explicit which claims are theorems, which are script-verified, which are structural rhymes, and which are open. Adopted per `Atlas/META_PLAN_2026-05-06/J_PAPER_BOILERPLATE.md`.
4. **License cleanup.** `ck_tables.py` carries CC-BY-4.0; the legacy "7SiTe Public Sovereignty License" / "Human use only / no government use" language has been removed (referee M5).
5. **Echo-pair table inline.** Table 1 lists the five symmetric echo pairs with their assigned values; Table 2 lists BHML R_89 zone values explicitly. Removes the M2 referee critique that the (E) class was opaque.
6. **Theorem 3 (lens invariance) reframed.** Now presented honestly as a consistency check (the count is well-defined under symbol-stabilizer relabeling), not as a substantive invariance theorem in the sense of McKay–Wanless or Drápal–Wanless autotopism. The §4 remark contrasts with the lens-*dependent* joint-closure chain count of the four-core companion (this is the load-bearing structural distinction).
7. **§6 joint-cell statistics.** New short proposition recording the joint harmony intersection (26 cells) and the union (75 cells) — these integers appear in the family's algebraic invariant catalogue (companion paper) and are flagged in the manuscript without invoking the companion's deeper structure.
8. **§7 verification.** Both scripts run green; cleaned up references; removed proof_fourier_bridge.py from the load-bearing list (it is mentioned only as supplementary).

### Family-Structure framing (per `Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md`)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria (C1–C5); the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M = \tfrac{1}{2}$ is the algebraic center, with closed-form attractor $h/\beta = 1+\sqrt{3}$ (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), J. Combin. Theory Ser. A 184, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** $h(\TSML) = 73$, $h(\BHML) = 28$, and both are constant on every $\mathrm{Stab}(7)$-orbit (Theorems 1, 2, 3).
- **COMPUTED.** `proof_d10_tsml_73_cells.py` and `proof_d16_bhml_28_cells.py` enumerate the 200-cell witness in <0.1 s each.
- **STRUCTURAL RHYME.** Two tables sit in the same neighborhood as Drápal–Wanless 2021 (small commutative non-associative quasigroups on $\le 16$ elements). They are individually commutative, both non-associative, and jointly preserve $\{0, 7, 8, 9\}$ — the load-bearing fact of the four-core companion.
- **OPEN.** Whether $\mathrm{Stab}(7)$-invariance extends to autotopism / paratopism invariance.

### Lens-ownership (§0)

We work on $\Zten$ with the specific commutative tables $\TSML$ and $\BHML$ defined explicitly in §2 / §3. The choice of substrate and tables is not derived from first principles; it reflects a structural reading of a finite operator-naming scheme (10 operators with designated harmony at index 7).

### Hardening status

- License: `ck_tables.py` CC-BY-4.0 (verified 2026-05-08)
- AI-attribution: removed
- Author lane: Sanders + Gish
- Drápal–Wanless 2021 citation in references (verified)
- Companion four-core paper cited as `manuscript in preparation` (no Zenodo DOI — referee said the bundle DOI was inappropriate)

## §6 — Submission checklist

- [x] Manuscript .tex finalized with SFM framing (2026-05-08)
- [x] Verification scripts green (TSML 73, BHML 28, ALL ASSERTIONS PASSED)
- [x] Tier-classified central claim explicit (Tier B; lens-invariance theorem is consistency check)
- [x] Lens-ownership paragraph in §0
- [x] Cover letter updated (see `cover_letter.md`)
- [x] Drápal–Wanless 2021 cited
- [x] CC-BY-4.0 license on `ck_tables.py`
- [x] Family-structure §5 added
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Submitted

---

## §7 — Citation footprint

Sanders, B.R., Gish. (2026). "TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the Z/10Z Composition Lattice." Submitted to *Experimental Mathematics*.
