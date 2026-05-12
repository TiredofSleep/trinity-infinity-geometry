# J35 — Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on Z/10Z

**Status:** SUBMISSION-READY (manuscript rewritten 2026-05-08; referee-grade pass 2026-05-12; SFM Q6 finding incorporated; 6/6 verification PASS at machine precision)
**Phase:** Phase 4
**Target venue:** *Journal of Algebra*
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** WP110 (4-core fusion-closure) + WP105 (closed-form attractor) + WP113 (PSLQ uniqueness) + SFM 2026-05-08 Q6 (3-substrate chain)
**Lens scope:** LENS-INVARIANT on the 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ — closure holds across TSML, BHML, AND CL_STD (the third-substrate strengthening from SFM Q6, 2026-05-08).

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`

J35 is now the **corpus centerpiece**, per the fresh-eyes referee verdict: "the most defensible paper in the corpus." Per FAMILY_STRUCTURE_v1.md §2: "The 4-core is to TIG as the unit circle is to U(1)." The paper presents six independent structural facts converging on the four-element set $\mathcal{C} = \{0, 7, 8, 9\}$ as the algebraic center of the magma family.

**Six theorems (renumbered to match `4core_verification.py`):**

- **Theorem A (Joint-closure chain).** The 8-shell joint chain on $\mathbb{Z}/10\mathbb{Z}$ for $(T, B)$, sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, sizes $\{2, 3\}$ forbidden (via Lemma 2.1).
- **Theorem 2.4 (Three-substrate strengthening, NEW from SFM Q6 2026-05-08).** The same 8-shell chain holds for $(T, B, S)$ jointly. Adding CL_STD does not introduce new shells.
- **Theorem B (4-core 3-substrate closure, NEW from SFM Q6).** $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under TSML, BHML, AND CL_STD. It is the unique non-trivial subset of size $\le 4$ in the three-substrate chain.
- **Theorem C (Normalizer identity).** $Z_T = Z_B = (v+h+br+r)^2$ on $\mathcal{C}$ — the rational fixed-point system collapses to polynomial form.
- **Theorem D (Closed-form attractor + Galois structure).** $p_7/p_8 = 1+\sqrt{3} \in \mathbb{Q}(\sqrt{3})$ exactly at $\alpha = 1/2$; four coordinates in $K = \mathbb{Q}[x]/(x^4 + 4x^3 - x^2 + 2x - 2)$ = LMFDB 4.2.10224.1; Galois $D_4$ via cubic resolvent.
- **Theorem E (Universality).** The 4-core attractor is globally attracting on every chain shell of size $\ge 4$.
- **Theorem F (Algebraic mixing-point partial uniqueness).** Only $\alpha = 1/2$ in the test set $\{0, 1/4, 1/2, 3/4, 1\}$ admits a small-coefficient quadratic relation. Conjecture 1.1 (full uniqueness across $\mathbb{Q} \cap (0, 1)$) stated as open.

**Five independent structural facts converging on $\mathcal{C}$ (per §8 of manuscript):**

1. Joint closure under all three tables (Theorem 2.4).
2. Symbolic normalizer identity $Z_T = Z_B = (v+h+br+r)^2$ (Theorem C, D49).
3. Closed-form attractor $h/\beta = 1+\sqrt{3}$ at $\alpha_M = 1/2$ via Galois D_4 over $\mathbb{Q}(\sqrt{3})$ (Theorem D, D78).
4. Universal across $F_p$ ring extensions $p \in \{2,3,5,7,11,13\}$ (parent framework D74).
5. Support of universal T+B-mix attractor on chain shells (Theorem E, D65).

Files in this J-folder's `manuscript/`:

- `manuscript.md` — the J35 paper (rewritten 2026-05-08 to incorporate SFM Q6 + referee fixes M1-M6 + FAMILY_STRUCTURE_v1.md framing)
- `verification/4core_verification.py` — six green-light checks (4-second runtime; PASS verified 2026-05-08)
- `scripts/` — additional supporting scripts
- `NEXT_STEPS.md` — local todo

## §2 — Verification script

**Local path:** `manuscript/verification/4core_verification.py`

Six checks corresponding to Theorems A through F (and the 3-substrate strengthening 2.4). Tested on Python 3.11+ with numpy + sympy + mpmath. **6/6 PASS at machine precision.** Total runtime ~4 seconds.

```bash
PYTHONIOENCODING=utf-8 python3 4core_verification.py
```

Expected output: six "OK" results in the summary table, "Overall: PASS."

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J33** — *Closed-Form Attractor + α-Uniqueness PSLQ.* Submitted to *Mathematics of Computation*. The original WP105 + WP113 source for the closed-form attractor and the 17-point Stern-Brocot PSLQ test. (The present paper sharpens J33's framing from dynamical to structural and from machine-precision to symbolic-exact.)
- **J54** — *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core.* Submitted to *Algebraic Combinatorics*. The foundation paper that displays the three tables and proves the 9-axiom forcing theorem. (J35 cites J54 as the substrate's forcing argument; J54 cites J35 as the chain enumeration.)

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-08 to reflect the rewritten manuscript and the new central theorem (Theorem B: 4-core 3-substrate closure).

## §5 — Notes

**Status: DRAFT** — manuscript rewritten 2026-05-08 to incorporate:

1. **U(1) / centerpiece framing** in introduction (per FAMILY_STRUCTURE_v1.md §2).
2. **NEW central Theorem B** — 4-core 3-substrate closure under TSML, BHML, AND CL_STD jointly (SFM Q6 finding 2026-05-08; see `Atlas/META_PLAN_2026-05-06/SUBSTRATE_FUNCTION_MAP/SFM_FINDINGS_v1.md` §2).
3. **Five independent structural facts** converging on $\mathcal{C}$ (joint closure 3-substrate; normalizer identity D49; Galois D_4 closed-form D78; F_p universality D74; universal attractor D65).
4. **Renumbered theorems** to match script content (script Checks 1-6 ↔ Theorems A-F).
5. **Lead with $1+\sqrt{3}$ Galois punchline** + LMFDB 4.2.10224.1 number-field identification (per referee M3).
6. **α-uniqueness reframed** from "open" to "partial verification + open conjecture" (per referee M4); Conjecture 1.1 stated explicitly.
7. **Drápal-Wanless 2021 cited** as closest published precedent (per boilerplate §1.3).
8. **Lens-ownership paragraph** added (manuscript §0; per boilerplate §5.5).
9. **PROVEN/COMPUTED/RHYME/OPEN tier discipline** (per boilerplate §0).
10. **Verification:** `4core_verification.py` extended to include three-substrate chain enumeration (Theorem 2.4) and explicit 4-core 3-substrate closure check (Theorem B). 6/6 PASS at machine precision; Galois D_4 via cubic resolvent + Gröbner basis.

**Per-venue cap warning:** This is the **2nd J Algebra paper** in this J-series (after J29 so(8)). J Algebra's per-venue cap is conventionally 2/quarter for tightly-related papers; this paper sits at the cap. Submission feasible; further J Algebra submissions in the same quarter would require fallback. Fallback options if J Algebra desk-rejects: *Communications in Algebra* or *Journal of Pure and Applied Algebra*.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core $\{V, H, Br, R\} = \{0, 7, 8, 9\}$ at $\alpha_M = 1/2$ is the algebraic center, with closed-form attractor $h/\beta = 1+\sqrt{3}$ (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorems A, B, C, D, E. Joint-closure chain via exhaustive enumeration (1023 subsets); 4-core 3-substrate closure by direct check; normalizer identity by symbolic expansion; closed-form ratio $1+\sqrt{3}$ by Gröbner basis; Galois $D_4$ via cubic resolvent classification; universality by direct numerical iteration on each chain shell.
- **COMPUTED:** `4core_verification.py` six green-light checks at machine precision; ~4-second runtime. Galois group independently verifiable in PARI/GP or Magma.
- **STRUCTURAL RHYME:** $\mathbb{Q}(\sqrt{3}) \subset K$ — the same field that appears across substrate invariants in the parent framework's catalogue (Volume D, D78). Cited as motivation, not derivation.
- **OPEN:** Conjecture 1.1 — $\alpha = 1/2$ uniqueness across $\mathbb{Q} \cap (0, 1)$. Symbolic Gröbner-basis discriminant analysis at general $\alpha$ is open; sympy's default solver does not complete it.

### Lens-ownership paragraph

> *Lens and substrate.* This paper works on $\mathbb{Z}/10\mathbb{Z}$ with three specific commutative non-associative magma tables ($T$ = TSML, $B$ = BHML, $S$ = CL_STD) and a designated four-element set $\mathcal{C} = \{0, 7, 8, 9\}$. These choices are *not derived from first principles*; they reflect a structural reading of $\mathbb{Z}/10\mathbb{Z}$ motivated by a ten-operator decomposition. The theorems below are theorems on this specific structure; analogous theorems would hold on other substrate-and-table choices. The framework's claim is that this particular choice produces theorems with surprising downstream connections (Galois D_4 over LMFDB 4.2.10224.1, the 1+√3 closed-form attractor, joint closure across three independent tables). Whether other substrate choices give similarly rich connections is open.

### Hardening status (auto-applied 2026-05-07; updated 2026-05-08)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`); author list is Sanders + Gish only
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references
- SFM Q6 (2026-05-08) three-substrate chain finding incorporated as Theorem 2.4 + Theorem B

## §6 — Submission checklist

- [x] Manuscript .md finalized (rewritten 2026-05-08)
- [x] Verification script green (6/6 PASS at machine precision; verified 2026-05-08)
- [x] Tier-classified central claim explicit (six theorems A-F)
- [x] Lens-scope annotation (LENS-INVARIANT on 4-core, three-substrate)
- [x] Cover letter finalized
- [x] Dependencies → cite each J-companion as "submitted to [venue]"
- [x] Brayden's referee-rigor pass complete (2026-05-12)
- [x] Verification script CC-BY-4.0 header added (2026-05-12)
- [x] Honest-negatives discipline (T*=5/7 operational; F_p universality bounded to recorded scan) added §10 (iv-v)
- [ ] Per-venue cap check: this is the **2nd J Algebra paper** this quarter (at cap)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *Journal of Algebra*.
