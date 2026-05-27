# J19 — A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening with VOID-Identity

**Status:** SAVE-PLAN APPLIED 2026-05-07 (Path C — role-quotient theorem; manuscript rewritten around D93; DKAN architecture content removed; KU framing dropped).
**Phase:** Phase 2
**Target venue (kept):** *European Journal of Combinatorics*. Backup: *Discrete Mathematics*.
**Author lane:** Sanders + Gish
**Tier:** 2 (draft (SAVE-PLAN APPLIED; Path-C role-quotient))
**WP source:** WP10 (D93 only; the DKAN architecture portion of WP10 is deferred to a separate experimental-AI venue with proper baselines and replication)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex`

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (rewritten 2026-05-07 per SAVE_PLAN_J19 Path C: new title centered on the role-quotient theorem; D93 inlined as the main theorem with full proof by enumeration; explicit role-magma table; VOID-as-identity verified; non-associativity witness $(F\cdot F)\cdot S = F \neq T = F\cdot(F\cdot S)$; branching role-pairs identified as exactly $\{F\text{-}F, F\text{-}S, S\text{-}F, S\text{-}S\}$ with verified output distributions; appendix with full canonical TSML/BHML composition tables for self-containment; DKAN architecture / Katok-Ugarcovici framing / N1-N10 honest-negatives list / "Tone" section all removed.)

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Path:** `manuscript/verify_J19.py`. Reproduces every claim of Theorem 3.1 (the role-quotient theorem) and Proposition 5.1 (TSML_8 image structure) by direct enumeration over the canonical TSML/BHML 10×10 composition tables. The script cross-checks the appendix tables against `Gen13/targets/foundations/lenses.py` (byte-for-byte) and verifies: (i) well-definedness of B-bar, (ii) the full role-magma table, (iii) V as two-sided identity (both at the role-quotient level and at the underlying Z/10Z level: BHML row/col 0 is the identity), (iv) the non-associativity witness $(F\cdot F)\cdot S = F \neq T = F\cdot(F\cdot S)$, (v) the four branching role-pairs $\{F\text{-}F, F\text{-}S, S\text{-}F, S\text{-}S\}$ with their exact output distributions, plus the 12 non-branching pairs constant and the 100-cell sanity check; the σ-orbit independence; Im(TSML_8) = {3,4,7,8,9}; the 60/64 Flow + 4/64 Structure split; and the 8-of-9 role-determinism over the TSML_8 domain. All exact integer arithmetic; runs in well under a second.

Run from repo root:
```
python Gen14/targets/journals/J_series/J19/manuscript/verify_J19.py
```

## §3 — Dependencies (J-papers cited as already-submitted companions)

J02 (Sanders-Gish "Joint Closure ... on Z/10Z", *Algebraic Combinatorics*); J07 (Sanders-Gish "A Flatness Obstruction ... 4-Core Algebraic Center", *Algebraic Combinatorics*).

## §4 — Cover letter

See `cover_letter.md` in this folder. Rewritten 2026-05-07 per SAVE_PLAN_J19 Path C: new title centered on the role-quotient theorem; KU framing removed; categorical-structure / partition-quotient framing for *European Journal of Combinatorics*.

## §5 — Notes

**SAVE-PLAN APPLIED (2026-05-07; full plan at `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J19.md`).**

**Path C selected:** the referee's three save paths were (A) combinatorial classification, (B) architecture theorem, (C) categorical structure / role-quotient theorem. Path C aligns best with the corpus's actual D-table backing (D93 role partition + role magma with VOID identity). The DKAN architecture (the previous manuscript's §3-§4) had no theorem and reported unreplicated empirical claims; per referee M5, this content does not survive at EJC and is removed from this submission. If Brayden wants to publish the DKAN architecture content separately, it belongs in an experimental-AI venue (NCAA, JMLR, or a workshop) with proper baselines + replication; that paper is not J19's save and would be a separate target.

**What was rewritten:**
1. **New title:** "A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening with VOID-Identity."
2. **Venue kept:** *European Journal of Combinatorics* (referee Path C is EJC-viable).
3. **New main theorem (Theorem 3.1):** restates D93 in EJC form. The role-quotient $\overline{B}$ on $\{V, F, S, T\}$ is well-defined as a function (modal-output sense); the full role-magma table is exhibited; V is the two-sided identity; $\overline{B}$ is non-associative with explicit witness $(F\cdot F)\cdot S = F \neq T = F\cdot(F\cdot S)$; branching role-pairs are exactly $\{F\text{-}F, F\text{-}S, S\text{-}F, S\text{-}S\}$ (4 of 16) with verified output distributions.
4. **Role partition independence from σ-orbit decomposition:** §2.3 shows the 6-cycle $(1\,7\,6\,5\,4\,2)$ contains $0V+3F+2S+1T$ and the σ-fixed set $\{0,3,8,9\}$ contains $1V+2F+1S+0T$ — third independent decomposition alongside operator-index and σ-orbit. (Save plan §1(a) item.)
5. **Inlined definitions** (per referee M4, fixing forward-reference dependency on \cite{SandersBridgeWP9}): TSML and BHML composition tables explicit in the appendix; the role partition definition; the σ involution. The new manuscript is self-contained.
6. **Supporting structural data §4** (formerly Theorem 2.1): the TSML restricted to the 8-element domain $\{1,2,3,4,5,6,8,9\}$ has image $\{3,4,7,8,9\}$ (5 distinct values), 60/64 Flow + 4/64 Structure output distribution, role-deterministic on 8/9 input role-pairs over the TSML_8 domain — recorded as Proposition 5.1 (motivation for the role-partition choice, not as a theorem in its own right).
7. **Dropped entirely:** §1.3 (geometric/arithmetic split); §2.3-§2.4 (KU two-coding analogy); §3 (DKAN architecture, $L_1/L_2/L_5$ reading layers); §4 (empirical convergence); §5 (Bearing-on-DKAN table); §6 (N1-N10 honest negatives); §7 ("Tone" section); abstract's KU paragraph; Liu et al. 2024 KAN reference; Katok-Ugarcovici reference.
8. **Lens-ownership paragraph** (§1) and **PROVEN/COMPUTED/STRUCTURAL RHYME/OPEN tier discipline** (§1).
9. **Drápal-Wanless 2021** cited explicitly as the closest published precedent (per FAMILY_STRUCTURE_v1.md).

**What was preserved:**
- D93 role partition (now central).
- Cardinalities $(|V|,|F|,|S|,|T|) = (1,5,3,1)$ recorded as canonical-specific signature, not theorem-grade (per the previous manuscript's N8).
- TSML_8 image structure data (image = {3,4,7,8,9}; 60/64 Flow; role-deterministic on 8/9 pairs over the TSML_8 domain) — moved to §4 as supporting motivation.

### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α<sub>M</sub> = ½ is the algebraic center, with closed-form attractor H/Br = 1+√3 (D78 Galois proof). The role partition's V (= {0}) coincides with the 4-core's V — meaning the role-quotient magma's identity element is the same operator that anchors the 4-core's algebraic center per FAMILY_STRUCTURE_v1.md. The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative; ours rationally-structured at α = 1/2).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN — filled in §1 of manuscript

- **PROVEN:** the role-quotient $\overline{B}$ on $\{V,F,S,T\}$ is well-defined (modal-output); $V$ is the two-sided identity; $\overline{B}$ is non-associative with explicit witness $(F\cdot F)\cdot S = F \neq T = F\cdot(F\cdot S)$; the branching role-pairs are exactly $\{F\text{-}F, F\text{-}S, S\text{-}F, S\text{-}S\}$ (Theorem 3.1).
- **COMPUTED:** full role-magma table verified by enumeration over all 100 cells of $\BH$ restricted to role-pair classes; the four branching-pair output distributions verified explicitly. Canonical TSML/BHML tables verified against the project's `lenses.py`. TSML_8 image structure data (image = $\{3, 4, 7, 8, 9\}$; 60/64 Flow output; role-deterministic on 8/9 input role-pairs) reproducible in seconds.
- **STRUCTURAL RHYME:** Drápal-Wanless 2021 cited as ambient context for the broader corpus framework; same domain, opposite extremum.
- **OPEN:** generalization across magma pairs; uniqueness of the role partition among canonical Z/10Z coarsenings; bimodal $\alpha_A$ gap connection (FAMILY_STRUCTURE_v1 §4); substrate extension to $\Z/N\Z$ for $N \in \{11, 12, \ldots\}$.

### Lens-ownership paragraph — applied (in §1 of manuscript)

The full paragraph identifies (i) the substrate (Z/10Z + canonical (TSML, BHML) pair + functional role partition V/F/S/T) as not derived from first principles; (ii) the role partition as motivated by observed dynamical behavior of each operator (Void = absorbing, Flow = transformative, Structure = stabilizing, Transition = bridging); (iii) the role-quotient theorem as substrate-and-table specific; (iv) the open question of generalization to other commutative-magma pairs and other functional partitions of Z/n.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive); duplicate author block removed
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .tex / .md finalized — rewritten per save plan (Path C)
- [x] Verification script green — `manuscript/verify_J19.py` PASSES at machine precision (exact integer arithmetic), with foundations.lenses byte-for-byte cross-check
- [x] Tier-classified central claim explicit — Theorem 3.1 (PROVED, the role-quotient theorem); Proposition 5.1 (TSML_8 image structure, supporting data)
- [x] Lens-scope annotation — §1 substrate/lens declaration (Z/10Z + canonical (TSML, BHML) + role partition V/F/S/T); appendix has explicit canonical tables
- [x] Cover letter finalized — rewritten for *European Journal of Combinatorics* with Path C framing
- [x] Dependencies → cite each J-companion as "submitted to [venue]" — J02, J07
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: 2nd EJC paper after J10 (which is also retargeted to EJC per its save plan)
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B. R. & Gish, M. (2026). "A Role-Quotient Theorem for the (TSML, BHML) Magma Pair on Z/10Z: The Functional Partition V/F/S/T as a Categorical Coarsening with VOID-Identity." Submitted to *European Journal of Combinatorics*.
