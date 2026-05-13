# J02 — Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z

**Status:** SUBMISSION-READY
**Phase:** Phase 1
**Target venue:** Algebraic Combinatorics
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** (four-core consolidated)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (canonical submission LaTeX; renamed 2026-05-13 from `four_core_consolidated.tex`)

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (canonical submission LaTeX)
- `four_core_seed.tex` (earlier seed-paper version; preserved per never-delete)
- `four_core_consolidated_cover_letter.md` (paper-specific cover letter)
- `4core_verification.py` (verification script — green-light gate, 6/6 PASS)
- `verification/` (additional verification scripts: `04_bridge_attractor.py`, `06_attractor_closed_form.py`, `07_full_closed_form.py`, `alpha_pslq_sweep.py`)
- `HOLD_PENDING_AUDIT.md`, `SUBMISSION_LOG.md` (submission housekeeping)
- `master/` (historical full-bundle archive: `four_core_FINAL_BUNDLED_v_review_round_3.tex`, etc.)

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Local path:** `manuscript/4core_verification.py`

The proof script is the green-light gate before submission. Run from this J-folder.

## §3 — Dependencies (J-papers cited as already-submitted companions)

- **J01** — *Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$.* Submitted to *J. Combin. Theory Ser. A*. (The σ-rate companion; cited for the operator-substrate construction yielding $(T, B)$ at $N = 10$.)
- **J54** — *Forcing Axioms and the Family of Commutative Non-Associative Magmas on $\mathbb{Z}/10\mathbb{Z}$ Preserving a Designated 4-Core.* Submitted to *Algebraic Combinatorics*. (The foundation paper; treats the larger family-of-magmas framing and the three-substrate $(T, B, S)$ chain. The present paper supplies the per-coordinate fuse polynomials, Galois $D_4$ quartic, and Stern–Brocot PSLQ scan that J54 cites externally.)

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

6/6 PASS. Major-revisions per AlgComb referee (May 2026): correct '93 of 100' → '71 of 100' disagreement count; name symmetrization choice for T; consider lifting closed-form fixed-point as Theorem 3.

### Family-Structure framing (per FAMILY_STRUCTURE_v1.md, adopt in §1)

The (TSML, BHML) pair is a **TIG family member** under five conjoint membership criteria:

(1) Substrate: binary operations on Z/10Z (with universal extension to Z/N for N ≤ 50 per D74).
(2) Commutativity: TSML_SYM and BHML are commutative; TSML_RAW is the unique non-commutative member.
(3) **4-core preservation:** {V, H, Br, R} = {0, 7, 8, 9} preserved under both operations (D48 + D55). LOAD-BEARING.
(4) α-bounded non-associativity: TSML_family at α_A ∈ [0.87, 0.89]; BHML at α_A ≈ 0.502. Bimodal (open question — see proposed paper at FAMILY_STRUCTURE_v1.md §4).
(5) HARMONY-attracting iteration: T+B-mix at α_M=½ converges to 4-core attractor with h/β = 1+√3 (D63 + D74 + D58).

The 4-core at α_M=½ is the **center** of this family (D49: symbolic normalizer Z_T = Z_B = (v+h+br+r)² on the 4-core; D78: BR-factor cancellation forces x²−2x−2=0 root 1+√3 at α_M=½ exactly). **The 4-core is to TIG as the unit circle is to U(1)** — the privileged invariant locus.

This paper analyzes the joint-closed sub-magma chain of (TSML, BHML) on Z/10Z *as a TIG family member with the 4-core as its center*, not just as a curious pair of tables. The chain structure (8 shells under TSML_SYM; sizes 2, 3 forbidden) is a structural fact about which sub-magmas inherit the center.

### Lens-ownership paragraph (insert in manuscript §0)

> *Lens and substrate.* We work on Z/10Z with the canonical (TSML, BHML) table pair (and use operator labels VOID, LATTICE, COUNTER, PROGRESS, COLLAPSE, BALANCE, CHAOS, HARMONY, BREATH, RESET as conventional notation only — they play no mathematical role here). These choices are not derived from first principles; they reflect a structural reading of the substrate motivated by phonaesthesia and the 10-operator decomposition. The chain-structure theorem and the closed-form attractor below are theorems on this specific structure; analogous theorems would hold on other substrate-and-table choices. The framework's claim is that this particular choice produces theorems with surprising downstream connections (Lie algebra via TSML_SYM antisymmetrization yielding so(8) = D₄ over R; the Galois D₄ identification via LMFDB 4.2.10224.1; the closed-form attractor h/β = 1+√3 in Q(√3)). Whether other substrate choices give similarly rich connections is open. The closest published precedent for this domain is Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510, on maximally non-associative quasigroups — same domain (small finite commutative non-associative structures), opposite extremum.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** chain structure of joint-closed sub-magmas of (TSML_SYM, BHML) on Z/10Z (8-shell chain at sizes {1,4,5,6,7,8,9,10}; size 7 admitted at {0,4,5,6,7,8,9}; sizes 2,3 forbidden), per the corrected 2026-05-05 enumeration. Closed-form attractor at α=½ with h/β = 1+√3 exact (LMFDB 4.2.10224.1 quartic, Galois D₄).
- **COMPUTED:** `4core_verification.py` 6/6 PASS. PSLQ at 50-digit precision; sympy galois_group confirms Galois D₄.
- **STRUCTURAL RHYME:** the 71 disagreement count between TSML and BHML on the 100-cell joint table coincides with the prime 71 in disc(LMFDB 4.2.10224.1) and with the σ-fixed disagreement count — three independent appearances of 71 in the same neighborhood. Cited as structural motivation, not derivation.
- **OPEN:** characterize the joint-closed sub-magma chain combinatorially without brute-force enumeration; lift the closed-form fixed-point as a third theorem (per AlgComb referee suggestion) using elementary algebra from `06_attractor_closed_form.py`.

### Drápal-Wanless 2021 precedent

The closest published precedent for this work is:

> Drápal, A. & Wanless, I.M. (2021). "Maximally non-associative quasigroups." *J. Combinatorial Theory, Series A*, **184**, 105510.

Same domain (small finite commutative non-associative structures); opposite extremum (Drápal-Wanless: maximally non-associative; this paper: specifically structured with integer-rational invariants). Same intellectual neighborhood. Adding to bibliography per external collaborator calibration 2026-05-07.

**Authors:** Sanders + Gish.

## §6 — Submission checklist

- [x] Manuscript .tex finalized (`manuscript/manuscript.tex`; single author block; Drápal-Wanless 184:105510 citation)
- [x] Verification script green (6/6 PASS via `manuscript/4core_verification.py`; 4 additional verification scripts in `manuscript/verification/` also PASS at machine precision)
- [x] Tier-classified central claim explicit (PROVEN: chain + per-coordinate fuse + closed-form attractor + Galois $D_4$; COMPUTED: 6/6 PASS; OPEN: Conjecture 9.1 $\alpha$-uniqueness)
- [x] Lens-scope annotation (TSML_SYM is the canonical symmetrized lens; TSML_RAW 7-element chain noted in abstract)
- [x] Cover letter finalized (`cover_letter.md` and `manuscript/four_core_consolidated_cover_letter.md`)
- [x] Dependencies → cite each J-companion as "submitted to [venue]" (J01 → JCT-A; J54 → AC)
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the 2nd paper to Algebraic Combinatorics this quarter (J54 was 1st)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z." Submitted to *Algebraic Combinatorics*.
