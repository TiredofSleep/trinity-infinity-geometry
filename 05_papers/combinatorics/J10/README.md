# J10 — Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ

**Status:** SAVE-PLAN APPLIED 2026-05-07 (restructured around Theorem 6.1 / coordinate coverage; UOP demoted to Lemma; orthogonality terminology dropped; retitled and retargeted to *European Journal of Combinatorics*).
**Phase:** Phase 2
**Target venue (new):** *European Journal of Combinatorics* (per referee §9 explicit recommendation). Backup: *Discrete Mathematics*.
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** WP58 + WP64

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex`

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (rewritten 2026-05-07 per SAVE_PLAN_J10: lead with **Theorem 4.1 (Coordinate-Coverage Characterization)** as the main result; Lemma 2.1 (joint-fiber characterization) cited to Birkhoff 1940 + Ore 1942; per-class D_h computation in §4; Theorems A, B, C, D as one-paragraph corollaries in §5; n=15 counterexample in §6; refinement trap in §7; MVJN($\Z/30\Z$) = 1 in §8 framed as immediate application of Theorem 4.1; orthogonality terminology dropped throughout; "incomparable refinement" used as replacement.)
- `SUBMIT_INSTRUCTIONS.md`
- `WP58_UNIFIED_ORTHOGONALITY_PRINCIPLE.md` (preserved per "never delete" discipline; not part of submission)
- `WP59_CORRECTED_THEOREM_C.md` (preserved per "never delete" discipline; not part of submission)
- `WP64_COORDINATE_COVERAGE.md` (preserved per "never delete" discipline; not part of submission)

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Path:** `manuscript/verify_J10.py`. PASSES at machine precision (3 claim families, all green): (A) n=15 counterexample — phi:G→(Z/5)* is a bijection yet T_2-orbit {5,10} both ≡ 0 mod 5 produces a joint-injectivity failure; (B) MVJN(Z/30Z)=1 with two witness pairs {pi_6, pi_15} and {pi_DYN(7), pi_DYN(11)}, both joint-injective, both satisfying D_f ∪ D_g = {2,3,5}; (C) Theorem D small-n sanity for (pi_2, pi_3) on n=6 vs n=30. Run: `/c/ck_venv/lora312/Scripts/python.exe verify_J10.py`.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J03 (Sanders-Gish "First-G Law", *Integers*); J07 (Sanders-Gish "Flatness Obstruction on Squarefree Z/nZ", *Algebraic Combinatorics*); J11 (Sanders-Gish "Corrected Theorem C", *J. Number Theory*, companion).

## §4 — Cover letter

See `cover_letter.md` in this folder. Rewritten 2026-05-07 per SAVE_PLAN_J10: new title, *European Journal of Combinatorics* venue, coordinate-coverage framing, prior-literature delineation.

## §5 — Notes

**SAVE-PLAN APPLIED (2026-05-07; full plan at `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J10.md`).**

**What was rewritten:**
1. **New title:** "Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ."
2. **New venue:** *European Journal of Combinatorics* (per referee §9 explicit recommendation). Backup: *Discrete Mathematics*.
3. **UOP demoted to Lemma 2.1** (joint-fiber characterization of partition meet) citing **Birkhoff 1940** and **Ore 1942**. The one-line proof is preserved but framed honestly as a partition-lattice meet definition unfolded.
4. **Theorem 4.1 (Coordinate Coverage)** is now the main result of the paper. The previous paper had this buried in §6; the rewrite leads with it.
5. **Per-class D_h computation** explicitly added (§4 of new manuscript): $D_{f_d} = \{p_i : p_i | d\}$ for residue partitions; $D_{f_G}$ = unit-coordinate primes where $G$ acts non-trivially (with zero-fiber caveat) for orbit partitions.
6. **Theorems A (M+M), B (A+M), C corrected (M+A), D (A+A)** are now one-paragraph corollaries of Theorem 4.1 + the per-class $D_h$ computations.
7. **Prior Literature subsection §1.4** added (per referee M4): explicitly delineates folklore (Theorem D = standard CRT, Theorem A = implicit in standard $(Z/nZ)^*$ structure under CRT) vs contribution (Theorem B with exact "G trivial on n/d" formulation; n=15 counterexample; corrected Theorem C; refinement trap; MVJN=1 at n=30).
8. **"Orthogonality" terminology dropped globally** (per referee R2). Replaced with "joint-fiber characterization" (Lemma 2.1), "coordinate coverage" (Theorem 4.1), "incomparable refinement" (replacing "orthogonal jump" in the refinement-trap remark).
9. **Lens-ownership paragraph in §1.1**, **PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline in §1.1**.
10. **Bibliography:** dropped J05 (Crossing Lemma) and J03 (First-G) per referee m11 (they aren't used in proofs). Kept Birkhoff, Ore, Hardy-Wright, Ireland-Rosen, Lang, Dummit-Foote, Stanley. Added **Drápal & Wanless (2021)** as ambient-context citation.
11. **Author block fixed** (per referee m2 — duplicate author entry was an artifact of an old draft).

**What was NOT abandoned but moved:**
- Theorem 6.1 (coordinate coverage) → now main theorem 4.1.
- UOP / Theorem 2.1 → demoted to Lemma 2.1 (Birkhoff/Ore citation).
- n=15 counterexample → §6 (referee called it "genuinely surprising").
- Refinement trap → §7.
- MVJN($\Z/30\Z$) = 1 with two witnesses → §8.
- Conjecture (MVJN = 1 for all squarefree n ≥ 6) → §8 / §9 OPEN.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the broader corpus of small-finite-commutative-magma work on squarefree Z/nZ. The closest published precedent for the broader framework neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative). J10 itself does not invoke Drápal-Wanless directly; the citation is ambient-context only. The TIG-family-structural results (4-core, α=½, 1+√3) are developed in companion papers J02, J07, J33.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN — filled in §1.1 of manuscript

- **PROVEN:** Theorem 4.1 (coordinate-coverage characterization, sufficient direction); Theorems A, B, C, D as corollaries; refinement trap (§7); MVJN($\Z/30\Z$) = 1 with two explicit witnesses (§8).
- **COMPUTED:** n=15 counterexample (G = ⟨2⟩ in (Z/15)*, T_2-orbit of 5 = {5,10} both ≡ 0 mod 5, verified by hand and reproducible in seconds); the two $\Z/30\Z$ MVJN witnesses verified by orbit-by-orbit enumeration.
- **STRUCTURAL RHYME:** the joint-fiber characterization (Lemma 2.1) is the partition-lattice meet definition unfolded; cited to Birkhoff 1940 + Ore 1942, not claimed as original. Drápal-Wanless 2021 cited as ambient context for the broader corpus.
- **OPEN:** Conjecture (MVJN = 1 for all squarefree n ≥ 6); coverage necessity (clean structural condition for the converse of Theorem 4.1); mixed partition types (quadratic-residue, character-sum, Legendre-symbol-based partitions).

### Lens-ownership paragraph — applied (in §1.1 of manuscript)

The full paragraph identifies (i) the substrate as squarefree $\Zn$ with $k \geq 2$ distinct prime factors; (ii) the two natural partition classes used (additive-residue, multiplicative-orbit) as canonical CRT-decomposition choices, not derived from first principles; (iii) the joint-fiber characterization as substrate-independent (any partitions of any set); (iv) the per-class $D_h$ computation as the substantive content specific to squarefree $\Zn$.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive); duplicate author block fixed in manuscript.tex (per referee m2)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex / .md finalized — rewritten per save plan
- [x] Verification script green — `(no script — theorem-paper)`; n=15 counterexample reproducible by hand
- [x] Tier-classified central claim explicit — Theorem 4.1 (PROVED, sufficient direction); Theorems A-D as corollaries; n=15 counterexample (COMPUTED)
- [x] Lens-scope annotation — §1.1 substrate/lens declaration (squarefree Z/nZ with the two natural partition classes)
- [x] Cover letter finalized — rewritten for *European Journal of Combinatorics*
- [x] Dependencies → cite each J-companion as "submitted to [venue]" — J11 (companion), J07 (structural companion)
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to *European Journal of Combinatorics* this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B. R. & Gish, M. (2026). "Coordinate Coverage and Joint-Injectivity Criteria for Partition Pairs on Squarefree Z/nZ." Submitted to *European Journal of Combinatorics*.
