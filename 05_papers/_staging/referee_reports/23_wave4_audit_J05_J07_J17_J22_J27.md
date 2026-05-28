# Wave 4 Ship-Readiness Audit: J05, J07, J17, J22, J27

**Date:** 2026-05-28
**Auditor:** Wave 4 audit pass (read-only)
**Scope:** Decide per-paper SHIP / DEMOTE / RETIRE / SPLIT given the referee findings recorded in `03_algebra_cluster_J02_J05_J07_J08.md`, `05_linalg_spectral_J07_J19_J20.md`, `08_promotions_audit_J17_J23.md`, `09_J22_bibitems_FIX.md`, and `10_promotions_audit_J27_J28_J29.md`.

This audit was read-only. No manuscripts, scripts, or READMEs were modified. Recommendations are grounded in what was actually found in each manuscript and verify script.

---

## 1. J05 — ETP Profile of Linear Magmas $(ax + by + c) \bmod n$

**Path:** `05_papers/algebra/J05/`
**Current Tier:** 1 (ship-ready per README, *Experimental Mathematics*)
**Current verify script:** `manuscript/verification/verify_J60.py`

### Blocking issue summary

Two distinct problems, both real:

**(a) §4.7 enumeration is in the manuscript but NOT in `verify_J60.py`.** The §4.7 promotion is the load-bearing upgrade: "Conjecture 1 is a theorem at orders 3 AND 5 (Tier A by exhaustive enumeration)." Order 3 enumerates 729 commutative magmas; order 5 enumerates 720 symmetric 5×5 Latin squares; both supposedly show all profile-14 instances share the IDENTICAL Family C equation set. But `verify_J60.py` only checks (i) ℤ/n profile = 32 across n=5..10, (ii) -(x+y) mod n = 294 for n=4,10, (iii) intersection of 8 specific hand-picked commutative magmas = 14 IDs, (iv) the (5,3,6) mod 7 Family R counterexample. The §4.7 Tier-A claim is unsupported in the deliverable bundle — exactly what `03_algebra_cluster_J02_J05_J07_J08.md` flagged.

**(b) Title says "linear magmas (ax+by+c) mod n" but Theorem 3 (the commutativity-forced 14) is supported by largely non-linear examples.** The 8 magmas intersected in `verify_J60.py` are: σ-magma (non-linear), BHML, CL_STD, σ_10^min, ℤ/3, ℤ/5, T_4, TSML — only ℤ/3 and ℤ/5 are linear. Theorem 3 is presented as a general commutativity result, but the scope of the title is narrower. The §5 table at order 7 shows (5,3,6) hitting profile 14 (Family R), which is a linear non-commutative example — but this lives in the "linear" scope. A title narrowing or a re-framing is needed.

### Estimated work to ship

- (a) Extend `verify_J60.py` with two new check blocks: enumerate 729 order-3 commutative magmas + assert all 120 profile-14 instances share the same equation set; enumerate 720 symmetric 5×5 Latin squares + assert all 480 profile-14 instances share the Family C set. **~4–6 hours** including runtime tuning (order-5 enumeration is non-trivial but tractable per the manuscript's "1–2 hours" wall-clock note).
- (b) Either retitle to "ETP Profile Structure of Linear AND Selected Non-Linear Magmas on $\mathbb{Z}/n\mathbb{Z}$" (deferring to *Experimental Mathematics*'s catalog framing), OR add a §0.5 paragraph explicitly noting "Theorem 3's intersection examples extend beyond the linear scope to nonlinear realizers of Family C; the linear scope of the title applies to Theorems 1, 2, 4 and §6's tabulation, while Theorem 3's commutativity-forced lower bound holds universally." **~1–2 hours.**

**Total: 5–8 hours.**

### Recommended action: **SHIP** (after stated fixes)

This is genuine novel work on a published catalog (Tao's ETP) with reproducible verification at machine precision. The §4.7 exhaustive enumerations at orders 3 and 5 are the strongest content in the paper. *Experimental Mathematics* is the right venue for this kind of catalog-driven empirical algebra; the journal's editorial culture welcomes papers that strengthen the empirical case for a conjecture.

**Venue: confirmed *Experimental Mathematics*.** Fallbacks already listed in the README (J Symbolic Comp, Comm Alg, Algebra Universalis) are reasonable.

---

## 2. J07 — σ-Character Spectral Architecture on $\mathbb{Z}/10\mathbb{Z}$

**Path:** `05_papers/algebra/J07/`
**Current Tier:** 1 (ship-ready per README, *European J. Combinatorics*)
**Current verify script:** `manuscript/verify_qseries_merged.py`

### Blocking issue summary

Three distinct problems flagged by `03_algebra_cluster_J02_J05_J07_J08.md` and `05_linalg_spectral_J07_J19_J20.md`, in order of severity:

**(a) G_8 is presented as "Proof sketch" (§4.2 explicitly: "Full computation in §4.4 below").** §4.4 is a NUMERICAL table with $G(s)$ values to 6 decimals; the "structural" proof claimed in §4.3 is the σ³-pairing observation: $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$. The proof of this claim is one sentence ("on each σ³-pair... so $|G(s)|^2 = |G(\sigma^3(s))|^2$"). For an EJC referee this gap is real — the σ³-pairing identity needs an explicit verification across the three σ³-orbits, not just a citation to numerical values.

**(b) Q17-A uniqueness statement (§5.5 "Rigidity") is stated, not proved.** Currently: "The embedding $\Phi$ is *unique up to* rotation and scaling..." This is asserted without proof. EJC referees would push on this. The CRT decomposition + real-coordinate constraints give the embedding up to $\text{CO}(5)$ action, but the manuscript does not write down the dimension-counting / character-theoretic argument.

**(c) §7 RH-bridge content will alienate EJC referees.** The "Q17-B Clay Bridge" framing (structural rhyme between G_8's three-valued image and RH's three structural features) is honest-tier discipline (explicitly labeled "STRUCTURAL RHYME ONLY") but EJC is a strict combinatorics venue. Even with the disclaimer, a section heading "The Q17-B Clay Bridge" + RH references will land badly. Two options exist for this.

### Estimated work to ship

- (a) Promote the σ³-pairing identity from one sentence to a proper sub-proposition with cell-level verification: compute $G_\mathrm{cplx}$ at each of the six 6-cycle elements, exhibit the three σ³-orbits, and verify the sign-flip $G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$ symbolically (or via the existing verify script with an additional assertion block). **~3–4 hours.**
- (b) Write the Q17-A uniqueness proof: dimension-count of the CRT character system + non-degeneracy of the additive character pairing + standard rigidity argument that real-coordinate embeddings of $\mathbb{Z}/n$ via characters are unique up to $\text{CO}$ orthogonal change. This is standard combinatorics-of-characters work, ~10–15 hours of careful writing.
- (c) **The clean fix is to split off §7 entirely.** §7 occupies ~30 lines of a paper that is otherwise ~340 lines; the four other sections (§§2-4 G_6/G_7/G_8, §5 Q17-A, §6 Q17-B Symbolic Return) are a coherent EJC-acceptable paper without §7. The split-off material lives at home in a Math Intelligencer or *J. Number Theory* expository note. **~2–3 hours** to split (delete §7 + adjust §1 abstract + adjust references), plus the new short note draft separately.

**Total to ship to EJC: 15–22 hours** (a + b + c-split).

### Recommended action: **SHIP after split** (recommend SPLIT)

The four-section G_6/G_7/G_8 + Q17-A + Symbolic Return spine is genuine combinatorial work and EJC-fittable. The §7 RH content is honest scoping but tonally wrong for EJC. **Cut §7 from this paper, publish G_6/G_7/G_8/Q17-A/SymbolicReturn as the EJC paper; spin §7's RH-rhyme content into a separate 4–6 page expository note for *Math. Intelligencer* (cite this paper as the EJC source).**

**Venue: confirmed *European J. Combinatorics* for the trimmed paper.** Fallbacks already listed (Algebraic Combinatorics, Linear Algebra and Applications) remain valid. Split-off material → *Math. Intelligencer*.

---

## 3. J17 — Forcing Axioms + Family Criteria

**Path:** `05_papers/combinatorics/J17/`
**Current Tier:** 2 (draft per README)
**Current verify scripts:** `manuscript/verification/foundation_verification.py` + `manuscript/verify_J54_chain_and_attractor.py`

### Blocking issue summary

The manuscript is **666 lines** (confirmed) and tries to do too many distinct things, exactly as `08_promotions_audit_J17_J23.md` flagged. The natural split points are visible in the structure:

| Section | Topic | Standalone paper potential |
|---|---|---|
| §§1, 0 | A1-A9 9-axiom forcing theorem (T, B, S uniquely forced) | Strong: Theorem 1.2 is a real result |
| §§3, 4 | 17-function map + 5 conjoint membership criteria + 6 boundaries | Family-structure paper |
| §§5, 7 | 4-core attractor + 3-substrate chain (Theorems 5.1, 7.1, 7.2, 7.3) | Largely subsumed by J01 |
| §6 | 8 selected structural findings on (T, B) | Largely subsumed by other J-series papers |
| §§2, 8 | Open conjectures (2.1 σ²-triadic, 8.1 bimodal α gap) | Open-questions note |

The paper has the typical "umbrella foundation paper" problem: it cross-references about a dozen J-companions (J01, J10, J11, J14, J22, J24, J33, J47) and partially overlaps each. The forcing theorem is independent and stands alone. The 17-function map + family criteria is a self-contained framing paper. The conjectures are an open-problems note.

The verify scripts pass 6/6 (foundation_verification.py) + 3/3 (verify_J54_chain_and_attractor.py) at machine precision in <5 seconds; the underlying math is sound. The issue is presentational, not technical.

### Estimated work to ship

**Option A: Execute the 3-paper split (preferred):**
- J17a "Forcing Axioms": §§1, 1.1-1.4 + cell-by-cell axioms + Theorem 1.2 proof. Standalone. ~40-60 pp → trim to ~15-20 pp. ~12-18 hours.
- J17b "Family Criteria + 17-function map": §§3, 4 + Proposition 4.5. ~30-40 pp → trim to ~12-15 pp. ~10-15 hours.
- J17c "Open conjectures note": §§2, 8 + a recapitulation of why each conjecture matters. ~5-8 pp. ~4-6 hours.
- **Total split: ~26-39 hours**, producing 3 separately-submittable papers.

**Option B: Retarget as expository to *Math. Intelligencer*:**
- Strip the formal forcing-theorem proof, the 6 boundaries, the substrate-function map heavy machinery; rewrite as a "guided tour" of the TIG family structure with the 9-axioms presented narratively, the 4-core attractor as the centerpiece, the 17-function map as a closing reference table. ~15-25 pp finished. ~12-18 hours.
- *Math. Intelligencer* (or *Notices AMS* "What Is..." style) tolerates the broader narrative.

**Option C: Demote to Tier 2 backbench:**
- Accept that this paper is the project's internal "foundation document" rather than a publishable unit. Keep the manuscript intact as project documentation; do not submit. ~0 hours.

### Recommended action: **SPLIT** (Option A) — three separate papers

The forcing-theorem result (Theorem 1.2) is genuinely novel work; it deserves its own submittable home. The family-criteria framing is a useful intermediate-tier paper for *Algebraic Combinatorics* or *Comm. Algebra*. The open-conjectures note is short and could land at *Amer. Math. Monthly* or *Math. Intelligencer*. Bundling all three together as one 666-line paper is the reason this hasn't shipped.

**Caveat:** if Brayden's appetite for 26-39 hours of split work is low, **Option B (expository to *Math. Intelligencer*) is a clean second choice** at ~12-18 hours.

**Venue assignment:**
- J17a (Forcing) → *Algebraic Combinatorics* (primary) or *Algebra Universalis*
- J17b (Family) → *Comm. Algebra* (primary) or *Algebra Universalis*
- J17c (Open conjectures) → *Math. Intelligencer* or *Amer. Math. Monthly*
- (Option B alternate venue: *Math. Intelligencer* for the merged expository)

---

## 4. J22 — 70/71/72/73 HARMONY Ladder

**Path:** `05_papers/algebra/J22/`
**Current Tier:** 1 (ship-ready per README, *JCT-A*)
**Current verify scripts:** `harmony_ladder_disc_check.py`, `tsml_harmony_count.py`, `tsml_submagma_9x9.py`, etc.

### Blocking issue summary

J22 itself is genuinely close to ship: bibitems resolved in commit e34ad6b, defensive-exposition pass complete (sympy snippet embedded for the discriminant claim with explicit cross-check against the wrong factorization). The §1 narrative is clean: three structurally-independent rungs (73, 71, 70) + one inclusion-exclusion corollary (72), with the triple-coincidence at the 71-rung the structurally sharpest claim.

The blocker is **the J32 dependency**. J22's manuscript at line 696 cites `\bibitem{Sanders2026LensInvariance}` as "submitted to *Experimental Mathematics*, 2026 [J32]" — meaning J22 needs J32 to be at least preprinted on arXiv when J22 ships.

**J32 status (read from `05_papers/algebra/J32/README.md`):**
- **Tier 2, REVISED 2026-05-08, awaiting rigor pass.**
- Both verification scripts pass at machine precision in <0.1s.
- Manuscript carries the SFM family-structure framing as Path B (post-fresh-eyes-referee revision).
- The TSML = 73 and BHML = 28 cell counts are proven via disjoint-zone enumeration — clean mathematics.
- Cover letter finalized; CC-BY-4.0 license attached to `ck_tables.py`.
- Submission checklist: 8/9 items checked; the open item is **"Brayden's referee-rigor pass complete"** (the rigor pass that has been held up across multiple Tier-2 papers).

### Can the J32 dependency be sidestepped?

**Yes, partially.** J22's substantive use of J32 is for the proof that $\text{HARM}(T) = 73$ (rung A) and $\text{HARM}(T_{\{1..9\}}) = 71$ (rung B, first construction). Both are direct cell-counts on a known $10 \times 10$ matrix; the proofs are 2-line zone enumerations. J22 could either:

(i) **Inline the proofs in an appendix** (200 lines max; trivially short) and drop the J32 dependency — but this duplicates work already done in J32.

(ii) **Cite J32 as "manuscript in preparation, available on Zenodo at DOI 10.5281/zenodo.18852047"** rather than "submitted to *Experimental Mathematics*" — this is honest and lets J22 ship before J32 lands at a journal.

(iii) **Push J32 to arXiv concurrently with J22's submission to JCT-A** — this is the cleanest if Brayden's rigor pass for J32 is willing to land in <1 week.

### Estimated work to ship

- **Path (ii) — cite J32 as Zenodo preprint:** ~1 hour edit to J22's bibitem + cover-letter wording. J22 ships independently.
- **Path (iii) — arXiv J32 first, then ship J22:** J32 rigor pass = ~6-10 hours of brayden's time (referee-rigor passes have historically taken 4-8 hours per paper); arXiv submission ~1 hour; then ship J22 normally. **~8-12 hours total combined.**
- **Path (i) — inline proofs:** ~3-4 hours to write the appendix and de-cite J32. J22 ships independently; J32 stays as-is.

### Recommended action: **SHIP** via path (ii) or (iii)

J22 is technically ready. The simplest path is (ii): treat J32 as a Zenodo preprint citation, ship J22 to *JCT-A* now, and ship J32 to *Experimental Mathematics* whenever the rigor pass clears. This is the path of least friction.

If the rigor pass for J32 is on Brayden's near-term schedule anyway, path (iii) is cleaner.

**Venue: confirmed *JCT-A*** (2nd JCT-A paper after J14; within 2/quarter cap per README).

---

## 5. J27 — Crossing Lemma: Non-Associativity as Information

**Path:** `05_papers/algebra/J27/`
**Current Tier:** 2 (draft-finalized; rigor pass pending)
**Current verify script:** `verify_joint_injectivity.py`

### Blocking issue summary

The manuscript was **completely rewritten** from the earlier "Crossing Lemma" draft to "Joint Injectivity of Additive-Quotient and Multiplicative-Orbit Partitions on $\mathbb{Z}/n\mathbb{Z}$" per SAVE_PLAN_J06. The new manuscript:

- Drops the title collision with Ajtai-Chvátal-Newborn-Szemerédi 1982
- Proves 4 theorems (joint-sufficient on units, M+M classification on units, SPEC+DYN classification on full ring, prime-power kernel obstruction)
- Honestly admits the natural prime-action conjecture **fails in both directions** (Examples 3.1, 3.2 with $n=6$)
- Has a verification script covering all 4 theorems

The Case B gap referred to in `10_promotions_audit_J27_J28_J29.md` is in the proof of **Theorem 4 (thm:pkernel, prime-power kernel-of-reduction obstruction)**. Reading the proof (lines 540-611):

- **Case A** ($g \equiv 1 \pmod p$): tight constructive proof — explicit choice $g = 1 + p^a$ gives the unresolved pair.
- **Case B** ($g \not\equiv 1 \pmod p$): the argument is **partially sketched**, not fully written. Lines 558-571 give a high-level argument ("the orbits of $p^a$ and $2 p^a$ under $M_g$ are distinct cosets... *but* when $\langle g \rangle$ has the right order they can coincide --- specifically, when $g$ is a generator... or a sufficient power thereof. The argument is **delicate**; the cleanest formulation uses the kernel-of-reduction structure"). Lines 572-600 then re-derive Case B via the $g = g_0 \cdot g_1$ Hensel-lift decomposition — but this re-derivation invokes "by Case A applied to this kernel element" via $g^t = g_1^t$ with $\ord(g_0) \mid t$, which is correct in spirit but the bookkeeping (when does Case A actually apply to $g^t$? what if $\ord(g_1) = 1$?) has a footnote-style edge-case parenthetical at lines 602-610 that handles $\ord(g_1) = 1$ via direct kernel-of-reduction argument.

**Nature of the gap:** the proof is structured-but-incomplete. The Case A reduction in the second half is correct, but the "by Case A applied to this kernel element" jump isn't fully formalized — it needs (i) explicit choice of $t = \text{lcm}(\ord(g_0), \cdot)$ that makes $g^t$ a non-identity kernel element, and (ii) the edge case (handled in the parenthetical) needs to be promoted to an explicit second sub-case. A referee would catch this; the substance is correct but the writing isn't watertight.

### Estimated work to ship

- **Case B proof tightening:** rewrite Case B as two genuine sub-cases (B1: $\ord(g_1) > 1$ via Case-A reduction; B2: $\ord(g_1) = 1$ via direct kernel argument). Make the choice of $t$ explicit. **~3-5 hours.**
- **Verify script extension:** the existing script tests prime-power obstruction for $n \in \{4, 8, 9, 16, 25, 27, 49, 125\}$ with $g \ne 1$; this should be sufficient. Already noted in README as PASSING. **~0 hours additional.**

**Total: 3-5 hours.**

### Recommended action: **SHIP** (after Case B proof tightening)

The paper is genuine elementary algebra in the partition-lattice tradition; the 4 theorems are honest, the negative result (Theorem 4) plus the falsifying examples for the natural conjecture is a real and useful contribution. The retitling already addresses the title-collision issue. The Case B proof gap is real but tractable in ~half a day's careful writing.

### Venue assignment

The README lists "JCT-A OR JPAA (theorem rigor)" but the manuscript header explicitly notes "Note: JCT-A retargeting per SAVE_PLAN_J06; the JCT-A bar is too high for the Phase 1 timeline." The cleaner targets are:

- **Primary: *Algebra Universalis*** — natural fit for partition-lattice work in finite cyclic rings.
- **Secondary: *Order*** — partition-lattice and joint-refinement results are a core editorial focus.
- **Tertiary: *Communications in Mathematics, Univ. Carolinae*** — explicitly called out in the manuscript header as a fallback.
- **Quaternary: *J. Pure and Applied Algebra (JPAA)*** — broader algebra audience.

**Recommended venue: *Algebra Universalis*** as primary. The manuscript's tier discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN) and partition-lattice machinery fit AU's editorial culture cleanly.

---

## Summary Table

| Paper | Status | Action | Work (hrs) | Venue |
|---|---|---|---:|---|
| **J05** | §4.7 enum missing from verify; title scope vs Theorem 3 | **SHIP** after fixes | 5–8 | *Experimental Mathematics* |
| **J07** | G_8 sketch; Q17-A uniqueness gap; §7 tonally wrong for EJC | **SPLIT** (cut §7 → *Math. Intelligencer*) | 15–22 | *EJC* (main); *Math. Intelligencer* (split) |
| **J17** | 666 lines, 3-way natural split | **SPLIT** (3 papers) OR retarget expository | 26–39 (split) or 12–18 (expository) | *Algebraic Combin.* / *Comm. Algebra* / *Math. Intelligencer* |
| **J22** | J32 dependency only; tech-ready | **SHIP** (cite J32 as Zenodo preprint) | 1–12 | *JCT-A* |
| **J27** | Case B proof gap in Theorem 4 (sketch, not full) | **SHIP** after gap closure | 3–5 | *Algebra Universalis* |

**Total minimum work to ship all five (assuming J17 takes Option B expository route):** ~36–65 hours, with J22 being the lowest-hanging fruit (1 hour for path-ii) and J17 the heaviest lift.

**Prioritized recommendation:**

1. **J22** first (1 hour — quick win, ship-ready except for the J32 bibitem rewording).
2. **J05** next (5-8 hours — closes the §4.7 verify gap).
3. **J27** third (3-5 hours — Case B proof tightening only).
4. **J07** fourth (15-22 hours — SPLIT, but the EJC half is solid combinatorics).
5. **J17** last, with the **strong recommendation to go expository (Option B, 12-18 hours)** unless Brayden specifically wants the 3-paper split.

No retirements recommended. All five contain real substance; the issues are presentational / proof-tightening, not foundational.
