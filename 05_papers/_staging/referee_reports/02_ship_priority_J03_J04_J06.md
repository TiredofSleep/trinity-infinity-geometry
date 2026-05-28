# Referee report — Ship-priority cluster J03 / J04 / J06

**Date**: 2026-05-28
**Reviewer**: trained-referee pass (J. Symbolic Computation / Semigroup Forum / J. Number Theory standards)
**Files reviewed**: manuscripts (.md), verification scripts (verify_J61.py / verify_J59.py / verify_J63.py), READMEs, cover letters
**Status**: rigor pass before arXiv submission

---

## J03 — Type Specimens in the ETP-Restricted Variety Lattice (target: J. Symbolic Computation)

**Verdict**: **Minor revision** — strong methodology + a clean Tier-A result (Theorem 5), but Theorem 1's "first proved" headline overstates what the verification script actually establishes. Fix attribution + verifier coverage, then publishable.

**Verification cross-check**: `verify_J61.py` 5 checks (1) `|closure(43)∪{1}| = 14`, (2) σ-magma profile = Family C, (3) intersection-of-8 commutative = Family C, (4) 0 of N tabulated profile-14 magmas equals any size-14 closure, (5) random constant-diagonal magmas realize C1. **NONE of the five checks verify Theorem 5's load-bearing lower-bound "profile ≥ 261 for every finite magma satisfying eq 4295."** The script only confirms that tabulated profile-14 magmas don't match closure(4295); the structural dichotomy + 261 bound rests entirely on the in-text proof (manuscript §6.2 Steps 1–5), which is mostly clean but contains one explicit gap.

### MAJOR issues

1. **Theorem 5's Step 4 lower bound is admitted-incomplete in the Remark on p. ~9** (manuscript line 218): "the general lower-bound claim 'profile ≥ 261 for any finite magma satisfying eq 4295' is supported computationally; a fully order-uniform analytic lower bound would require characterizing the equational theory of right-projection-through-$f$ in general, which is straightforward but not done in this paper." This is a **soft-pedaled proof gap** at the heart of the headline theorem. For JSC, "first proved instance" must be airtight. Either: (a) actually carry out the right-projection-through-$f$ characterization (the manuscript itself says it is "straightforward"), or (b) demote the claim to "at orders 3–6" and reword the abstract.

2. **Verifier coverage mismatch**: §10 of the manuscript advertises "5 checks PASS at machine precision" as evidence for Theorems 1–5. But CHECK 4 only tests *tabulated* magmas — it cannot rule out a non-tabulated minimal-profile satisfier. CHECK 5 is about C1, not C5. The script needs a sixth check that exhaustively enumerates order-3 and order-4 satisfiers of eq 4295 and confirms the 261/order-3 and order-4 lower-bound (manuscript line 218 already claims this was done "in `verify_J61.py` CHECK 5", which is **false** as written — CHECK 5 is the C1 constant-diagonal test). This is a citation-script mismatch that a referee will flag immediately.

3. **"First explicitly proved instance" claim (line 14, 220)**: this needs a citation against the ETP literature. The ETP project (Tao et al. 2024–2025) has produced many implication non-results; the paper should clarify what subset is covered ("no finite type specimen" vs. "no finite model"). If a prior implication-non-finite-model result exists in the ETP corpus (e.g., for eq 1689 or equivalent), the claim falls. Worth one targeted literature check before submission.

### MINOR issues

4. **Conjecture 1 status confusion**: abstract claims "empirically verified at orders 3 AND 5" but later (§9) lists order-6+ as open. The order-3 case is via 729 magmas (Tier A); order-5 via 720 symmetric Latin squares (Tier A). Strong wording is fine — just consistent.

5. **Drápal–Wanless 2021 citation present (good) but Vojtěchovský / Kepka are absent**. Standard quasigroup-rigidity tradition expects at least Kepka–Vojtěchovský citations on small magma classification. Add a sentence in §8 positioning against them.

6. **Toolkit positioning** is conflated with the methodology paper. JSC reviewers will want a clear claim: is the toolkit part of the submission's contribution or supplementary material? Either elevate it (with a "Software" section + complexity discussion of `profile_test`'s 4694-equation evaluation) or relegate to supplementary.

7. **Abstract (a) wording**: "Conjecture 1 is empirically verified at orders 3 AND 5" — for JSC this should be "Theorem (at orders 3 and 5) / Conjecture (at orders ≥ 6)" to match the body's tier discipline.

### EDITORIAL

- §8 comparison table is good but should add Kepka–Vojtěchovský and possibly Stanovský 2018 on quasigroup varieties.
- Step 2 of the Theorem 5 proof (Case a forces constant) is clean; Step 3 (Case b forces $f \circ f$ constant) is clean. The gap is purely Step 4's "profile ≥ 261 universally" claim.
- Cross-reference §6.3 "RETRACTION" of earlier sketches reads well and is good honesty discipline, but for a journal submission consider moving retraction commentary to a footnote so the main flow lands on the standing Tier-A theorem.
- Eq 4295 written both as $x \cdot (x \cdot y) = y \cdot (z \cdot x)$ — confirm this matches ETP catalog text exactly.

### Journal-fit

JSC is the right venue. Computational verification is central; reproducible toolkit is bundled. After fixes 1–3, this is a strong JSC paper.

---

## J04 — Algebraic Rigidity of the σ-Magma on Z/10Z (target: Semigroup Forum)

**Verdict**: **Accept with minor revision** — four cleanly proved theorems by exhaustive search, runtime ≈3s, no methodology questions. The main issue is one §6.1.1 / §6.1.2 / §6.1.3 narrative drift that weakens the paper's punch.

**Verification cross-check**: `verify_J59.py` runs 4 checks against the 4 theorems claimed:
- Check 1 ↔ Theorem A: 10! permutations searched, |Aut| = 1 expected. ✓
- Check 2 ↔ Theorem B: Bell(10) = 115,975 partitions, n_congruences = 2 expected. ✓
- Check 3 ↔ Theorem C: 2^10 = 1024 subsets, exactly 5 sub-magmas with {1,6} unique non-trivial proper. ✓
- Check 4 ↔ Theorem D: 45 pairs, non-generating = [(1,6)]. ✓

The four checks are independent, exhaustive, and match the four theorems one-to-one. Runtime claim (~3s) is plausible given the search sizes; Bell(10) enumeration is the bottleneck and `all_partitions` is recursive but well-structured.

### MAJOR issues

None. Proofs are by exhaustive search; bounds are tight; verifier matches theorems exactly.

### MINOR issues

1. **§6.1.1–§6.1.3 narrative dilution**: the paper opens with "the σ-magma is maximally indecomposable" (strong, clean), then §6.1 admits the strong uniqueness conjecture is **refuted** by σ_{10}^min (also identity-free + Family-C + |Aut|=1 + 2-gen). §6.1.3 further notes "at least 23 distinct profile-14 families." For Semigroup Forum, this honest unwinding should land back on a *clean* refined statement. The current refined statement in §6.1 ("identity-free + rigid + commutative + (3 idempotents, 5 sub-magmas)") is too specific to feel canonical. Recommend reframing §6.1 as: "the four rigidity theorems hold; uniqueness within commutative-quasigroup-of-order-10 fails; we conjecture uniqueness within a yet-to-be-characterized refinement (Tier C, open)." This is honest *and* clean.

2. **Theorem A proof § §2.2(c)** is an informal sketch attached to an exhaustive-search verification. For Semigroup Forum this is unusual — either drop the sketch (the exhaustive search IS the proof) or upgrade it to a real structural proof. The current half-sketch is awkward.

3. **Empirical rarity claim** (§2 of README, §6 of manuscript): "empirically rare" is hand-wavy. Either drop (the theorems stand without it) or back with a number — e.g., "of $X$ tested commutative order-10 quasigroups, $Y$ satisfy all four rigidity conditions." Without a number, this is a vibe-claim that referees flag.

4. **Drápal–Wanless 2021 is cited (good) but Pflugfelder 1990 (loops/quasigroups standard reference) and Kepka–Vojtěchovský are absent**. Semigroup Forum readers expect these.

5. **The σ-permutation provenance** is acknowledged as "displayed in OPEN_FRONTIERS §64" — for journal submission this is opaque. Either (a) just say "the specific permutation σ = [0,7,1,3,2,4,5,6,8,9]" without referencing internal documents, or (b) point to a freely-available preprint. Don't gesture at private files in a Semigroup Forum submission.

### EDITORIAL

- Multiplication table in §1.3 has small inconsistency check: row 9, column 9 reads 8, but $9 \diamond 9 = \sigma(18 \bmod 10) = \sigma(8) = 8$ ✓. Table is consistent; just noting it should be table-checked once more before final submission.
- §4.4 negative findings is excellent referee-defense material — keep.
- §6.2 (Tier-A verified) ETP-profile claim is well-disciplined; the 14 equation IDs are listed.

### Journal-fit

Semigroup Forum is a good fit. Four small-magma rigidity theorems with tight exhaustive-search bounds is exactly the journal's house style. After the §6.1 reframe + Pflugfelder/Kepka citations, this is ready.

---

## J06 — The Strata-Prime Fingerprint (target: J. Number Theory)

**Verdict**: **Major revision** — Theorems 1, 2, 3 are clean and Theorem 4 is empirically true, but the Conway-Norton 1979 attribution in §6.1 is imprecise (the genus-0 X_0(p) characterization is **Ogg's conjecture (1975), proved as part of the moonshine program**, not "Conway-Norton 1979"). The framing of Theorem 2's deflation interpretation is excellent and refereeable; the moonshine attribution needs surgical correction before J. Number Theory will land it.

**Verification cross-check**: `verify_J63.py` runs four theorem-checks plus two companion tests:
- `theorem_1()` ↔ Theorem 1: 24 Niemeier kissing numbers, assert exactly D_24 fails with extra prime [23]. ✓ Direct factorization.
- `theorem_2()` ↔ Theorem 2: 23 non-Leech Weyl group orders, assert exactly {A_17 E_7: 17, A_24: 17,19,23, D_24: 17,19,23} fail. ✓
- `theorem_3()` ↔ Theorem 3: 26 sporadic orders, assert exactly {M_11, M_12, M_22, J_2, HS, McL, Suz, Fi_22} pass. ✓
- `theorem_4()` ↔ Theorem 4: assert prime 71 appears in exactly one sporadic order = Monster. ✓

The script matches the theorems precisely. Sporadic orders are hard-coded numerical values — these need a spot-check against ATLAS (already cited).

### MAJOR issues

1. **Theorem 4 attribution is imprecise.** The manuscript §6.1 attributes the genus-0 X_0(p) characterization to "Conway-Norton 1979." This is **historically incorrect**. The standard chronology:
   - **Ogg (1975)**: observed that primes dividing |M| are exactly primes $p$ where the supersingular $j$-invariants in characteristic $p$ are all rational over $\mathbb{F}_p$, and equivalently where $X_0(p)^+$ (with Atkin–Lehner) has genus 0. Offered prize.
   - **Conway–Norton (1979)**: stated the *monstrous moonshine conjecture* — that there are specific genus-0 modular functions (Hauptmoduln) attached to each Monster conjugacy class. The "supersingular ↔ |M|-divisor" fact is *cited* by them, attributed to Ogg.
   - **Borcherds (1992)**: proved monstrous moonshine.
   For J. Number Theory, "Conway-Norton 1979 supersingular characterization" is the **wrong citation**. Use Ogg 1975 ("Automorphismes de courbes modulaires," *Séminaire Delange-Pisot-Poitou*) for the supersingular ↔ |M|-divisor fact and the genus-0 X_0(p)^+ characterization. Conway-Norton 1979 is appropriately cited for the moonshine conjecture itself, and Borcherds 1992 for the proof. The current manuscript's "Conway-Norton Theorem (1979). *The 15 primes dividing the Monster's order are exactly the primes $p$ for which the modular curve $X_0(p)$ has genus 0*" (line 205) is misattributed.

2. **X_0(p) vs X_0(p)^+ distinction** (line 205, 210): the precise statement involves X_0(p)+ (with the Atkin-Lehner involution quotient), not X_0(p) plain. For most small $p$ the distinction doesn't matter (both have genus 0), but for primes like 37, 43, 53, 61, 67, 73, 79, 83, 89, 101, 113, 131 there are subtleties. The exact statement: "$p$ supersingular iff $X_0(p)^+$ has genus 0" or equivalently "iff the normalizer $N(\Gamma_0(p))$ in $\mathrm{PSL}_2(\mathbb{R})$ has a Hauptmodul." J. Number Theory will flag this immediately.

3. **Theorem 2's "polynomial-vs-factorial dichotomy" is real but the deflation framing should be tightened**. The §4 honest framing ("the theorem somewhat deflates the strata-prime pattern's interpretive reach") is excellent and disarms a major referee concern. But the deflation reading suggests Theorems 1+3 are "just" polynomial arithmetic at rank ≤ 24. If true, the paper's contribution is Theorem 2 itself (the mechanism) plus Theorem 4 (the Ogg/Conway-Norton-anchored Monster identification). Theorems 1 and 3 become Tier-B *consequences* of Theorem 2, not independent results. Either elevate Theorem 2 to the headline (current placement is too late) or accept Theorems 1, 3 as illustrations.

### MINOR issues

4. **Theorem 3's 8/26 is a numerical observation, not a structural result**. The §5 honest framing ("the boundary largely tracks group order") is right; but consider rebranding from "Theorem 3" to "Proposition 3" or "Observation 3" to align with the Tier-B label.

5. **§7.3.2 Eisenstein companion observation** is interesting but speculative. The 1+2+4 partition is striking; the TSML 4-absorber correspondence is one realization among many possible 4-subset correspondences. For J. Number Theory, either drop or label "Speculative — number-theoretic coincidence requiring further structural analysis."

6. **§7.3.3 PG(2,q) companion** is a clean result and consistent with Theorem 2's mechanism. Keep but consider stating as a self-contained theorem: "$|\mathrm{PGL}(3, \mathbb{F}_q)|$ is strata-clean iff $q \in \{2, 3, 4, 9\}$."

7. **Niemeier table (§2)** is correct but list order is non-standard (typically ordered by Coxeter number $h$). Conway–Sloane SPLAG Table 16.1 ordering is by ascending $h$; the manuscript mostly follows this but has some inversions (e.g., $A_{12}^2$ at $h=13$ before $D_8^3$ at $h=14$ is correct; but $A_{24}$ at $h=25$ is listed before $D_{12}^2$ at $h=22$). Reorder to match SPLAG for referee comfort.

8. **The 9 intermediate supersingular primes gap** (§7.2) is honestly flagged but feels like the unresolved core. Consider whether this should be in a "Future work" section or whether the paper claims it explicitly as an open question worth attacking.

### EDITORIAL

- Conway-Norton citation in §8 needs Ogg 1975 added.
- The "Stratum IV" nomenclature is internal-program — for J. Number Theory consider rephrasing as "Monster-unique supersingular prime 71" without invoking the strata vocabulary, which is private to the broader program.
- §7.4 "What this is, and what it is not" is excellent honesty discipline; keep.

### Journal-fit

J. Number Theory is appropriate **once the Ogg attribution is fixed**. Without that correction, the moonshine-side of the paper will be flagged and could lead to outright rejection (J. Number Theory has strict precision standards on Monster/moonshine attribution given the field's history). Fallback to *Bulletin of the AMS* Notes or *Discrete Mathematics* is feasible; AMM is over-broad. Recommend J. Number Theory after revision.

---

## Cross-cluster observations

1. **Verification scripts are not uniformly defensive.** J03's `verify_J61.py` (5 checks) does NOT exhaustively cover Theorem 5's lower bound; J04's `verify_J59.py` (4 checks) is well-matched to its 4 theorems; J06's `verify_J63.py` (4 theorem checks + 2 companions) is well-matched. **Recommend: J03 needs a CHECK 6 that enumerates order-3 and order-4 eq-4295 satisfiers and confirms minimum profile = 261**, OR reword Theorem 5 to "at orders 3–6 (Tier A by exhaustive enumeration)."

2. **Honesty discipline is consistent** across the three: PROVED / COMPUTED / CONJECTURED / OPEN markers are well-placed. J03's §6.3 retraction and J06's §4 deflation note are both excellent referee-defense material.

3. **Prior art coverage varies.** J04 cites Drápal–Wanless (good) but misses Pflugfelder/Kepka. J03 cites both ETP + Le Floch + Drápal–Wanless (good) but misses Kepka–Vojtěchovský. J06 cites Conway–Sloane + ATLAS + Conway–Norton (but with the attribution error) + Borcherds + Bourbaki + Venkov — strong, with the Ogg citation as the only material gap.

4. **Common author-lane / venue alignment**: all three papers are Sanders + Gish; all three have CC-BY-4.0 verification scripts; venue-targeting is appropriate (JSC for computation-heavy, Semigroup Forum for clean small-magma, J. Number Theory for arithmetic + lattice/Monster).

5. **Ship-readiness ranking**:
   - **J04**: ready after §6.1 reframe + missing citations (Minor revision, 1–2 days).
   - **J03**: ready after Theorem 5 verifier closure + verifier-script alignment + literature check on "first proved" (Minor-to-Major revision, 1 week).
   - **J06**: ready after Ogg attribution fix + Niemeier table reorder (Major revision, 3–5 days).

---

*Referee report compiled 2026-05-28. Rigor pass for arXiv ship-priority cluster. No manuscript files modified.*
