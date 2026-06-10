# Referee Report — Algebra Cluster: J02, J05, J07, J08

**Reviewer venue cluster:** *Mathematical Intelligencer* (J02), *Experimental Mathematics* (J05), *European J. Combinatorics* (J07), *Algebra Universalis* (J08)
**Date:** 2026-05-28
**Source commit:** post-renumbering (0d6d0f1, J01–J52 scheme)
**Reviewer note:** Independent referee pass, cross-checking the prior cluster-03 report (which flagged J08 §1.1 as asymmetric). I confirm one of the prior findings, refute another, and identify two new technical errors in J08.

---

## J02 — The TSML 8×8 Null Space and a Structural Rhyme with RH (target: *Mathematical Intelligencer*)

**Verdict:** **Minor revision** — the short note is honest, the rhyme/proof boundary is sharply drawn, and the 5-line verification reproduces. One opening typo and a couple of expository tightens.

**Verification cross-check:** `verify_J62.py` is clean: it loads canonical `TSML` from `ck_tables.py`, slices indices `[1,2,3,4,5,6,8,9]`, asserts `rank(T8) == 7`, asserts `T8 @ v0 == 0` for `v0 = (0,0,0,0,1,-1,0,0)/√2`, asserts the largest eigenvalue ≈ 54.0767, and confirms `T8[4] == T8[5]` (CREATE row = ASCEND row). Runtime <0.1s, NumPy only, all asserts match the manuscript values. I independently re-derived rows 5 and 6 of the 8×8 core from `ck_tables.py` (TSML rows 5 and 6 in the original = `[0,7,7,7,7,7,7,7,7,7]` each, both reducing to `(7,7,7,7,7,7,7,7)` after stripping cols 0 and 7). The CREATE−ASCEND degeneracy is real and the proof in §3 is two lines as advertised.

### MAJOR issues

1. **None.** The rhyme/proof boundary at §5.4 (Conjecture Z.5) and §6 ("What this is and is not") is the strongest framing among Tier-1 RH-adjacent papers in the corpus. The Math Intelligencer audience will recognize the discipline.

### MINOR issues

1. **§1, line 29 typo.** `Let $\mathbb{Z}/10\mathbb{Z} = \{0, 1, 2, 3, 4, 5, 6, 8, 9\}$` lists only 9 elements (missing 7). The parenthetical "(we use 8, 9 because we want zero-indexed operator labels; the carrier set is just the integers mod 10)" reads as patching the typo but contradicts the set as written. Either write `$\mathbb{Z}/10\mathbb{Z} = \{0, 1, \ldots, 9\}$` cleanly, or explicitly say "we sometimes restrict to the 9-element subset for operator naming." As written, the line is a non-equality. **Fix before submission.**
2. **§1, line 55 non-associativity example.** The text presents three triples $(i,j,k)$ each producing $(i*j)*k = i*(j*k) = 7$, then defers non-associativity to "the BHML companion table; see [J01]." For a self-contained short note, exhibit one $(i,j,k)$ where the two associations *differ* in TSML itself. Otherwise the reader cannot verify non-associativity from this paper.
3. **§4 verification snippet line 121.** The five-line example imports `ck_tables` from GitHub but the actual `verify_J62.py` adjusts `sys.path` to the local repo root. Either harmonize (give the in-paper snippet a `sys.path` line) or footnote that the runnable form is the appendix script.
4. **§5.4 Conjecture Z.5.** The "3-grading + 6-corridor structure" referenced here without in-paper definition. For Mathematical Intelligencer's broad audience, give either a self-contained one-line definition or replace the load-bearing technical content with a pointer to J07 §1.4 (which has the six-layer table).
5. **§7.2 σ³ on 5-6 vs CREATE-ASCEND.** The aside about σ³ swapping (5,4)(2,7)(1,6) "not 5 and 6" is correct (verified: σ on the 6-cycle (1 7 6 5 4 2) gives σ³ = (1,5)(2,6)(4,7), so σ³(5) = 1, NOT 4). The manuscript writes "σ³ swaps 5 and 4" — this is WRONG. σ³(5) = 1, σ³(4) = 7. The fixed statement should be "σ³ pairs are {1,5}, {2,6}, {4,7}." **Fix the parenthetical.**

### EDITORIAL

- Drápal-Wanless (2021) cited correctly in §References.
- "Tier-A" / "Tier-B" markers consistent with corpus convention.
- Title threading "rhyme, not proof" is well calibrated.

### Journal-fit (Mathematical Intelligencer)

Excellent. The Intelligencer audience routinely sees expository pieces that draw structural analogies with major open problems while explicitly disclaiming proof. The 5-line NumPy verifier is exactly the kind of reproducible exhibit the Intelligencer favors. Fallback to *L'Enseignement Mathématique* is sensible.

---

## J05 — ETP Profile Structure of Linear Magmas (ax+by+c) mod n (target: *Experimental Mathematics*)

**Verdict:** **Minor revision** — clean computational catalog with 4/4 PASS verification; scope tightening required around "linear magma" vs. σ-magma examples, plus one verification gap.

**Verification cross-check:** `verify_J60.py` performs 4 ETP-backed checks: Theorem 1 (ℤ/n profile = 32 for n ∈ {5..10} with IDENTICAL equation IDs), Theorem 2 (−(x+y) mod n = 294 for n=4 and 10), Theorem 3 (intersection of 8 commutative magmas = 14 specific IDs), Theorem 4 ((5x+3y+6) mod 7 has profile 14 with intersection {1} against σ-magma profile). All four are decidable by the script. Runtime ~30s plausible given ETP overhead. Order ranges tested: n ∈ {5,6,7,8,9,10} for Theorem 1; n ∈ {4,10} for Theorem 2 (Theorem 2 itself only claims these); 8 specific magmas at orders 3,5,10 for Theorem 3; one (a,b,c,n) for Theorem 4.

### MAJOR issues

1. **§4.7 order-3 and order-5 enumerations are not in `verify_J60.py`.** The text says "we enumerated all 729 = 3⁶ commutative order-3 magmas" (with 120 at profile 14, all Family C) and "all 720 symmetric 5×5 Latin squares" (with 480 at profile 14, all Family C). The verify script tests Theorem 3's intersection but does NOT run these enumerations. The phrasing "Conjecture 1 confirmed at order 3 (Tier A)" — restated in J03 and J60 — rests on an unscripted computation. **Required:** add `verify_order3_enumeration.py` and `verify_order5_enumeration.py` to `manuscript/verification/`. These are tractable (~minutes), and without them the Tier-A claim is unsupported in the deliverable bundle.

2. **"Linear magma" scope mismatch with σ-magma examples.** The title and §1 frame the paper as a catalog of linear magmas $(ax+by+c) \bmod n$. But §4.5 introduces $\sigma_n^{\min}$ via permutation composition: $x \diamond y = \sigma((x+y) \bmod n)$ — this is NOT a linear magma in the sense of §1.1 (linearity requires $\sigma = \mathrm{id}$ or coefficients $a, b$). Verify line 98 confirms: `[sm[(x+y) % 10] for y in range(10)]`. Two options: (a) broaden the title/scope to "permuted-linear" or "generalized linear," (b) move σ-magma material to a §6.5 "non-linear addendum" with explicit scope flag. As written, Theorem 3's "every commutative magma at order ≥ 5 satisfies at least 14 IDs" uses non-linear σ-magmas in its support, blurring the catalog's stated boundary.

3. **§1.1 commutativity criterion needs a one-line proof or lemma.** "linear magma is commutative iff $a \equiv b \pmod n$" — correct (since then $ax + by + c = bx + ay + c$ iff $a \equiv b$, modulo $c$ that drops out). Promote to Lemma 1 with a two-line proof so the reader doesn't have to reconstruct.

4. **§1.1 quasigroup criterion stated, not proved.** "quasigroup-with-condition iff $\gcd(a,n) = \gcd(b,n) = 1$" — Experimental Mathematics readers will want a Proposition with proof. The condition is sufficient; necessity also holds (if either gcd > 1, the rows of $L_a$ or $L_b$ collide, so the magma isn't a quasigroup). One paragraph.

### MINOR issues

- §3.2 verification block prints `294/4694` without showing the actual table. Add the matrix for n=4 explicitly so the reader can spot-check by hand.
- §6.3 order-5 row "(unspecified, conj 294)" for the negation magma is computable in ~1s. Either compute or remove the row (per Conjecture 2 §3.5).
- §5.2 anchor-equation table (23 families) cited as data; provide the JSON/CSV in a supplementary file.
- §6 tables for n=4 and n=5 are sparse; expand or footnote that the full 64- and 125-row tables are in `manuscript/data/linear_magma_profiles.csv`.
- §3.4 reference to "OPEN_FRONTIERS §65" is internal; replace with a self-contained citation.
- §4.7 arithmetic note: 3⁶ = 729 counts symmetric 3×3 tables with free entries (3 diag + 3 upper triangular = 6 entries, 3⁶ states). Make this explicit so the reader doesn't reinvent.

### EDITORIAL

- Drápal-Wanless (2021) cited correctly in §References.
- Tier discipline (PROVED for empirical-tier verification per Tao convention; CONJECTURED at Tier-C) clear in §0; good.
- §10 References: missing the implications.json source URL in the ETP repo.

### Journal-fit (Experimental Mathematics)

Strong fit. Computational enumeration + catalog format + reproducible scripts = ExperimentalMath bread-and-butter. The 22-non-commutative + 1-commutative profile-14 classification is genuinely novel and is the strongest single result. The cross-order universality of Family C (verified at orders 3 and 5, conjectural elsewhere) is the kind of "structural pattern pointing to deeper theorem" that ExperimentalMath publishes.

---

## J07 — Spectral Architecture of the σ-Character on Z/10Z (target: *European J. Combinatorics*)

**Verdict:** **Minor revision** — five theorems are tight, merger consolidation reads cleanly, math-fix R1 is applied throughout. Need cosmetic tightening around the rhyme section and one definition cleanup.

**Verification cross-check:** `verify_qseries_merged.py` is self-contained NumPy-only, ~5s runtime. Verifies all five theorems:
- **G_6** (σ⁶ = id): direct iteration over all 10 elements. PASS.
- **G_7** (period distribution {1: 4, 6: 6}, mean 4, variance 6): direct enumeration. PASS.
- **G_8** (three-valued G(s): {0, 1.871644, 9.389185}): exact χ-iteration over 9 terms with ω = exp(2πi/9). Verifies anchors give 0, σ³-pairing structure ({1,5}, {2,6}, {4,7}), low-orbit value at s=1 and high-orbit value at s=4. PASS.
- **Q17-A** (5D embedding Φ injective): pairwise-distance check over 10 image points. PASS for injectivity. NOTE: the D₁₀ symmetry check on line 152 is `lambda v_s, v_s1: True` — a tautology, NOT a real test. The "PASS" output for "D_10 symmetry (structural)" is unsupported by the script. **Fix script** to verify the rotation action explicitly.
- **Q17-B** (Symbolic Return): direct corollary of G_6, trajectory enumeration. PASS.

I independently verified the σ³-pairing claim: σ on the 6-cycle (1 7 6 5 4 2) gives σ³(1) = 5, σ³(2) = 6, σ³(4) = 7 (so the three 2-cycles are exactly {1,5}, {2,6}, {4,7}). The χ-imbalance ν₊ table at §4.4 row-by-row reproduces (e.g., s=4 trajectory (4, 2, 1) has χ-values (+1, -1, +1), so ν₊ = 2 ✓; s=7 trajectory (7, 6, 5) has χ-values (-1, -1, -1), so ν₊ = 0 ✓). Both are in the high-locus orbit {4, 7} as claimed.

### MAJOR issues

1. **Q17-A's D₁₀ symmetry claim is unverified by `verify_qseries_merged.py`.** Line 152 of the verifier is a no-op (`lambda v_s, v_s1: True`). The §5.3 theorem text claims the image admits D₁₀ symmetry via $s \mapsto s+1$ (rotation) and $s \mapsto -s$ (reflection), generating order 20. Add an explicit script check: compute $\Phi(s+1) - R \Phi(s)$ for the asserted rotation matrix $R \in O(5)$ and verify within machine epsilon. Without this, the "Tier-A construction" half of Q17-A is sound but the "Tier-B uniqueness" half is unverified.

2. **§4.1 definition of G(s) needs the sum range justified.** "The sum is over the first 9 σ-iterates" — why 9? The natural choice for σ of order 6 would be 6 terms. The 9-term choice (with ω = 9th root of unity) is the load-bearing structural choice that produces the 3-valued image, but the §4.1 prose presents it as a definition without motivation. Add one sentence: "The 9-term length with ω = exp(2πi/9) is chosen so that the sum visits the σ-orbit's first three positions twice (since 6 = period and 9 = 6 + 3); this is the source of the χ-imbalance amplification at §4.4."

3. **Merger consolidation is clean** (J50, J51, J52 absorbed with proper subsumption notes in §9, math-fix R1 applied throughout) — confirm by inspection. **No issue here**; flagging it positively.

4. **Conjecture Z.5 in §7.2 cross-cuts with J02 §5.4.** The two papers share Conjecture Z.5 verbatim. Either (a) state it once in J02 (the explicit RH-rhyme paper) and cite it from J07, or (b) state it once in J07 (the spectral paper that does most of the spadework) and cite it from J02. As written, both papers are self-contained but the load-bearing conjecture is dual-stated, which is publication-redundant.

### MINOR issues

- §1.3 χ defined with "two carry $\chi = +1$ and four carry $\chi = -1$." Worth verifying this χ corresponds to a "real" character: it does not, it's the β-exception indicator. This is acknowledged ("not a multiplicative character") but the name "character" is itself slightly misleading. Consider relabeling as "β-exception sign function" or "χ-discriminator" in the abstract for EJC readers (Combinatorics audience may expect "character" to mean multiplicative).
- §5.2 line 203 typo in $(-1)^s$ — should clarify whether this is the multiplicative character of $\mathbb{Z}/2\mathbb{Z}$ at the generator (it is, but spell it).
- §5.4 Plancherel identity stated without proof. One paragraph proof or a citation.
- §7 (Clay bridge) is concise; the rhyme/proof discipline is sound. **No major issue.**
- §8 question 1 (closed-form recovery for $G_{\mathrm{low}}, G_{\mathrm{high}}$) — note that 9.389185 / 1.871644 ≈ 5.0165, which is suspiciously close to but not equal to 5. Worth noting this in the open question.
- $G_{\mathrm{low}} = 1.871644$ and $G_{\mathrm{high}} = 9.389185$ — I cross-checked: G(s) for s=1 numerically using the verifier's `G` function yields 1.871643... and for s=4 yields 9.389185.... Values are correct to the stated 6 decimal places.

### EDITORIAL

- Drápal-Wanless (2021) cited correctly.
- J50/J51/J52 marked as MERGED with subsumption notes in §9 — clean audit trail.
- Math-fix R1 (high-locus = {4, 7} via σ³-pairing, NOT {5, 7} via σ²) applied consistently throughout §4. Verified at line 164.
- §1.4 6-layer table is a strong navigational tool; keep it.

### Journal-fit (European Journal of Combinatorics)

Good fit. EJC accepts combinatorial-spectral papers with explicit symmetry-group content; the σ permutation of order 6 in $S_{10}$, its three-valued χ-coherence integral, and the 5D Fourier embedding all sit cleanly in EJC's scope. The χ-imbalance discriminator ν₊ as the structural explanation for the three-valued image is the combinatorial novelty (since the trichotomy follows from a pure counting argument on first-three positions). The "rhyme with RH" framing in §7 is light enough not to overshadow the combinatorial content.

---

## J08 — F_p Structure of the 4-Core Commutative Non-Associative Algebra (target: *Algebra Universalis*)

**Verdict:** **Major revision** — the merger logic and BHML chain-shell determinant tabulation are sound, but the paper contains two technical errors in §1.2/§2.5 that contradict its own Tier-A claims, plus broken references to verifiers that no longer exist post-renumbering.

**Verification cross-check:** `verify_J_Fp_merged.py` only fully verifies Theorem 1 (idempotent counts per prime). Theorems 2 and 3 are *referenced* to `verify_J14.py` / `verify_J16.py`, which **do not exist in the post-renumbering corpus** (J14, J16 were renumbered/absorbed). Theorem 4's chain-shell determinants are softened to "STRUCTURAL claim verified" with permissive mismatch handling on lines 158–168 — this is an audit trail, not a verification. **Lines 159–168 of the script explicitly accept det-mismatch as "ck_tables.py BHML may differ from J14/J16 source"** without failing. A Tier-A claim that does not fail-fast on numerical mismatch is not a Tier-A claim.

### MAJOR issues

1. **REFUTE the prior referee's flag of §1.1 table asymmetry.** I cross-checked the manuscript table (lines 42-47) against the actual BHML 4-core in `ck_tables.py` (rows 0, 7, 8, 9 at columns 0, 7, 8, 9). The BHML 4-core matrix is:
   ```
   [[0 7 8 9]
    [7 8 9 0]
    [8 9 7 8]
    [9 0 8 0]]
   ```
   This is symmetric: (0,7)↔(7,0)=7, (7,8)↔(8,7)=9, (8,9)↔(9,8)=8, (7,9)↔(9,7)=0, (0,8)↔(8,0)=8, (0,9)↔(9,0)=9. Translating to basis labels {e_0=0, e_2=7, e_3=8, e_4=9}, the manuscript §1.1 table is also symmetric: (e_2,e_3)=(e_3,e_2)=e_4, (e_2,e_4)=(e_4,e_2)=e_0, (e_3,e_4)=(e_4,e_3)=e_3. **The prior cluster-03 referee compared row 8 [the e_3 row] with column 4 [the e_4 column], which is an off-by-one indexing error: those rows/cols aren't supposed to match.** The correct symmetry check is row e_i vs column e_i. **The table IS symmetric and IS consistent with the BHML 4-core.** This claim should NOT be in the revision list.

2. **NEW FINDING — §1.2 $L_{e_3}$ is NOT a 4-cycle.** Manuscript line 78: "$L_{e_3}$ acts as $e_0 \to e_3, e_2 \to e_4, e_3 \to e_2, e_4 \to e_3$. This is the permutation $(e_0\,e_3\,e_2\,e_4)$ — a 4-cycle, so $L_{e_3}^4 = \mathrm{id}_V$." This is FALSE. The map $L_{e_3}$ sends $e_0 \to e_3$ and $e_4 \to e_3$ — both map to $e_3$, so $L_{e_3}$ is NOT injective and therefore NOT a permutation. The map has rank ≤ 3 (with $e_0 - e_4$ in the kernel). Consequently $L_{e_3}^4 \neq \mathrm{id}_V$. The §1.2 claim must be corrected. The rank-3 nature of $L_{e_3}$ may have downstream implications for the §2.2 / §2.5 invariants. **Fix and propagate.**

3. **NEW FINDING — §2.5 power-associativity FAILS for $a = e_2$.** The manuscript claims (Tier A): "$V_p$ is power-associative: $a^2 \cdot a = a \cdot a^2$ and $a^3 \cdot a = a^2 \cdot a^2$ for every $a$." Direct check for $a = e_2$, using the §1.1 table:
   - $e_2^2 = e_2 \cdot e_2 = e_3$
   - $e_2^3 = e_2 \cdot e_2^2 = e_2 \cdot e_3 = e_4$ (associativity not needed; commutativity gives the same)
   - $e_2^3 \cdot e_2 = e_4 \cdot e_2 = e_0$
   - $e_2^2 \cdot e_2^2 = e_3 \cdot e_3 = e_2$
   - $e_0 \neq e_2$, so $a^3 \cdot a \neq a^2 \cdot a^2$ at $a = e_2$. **Power-associativity FAILS.** The integer-valued "polynomial identity" the §2.5 proof gestures at does NOT vanish; it evaluates to $e_0 - e_2 \neq 0$ in $V$. This is not a mod-$p$ artifact — it's a failure over $\mathbb{Z}$. **Theorem 1's "five lens-invariant properties" reduces to four**; the §2.5 power-associativity entry must be removed or the multiplication table corrected.

4. **§2.2 "Minkowski signature (1,3) on $L_{e_2}$" sketch is loose.** The proof says "Direct computation shows the 1-eigenspace has dimension 1 and the complementary eigenspace has dimension 3, for every $p \in \{2, 3, 5, 7, 11, 13\}$." But $L_{e_2}$ is a cyclic permutation of order 4 — its eigenvalues over $\mathbb{C}$ are the four fourth-roots of unity $\{1, i, -1, -i\}$, each with 1-dim eigenspace. Over $\mathbb{F}_p$ the splitting depends on $p$ mod 4: at $p \equiv 1 \pmod 4$ (e.g., 5, 13) all four roots split into $\mathbb{F}_p$ as a 1+1+1+1 signature; at $p \equiv 3 \pmod 4$ (e.g., 3, 7, 11) only ±1 are $\mathbb{F}_p$-rational and the other two are conjugate over $\mathbb{F}_{p^2}$, giving a (1, 1, 2)-splitting in $\mathbb{F}_p$. At $p = 2$ the polynomial $x^4 - 1 = (x-1)^4$, so the splitting is (4) with a single Jordan block. The "(1, 3) Minkowski signature for every $p$" is therefore not literally true. Either qualify the statement ("over $\mathbb{F}_p$ when 4 | (p−1)") or replace with the actual prime-by-prime splitting.

5. **§3 broken verification chain.** `verify_J14.py` and `verify_J16.py` are referenced in lines 197, 213, 266 but **do not exist** in the post-renumbering `05_papers/` tree. J14 and J16 were absorbed or renumbered. Either include the missing scripts inline (the |Aut| enumeration is a brute-force isomorphism check, ~50 lines per prime), point at the surviving descendants, or downgrade Theorems 2-3 to "Tier A by external reference, not bundled."

6. **§4 Theorem 3 proof is incomplete.** Lines 209–212 give specific orthogonal idempotents:
   $\epsilon_2 = 2e_3 + 3e_4$, $\epsilon_3 = 3e_3 + 2e_4$, $\epsilon_4 = e_4 - e_2$
   over $\mathbb{F}_5$. Direct check using the §1.1 table:
   - $\epsilon_2 \cdot \epsilon_2 = (2e_3 + 3e_4)(2e_3 + 3e_4) = 4 e_3^2 + 12 e_3 e_4 + 9 e_4^2 = 4 e_2 + 12 e_3 + 9 e_0 = 4 e_2 + 2 e_3 + 4 e_0$ (mod 5). For this to equal $\epsilon_2 = 2 e_3 + 3 e_4$, we need $4 e_2 + 2 e_3 + 4 e_0 = 2 e_3 + 3 e_4$, i.e., $4 e_2 + 4 e_0 + 0 \cdot e_3 + 3 e_4 = 0$ in $V_5$ — but $\{e_0, e_2, e_3, e_4\}$ is a basis, so this is false. **The stated $\epsilon_2$ is NOT idempotent.** The proof sketch needs full restatement (possibly with the correct idempotents from `verify_J16.py`, which is itself missing).
   - The "orbit-stabilizer count gives 40 as $|S_3| \cdot |\text{stabilizer}^{-1}| \cdot |\text{extra factor}|$" reads as a placeholder, not a proof. Replace with a clean enumeration.

7. **Theorem 4 chain-shell determinants softening.** Per item above, the verify script accepts mismatches as "BHML version drift." If the published claim is the seven specific determinants 5305, 2843, −2886, 2929, −7542, 7272, −7002, then `verify_J_Fp_merged.py` must FAIL on mismatch, not log-and-continue. Tighten the script.

### MINOR issues

- §1.1 line 67 BHML 4×4 matrix is correctly transcribed from `ck_tables.py`; the §1.1 explicit table at lines 42-47 is consistent with it. **Confirmed by direct comparison.**
- §2.1 idempotent count table: the verify script's EXPECTED_NZ dict (`{2:3, 3:5, 5:3, 7:3, 11:5, 13:7}`) matches the §2.1 table. Good consistency.
- §3 "$|\mathrm{Aut}(V_2)| = 6 = S_3$" — needs proof or citation (there are multiple order-6 groups: $S_3$ and $C_6$).
- §4.2 phrasing "smallest prime with 4 divides $|\mathbb{F}_5^*| = 4$" is awkward. Rephrase as "$\mathbb{F}_5$ is the smallest prime where $\mathbb{F}_p^\times$ contains a primitive 4th root of unity."
- §5.1 "70 = C(8,4)" rhyme: appropriate caveat. Good Tier discipline.
- §6.4 cross-refs to J20, J37 should be checked post-renumbering.

### EDITORIAL

- Drápal-Wanless (2021) cited correctly (preamble line 31, §References).
- Tier markers: claims four Tier-A theorems; with the §2.5 power-associativity failure and the §1.2 $L_{e_3}$ error, two of those Tier-A claims downgrade. Be explicit.
- Source-paper merger tombstones (J48, J49) not present in the manuscript tree — add explicit `MERGED_INTO_J08.md` notes per the prior cluster-03 referee.

### Journal-fit (Algebra Universalis)

Algebra Universalis publishes variety-theoretic / equational-class results. The current paper is more of an "$\mathbb{F}_p$ structure" paper than a variety-theory paper. The §2 lens-invariant skeleton — once the technical errors above are fixed — is variety-flavored (preservation of equational identities across primes). The §3 Aut-variation is structural-Lie-type and closer to J. Algebra or Algebras & Representation Theory. **Recommendation:** re-frame §2 as the primary contribution, demote §3 to a §5 corollary, and add explicit variety-lattice language. With the §1.2, §2.5 fixes and the verifier tightened, Algebra Universalis is the right home.

---

## Cross-paper observations

1. **Conjecture Z.5 duplicated between J02 and J07.** State once, cite from the other.
2. **σ-permutation is consistent** across J02 §7, J05 verify_J60 line 84, J07 §1.2 — all agree σ = (0)(3)(8)(9)(1 7 6 5 4 2). Good.
3. **Drápal-Wanless (2021) cited correctly in all four papers.** Good.
4. **Tier discipline:** J02 and J07 strong; J05 has one verification gap (order-3 and order-5 enumerations not scripted); J08 has technical errors AND verifier softening — needs the most work.
5. **Verifier-script bundling:** J02 `verify_J62.py` is fully self-contained from `ck_tables.py`. J07 `verify_qseries_merged.py` is self-contained, but the Q17-A D₁₀ check is a no-op (fix). J05 `verify_J60.py` depends on an external ETP clone — flag in README. J08 `verify_J_Fp_merged.py` references missing verifiers and softens mismatch — fix or replace.

---

*— Independent referee pass, 2026-05-28.*
