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
- **Four papers on regular magic squares of odd order are unread** (found 2026-11-16). Odd magic(n) is regular,
  so they are on point: Lee, Love, Narayan, Wascher and Webster (LAA 437, 2012), now cited; Chan, Mainkar,
  Narayan and Webster (LAA 457, 2014), whose keywords are eigenvalues and circulant matrices; Liu, Gao and Zhao
  (LAA 459, 2014), on an open problem about these squares; and Loly et al. (2009), below. All four are now in
  the note's bibliography, which says it has not found the formula "in the literature we could read". The
  author has to open them (LAA's open archive; ScienceDirect shows automated readers a CAPTCHA). Jitjankarn and
  Rungratgasame (Mat. Vesnik 2022, open access, read) build nonsingular regular squares of every odd order by
  another construction; also cited.
- **Loly, Cameron, Trump and Schindel, "Magic square spectra", Linear Algebra Appl. 430 (2009) 2659–2680**
  (doi:10.1016/j.laa.2008.10.032) is paywalled and was not read. Secondary sources describe it as a study of
  the eigenvalues and singular values of selected magic squares of orders 3 to 8. None reports a determinant
  formula or a result for siamese squares of every odd order. Read it before calling the closed form new.
- Staab et al. (2010) and Mattingly (2000) are now cited in the text, for the even orders.
- The OEIS program returns 0 for singly even n. That matches OEIS's data, but singularity there is observed, not
  proved (Moler's rank n/2 + 2). The draft says so.
