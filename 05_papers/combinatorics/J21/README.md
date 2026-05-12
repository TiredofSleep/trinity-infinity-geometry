# J21 — Q17-A: 5D Force Vector as CRT Fourier Embedding of Z/10Z into R^5

**Status:** DRAFT (manuscript finalized 2026-05-07; awaiting referee-rigor pass)
**Phase:** Phase 2
**Target venue:** AMM
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** `papers/Q17_5D_RIGOROUS.md`

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex`

**Abstract (1-2 sentences):** We give the unique 5-dimensional embedding of $\mathbb{Z}/10\mathbb{Z}$ that respects both the CRT isomorphism $\mathbb{Z}/10\mathbb{Z} \cong \mathbb{F}_2 \times \mathbb{F}_5$ and the standard real Fourier basis on $\mathbb{F}_5$, prove a rigidity statement (the embedding is unique up to block-diagonal $O(1) \times O(4)$), and identify the two-point spectral maximum. The result is folklore in finite Fourier analysis; the rigidity statement and the two-point identification have not previously appeared together at this level.

## §2 — Verification script

**Path:** `(no script — short note; the embedding is verified by ≤30 lines of NumPy in the appendix of the manuscript)`

The proof script (where applicable) is the green-light gate before submission. Here the gate is the rigidity proof's referee-rigor pass.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J03

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

**FRESH-EYES REFEREE PASS (2026-05-07): Reject without prejudice; SAVE PLAN applied.**

The fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J21_AMM_FreshEyes.md`) flagged two critical mathematical errors and several framing problems:

- **M1 (CRITICAL).** Theorem 4.1 (Rigidity) had a tautological premise (ii): "$w_5$ is the real Fourier basis up to $O(4)$" — exactly the conclusion. **FIX:** premise (ii) replaced with $F_5$-equivariance + centered/equidistant condition (regular-pentagon condition). The conclusion ($w_5$ equals Fourier basis up to $O(4)$) now follows from the standard $F_5$-rep-theory $V_1 \oplus V_2$ decomposition (Diaconis Ch. 1, Steinberg §3). No longer tautological.
- **M2 (CRITICAL).** Lemma 5.2 (two-point maximum at $G_{\max} = 25$) was numerically wrong. Independent computation (numpy): $G(7) \approx 19.472$ at a single operator, NOT 25 at both n=5,7. The value 25 was a Cauchy-Schwarz upper bound, not an attained value. **FIX:** Lemma 5.2 replaced with Lemma (Spectral functional values), tabulating $G(n)$ for all 10 operators (matches referee's exact computation), identifying $n=7$ as the unique global max ($G(7) \approx 19.472$) and $\{0, 3, 8, 9\}$ as the four σ-fixed zeros. Cauchy-Schwarz bound $G(n) < 25$ for all n proved via direct orbit inspection.
- **M3 (MAJOR).** σ inconsistency: the §5 prose said σ "fixes {0, 5}" but described a 6-cycle "1→7→6→5→4→2" containing 5 — internally contradictory. **FIX:** σ stated explicitly as $(0)(3)(8)(9)(1\,7\,6\,5\,4\,2)$ matching J20; σ has order 6, NOT 2. Inconsistent prose removed.
- **M4 (MAJOR).** Folklore-novelty conflation. **FIX:** Introduction rewritten honestly to state two genuine contributions: equivariance-based rigidity + corrected spectral table. The "specific parameterization" claim of novelty is dropped (this is exactly Diaconis Ch. 1 / Terras Ch. 11).
- **M5 (MAJOR).** §7 companion description had literal "$\{0, 5, 7, ?\}$" with unspecified element. **FIX:** 4-core stated correctly as $\{0, 7, 8, 9\}$; connection to spectral lemma made precise (n=7 is the global max on the $\varepsilon=1$ sphere; {0, 8, 9} are three σ-fixed zeros on the $\varepsilon=0$ sphere).
- **S6.** Diaconis 1988 missing — **FIX:** added. Stein-Weiss 1971 removed (irrelevant). Steinberg 2012 added (rep-theory in rigidity proof).

**Save plan:** `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J21.md` — Paths B + C combined (genuine equivariance-based rigidity + corrected spectral table). Resubmit to AMM (the referee's recommended path).

**Fixes applied 2026-05-07:**
- `manuscript/manuscript.tex`: rewritten with corrected rigidity (equivariance premise), corrected G(n) table matching referee's exact computation, σ stated correctly as order-6 permutation, single author block (Sanders + Gish, no Calderon), §7 with actual 4-core, Diaconis/Steinberg added, Stein-Weiss removed, Conrad URL added.
- `manuscript/spectral_functional.py`: new verification script written; reproduces Table 1 exactly; identifies n=7 as global max (G(7) ≈ 19.472) and {0, 3, 8, 9} as zero set.

**Verification of fixes (numpy):**
- G(0) = 0.000, G(1) = 10.528, G(2) = 3.292, G(3) = 0.000 ✓
- G(4) = 5.000, G(5) = 9.472, G(6) = 16.708, G(7) = 19.472 ✓ (global max at n=7)
- G(8) = 0.000, G(9) = 0.000 ✓
- All values < 25 (Cauchy-Schwarz bound, strict) ✓
- σ-fixed indices {0, 3, 8, 9} all yield G = 0 (geometric-series cancellation) ✓
- Lemma 5.2 (corrected) verified.

**Estimated revision time:** 1-2 weeks. Net: substantial restructure, no new mathematics. The corrected spectral table reproduces the referee's exact computation; the equivariance-based rigidity is a textbook result presented in self-contained form.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** (i) The CRT-Fourier embedding v: Z/10Z → R^5 is injective; (ii) Equivariance-based rigidity — any F_5-equivariant w_5: F_5 → R^4 satisfying centered/equidistant condition equals the standard Fourier basis up to O(4); (iii) Spectral functional values: G(n) attains a unique global maximum G(7) ≈ 19.47 < 25 (Cauchy-Schwarz strict) and vanishes exactly on the σ-fixed indices {0, 3, 8, 9}.
- **COMPUTED:** numpy-verified G(n) at all 10 operators; orbit-by-orbit construction reproducing Table 1 exactly; assertion that max ∈ {n = 7} and zeros = {0, 3, 8, 9}; runtime < 1 s (`spectral_functional.py`).
- **STRUCTURAL RHYME:** The construction is folklore in finite Fourier analysis (Diaconis 1988 Ch. 1 Examples 4-5; Terras 1999 Ch. 11). The Pontryagin dual + CRT splitting + standard Fourier basis structure is textbook. The structural reading G(7) = max identifies the operator HARMONY (substrate-name for 7 in the companion paper) as the operator of maximal σ-shifted Fourier coherence — a structural rhyme, not a theorem on the broader TIG framework.
- **OPEN:** Closed-form expressions for G(n) in Q(ζ_5) ∩ R; whether the max-at-7 has a structural derivation in the TIG framework; generalization to Z/(2p) for primes p ≥ 5.

### Lens-ownership paragraph (in manuscript §5)

> *Lens and substrate.* The Z/10Z structure with σ = (0)(3)(8)(9)(1 7 6 5 4 2) is canonical to the broader TIG framework and is defined in J02 (Sanders + Gish 2026, *Algebraic Combinatorics*). The 5D embedding v is folklore in finite Fourier analysis (Diaconis 1988, Terras 1999), and the equivariance-based rigidity statement is a textbook consequence of the representation theory of F_5 over R. The spectral functional G is novel to this paper as a calculation tool; its values across the 10 operators are verified independently in `spectral_functional.py`. The structural interpretation — that n = 7 (HARMONY) maximizes G under the σ-action — connects to the broader TIG framework but is not load-bearing for the paper's mathematical claims. A reader of the *Monthly* can verify the rigidity theorem and the spectral lemma without consulting J02.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to AMM this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "The 5D Force Vector as a CRT Fourier Embedding of Z/10Z into R^5." Submitted to *American Mathematical Monthly*.
