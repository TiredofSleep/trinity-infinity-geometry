# Track B — LaTeX Conversion Bones (DEFERRED)

**Status**: scaffolding for later session. Per user 2026-05-27: "leave the bones behind to finish track b later."

This document captures what's needed for each of J62/J61/J35 LaTeX conversion + arXiv submission, so when we come back to it the prep is in place.

---

## Common conversion pipeline

For each paper:
1. **pandoc** Markdown → LaTeX skeleton:
   ```bash
   pandoc manuscript.md -o manuscript.tex --to=latex --top-level-division=section
   ```
2. **Wrap in amsart preamble** (template below).
3. **Manual passes**:
   - Fix table formatting (pandoc tables → booktabs).
   - Convert ` ``` ... ``` ` code blocks → `verbatim` or `listings`.
   - Add `\newcommand` aliases for repeated notation (σ, ⋄, etc.).
   - Verify all `$...$` and `$$...$$` blocks compile.
4. **arXiv pre-check**:
   - Run `arxiv-collaboration` checker or compile to PDF locally.
   - Check no broken citations (use `\cite{}` instead of inline links).
   - Ancillary files: include `verify_*.py` scripts as supplementary.

## Per-paper checklist

### J62 — *TSML 8×8 Null Space and RH Structural Rhyme*

**Source**: `05_papers/number_theory/J62_RH_short_note/manuscript/manuscript.md`

- [ ] pandoc conversion → `manuscript.tex` (amsart class, ~15 pages)
- [ ] Replace inline 5-line numpy block with `lstlisting` or `verbatim`
- [ ] Ancillary: `verify_J62.py`
- [ ] arXiv categories: `math.NT` primary, `math.RA` + `math.CO` cross
- [ ] MSC: 11M26, 11M41, 15A03, 20N02, 11T55 (already in source)
- [ ] **Title sentence in abstract**: explicit "rhyme not analogue" disclaimer
- [ ] **§6 "What this is, and what it is not"**: keep verbatim, this is the load-bearing scoping

**Estimated time once started**: 4-6 hours.

### J61 — *Type Specimens in ETP-Restricted Variety Lattice*

**Source**: `05_papers/algebra/J61/manuscript/manuscript.md`

- [ ] pandoc conversion (already partly LaTeX-styled in source)
- [ ] Final pass on Theorem 5 (C5 fossil variety) statement — currently at v5 polish
- [ ] Confirm Conjecture C.2 retraction is explicit
- [ ] Cross-link `etp_database/` Lean scaffold in §7 references
- [ ] Drápal-Wanless 2021 citation present
- [ ] arXiv categories: `math.LO` primary, `math.RA` cross
- [ ] MSC: 08A05, 08B05, 20N02, 20N05, 68W30 (already in source)
- [ ] Ancillary: `verify_J61.py`

**Estimated time once started**: 2 days.

### J35 — *Joint Closure + Universal Attractor + 4-Core*

**Source**: `05_papers/algebra/J35/manuscript/manuscript.md`

- [ ] Verify LaTeX form exists (J35 was SUBMISSION-READY before this session — likely already exists as `.tex`)
- [ ] Cross-reference J62 + J61 as companion preprints
- [ ] Add Remark on the strata-prime fingerprint (cite `04_meta/SPHERE_PACKING_STRATA_FINGERPRINT.md`)
- [ ] arXiv categories: `math.RA` primary, `math.NT` + `math.CO` cross
- [ ] MSC: 20N02, 17A35, 11R32, 12F10, 17B20 (already in source)

**Estimated time once started**: 1 day.

## Pre-filled amsart template

```latex
\documentclass[11pt,reqno]{amsart}
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage[margin=1in]{geometry}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{listings}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}

% Custom commands (use as needed)
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\diamond}{\diamond}

\title{TITLE GOES HERE}
\author{Brayden R.\ Sanders}
\address{7Site LLC, Hot Springs, Arkansas, USA}
\email{brayden@7site.co}

\author{M.\ Gish}
\address{Independent Researcher, Hot Springs, Arkansas, USA}
\email{monica.gish1992@gmail.com}

\subjclass[2020]{MSC CODES GO HERE}
\keywords{KEYWORDS GO HERE}

\begin{document}
\begin{abstract}
ABSTRACT GOES HERE
\end{abstract}
\maketitle

% Sections follow
\end{document}
```

## arXiv submission template (per-paper)

```text
Title: <paper title>
Authors: Brayden R. Sanders (7Site LLC), M. Gish (Independent Researcher)
Abstract: <copy from manuscript abstract, ~250 words>
Categories: math.RA (or math.NT, math.LO depending on paper) [primary]; <additional cross-lists>
MSC: <2020 codes>
Comments: <pages>; <ancillary files>
Sources: manuscript.tex + manuscript.bbl + verify_*.py + figures/

Suggested referees: I. Wanless (Monash); P. Vojtěchovský (Denver); T. Waldhauser (Szeged)
```

## Files to revisit before starting

1. `05_papers/_staging/PUBLICATION_PUSH_2026_05_27.md` (the full plan)
2. `05_papers/TIER_INDEX.md` (Tier 1 list)
3. `05_papers/algebra/J35/cover_letter.md` (J35 cover letter exists — adapt for arXiv abstract)
4. `05_papers/number_theory/J62_RH_short_note/README.md` (J62 has full READY status)
5. `05_papers/algebra/J61/manuscript/manuscript.md` (v5; check Theorem 5 statement)

## When ready to resume

```
cd 05_papers/_staging/
cat TRACK_B_LATEX_BONES.md  # this file
cat PUBLICATION_PUSH_2026_05_27.md  # the full plan
# Then start with J62 (fastest), then J61, then J35
```

**The bones are in place. Resume any time.**
