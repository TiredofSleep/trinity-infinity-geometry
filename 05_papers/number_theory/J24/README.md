# J24 — The Discrete Fejér Quotient on Squarefree Moduli: Spectral Characterization, Layered Divisors, and the Asymptotic Corridor Average

**Status:** MERGED 2026-05-13 (J24 + J41 consolidated into a single Integers submission; 10/10 verification PASS; previously: Fork A restoration 2026-05-08, substance upgrade 2026-05-13 added Theorem 5.2 + Cor 5.4)
**Phase:** Phase 1 (Triadic Launch)
**Target venue:** Integers — Electronic Journal of Combinatorial Number Theory
**Author lane:** Sanders + Gish
**Tier:** 2 (draft (Integers; J24 absorbed J41, needs final consolidation pass))
**WP source:** WP34 (First-G Law) + WP35 (Prime Phase Transition) + held draft `_held_first_g/first_g_sinc2_FINAL.tex`

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.tex` (canonical submission LaTeX, ~25 pages amsart, 7 theorems + 2 corollaries spanning closed form, full-period cancellation, First-G localization, spectral characterization, layered divisors, continuum limit, and corridor average)

Files in this J-folder's `manuscript/`:

- `manuscript.tex` (canonical submission LaTeX; merged J24 + J41 manuscript on 2026-05-13)
- `proof_first_g_event.py` (verification for Theorem 4.1 First-G localization; 305 squarefree b in [2, 500], 22,367 (b,k) pairs, zero counterexamples)
- `verify_J03.py` (consolidated verification for the remaining nine claims; 10/10 PASS at machine precision)

The submission package lives in this J-folder. Edit + verify here; submit from here.

## §2 — Verification scripts

**Paths:**
- `manuscript/verify_J03.py` — ten checks covering Theorems 3.1 (closed form), 3.2 prime case (full-period cancellation as biconditional via prime test), **3.2 composite case** (full-period cancellation at composite f via $R(f \cdot m, f) = 0$), 5.1 (synchronization), 5.2 (obstruction-zero correspondence: $f_b(k)=0 \Leftrightarrow \gcd(k,b)>1$), **6.1 (squarefree layered-divisor structure: $2^j-1$ count at the j-th primorial)**, 7.1 (continuum limit), **7.2 (corridor average $\to \Si(2\pi)/\pi$)**, Cor 3.3 (endpoint values), Cor 5.4 (asymptotic zero density). **10/10 verifications pass** at machine precision; max closed-form deviation 4.44 × 10⁻¹⁶ across 14 primes (f up to 47); 900/900 cells match the obstruction-zero equivalence for squarefree b ≤ 50, k ≤ 30; 50/50 squarefree b satisfy the layered $2^j-1$ count; Euler-product density matched to 6.67 × 10⁻⁶ for b up to 2310; corridor-average deviation 4.8 × 10⁻⁵ at f = 1000. Runtime ~5s.
- `manuscript/proof_first_g_event.py` — Theorem 4.1 (First-G localization: $k^{*}(b)=\mathrm{spf}(b)$ for every $b>1$). Direct enumeration over 305 squarefree $b \in [2, 500]$, 22,367 (b,k) pairs, zero counterexamples. Runtime <3s.

Both scripts are the green-light gate before submission. Run order: `verify_J03.py` first (the ten-claim gate), then `proof_first_g_event.py` (the integer-enumeration gate on Theorem 4.1).

## §3 — Dependencies (J-papers cited as already-submitted companions)

J14, J15

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes

### SAVE PLAN J24 — IMPLEMENTED 2026-05-08 (Fork A restoration complete)

**Verdict: KEEP-VIABLE — DONE.** Fork A restoration is implemented. The held draft `_legacy_tiers/tier1_submit_now/_held_first_g/first_g_sinc2_FINAL.tex` (552 lines, two non-trivial theorems, machine-precision verification at max deviation 4.44 × 10⁻¹⁶ across 8 primes) has been copied into `manuscript/manuscript.tex` and augmented per SAVE_PLAN §2 with:

1. **§0 lens-and-substrate preamble** (per `J_PAPER_BOILERPLATE.md` §5.5) — short variant, since J24 is not a magma paper. Acknowledges substrate is plain Z, no operator labels, companion papers reside on Z/N.
2. **§1 tier-discipline paragraph (PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN)** per `J_PAPER_BOILERPLATE.md` §0/§2. Explicitly classifies what is proved, what is computationally verified, what is structural rhyme (sinc²(1/2) = (2/3)/ζ(2)), and what is open (the corridor-midpoint question).
3. **5 new bibliography entries** — Erdős 1959, Pomerance 1985, Tenenbaum 2015, Iwaniec-Kowalski 2004, Friedlander-Iwaniec 2010. Bibliography total now 15 entries (4 textbooks + 7 journal/series + 1 Shannon DOI + 3 internal companions).
4. **Author lane: Sanders + Gish only.** Luther dropped per Brayden directive (held draft already correct).
5. **Title:** *The First-G Event and a Discrete Sinc² Identity* (held draft title; tighter than the stub's overpromising subtitle).
6. **Drápal-Wanless framing:** not invoked in J24 directly (J24 is not a magma paper) but referenced in the lens-ownership preamble as the broader-program neighborhood.
7. **Verification scripts:** `proof_first_g_event.py` (305 squarefree b in [2,500], 22,367 (b,k) pairs, zero counterexamples, runtime <3s) and `verify_J03.py` (closed-form / synchronization / continuum-limit / endpoint-minimum checks; 5/5 verifications pass; max deviation 4.44 × 10⁻¹⁶; renamed 2026-05-13 from `verify_first_g.py` when porting Fork A into the public repo).

The Triadic Launch slot is preserved. Estimated revision time per save plan: 4–6 hours. Implementation completed in single pass.

### Earlier referee audit (2026-05-07): paper was too thin — superseded by Fork A restoration above

Brayden's instinct ("not substantial enough") was validated by the earlier line-by-line referee. The stub had Theorem 3.1 Part (i) as a 3-line tautology (definition of spf(b)), all four corollaries as one-line rereads, and substantive content (closed-form R(k,f), sinc² synchronization) stripped out and moved to J25 in a 2026-04-19 shrink. **Fork A reverses that shrink.** Theorem 4.2 (closed form), Theorem 5.1 (synchronization), Theorem 6.1 (continuum limit) are now in J24 directly. J25 keeps the cryptographic/ω-blindness application development separately.

### REFEREE AUDIT (2026-05-07): paper IS too thin for *Integers* — see J03_FirstG_Substance_Audit.md

Brayden's instinct ("not substantial enough") was validated by the line-by-line referee:
- Theorem 3.1 Part (i) is a 3-line tautology (definition of spf(b))
- All four corollaries are one-line rereads
- Substantive content (closed-form R(k,f), sinc² synchronization) was stripped out and moved to J25 Prime Phase Transition
- §1 self-admits marginal novelty: "what is new is the packaging" — desk-reject trigger

**Three forks (Brayden's call before Triadic Launch):**

- **Fork A (preferred):** restore harmonic content from `_legacy_tiers/_held_first_g/first_g_sinc2_FINAL.tex` — closed-form R(k,f), synchronization theorem, continuum limit, exact `sinc²` values. 4-6 hours. Makes J24 a real *Integers* note.
- **Fork B (safer):** swap **J32** (TSML 73 / BHML 28 cells, *Exp Math*, SUBMISSION-READY) into the Triadic Launch slot. Demote J24 to AMM-Note or arXiv-only.
- **Fork C (last resort):** Submit current J24 to *AMM Notes* / *Math Magazine* instead of *Integers*.

Recommendation: **A > B > C.** Either way: do not submit current J24 to *Integers* unmodified.

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN (post J24 + J41 merger; 7 theorems + 2 corollaries)

- **PROVEN:**
  - *Theorem 3.1 (closed form).* R(k, f) = sin²(πk/f) / (k² sin²(π/f)) for every f ≥ 2, k ≥ 1. Fejér-type identity.
  - *Theorem 3.2 (full-period cancellation).* R(k, f) = 0 iff f | k, uniform in f ≥ 2. (Promotes Lemma 1 of the absorbed J41 manuscript.)
  - *Theorem 4.1 (First-G localization).* For every b > 1, k*(b) = spf(b). One-line gcd argument.
  - *Theorem 5.1 (synchronization at smallest spectral zero).* For every b > 1, the First-G event and the smallest integer zero of f_b coincide at k = spf(b). Special case of Theorem 5.2 at the smallest zero.
  - *Theorem 5.2 (obstruction-zero correspondence — central new contribution).* For every b > 1 with distinct prime factors p₁, ..., p_r, the spectral product $f_b(k) := \prod_j R(k, p_j)$ vanishes at integer k ≥ 1 iff gcd(k, b) > 1. The integer zero set of $f_b$ is exactly $\bigcup_j p_j \mathbb{N}$; $f_b$ acts as a continuous-in-k indicator for the obstruction event.
  - *Theorem 6.1 (squarefree layered-divisor structure — from absorbed J41).* For squarefree b = p₁...p_r and the j-th primorial b_j = p₁p₂...p_j, exactly $2^j - 1$ non-trivial divisors d|b satisfy R(b_j, d) = 0.
  - *Theorem 7.1 (continuum limit).* R(k, f) → sinc²(k/f) as f → ∞ with k/f fixed.
  - *Theorem 7.2 (asymptotic corridor average — from absorbed J41).* $\frac{1}{f-1}\sum_{k=1}^{f-1} R(k, f) \to \int_0^1 \sinc^2(t)\, dt = \mathrm{Si}(2\pi)/\pi \approx 0.4514$ as $f \to \infty$.
  - *Corollary 3.3 (endpoint values).* R(1,f) = 1, R(f-1,f) = 1/(f-1)², R(f,f) = 0, strict monotonicity on {1, ..., f-1}.
  - *Corollary 5.3 (inclusion-exclusion identity for |G_k|).* $|G_k(b)| = \#\{j \le k : f_b(j) = 0\} = -\sum_{d \mid \mathrm{rad}(b),\, d > 1} \mu(d) \lfloor k/d \rfloor$.
  - *Corollary 5.4 (asymptotic zero density).* Zero density of $f_b$ in $\mathbb{N}$ equals $1 - \varphi(\mathrm{rad}(b))/\mathrm{rad}(b)$.
- **COMPUTED:**
  - 22,367 (b,k) pairs over 305 squarefree b ∈ [2, 500], zero counterexamples, runtime <3s (`proof_first_g_event.py`).
  - 4,225 (p, k) pairs for the prime-case full-period cancellation (Lemma form) — every prime $p \in \{3, 5, \dots, 199\}$, every $k \in \{1, \dots, p\}$, exact integer divisibility cross-checked with floating-point evaluation, zero counterexamples.
  - 145 (f, m) pairs for the composite-case full-period cancellation: $f \in \{2, \dots, 30\}$, $m \in \{1, \dots, 5\}$, $|R(f m, f)| < 10^{-10}$ across all 145 cells.
  - 14 primes f ∈ {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47}, all k ∈ {1, ..., f+1}, max deviation 4.44 × 10⁻¹⁶ for the closed form.
  - 900/900 cell-level boolean matches of $f_b(k)=0 \Leftrightarrow \gcd(k,b)>1$ for 30 squarefree $b \in [2, 50]$ and $k \in [1, 30]$.
  - Euler-product density predictions match observed obstruction densities to within 7 × 10⁻⁶ for b up to 2310 over window K = 100,000.
  - Layered structure $2^j - 1$ count verified for 50 squarefree b in [6, 210] with $\omega(b) \ge 2$; zero counterexamples on (i) smallest-k = spf(b), (ii) $b_2$ count = 3, (iii) $b_3$ count = 7 (where ω(b) ≥ 3).
  - Corridor average converges to Si(2π)/π ≈ 0.45141: deviation 4.0 × 10⁻⁴ at f = 50, 3.4 × 10⁻⁴ at f = 100, 9.2 × 10⁻⁵ at f = 500, 4.8 × 10⁻⁵ at f = 1000.
- **STRUCTURAL RHYME:**
  - *Identity sinc²(1/2) = 4/π² = (2/3)/ζ(2).* One-line consequence of ζ(2) = π²/6. Cited as motivation for the corridor midpoint, not as derivational input.
  - *Primon-gas reading: 1/ζ(2) = density of squarefree integers.* The squarefree restriction in our verification sample sits in this regime — bridge connection only.
  - *Drápal-Wanless 2021, JCTA.* Cited in the J-series broadly as the closest published precedent for the magma framework; not invoked in this paper directly.
- **OPEN:**
  - Why does the corridor midpoint at t = 1/2 make sinc²(1/2) = (2/3)/ζ(2) structurally relevant beyond its one-line derivation?
  - Does the spectral product $f_b$ admit a Ramanujan-sum or character-sum form beyond the inclusion-exclusion identity in Cor 5.3?
  - Is there a closed-form non-squarefree refinement of Theorem 6.1's $2^j - 1$ count beyond reduction to $\rad(b)$?

### Status update (2026-05-08, post-SAVE-PLAN)

- **Manuscript:** `manuscript/manuscript.tex` (Fork A restoration). amsart, ~14 pages with the §0 lens preamble, §1 tier-discipline paragraph, expanded bibliography (15 entries). Title: *The First-G Event and a Discrete Sinc² Identity*.
- **Verification scripts:**
  - `manuscript/proof_first_g_event.py` — Theorem 3.1 First-G localization. Runtime <3s. 305 squarefree b in [2, 500], 22,367 (b,k) pairs, zero counterexamples.
  - `manuscript/verify_J03.py` — Theorems 4.2 / 5.1 / 6.1 + Cor 4.4(ii). 5/5 verifications pass; max closed-form deviation 4.44 × 10⁻¹⁶ across 8 primes (renamed 2026-05-13 from `verify_first_g.py` when porting Fork A into the public repo).
- **Cover letter:** `cover_letter.md` rewritten 2026-05-08 to lead with the synchronization theorem (not "this paper exists to be cited by J25"). ~700 words.
- **Author lane:** Sanders + Gish (Luther dropped per Brayden directive 2026-05-07). Held draft already correct; no Luther reference in the new manuscript.
- **Pre-submission remaining:** Brayden's referee-rigor pass; arXiv same-day upload at submission time; Integers style-file pass if amsart not accepted on first submission.



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

- [x] Manuscript .tex finalized (`manuscript/manuscript.tex`; Fork A restoration with §0 lens preamble + §1 tier-discipline paragraph + 15-entry bibliography)
- [x] Verification scripts green (`manuscript/verify_J03.py` → 5/5 PASS at machine precision; `manuscript/proof_first_g_event.py` → 22,367 (b,k) pairs, zero counterexamples)
- [x] Tier-classified central claim explicit (PROVEN: Theorems 3.1, 4.2, 5.1, 6.1 + Cor 4.4; COMPUTED: closed-form deviation 4.44e-16, First-G enumeration; STRUCTURAL RHYME: sinc²(1/2) = 4/π² = (2/3)/ζ(2); OPEN: corridor-midpoint substrate question)
- [x] Lens-scope annotation — §0 of manuscript states the substrate is plain $\Z$ (J24 is not a magma paper); the broader-program magma framework (Drápal-Wanless 2021 neighborhood) is referenced as context, not invoked
- [x] Cover letter finalized (`cover_letter.md`; leads with the synchronization theorem 5.1, ~700 words)
- [x] Dependencies → cite each J-companion as "submitted to [venue]" (J14 → JCT-A; J15 → AC)
- [x] Author lane: Sanders + Gish only (Luther dropped per Brayden directive 2026-05-07)
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators) — pending
- [ ] Per-venue cap check: this is the 1st paper to Integers this quarter
- [ ] Submitted (arXiv same-day upload at submission time)

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish. (2026). "First-G Law: Squarefree Stability of the Smallest-Prime-Factor Coprime Window." Submitted to *Integers*.
