# J01 — Non-Associativity Decay in Binary Composition Tables over Z/NZ

**Status:** SUBMISSION-READY
**Phase:** Phase 1
**Target venue:** JCT-A
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** WP101

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (canonical submission LaTeX; the markdown working version is preserved at `manuscript/WP101_SIGMA_RATE_THEOREM.md`)

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (canonical submission LaTeX; renamed 2026-05-13 from `sigma_rate_theorem.tex`)
- `WP101_SIGMA_RATE_THEOREM.md` (markdown working version; preserved per never-delete)
- `verify_sigma_rate.py` (verification script — green-light gate)
- `universal_markov_and_binary_cl.py` (supporting computation)
- `jcta_cover_letter.md` (JCT-A-specific cover letter draft)
- `LATEX_BUNDLE_NOTES.md`, `SUBMISSION_LOG.md`, `SUBMIT_INSTRUCTIONS.md` (submission housekeeping)
- `f6_burgers_test_2026_05_02/` (companion F6 Burgers test subfolder)
- `master/` (historical full-bundle archive: `sigma_rate_theorem_FINAL_v_review_round_8.tex`, `sigma_rate_theorem_v_april.tex`, `proof_sigma_rate_april.py`, etc.)

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Local path:** `manuscript/master/proof_sigma_rate.py`

The proof script is the green-light gate before submission. Run from this J-folder.

## §3 — Dependencies (J-papers cited as already-submitted companions)

_(none — this paper is foundational in the J-series)_

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

Round-3 audited; 4/4 PASS. Major-revisions per JCT-A referee (May 2026) — **all three items addressed in the 2026-05-13 referee-readiness pass**:

- ✅ **Notation unification.** Remark `rem:notation` in §2 enumerates $h:=N-1$, $\varphi(N)$, $\DIS$/$\ECHO$, $E(N)/E_h(N)$, $\varepsilon(N)$, and the three rules $\HARM$/$\VOID$/$\ECHO$ in one place. The residual count $\varepsilon(N)$ is now explicitly defined as the Case-3 count with the bound $0\le\varepsilon(N)\le 2\varphi(N)$ stated up front and proved in §\ref{sec:rate}.
- ✅ **Subcase (1f) density.** Compressed from 8 lines to 3 lines: the key insight (both inner and outer compositions reduce to $0$ via $\VOID$ because $b,c \ne h$ blocks $\HARM$ on the inner and $m \ne h$ blocks $\HARM$ on the outer) is now stated as a single chain of three $\VOID$ applications instead of the previous case-by-case rewrite.
- ✅ **`Four-rule' framing clarity.** Remark `rem:three-rules` after Definition~\ref{def:cl} makes the four-case display vs.\ three-rule structure explicit: there are three rules ($\HARM$, $\VOID$, $\ECHO$) in priority order, with the fourth case in the display being a fall-through default to $\HARM$ rather than a separate rule. The abstract, introduction, and cover letter all use the "three-rule" wording consistently.

### Lens-ownership paragraph (insert in manuscript §0)

> *Lens and substrate.* We work on Z/N for squarefree N, with the specific binary composition family CL_N (whose definition follows Birkhoff-style cell-rules driven by HARMONY/VOID/ECHO outputs). These choices are not derived from first principles; they reflect a structural reading of the substrate motivated by the 10-operator decomposition observed in the runtime DOING-table. The σ-rate theorem below is a theorem on this specific structure; analogous theorems would hold on other substrate families with appropriately chosen tables. The framework's claim is that this particular substrate-and-table-choice produces theorems with surprising downstream connections (cosmology via Bialynicki-Birula-Mycielski 1976, Lie algebra via TSML_SYM antisymmetrization, number theory via LMFDB 4.2.10224.1). Whether other substrate choices give similarly rich downstream connections is open.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** σ(N) ≤ 2/N for squarefree N (the σ-rate decay theorem on the CL_N family; case-analysis proof with three cases reducing to CRT + ECHO count).
- **COMPUTED:** `proof_sigma_rate.py` 4/4 PASS; verified for squarefree N ∈ {2..250} extending earlier ranges; case 3 bound 2φ(N) confirmed loose with substantial slack.
- **STRUCTURAL RHYME:** the C = 2 constant connects to the squarefree-density 1/ζ(2) regime and (via primon-gas heuristic) to the corridor-midpoint structure of WP101 — flagged as motivational, not derivational.
- **OPEN:** prove E_h(N) = 0 for all squarefree N (currently empirical for N ≤ 250); sharpen the case-3 bound below 2φ(N) at finite N.

### Drápal-Wanless 2021 precedent

The closest published precedent for the broader CL_N family framework is Drápal-Wanless 2021 *JCTA* on maximally non-associative quasigroups (referenced via J02 four-core).



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
- [ ] Per-venue cap check: this is the Nth paper to JCT-A this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "Non-Associativity Decay in Binary Composition Tables over Z/NZ." Submitted to *JCT-A*.
