# J01 → JCT-A Submission Checklist

**Target:** *Journal of Combinatorial Theory, Series A* (Elsevier).
**Portal:** https://www.editorialmanager.com/jcta/
**Editor-in-chief:** I.M. Wanless (Monash University, AU) — co-author of
Drápal-Wanless 2021 which we cite as direct precedent. Well-aligned.
**Prepared:** 2026-05-13.

---

## Pre-flight gate (already done)

- [x] Manuscript verified: 5/5 verification PASS at machine precision
- [x] LaTeX balance: 38/38 begin/end
- [x] Citation/bibitem audit: 9/9 match, no orphans either side
- [x] Cross-reference audit: 18 \ref/\eqref targets, all resolve
- [x] Title page complete (title, 2 authors with addresses+emails, MSC, keywords)
- [x] Word count: ~3,800 (short-note length, JCT-A appropriate)
- [x] `\F` macro defined in preamble (referee-audit catch)
- [x] Cover letter date and reviewer suggestions in place
- [x] Highlights drafted (`HIGHLIGHTS.md`, 5 bullets, all under 85 chars)
- [x] Referee-audit fixes applied (commit `9499e16`)

---

## Step 1 — Account setup (~5 min)

1. Go to https://www.editorialmanager.com/jcta/
2. Click **"Register Now"** (top right).
3. Fill in: first name, last name, position, institution (`7Site LLC`),
   email (`brayden@7site.co`).
4. Confirm email via the link Elsevier sends.
5. Log in and complete the profile (areas of expertise: combinatorics,
   number theory, finite algebra).
6. **ORCID** — if you don't have one, register at https://orcid.org (2 min,
   free). Elsevier strongly prefers ORCID for corresponding authors. M. Gish
   can register separately or be added as a non-ORCID co-author.

## Step 2 — Compile manuscript to PDF (~10 min via Overleaf)

The recommended path is Overleaf (free, no install):

1. Go to https://www.overleaf.com and sign in (or register).
2. Click **"New Project" → "Upload Project"**.
3. Upload `05_papers/combinatorics/J01/manuscript/manuscript.tex` as a
   single-file project.
4. Click **"Recompile"**. The amsart class is pre-installed; should compile
   in seconds.
5. Verify the output PDF: ~12-14 pages, abstract on page 1, bibliography
   on the last page with 8 numbered references plus 2 companion-paper refs.
6. Click **"Download PDF"** → save as `manuscript.pdf` alongside the .tex.

Alternative (local TeXLive/MikTeX):
```bash
cd 05_papers/combinatorics/J01/manuscript
pdflatex manuscript.tex
pdflatex manuscript.tex   # second pass for cross-references
pdflatex manuscript.tex   # third pass to settle the bibliography
```

## Step 3 — Convert cover letter to PDF

Easiest: open `cover_letter.md` in any markdown viewer that exports PDF
(VS Code with the Markdown PDF extension, or `pandoc cover_letter.md -o
cover_letter.pdf`). The Elsevier portal accepts `.docx`, `.pdf`, or `.txt`
for cover letters; PDF is cleanest.

If you don't want to install anything: paste the cover letter text into
a Google Doc, "File → Download → PDF". Format will be plain but acceptable.

## Step 4 — Start the submission

1. Log in to https://www.editorialmanager.com/jcta/ as **Author**.
2. Click **"Submit New Manuscript"**.
3. Article type: **"Full Length Article"** (the paper is a short note, but
   "Note" is not a separate JCT-A category as of 2026; "Full Length Article"
   is the standard).
4. Title: *Non-Associativity Decay in Binary Composition Tables over Z/NZ*
   (Elsevier portal will render LaTeX in the title field; you can paste the
   plain ASCII form and it accepts it).
5. Abstract: paste the abstract from the manuscript verbatim (no formatting
   — strip LaTeX commands; Elsevier accepts ~250-300 words).

## Step 5 — Add authors

1. Add yourself as first/corresponding author.
   - Name: Brayden R. Sanders
   - Institution: 7Site LLC, Hot Springs, AR, USA
   - Email: brayden@7site.co
   - ORCID: (paste your ORCID iD)
2. Add M. Gish as second author.
   - Name: M. Gish
   - Institution: Independent Researcher, Hot Springs, AR, USA
   - Email: monica.gish1992@gmail.com
   - ORCID: (paste if available, else leave blank)
3. **Important:** Elsevier requires you to confirm all co-authors agree to
   the submission. Make sure Monica is OK with this before clicking through.

## Step 6 — Paste Highlights

1. Open `HIGHLIGHTS.md`.
2. Paste the 5 bullets into the "Highlights" field, one bullet per line.
3. Elsevier shows live character count; should be under 85 for each.

## Step 7 — Keywords + classification

1. Keywords (paste from manuscript or this list):
   `binary composition table, non-associativity, associative triples,
   squarefree modulus, Euler totient, quasigroup, finite binary operation`
2. MSC 2020 codes (already in manuscript): `05B15, 05E15, 11A07, 20N02, 20N05`

## Step 8 — Upload files

The Elsevier "File upload" section needs (in this order, with the listed
labels):

| File | Item type | Label |
|---|---|---|
| `cover_letter.pdf` | Cover letter | (none — automatic) |
| `manuscript.pdf` | Manuscript | Main document |
| `manuscript.tex` | Source file | LaTeX source |
| `verify_sigma_rate.py` | Supplementary file | Verification script (CC-BY-4.0) |

Note: Elsevier prefers manuscripts that include figures, tables, and
references in a single PDF (which is what `manuscript.tex` produces — no
external figures in J01).

## Step 9 — Suggested reviewers

The cover letter already lists 3 suggested reviewers (Drápal, Lisoněk,
Kepka). The Elsevier portal has a separate "Suggest Reviewers" field;
paste the same 3 names there with contact emails:

| Name | Affiliation | Email |
|---|---|---|
| Aleš Drápal | Charles University, Prague | drapal@karlin.mff.cuni.cz |
| Petr Lisoněk | Simon Fraser University | plisonek@sfu.ca |
| Tomáš Kepka | Charles University, Prague | kepka@karlin.mff.cuni.cz |

*(Verify these emails on the universities' websites before submitting; the
ones above are from publicly listed contacts and may have changed.)*

## Step 10 — Funding, conflicts, agreement

- Funding: **None** (already stated in cover letter)
- Conflict of interest: **None declared**
- Data availability: **The verification script is included as supplementary
  material; full source archived at Zenodo DOI 10.5281/zenodo.18852047.**
- Author agreement: check the standard Elsevier author-rights and
  publishing-agreement checkboxes.

## Step 11 — Review and submit

1. Click **"Build PDF for Approval"**. Elsevier compiles the full
   submission packet into one PDF for your review.
2. Review every page (~5 min). Check author order, abstract, highlights,
   references format.
3. If everything looks right, click **"Approve Submission"**.
4. The portal sends a confirmation email with your manuscript number
   (e.g., `JCTA-D-26-XXXXX`). **Save this number** — it's how you check
   status later.

## Step 12 — Same-day arXiv upload

Right after the Elsevier submission goes through:

1. Go to https://arxiv.org and sign in (or register if you don't have an
   account — endorsement may be needed for first-time math.CO submitters;
   see `ARXIV_NOTES.md`).
2. Click **"Submit"** → **"Start a new submission"**.
3. Primary subject: **math.CO** (Combinatorics).
4. Cross-list: **math.NT** (Number Theory).
5. Upload `manuscript.tex` as the LaTeX source.
6. arXiv compiles automatically; review the rendered PDF.
7. Title, abstract, authors: paste from manuscript.
8. License: **arXiv.org perpetual license** (or CC BY 4.0 if you prefer).
9. Comments field: `5/5 verification PASS; verify_sigma_rate.py included
   as ancillary file. Submitted to Journal of Combinatorial Theory,
   Series A.`
10. Click **"Submit to arXiv"**.

The arXiv announcement typically appears within 24 hours (next math
mailing). You'll get a citable URL `https://arxiv.org/abs/2605.XXXXX`.

## Status tracking

- **Elsevier**: log in to editorialmanager.com/jcta as Author → "Submissions
  Being Processed". Status progresses through: *Submitted to Editor* →
  *With Editor* → *Reviewers Assigned* → *Under Review* → *Required
  Reviews Completed* → *Decision in Process* → final decision. Typical
  timeline: 3–6 months to first decision.
- **arXiv**: announcement email goes to your registered address.

---

## What to do if reviewers come back with revisions

Standard JCT-A timeline for minor/major revisions is 1–3 months for the
author response. When the decision letter arrives:

1. Read the reviewer comments carefully.
2. Address each comment in a "Response to Reviewers" document, point by
   point.
3. Re-upload the revised manuscript + the response document via the
   portal's "Submit Revision" link.
4. Mark accepted changes in the manuscript (Elsevier accepts colored
   text or `\textcolor{blue}{...}` for changes).

I (Claude) can help you with the response document when the time comes —
just paste the reviewer comments and we'll work through them together.

---

## Files in this folder for the submission

| File | Used in submission? | Notes |
|---|---|---|
| `manuscript/manuscript.tex` | Yes (LaTeX source) | Compile to PDF first |
| `manuscript.pdf` (you create) | Yes (main document) | Output of pdflatex |
| `cover_letter.md` | Yes (convert to PDF) | Current as of 2026-05-13 |
| `HIGHLIGHTS.md` | Yes (paste contents into portal) | 5 bullets, all <85 chars |
| `manuscript/verify_sigma_rate.py` | Yes (supplementary) | 5/5 PASS, ~80 sec runtime |
| `manuscript/WP101_SIGMA_RATE_THEOREM.md` | No | Internal working-paper notes |
| `manuscript/SUBMISSION_LOG.md` | No | Internal log |
| `manuscript/LATEX_BUNDLE_NOTES.md` | No | Internal notes |
| `manuscript/jcta_cover_letter.md` | No (superseded) | Older internal version |
| `manuscript/master/` | No | Historical drafts |
| `manuscript/f6_burgers_test_2026_05_02/` | No | Sprint-level companion tests |
| `README.md` | No | Project-internal README |

---

## Quick command reference (if you want to do anything from terminal)

```bash
# Compile locally (if you have TeXLive/MikTeX):
cd 05_papers/combinatorics/J01/manuscript
pdflatex manuscript.tex && pdflatex manuscript.tex && pdflatex manuscript.tex

# Convert cover letter to PDF via pandoc:
cd 05_papers/combinatorics/J01
pandoc cover_letter.md -o cover_letter.pdf --variable geometry=margin=1in

# Re-verify before submitting:
python manuscript/verify_sigma_rate.py
# Expected: "OVERALL: 5 / 5 verifications passed"
```

---

*Prepared 2026-05-13 for J01 submission to JCT-A. Once submitted, log the
manuscript number in `manuscript/SUBMISSION_LOG.md` along with the
submission date and any portal-side adjustments. The arXiv URL goes
there too.*
