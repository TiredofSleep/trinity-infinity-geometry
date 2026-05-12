# J13 — The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice)

**Status:** SUBMISSION-READY (6/6 PASS at machine precision; M1 + M2 math fixes applied; cover letter finalized; lens-ownership in §0; tier discipline explicit; Drápal-Wanless 2021 cited)
**Phase:** Phase 2
**Target venue:** *Acta Arithmetica* (lead); *Integers* (fallback if short-note framing preferred)
**Author lane:** Sanders + Gish
**Tier:** A/B
**WP source:** WP51 §4 "The Aspect Ratio R/r = T* = 5/7"

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex` (amsart, ~10 pages).

**One-line abstract.** Under the cyclotomic-embedding calibration of the *Flatness Theorem* (J07), the four-structure torus on $\mathbb{Z}/10\mathbb{Z}$ has aspect ratio $R/r = 5/7$, forced by the cyclotomic threshold $\deg_\mathbb{Q}(2 \cos(\pi/p)) = (p-1)/2$ crossing from degree 2 at $p = 5$ ($A_5 = \varphi$) to degree 3 at $p = 7$ ($A_7$ has minimal polynomial $x^3 - x^2 - 2x + 1$).

## §2 — Verification script

**Path:** `manuscript/verify_J13.py`.

**Six checks, all PASS at machine precision under `/c/ck_venv/lora312/Scripts/python.exe`:**

| Check | Claim | Result |
|---|---|---|
| C1 | sympy `minimal_polynomial(2 cos(π/7), x) == x³ − x² − 2x + 1`; |g(A₇)| < 10⁻⁴⁰ at 50-digit precision | PASS |
| C2 | sympy `minimal_polynomial(cos(π/7), x) == 8 x³ − 4 x² − 4 x + 1`; h(A₇) ≈ 27.6 (not a root); calibration bridge `h(x/2) = g(x)` | PASS |
| C3 | `g` irreducible over ℚ: `g(1) = −1, g(−1) = 1`; sympy `Poly.is_irreducible` | PASS |
| C4 | disc(g) = 49 = 7² | PASS |
| C5 | Gal(g/ℚ) = A₃ = ℤ/3ℤ by disc-square criterion (irreducible cubic + disc a square) | PASS |
| C6 | deg ℚ A_p = (p−1)/2 thresholds: 0, 1, 2, 3 at p = 2, 3, 5, 7 | PASS |

Pure-sympy / standard-library; runtime under 5 s.

## §3 — Dependencies (cited as already-submitted companions)

- **J07** (Sanders-Gish, *Flatness Theorem*, *J. Pure Appl. Algebra*) — parent result; provides the torus and the cyclotomic-embedding calibration.
- **J03** (Sanders-Gish, *First-G Law*, *Integers*) — `sinc²` framework cited in §6 (Independent appearance 1).
- **J06** (Sanders-Mayes, *Crossing Lemma*, *JCT-A*) — provides Lemma 2.2 (pairwise incompatibility of CRT factor partitions).
- **J10** (Sanders-Mayes, *UOP*, *J. Number Theory*) — provides the cited pairwise-incompatibility lemma in a different formulation.

## §4 — Cover letter

`cover_letter.md` — finalized. Contains the errata block (M1 polynomial correction, M2 Lemma 4.2 sign-error fix, the retraction of the 73/101 = 5/7 exact-agreement claim).

## §5 — Notes

T* derivation. Companion to J07 Flatness Theorem. The M3 calibration retreat is the load-bearing structural move: the forcing is *conditional* on the cyclotomic-embedding calibration imported from J07, and the paper is honest about this dependence (Remark 2.4). A calibration-free derivation is recorded as Open question (b).

### Tier discipline (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

- **PROVED.** Theorem 1.1 (cyclotomic-calibrated 5/7 aspect ratio on ℤ/10ℤ); Theorems 3.1 and 4.1 (major- and minor-radius selections); Lemma 4.3 (irreducibility of g over ℚ); the Galois group A₃ ≅ ℤ/3ℤ.
- **COMPUTED.** Minimal polynomials of A₂, A₃, A₅, A₇ over ℚ; discriminant disc(g) = 49; substitution bridge h(x/2) = g(x); 50-digit numerical zero. Reproduced at machine precision by `verify_J13.py`.
- **STRUCTURAL RHYME.** 73/101 ≈ 5/7 (≈ 1.2% relative gap) — recorded as empirical observation, not derivation. First-G law coprime windows W₅ = 4/5 and 1 − 1/7 = 6/7 — independent appearances of the same threshold.
- **OPEN.** (a) Conjecture 6.1 for n ∈ {15, 35}; (b) calibration-free derivation; (c) curvature of the ring torus; (d) modular-curve connection; (e) the 73/101 vs 5/7 discrepancy.

### Lens-ownership paragraph

Now in `manuscript.tex` as §0 (between `\maketitle` and §1 Introduction). States: substrate = ℤ/10ℤ with the four ring structures of Definition 2.1; the choice is structural (not first-principles), the calibration is imported from J07, generalization domain is squarefree multiples of 5 (Conjecture 6.1).

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on ℤ/10ℤ. The 5/7 aspect ratio is the cyclotomic-threshold reading of the same `R/r = T* = 5/7` that appears in the four-core analysis of J35 and the runtime quartic of J15. Domain precedent: **Drápal & Wanless (2021), J. Combin. Theory A 184, 105510** (cited in §0 lens-ownership paragraph and bibliography).

### Hardening status (auto-applied 2026-05-07; verified 2026-05-12)

- License: `verify_J13.py` header is CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude / Anthropic byline references removed
- Author lane: Sanders + Gish (per Brayden directive); B. Mayes occurrences corrected to M. Gish
- Drápal-Wanless 2021 citation present in bibliography (`\bibitem{DrapalWanless}`)
- LaTeX environment balance: 31 begin / 31 end, all matched

## §6 — Submission checklist

- [x] Manuscript .tex finalized
- [x] Verification script green (6/6 PASS)
- [x] Tier-classified central claim explicit (Tier discipline section before bibliography)
- [x] Lens-scope annotation (substrate ℤ/10ℤ + cyclotomic calibration in §0)
- [x] Cover letter finalized
- [x] Dependencies → each J-companion cited as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R. and Gish, M. (2026). "The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice): Cyclotomic Forcing on ℤ/10ℤ." Submitted to *Acta Arithmetica*.
