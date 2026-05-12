# J04 — Full-Period Cancellation of R(k, f) and the spf-Localization for Squarefree Moduli

**Status:** SAVE-PLAN IMPLEMENTED (manuscript rewritten 2026-05-08; Theorem 1.A + Theorem 2 + Theorem 3 in place)
**Phase:** Phase 1 (Triadic Launch companion to J03)
**Target venue:** Integers
**Author lane:** Sanders + Gish
**Tier:** B
**WP source:** (full-period cancellation; formerly "sinc² zero law" — renamed 2026-05-07 per external collaborator calibration; "Zero Law" implied prime-specific structure but R(k,f) = sin²(πk/f)/(k² sin²(π/f)) vanishes at k = f for ANY f via sin²(π) = 0)

---

## §1 — Manuscript

**Local path:** `manuscript/`

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (current submission file — implements SAVE_PLAN_J04: Theorem 1.A + Theorem 2 + Theorem 3)
- `proof_d25_loop_closure.py` (verifier — 5/5 PASS at machine precision)
- `sinc2_zero_law.tex` (legacy draft retained for traceability; superseded by `manuscript.tex`)
- `cover_letter_template.md`
- `LATEX_BUNDLE_NOTES.md`
- `SUBMIT_INSTRUCTIONS.md`
- `WP34_FIRST_G_LAW.md`
- `WP35_PRIME_PHASE_TRANSITION.md`
- `WP_SINC2_ZERO_LAW.md`
- `verify_prime_phase_transition.py`

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification script

**Path:** `papers/proof_d25_loop_closure.py`

The proof script (where applicable) is the green-light gate before submission. If "(no script — theorem-paper)" or similar, the gate is the proof's referee-rigor pass.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J03 (First-G synchronization companion, also submitted to *Integers*).

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

### SAVE PLAN J04 — IMPLEMENTED 2026-05-08

**Verdict: KEEP-WITH-MAJOR-WORK — DONE.** Per SAVE_PLAN_J04, the manuscript has been rewritten from scratch as a real *Integers* contribution. The fresh-eyes referee's earlier "Reject" applied to the version that existed before; the current `manuscript/manuscript.tex` (revised 2026-05-08) implements the save plan in full:

1. **Title changed** from "The Sinc² Zero Law for Squarefree Moduli" to *Full-Period Cancellation of R(k, f) and the spf-Localization for Squarefree Moduli*.
2. **Lemma 1 (basic biconditional)** retained as canonical entry point.
3. **Theorem 1.A (full-period cancellation)** added: R(k, f) = 0 iff f | k, uniform in f. The canonical statement of the Fejér-quotient zero set; promotes Lemma 1 to the R(k, f) framing.
4. **Theorem 2 rebuilt** with the layered-divisor structure: for squarefree b = p₁ p₂ … pᵣ, the smallest k at which any non-trivial divisor d | b yields R(k, d) = 0 is exactly k = spf(b), AND at the j-th primorial divisor k = b_j = p₁…p_j, exactly **2^j − 1** non-trivial divisors d | b satisfy R(b_j, d) = 0. Proof uses the Boolean structure of the divisor lattice on rad(b) — squarefree-ness essential here.
5. **Theorem 3 added (asymptotic average)** via D14: (1/(f-1)) ∑ R(k, f) → Si(2π)/π ≈ 0.4514 as f → ∞. Proof uses Riemann sum + the closed-form integration ∫₀^π sin²(u)/u² du = Si(2π).
6. **Corollary** added cleanly tying Theorem 2 to J03 (cuts the previous §3 trio of restatement corollaries per referee Issue 2; cuts §4 boundary-value section per referee M2 — Montgomery non-sequitur).
7. **§0 lens-and-substrate preamble** + **§1 tier-discipline (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN)** paragraph per `J_PAPER_BOILERPLATE.md` §5.5 / §0.
8. **Bibliography expanded** to 9 entries (Apostol, Erdős, Fejér, Hardy-Wright, Iwaniec-Kowalski, Tenenbaum, Zygmund + 2 internal companions). Drápal-Wanless not invoked (J04 is not a magma paper).
9. **Verification script rewritten** (`proof_d25_loop_closure.py`):
   - DROPPED the bisection block (referee M3) — fold-of-sinc² content not in the manuscript.
   - DROPPED the strict-monotonicity assertion outside (0,1) (referee M4) — replaced with informational "non-increasing at integer arguments" report.
   - ADDED Theorem 2 layered-closure check (50 squarefree b, exact divisibility, 2^j − 1 count at b_2 and b_3).
   - ADDED Theorem 3 asymptotic-average check (f ∈ {50, 100, 500, 1000}; convergence to Si(2π)/π within 5 × 10⁻⁵ at f = 1000).
   - 5/5 verifications PASS; runtime <5s; prints `ALL ASSERTIONS PASSED`.
10. **Author lane:** Sanders + Gish (Luther dropped per Brayden directive 2026-05-07).
11. **Cover letter rewritten** to frame J04 as a J03 companion (not a duplicate); explicit Theorem-1.A / Theorem-2 / Theorem-3 differentiation in the intro.

**Per-venue cap:** with both J03 (Fork A restored) and J04 (rebuilt) going to *Integers*, the per-quarter cap (2 papers) is exactly used. The two-paper companion structure is intentional; cross-citations are explicit; each paper stands alone.

**RENAMED 2026-05-07** per external collaborator calibration. Previous title
"The Sinc² Zero Law for Squarefree Moduli" carried implicit prime-specific
structural overclaim. The correct framing: R(k, f) = sin²(πk/f)/(k² sin²(π/f))
vanishes at k = f because sin²(π) = 0 — for ANY f, not just primes. The
prime-3-to-199 sweep is verification of the formula, not a prime-specific
theorem.

### Lens-ownership paragraph (insert in manuscript §0)

> *Lens and substrate.* We work on Z/n for squarefree n with the discrete Fejér quotient R(k, f) = sin²(πk/f) / (k² sin²(π/f)). This object is not "TIG-specific"; it is the standard discrete Fejér kernel familiar from Fourier analysis on cyclic groups. The squarefree-modulus restriction reflects the regime where the spf-localization (Theorem 2) applies cleanly. The paper's role within a broader research program is noted in the Companion section, but the result and proof here are self-contained.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (post-SAVE-PLAN, final)

- **PROVEN:**
  - *Lemma 1 (basic divisibility biconditional).* sinc²(k/b) = 0 ⇔ b | k for every b ≥ 1, k ≥ 1.
  - *Theorem 1.A (full-period cancellation).* R(k, f) = 0 ⇔ f | k for every f ≥ 2, k ≥ 1.
  - *Theorem 2 (squarefree layered structure).* For squarefree b = p₁…pᵣ, the smallest k with R(k, d) = 0 for some non-trivial d | b is k = spf(b), and at the j-th primorial divisor b_j = p₁…p_j the count is exactly 2^j − 1.
  - *Theorem 3 (asymptotic average).* (1/(f-1)) ∑ R(k, f) → Si(2π)/π ≈ 0.4514 as f → ∞.
  - *Corollary (J03 companion).* The first-zero index in J04 Theorem 2 equals the First-G event of J03 Theorem 3.1.
- **COMPUTED:** `proof_d25_loop_closure.py` runs green:
  - Lemma 1 verified across 4,225 (p, k) pairs (45 primes 3..199).
  - Theorem 1.A verified across 145 (f, m) pairs (f ∈ {2..30}, m ∈ {1..5}).
  - Theorem 2 verified across 50 squarefree b (omega ≥ 2); zero failures for both spf-smallest-k and 2^j − 1 counts at b_2 and b_3.
  - Theorem 3 verified at f ∈ {50, 100, 500, 1000}; deviation ≤ 5 × 10⁻⁵ at f = 1000.
  - Runtime <5s; prints `ALL ASSERTIONS PASSED`.
- **STRUCTURAL RHYME:** the identity sinc²(1/2) = (2/3)/ζ(2) is a one-line algebraic consequence of ζ(2) = π²/6 — not a TIG theorem. Cited as structural motivation only.
- **OPEN:** *why does the corridor midpoint of the substrate sit at 1/2 such that sinc²(1/2) = (2/3)/ζ(2) becomes structurally relevant?* Not addressed in this paper; flagged as open. Also: does the Theorem 2 layered count 2^j − 1 extend to non-squarefree b via the radical? The formal answer is yes (Remark in §4), but the explicit count for divisors of b itself acquires multiplicities; not pursued here.

**Per-venue cap:** 2nd *Integers* paper this quarter after J03 (within cap).

**Authors:** Sanders + Gish.

**Cite:** J03 (First-G companion, submitted to *Integers*).
Drápal-Wanless 2021 *JCTA* on maximally non-associative quasigroups is the
closest published precedent for the broader (TSML, BHML) magma framework
(referenced via J02).



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
- [ ] Per-venue cap check: this is the Nth paper to Integers this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "Full-Period Cancellation of R(k, f): The Integer-Multiple Zero of the Discrete Fejér Quotient (Squarefree Case)." Submitted to *Integers*.
