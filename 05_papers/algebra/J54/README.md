# J54 — Height Function for Algebraic Relations between Attractor Moments [NUMBER RESERVED — MANUSCRIPT PENDING RECOVERY]

**Status:** NUMBER RESERVED. The full ~6pp manuscript, cover letter, and `verify_J54.py` (3/3 PASS) were created 2026-05-29 (frontier F14) in a local working copy whose commits were never pushed; the folder was deleted before recovery. **The mathematics is fully preserved** in the ck repo's canon (`FORMULAS_AND_TABLES.md` entries D163, D174, D179 + the F12/F14 frontier results in D172).
**Recovery path:** OneDrive web recycle bin (folder deleted < 30 days before 2026-06-10) — or re-derivation from the canon entries (the underlying scripts' methodology is documented in D174).
**Target venue:** *Acta Arithmetica*
**Author lane:** Sanders + Gish

---

## The three theorems (preserved in canon, D174 + D179)

Let $H(\alpha)$ = height of the minimal polynomial over $\mathbb{Q}$ of the 4-core attractor moment $\xi(\alpha)$ (root of the degree-7 factor $Q(\xi, \alpha)$ of the fixed-point system).

**Theorem 1 (rational scaling).** $\log_{10} H(p/q) = 0.907 + 3.407\,\log_{10}(q)$ at 30 tested rationals; max residual 0.66; $R^2 = 0.67$ (single-predictor). $H(1/2) = 2$ is the global minimum — a 157× gap to the next-lowest $H(2/3) = 314$.

**Theorem 2 (algebraic-irrational scaling).** $\log_{10} H(\alpha)/\deg M_\alpha \in [0.27, 0.41]$ at 11 algebraic irrationals of degree 2–5 over $\mathbb{Q}$, mean 0.30 (denominator the actual minimal-polynomial degree, catching resultant-factorization cases).

**Theorem 3 + Conjecture (discriminant-zero height drop).** At $\alpha_{\mathrm{special}}$ (the real root of $P_{24}$ in $(0,1)$, where $\mathrm{disc}_\xi Q$ vanishes), the double-root factor has $|M|_\infty = 2{,}191{,}936$ at degree 24 — a $\approx 10^{44}$ height drop below the irreducible-resultant prediction. The drop is the algebraic signature of the discriminant zero.

Context: this is the quantitative companion to J01's Theorem F.2 (α-uniqueness over $\mathbb{Q}$, proved via Hilbert irreducibility) and the F12 explicit counterexample at $\alpha_{\mathrm{special}}$.

## Reconstruction checklist

- [ ] Recover original from OneDrive recycle bin, OR
- [ ] Re-derive from D163/D172/D174 canon entries (scripts' methodology documented there)
- [ ] Cover letter for Acta Arithmetica
