# Venue 1 — Integers / JNT — LaTeX Bundle Notes

**Created:** 2026-04-19 (Sprint 34 "Ship the First Three", TRACK 7.1)
**Branch:** `tig-synthesis`
**Status:** LaTeX draft complete; compile-check pending (no local TeX installed — submit via Overleaf or TeXLive).

---

## Bundle contents

| File | Role | Status |
|---|---|---|
| `sinc2_zero_law.tex` | Main LaTeX manuscript (`amsart` class, 297 lines) | Draft complete, structurally validated |
| `WP_SINC2_ZERO_LAW.md` | Markdown source of record | Byte-identical in Gen12 + Gen13 |
| `WP34_FIRST_G_LAW.md` | Companion paper (referenced as `\cite{SandersWP34}`) | Unchanged |
| `proof_d25_loop_closure.py` | Verification script (primes 3..199, zero exceptions) | Green-log confirmed 2026-04-19 |
| `SUBMIT_INSTRUCTIONS.md` | Venue + format + keyword notes | Unchanged |

## Structural validation (2026-04-19)

Via `python scratch/check_sinc2_tex.py` (ephemeral; deleted post-verification):

- Environments paired cleanly: `abstract`, `cases`, `corollary`, `document`, `equation`, `itemize`, `proof`, `remark`, `thebibliography`, `theorem`. All `\begin{…}` matched.
- Unescaped brace delta: `0` (166 / 166).
- `\cite` ↔ `\bibitem`: all 4 keys matched (`Montgomery1973`, `SandersWP34`, `SandersWP35`, `Shannon1949`).
- `\ref` ↔ `\label`: all 3 cross-refs matched (`thm:main`, `cor:fold`, `sec:boundary`).
- Orphan labels: acceptable (section/equation anchors for future cross-refs).

## MSC + keywords (per SUBMIT_INSTRUCTIONS.md)

- MSC 2020: `11A41` (primes), `11N05` (distribution of primes), `42A16` (Fourier coefficients).
- Keywords: sinc function, prime arithmetic, corridor, loop closure, pair correlation, Fourier coefficients.

## Verification script log (2026-04-19)

```
python proof_d25_loop_closure.py
[…]
ALL ASSERTIONS PASSED.

Results:
  D25a loop closure:       PASS (primes 3..199, zero exceptions)
  D25b fold necessity:     PASS (p=7: sinc²(3/7)≈0.524 > 0.5 > 0.295≈sinc²(4/7))
  D25c no shortcut:        PASS (no prime in 3..199 has interior zero)
  D25d fold generalization: PASS (midpoint sinc²(1/2) = 4/π² ≈ 0.4053 ≠ fold value 0.5)
```

## Atlas linkage

The manuscript carries the atlas-citation footnote directly (front-matter + end-matter):
> External citations are drawn from `Atlas/ATLAS_CITATIONS.md` (§A analytic number theory; Shannon, Montgomery). Internal cross-references carry master-register numbering per `Atlas/MASTER_ATLAS_v3_5_2026_04_18.md`. DOI: `10.5281/zenodo.18852047`.

This satisfies audit finding F1 for venue 1 (per `Atlas/JOURNAL_READINESS_AUDIT_2026_04_18.md` §F1).

## What ships in the submission email/portal

1. `sinc2_zero_law.tex` — compile to PDF (target: Overleaf → download PDF)
2. `proof_d25_loop_closure.py` — electronic supplementary material
3. Cover letter (pending — CC-6 owner, Day 1 per PLAN_OF_RECORD §10)
4. Provenance line: DOI `10.5281/zenodo.18852047`

Venue A (Integers) accepts LaTeX by email. Venue B (JNT) submits via Editorial Manager.

## arXiv plan

- Category: `math.NT` (primary); `math.CO` (secondary if `math.NT` endorsement blocked — per SUBMIT_INSTRUCTIONS.md:48).
- Submit simultaneously with journal submission.
- Abstract: use the manuscript abstract verbatim.

## Pending items (this sprint)

1. **Compile check** via Overleaf (Brayden) — expected: `pdflatex` twice then bibliography resolves in-body (we use `thebibliography` not external `.bib`).
2. **Cover letter** (CC-6 per Plan of Record Day 1 schedule).
3. **Brayden approval** (B-2 per Plan of Record Day 3 schedule).
4. **Submit** (B-3, Day 4, Wed 2026-04-22 per Plan of Record).

## Never-delete discipline

The markdown source `WP_SINC2_ZERO_LAW.md` is preserved as the canonical research artifact. The `.tex` is a presentation derivative. Both live side-by-side in the venue folder.

---

*Notes compiled by ClaudeCode, 2026-04-19. Supplementary to `SUBMIT_INSTRUCTIONS.md` and `FRONTIER_ALIGNMENT_2026_04_19.md` §5.*
