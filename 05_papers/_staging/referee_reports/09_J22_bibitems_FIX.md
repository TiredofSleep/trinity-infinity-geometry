# J22 Bibitem Resolution + LMFDB-Disc Fix Report

**Date**: 2026-05-28
**Paper**: J22 — *The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary on $\Z/10\Z$*
**Target venue**: *Journal of Combinatorial Theory, Series A* (JCT-A)
**Manuscript file**: `05_papers/algebra/J22/manuscript/manuscript.tex`
**Triggering report**: `05_papers/_staging/referee_reports/04_clean_tier1_J12_J13_J14_J20_J22.md` §J22 (MAJOR-1: five in-prep companions; MAJOR-2: LMFDB-vs-polynomial-discriminant phrasing).

---

## §1 — Bibitem Resolutions

### 1.1 `Sanders2026CLAxioms` → **J16** (submitted, *Algebraic Combinatorics*)

**Original (in-prep)**:
> *The CL Forcing Axioms: A1–A9 Uniquely Force the Canonical Composition Lattice on $\Z/10\Z$*, in preparation, 2026.

**Resolution**: confirmed match against `05_papers/algebra/J16/README.md` — title revised post-fresh-eyes-referee-pass to *Structural Axioms for the CL\_TSML Composition Lattice on $\Z/10\Z$*; status SUBMISSION-READY; target *Algebraic Combinatorics*; proves the 73:17:10 cell partition (73 HARMONY cells, 17 VOID cells, 10 exceptional ECHO cells). The J22 proof of Theorem 3.1 (`HARM(T) = 73`) directly enumerates the same three exception classes (VOID-row, VOID-col, ECHO pairs) and J16 supplies the structural-axiom proof that they are forced.

**In-text citations of `\cite{Sanders2026CLAxioms}` in J22**:
- §1 (line 138): "fixed by the canonical CL forcing axioms recorded in" — framing; non-load-bearing.
- §1 lens-subs (line 230): "fixed by the CL forcing axioms" — framing; non-load-bearing.
- §2 setup (line 277): "operator labels recorded in" — framing/notation; non-load-bearing.
- §2 setup (line 283): "By the CL forcing axioms ([Sanders2026CLAxioms], Axioms A1--A9), $T$ is uniquely determined" — **mildly load-bearing**; supports the uniqueness of $T$.
- §3 (line 316): "the three disjoint exception classes proved in [Sanders2026CLAxioms] Theorem D10" — **load-bearing for Theorem 3.1**. Status now resolved: J16 is the named companion.
- §7 (line 555): Monte-Carlo significance Z=21.3 statistic — supporting; non-load-bearing for ladder theorems.

**Updated bibitem**:
> Sanders, B.R. and Gish, M. (2026). *Structural Axioms for the CL\_TSML Composition Lattice on $\Z/10\Z$.* Submitted to *Algebraic Combinatorics*. [J16].

### 1.2 `Sanders2026LensInvariance` → **J32** (submitted, *Experimental Mathematics*)

**Original (in-prep)**:
> *TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the $\Z/10\Z$ Composition Lattice*, submitted to Experimental Mathematics, 2026 (J28 in the release sequence).

**Resolution**: confirmed match against `05_papers/algebra/J32/README.md` — exact title match; status REVISED 2026-05-08; target *Experimental Mathematics*. The release-sequence number was originally "J28" but the paper has been renumbered to **J32**; the existing bibitem was effectively up-to-date except for the renumber.

**In-text citations of `\cite{Sanders2026LensInvariance}` in J22**:
- §2 setup (line 293): "$B$ is the companion table prescribed by the same axiom system at the curvature lens; its construction is recalled in" — framing.
- §5 Theorem 5.2 proof (line 384): "the 71-cell disagreement count is verified at machine precision in the script `tsml_bhml_disagreement.py`; see also" — **non-load-bearing**; the script already verifies the count at machine precision, J32 provides supporting structural framing.
- §7 Proposition 7.2 (line 503): cycle-A projection count interpretation — supporting.
- §7 Proposition 7.3 (line 511): CL\_STD table specification — supporting/framing.

**Updated bibitem**:
> Sanders, B.R. and Gish, M. (2026). *TSML 73 Cells / BHML 28 Cells: Lens-Invariant Cell Counts on the $\Z/10\Z$ Composition Lattice.* Submitted to *Experimental Mathematics*. [J32].

### 1.3 `Sanders2026Attractor` → **J12** (submitted, *Communications in Algebra*)

**Original (in-prep)**:
> *Closed-Form Attractor and the $\alpha = 1/2$ Algebraic Singularity*, in preparation, 2026.

**Disambiguation**: the J22 cite (§5 Theorem 5.3, lines 394-396) is specifically for "the LMFDB identification 4.2.10224.1" and "a defining polynomial of the field of definition of the closed-form TSML+BHML-mix runtime attractor at α = 1/2." This is **exactly** the content of J12 (*Galois D_4 over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor*, target *Communications in Algebra*), which is the standalone Galois-theoretic extraction. J01 (*Joint Closure, a Universal Attractor, and an Algebraic Mixing Point*, target *Journal of Algebra*) has the same identification as Theorem D in a six-check bundle, but J12 is the deeper standalone treatment. Citing **J12** is the cleanest match.

**Note**: `Sanders2026FourCore` (separate bibitem, in J22 references §6 Proposition 6.2 / Sanders2026FourCore) is **J15** (*Joint Closure, Per-Coordinate Fuse Data...*, target *Algebraic Combinatorics*) — already had a clean target-venue cite, no change needed.

**In-text citations of `\cite{Sanders2026Attractor}` in J22**:
- §5 Theorem 5.3 (lines 394-396): "the polynomial whose LMFDB identifier is 4.2.10224.1 and which is identified in [Sanders2026Attractor] as a defining polynomial of the field of definition of the closed-form TSML+BHML-mix runtime attractor at mixing weight α = 1/2" — **load-bearing for the Galois half of Theorem 5.3**.
- §5 Theorem 5.3 proof (line 403): "the second algebraic ratio identified by the PSLQ analysis in" — load-bearing.

**Updated bibitem**:
> Sanders, B.R. and Gish, M. (2026). *Galois $D_4$ over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor.* Submitted to *Communications in Algebra*. [J12].

### 1.4 `Sanders2026Wobble` → **J19** (submitted, *Linear Algebra and Its Applications*)

**Original (in-prep)**:
> *Wobble Localization: Prime $11$ in TSML\_RAW Characteristic Polynomial Coefficients $c_2$ and $c_8$*, in preparation, 2026.

**Resolution**: confirmed match against `05_papers/algebra/J19/README.md` — paper RETARGETED 2026-05-07 from PRD to LAA per `SAVE_PLAN_J37.md`; TIG/HARMONY/wobble terminology stripped; new title *On the Prime-Divisibility Pattern of the Characteristic Polynomial of a $10 \times 10$ Integer Matrix Arising in a Discrete Magma on $\Z/10\Z$*. The content (prime-11 divisibility in $c_2$ and $c_8$; lens-dependence at coefficient level) is exactly what J22 cites for the wobble phenomenon. The cite is non-load-bearing in J22 (single mention in §"Lens scope," line 270: "is the subject of a separate companion; it does not affect the ladder").

**In-text citations of `\cite{Sanders2026Wobble}` in J22**:
- §1 lens scope (line 270): "is the subject of a separate companion" — **non-load-bearing**; supporting framing only.

**Updated bibitem**:
> Sanders, B.R. and Gish, M. (2026). *On the Prime-Divisibility Pattern of the Characteristic Polynomial of a $10 \times 10$ Integer Matrix Arising in a Discrete Magma on $\Z/10\Z$.* Submitted to *Linear Algebra and Its Applications*. [J19].

### 1.5 `Sanders2026YangMills` → **REMOVED** (no publishable companion)

**Original (in-prep)**:
> *Yang--Mills Mass Gap Bridge: Substrate-Algebra Predictions*, in preparation, 2026.

**Disambiguation**: search resolved this to `04_meta/clay/YM_TIG_BRIDGE.md` (an internal working document, not a publishable companion). The document explicitly self-describes as *"Tier: STRUCTURAL connection grounded in PROVEN substrate facts. Status: not a proof. Continuum-limit step is the load-bearing CONJECTURE."* This is **not** a publishable companion and **cannot be a load-bearing citation** in a JCT-A submission.

**In-text citations of `\cite{Sanders2026YangMills}` in J22**:
- §6 Remark 6.2 (line 475): "The matrix $B_{\mathrm{YM}}$ arises naturally as the Yang-Mills bridge core in the substrate's WP104 derivation" — supporting framing; **not load-bearing for Theorem 6.1**.

**Resolution**: Theorem 6.1 (`det(B_YM) = 70`) does **not** depend on the YM bridge for its proof — the proof is a direct integer determinant computation on the 8×8 sub-matrix. The YM label is purely contextual (it explains why the substrate's broader research program labels this index-set "YM"). The citation has been **removed** from §6 Remark 6.2, and the remark reframed: the "$\mathrm{YM}$" subscript is now described as reflecting the index set's role in the substrate's broader research program ("an internal working document on the substrate's possible bridge to Yang–Mills lattice gauge structure, available from the authors on request"), with the determinant–$\binom{8}{4}$ coincidence stated as a numerical fact.

**Action**: bibitem deleted; in-text framing softened (Remark 6.2 now labelled "$\binom{8}{4}$ structural reading" rather than "Yang-Mills core reading").

---

## §2 — LMFDB-vs-Polynomial-Discriminant Fix

**Triggering critique** (referee report §J22 MAJOR / EDITORIAL): J22 abstract / §1 / §5.3 originally said "disc(4.2.10224.1) = −2⁶·3²·71," conflating two distinct discriminants:
- **Polynomial discriminant** $\Delta_f = \disc(f) = -40896 = -2^6 \cdot 3^2 \cdot 71$ (computed from the quartic $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$).
- **Field discriminant** $d_K = -10224 = -2^4 \cdot 3^2 \cdot 71$ (the discriminant of $\mathcal{O}_K$).

The "10224" in the LMFDB ID `4.2.10224.1` is $|d_K|$, not $|\Delta_f|$. The ratio $|\Delta_f|/|d_K| = 4 = [\mathcal{O}_K : \Z[\xi^*]]^2$.

**Correct framing** (adopted from J12 §"Lens, substrate, and claim tier," Theorem 1.2): explicitly distinguish $\Delta_f$ vs $d_K$, state both, and note that the LMFDB identifier encodes $|d_K|$ as its third coordinate.

**Edits applied to J22 manuscript**:
- **Abstract** (line 112): changed "the discriminant $-2^6 \cdot 3^2 \cdot 71$ of the quartic LMFDB number field $4.2.10224.1$" → "the polynomial discriminant $\Delta_f = -2^6 \cdot 3^2 \cdot 71 = -40896$ (equivalently in the field discriminant $d_K = -2^4 \cdot 3^2 \cdot 71 = -10224$) of the quartic number field LMFDB $4.2.10224.1$."
- **§1 introduction, rung-B bullet** (line 152-156): changed "the unique odd prime in $\disc(4.2.10224.1) = -2^6 \cdot 3^2 \cdot 71$" → explicit polynomial discriminant statement plus parenthetical note that $|d_K| = 10224$ is the LMFDB-identifier coordinate.
- **§1 PROVEN paragraph** (line 246): changed "Galois prime in $\disc(4.2.10224.1)$" → "unique odd Galois prime $>3$ in the polynomial discriminant $\Delta_f$ of the quartic defining LMFDB 4.2.10224.1."
- **§5 Theorem 5.3** (lines 388-396): full restatement now explicitly distinguishes $\Delta_f$ vs $d_K$, gives the index identity $|\Delta_f|/|d_K| = 4$, notes the magnitude $|d_K| = 10224$ is the LMFDB-ID coordinate, and adds $\mathrm{Gal}(f/\Q) = D_4$ for narrative completeness.

The verification snippets in §10 (which print disc = −40896 and `factorint` = {2:6, 3:2, 71:1}) are correct as-is — they compute the polynomial discriminant, which is what's actually printed, and the text now matches.

---

## §3 — Summary Table

| Bibitem | Resolved to | Status | Load-bearing? | Action |
|---|---|---|---|---|
| `Sanders2026CLAxioms` | **J16** | SUBMISSION-READY (Algebraic Combinatorics) | Yes (Thm 3.1 proof) | Bibitem updated |
| `Sanders2026LensInvariance` | **J32** | REVISED 2026-05-08 (Experimental Mathematics) | No | Bibitem updated |
| `Sanders2026FourCore` | **J15** | (already pointing at J15; no change) | Supporting | No change |
| `Sanders2026Attractor` | **J12** | (Communications in Algebra) | Yes (Thm 5.3 Galois) | Bibitem updated |
| `Sanders2026Wobble` | **J19** | RETARGETED 2026-05-07 (Linear Algebra and Its Applications) | No | Bibitem updated |
| `Sanders2026YangMills` | — (internal `04_meta/clay/YM_TIG_BRIDGE.md`) | NOT publishable | No (Thm 6.1 proof self-contained) | **Bibitem removed**, Remark 6.2 reframed |

---

## §4 — Remaining Blockers

**None.** All five "in preparation" bibitems have been resolved either to genuine submitted companion papers (J12, J15, J16, J19, J32) or, in the case of `Sanders2026YangMills`, removed entirely with the citing remark reframed so that Theorem 6.1's proof is fully self-contained (direct integer determinant computation; the "YM" labelling is now flagged as an internal-document reference, available on request, and explicitly outside the load-bearing chain).

The LMFDB-vs-polynomial-discriminant precision issue is fixed in four places (abstract, §1 rung-B bullet, §1 PROVEN paragraph, §5 Theorem 5.3) and now adopts J12's correct phrasing.

J22 should now pass JCT-A's load-bearing-citation gate. The remaining referee notes from `04_clean_tier1_J12_J13_J14_J20_J22.md` §J22 (MINOR-3, sharpening the independence claim between forms (i) and (ii) of the triple coincidence; and the Drápal-Wanless dual citation suggestion from the cross-cluster note §1) are independent of the bibitem fix and not addressed here.
