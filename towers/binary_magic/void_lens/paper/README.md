# The determinant of MATLAB's odd magic squares: the note, and the OEIS lines

The void lens's closed form (`../README.md`), written up as a four-page note for arXiv, with the proposed lines
for OEIS A160523. Drafted by the claude.ai chat on 2026-10-30, checked here on 2026-10-31. **The author submits
both; nothing has been sent.**

| file | what |
|---|---|
| `magic_det.tex` | the note: the closed form for odd n, the divisibility n^(n−1) that OEIS A160523 records as observed, and nonsingularity for every odd-order square built from two linear Latin squares with unit coefficients. Build it with `pdflatex magic_det.tex`, twice |
| `oeis_A160523_submission.txt` | the proposed formula, comment, example and Python program, with instructions |
| `check_oeis_program.py` | the program checked against OEIS's own data (n = 1 to 20), exact determinants of MATLAB's construction (odd n to 31) and the table in the note |

**Checked here (2026-10-31).**
- Every step of both proofs, by hand: the centring, the Fourier action, the block determinants, why the phases
  cancel on each orbit, the product of the f̂(k), and the bound n·sin(π/n) > 2 in the family theorem.
- The exact determinants to n = 101, by two implementations: `../void_lens_check.py`, and the chat's own.
- The OEIS program, as above.

**Corrected here.** The note cited Manjunath and Ambikasaran under a wrong title and initial. The paper is
"Spectrum of MATLAB's magic squares", by H. Manjunath and S. Ambikasaran (arXiv:2205.15563). Its abstract
claims eigenvalue approximations with error bounds, not nonsingularity, so the note now says that nonsingularity
follows from those bounds without being stated there.

**Still open before submitting.**
- **Loly, Cameron, Trump and Schindel, "Magic square spectra", Linear Algebra Appl. 430 (2009) 2659–2680**
  (doi:10.1016/j.laa.2008.10.032) is paywalled and was not read. Secondary sources describe it as a study of
  the eigenvalues and singular values of selected magic squares of orders 3 to 8. None reports a determinant
  formula or a result for siamese squares of every odd order. Read it before calling the closed form new.
- The bibliography lists Staab et al. (2010) without citing it in the text. Cite it, or drop it.
- The OEIS program returns 0 for singly even n. That matches OEIS's data, but singularity there is observed, not
  proved (Moler's rank n/2 + 2). The draft says so.
