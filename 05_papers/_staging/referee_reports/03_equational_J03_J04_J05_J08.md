# Referee Report — Cluster 03: Computational/Equational Algebra (J03, J04, J05, J08)

**Reviewer venue cluster:** *Journal of Symbolic Computation* (J03), *Semigroup Forum* (J04), *Experimental Mathematics* (J05), *Algebra Universalis* (J08)
**Date:** 2026-05-27
**Source commit:** post-renumbering (0d6d0f1, J01–J52 scheme)

---

## J03 — Type Specimens in the ETP-Restricted Variety Lattice (JSC)

**Verdict:** **Major revision** — central Fossil-Variety Theorem 5 is publishable but needs proof-tightening; framing as "first proved instance" is overclaimed; the toolkit is JSC-appropriate.

**Verification cross-check:** `verify_J61.py` runs 5 checks (closure(43) size = 14, σ-magma realizes Family C, 8-commutative intersection = Family C, no tabulated profile-14 magma matches a size-14 closure, random const-diag → C1). Checks 1–4 are sound. Check 5 is probabilistic ("≥1 hit in 30 trials"), not a verification of C1 universality. Runtime claim "~15s" reasonable given ETP overhead.

### MAJOR issues

1. **Theorem 5, Step 4 lower bound is incomplete.** The claim "profile ≥ 261 for *any* finite magma satisfying eq 4295 at any order" rests on order-3 enumeration plus orders 4–6 spot-checks. The manuscript itself flags this (Remark on the lower bound 261) but the theorem statement still says "every finite magma … has equational theory of size at least 261." The honest formulation: *theorem at orders 3–6 (Tier A), conjecture at orders ≥ 7*. Without an order-uniform analytic bound on the right-projection-through-f profile, Theorem 5 should be downgraded to "Tier A at finite orders 3–6; Tier C at higher orders" — or upgraded by providing the missing structural argument.

2. **"First explicitly proved instance" overclaim.** Section 7 (Significance) and the abstract both assert C5/eq 4295 is "the first explicitly proved instance of an ETP equation with no finite type specimen." This is a substantial novelty claim with respect to the rapidly evolving ETP community (Tao et al. 2024–2025, the Schröder revival arXiv 2603.29909, the latent-space arXiv 2601.20759). A literature scan citing what the ETP project itself has and has not proved about specific equation classes is required.

3. **Table in §6.1 still lists C8 as "FOSSIL VARIETY" but the §6.3 retraction text demotes all C3–C8 to Tier B.** Internal inconsistency. The C8 entry should read "OPEN (Tier B empirical, order-3 enumeration)" to match §6.3.

4. **Conjecture 1 claim "verified at orders 3 AND 5" is shaky for order 3.** The §4.7 paragraph in J05 (which J03 cites approvingly) says all 729 order-3 commutative magmas were enumerated and 120 of them share IDENTICAL Family C equation set at profile 14. But verify_J61.py does not include this enumeration; the count "120 of 729 with profile 14" is asserted, not script-verified. A `verify_order3_enumeration.py` is needed.

### MINOR issues

- §3.2 Step 2 code snippet says `closure(anchor_eq) | {1} == profile`; this assumes the equation-1 element is always present in closures, which is conventionally correct but should be stated as a lemma.
- Worked Example 1 (Lo Shu D₄ orbit mod 3): profile values $T_1 = 179, T_4 = 313$ are cited from J29 without a within-document verification. Add a footnote.
- §5 (Worked example 2): the conjecture "σ-magma is unique identity-free rigid commutative type specimen at order 10" is restated. J04 §6 already refutes the strong form via σ₁₀^min. This contradiction should be resolved (either retire the J03 phrasing or qualify it).
- The 23-family enumeration is asserted multiple times. Provide the list-as-data appendix.

### EDITORIAL

- Section numbering: §6 has TWO §6.2-style subsections labeled inconsistently. The retraction announcement should appear before the data table in §6, not after.
- Drápal-Wanless (2021) citation: present and correctly attributed at p.21 (Comparison table, row 4) and §References. CORRECT.
- Tier markers (PROVED / COMPUTED / STRUCTURAL / OPEN / Tier-A / Tier-B / Tier-C) used consistently. Good discipline.

### Journal-fit (Journal of Symbolic Computation)

JSC is the right home for this paper IF the algorithmic content of `etp_engineering_toolkit_v2.py` is foregrounded: §3 methodology + §9 toolkit + §10 verification together constitute the algorithmic claim. Complexity statements ("~15 seconds" / "~300 lines") are imprecise by JSC standards; replace with O(|ETP| · time_per_test) or measured per-step timings. Make sure `implications.json`'s authoritative source is cited (which Tao commit / which paper). The Fossil-Variety Theorem (if tightened) is a clean computational-algebra result that fits JSC's scope.

---

## J04 — Algebraic Rigidity of the σ-Magma on ℤ/10ℤ (Semigroup Forum)

**Verdict:** **Minor revision** — four exhaustive-search theorems are airtight; manuscript needs cosmetic LaTeX cleanup and one notation fix.

**Verification cross-check:** `verify_J59.py` is self-contained (no ETP dependency), uses only `itertools`. Enumeration ranges check out: 10! = 3,628,800 permutations (Theorem A), Bell(10) = 115,975 partitions (Theorem B), 2¹⁰ = 1024 subsets (Theorem C), C(10,2) = 45 pairs (Theorem D). Runtime "~3s" plausible for a 2020-era laptop. Result claims (|Aut|=1, 2 congruences, 5 sub-magmas, exactly one non-generating pair {1,6}) are all decidable by these enumerations.

### MAJOR issues

1. **None.** The four theorems are clean exhaustive-search results bounded by tractable finite sets.

### MINOR issues

1. **Multiplication-table rendering bug (lines 124–125).** Row 9 of the σ-magma table uses `\&` (escaped ampersand) instead of `&` — will not compile correctly. Similarly the `{1,6}` sub-magma table (lines 219–220).
2. **Uniqueness conjecture status muddled.** §6.1 states "FALSE in its strong form" and presents σ₁₀^min as a counterexample with IDENTICAL 14 ETP equations. But §6.4 then introduces a refined Tier-B/Tier-C statement. The narrative flow is: strong conjecture → refuted → refined → still-open. This should be one paragraph, not three subsections. Reader is left unsure what the actual open question is.
3. **Section 6 cross-reference to J01/J29/J05 should add a footnote** clarifying which artifacts BHML, CL_STD, TSML, T₂, T₄ refer to. Semigroup Forum readers may not have J01 to hand.
4. **σ permutation cycle parity claim** (§2.1): "σ is an odd permutation in S₁₀" — yes, the 6-cycle is odd. The four fixed points contribute trivially. Correct, but worth a footnote: the parity is used nowhere in the paper. If irrelevant, omit.
5. **§5.3 Family R reference.** "Family R" is introduced without prior definition (Family C is defined; Family R only appears in J05 §6 as the (5,3,6) mod 7 magma). Either define or remove the cross-reference.

### EDITORIAL

- Drápal-Wanless (2021): present in §References. CORRECT.
- §References lacks page range for McKay-Meynert-Myrvold (the paper extends pp. 98–119; the entry has only volume).
- Tier discipline excellent: PROVED for Theorems A–D, STRUCTURAL for the simultaneous-rigidity meta-claim, OPEN for §6. Good.
- The "maximally indecomposable" framing in §6 introduction is evocative; Semigroup Forum should accept it but a precise definition would strengthen the contribution.

### Journal-fit (Semigroup Forum)

Excellent fit. Semigroup Forum publishes structural-algebraic rigidity results of exactly this type. Four independent theorems by exhaustive search at small order, with a unifying interpretation ("maximally indecomposable commutative quasigroup of order 10"), is journal-standard. The σ-magma's specific choice (the framework-derived permutation) is foregrounded but the theorems are framework-independent — which Semigroup Forum will appreciate.

---

## J05 — ETP Profile Structure of Linear Magmas (ax+by+c) mod n (Experimental Mathematics)

**Verdict:** **Minor revision** — clean computational catalog; needs "linear magma" defined precisely up front and one verification gap closed.

**Verification cross-check:** `verify_J60.py` tests Theorems 1–4 against the ETP catalog. Theorem 1 (Z/n profile = 32 for n ∈ {5..10}) is verified by direct enumeration. Theorem 2 only checks n ∈ {4, 10} — fine, that's what's claimed. Theorem 3 (8-commutative intersection = 14 IDs) verified. Theorem 4 ((5,3,6) mod 7 profile = 14, different from σ-magma) verified. Runtime "~30s" plausible. PASS at machine precision.

### MAJOR issues

1. **§4.7 order-3 enumeration claim is NOT in the verify script.** The text claims "we enumerated all 729 = 3⁶ commutative order-3 magmas … 120 have profile 14, ALL sharing the IDENTICAL Family C equation set." The verify_J60.py does NOT perform this enumeration. The claim "Conjecture 1 confirmed at order 3" therefore rests on an unscripted computation. Required: add the order-3 (and order-5) full-enumeration scripts to the verification directory.

   *Note:* 3⁶ = 729 counts symmetric 3×3 tables with free off-diagonal entries, NOT all commutative order-3 magmas (commutativity does not constrain the diagonal). The arithmetic is correct (6 free entries: 3 diagonal + 3 upper-triangular off-diagonal) — but readers will check, so make this explicit.

2. **"Linear magma" definition needs sharpening at §1.1.** The current definition is fine but does not address what makes a linear magma a *quasigroup*. The quasigroup-with-condition note (§1.1) mentions gcd(a,n) = gcd(b,n) = 1 — this is correct but should be stated as a Theorem or Proposition with a one-line proof.

3. **Theorem 3 "any order ≥ 5" is the claim, but the intersection in verify_J60.py is computed over 8 specific magmas at orders 3, 5, 10.** The Z/3 entry pulls the floor below order 5. The statement should be: "Theorem 3 (verified): the intersection of the profiles of these 8 magmas equals these 14 IDs." The interpretation as a universal lower bound for "any commutative magma at order ≥ 5" is stronger and not directly verified.

### MINOR issues

- §4.4 small-order exception note for n=4 cites tabulated data without verification. Add the source: ETP `Generated/All4x4Tables/data/`.
- §5.2 anchor-equation table 23-row classification is cited with "1 family" or "3 families" counts; these are not in the verify script. Provide the list-as-data.
- §6 tables have unspecified "?" for order-5 negation magma profile. Either compute (~1s of work) or remove the row.
- §3.4 reference to "OPEN_FRONTIERS §65" — Experimental Mathematics readers will not have this. Provide a self-contained citation or reformulate ("a prior internal note that we have since corrected").

### EDITORIAL

- Drápal-Wanless (2021): present in §References. CORRECT.
- §10 (References): missing the implications.json source URL (ETP repo Generated/All4x4Tables/data/implications.json).
- Tier discipline: PROVED used for "computationally verified at machine precision" — consistent with Tao's ETP convention but should be stated up front (§0 mentions this; good).
- The "engineering recipes" §7 table is publication-friendly; Experimental Mathematics readers will use it.

### Journal-fit (Experimental Mathematics)

Strong fit. Experimental Mathematics specializes in: (i) computational enumeration of structural patterns, (ii) catalog-style results with conjectures pointing to deeper structure, (iii) reproducible verification scripts. This paper delivers all three. The cross-order universality of Family C's 14 equation IDs is exactly the kind of structural pattern Experimental Mathematics publishes. The 22-non-commutative + 1-commutative family classification at profile 14 is genuinely novel.

---

## J08 — F_p Structure of the 4-Core Commutative Non-Associative Algebra (Algebra Universalis)

**Verdict:** **Major revision** — merger logic is sound but the paper has substantive technical issues: §1.1 multiplication table is non-associative-AND-non-power-associative in ways §2.5 does not address; §2.2 invariant skeleton claim has internal contradictions; the verification script doesn't actually compute |Aut(V_p)|.

**Verification cross-check:** `verify_J_Fp_merged.py` verifies Theorem 1 (idempotent counts per prime) and Theorem 4 (BHML chain-shell determinants), and *references* Theorems 2 and 3 to `verify_J14.py` / `verify_J16.py` without re-computing them. The script's own §4 (check_T4_chain_shell_dets) is permissive: it accepts EXPECTED_DETS mismatch as "ck_tables.py BHML may differ from J14/J16 source" and continues. This is not a verification — it's an audit trail.

### MAJOR issues

1. **Multiplication table inconsistency between abstract description and §1.1 table.** The §1.1 explicit multiplication table is presented as a 4×4 with row 9 = `[e_4, e_0, e_3, e_0]` (the last row of the rendered table). But the verbal "equivalent" identities below the table (lines 49–53) say $e_4 \cdot e_4 = e_0$, which matches; but also $e_4 \cdot e_3 = e_3$, which the table reading gives. However: the table is asymmetric in row 8 / row 9 (row 8 has `e_3 e_4 e_2 e_3` while column 4 has `e_4 e_0 e_3 e_0`). For a commutative algebra, the table must be symmetric. Either there is a transcription error, or the algebra is NOT commutative — in which case "commutative non-associative" in the title is false. **This must be fixed before submission.**

2. **Power-associativity claim (§2.5) is sweeping.** "Direct polynomial-identity verification … vanish modulo every p" — the verify script does NOT compute this. The claim is "Tier A" but not script-verified.

3. **Idempotent-count §2.1 has TWO contradictory tables.** Lines 99–104 (table) show: p=2 has 4 total / 3 nonzero. p=3 has 6/5. p=5 has 4/3. The verify_J_Fp_merged.py EXPECTED_NZ dict (line 100) agrees. But the abstract says "$|\mathrm{Aut}(V_p)| \in \{6, 24, 40, 336, 1320, 2184\}$" — yet the verify script does NOT compute these. Theorem 2 is "Tier A (proved by direct group-theoretic enumeration in each characteristic)" but the verifier explicitly says "REFERENCE TO J14 verify" and "(Verified by J14's verify_J14.py at upstream tig_dirac.py)". J14 is NOT in the current portfolio (was renumbered or absorbed). The proof chain is broken.

4. **Theorem 3 proof sketch (lines 209–212) gives a specific decomposition** $\epsilon_2 = 2 e_3 + 3 e_4$, etc., but does not verify orthogonality directly. The "orbit-stabilizer count gives 40 as $|S_3| \cdot |\text{stabilizer}^{-1}| \cdot |\text{extra factor}|$" reads as a guessed formula, not a proof. A clean direct verification would be: enumerate idempotents in V_5, check orthogonal-triple existence, compute Aut.

5. **Merger tombstones for J48/J49 absent.** The paper says "Source papers (J48, J49) marked as MERGED" but the current J48 and J49 directories (still in `/05_papers/algebra/`) need explicit tombstone files referencing J08. Otherwise the audit trail breaks.

6. **§2.3 / §5.1 BHML chain-shell determinants.** The verify script EXPECTED_DETS = [5305, 2843, -2886, 2929, -7542, 7272, -7002] does not match observed values from ck_tables.py — the script flags this as "STRUCTURAL claim verified" but DOES NOT FAIL. This is a verification softening that should not exist in a paper claiming Tier-A. Either fix ck_tables.py or update the manuscript determinants to match.

### MINOR issues

- §1.1 line 124: "[[0 7 8 9] / [7 8 9 0] / [8 9 7 8] / [9 0 8 0]]" — this 4×4 is asymmetric (entry (2,3) = 8 vs (3,2) = 8; entry (2,1)=9 vs (1,2)=8 — INCONSISTENT). Verify before committing.
- §5.1 "70 = C(8,4)" rhyme: appropriate caveat ("structural rhyme honestly demoted to small-integer coincidence pending further derivation"). Good Tier discipline.
- §3 Theorem 2's $|\mathrm{Aut}(V_2)| = 6 = S_3$: the assertion "= S_3" needs proof or citation. There are multiple groups of order 6.
- §4.2 "smallest prime with 4 divides |F_p^*| = 4" — $|\mathbb{F}_5^*| = 4$, so 4 divides 4. Correct but the phrasing is awkward.

### EDITORIAL

- Drápal-Wanless (2021): present and prominently cited (line 31 of preamble, §References). CORRECT.
- Tier markers (Tier A / Tier B): the abstract claims four Tier-A theorems, but the verify script downgrades two of them. Be explicit: "Tier A (with verification gaps for §2.5 power-associativity and §3 Aut variation, deferred to J14)."
- Title "F_p Structure of the 4-Core Commutative Non-Associative Algebra" is fine.
- §6.4 cross-references to J20, J37 should be checked post-renumbering.

### Journal-fit (Algebra Universalis)

Algebra Universalis publishes variety-theoretic and equational-class results in the Birkhoff tradition. The paper as currently structured is more of an *F_p structure paper* than a variety-theory paper. The lens-invariant skeleton (§2) is genuinely variety-flavored; the Aut variation (§3) is structural-Lie-type adjacent (closer to J. Algebra). Recommendation: re-frame the §2 lens-invariant skeleton as the *primary contribution* (this is the Algebra Universalis core), demote §3 Aut variation to a §5 corollary, and add explicit variety-lattice language (subvariety inclusions, equational identities preserved by reduction). With these changes the paper is a strong Algebra Universalis candidate.

---

## Cross-paper observations

1. **Drápal-Wanless (2021) is cited correctly in all four papers.** Good.
2. **Honesty discipline (PROVED / COMPUTED / STRUCTURAL / OPEN) is well applied** in J03, J04, J05. J08 has gaps (see Major issues 2, 3, 6).
3. **The renumbering (J01–J52)** is consistent across the four papers but some cross-references in J08 (J14, J16, J20, J37) need verification — those papers may have been renumbered away.
4. **Inter-paper consistency:** J03 §5, J04 §6, J05 §4 all cite the "14 ETP equations of Family C" and the σ-magma realization. These three statements are mutually consistent. Good.
