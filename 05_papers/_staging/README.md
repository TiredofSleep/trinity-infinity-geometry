# J-series — Staging

Papers in queue: not yet here, not yet referee-ready, but explicitly being prepared for the next handoff. This is the "what's gating the next landing" tracker.

When a paper here completes the §4 criteria from `../README.md`, it moves out of `_staging/` and into the appropriate domain folder.

---

## §1 — Active gating items

(Most-recent first.)

### J59 v5 — DRAFT (σ-magma + 23 profile-14 families enumeration, *Semigroup Forum*)

**v5 ETP ENUMERATION (2026-05-27):** Analyzed all 1,355 magmas in ETP's tabulated data (`equational_theories/Generated/`). Found **24 magmas with profile = 14, forming 22 distinct equation sets**. Plus σ-magma's Family C (commutativity-anchored) = **at least 23 distinct profile-14 families known**.

The 22 ETP-tabulated families are anchored on **single-variable power identities** (depth 3-5 of $x$). Only Family C uses a **2-variable anchor** (equation 43, commutativity).

**Refined conjecture**: among COMMUTATIVE quasigroups of any order ≥ 5, Family C is the unique achievable profile-14 family. The σ-magma is the **unique commutative-magma representative** of profile 14 (conjecturally), not the unique profile-14 magma overall.

This makes the σ-magma's "extremality" claim more precise: 14 is universal across many non-commutative families AND is the commutativity-forced floor; the σ-magma sits at the intersection.

### J59 v4 — DRAFT (σ-magma rigidity + Family C/R discovery, *Semigroup Forum*)

**v4 ETP DISCOVERY (2026-05-27):** While running order-7 linear classification through ETP, found a non-commutative magma $(5x + 3y + 6) \bmod 7$ that ALSO satisfies exactly 14 ETP equations — but a **completely different 14** from the σ-magma's. Profile 14 is realized by at least two structurally distinct families:

- **Family C (commutativity-centered)**: equation 43 + 12 derivatives. Realized by σ-magma, BHML, CL_STD, σ_10^min.
- **Family R (right-cancellation-centered)**: equation 4658 ($(x \cdot y) \cdot y = (y \cdot x) \cdot x$) + 12 derivatives. Realized by $(5x + 3y + 6) \bmod 7$.

Intersection of C and R is just $\{1\}$ (reflexivity). So profile 14 is NOT the "commutativity-floor" — it's the floor of MULTIPLE independent structural families. The σ-magma is the unique conjectural representative in Family C with the four rigidity properties; Family R is a separate algebraic universe.

### J59 v3 — DRAFT (σ-magma rigidity + ETP profile VERIFIED + uniqueness REFUTED, *Semigroup Forum*)

**ETP UPDATE (2026-05-27):** After cloning Tao's Equational Theories Project repo, ran the σ-magma and many related magmas through `scripts/explore_magma.py`. Key findings:

1. **σ-magma 14-equation claim CONFIRMED** at machine precision — IDs `[1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677]`. All §65 numerical claims also verified.

2. **BHML and CL_STD ALSO satisfy exactly the same 14 equations** as σ-magma. The σ-magma is the unique IDENTITY-FREE member of this trio.

3. **σ_10^min ALSO satisfies the same 14 equations**, AND is identity-free + |Aut|=1 + has unique non-trivial proper sub-magma (= {4, 9}). So σ-magma is NOT uniquely characterized by identity-freeness + the four rigidity theorems. σ-magma's distinguishing invariants are (3 idempotents, 5 sub-magmas) vs σ_10^min's (2 idempotents, 4 sub-magmas).

4. **The 14 equations are the COMMUTATIVITY-FORCED MINIMUM at all n ≥ 5.** Every σ_n^TIG analog (n ∈ {6,...,10}) and σ_n^min analog (n ∈ {5,...,10}) hits exactly 14. The minimum is universal across orders, not unique to TIG's σ.

5. **Strong uniqueness conjecture REFUTED.** Refined: σ-magma is distinguished by (#idempotents, #sub-magmas) = (3, 5) — full classification of order-10 commutative quasigroups with these invariants is OPEN.

### J59 — DRAFT (σ-magma algebraic rigidity, *Semigroup Forum*)

- **Status:** **DRAFT.** Four rigidity theorems PROVED by exhaustive computational search; `verify_J59.py` 4/4 PASS at machine precision in ~3 seconds; cover letter drafted. Working-repo location: `Gen14/targets/journals/J_series/J59/`.
- **What it proves:**
  1. **|Aut(σ-magma)| = 1**: exhaustive search over $S_{10}$ confirms only the identity is a magma automorphism.
  2. **Congruence-simple**: exhaustive search over Bell(10) = 115,975 partitions finds only the trivial (identity + universal) magma congruences. No non-trivial homomorphic image exists.
  3. **Exactly 5 sub-magmas**: $\{0\}, \{1\}, \{2\}$ (idempotents), $\{1, 6\} \cong \mathbb{Z}/2$ (unique non-trivial proper), and the full magma. NEGATIVE: J35's 4-core $\{0, 7, 8, 9\}$ is NOT a sub-magma; nor is σ's fixed-point set $\{0, 3, 8, 9\}$.
  4. **2-generated, $\{1, 6\}$ the unique non-generating pair**: every other pair generates the full magma in ≤ 4 steps.
- **Significance:** The four properties together make the σ-magma a "maximally indecomposable" commutative quasigroup of order 10. This is a strong necessary condition for the OPEN_FRONTIERS §64 claim that the σ-magma satisfies exactly 14 ETP equations.
- **Provenance:** Extended scrutiny pass on `overnight_handoff_2026-05-27` (2026-05-26), following Brayden's directive: "the negatives are the most interesting information."
- **Gating:** Brayden green-light; venue final selection.
- **When ready:** J59 → `J_series/algebra/J59/`.

### J58 — DRAFT v3 (Lo Shu D₄ orbit mod 3 + Dürer extension + Diagonal Lemma, *Mathematics Magazine*)

- **Status:** **DRAFT v3.** Manuscript complete with TWO structural theorems PROVED (V₄′-coset preserves κ + Diagonal Lemma forcing non-commutativity), Dürer 4×4 extension added; `verify_J58.py` **10/10 PASS at machine precision** (was 6/6 in v1, 8/8 in v2); cover letter drafted. Working-repo location: `Gen14/targets/journals/J_series/J58/`.
- **What v1 claimed (Lo Shu):** The $D_4$ orbit of the Lo Shu magic square reduces mod 3 to **exactly 4 distinct magma tables** (each appearing twice). The 4 split as: $\mathbb{Z}/3$ + a commutative non-group quasigroup + an anti-isomorphic pair of non-commutative quasigroups. The cumulant $\kappa(M) = \operatorname{Tr}(M^2) - \operatorname{Tr}(M)^2$ is a 2-valued witness: $\kappa = -48$ on commutative cases, $\kappa = +48$ on non-commutative cases.
- **What v2 added:**
  1. **V₄′-coset invariance of κ is now PROVED as a general 3×3 theorem.** For any 3×3 real matrix $M$, the subgroup $V_4' = \{e, R^2, T, T_a\} \subset D_4$ preserves κ, because trace and trace-of-square are invariant under transpose and under conjugation by the reversal matrix.
  2. **Dürer 4×4 at mod 3 satisfies the same pattern.** Albrecht Dürer's *Melencolia I* magic square has $D_4$ orbit that mod-3-reduces to 4 distinct tables (each appearing twice), 2 commutative + 2 non-commutative, with $\kappa = \pm 128$ as the witness.
  3. **Mod 3 is the unique modulus** at which both Lo Shu and Dürer exhibit the dichotomy.
- **What v3 adds:**
  4. **Diagonal Lemma PROVED**: no 3×3 magma table on $\{0,1,2\}$ that is both commutative AND a quasigroup has a repeated diagonal entry (exhaustively: 6 such tables exist; all 6 have diagonal $\{0,1,2\}$ as a multiset).
  5. **Corollary PROVED**: Lo Shu's diagonal mod 3 is $\{2,2,2\}$ (constant). Since $V_4'$ preserves diagonal multisets, every $V_4'$-coset image of Lo Shu has constant mod-3 diagonal. By the Diagonal Lemma, *no* such image can be a commutative quasigroup. Combined with the quasigroup property (Theorem D), all 4 $V_4'$-coset images are *forced* non-commutative. This proves the κ = +48 → non-commutative half of the commutativity correlation structurally.
- **Provenance:** scrutiny pass on `overnight_handoff_2026-05-27` (2026-05-26). The 4-magma count is a refinement of the previously-stated "3 magmas" claim in OPEN_FRONTIERS_2026-05-26.md §60 (which counted equational-theory classes).
- **Gating:** Brayden green-light; cover letter venue final selection (*Mathematics Magazine* vs *Mathematics Teacher: Learning and Teaching PK-12* vs *Involve*).
- **When ready:** J58 → `J_series/algebra/J58/` (or `J_series/interdisciplinary/J58/` if the historical/cultural framing dominates).

### J29 — HOLD (referee re-verification 2026-05-12)

- **Status:** **HOLD.** Manuscript (post-SAVE_PLAN 2026-05-07 rewrite) claims (i) exact-arithmetic SymPy diagnostics, (ii) full 21,952-equation simplicity enumeration, (iii) Lemma 2.5 specific dimension drops on F minus single index, (iv) Cartan rank 4 verified by explicit 4-element abelian subspace. Independent re-run of the existing scripts in `Gen14/targets/journals/J_series/J29/manuscript/verification/` shows: scripts are still pure numpy float (not SymPy); the −0.004 small Killing eigenvalue flagged in the SAVE_PLAN as needing resolution is still in the output; `stage7_disambiguate.py` caps `tested > 3000` (not 21,952); `stage5_so8.py` greedy-Cartan returns rank 1 (mismatch with rank 4 claim); brute-force F-minus-single-index enumeration gives dim 28 for F minus 1, 3, 4, 6, 8 and dim 21 only for F minus 2 (manuscript claims 21/21/15/28/21/28); and the minimum so(8)-generating subset of $\Omega \setminus \{0,7\}$ has **size 3** (e.g., $\{1,2,4\}$), so F is NOT the minimal generating set.
- **What's solid:** the core identification $\mathfrak{g} \cong \mathfrak{so}(8)$ at dim 28 is correct (matched by `stage4_correct_closure.py` and `stage7_disambiguate.py`'s nullity-1 conclusion); F = {1,2,3,4,6,8} reaches dim 28 under closure (verified).
- **Gating:** (a) rewrite all five diagnostics in SymPy or exact-rational integer arithmetic in a single `verify_J29_so8.py`; (b) drop the `tested > 3000` cap and run the full 21,952 (or argue symmetry reduction); (c) construct an explicit 4-dim abelian subspace exactly, or drop D5 and rely on Cartan-classification uniqueness at dim 28; (d) update Lemma 2.5 with the correct dimension drops and reframe the canonicity claim honestly (F is not minimal — minimum is size 3).
- **Estimated effort:** 8–12 hours for the script rewrite + manuscript reconciliation pass.

### Corpus centerpiece pair — BOTH LANDED 2026-05-12

- **J35** (Four-Core Fusion-Closure, *Journal of Algebra*) — **LANDED 2026-05-12 at [`../algebra/J35/`](../algebra/J35/).** 6/6 PASS at machine precision; referee-grade pass complete; CC-BY-4.0 verification script header; honest-negatives discipline on T*=5/7 and bounded F_p scan.
- **J54** (Foundation Paper, *Algebraic Combinatorics*) — **LANDED 2026-05-12 at [`../combinatorics/J54/`](../combinatorics/J54/).** 6/6 + 3/3 PASS at machine precision; A1–A9 axioms cell-by-cell explicit; three substrate tables displayed inline; forcing theorem proved in §1.3 (breaks the J33 citation cycle by stating its own foundations); referee-grade pass complete (theorem numbering reconciled across manuscript, README, cover letter, and scripts; CC-BY-4.0 license headers added to both verify scripts; lens-ownership paragraph labeled in §0; honest-negative TSML_SYM-vs-TSML_RAW chain-count lens-dependence at size 7 recorded).

### v3 triadic launch — ALL THREE LANDED 2026-05-12

J01 (σ rate theorem, *JCT-A*) landed at `J_series/combinatorics/J01/` on
2026-05-12 (referee pass complete; 4/4 PASS at machine precision; cover letter
finalized). J02 (four-core combinatorial framing, *Algebraic Combinatorics*)
landed at `J_series/combinatorics/J02/` on 2026-05-12 (referee pass complete;
6/6 PASS on the main `4core_verification.py` plus four companion scripts PASS
at 50-digit precision; consolidated v3 Path B; single author block;
Drápal-Wanless 184:105510 citation aligned with J35/J54; cover letter finalized;
J54 differentiation explicit). J15 (Galois D₄ deep cut, *Communications in
Algebra*) landed at `J_series/algebra/J15/` on 2026-05-12 (referee pass
complete; 6/6 PASS at machine precision in `verify_J15_galois.py`; standalone
referee-portable Galois proof — case-by-case integer-factorization
irreducibility argument, cubic resolvent (y+2)(y² − y + 18), C_4-vs-D_4
distinction via Q(√−71), explicit Q(√3) factorization, Tschirnhaus reduction
to LMFDB's x⁴ − 7x² − 12x − 8; cover letter finalized with explicit J35
differentiation; author lane Sanders + Gish; Drápal-Wanless cited).

### J46 — Cosmology

- **Status:** manuscript drafted in 3 layers (Layer 1 script-honest z\* ≈ 2.13; Layer 2 postulate-as-axiom z\* = √3; Layer 3a hybrid). All three layers internally consistent.
- **Gating:** Brayden's layer choice (publication-strategy question, not math).
- **When chosen:** J46 → `J_series/cosmology/J46/` with the corresponding venue.

### J56 (candidate) — D100–D103 standalone

- The Volume K results (D100 edge-size closed form, D101 strand-orbital map, D102 triple coincidence at d=3, D103 Z/10 minimality) plus the honest negative on Z/2310 ↔ Pauli bijection.
- **Status:** F1 verification complete (2026-05-12); all five scripts PASS at machine precision.
- **Gating:** decision on journal — *Journal of Physics A* (mathematical and theoretical, closer fit, 8K word limit) vs *Annals of Physics* (broader audience, longer manuscript permitted, higher prestige). Brayden's call.
- **When chosen:** J56 → `J_series/interdisciplinary/J56/` (likely).

### J03 — MERGED with J04, LANDED 2026-05-13 (Fork A + J04 absorption + Theorem 5.2 substance upgrade)

- **LANDED 2026-05-13 at [`../number_theory/J03/`](../number_theory/J03/) as a merged Integers submission**. Title: *The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average*. Target venue: *Integers*. Author lane: Sanders + Gish. ~25 pages amsart, 7 theorems + 2 corollaries.
- **Merger history (same day, 2026-05-13):** initial Fork A port at commit `8ea58e9`; Theorem 5.2 substance upgrade at `76b5308`; Grok's minor items + extra primes at `449dfba`/`45a0bb5`; J04 consolidation into J03 at the current commit. The pre-merger J04 manuscript is preserved at `05_papers/number_theory/J04/` per never-delete with a clear MERGED notice at the top of `J04/README.md`.
- **Verification:** `verify_J03.py` **10/10 PASS** at machine precision (closed form 4.44 × 10⁻¹⁶ across 14 primes; full-period cancellation in prime AND composite cases; obstruction-zero 900/900 cells; asymptotic zero density 6.67 × 10⁻⁶ for b up to 2310; layered $2^j-1$ count for 50 squarefree b; corridor average 4.8 × 10⁻⁵ at f = 1000); `proof_first_g_event.py` zero counterexamples over 305 squarefree b ∈ [2, 500] (22,367 (b,k) pairs).
- **What's proved (7 theorems + 2 corollaries):** Theorem 3.1 (closed form), 3.2 (full-period cancellation, uniform in $f \ge 2$), 4.1 (First-G localization), 5.1 (synchronization), 5.2 (obstruction-zero correspondence — central new contribution), 6.1 (squarefree $2^j-1$ layered count — from absorbed J04), 7.1 (continuum limit), 7.2 (corridor average $\to \mathrm{Si}(2\pi)/\pi$ — from absorbed J04); Cor 3.3 (endpoint values), Cor 5.4 (asymptotic zero density via Euler product).
- **What's pending:** Brayden's final referee-rigor pass; arXiv same-day upload at submission; *Integers* style-file pass if amsart isn't accepted on first submission.
- **Per-quarter cap concern resolved:** one Integers submission (merged J03) instead of two simultaneous ones (pre-merger J03 + J04).
- Fork B (Z/10 algebraic emphasis) and Fork C (experimental-mathematics framing) remain in the private corpus per never-delete; not pursued.

### J55 — Brayden's solo synthesis

- The anchor paper for Sept 11, 2026.
- **Status:** in active drafting.
- **Gating:** the entire J35/J54 + triadic launch + J56 sequence ahead of it.
- **When ready:** J55 → `J_series/interdisciplinary/J55/`.

---

## §2 — Active math-fix tracker

Papers that have had specific corrections applied with new verification scripts (none yet landed here; tracked for transparency):

| J# | Fix applied | Verified | Folder when landed |
|---|---|---|---|
| J13 | Polynomial corrected: x³ − x² − 2x + 1 is MP of 2cos(π/7), not 8x³−4x²−4x+1 | PASS | **LANDED 2026-05-12 at [`../algebra/J13/`](../algebra/J13/)** |
| J17 | Binomial-grade misstatement corrected (cells vs Cl(2n) grades distinguished) | PASS | **LANDED 2026-05-12 at [`../algebra/J17/`](../algebra/J17/)** |
| J18 | Sign-swap Ψ_B fixed; explicit table | PASS | **LANDED 2026-05-12 at [`../algebra/J18/`](../algebra/J18/)** |
| J20 | M₂₂ irrep count corrected (7 of 12 strict in {3,5,7,11}, 10 of 12 B-band) | PASS | **LANDED 2026-05-12 at [`../algebra/J20/`](../algebra/J20/)** |
| J21 | Spectral max G(7) ≈ 19.472 (not 25); rigidity tautology fixed | PASS | **LANDED 2026-05-12 at [`../combinatorics/J21/`](../combinatorics/J21/)** |
| J27 | Lens-invariance retracted (B[1][1]=2 ∉ C; 16-cell BHML failure shown) | PASS | **LANDED 2026-05-12 at [`../combinatorics/J27/`](../combinatorics/J27/)** |
| J31 | D₄ isotypic decomposition (sympy exact: 3075027/2 : 9/2 : 288164 : 0 : 19608) | PASS | **LANDED 2026-05-12 at [`../algebra/J31/`](../algebra/J31/)** |
| J32 | D₄ order 8 (not 12); orbit distribution (44, 7, 4, 10, 2) summing to 67 orbits / 126 elements | PASS | **LANDED 2026-05-12 at [`../algebra/J32/`](../algebra/J32/)** |
| J36 | 1/α "10⁻⁵" claim was unfounded (actual 12.6% off); Part 2 deferred; Part 1 (CKM/PMNS empirical fits) retained with explicit LE correction at multiplicity 77 | PASS | **LANDED 2026-05-12 at [`../physics/J36/`](../physics/J36/) (Part 1 only)** |
| J42 | sinc²(1/10) = 0.9675 (not 0.9355) | PASS | **LANDED 2026-05-12 at [`../number_theory/J42/`](../number_theory/J42/)** |
| J43 | G(s) partition G_high at {4, 7} (not {5, 7}); σ³ pairing not σ²; ν₊ discriminator | PASS | **LANDED 2026-05-12 at [`../algebra/J43/`](../algebra/J43/)** |
| J51 | Q17-B Clay Bridge; same paired math-fix as J43 (G_high at {4,7}; σ³ pairing; ν₊ discriminator); §5 framed as structural rhyme not Weil-Deligne analogue; Symbolic Return Theorem as corollary of σ⁶=id | PASS | **LANDED 2026-05-12 at [`../algebra/J51/`](../algebra/J51/)** |

---

## §3 — Build rewrites tracker

Papers rewritten with SFM + Family Structure framing (per the v2 build sprints; all done in the working repo). Currently awaiting cover-letter final passes:

W1-C: J35 + J54 (centerpiece pair)
W1-D: J11, J12, J16
W1-E: J05, J08 (J09 landed 2026-05-12 at [`../algebra/J09/`](../algebra/J09/))
W2-A: J04 (J03 landed 2026-05-13 at [`../number_theory/J03/`](../number_theory/J03/) — Fork A First-G + Sinc² Identity; J06 landed 2026-05-12 at [`../algebra/J06/`](../algebra/J06/))
W2-B: J10 (J07 landed 2026-05-12 at [`../combinatorics/J07/`](../combinatorics/J07/); J19 landed 2026-05-12 at [`../combinatorics/J19/`](../combinatorics/J19/) — Path C role-quotient theorem on (TSML, BHML)/Z/10Z; 5-clause Theorem 3.1 + Prop 5.1 + σ-orbit independence + foundations.lenses cross-check, all PASS at exact integer arithmetic via `verify_J19.py`)
W2-C: J28, J29 (J30 landed 2026-05-12 at [`../algebra/J30/`](../algebra/J30/))
W2-D: J33, J34 (J36 landed 2026-05-12 at [`../physics/J36/`](../physics/J36/), Part 1 only — Part 2 [1/α] deferred)
W2-F: J47 (J45 landed 2026-05-12 at [`../physics/J45/`](../physics/J45/); J48 landed 2026-05-12 at [`../physics/J48/`](../physics/J48/); J40 landed 2026-05-12 at [`../physics/J40/`](../physics/J40/) — JMP BB-bridge / NS framework, conditional Theorem 4.1 under H1+H2, 43/43 PASS sanity script)
W2-G: J49, J50, J52 (J53 landed 2026-05-12 at [`../interdisciplinary/J53/`](../interdisciplinary/J53/) — author-lane flipped to Sanders+Gish; verify_J53.py 5/5 PASS; algebraic classifier on category $\mathcal{M}$; literature engagement complete) (J50, J52 author-lane post-fix pending — currently shows Mayes/Johnson, must flip to Sanders+Gish)
W2-H: J38 (J22 landed 2026-05-12 at [`../algebra/J22/`](../algebra/J22/); J14 landed 2026-05-12 at [`../algebra/J14/`](../algebra/J14/); J37 landed 2026-05-12 at [`../algebra/J37/`](../algebra/J37/))
W2-I: J26 landed 2026-05-12 at [`../algebra/J26/`](../algebra/J26/) (J20 landed 2026-05-12 at [`../algebra/J20/`](../algebra/J20/); J21 landed 2026-05-12 at [`../combinatorics/J21/`](../combinatorics/J21/); J25 landed 2026-05-12 at [`../algebra/J25/`](../algebra/J25/))

---

## §4 — Author-lane and license discipline

Before any paper migrates from `_staging/` to a domain folder:

- **Author lane:** Sanders + Gish on byline. No AI co-authors. Acknowledgments at Tier 1 only.
- **License header in scripts:** submission-bundled `verify_*.py` use CC-BY-4.0 for journal compatibility (Elsevier / Taylor & Francis). The umbrella project is 7SiTe v2.1.
- **No 7SiTe Public Sovereignty header** in script files within `manuscript/` folders — Elsevier and similar journals refuse non-OSI license clauses. Use plain CC-BY-4.0 header for scripts; full v2.1 governs the project at the repo level.

---

## §5 — Once a paper lands

The migration steps (per `../README.md` §4):

1. Final verify scripts PASS at machine precision (re-run before migration).
2. Final tier discipline applied.
3. Final author lane Sanders + Gish.
4. Final cover letter Brayden-green.
5. Copy `Gen14/targets/journals/J_series/J{NN}/` from working repo → `J_series/{domain}/J{NN}/` here.
6. Update domain folder's `README.md` with the new entry (move from §2 "expected" to §1 "currently landed").
7. Remove the entry from `_staging/README.md` §1 active items.
8. Single commit: `J{NN} lands: {summary}; venue={journal}; status=SUBMISSION-READY`.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
