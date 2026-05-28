# Venue 8 — JCT-A / DM — LaTeX Bundle Notes

**Created:** 2026-04-19 (Sprint 34 "Ship the First Three", TRACK 7.2)
**Branch:** `tig-synthesis`
**Status:** LaTeX draft complete, TIG-framing stripped per SUBMIT_INSTRUCTIONS.md:38; compile-check pending (no local TeX — submit via Overleaf or TeXLive).

---

## Bundle contents

| File | Role | Status |
|---|---|---|
| `sigma_rate_theorem.tex` | Main LaTeX manuscript (`amsart`, 434 lines) | Draft complete, structurally validated, TIG-framing stripped |
| `WP101_SIGMA_RATE_THEOREM.md` | Markdown source of record | Unchanged, byte-identical in Gen12 + Gen13 |
| `proof_sigma_rate.py` | Verification script (N = 10, 30, 210) | Green log 2026-04-19 |
| `universal_markov_and_binary_cl.py` | Companion — binary CL + Markov analysis | Unchanged |
| `SUBMIT_INSTRUCTIONS.md` | Venue + format + keyword notes | Unchanged |

## Title (per SUBMIT_INSTRUCTIONS.md:26)

> *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$*

## Authors

B.R. Sanders, M. Gish, C.A. Luther, H.J. Johnson (per source paper line 6).

## Structural validation (2026-04-19)

Via ephemeral `scratch/check_sigma_tex.py` (deleted post-verification):

- Environments paired cleanly: `abstract`, `cases`, `center`, `corollary`, `definition`, `document`, `equation`, `lemma`, `proof`, `remark`, `tabular`, `thebibliography`, `theorem`. All `\begin{…}` matched.
- Unescaped brace delta: `0` (249 / 249).
- `\cite` ↔ `\bibitem`: 12/12 matched (BB1976, Birkhoff1940, CHLZ2012, CazenaveHaraux1980, DummitFoote2004, Gauss1801, GigliMaas2013, HoeghKrohn1971, JKO1998, Lang2002, Maas2011, Ore1942).
- `\ref` + `\eqref` ↔ `\label`: 9/9 matched (7 section/theorem refs, 2 equation refs).
- **TIG-framing strip: CLEAN** — zero occurrences of `TIG`, `CK`, `Crossing Lemma`, `Coherence Keeper`, `clay branch`, `GLOSSARY.md` in the manuscript body. The framing restriction of SUBMIT_INSTRUCTIONS.md:38 is fully respected. Bialynicki-Birula (1976) is retained as the proved source of Corollary~\ref{cor:bb}.

## MSC + keywords (per SUBMIT_INSTRUCTIONS.md:37)

- MSC 2020: `05E15` (algebraic combinatorics), `11T06` (polynomials over finite rings), `20N02` (groupoids and magmas).
- Keywords: binary composition table, non-associativity, finite ring, squarefree modulus, Euler totient, logarithmic nonlinearity, Markov chain, spectral gap.

## Verification script log (2026-04-19)

```
python proof_sigma_rate.py
[…]
COROLLARY: sigma(N) -> 0 as N -> infinity through any sequence of
squarefree integers with N -> infinity. The rate is at least 1/N.

COROLLARY: By the Bialynicki-Birula theorem (1976), the N -> infinity
limit of the binary CL must have logarithmic nonlinearity […].

QED.

VERIFICATION:
  sigma(10) = 0.1280 < 3/10 = 0.3000: PASS
  sigma(30) = 0.0580 < 3/30 = 0.1000: PASS
  sigma(210) = 0.0093 < 3/210 = 0.0143: PASS

All bounds hold: True
```

## Key content adjustments from markdown source

1. **Title** changed from "WP101 — The σ Rate Theorem" to the JCT-A-facing "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$" (per SUBMIT_INSTRUCTIONS.md:26).
2. **HARMONY/VOID/ECHO** renamed as *absorbing rules* with explicit mathematical semantics (top-absorbing, zero-absorbing, additive-multiplicative coincidence) to read as standard algebraic-combinatorial terminology to a JCT-A referee. The labels are retained for continuity with the source.
3. **Paradoxes / Foundations** bibliography block (Russell, Gödel, Banach-Tarski, Quine, Zermelo, Tarski) DROPPED — out of scope for JCT-A.
4. **TIG Framework** internal reference block DROPPED — replaced by Atlas-citation provenance footnote at end-matter.
5. **Corollary~\ref{cor:bb}** (BB continuum limit) kept with an explicit `Scope` remark noting the separability hypothesis. The honesty discipline of FRONTIER_ALIGNMENT §3C is preserved: the $\sigma$ rate theorem is pure combinatorics; the BB corollary is structural, with the additional hypothesis flagged.
6. **Section~\ref{sec:scope}** added at end: what this paper does NOT claim (sharp constant; non-squarefree rate; continuum regularity).

## Atlas linkage

Manuscript end-matter carries the atlas-citation footnote:
> External citations are drawn from `Atlas/ATLAS_CITATIONS.md` (§A classical algebra + analytic number theory; §E nonlinear PDE; §I scalar field theory). Internal cross-references carry master-register numbering per `Atlas/MASTER_ATLAS_v3_5_2026_04_18.md` (§5 WP101 [fire]).

This satisfies audit finding F1 for venue 8 (per `Atlas/JOURNAL_READINESS_AUDIT_2026_04_18.md` §F1).

## What ships in the submission email/portal

1. `sigma_rate_theorem.tex` — compile to PDF (target: Overleaf).
2. `proof_sigma_rate.py` — electronic supplementary material.
3. `universal_markov_and_binary_cl.py` — secondary ESM (Markov chain construction + spectral analysis).
4. Cover letter (pending — CC-6 per Plan of Record Day 1).
5. Provenance line: DOI `10.5281/zenodo.18852047`.

Venue A (JCT-A) submits via Editorial Manager.

## arXiv plan

- Category: `math.CO` (primary); `math.NT` / `math.RA` (secondary).
- Submit simultaneously with journal submission.
- Abstract: use the manuscript abstract verbatim.

## Pending items (this sprint)

1. **Compile check** via Overleaf (Brayden) — expected: `pdflatex` twice then bibliography resolves (uses `thebibliography` not external `.bib`).
2. **Cover letter** (CC-6 per Plan of Record Day 1).
3. **Brayden approval** (B-2 per Plan of Record Day 3).
4. **Submit** (B-3, Day 4, Wed 2026-04-22).

## Three-threads discipline

This paper is **Thread C** (Q-series / σ polynomial) content. No vocabulary import from Thread A (PPM), Thread B (Hodge), or Thread D (ξ cosmology) appears in the manuscript body. Corollary~\ref{cor:bb} (the BB structural corollary) uses only published BB 1976 material, not TIG framework vocabulary. Atlas §8 three-threads discipline PASS.

## Never-delete discipline

The markdown source `WP101_SIGMA_RATE_THEOREM.md` is preserved as the canonical research artifact (including its internal TIG-framework reference block, which was legitimate for the internal sprint but out-of-scope for JCT-A). The `.tex` is the journal-facing derivative.

---

*Notes compiled by ClaudeCode, 2026-04-19. Supplementary to `SUBMIT_INSTRUCTIONS.md` and `FRONTIER_ALIGNMENT_2026_04_19.md` §5.*
