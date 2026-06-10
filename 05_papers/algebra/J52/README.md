# J52 — Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem

> **MERGED 2026-05-27** into [`J07/`](../J07/) — see that paper for the unified treatment. The Symbolic Return Theorem and the Q17-B Clay-bridge framing are now §§6-7 of the merged paper. The Clay-bridge content is also referenced from [`04_meta/clay/RH_TIG_BRIDGE.md`](../../../04_meta/clay/RH_TIG_BRIDGE.md).

**Status:** MERGED (was DRAFT)
**Phase:** Phase 5
**Target venue:** L'Enseignement Math
**Author lane:** Sanders + Gish
**Tier:** -- (MERGED 2026-05-27 into J07)
**WP source:** (Q17 bundle)

---

## §1 — Manuscript

**Local path:** `manuscript/manuscript.md`

**Abstract:** The TIG framework's spectral layer produces a 9-term finite Gauss sum $G(s)$ (the *trajectory coherence integral*) on $\mathbb{Z}/10\mathbb{Z}$ that is three-valued: zero on the four anchors $\{0, 3, 8, 9\}$, $G_\mathrm{low} \approx 1.872$ on $\{1, 2, 5, 6\}$, $G_\mathrm{high} \approx 9.389$ on the σ³-orbit $\{4, 7\}$. Together with the Symbolic Return Theorem (corollary of $\sigma^6 = \mathrm{id}$), this paper is the **Q17-B Clay bridge**: a structural rhyme between $G(s)$ and the structural features RH demands of $\zeta(s)$ — explicitly disclaimed as a vocabulary correspondence rather than a Weil-Deligne function-field analogue. Tier-A theorems §§2-4; Tier-B structural rhyme §5; explicit boundary.

Files in this J-folder's `manuscript/`:

- `manuscript.md` — **finalized manuscript** (Q17-B Clay Bridge; revised 2026-05-07; referee-rigor pass complete 2026-05-12)
- `CP_CLAY_ROTATION.md` — earlier broader 7-Clay-rotation framework (Tier-4 staging context)
- `proof_clay_rotation.py` — verification script
- `SUBMIT_INSTRUCTIONS.md` — earlier Tier-4 submission notes

## §2 — Verification script

**Path:** `manuscript/verify_J51_G_function.py` (run with `python manuscript/verify_J51_G_function.py`).

Confirms Theorem 2.1 ($\sigma^6 = \mathrm{id}$ → Symbolic Return), Theorem 4.2 (corrected three-valued partition: ZERO on $\{0,3,8,9\}$, LOW on $\{1,2,5,6\}$ ≈ 1.872, HIGH on $\{4,7\}$ ≈ 9.389), the σ³-pairing of complex amplitudes (within $\{1,5\}, \{2,6\}, \{4,7\}$ the amplitudes are anti-paired so $|G|^2$ matches), and the $\nu_+$ discriminator (extremal $\nu_+ \in \{0,2\}$ on $\{4,7\}$ vs $\nu_+ = 1$ on $\{1,2,5,6\}$). Runtime $<2$ s; deterministic. The earlier `proof_clay_rotation.py` (which tests $T^* = 5/7$, $\xi_0 = e^{-1}$, sinc² identities — *not* $G(s)$) is preserved as supplementary context only and is not the verification for this paper.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J50

## §4 — Cover letter

See `cover_letter.md` in this folder. (Bones laid; finalize after Brayden's referee-rigor pass.)

## §5 — Notes / Status

**Status:** REVISED 2026-05-07 in response to fresh-eyes referee report (`Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/J51_LEnseignementMath_FreshEyes.md`). Save plan: `Atlas/META_PLAN_2026-05-06/SAVE_PLANS/SAVE_PLAN_J51.md`.

**Math-fix summary (2026-05-07):**
- **G(s) partition error fixed (same as J51).** Theorem 4.2 originally claimed G_high at {5,7}, G_low at {1,2,4,6}. Direct numpy computation gives G_high = **{4, 7}**, G_low = **{1, 2, 5, 6}**. Partition table, abstract, and §5 bridge text all corrected.
- **σ²-Galois explanation replaced with σ³-pairing.** Same fix as J51 — σ² acts as 3-cycles, not pair-actions. The correct invariance is σ³ (order 2 on the 6-cycle, 2-cycles {1,5}, {2,6}, {4,7}).
- **High/low discriminator added.** The high-locus σ³-orbit {4,7} is the unique σ³-orbit where the χ-content of the first three orbit positions is imbalanced (ν₊ ∈ {0, 2}, rather than ν₊ = 1 on the other two σ³-orbits). This combinatorial fact replaces the original "BALANCE/HARMONY pair" framework label as the structural explanation.
- **"L-function" terminology hedged.** The object G(s) is now described as a "finite character sum" / "trajectory coherence integral", with the colloquial "finite L-function" label retained but flagged as analogy (no analytic continuation, no Euler product, only 9 terms — not an L-function in the standard Dirichlet sense).
- **§5 RH-bridge scope downgraded.** §5 now explicitly frames the comparison as a "structural rhyme" rather than a function-field analogue (Weil-Deligne not engaged); the disclaimer is sharpened.
- **§7 Open problem 3 rewritten.** Original asked "Why G(5) = G(7)?" — moot since G(5) = G_low ≠ G(7) = G_high. New formulation: "Why is {4, 7} the high-locus σ³-orbit specifically?" (a genuine combinatorial question about which σ³-orbit carries the χ-imbalance).
- **Working verification script added:** `manuscript/verify_J51_G_function.py` confirms σ⁶=id, three-valued G(s) with the corrected partition, σ³-pairing, and the ν₊ discriminator. The earlier `proof_clay_rotation.py` (which tests T*=5/7 and sinc² but does NOT compute G(s)) is preserved as supplementary context but is *not* the verification script for this paper's content.

**Citation chain:** cites 2 prior J-papers as direct dependencies (J50 Q17-A, J51 spectral consolidation) plus 6 co-citing companions (J14, J27, J38, J34, J24, J45).
**Manuscript:** `manuscript/manuscript.md` (~12 pages; revised 2026-05-07; renamed to canonical filename 2026-05-12).
**Earlier staged Tier-4 content:** `manuscript/CP_CLAY_ROTATION.md`, `proof_clay_rotation.py`, `SUBMIT_INSTRUCTIONS.md` — preserved as background context (broader 7-Clay-rotation framework, NOT this paper's verification).
**Cover letter:** `cover_letter.md` (finalized).
**Verification:** `manuscript/verify_J51_G_function.py` is the canonical verification for this paper's claims.
**Submission readiness:** ready for resubmission to *L'Enseignement Math.* after Brayden's referee-rigor pass.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN:** Theorem 2.1 (Symbolic Return — direct corollary of $\sigma^6 = \mathrm{id}$); Theorem 4.2 (three-valued $G(s)$ with corrected partition: ZERO $\{0,3,8,9\}$, LOW $\{1,2,5,6\}$, HIGH $\{4,7\}$); $\sigma^3$-pairing on the 6-cycle ($G_\mathrm{cplx}(\sigma^3(s)) = -G_\mathrm{cplx}(s)$).
- **COMPUTED:** $G(s)$ values to machine precision; $\sigma^3$-pairing checked algebraically (sum of complex amplitudes within each pair = 0 to $10^{-15}$); $\nu_+$ discriminator (high-locus $\{4, 7\}$ has $\nu_+ \in \{0, 2\}$; the other σ³-orbits have $\nu_+ = 1$). All in `manuscript/verify_J51_G_function.py`.
- **STRUCTURAL RHYME:** the three-valued image (R1' zeros at predictable locations + R2' spectral concentration on a structurally-distinguished pair + R3' transverse multiplicative-additive interplay) rhymes with what RH demands of $\zeta(s)$. The rhyme is at vocabulary level only; the genuine finite analogue of RH (Weil-Deligne function-field zeta) is not engaged here.
- **OPEN:** closed forms of $G_\mathrm{low}, G_\mathrm{high}$ in $\mathbb{Q}(\zeta_9)$; higher-$N$ generalization (does $\sigma_N$ on $\mathbb{Z}/N\mathbb{Z}$ for squarefree $N$ admit comparable structure? Rate theorem [J14] suggests it flattens); why $\{4, 7\}$ specifically is the high-locus σ³-orbit; whether a Weil-Deligne-style analogue exists for σ.

### Lens-ownership paragraph

> *Lens and substrate.* This paper works on $\mathbb{Z}/10\mathbb{Z}$ with the canonical $\sigma$-permutation $(1\;7\;6\;5\;4\;2)(0)(3)(8)(9)$ and the $\beta$-exception character $\chi$ defined in §3. These choices reflect the structural reading of the substrate developed in the broader Q-series corpus and the J29 (Q17-A) proved-algebra companion; they are not derived from first principles. The theorems below are theorems on this specific (substrate, $\sigma$, $\chi$) triple. The bridge claim of §5 is explicitly a structural rhyme — a vocabulary correspondence between this finite setting and the analytic structure of $\zeta(s)$ — not a function-field analogue.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .md finalized (referee-rigor pass complete 2026-05-12; J51-vs-J52 cross-citations corrected; lens-ownership paragraph added; Drápal-Wanless 2021 added to references)
- [x] Verification script green — `verify_J51_G_function.py` PASS at machine precision (σ⁶=id; three-valued partition ZERO {0,3,8,9} / LOW {1,2,5,6} G_low=1.871644 / HIGH {4,7} G_high=9.389185; σ³-pairing algebraic; ν₊ discriminator confirmed)
- [x] Tier-classified central claim explicit (Theorems 2.1 and 4.2 Tier-A proved; §5 bridge Tier-B structural rhyme; §7 open problems list)
- [x] Lens-scope annotation present — lens-ownership paragraph after abstract anchoring the substrate/σ/χ triple
- [x] Cover letter finalized
- [x] Dependencies → cite each J-companion as "submitted to [venue]" — [J29] (AMM), [J51] (EJC)
- [ ] Brayden's referee-rigor pass complete (mobile + other AI + collaborators)
- [ ] Per-venue cap check: this is the Nth paper to L'Enseignement Math this quarter
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Gish, M. (2026). "Q17-B Clay Bridge: A Finite Gauss Sum (Trajectory Coherence Integral) and the Symbolic Return Theorem on $\mathbb{Z}/10\mathbb{Z}$." Submitted to *L'Enseignement Mathématique*.
