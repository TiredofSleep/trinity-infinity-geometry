# J20 — Total-Dimension Match V^{⊗n} and Cl(2n), with Refined-Cell Grading

**Status:** SUBMISSION-READY (manuscript referee-grade pass 2026-05-12; verification script `verify_J17.py` 6/6 PASS at machine precision)
**Phase:** Phase 2
**Target venue:** *Linear Algebra and its Applications*
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready (LinAlgApps, SUBMISSION-READY))
**WP source:** WP119 (Gen12/targets/clay/papers/sprint18_bridge_dirac_2026_05_04/journals/WP119_journal_clean.tex)
**Lens scope:** LENS-DEPENDENT in a controlled way — the coarse two-summand decomposition of `V` is one of three possible 2+2 partitions of the four basis lines; the choice is recorded in §0 (Lens) and Remark 2.1. The refined four-summand decomposition is the canonical `F_5`-line decomposition determined by the named basis. Total-dimension and refined-cell statements are basis-level; no claim depends on a representation-theoretic choice.

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex`

A short, self-contained note recording two basis-level statements about the 4-dimensional commutative non-associative algebra `V` over `F_5` introduced in the companion paper J37 (*Discrete Dirac on F_5^4*):

- **Theorem 3.1 (total-dimension match):** for every `n ≥ 0`,
  `dim_{F_5} V^{⊗n} = 4^n = 2^{2n} = dim_R Cl(2n, 0)`.
  Forced by `dim V = 4 = 2^2`; recorded here as the index entry into the refinement below.
- **Theorem 4.1 (refined-cell binomial grading):** for every `n ≥ 0`, the `4^n = 2^{2n}` one-dimensional refined cells of `V^{⊗n}` (labeled by `2n` structural bits, one bit pair per tensor slot) partition into Hamming-weight classes of multiplicities `C(2n, k)` matching the grade dimensions of `Cl(2n)`.
- **Proposition 5.1 (n=5, refined):** explicit distribution `1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1` summing to `1024 = 4^5 = dim Cl(10)`.
- **Proposition 5.2 (n=5, coarse):** coarse-cell distribution `1, 5, 10, 10, 5, 1 = C(5, k)` summing to `32`; recorded separately and explicitly *not* equated with the `Cl(2n)` grade sequence (Remark 4.2).

**The R1 math fix.** A prior draft conflated the coarse-cell distribution `C(n, k)` with the `Cl(2n)` grade distribution `C(2n, k)`. These are distinct sequences over distinct index sets:

| n | coarse cells | coarse weights | refined cells | refined weights | matches Cl |
|---|---|---|---|---|---|
| 1 | 2 | 1, 1 | 4 | 1, 2, 1 | Cl(2) |
| 2 | 4 | 1, 2, 1 | 16 | 1, 4, 6, 4, 1 | Cl(4) |
| 5 | 32 | 1, 5, 10, 10, 5, 1 | 1024 | 1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1 | Cl(10) |

The refined cells are the right object for the Clifford comparison; the coarse cells (each itself a `2^n`-dimensional subspace) are a coarser partition not directly comparable with Cl-grades.

## §2 — Verification script

**Local path:** `manuscript/verify_J17.py`

Six self-contained checks (standard-library Python only, no external dependencies) mapped one-to-one to the manuscript's claims:

```bash
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe verify_J17.py
```

Expected output: six "OK" results in the summary, "Overall: 6/6 PASS." Runtime <1s.

The six checks are:

1. **C1:** Total-dimension match `dim_{F_5} V^{⊗n} = 4^n = 2^{2n} = dim_R Cl(2n)` for `n = 0..5`.
2. **C2:** Coarse-cell count = `2^n` for `n = 1..5`.
3. **C3:** Coarse-cell distribution at `n = 5` equals `1, 5, 10, 10, 5, 1` summing to `32`.
4. **C4:** Refined-cell total `sum_k C(2n, k) = 4^n` for `n = 0..5`.
5. **C5:** Refined distribution `C(2n, k)` matches Cl(2n) grade dimensions, closed-form vs. direct enumeration over `4^n` structural-bit strings, for `n = 0..5`.
6. **C6:** Explicit `n = 5` refined distribution equals `C(10, k)` summing to `1024 = 4^5 = dim Cl(10)`.

The script is referee-portable on its own — it does *not* depend on the broader TIG reference library `tig_dirac.py`. The reference library is available at the project's public repository for readers who want to explore the algebra `V` directly, but verification of the load-bearing claims of this paper requires only Python's standard library.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J37** — *Discrete Dirac on F_5^4: Substrate Algebra of the 4-Core* (submitted to *Algebras and Representation Theory*). Defines the algebra `V` and its multiplication table; J20 cites the data needed in §2 directly so verification is self-contained at the basis level.
- **J50** — *F_p Universality: The Operator-Substrate Construction over Prime Fields* (submitted to *Algebra Universalis*). Sister companion in the same finite-field family; not load-bearing for J20.

## §4 — Cover letter

See `cover_letter.md` in this folder. Finalized 2026-05-12 to:

- Reference `verify_J17.py` as the green-light gate (6/6 PASS at machine precision).
- Explicitly state the R1 math fix (coarse vs. refined cells) and its acknowledgement of the prior anonymous referee.
- Emphasize the elementary, self-contained nature appropriate to *Linear Algebra and its Applications*.
- Author lane Sanders + Gish.
- Honest scoping: open items (O1–O3) confined to §6 (Open questions) and clearly labeled in §0.

## §5 — Notes

**Per-venue cap warning:** This is the 1st *Linear Algebra and its Applications* paper in this J-series this quarter. Within cap; submission feasible.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

The substrate `V` sits within the TIG family of finite commutative non-associative magmas (and their `F_p`-lifts). The closest published precedent is **Drápal & Wanless (2021), *J. Combin. Theory A* 184, 105510** (*Maximally nonassociative quasigroups*) — same domain, opposite structural extremum (theirs maximally non-associative; `V` here is at the structurally regular end, with idempotents and a Grassmann annihilator). Cited in §0 (Lens) and the bibliography.

### PROVED / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVED:** Theorem 3.1 (total-dimension match) and Theorem 4.1 (refined-cell binomial grading = `Cl(2n)` grade dimensions). Proofs are elementary: a dimension count and a binary-string popcount identity, respectively.
- **COMPUTED:** Propositions 5.1 (refined `n=5`) and 5.2 (coarse `n=5`); the full `n = 0..5` verification ladder in `verify_J17.py` (6/6 PASS; closed-form binomial cross-checked against direct enumeration over `4^n` strings).
- **STRUCTURAL RHYME:** Coarse-cell `n=5` distribution `1, 5, 10, 10, 5, 1` matches dimensions of `SU(5)` `1 ⊕ 5̄ ⊕ 10` plus conjugate (Remark 5.3 in manuscript). Recorded as a binomial-coefficient coincidence, **not** a representation-theoretic theorem; the present paper does not construct an `SU(5)` action on `V^{⊗5}`.
- **OPEN:** O1 (structure-preserving map `V^{⊗n} ⊗_{F_5} K → Cl(2n; K)` over a common base ring `K`); O2 (canonical `Spin(2n)` action on `V^{⊗n}` realising the refined-cell weights as weight-space dimensions); O3 (whether the Cl-periodicity `Cl(n+8) ≅ Cl(n) ⊗ Cl(8)` has non-trivial content beyond `4^{n+8} = 4^n · 4^8`). All confined to §6.

### Lens-ownership paragraph

> *Lens and substrate.* This paper works with a single 4-dimensional commutative non-associative algebra `V` over `F_5` defined by an explicit multiplication table on the basis `{e_0, e_2, e_3, e_4}`; the table is tabulated in the companion paper J37 and recalled in §2 below. The two decompositions of `V` used in this paper (coarse two-summand and refined four-summand) are basis-dependent splittings of an `F_5`-vector space. The coarse decomposition is one of three possible 2+2 partitions of the four basis lines; the choice made here is the one inherited from J37. The refined decomposition is the canonical `F_5`-line decomposition determined by the named basis. The closest published precedent for this kind of small finite commutative non-associative magma substrate is Drápal–Wanless (2021); they sit at the maximally non-associative extremum of the same family, while the present `V` sits at the structurally regular end. The output of this paper is two basis-level statements (Theorems 3.1, 4.1); the lens-dependent choice of coarse pairing is recorded in Remark 2.1.

(The same paragraph appears in the manuscript as §0 "Lens, substrate, and claim tier.")

### R1 math fix log

- **R1 (2026-05-07):** Theorem 3.2 corrected (binomial-vs-grade conflation) per fresh-eyes referee report `J17_LinAlgApps_FreshEyes.md`; restructured §3–§4 into separate total-dimension and refined-cell sections; "fine cells" → "coarse cells" rename; refined-cell decomposition introduced as the correct object for Cl-comparison. Helper `refined_cell_distribution(n)` and `refined_cell_distribution_enumerated(n)` in `tig_dirac.py` retained for reference; submission-bundled `verify_J17.py` re-implements them standalone.

### Hardening status (auto-applied 2026-05-07; updated 2026-05-12)

- License: submission script CC-BY-4.0 header (`verify_J17.py`)
- AI-attribution: none in manuscript (acknowledgments name only the prior anonymous referee, no AI co-author)
- Author lane: Sanders + Gish; duplicate `\author{}` block split into separate `\author{Sanders}` + `\author{Gish}` per amsart convention
- Drápal–Wanless 2021 citation in bibliography and §0
- §0 added (Lens, substrate, claim tier) — was missing in v2026-05-07 draft; added 2026-05-12

## §6 — Submission checklist

- [x] Manuscript .tex finalized (referee-grade pass 2026-05-12)
- [x] Verification script green (`verify_J17.py`: 6/6 PASS at machine precision)
- [x] Tier-classified central claims explicit (Theorems 3.1, 4.1; Propositions 5.1, 5.2)
- [x] Lens-scope annotation (§0)
- [x] Cover letter finalized
- [x] Dependencies → J37 cited as "submitted to *Algebras and Representation Theory*"
- [x] R1 fresh-eyes math-fix applied (coarse vs. refined cells)
- [x] Verification script CC-BY-4.0 header
- [x] Per-venue cap check: 1st *Linear Algebra and its Applications* paper this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Total-Dimension Match Between Tensor Powers of a Finite-Field 4-Algebra and Real Clifford Algebras Cl(2n), with a Refined-Cell Grading." Submitted to *Linear Algebra and its Applications*.
