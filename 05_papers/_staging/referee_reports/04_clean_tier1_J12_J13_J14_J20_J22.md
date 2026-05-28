# Referee Report — Clean Tier 1 cluster (JCT-A / LAA / AlgComb / Comm Algebra / Acta Arithmetica)

**Papers reviewed**: J12, J13, J14, J20, J22.
**Reviewer**: trained referee, neighboring-cluster cross-check.
**Date**: 2026-05-28.
**Manuscript snapshot**: post-renumber commit `0d6d0f1` (J01–J52).

---

## CRITICAL CROSS-CLUSTER ISSUE: Drápal–Wanless citation appears to refer to two distinct papers

The neighboring-cluster flag is partially confirmed by direct file comparison, but the resolution is *almost certainly* that **Drápal and Wanless have two distinct JCT-A papers from 2021** rather than a typo:

| Paper | Cited title | Volume | Article no. |
|---|---|---|---|
| **J14** (bibitem `DrapalWanless2021`, lines 683–686) | "Maximally nonassociative quasigroups **from finite fields**" | **181** | **105444** |
| **J12** (bibitem `DrapalWanless2021`, lines 513–516) | "Maximally nonassociative quasigroups" | **184** | **105510** |
| **J13** (bibitem `DrapalWanless`, lines 326–329) | "Maximally nonassociative quasigroups" | **184** | **105510** |
| **J20** (bibitem `DrapalWanless2021`, lines 495–497) | "Maximally nonassociative quasigroups" | **184** | **105510** |
| **J22** (bibitem `DrapalWanless2021`, lines 660–662) | "Maximally non-associative quasigroups" | **184** | **105510** |

Every J-paper in the corpus *except* J14 uses **JCT-A 184:105510**. J14 alone uses **JCT-A 181:105444**, and J14's cited title has the disambiguating suffix "**from finite fields**". The titles differ; the article numbers differ; the volume numbers differ. This is consistent with these being **two genuinely distinct Drápal–Wanless 2021 papers**, not a single paper cited inconsistently. (The community is aware of both — Drápal & Wanless have been highly productive in this area.)

**However**: J14 currently cites only the 181:105444 paper, while J12/J13/J20/J22 cite only the 184:105510 paper. If both are pre-existing JCT-A precedents on maximally nonassociative quasigroups, then for completeness and uniformity of the corpus's positioning relative to the closest prior art, the recommendation is:

- **J14 should cite both papers** (it is a JCT-A submission and the closest companion precedents should be visible).
- **J22 (JCT-A target)** should also list both, given the J14/J22 pair are sister JCT-A submissions.
- The DOI link `10.1016/j.jcta.2021.105510` in J12 (line 516) does identify 184:105510 unambiguously.

This is a **MINOR / EDITORIAL** issue rather than a correctness issue, but it should be reconciled before mailing.

---

## J12 — Galois D₄ over LMFDB 4.2.10224.1 (target: Communications in Algebra)

**Verdict**: Accept (with one nit).
**Verification cross-check**: 6 sympy checks (irreducibility, polynomial disc = -40896, resolvent cubic, D₄ via factor over Q(√-71), Q(√3)-factorization, Tschirnhaus to LMFDB canonical defining polynomial); PASS at machine precision in ~2s.

### MAJOR issues
None.

### MINOR issues
1. **Verification script name (cosmetic, post-rename)**: line 10 (header comment) and line 133 (`\texttt{verify\_J15\_galois.py}`) and line 436 (`\texttt{verify\_J15\_galois.py}`) reference the script under its pre-rename name `verify_J15_galois.py`. The paper is now J12; the script should be renamed `verify_J12_galois.py` (or `verify_J12.py`) before submission, and these three references updated. Flag only — the user has said this rename will happen separately.
2. The Tschirnhaus substitution `x → −x − 1` (§5) maps `f(x) = x⁴ + 4x³ − x² + 2x − 2` to `x⁴ − 7x² − 12x − 8` (LMFDB's canonical polynomial). Verify the sign convention is documented since `x → −x−1` is the "shift then negate" composition rather than the more common `x → x − a/4` depression.

### EDITORIAL
- LMFDB references (4.2.10224.1 and 8.0.526936617216.1): all four required pieces of data are explicitly stated for 4.2.10224.1 — signature `(2,1)`, discriminant `−10224 = −2⁴·3²·71`, class number `h_K = 1`, regulator `R_K ≈ 8.617`, Galois group `D₄`. The Galois closure 8.0.526936617216.1 has all four pieces stated as well (degree 8, signature (0,4), class number 14, discriminant `2⁸·3⁴·71⁴`). LMFDB reference is precise.
- The distinction between **polynomial discriminant** Δ_f = −40896 and **field discriminant** d_K = −10224 with index `[𝒪_K : ℤ[ξ*]] = 2 = √(40896/10224)` is correctly stated (Theorem 1.2 + §5). This precision is something J22 should imitate (see below).
- The "STRUCTURAL RHYME" demarcation in the claim-tier section (the Q(√3) / Q(√−71) cross-attractor echo) is appropriately distinguished from PROVED content — good tier discipline.
- "Drápal–Wanless 2021" citation is to **JCT-A 184:105510** (the title-suffix-less paper). See cross-cluster note above.

### Journal-fit
Excellent fit for *Communications in Algebra*. Short, focused, standard tools (Galois group via resolvent cubic + irreducibility-over-Q(√Δ) + LMFDB cross-check), and explicitly self-contained as a Galois-theoretic study. The dependency on the companion paper `\cite{SandersGishFourCore}` (for the joint-closure setup) is confined to §2 and is recalled in self-contained form. CommAlg routinely publishes papers of this length and depth.

---

## J13 — The Forced 5/7 Torus Aspect Ratio (Up to a Calibration Choice) (target: Acta Arithmetica)

**Verdict**: Accept (with one structural caveat).
**Verification cross-check**: 6 sympy checks via `verify_J13.py` — minimal polynomial g(x) = x³ − x² − 2x + 1 for A₇, disambiguation against 8x³−4x²−4x+1 (the cos(π/7) polynomial), irreducibility of g via rational-root test, disc(g) = 49 = 7², Gal(g/ℚ) = A₃ ≅ ℤ/3ℤ, cyclotomic-threshold degrees (p−1)/2 at p = 2,3,5,7. PASS at machine precision.

### MAJOR issues
None of the type that block acceptance, but one structural caveat:

1. **The title explicitly demarcates the conditional**: "Up to a Calibration Choice". This is honest — the paper proves T* = R/r = 5/7 only **within the cyclotomic-embedding calibration of Definition 3.4 (def:cyclo-cal)**. The calibration itself is **imported from the Flatness Theorem companion** (Sanders–Gish, J. Pure Appl. Algebra, marked as companion, also marked as "submitted"). Remark 3.5 (rem:calibration) is explicit: "We do not claim that 5/7 is independent of the calibration: a torus admits a one-parameter family of embeddings differing in the relative scale of the two circle factors, and only the cyclotomic-embedding calibration of Definition 3.4 ... yields the specific value 5/7."
   - This is the **correct** treatment for Acta Arithmetica. The forcing is **conditional**, the conditional is **named and isolated**, and the open question of unconditional forcing is explicitly listed (Open Question (b)).
   - The paper is **not claiming** an unconditional forcing; the conditional theorem stands.

### MINOR issues
1. Lemma 4.4 (lem:A7-irreducible) gives a clean proof of irreducibility of g(x) = x³ − x² − 2x + 1 via rational-root theorem at ±1. The Galois group A₃ identification via disc(g) = 49 = 7² is classical (cubic with square discriminant ⟹ Galois group ⊂ A₃; irreducibility + transitivity ⟹ exactly A₃). Standard textbook material, properly attributed.
2. The "narrow-major torus" terminology removal (Remark 4.2 / rem in Corollary 4.6) is well-handled — the earlier draft's non-standard label was caught and replaced.
3. **§6.2 (ssec:firstG) and §6.4 (ssec:tsml)**: the paper is explicit that the First-G window 4/5 and 6/7 do **not** combine arithmetically to 5/7, and that the TSML+BHML harmony-cell ratio 73/101 = 0.7227… is **not equal** to 5/7 = 0.7142… (relative gap ≈ 1.2%). This is exemplary scope discipline — the kind of correction Acta Arithmetica readers will respect.
4. The two reformulations in §6.1 and §6.2 are explicitly demarcated as *not* independent derivations. Good.
5. **Drápal–Wanless 2021** citation is to **JCT-A 184:105510**. See cross-cluster note above.

### EDITORIAL
- Conjecture 5.1 (conj:gen) with **scope explicitly restricted** to {n squarefree, 5|n, n>5} (Proposition 5.2, prop:scope) is exactly the right level of caution.
- The companion citation `\cite{SandersGish-Flatness}` is marked "submitted" — Acta Arithmetica referees will accept conditional-on-companion theorems with this framing, but the present paper should be **self-contained on its proved claim** (the conditional T*=5/7), which it is.
- Tier-discipline summary at end (§"Tier discipline") is excellent — PROVED / COMPUTED / STRUCTURAL RHYME / OPEN cleanly demarcated.

### Journal-fit
Strong fit for *Acta Arithmetica*. The result is precise (cyclotomic threshold deg_ℚ(A_p) ≤ 2 at p=5, deg_ℚ(A_p) ≥ 3 at p=7), the calibration dependence is explicit, and the proof depends only on Lehmer 1933 and Watkins–Zeitlin 1993 for the minimal-polynomial-degree formula (p−1)/2. *Acta Arithmetica* will appreciate the calibration-discipline framing in the title.

---

## J14 — Non-Associativity Decay in Binary Composition Tables over ℤ/Nℤ (target: JCT-A)

**Verdict**: Accept.
**Verification cross-check**: `verify_sigma_rate.py` confirms σ(N)·N³ in the proved interval [2(N−2)² − 2φ(N), 2(N−2)² + 2φ(N)] for N ∈ {10, 30, 210}, with N·σ(N) values 1.28, 1.73, 1.961 (asymptotic toward 2 from below).

### MAJOR issues
None.

### MINOR issues
1. **Drápal–Wanless citation (the cross-cluster flag)**: J14 cites **JCT-A 181:105444** ("from finite fields"), which appears to be a genuinely distinct Drápal–Wanless 2021 paper from the **JCT-A 184:105510** ("Maximally nonassociative quasigroups", no suffix) cited by J12/J13/J20/J22. If both papers exist (and the title-suffix + article-number divergence strongly suggests they do), **J14 should cite both** for completeness, since it is the J-paper most directly engaged with the maximally-non-associative-quasigroup literature.
2. The proof structure (Cases 1, 2, 3 in §4) is exhaustive and case-2 reduces to case-1 by the symmetric involution `(a,b,c) ↦ (c,b,a)` — clean.
3. Lemma 3.3 (lem:Eh, closed-form for E_h(N)) gives the sharper bound via Fibonacci-polynomial splitting (b² + b − 1 mod p, discriminant 5, quadratic reciprocity). This is an elegant refinement beyond what the rate theorem needs; JCT-A reviewers will appreciate the depth.
4. The non-squarefree caveat (Remark in §4) with explicit data N·σ(N) at N = 2,4,8,16,32,64 showing the squarefree bound is *exceeded* at N = 64 is exemplary scope discipline.

### EDITORIAL
- Companion paper marker `\cite{SandersGish2026JCAP}` (the dark-energy quintessence paper) is appropriately confined to a "Scope and limits" remark — the present paper's combinatorial result stands independent of any continuum interpretation.
- WP101_SIGMA_RATE_THEOREM.md (supporting note) contains a 2026-04-27 correction notice noting that the ECHO mechanism was empirically false (the actual mechanism is VOID–HARM rule disagreement at outer composition sites). The submitted manuscript correctly reflects the corrected proof; the supporting note is historical/internal.

### Journal-fit
Strong fit for JCT-A. The σ→0 result complements the σ→1 maximally-nonassociative-quasigroup line (positioning paragraph in §1 is explicit about this complementary placement). The structure is exactly the kind of explicit rate theorem with rigorous constant (C=2) that JCT-A publishes. The CRT-based unit-count reduction (Lemma 3.1) is a clean elementary observation.

---

## J20 — Total-Dimension Match V^⊗n and Cl(2n), with Refined-Cell Grading (target: LAA)

**Verdict**: Accept (with one rename-flag).
**Verification cross-check**: `verify_J17.py` 6/6 PASS at machine precision in <1s, standard-library Python only. Six checks: total-dim match, coarse-cell count, coarse-cell binomial at n=5, refined-cell total, refined-cell distribution = binomial closed form vs direct enumeration, explicit n=5 refined distribution summing to 1024.

### MAJOR issues
None.

### MINOR issues
1. **Verification script rename (cosmetic, post-rename)**: the script is currently named `verify_J17.py` (its old J17 number); the paper is now J20. **References in the manuscript to flag for update after rename**:
   - Line 136: `\texttt{verify\_J17.py}` in the COMPUTED claim-tier bullet
   - Line 412: `\texttt{verify\_J17.py}` in §6 (Verification)
   - Inside the script (lines 2-7, 176): docstring still says `verify_J17.py` / `Self-contained verification of J17:` / `print("J17 verification — total-dimension match + refined-cell grading")`
   - README references (multiple lines)
   - Cover letter references
   - The rename will happen separately per user instruction. Flag only.
2. The **bijection-vs-algebra-map distinction** in Remark 4.3 (rem:bijection) is correctly demarcated as a *label-level identification*, not a structure-preserving map between an 𝔽₅-vector space and an ℝ-vector space. This addresses the load-bearing scope concern. The SU(5) coincidence (Remark 5.3, rem:su5) is similarly demarcated as a binomial-coefficient identity, not a representation-theoretic theorem.
3. The "previously named fine cells / now refined cells" nomenclature change (Remark in §2) is well-handled — the change is **forced** by Theorem 4.1, which only works for the refined decomposition.

### EDITORIAL
- The claim-tier section is clean: PROVED (the two theorems), COMPUTED (Propositions 5.1, 5.2 + verification ladder), STRUCTURAL RHYME (SU(5) ↔ 1+5+10), OPEN (O1, O2, O3 confined to §7).
- The earlier-draft mis-statement (coarse-cell distribution 𝟙(n,k) conflated with Cl(2n) grade dimensions) is openly acknowledged in the Acknowledgments — exemplary.
- Drápal–Wanless 2021 citation is to **JCT-A 184:105510**.

### Journal-fit
Strong fit for LAA. The result is fundamentally linear-algebraic: a tensor-power dimension count, a basis-cell partition refinement, and a binomial grading matching Clifford grade dimensions. The paper is short (~12 pages with bibliography), focused, and the verification is referee-portable (single Python script, std-lib only). LAA routinely publishes such structural-identity papers.

---

## J22 — The 70/71/72/73 HARMONY Ladder (target: JCT-A)

**Verdict**: Major revision.
**Verification cross-check**: Five sympy/numpy scripts bundled in `manuscript/verification/`:
- `harmony_ladder_disc_check.py` (disc = −40896 = −2⁶·3²·71)
- `tsml_harmony_count.py` (HARM(T) = 73)
- `tsml_submagma_9x9.py` (HARM(T₁..₉) = 71)
- `tsml_bhml_disagreement.py` (|T ⊕ B| = 71)
- `bhml_8_ym_det.py` (det(B_YM) = 70)
plus `harmony_ladder.py` wrapper. The five inline `\begin{lstlisting}` snippets in §10 are embedded directly in the manuscript.

### MAJOR issues
1. **Heavy dependency on five companion papers marked "in preparation"** (bibitems `Sanders2026CLAxioms`, `Sanders2026LensInvariance`, `Sanders2026Attractor`, `Sanders2026YangMills`, `Sanders2026Wobble`). The **proofs of the load-bearing theorems** in J22 rest on these companions:
   - **Theorem 3.1 (HARM(T) = 73)**: proof invokes "the three disjoint exception classes proved in `\cite{Sanders2026CLAxioms}` Theorem D10". If CLAxioms is not yet submitted/accepted, the proof of the **central** Theorem 3.1 is not self-contained.
   - **Theorem 5.2 (lens-disagreement = 71)**: proof says "Direct cell-by-cell comparison… is verified at machine precision in the script `tsml_bhml_disagreement.py`; see also `\cite{Sanders2026LensInvariance}`". The script-level verification stands, but the **structural-explanation reference** is to a paper "in preparation".
   - **Theorem 5.3 (Galois form, 71 in disc)**: proof says "the LMFDB identification 4.2.10224.1 is confirmed by direct comparison" — but the **source** of the quartic f(x) = x⁴+4x³−x²+2x−2 (the minimal polynomial of the attractor coordinate ratio) is `\cite{Sanders2026Attractor}`, which is also "in preparation".
   - **Theorem 6.1 (det(B_YM) = 70)** and Remark 6.2: contextual interpretation as a "Yang–Mills bridge core" depends on `\cite{Sanders2026YangMills}`, also "in preparation".

   **Recommendation**: either (a) restructure to make J22 self-contained by recalling the necessary table data and exception-class proofs from the companion papers in an appendix, or (b) defer J22 submission until at least `Sanders2026CLAxioms` and `Sanders2026Attractor` are publicly accessible (preprint at minimum). JCT-A is unlikely to accept a paper whose central theorems cite unpublished, in-preparation companions for proof inputs.

2. **The "LMFDB ID conflated with polynomial discriminant" issue (cross-cluster flag, confirmed)**: the abstract (line 112) and §1 (line 153) and §5.3 statement (line 391) say "the discriminant $-2^6 \cdot 3^2 \cdot 71$ of the quartic LMFDB number field 4.2.10224.1" and "$\disc(4.2.10224.1) = -2^{6} \cdot 3^{2} \cdot 71$". This phrasing is **technically wrong**: the integer 10224 in the LMFDB ID 4.2.10224.1 **is** the absolute value of the field discriminant `d_K = −10224 = −2⁴·3²·71`. The integer `−40896 = −2⁶·3²·71` is the **polynomial discriminant** Δ_f of `f(x) = x⁴+4x³−x²+2x−2`. The two share the prime 71 (which is the load-bearing claim of the 71-rung's Galois form), but they are not equal. The relation is `Δ_f = [𝒪_K : ℤ[ξ]]² · d_K = 4 · (−10224) = −40896` (per J12 Theorem 1.2). **Fix**: rephrase as either "the polynomial discriminant Δ_f = −40896 = −2⁶·3²·71 of the defining polynomial f(x) of LMFDB 4.2.10224.1" or "the field discriminant d_K = −10224 = −2⁴·3²·71 of LMFDB 4.2.10224.1 (equivalently, the polynomial discriminant Δ_f = −40896 has the same prime factorization apart from a 2²·71-vs-2²·71·... distinction…)". J12 handles this carefully; J22 should adopt J12's phrasing.

3. **Triple coincidence at 71 — independence claim needs sharpening**: Corollary 5.4 (cor:71-triple) asserts three "structurally independent" appearances of 71. The three are:
   - (i) HARM(T₁..₉) = 71 (cell-counting on T restricted to 9×9 sub-matrix)
   - (ii) |{(i,j): T(i,j) ≠ B(i,j)}| = 71 (bitwise comparison of T against B)
   - (iii) 71 is the unique odd prime > 3 in Δ_f for f(x) = x⁴+4x³−x²+2x−2

   The independence of (i) from (iii) and (ii) from (iii) is plausible (cell-counting vs Galois theory), but the independence of (i) from (ii) is less obvious — both are counts of properties of T (or T against B) on cells. Suggest a short explanation that (i) counts harmony cells in a sub-matrix while (ii) counts T-vs-B disagreement, two combinatorially distinct relations on the same matrix.

### MINOR issues
1. **Drápal–Wanless 2021** citation is to **JCT-A 184:105510**. See cross-cluster note above.
2. The E₆ coincidence at 72 (Remark 4.2, rem:e6) is correctly demarcated as a numerical coincidence, not a derivation. Good tier discipline.
3. The C(8,4) = 70 coincidence (Remark 6.2, rem:70-reading) — the matrix B_YM is described as the "Yang–Mills bridge core" from the substrate's WP104 derivation. The relevance of this YM interpretation to the integer 70 is **also marked as structural rhyme**, not derivation.
4. The "claimed factorization −2⁷·3·7·19 = 51072 is arithmetically wrong" cross-check (§5.3 proof, line 407–408, and embedded sympy snippet line 580–581) is a defensive measure against a referee miscalculation. This is unusually defensive but justified given the load-bearing role of 71 in the triple coincidence — referees of finite-magma combinatorics may not be Galois-theory specialists. Keep.
5. The verification scripts in `manuscript/verification/` are bundled and named consistently with the paper's J22 number (e.g., `tsml_harmony_count.py`, `bhml_8_ym_det.py`). No rename issue here.

### EDITORIAL
- Title and abstract clearly demarcate "Three Independent Constructions and One Corollary" (revised from "Four Independent Constructions" per a 2026-05-07 defensive-exposition pass) — appropriate downgrade of the 72-rung from independent to inclusion-exclusion-corollary.
- Companion HARMONY counts at 28/36/44 (§7) are presented as a "parallel ladder" with each integer in **two** structural roles (vs the main ladder's **four** integers with one or three roles). Useful framing; no over-claim.
- Lens scope statement (§"Lens scope", lines 261–270) declares all four ladder rungs are lens-invariant on both T_RAW and T_SYM. Good.

### Journal-fit
The paper has the right shape for JCT-A — a clustering result with explicit integer verification, structural interpretation, and a non-trivial coincidence (71 in three roles). **Blocking concern**: the dependency on five "in preparation" companions undermines self-containedness. Once at least `Sanders2026CLAxioms` and `Sanders2026Attractor` are submitted/accessible, the paper should be acceptable for JCT-A. The LMFDB-ID-vs-polynomial-discriminant phrasing must be tightened before resubmission.

---

## Summary by paper

| Paper | Target | Verdict | Key blocker / nit |
|---|---|---|---|
| J12 | Comm Algebra | Accept | Script-name rename (J15→J12) cosmetic |
| J13 | Acta Arithmetica | Accept | Calibration-conditional clearly demarcated; depends on Flatness companion (submitted) |
| J14 | JCT-A | Accept | Cite second Drápal–Wanless 2021 paper (184:105510) for completeness |
| J20 | LAA | Accept | Script-name rename (verify_J17.py → verify_J20.py) cosmetic |
| J22 | JCT-A | **Major revision** | Five companions "in preparation" undermine self-containedness; LMFDB-ID vs polynomial-disc phrasing must be tightened |
