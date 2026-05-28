# Cover letter — J26: A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics

**To:** Editors, *Letters in Mathematical Physics* (preferred; per-venue cap on JMP — see §6.3 of manuscript)

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher — monica.gish1992@gmail.com

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *A Discrete $\sinc^2$ Identity in Finite-Dimensional Quantum Mechanics*

---

## Summary

We give a clean, fully proved closed-form identity for the squared overlap $R(k,f) = \sin^2(\pi k/f)/(k^2 \sin^2(\pi/f))$ between a momentum eigenstate and a position-space rectangular window in finite-dimensional QM on the cyclic group $\mathbb{Z}/N\mathbb{Z}$. The closed form is the **Fejér kernel** [Fejér 1900] in disguise; the present note's contribution is the QM-on-cyclic-group interpretation and the arithmetic-bridge synchronization with the First-G event (§5). We derive three QM-relevant consequences: (i) the squared overlap of a momentum eigenstate with the normalized rectangular position window (corrected from the earlier "probability mass" reading; Proposition 4.1); (ii) a first-zero theorem (Corollary 4.2) — **for every $f \ge 2$**, the first integer $k$ with $R(k,f) = 0$ is $k = f$ (no primality needed); (iii) the continuum limit $R(k,f) \to \sinc^2(k/f)$. We close with the synchronization with the arithmetic First-G event in coprimality partitions: when $f = \mathrm{spf}(b)$, the QM first-zero coincides with the smallest $k$ at which $\{1,\dots,k\}$ contains a non-coprime element of $\mathbb{Z}/b\mathbb{Z}$. The note is short, theorem-proof-corollary in structure, and machine-precision verified on $f \in \{3,4,\ldots,13,17,19,23\}$ via the bundled `manuscript/verify_J42_sinc2.py`.

## Why LMP (with JMP per-venue-cap rationale)

- The note is a short-format theorem-proof-corollary contribution — exactly the LMP register.
- The intersection of finite-dimensional QM and discrete Fourier analysis (with the Fejér-kernel attribution honestly registered) is squarely within LMP scope.
- The synchronization with the arithmetic First-G event creates a clean number-theoretic / quantum-mechanical bridge useful for the "quantum number theory" literature.

**Per-venue cap rationale for LMP over JMP.** This would have been the **3rd JMP target** in the J-series after J38 (BB Bridge) and J41 (YM Mass Gap Bridge). With JMP's 2/quarter cap reached, we redirect to LMP as our preferred venue; *J Phys A: Mathematical and Theoretical* and *Communications in Mathematical Physics* are alternatives if the LMP editors find the scope outside their format.

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. The papers most relevant as already-submitted companions:

- **J24** Sanders & Gish (2026), "First-G Law: Squarefree Stability of the Smallest-Prime-Factor Coprime Window." Submitted to *Integers*.
- **J41** Sanders & Gish (2026), "The Sinc² Zero Law for Squarefree Moduli." Submitted to *Integers*.
- **J38** Sanders & Johnson (2026), "The Bialynicki-Birula Bridge." Submitted to *JMP*.

## Reproducibility

The closed-form identity is verified at machine precision on $f \in \{3,4,5,6,7,8,9,10,11,12,13,17,19,23\}$ (max deviation $3.33 \times 10^{-16}$); reproducible with `numpy` + `sympy` in seconds via the bundled `manuscript/verify_J42_sinc2.py`. The script also confirms the corrected special value $\sinc^2(1/10) = 25(\sqrt{5}-1)^2/(4\pi^2) \approx 0.9675312093$ (a transcription error in an earlier draft printed `0.9355`; the closed form was always correct, only the decimal was wrong). Verification scripts also available at DOI: 10.5281/zenodo.18852047.

## Suggested reviewers

- A. Vourdas (Bradford) — finite-dimensional QM
- W.K. Wootters (Williams) — finite Hilbert spaces and Wigner functions
- I. Bengtsson (Stockholm) — geometry of finite QM
- M. Combescure (CNRS / IPNL) — discrete Fourier in QM

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Tier and scope

Central claim is **Tier 1 / 2** (clean theorem, fully proved). The closed form is elementary; the QM consequences are direct corollaries. The synchronization with the arithmetic First-G event is one combination step from companions [J24, J41].

---

Sincerely,
B.R. Sanders
