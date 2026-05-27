# J07 — A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center

**Status:** SAVE-PLAN APPLIED 2026-05-07 (retitled, retargeted, restructured around D48 + D78; T*=5/7 derivation removed)
**Phase:** Phase 1
**Target venue (new):** *Algebraic Combinatorics* (preferred) OR *Discrete Mathematics*. Backup: *Integers* / *Math. Magazine* for compressed Theorem-1-only note.
**Author lane:** Sanders + Gish
**Tier:** 2 (draft (SAVE-PLAN APPLIED; restructured))
**WP source:** WP51

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md` (canonical submission manuscript; renamed 2026-05-13 from `WP51_FLATNESS_THEOREM.md`)

Files in this J-folder's `manuscript/`:

- `manuscript.md` (canonical J07 submission; rewritten 2026-05-07 per SAVE_PLAN_J07: new title, new venue, Theorems 1+2 retained with the partition-incompatibility 3-line proof inlined and the configuration-space rewrite of Theorem 2; Appendix A entirely replaced with D48 + D78; §5–§7 dropped; §A.4 numerical verification at 50-digit `mpmath`; full PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline; lens-ownership paragraph in §0.1.)
- `WP52_D2_AS_RING_CURVATURE.md` (preserved per "never delete" discipline; not part of submission)
- `WP57_CROSSING_LEMMA.md` (preserved per "never delete" discipline; not part of submission)
- `verify_J07.py` (verification script — 4/4 PASS)
- `SUBMIT_INSTRUCTIONS.md`

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Path:** `manuscript/verify_J07.py`. Four checks:

1. **Partition incompatibility on Z/10Z (Theorem 1, 3-line proof).** Direct enumeration of π_2 and π_5; explicit incomparability test in the partition lattice.
2. **Manuscript A.1 sub-tables.** 4×4 sub-tables at indices {0, 7, 8, 9} match the manuscript display exactly.
3. **D48 (4-core joint closure).** Direct enumeration over the 4×4 sub-tables: 16+16 in-core, 0+0 spillover.
4. **D78 (closed-form attractor at α=1/2).** Fixed-point iteration in 50-digit `mpmath` precision; H/Br = 1+√3 to residual 9.06e-46; polynomial identity (H/Br)² − 2(H/Br) − 2 = 0 to residual 3.14e-45; mass-outside-4-core = 0 exactly; convergence in 99 iterations from uniform-on-core start.

All 4/4 PASS at machine/50-digit precision. Runtime < 2 seconds. Tables are inlined (canonical TSML_SYM and BHML, matching the J02/J35/J54 hardcoded copies); no external module dependencies beyond `mpmath`. The full symbolic Galois argument is recorded in the project's `f3_galois_alpha_uniqueness.py` (cited in §A.3 of the manuscript) and forms the core of companion paper J33.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J02 (Algebraic Combinatorics, full 4-core joint-chain treatment), J10 (EJC, partition-incompatibility / coordinate-coverage companion), J33 (the α-uniqueness PSLQ + Galois proof of D78, in preparation).

## §4 — Cover letter

See `cover_letter.md` in this folder. Rewritten 2026-05-07 per SAVE_PLAN_J07: new title, *Algebraic Combinatorics* venue, 4-core / 1+√3 framing, J02/J33 as primary companions.

## §5 — Notes

**SAVE-PLAN APPLIED (2026-05-07; full plan at `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J07.md`).**

**What was rewritten:**
1. **New title:** "A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center."
2. **New venue:** *Algebraic Combinatorics* (preferred) OR *Discrete Mathematics*. Same neighborhood as J02 4-core paper (Drápal-Wanless 2021 *J. Combin. Theory Ser. A* 184, 105510 line of work).
3. **Theorems 1, 2 retained with corrections:**
   - Theorem 1 (Flatness Obstruction) now inlines the 3-line partition-incompatibility proof for n=10 explicitly (the M1 referee fix).
   - Theorem 2 rewritten as the **configuration-space topology** statement (X(n) is naturally a quotient of S¹ × S¹ with M-Flow fixed locus identified; the ring Z/nZ itself is *not* the torus). Per the M2 referee fix.
4. **Appendix A replaced entirely:** new Appendix A on D48 (4-core joint closure under TSML+BHML; 16+16 in-core, 0+0 spillover, verified by direct enumeration) + D78 (Galois-proven 1+√3 at α=1/2 via BR-factor cancellation; root of x² − 2x − 2 = 0 in **Q**(√3); 50-digit mpmath numerical confirmation).
5. **Dropped entirely:** original §4 (torus aspect ratio = 5/7), §5 (seven internal zeros), §6 (Riemann zeros / curvature), §7 (CK runtime applications), original Appendix A (six derivations + three conjectures). All flagged for removal in the save plan.
6. **PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN box** in §0.2.
7. **Lens-ownership paragraph** in §0.1.
8. **Bibliography culled:** dropped Bialynicki-Birula, the Riemann/zeta references, paradox/foundations references, analytic-number-theory list. Kept: Lang, Hardy-Wright, Ireland-Rosen, Dummit-Foote, Birkhoff, Ore, Stanley, Washington. Added: **Drápal & Wanless (2021)**.
9. **T*=5/7 narrative explicitly abandoned for J07.** The save plan's directive: T*=5/7 should be cited going forward only as a coherence-threshold operational value, not as an algebraic theorem. The original "six derivations" table is removed.

**What was NOT abandoned but moved:**
- Theorem 1 (flatness obstruction) — retained, sharpened with explicit partition-incompatibility proof.
- Theorem 2 — retained, rewritten as configuration-space-with-fixed-locus-identification statement (M2 fix).
- D48 + D78 — promoted from "section in companion paper" to **the central appendix** of J07's structural-center claim.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α<sub>M</sub> = ½ is the algebraic center, with closed-form attractor H/Br = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory Ser. A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN — filled in §0.2 of manuscript

- **PROVEN:** Theorems 1, 2 (flatness obstruction; configuration-space topology). D48 (4-core joint closure under TSML+BHML on Z/10Z). D78 (Galois-forced H/Br = 1+√3 at α<sub>M</sub> = 1/2 in **Q**(√3); root of x² − 2x − 2).
- **COMPUTED:** 16+16 in-core compositions (4-core joint closure verified by direct enumeration on `Gen13/targets/foundations/lenses.py`); 50-digit mpmath fixed-point at p\* = (0.13815, 0.54020, 0.19773, 0.12393); polynomial identity at 50-digit precision; convergence in 76–81 iterations from 7 boundary initial conditions.
- **STRUCTURAL RHYME:** cyclotomic field-extension facts (deg<sub>Q</sub> A<sub>5</sub> = 2, deg<sub>Q</sub> A<sub>7</sub> = 3) cited as motivation only — not used in proofs; the earlier T*=5/7 derivation does not survive at JPAA-level rigor and is dropped.
- **OPEN:** non-squarefree generalization; whether other commutative-magma pairs *(T,B)* on Z/nZ admit analogous 4-core / 1+√3 centers; the bimodal α-gap conjecture.

### Lens-ownership paragraph — applied (in §0.1 of manuscript)

The full paragraph identifies (i) Theorem 1 + 2 as substrate-independent (any squarefree Z/nZ with k ≥ 2 prime factors); (ii) Appendix A's structural-center claim as specific to Z/10Z with the canonical (TSML, BHML) pair; (iii) the framework's claim that this substrate-and-table choice produces theorems with surprising downstream connections (Drápal–Wanless 2021 neighborhood; Galois extensions in **Q**(√3); LMFDB 4.2.10224.1 in companion J33).

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex / .md finalized — rewritten per save plan
- [x] Verification script green — `manuscript/verify_J07.py` → 4/4 PASS at machine / 50-digit `mpmath` precision (partition incompatibility; sub-tables; D48 joint closure 16+16; D78 attractor H/Br = 1+√3 with polynomial identity)
- [x] Tier-classified central claim explicit — Theorems 1, 2 (PROVED, substrate-independent); Appendix A D48+D78 (PROVED for Z/10Z with canonical tables)
- [x] Lens-scope annotation — §0.1 gives the substrate/lens declaration; the canonical TSML/BHML are the ones used
- [x] Cover letter finalized — rewritten for *Algebraic Combinatorics*
- [x] Dependencies → cite each J-companion as "submitted to [venue]" — J02, J10, J33
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to *Algebraic Combinatorics* this quarter (J02 also targets AC; verify cap)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B. R. & Gish, M. (2026). "A Flatness Obstruction on Squarefree Z/nZ: Four Algebraic Structures and the 4-Core Algebraic Center." Submitted to *Algebraic Combinatorics*.
