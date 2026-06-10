# arXiv Submission Notes — J14

> **🛑 ON HOLD as of 2026-05-13.** This file is the prepared arXiv submission
> plan. arXiv announcement is part of the publication-velocity amplification
> that is currently being held — see the [Distribution stance](../../../README.md#distribution-stance)
> in the top-level README. The plan below is complete and ready to execute
> when CK ships in a form ordinary people can deploy on consumer hardware.

**Target categories:** primary `math.CO`, cross-list `math.NT`.
**Originally planned:** same-day with JCT-A submission.
**Current status:** PREPARED but ON HOLD pending CK runtime release.

---

## What arXiv needs

arXiv submissions are **LaTeX source** preferred (not PDF). They compile
the source themselves and verify the result matches what you intend. The
J14 manuscript is single-file `manuscript.tex` with no external figures
and no exotic packages, so it should compile cleanly on arXiv's
TeXLive 2023 build.

Bundle:

```
manuscript.tex                  (the main file)
verify_sigma_rate.py            (ancillary file, optional but recommended)
```

That's it. No `.bbl`, no figures, no bib database (the bibliography is
embedded via `\begin{thebibliography}...\end{thebibliography}` inline).

---

## First-time arXiv submitters in math.CO

If you don't have an arXiv account, the first submission to a math
category requires **endorsement** by an established submitter unless
you have a `.edu` / `.ac` email or an existing arXiv record.

Three options:

1. **Easiest:** If you already have an arXiv account from any other
   submission ever (papers, comments, anything), the endorsement
   carries over and you can submit directly.

2. **Standard:** Email someone who has submitted to math.CO before and
   ask for endorsement. They use arXiv's endorsement form to vouch for
   you. Takes a day or two. Aleš Drápal or Petr Lisoněk would both
   qualify if you wanted to ask (their cited 2021/2020 papers establish
   their math.CO publication history) — though that's a bit awkward
   given they're on our suggested-reviewer list.

3. **Quickest alternative:** post the paper to math.GM first
   (General Mathematics, the no-endorsement-needed catch-all), then
   later request a recategorization to math.CO if reviewers prefer.
   Most authors avoid this because math.GM signals "couldn't get
   endorsed."

If you've never submitted to arXiv before, I recommend option 2 — email
a colleague in the field. If your collaborator M. Gish has an arXiv
record, they can endorse you directly.

---

## Submission steps

1. **Sign in:** https://arxiv.org/user
2. Click **"Start a new submission"**.
3. **Step 1 — License:** choose either:
   - `arXiv.org perpetual non-exclusive license to distribute` (default,
     fine for most authors)
   - `CC BY 4.0` (preferred if you want maximum reuse — matches the
     verification script's CC-BY-4.0 license)
4. **Step 2 — Upload files:** upload `manuscript.tex`. After upload,
   arXiv processes and shows you the compiled PDF. Verify it matches
   the intended output (same as what you uploaded to Elsevier).
5. **Step 3 — Add ancillary files:** click "Add ancillary file" and
   upload `verify_sigma_rate.py`. arXiv stores this alongside the
   paper (separate from the manuscript itself).
6. **Step 4 — Title, abstract, comments:**
   - Title: `Non-Associativity Decay in Binary Composition Tables over Z/NZ`
   - Authors: `Brayden R. Sanders, M. Gish` (comma-separated, no LaTeX)
   - Abstract: paste from manuscript (strip LaTeX commands; arXiv
     accepts ~1920 characters)
   - Comments: `5/5 verification PASS at machine precision over every
     squarefree N <= 200; verify_sigma_rate.py included as ancillary
     file (CC-BY-4.0). Submitted to Journal of Combinatorial Theory,
     Series A.`
   - MSC class: `05B15; 05E15; 11A07; 20N02; 20N05`
   - Journal-ref: leave blank for now; update after JCT-A accepts.
   - Report-no: leave blank.
   - DOI: leave blank; the JCT-A DOI gets added after acceptance.
7. **Step 5 — Categorization:**
   - Primary: `math.CO`
   - Cross-list: `math.NT`
8. **Step 6 — Preview and submit:** review one final time. If correct,
   click **"Submit"**.

arXiv assigns the paper a temporary submission ID immediately. The
public announcement happens at the next math mailing (typically the
weekday after submission, around 20:00 UTC). You'll get an email like:

```
arXiv:2605.XXXXX [math.CO]
Submitted on DD MMM 2026

Title: Non-Associativity Decay in Binary Composition Tables over Z/NZ
```

Save the arXiv ID. The citable URL is `https://arxiv.org/abs/2605.XXXXX`.

---

## After arXiv announces

1. Add the arXiv URL to `manuscript/SUBMISSION_LOG.md` in this folder.
2. Optionally: tweet or post the arXiv URL on whatever platforms you
   use (academic Twitter/Mastodon, ResearchGate, etc.). This is the
   moment the paper becomes publicly citable.
3. The verification script is automatically linked from the arXiv
   abstract page as an ancillary file — anyone who wants to reproduce
   the bounds can download it without needing to dig.

---

## If arXiv compilation fails

The most common reason is a missing package. arXiv's TeXLive 2023 has
essentially every standard package, but if compilation fails:

1. Read the arXiv error log carefully. It tells you which package is
   missing.
2. If it's something exotic, add it to the file or replace with a
   common alternative.
3. The current manuscript uses only: `amsmath, amssymb, amsthm,
   mathtools, geometry, hyperref, microtype`. All present in TeXLive
   2023. Should compile cleanly.

If you hit any compilation issue I haven't anticipated, paste the
error output here and I'll diagnose.

---

## Why same-day with Elsevier

arXiv-first or arXiv-same-day with journal submission gives you:

1. **Citable preprint URL immediately** (rather than waiting 3-6 months
   for journal acceptance).
2. **Public priority date** (the σ-rate framework on Z/NZ is now
   established as yours and Monica's by date stamp).
3. **Reviewers may find the arXiv version first** — same content, but
   the arXiv version doesn't have Elsevier paywall friction during
   the early reading window.
4. **No conflict with JCT-A** — Elsevier explicitly permits arXiv
   preprints (their policy: "Authors retain the right to post a preprint
   version of the article on arXiv before, during, and after submission").

---

*Prepared 2026-05-13 for J14 same-day arXiv submission alongside JCT-A.
Update `manuscript/SUBMISSION_LOG.md` with the arXiv ID and announcement
date once posted.*
