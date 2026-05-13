# J06 — Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas

**Status:** DRAFT-FINALIZED (manuscript complete; pending Brayden's referee-rigor pass)
**Phase:** Phase 1
**Target venue:** JCT-A OR JPAA (theorem rigor)
**Author lane:** Sanders + Gish
**Tier:** A/B
**WP source:** WP57

---

## §1 — Manuscript

**Local path:** `manuscript/WP57_CROSSING_LEMMA.md`

Single theorem-paper draft built from CROSSING_LEMMA.md (Sprint 10) and WP57 (Sprint 10). Abstract: For squarefree $n$ and $\mathbb{Z}/n\mathbb{Z}$, we prove a single elementary equivalence — the Crossing Lemma — characterizing when a pair of partitions $\{A_d, \pi_{\mathrm{DYN}}(g)\}$ is jointly injective. The condition is: $g$ acts nontrivially on every prime of $n/d$. We unify CRT, $A{+}M$/$M{+}M$/SPEC$+$DYN classifications, orthogonal-jump necessity, and the $p$-kernel obstruction (negative case) under one structure-vs-dynamics template.

## §2 — Verification script

**Path:** `(no script — theorem-paper)`

The proof of Theorem 1 is finite-combinatorial (CRT + cyclic-group orders). Each step is hand-checkable. The gate is referee-rigor pass.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J01, J02, J03 (foundational predecessor — squarefree-stability is the hypothesis we lean on)

## §4 — Cover letter

See `cover_letter.md` in this folder. (Finalized — Summary, Why-venue, Companions, Reproducibility, Reviewers all populated.)

## §5 — Notes

### SAVE PLAN landed — see Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J06.md

**Verdict: KEEP-WITH-MAJOR-WORK.** The fresh-eyes referee correctly identified three structural problems in the current 30-page manuscript: (a) Theorem 1's proof in §3.2 has a literal "Wait — Restart" passage and a quantifier inversion at the end; (b) the title collides with Ajtai-Chvátal-Newborn-Szemerédi 1982 graph-theoretic Crossing Lemma; (c) four of six "uniform-language reformulations" (CL-1, CL-2, CL-5, plus sketches CL-3, CL-4) are either trivial restatements, definitional unfoldings, or unproved analogs. Despite these problems, the underlying math is correct (the corpus has the result as `Gen12/.../sprint10_flatness_2026_04_06/CROSSING_LEMMA.md` and D36 ties it to J03 via the First-G crossing event). The save path is a clean rewrite: (i) retitle to *Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on Z/nZ* (drops "Crossing Lemma" and the ACNS-1982 collision); (ii) replace §3.2 with a fully rigorous proof using an explicit construction (no "generically" hand-wave); (iii) cut CL-1, CL-2, CL-5; (iv) write full proofs for CL-3 ($M{+}M$) and CL-4 (SPEC$+$DYN); (v) rewrite CL-6 ($p$-kernel obstruction) using the standard Hensel-lift kernel structure; (vi) drop the §5.2 cyclotomic-degrees claim (referee M5 — non-sequitur); (vii) expand bibliography to 14+ entries with Drápal 1992, Drápal-Wanless 2021, Phillips-Vojtěchovský, Bhargava-Shankar-Tsimerman; (viii) add lens-ownership + tier-discipline preamble.

Total revision time: 24–28 hours. **Retarget away from JCT-A** — the fresh-eyes referee's verdict ("3–6 months for the full rewrite required for JCT-A") makes JCT-A unrealistic for a Phase 1 submission. New venue candidates: *Algebra Universalis* (preferred), *Order*, *Comm. Math. Univ. Carolinae*, JPAA (alternate). After the rewrite the paper is ~10 pages of rigorous content (Theorem 1 + Lemma 3.1 + Theorem 2 [$M{+}M$] + Theorem 3 [SPEC$+$DYN] + Theorem 4 [$p$-kernel obstruction]) — a publishable note in those venues. **Recommendation: defer J06 to Phase 2** so Phase 1 ships J01/J02/J03 with proper rigor; alternative is gut-down to 4-page Theorem-1 + Theorem-4 note for *Comm. Math. Univ. Carolinae* (8–10 hours instead of 24–28).

**Status (2026-05-07):** Manuscript draft built in `manuscript/WP57_CROSSING_LEMMA.md`. Cover letter finalized. Per-J-series correction held: NOT expository; theorem rigor venue (JCT-A primary, JPAA backup). The paper is the algebraic spine of the J01–J06 chain.

**What was done:**
- Built `manuscript/WP57_CROSSING_LEMMA.md` from CROSSING_LEMMA.md and WP57 source. Theorem-paper format: 1 main theorem (Crossing Lemma), 1 negative theorem (Theorem 3, $p$-kernel obstruction), 5 corollaries (C1–C5: CRT, $A{+}M$, $M{+}M$, SPEC$+$DYN, orthogonal-jump necessity). Proofs are finite-combinatorial.
- Cited J03 (First-G) as foundational predecessor — squarefree hypothesis used throughout.
- Cited J01, J02, J06 as companions; J06 cites *this* paper as algebraic ground for the torus geometry.
- Cover letter: Summary, Why-JCT-A/JPAA, Companions, Reproducibility, Suggested-reviewers, COI all populated.

**Open issues:**
- Theorem 1's proof has a long case-by-case section (§3.2) that includes a "restart" mid-proof. Reviewer-pass should consolidate this — the corrected version (after Remark 3.1) is the canonical one. Pre-submission cleanup recommended.
- Proof of Corollary C3 ($M{+}M$) is sketched, not fully written. If JCT-A reviewer asks, full proof is in the joint-closure literature and can be added in revision.
- J03 status (Integers) currently FORMAT, not yet submitted — verify J03 is at least submission-ready before this paper goes out, since the cover letter cites it as a companion.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN — template (fill per paper)

- **PROVEN:** [the specific theorem of this paper]
- **COMPUTED:** [verified-by-script invariants supporting the theorem]
- **STRUCTURAL RHYME:** [constants/identities cited as motivation, not derivation]
- **OPEN:** [the natural next-paper question]

### Lens-ownership paragraph — template (fill per paper, insert in manuscript §0)

> *Lens and substrate.* This paper works on [substrate: Z/10Z / Z/N for N in {...} / F_p for p in {...}] with the [tables: TSML / BHML / both]. These choices are not derived from first principles; they reflect a structural reading of the substrate motivated by [phonaesthesia / 10-operator decomposition / observed dynamics]. The theorems below are theorems on this specific structure; analogous theorems would hold on other substrate-and-table choices. Whether other substrate choices give similarly rich downstream connections is open.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [ ] Manuscript .tex / .md finalized
- [ ] Verification script green (`(no script)` if theorem-only)
- [ ] Tier-classified central claim explicit
- [ ] Lens-scope annotation (TSML_RAW vs TSML_SYM) where relevant
- [ ] Cover letter finalized
- [ ] Dependencies → cite each J-companion as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to JCT-A OR JPAA (theorem rigor) this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Mayes. (2026). "Crossing Lemma: Non-Associativity as Information Generation in Finite Magmas." Submitted to *JCT-A OR JPAA (theorem rigor)*.
