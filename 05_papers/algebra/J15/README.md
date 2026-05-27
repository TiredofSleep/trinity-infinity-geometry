# J15 — Galois D₄ over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor

**Status:** SUBMISSION-READY (manuscript referee-grade pass 2026-05-12; verification script `verify_J15_galois.py` 6/6 PASS at machine precision)
**Phase:** Phase 2
**Target venue:** *Communications in Algebra*
**Author lane:** Sanders + Gish
**Tier:** 1 (ship-ready (Communications in Algebra, SUBMISSION-READY))
**WP source:** WP105 (closed-form attractor) + WP113 (PSLQ uniqueness); Galois content of J35's Theorem D extracted into its own self-contained treatment
**Lens scope:** LENS-INVARIANT in the sense relevant to a Galois paper — the polynomial `f(x) = x^4 + 4x^3 - x^2 + 2x - 2` and its number field are algebraic objects independent of the TSML/BHML lens choice; the lens enters only in the *route* from `(T, B)` on `Z/10Z` to `f`.

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex`

The Galois-theoretic content of the four-core attractor — extracted from J35 (the *Journal of Algebra* corpus centerpiece, where it appears as Theorem D / Theorem 5.2 inside a six-check fusion-closure bundle) — and rebuilt as a self-contained 12-page algebraic-number-theory submission for *Communications in Algebra*. J15 differentiates from J35 by depth on the single Galois question: explicit irreducibility argument over `Q` (case-by-case + mod-7 cross-check), explicit cubic resolvent computation with rational root and quadratic-factor discriminant `-71`, explicit C_4-vs-D_4 distinction via irreducibility over `Q(sqrt(-71))`, explicit `Q(sqrt(3))`-factorization, and explicit Tschirnhaus reduction to LMFDB's canonical defining polynomial `x^4 - 7x^2 - 12x - 8`. J35 carries the broader fusion-closure picture; J15 carries the proof that justifies J35's bare assertion `Gal(f/Q) = D_4`.

**Single theorem (Theorem 1.1):** the unique positive real root `ξ* = r/β` of the four-core fuse iteration's fixed point satisfies `f(ξ*) = 0`; `Gal(f/Q) = D_4`; `K = Q[x]/(f) = LMFDB 4.2.10224.1`; `Q(sqrt(3)) ⊂ K`.

## §2 — Verification script

**Local path:** `manuscript/verify_J15_galois.py`

Six sympy checks for the Galois content (mapped one-to-one to the theorem's claims and the §3–§5 proof steps). Tested on Python 3.11+ with sympy. **6/6 PASS at machine precision.** Total runtime ~2 seconds.

```bash
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe verify_J15_galois.py
```

Expected output: six "OK" results in the summary table, "Overall: PASS."

The six checks are:

1. **Irreducibility over Q** — case-by-case ruling out of `(x^2 + ax + b)(x^2 + cx + d)` over `Z` for all four sign-cases of `bd = -2`, plus mod-7 irreducibility cross-check (and the mod-5 reducible counterexample recorded for transparency).
2. **Polynomial discriminant** — `Δ_f = -40896 = -2^6 · 3^2 · 71`.
3. **Cubic resolvent** — `g(y) = y^3 + y^2 + 16y + 36 = (y+2)(y^2 - y + 18)` with rational root `-2` and quadratic-factor discriminant `-71`.
4. **Galois group D_4** — `f` irreducible over `Q(sqrt(-71))` via `sympy.factor(f, extension=[sqrt(-71)])`, distinguishing `D_4` from `C_4` under the Cohen 1993 §6.3.2 classification.
5. **Q(sqrt(3)) subfield** — explicit factorization `f = (x^2 + (2+√3)x - (1+√3))(x^2 + (2-√3)x - (1-√3))` with conjugate quadratic discriminants `11 ± 8√3` (norm `-71`).
6. **LMFDB identification** — Tschirnhaus reduction `x → -x - 1` to `x^4 - 7x^2 - 12x - 8` (LMFDB's canonical defining polynomial of `4.2.10224.1`), index `[O_K : Z[ξ*]] = 2`.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J02** — *Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z.* Submitted to *Algebraic Combinatorics*. Provides the substrate (`(T, B)` tables and joint fuse data) that defines `F_{1/2}` and the four-core simplex.
- **J35** — *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z.* Submitted to *Journal of Algebra*. The corpus-centerpiece companion: J15 is the deeper standalone proof of J35's Theorem D Galois content.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-12 to:
- Reference `verify_J15_galois.py` as the green-light gate (6/6 PASS).
- Explicitly differentiate J15's role (depth on the Galois question) from J35's role (six-fact fusion-closure spread).
- Drop AI-attribution language; author lane Sanders + Gish only.

## §5 — Notes

**Per-venue cap warning:** This is the **1st *Communications in Algebra* paper** in this J-series this quarter. Within cap; submission feasible.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The closest published precedent for the input substrate is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative). The present paper does not depend on any specifically TIG-framework claim; the input substrate `(T, B)` is taken as given from the companion J02, and the output is a self-contained Galois-theoretic statement about the resulting fixed-point quartic.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem 1.1 in its entirety — irreducibility of `f` over `Q`, `Gal(f/Q) = D_4`, identification `K = LMFDB 4.2.10224.1`, and the `Q(sqrt(3))` subfield via explicit factorization.
- **COMPUTED:** Polynomial discriminant `-40896 = -2^6 · 3^2 · 71`; cubic resolvent `g(y) = (y+2)(y^2 - y + 18)` with rational root `-2` and quadratic-discriminant `-71`; Tschirnhaus reduction to `x^4 - 7x^2 - 12x - 8`; index `[O_K : Z[ξ*]] = 2`; irreducibility of `f` over `Q(sqrt(-71))`. All six checks PASS at machine precision in `verify_J15_galois.py` (~2 seconds).
- **STRUCTURAL RHYME:** The two quadratic subfields `Q(sqrt(3))` (from `h/β = 1+sqrt(3)`) and `Q(sqrt(-71))` (from `Δ_f`) reappear in other diagnostics across the parent framework's catalogue. Cited in §0 (Lens) as motivation for reader interest, not as a derivation.
- **OPEN:** Whether the route from `(T, B)` on `Z/10Z` to `LMFDB 4.2.10224.1` extends to other small finite commutative non-associative magma families is open; the present paper does not address α-uniqueness (companion J35 has a partial result; full uniqueness across `Q ∩ (0,1)` is stated as Conjecture 1.1 there).

### Lens-ownership paragraph

> *Lens and substrate.* This paper works on `Z/10Z` with two specific commutative non-associative magma tables `T` (TSML) and `B` (BHML), introduced and tabulated in the companion paper J02 (and surveyed alongside related "small finite commutative non-associative magma" work in Drápal–Wanless 2021). These tables are *not derived from first principles*; they reflect a structural reading of `Z/10Z` via a ten-operator decomposition. The four-element set `C_4 = {0, 7, 8, 9}` that produces the quartic of this paper arises as the unique fusion-closed sub-magma supporting the symmetric-mixing iteration `F_{1/2}` on `Z/10Z` under the joint action of `(T, B)`; closure across these specific tables is the substrate input, the Galois content of the resulting fixed point is the present paper's output. Analogous Galois questions on other substrate-and-table choices are open; whether other substrate choices yield similarly rich number-theoretic closures is not addressed here.

(The same paragraph appears in the manuscript as §0 / "Lens, substrate, and claim tier.")

### Hardening status (auto-applied 2026-05-07; updated 2026-05-12)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Anthropic / Claude byline references removed
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references and §0
- LaTeX header: `% J15 …` (was stale `% J22`); duplicate `\author{}` block split into separate `\author{Sanders} / \author{Gish}`
- Discriminant clarity: theorem now distinguishes polynomial discriminant `Δ_f = -40896` from field discriminant `d_K = -10224` and gives the index `[O_K : Z[ξ*]] = 2` explicitly

## §6 — Submission checklist

- [x] Manuscript .tex finalized (referee-grade pass 2026-05-12)
- [x] Verification script green (`verify_J15_galois.py`: 6/6 PASS at machine precision)
- [x] Tier-classified central claim explicit (single Theorem 1.1)
- [x] Lens-scope annotation
- [x] Cover letter finalized
- [x] Dependencies → J02 and J35 cited as "submitted to [venue]"
- [x] Brayden's referee-rigor pass complete (2026-05-12)
- [x] Verification script CC-BY-4.0 header
- [x] Per-venue cap check: 1st *Communications in Algebra* paper this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Galois D₄ over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor." Submitted to *Communications in Algebra*.
