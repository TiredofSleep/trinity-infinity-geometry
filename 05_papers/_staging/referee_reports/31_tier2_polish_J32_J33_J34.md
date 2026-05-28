# 31 — Tier 2 Polish Pass: J32 + J33 + J34

**Date:** 2026-05-28
**Scope:** Tier 2 polish on the first three of the Tier 2 papers per `_staging/TIER_INDEX.md` — J32 (algebra), J33 (combinatorics), J34 (combinatorics).
**Mandate:** Bring each paper to "good Tier 2 standing" — clean status, scoped venue, verify script PASS, known issues documented. Manuscripts otherwise untouched.

---

## J32 — TSML 73 / BHML 28 Cell Counts

**Paths:** `05_papers/algebra/J32/{README.md, cover_letter.md, manuscript/manuscript.tex, manuscript/proof_d10_tsml_73_cells.py, manuscript/proof_d16_bhml_28_cells.py, manuscript/ck_tables.py}`

### Manuscript-level summary

The paper proves two specific harmony-cell counts on Z/10Z by elementary disjoint-zone enumeration:

- **Theorem 1** (TSML harmony count): `h(TSML) = 73`. Proof: three disjoint exception classes (V0, V1, E) account for 27 non-harmony cells (9 + 8 + 10); default rule (D) gives the remaining 73 = HARMONY. Two-line proof.
- **Theorem 2** (BHML harmony count): `h(BHML) = 28`. Proof: four disjoint zones (R_A, R_B, R_7, R_89) contribute 2 + 11 + 2 + 13 = 28 harmony cells. Two-line proof.
- **Theorem 3** (Symbol-stabilizer invariance): both counts are constant on Stab(7)-orbits of S_10 acting by transport of structure. Two-line proof; honestly framed in Remark 4.1 as a consistency check rather than a substantive autotopism invariance theorem.

§5 (family-structure) locates TSML and BHML as canonical members of a finite family of commutative non-associative magmas on Z/10Z satisfying five conjoint conditions (C1–C5), with Drápal–Wanless 2021 as the closest published precedent. §6 records joint cell statistics (intersection = 26, union = 75) without invoking the deeper joint-closure chain of the companion four-core paper.

Tier markers (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are explicit at §0 of the manuscript and §5 of the README.

### Verify scripts

- `proof_d10_tsml_73_cells.py` — PASS (`ALL ASSERTIONS PASSED`). Verifies TSML = 73 by disjoint enumeration over the 100 cells.
- `proof_d16_bhml_28_cells.py` — PASS (`ALL ASSERTIONS PASSED`). Verifies BHML = 28 by four-zone partition.

Both scripts terminate in well under 0.1 s on standard CPython with no external dependencies; tables defined in bundled `ck_tables.py` (CC-BY-4.0).

### README edits applied

- **§1 file list corrected.** The README previously claimed the main manuscript file was `tsml_bhml_cell_counts.tex` and listed five auxiliary files (`proof_fourier_bridge.py`, `SUBMIT_INSTRUCTIONS.md`, `WP35_PRIME_PHASE_TRANSITION.md`, `WP_OPERATOR_RING_PARTITION.md`, and the `tsml_bhml_cell_counts.tex` itself) — none of which exist in `manuscript/`. The actual file is `manuscript.tex` and the directory contains exactly four files (one `.tex`, two `.py` proofs, and `ck_tables.py`). README §1 normalized to the actual contents.
- **Known-issues §extended** with three polish-pass observations: (1) verify scripts confirmed PASS; (2) both cell-count theorems are sound by elementary disjoint-zone enumeration; (3) the file-list correction noted above.

### Known substantive issues (flagged for future user attention)

- Brayden's referee-rigor pass (mobile + other AI + collaborators) is not yet complete.
- Theorem 3 (lens-invariance) is honestly framed as a consistency check; whether the Stab(7)-invariance extends to autotopism / paratopism invariance is open. Either tighten or leave as a one-paragraph open question before submission.
- The companion four-core paper is cited as `manuscript in preparation` — coordinate with VENUE_SCHEDULE.md / J15 (Algebraic Combinatorics target) for cross-citation consistency.

### Recommended target venue

**Experimental Mathematics** (unchanged from the existing README assignment). The paper fits the *Experimental Mathematics* scope exactly: small finite cell-count theorem with runnable 200-cell witness, PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline, self-contained reproducibility from the manuscript folder.

### Tier 2 readiness verdict

**GOOD.** The math is sound, scripts pass, abstract is honest, file list is now accurate. Ship-blockers are external (referee-rigor pass + Brayden's final read). No demotion needed.

---

## J33 — Flatness Obstruction on Squarefree Z/nZ

**Paths:** `05_papers/combinatorics/J33/{README.md, cover_letter.md, manuscript/manuscript.md, manuscript/verify_J07.py}`

### Manuscript-level summary

Two theorems on the four-structure system (A-Struct, M-Struct, A-Flow, M-Flow) on squarefree Z/nZ with k ≥ 2 distinct prime factors:

- **Theorem 1 (Flatness Obstruction)** — No flat 2D-grid embedding with separately totally ordered coordinate axes can simultaneously carry all four structures. Proof reduces to the explicit partition-incompatibility of prime-factor residue partitions (Birkhoff 1940 / Ore 1942), with a 3-line proof for n=10 inlined.
- **Theorem 2 (Configuration-Space Topology)** — The natural carrier is the quotient of S¹ × S¹ obtained by identifying M-Flow fixed points. Honestly framed: the ring Z/nZ is *not* the torus; it is the lattice of marked points where both phases are simultaneously rational with denominator dividing n.

Appendix A supplies the algebraic-center material for Z/10Z with the canonical (TSML, BHML) pair: D48 (4-core joint closure, 16 + 16 in-core / 0 + 0 spillover) and D78 (Galois-forced H/Br = 1+√3 at α_M = 1/2 in **Q**(√3), root of x² − 2x − 2 = 0). Verified at 50-digit `mpmath` to residual 9.06e-46.

The earlier "torus aspect ratio = 5/7" derivation was explicitly abandoned per SAVE_PLAN_J07 (2026-05-07); the cyclotomic field-extension facts deg_Q A_5 = 2 and deg_Q A_7 = 3 remain as STRUCTURAL RHYME motivation only.

Tier markers (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are explicit in §0.2 of the manuscript and §5 of the README.

### Verify script

- `verify_J07.py` — PASS 4/4 at machine / 50-digit `mpmath` precision. Checks: (1) Theorem 1 partition incompatibility at n=10; (2) manuscript A.1 sub-tables match canonical TSML / BHML; (3) D48 joint closure 16 + 16; (4) D78 closed-form attractor 1+√3 with polynomial identity (H/Br)² − 2(H/Br) − 2 = 0 to 50 digits, convergence in 99 iterations from uniform start. Runtime < 2 s.

### README edits applied

- **Known-issues §extended** with four polish-pass observations:
  1. Verify script confirmed PASS 4/4 at 50-digit precision.
  2. **CRITICAL — self-citation collision under 2026-05-27 renumbering.** The manuscript at `manuscript/manuscript.md` references "companion paper J33" three times (§0.1 lens-ownership, §A.3 D78 statement, §A.5 status statement) plus the references list at line 211 calling the *other* paper "[J33]". Under the post-2026-05-27 renumbering, *this* paper (Flatness Obstruction) is J33; the cited "α-uniqueness PSLQ" paper has a different number and must be re-labeled throughout. The same issue appears in `cover_letter.md` line 39.
  3. Theorem 1 + Theorem 2 sound, no math errors of the J08 type.
  4. Appendix A.3 (D78) cites a verification script (`f3_galois_alpha_uniqueness.py`) located outside the submission folder; the 50-digit `mpmath` confirmation is bundled in `verify_J07.py` and reproduces the polynomial identity, but the structural BR-factor cancellation derivation is referenced rather than inlined.

### Known substantive issues (flagged for future user attention)

- **Self-citation collision under renumbering (ship-blocker).** Three "J33" references inside the J33 manuscript and one in the cover letter actually refer to a different paper (the α-uniqueness PSLQ paper). All must be re-labeled with the current post-2026-05-27 number before submission. This is the single biggest ship-blocker for J33.
- Brayden's referee-rigor pass not yet complete.
- Per-venue cap check vs J15 (also targeting *Algebraic Combinatorics*) pending; coordinate with VENUE_SCHEDULE.md.
- No new fresh-eyes referee report has been issued post-save-plan rewrite; a second-pass referee read may surface new issues, particularly on Theorem 2's "the ring is not the torus" framing (which is the M2 referee fix and is correct as written but could be sharpened).
- Appendix A's reliance on a verification script (`f3_galois_alpha_uniqueness.py`) outside the submission folder is acceptable for Tier 2 draft but should be addressed before ship (either inline the BR-factor cancellation steps or bundle the script).

### Recommended target venue

**Algebraic Combinatorics** (unchanged from existing README assignment). Backup: *Discrete Mathematics*. The Birkhoff–Ore partition-lattice framing of Theorem 1 combined with the small finite commutative non-associative magma analysis of Appendix A (Drápal–Wanless 2021 neighborhood) sits squarely in the AC scope. The per-venue cap with J15 is the only concern.

### Tier 2 readiness verdict

**NEEDS WORK.** The math is sound and the verify script passes at high precision, but the self-citation collision (three "J33"→"different J-paper" references inside the J33 manuscript plus one in the cover letter) is a real ship-blocker that must be resolved before submission. The fix is bounded (search/replace the J-number) but requires confirmation of the new number for the α-uniqueness PSLQ companion. After that fix, J33 is GOOD Tier 2.

---

## J34 — Coordinate Coverage + Joint Injectivity

**Paths:** `05_papers/combinatorics/J34/{README.md, cover_letter.md, manuscript/manuscript.tex, manuscript/verify_J10.py}`

### Manuscript-level summary

The paper proves a clean sufficient condition for joint injectivity of partition pairs on squarefree Z/nZ with k ≥ 2 distinct prime factors:

- **Theorem 4.1 (Coordinate-Coverage Characterization, sufficient direction)** — If `D_f ∪ D_g = {p_1, ..., p_k}` then `J = (f, g)` is injective. Per-class computation of D_h is the substantive content (Lemmas 4.2 + 4.3 for additive-residue and multiplicative-orbit partitions).
- **Theorems A (M+M), B (A+M), C corrected (M+A), D (A+A)** — one-paragraph corollaries of Theorem 4.1 via the per-class D_h.
- **Example 6.1 (n=15 counterexample)** — `G = <2> ≤ (Z/15Z)*`, T_2-orbit of 5 = {5, 10} both ≡ 0 mod 5 → joint-injectivity failure despite `φ: G → (Z/5Z)*` being a bijection. Refutes a previously-asserted "φ injective" condition.
- **Theorem 7.1 (Refinement Trap)** — no pair in a single refinement chain achieves sufficiency unless one element is already π_disc.
- **Theorem 8.1 (MVJN(Z/30Z) = 1)** with two explicit witness pairs.

UOP (Unified Orthogonality Principle) has been demoted to Lemma 2.1 (joint-fiber characterization of partition meet) citing Birkhoff 1940 + Ore 1942 per SAVE_PLAN_J10. "Orthogonality" terminology dropped globally; replaced with "joint-fiber characterization", "coordinate coverage", "incomparable refinement".

Tier markers (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) are explicit in §1.1 of the manuscript and §5 of the README.

### Verify script

- `verify_J10.py` — PASS all three claim families: (A) n=15 counterexample confirming "φ injective" is necessary not sufficient; (B) MVJN(Z/30Z) = 1 with two witness pairs; (C) Theorem D small-n sanity (joint-injective on n=6 vs not joint-injective on n=30 for (π_2, π_3)). Runtime sub-second.

### README edits applied

- **Known-issues §extended** with four polish-pass observations:
  1. Verify script confirmed PASS on all three claim families.
  2. Notation harmonization needed: verify script and README §2 use π_6 as the first MVJN witness, but manuscript Theorem 5.1 / §8 names π_SPEC ("signed parity-3-residue"). Both are valid (π_6 is a concrete realization of π_SPEC) but the notation should harmonize before submission.
  3. Theorem 4.1 sufficient-direction proof is sound; necessity (converse) is honestly flagged as open. No math errors of the J08 type.
  4. Lemma 2.1 (joint-fiber characterization) correctly attributed to Birkhoff (1940) + Ore (1942).

### Known substantive issues (flagged for future user attention)

- **Theorem 4.1 necessity direction is open.** Only the sufficient direction is proven. Remark 3.4 and §9 honestly flag this; for ship, either tighten by finding a clean structural condition for the converse, or leave as an explicit open question with a one-paragraph remark.
- **Notation mismatch (π_6 vs π_SPEC).** verify_J10.py uses π_6 (= partition by residue mod 6) as W1; manuscript uses π_SPEC (signed parity-3-residue). Both are valid but should harmonize. Verify script comments lines 207–214 already note the substitution.
- Brayden's referee-rigor pass not yet complete.
- Per-venue cap check for EJC pending — J35 and J36 also target EJC; coordinate with VENUE_SCHEDULE.md.
- No paper-specific referee report in `_staging/referee_reports/` for J34 post-rewrite; a second-pass referee read may surface new issues.
- Theorem A bibliography note "to the best of our knowledge implicit in standard CRT" is honest but should be tightened with a search for prior publication before ship.

### Recommended target venue

**European Journal of Combinatorics** (unchanged from existing README assignment, per referee §9 explicit recommendation). Backup: *Discrete Mathematics*. The coordinate-coverage framing with the per-class D_h computation and the n=15 counterexample fit the EJC scope precisely. The per-venue cap with J35 / J36 is the operational concern.

### Tier 2 readiness verdict

**GOOD.** Math is sound, verify script passes, abstract is honest, Theorem 4.1 necessity direction is honestly flagged as open. The notation harmonization (π_6 vs π_SPEC) is a minor housekeeping issue. Ship-blockers are external (referee-rigor pass + EJC per-venue cap).

---

## Bottom line — three verdicts

| Paper | Verdict | Top action item |
|---|---|---|
| **J32** | **GOOD** | Brayden's referee-rigor pass; optional one-paragraph autotopism remark |
| **J33** | **NEEDS WORK** | Resolve the self-citation collision: re-label all "companion paper J33" references inside the J33 manuscript and cover letter (they refer to a different paper — the α-uniqueness PSLQ companion under post-2026-05-27 renumbering) |
| **J34** | **GOOD** | Brayden's referee-rigor pass; harmonize π_6 vs π_SPEC notation before submission |

All three are at "good Tier 2 standing" once their respective ship-blockers are resolved. J32 and J34 are ready for the referee-rigor pass; J33 needs the self-citation fix first.

---

## Files touched in this polish pass

- `05_papers/algebra/J32/README.md` — §1 file list corrected; Known-issues §extended with polish-pass observations.
- `05_papers/combinatorics/J33/README.md` — Known-issues §extended with polish-pass observations including the self-citation-collision ship-blocker flag.
- `05_papers/combinatorics/J34/README.md` — Known-issues §extended with polish-pass observations including the π_6 vs π_SPEC notation note.

No manuscript or verify-script content was changed.
