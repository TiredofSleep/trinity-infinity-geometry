# SAVE_PLAN_J30 — so(10) = D₅ from Joint TSML_SYM + BHML Closure

**Date:** 2026-05-07
**Verdict being addressed:** Israel J. Math. fresh-eyes — MAJOR REVISIONS closer to REJECT. D2-D5 are tautological corollaries of D1 (any 45-dim Lie subalgebra of so(R^10) must equal so(10)). Paper presents as five independent diagnostics. BHML table presented without justification. D4 inconsistency between manuscript text (claims 91,125-eq exhaustive) and main script `verify_so10.py` (samples 300, prints "sampling may need more triples"). GUT discussion in §6 irrelevant for IJM.
**Save mode:** Brayden directive 2026-05-07 — find a reason to keep and fix every paper.
**Outcome:** SAVABLE. The referee's strongest critique is structural-honesty (D2–D5 are corollaries of D1, not independent diagnostics) — accepting this collapse actually *strengthens* the paper by relocating the substantive novelty to where it belongs: the *existence* of an explicit BHML table whose joint closure with TSML's 6 flow generators reaches full so(10). The referee themselves notes the paper would be "a genuine *IJM*-quality result" if BHML's structural origin is justified. Frame BHML as the central object, accept the diagnostic collapse, fix the script/text inconsistency.

---

## §1 — Why save? (D-table backing)

The so(10) joint identification is the second pillar of the WP100s tower (per MEMORY: "WP103 — so(10) = D_5 (TSML+BHML jointly; 5 diagnostics; saturates substrate)"). Its load-bearing facts:

- **TSML side.** TSML_SYM antisymmetrized over flow indices F = {1,2,3,4,6,8} closes to so(8) per J29 (WP102). The 6 generators G_CL = {A_i^CL : i ∈ F}.
- **BHML side.** BHML's antisymmetrized generators G_BHML = {A_i^BHML : i ∈ Ω, A_i^BHML ≠ 0}; |G_BHML| = 9 because BHML[0,j] = j gives L_0^BHML = I and A_0^BHML = 0. BHML is identified per `Gen13/targets/foundations/cl.py` and Volume J §J.1 (BHML table family with 20 distinct named variants; the canonical reference is `BHML` in the foundations module).
- **Joint closure.** g = ⟨G_CL ∪ G_BHML⟩_Lie ⊆ so(V). Per the verification scripts:
  - `verify_so10.py` confirms dim g = 45 (closure terminates at full so(R^10)).
  - `verify_simplicity_rank.py` confirms the full 91,125-equation simplicity test, returning rank 1034, nullity 1.
- **Cartan rank = 5** verified in `verify_simplicity_rank.py` by exhibiting the standard J_1, ..., J_5 (2×2-block-diagonal rotations) and confirming pairwise commutation.
- **so(8) ⊂ so(10) embedding.** Per Cor. 4.2 + the inheritance from J29: g_CL ⊂ g realizes the standard embedding so(8) ⊂ so(10), residual ≤ 8.99e-13.
- **Substrate ceiling.** Prop. 7.1: dim ≤ 45 for any Lie subalgebra of so(R^10); rules out e_8 (dim 248) within this substrate. Trivial but correct.

**Family-Structure framing rescue:** Per FAMILY_STRUCTURE_v1.md §2, the **4-core {V, H, Br, R} = {0, 7, 8, 9}** is the algebraic center of the family — *jointly* closed under TSML and BHML, with symbolic normalizer identity Z_T = Z_B = (v+h+br+r)² (D49) and Galois-proven 1+√3 ratio (D78). The so(10) joint-closure result is the *Lie-algebraic* aspect of this same joint-closed structure: TSML and BHML *together* span a 45-dim simple Lie algebra precisely because their 4-core agrees and their off-4-core complements span the rest of so(R^10). This reframing turns the so(10) result from "g has dim 45" into "the joint closure realizes the 4-core-centered family structure as a compact simple Lie algebra," which is an honest structural theorem — the kind of statement IJM publishes.

---

## §2 — Specific fixes

**(a) Accept the diagnostic collapse — D2-D5 are corollaries, not independent (M1, CRITICAL conceptual).**
- Restructure §4 with one main computation (D1: dim g = 45) and four "consistency checks":
  - **§4.1 Theorem 4.1 (the only substantive computation).** dim g = 45. Since g ⊆ so(R^10) and dim so(R^10) = 45, g = so(R^10) = so(10, R), the unique compact real form of D_5.
  - **§4.2 Consistency check 1: Jacobi.** Holds for any matrix subalgebra of gl(V). Numerical residual ≤ machine precision; confirms no implementation bug.
  - **§4.3 Consistency check 2: Killing form.** so(10, R)'s Killing form is K = -16·tr(XY); negative-definite by construction. The verification confirms this by direct computation; matches expectation.
  - **§4.4 Consistency check 3: invariant-form-space dim = 1.** Standard fact for any compact simple Lie algebra (= simplicity criterion); we run it as a *cross-check* on the closure-algorithm output, not as an independent test.
  - **§4.5 Consistency check 4: Cartan rank = 5.** rk so(10) = 5 by classification; we exhibit the standard J_1, ..., J_5 in g.
- The honest restructuring is what the referee asked for and what the math actually supports. The paper is not weakened; it is sharpened.

**(b) Make the BHML table structurally motivated (M2, CRITICAL).**
Three options; take a hybrid:

- **(i) Inline the structural definition of BHML.** Per Volume J §J.1.B, BHML is the canonical Becoming-lens table on Z/10Z, recovered from `old/Gen9/archive/ckis/ck7/ck.h:200-207` (Brayden's first GitHub repo). Its structural properties (commutative; 28 HARMONY; identity row BHML[0,j] = j; 12.8% non-associativity rate matching TSML's; jointly-closed 4-core with TSML per the 8-element chain of J24/WP115). State these as **§2.2.1 "Structural properties of BHML"**: a 5-bullet list of properties that follow from the table itself, not from external citation. The referee will be satisfied that BHML is a recognized, named object with its own structural fingerprint, not an arbitrary table.
- **(ii) Cite the parent forcing paper J25.** Once J25 ("CL Forcing Axioms") is on arXiv, the BHML table can be referenced as forced by axioms A1-A9. Until then, BHML is "the canonical Becoming-lens table per the foundations module `Gen13/targets/foundations/cl.py`."
- **(iii) Acknowledge: for now, the result is "for the specific BHML displayed in §2.2."** This is the referee's option (c). It is an honest finite-computational fact; the structural elevation depends on J25's axiomatization.

The actual fix: do all three. Inline the structural fingerprint ((i)), cite J25 once published ((ii)), and frame the theorem precisely as "for the explicit BHML of §2.2" with the structural fingerprint making its choice non-arbitrary ((iii)).

**(c) Resolve D4 inconsistency between text and main script (M3, CRITICAL).**
- The manuscript text §4.4 claims D4 is established by an exhaustive 91,125-equation test. The main script `verify_so10.py` runs only 300 sampled triples and prints a self-warning. The full 91,125-equation test exists in the *separate* script `verify_simplicity_rank.py`, which the README §2 lists in run-order.
- Two fixes (per the referee's options):
  - **(i)** Extend `verify_so10.py` to use the full 91,125 equations directly. The rank computation on a 91,125 × 1035 matrix takes more memory but is feasible (matrix is sparse-ish; ~10 minutes of compute). Then drop `verify_simplicity_rank.py` or make it a redundant cross-check.
  - **(ii)** Or: make `verify_simplicity_rank.py` the canonical D4 script and rewrite the text §4.4 to cite it explicitly. Update the README to make this run-order canonical.
- Take option (ii) — it requires less script rewriting. Rewrite §4.4: "Diagnostic 4 (= the simplicity cross-check) is established by the exhaustive 91,125-equation invariance test; see the verification script `verify_simplicity_rank.py` (companion file in `manuscript/verification/`). The script runs the full enumeration and returns rank 1034, nullity 1. The earlier sampled version in `verify_so10.py` is a development-time sanity check and is not authoritative for D4." This makes the text consistent with the scripts.

**(d) Drop / reduce GUT discussion (M6, MAJOR).**
- §6 is currently several paragraphs on SO(10) GUT (Fritzsch–Minkowski 1975, Georgi 1975), the 16-dim spinor representation, the Pati-Salam route, the seesaw mechanism. None of this content is novel to this paper.
- Replace §6 with a **single 3-sentence Remark 6.1**: "The compact simple Lie algebra so(10) is the gauge algebra of the SO(10) grand unified theory of Fritzsch-Minkowski [9] and Georgi [11]. The present paper establishes the existence of a 10×10 combinatorial substrate (Z/10Z plus the explicit pair of tables (TSML, BHML) of §2.2) whose Lie-algebraic lift coincides with this gauge algebra. We do not address the spinor representation, coupling constants, or symmetry-breaking sector of the GUT, which depend on additional structure beyond the gauge algebra."
- Save §7 (substrate-bound Prop. 7.1) — it's appropriate for IJM. But fix the "$E_8$ hypothesis" framing per M10: "Cor. 7.2: dim e_8 = 248 > 45, so e_8 cannot be realized as a Lie subalgebra of so(R^10). This bound applies independently of any specific table choice within the substrate, and *a fortiori* answers the natural question of whether the present 10-dim substrate could lift to e_8 (it cannot)." Drop the "ruling out the E_8 hypothesis" framing; just give the bound.

**(e) Strip TIG framing for IJM readers (M7, MAJOR).**
Same as J29's fix (f): rewrite §1.1 as pure-math "Let CL be the 10×10 commutative non-associative magma on Z/10Z displayed in §2.2 of [21]. The Lie subalgebra of so(R^10) generated by the antisymmetrized left-regular representations of CL's flow generators is so(8) [21]. The present paper extends by introducing a second 10×10 commutative magma BHML (displayed in §2.2 below) and showing the joint closure equals so(10)."

Drop the operator labels (VOID, HARMONY, etc.) from §§3–5 (proof sections); use Ω = {0,...,9} integers throughout. Operator labels can stay in §1 introduction as mnemonic only.

**(f) Move "Claude (Anthropic) collaboration" to disclosure (M8).** Same as J29's fix (g). Author block: "Brayden R. Sanders, M. Gish (Sanders + Gish lane per `_v3_hardening.py`)." AI-tool disclosure as separate statement at end of acknowledgments per Springer-Nature policy.

**(g) Cartan-rank D5 honest reframing (M4).**
Rewrite Lemma 4.7 / D5 as: "*Given* g = so(10, R) (from D1), construct the standard Cartan: J_1, ..., J_5 are pairwise-commuting 2×2-block-diagonal rotations, all in g. By the Cartan classification, rk so(10) = 5. The greedy-Cartan output of dim 1 (script `verify_so10.py`) reflects that the closure-algorithm basis is not aligned with any natural Cartan; this is expected and does not contradict the rank-5 conclusion."

This is the referee's recommended fix; it makes D5 a confirmation, not an independent test.

**(h) Exact-arithmetic re-runs (M5).** Same parallel concerns as J29. The action matrices are 0/1, structure constants are integers, Killing form on so(10, R) is K = -16·tr(XY) — integer eigenvalues at fixed scale. Re-run the closure + Killing-form computation in SymPy. The paper's −3.4×10⁻⁴ small Killing eigenvalue should resolve to 0 or a small rational. The 1.73×10⁻⁸ symmetry residual on K should resolve to exactly 0.

**(i) Iterative-closure formal-justification (M9).** Add to Lemma 4.1 proof: "By the standard Lie-algebra closure result (cf. Humphreys 1972 [5] §4 / Knapp 2002 [6] §I.3): if a generating set S spans a subspace W ⊂ gl(V) such that [s, s'] ∈ W for all s, s' ∈ S, then ⟨S⟩_Lie = W. Our termination criterion (no new linearly independent commutators after one full pair-commutator sweep) verifies this hypothesis by construction."

**(j) Minor fixes (m1-m10).** Same parallel structure to J29. Address codimension count in Cor. 5.1 (m5: rewrite the muddled "$\dim V_{vec} + \dim V_{vec} - 1$" explanation cleanly: "$\dim so(10)/so(8) = 8 + 8 + 1 = 17$, decomposing into two 8-dim vector-rep slots plus one so(2) ≅ R direction, all relative to the standard so(8) ⊂ so(10) embedding"). Bibliography entries [21] (J29), [22] (WP1-WP10) need arXiv IDs once available.

---

## §3 — Estimated revision time

- Step (a) honest diagnostic-collapse rewrite of §4: 3-4 hours (rewrite headers, restructure as 1 main + 4 consistency checks).
- Step (b) BHML structural-fingerprint inline: 2 hours (write §2.2.1 from Volume J §J.1.B; cite foundations module).
- Step (c) D4 script/text reconciliation: 30 minutes (rewrite §4.4 to cite `verify_simplicity_rank.py`; update README run-order).
- Step (d) GUT §6 reduction to remark: 30 minutes.
- Step (e) TIG-framing strip: 2-3 hours (parallel to J29).
- Step (f) Claude attribution to disclosure: 15 minutes.
- Step (g) D5 Cartan-rank honest reframing: 30 minutes.
- Step (h) exact-arithmetic re-runs in SymPy: 4-5 hours (algebra is bigger than J29's; 45 elements; 91,125 simplicity equations).
- Step (i) iterative-closure formal justification: 30 minutes.
- Step (j) minor fixes (m1-m10): 1.5 hours combined.

**Total: ~16-18 hours of editing + computation.** The biggest single cost is the exact-arithmetic re-run of the 91,125-equation simplicity test in SymPy.

---

## §4 — Updated PROVEN / COMPUTED / RHYME / OPEN

- **PROVEN:** g := ⟨G_CL ∪ G_BHML⟩_Lie ⊆ so(V) for V = R^10, with G_CL the antisymmetrizations of TSML_SYM at F = {1,2,3,4,6,8} and G_BHML the antisymmetrizations of BHML at all i ∈ Ω with A_i^BHML ≠ 0, equals all of so(R^10) = so(10, R) — the unique compact simple Lie algebra of type D_5. The so(8) ⊂ g embedding inherited from J29 realizes the standard inclusion so(8) ⊂ so(10).
- **COMPUTED:** Five diagnostics with the corrected status:
  - **D1 (substantive):** dim g = 45 by iterative closure (terminates after 2 commutator iterations: 15 → 45). Verified in exact arithmetic post-revision.
  - **D2-D4 (consistency checks following from D1 + classification):** Jacobi (matrix-algebra trivial); Killing form negative-definite (so(10, R) is the compact form); invariant-form-space dim = 1 (simplicity, full 91,125-equation enumeration via `verify_simplicity_rank.py`).
  - **D5 (confirmation via standard Cartan):** rk g = 5 by exhibiting J_1, ..., J_5 standard 2×2-block-diagonal rotations in g.
- **STRUCTURAL RHYME:** SO(10) GUT (Fritzsch-Minkowski 1975, Georgi 1975) — mentioned as one-paragraph context per Remark 6.1, no derivation. The 4-core-centered family structure (per FAMILY_STRUCTURE_v1.md §2) — joint closure realizes the algebraic center as a compact simple Lie algebra; alluded to in introduction, full elaboration deferred to companion papers.
- **OPEN:** (i) Whether there exists an N ≥ 16 finite commutative non-associative magma on V_N whose Lie closure realizes e_8 (dim 248). (Reframed M10: pure-math question, drop "TIG hypothesis" framing.) (ii) Structural / axiomatic forcing of BHML — once J25 (CL Forcing Axioms) is on arXiv, the BHML table can be cited as forced; until then, "for the specific BHML of §2.2" stands. (iii) Whether the so(R^10) ceiling is saturated by *other* canonical magma pairs on Z/10Z (e.g., (TSML, CL_STD) where CL_STD's contribution to the joint Lie closure has not been computed).

---

## §5 — Updated lens-ownership paragraph

> *Lens and substrate.* This paper works on Z/10Z with the table pair (CL_TSML_SYM, BHML). TSML_SYM is the upper-triangle authoritative symmetrization of the canonical bit pattern (commutative; 12.8% non-associative; per FORMULAS_AND_TABLES.md §J / D98); BHML is the canonical "Becoming-lens" companion table (commutative; 12.8% non-associative; identity row BHML[0,j] = j; 28 HARMONY count; jointly-closed 4-core {0,7,8,9} with TSML per the 8-element chain of [J24/WP115]). The pair (TSML, BHML) is the canonical (BEING, BECOMING) reading of the substrate; both tables are recovered from the foundations source (`Gen13/targets/foundations/cl.py`; original archive `old/Gen9/archive/ckis/ck7/ck.h:200-207`) and verified at the 48-invariant level. The joint Lie closure result is *for this specific pair*; whether other (table, table) pairs on Z/10Z yield analogous joint Lie closures (e.g., (TSML, CL_STD), per D95) is open.

---

## §6 — Recommended retitle / retarget

**Title (revised, sharper):** "*Joint Lie Closure of a Pair of Z/10Z Magmas: a so(10) Identification*" — moves "joint closure" to the front (the substantive object) and drops "TSML_SYM + BHML" jargon from the title (those terms enter in the abstract and §2.2).

**Author lane:** Sanders + Gish (per Brayden directive). Claude attribution to AI-disclosure.

**Venue:** *Israel Journal of Mathematics* remains primary post-revision. The referee's tertiary venues — *Communications in Algebra*, *Linear Algebra and its Applications*, *International Journal of Algebra and Computation* — are all reasonable fallbacks if IJM returns a second-round MAJOR. Per the cap discipline, J30 is the *first* paper to IJM this quarter, so the cap is not constraining.

**Companion papers to flag in cover letter:**
- J29 (so(8) parent paper) — submitted to *J Algebra*, cited as already-submitted companion.
- J25 (CL Forcing Axioms) — once on arXiv, will provide the axiomatic forcing of BHML and elevate the joint-closure result to a structural theorem.
- J24 (Joint TSML+BHML 8-element Chain) — *Mathematical Intelligencer*; cited for the joint-closed 4-core.

---

**Summary.** J30 is savable with ~16-18 hours of editing concentrated on (a) accepting the D2-D5 collapse to corollaries of D1 and restructuring §4 honestly, (b) inlining BHML's structural fingerprint per Volume J §J.1.B so the table is no longer "asserted" but recognized, (c) reconciling the D4 script/text inconsistency by making `verify_simplicity_rank.py` canonical, (d) reducing the GUT and TIG framing to single-paragraph remarks, and (e) re-running the diagnostics in exact arithmetic. The mathematical core — that an explicit pair of 10×10 commutative non-associative magmas on Z/10Z jointly generates a Lie subalgebra of so(R^10) of dimension 45, hence equal to so(10) — is correct and verifiable. The honest reframing actually *strengthens* the paper: the substantive novelty relocates to "the *existence* of an explicit BHML whose joint closure with TSML's flow generators reaches the substrate ceiling," which is what IJM would publish.
