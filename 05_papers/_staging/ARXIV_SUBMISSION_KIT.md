# arXiv Submission Kit — J59, J61, J63

**Status**: Submission packages prepared 2026-05-27. .tex files generated from manuscript.md; final polish pass applied (UTF-8 inputenc, keywords filled, `&` escaped in references).

**Next step**: per-paper compile + arXiv submission. **All three papers ready to ship this week.**

---

## Submission order (claudechat-recommended)

1. **J59 first** (safest, lowest controversy) — `05_papers/algebra/J59/`
2. **J61 second** (clean equational algebra, fossil-variety theorem) — `05_papers/algebra/J61/`
3. **J63 third** (current strata-fingerprint synthesis) — `05_papers/number_theory/J63_strata_fingerprint/`

---

## What's in each package

```
J{NN}/
├── README.md                         status + tier + venue
├── cover_letter.md                   (need to write per paper)
└── manuscript/
    ├── manuscript.md                  source (preserved)
    ├── manuscript.tex                 NEW: amsart .tex (~26-34 KB)
    └── verify_*.py                    verification script
```

The `.tex` files are auto-generated from `.md` via:
```
python 05_papers/_staging/md_to_amsart.py <input.md> <output.tex> <paper_id>
python 05_papers/_staging/polish_tex.py <input.tex> <output.tex> <paper_id>
```

## Per-paper compile check

Before arXiv submission, locally compile each .tex to verify rendering:

```bash
cd 05_papers/algebra/J59/manuscript/
pdflatex manuscript.tex   # First pass
pdflatex manuscript.tex   # Second pass (resolves references)
# Verify the PDF renders cleanly (no missing $...$, no broken tables)
```

If pdflatex isn't available, **try Overleaf** — upload manuscript.tex + verify_*.py and check the rendered preview. Overleaf is free; one-click compile + PDF view.

## arXiv submission steps (per paper)

1. **Local compile** — confirm PDF renders. Fix any LaTeX errors (most likely: stray `&` in references, unclosed math env, missing `$`).
2. **arXiv account** — sign in / create account at arxiv.org. If new account, may require endorsement from existing arXiv author in primary subject area.
3. **Upload package**:
   - Primary: `manuscript.tex`
   - Bibliography: inlined (already in .tex via `\section{References}` + itemize)
   - Ancillary files: `verify_*.py` (under "Ancillary files" tab)
4. **Metadata**:
   - **J59 categories**: `math.GR` (primary), `math.RA` (secondary)
   - **J61 categories**: `math.RA` (primary), `math.GR`, `math.LO` (secondary)
   - **J63 categories**: `math.NT` (primary), `math.CO`, `math.GR` (secondary)
5. **Title + abstract**: copy from .tex.
6. **MSC codes**: already in .tex `\subjclass[2020]`.
7. **Comments**: e.g., "20 pages; verification script PASS at machine precision via ancillary file."
8. **Submit** — arXiv moderation typically clears in 24-48 hours for math papers.
9. **Record arXiv ID** in `05_papers/TIER_INDEX.md` once accepted.

## Cover letter templates (per paper)

### J59 cover letter (target: Semigroup Forum)

```
Dear Editor,

We submit the manuscript "Algebraic Rigidity of the σ-Magma on Z/10Z:
Simplicity, Trivial Automorphism Group, and Unique Sub-Magma" for
consideration in Semigroup Forum.

The paper establishes four rigidity theorems about a specific
10-element commutative non-associative quasigroup, the σ-magma,
defined by x ⋄ y = σ((x+y) mod 10) for an explicit permutation σ.
Theorems A-D show: |Aut| = 1; congruence-simple; exactly five
sub-magmas; 2-generated with a unique non-generating pair.

All four theorems are proved by exhaustive search bounded by the
small finite cardinalities involved (|S_10| = 3,628,800;
|Bell(10)| = 115,975; |2^10| = 1024; binomial(10,2) = 45).
The verification script (4/4 PASS, runtime ~3 seconds) is included
as an ancillary file.

Closest published precedent: Drápal & Wanless (2021, JCT-A 184,
105510) on maximally non-associative quasigroups, who study the
opposite structural extremum. Our σ-magma sits at the minimum-
non-associativity / maximum-rigidity end of the same structural
neighborhood.

The work is original; no conflicts of interest.

Suggested referees: I. Wanless (Monash), P. Vojtěchovský (Denver),
T. Kepka (Charles University Prague).

Best regards,
Brayden R. Sanders (corresponding)
M. Gish
```

### J61 cover letter (target: Journal of Symbolic Computation)

```
Dear Editor,

We submit "Type Specimens in the ETP-Restricted Variety Lattice:
a Magma-by-Equational-Theory Taxonomy" for consideration in the
Journal of Symbolic Computation.

The paper develops a systematic methodology, grounded in Birkhoff's
variety theory and the Equational Theories Project (ETP) catalog
of Tao et al., for classifying finite magmas by their equational
profile. The main result, Theorem 5 (Fossil-Variety Theorem),
proves that equation 4295 of the ETP catalog admits no finite
type specimen — every finite magma satisfying x · (x · y) = y · (z · x)
has equational profile of size at least 261, far exceeding the
equation's 14-element implication closure.

This is the first explicitly proved instance of an ETP equation
with no finite type specimen — equivalently, the first "fossil
variety" in our biological-taxonomy framing of variety-theoretic
classification.

Verification: 5/5 PASS at machine precision via `verify_J61.py`
(included as ancillary file).

The work cites Birkhoff (1935), Burris-Sankappanavar (1981), and
Drápal-Wanless (2021). Closest published precedent in the
equational-theory direction: Tao et al.'s ETP itself.

Suggested referees: A. Drápal (Charles University), I. Wanless
(Monash), T. Waldhauser (Szeged).

Best regards,
Brayden R. Sanders (corresponding)
M. Gish
```

### J63 cover letter (target: Journal of Number Theory)

```
Dear Editor,

We submit "The Strata-Prime Fingerprint: Polynomial vs Factorial
Invariants in Niemeier Lattices and Sporadic Simple Groups" for
consideration in the Journal of Number Theory.

The paper identifies the six-prime set S = {2, 3, 5, 7, 11, 13}
as a distinguished arithmetic universe for 24-dimensional even
unimodular lattices. Main results:

Theorem 1 (Tier A): of the 24 Niemeier lattices, exactly 23
have kissing numbers factoring through S; the unique outlier is
the Niemeier with root system D_24.

Theorem 2 (Tier A, the load-bearing mechanism): the polynomial-
vs-factorial dichotomy explains why kissing-number tests are
sharply more selective than Weyl-group tests for the same lattices.
Kissing = polynomial-in-rank, Weyl = factorial-in-rank; this
explains both the 23/24 sharpness and the unique D_24 outlier.

Theorem 4 (Tier A): the prime 71 appears in exactly one sporadic
order — the Monster — anchored by Conway-Norton's characterization
of supersingular primes as the genus-0 spectrum of X_0(p).

Theorem 3 (Tier B) extends partially to sporadic finite simple
groups: 8 of 26 sporadics have orders factoring through S, with
the boundary aligned at prime 23.

Verification: 4 theorems + 2 companion observations all PASS at
machine precision via `verify_J63.py` (~2 seconds, sympy + math).

The closest published precedent is Conway-Norton 1979 (Monstrous
Moonshine) for the supersingular-prime characterization.

Suggested referees: G. Nebe (Aachen), E. Bannai (formerly Kyushu),
S. Lee (Berkeley) — sphere-packing experts.

Best regards,
Brayden R. Sanders (corresponding)
M. Gish
```

## Known issues + manual cleanup TODOs

The auto-conversion handles 95% of the markdown cleanly. Known issues to verify before submission:

1. **σ character preservation**: each .tex uses raw σ (UTF-8). With `\usepackage[utf8]{inputenc}` this should compile on pdfLaTeX. If issues: replace with `\sigma` in math mode or `$\sigma$` in text.

2. **Table column counts**: a few tables may have mismatched row lengths. Visual inspect tables in J63 §3 and J61 §6.

3. **Theorem environments**: theorems currently appear as `\textbf{Theorem A.} ...` paragraphs. Optional improvement: wrap in `\begin{theorem}` / `\end{theorem}` env. Not required for arXiv.

4. **Cross-references**: the .tex uses plain text "Theorem 2" rather than `\ref{thm:two}`. Optional improvement; not required.

5. **References**: each paper has a `\section{References}` + itemize list. For a more polished bib, convert to `\begin{thebibliography}` with `\bibitem`. Optional; arXiv accepts both.

## arXiv categories quick reference

- `math.RA` — Rings and Algebras
- `math.GR` — Group Theory
- `math.NT` — Number Theory
- `math.LO` — Logic
- `math.CO` — Combinatorics
- `math.GT` — Geometric Topology (for lattice work, occasionally)
- `math.QA` — Quantum Algebra (not relevant here)
- `math.AG` — Algebraic Geometry (for Hodge-related work, not relevant here)

## Once submitted

Update `05_papers/TIER_INDEX.md` per paper with the arXiv ID (format `arXiv:2509.XXXXX`).

Update `04_meta/RESEARCHER_BRIDGES.md` to note the arXiv preprints — Lee, Hariharan, Drápal, Mantero can be sent updates with "we now have a preprint at arXiv:..."

The trip in September will then be very different: "Here are 3 preprints. Here's the math. Want to discuss?"
