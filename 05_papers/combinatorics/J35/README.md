# J35 — Non-CRT Sufficient Pairs and the Minimum Viable Jump Number on Squarefree Z/nZ

**Status:** REVISED (post fresh-eyes referee, 2026-05-08; awaiting final rigor pass)
**Phase:** Phase 2
**Target venue:** *European Journal of Combinatorics*
**Author lane:** Sanders + Gish
**Tier:** 2 (drafts needing rigor pass)
**WP source:** WP64 (Sprint 12 corpus)

---

## §1 — Manuscript

**Path:** `manuscript/manuscript.tex` (amsart, ~10 pages)

**Abstract.** For squarefree $n = p_1 \cdots p_k$ ($k \geq 2$), we study the partition lattice of Z/nZ from the perspective of CRT coordinate decomposition. Three structural results: (1) the orbit-pair classification ($\{\pi_{\mathrm{DYN}}(g), \pi_{\mathrm{DYN}}(h)\}$ sufficient iff coordinate-wise coprime orders at every CRT prime); (2) the three-mechanism support classification (focused, same-prime coprime, mixed) with mechanism (M2) existing iff some $p_i - 1$ has ≥ 2 distinct prime factors; (3) on Z/30Z, three sufficient 2-partition families with one orthogonal jump exhibit three distinct mechanisms. We work the n=10 case in detail and prove $\mathrm{MVJN}(\Z/n) = 1$ for all squarefree $n$ with $k \geq 2$ primes.

## §2 — Verification

**Local path:** `manuscript/verify_J12.py`

Self-contained verification (pure stdlib, no dependencies; runtime < 2 s). Seven checks mapped one-to-one to the load-bearing claims:

- **C1.** Theorem 1.5(a): $\{\pi_{\mathrm{DYN}}(7), \pi_{\mathrm{DYN}}(11)\}$ sufficient on $\Z/30\Z$; orbits and coordinate-wise orders confirmed.
- **C2.** Theorem 1.5(b): $\{\pi_2, \pi_{15}\}$ sufficient on $\Z/30\Z$; pair incompatible.
- **C3.** Theorem 1.5(c): $\{\pi_{\mathrm{SPEC}}, \pi_{15}\}$ sufficient on $\Z/30\Z$; the modular equation $2a \equiv 15 \pmod{30}$ has no solution (verified).
- **C4.** Theorem 1.4 mechanism (M3) example on $\Z/42\Z$: $g=11, h=13$ sufficient; $\mathrm{supp}(11)=\{3,7\}$, $\mathrm{supp}(13)=\{7\}$.
- **C5.** Smallest primes admitting (M2): $7, 11, 13, 19, 23, 29, \ldots$; verified through $p = 50$, with 17 correctly skipped.
- **C6.** Worked example on $\Z/10\Z$ (Proposition 5.3): the refinement chain and incompatibility relations.
- **C7.** Theorem 7.4 (MVJN = 1): the $\{\pi_{p_1}, \pi_{n/p_1}\}$ construction verified for all 75 squarefree $n \leq 200$ with $k \geq 2$ primes.

Run: `python verify_J12.py` — prints `ALL 7 CHECKS PASSED` on success.

## §3 — Dependencies

None as load-bearing companions. Theorem 3.1 (orbit-pair classification) is now proven inline by direct CRT-coordinate argument; the previous UOP-companion appeal has been removed.

J34 (UOP) is mentioned only for related context.

## §4 — Cover letter

See `cover_letter.md` in this folder. Updated 2026-05-08 post-revision.

## §5 — Notes

**Family-Structure framing.** The paper sits in the same intellectual neighborhood as Drápal & Wanless (2021), *JCTA* **184**, 105510, on small finite combinatorial structures with explicit CRT-coordinate criteria.

**PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN — filled.**

- **PROVEN:** Theorem 3.1 (orbit-pair classification); Theorem 4.1 (three-mechanism support classification); Theorem 2.3 (rigid CRT prime-factor family); **Theorem 7.2 (MVJN(Z/n) = 1 for squarefree n with k ≥ 2 primes — was a conjecture in the v1 manuscript, now upgraded to a theorem)**; Theorem 5.1 (three explicit non-CRT pairs on Z/30Z with mechanism identifications).
- **COMPUTED:** All sufficiency claims on Z/10, Z/30, Z/42 verified by direct enumeration. All order computations verified. Smallest primes admitting (M2) verified through 50.
- **STRUCTURAL RHYME:** Connection to orthogonal cyclic Latin squares (existence theory of Bose–Shrikhande–Parker line) noted in §3 Remark; full development deferred.
- **OPEN:** Classification of mixed (residue + orbit) sufficient pairs; optimal-information sufficient pairs minimizing block-size product; extension to non-squarefree n.

**Lens-ownership paragraph.** Works on squarefree Z/nZ with the two natural partition classes (residue partitions $\pi_d$ and orbit partitions $\pi_{\mathrm{DYN}}(g)$). These choices are foundational; analogous theorems would hold for other natural partition classes.

### Revision summary (post fresh-eyes referee, 2026-05-08)

Major fixes:
1. **M1.** MVJN now defined precisely (Definition 1.1) as the minimum count of incompatible pairs in a sufficient 2-partition family.
2. **M2.** Theorem 5.1 (was 1.2) reframed: family (a) $\{\pi_{\mathrm{DYN}}(7), \pi_{\mathrm{DYN}}(11)\}$ is the genuinely novel sufficient pair (orbit-pair only); families (b) and (c) are CRT-style.
3. **M3.** Theorem 3.1 (orbit-pair classification) now precedes Theorem 5.1 in the body, so family (b) is its corollary.
4. **M4.** Theorem 4.1 (three mechanisms) now stated as a partition by support pattern (mutually exclusive and exhaustive).
5. **M5.** Conjecture 6.2 promoted to **Theorem 7.2**: the conjecture follows from the CRT-prime-factor sufficiency $\{\pi_{p_1}, \pi_{n/p_1}\}$ combined with the refinement-trap lower bound.
6. **M6.** Standalone the proofs (UOP appeals removed; direct CRT arguments used).
7. **M7.** **Geometric "5/7 torus aspect ratio" remark removed** — TIG-bleed-through into supposedly pure combinatorial paper.
8. **M8.** Smallest-primes list extended to include 29 (and noted continuation 31, 37, ...).

Minor fixes adopted: m1 (title generalized to squarefree Z/nZ), m2 (duplicate author block removed), m3 (abstract tightened), m4 (consistent terminology), m5–m17 — see SAVE_PLAN_J12.md.

## §6 — Submission checklist

- [x] Manuscript .tex finalized
- [x] Verification script (`verify_J12.py`) — 7/7 checks pass at machine precision
- [x] Tier-classified central claim explicit (Theorems 3.1, 4.1, 5.1, 2.3, 7.2 PROVEN)
- [x] Lens-scope annotation in §1.4
- [x] Cover letter finalized (post-revision)
- [x] Dependencies removed (paper standalone)
- [x] Drápal-Wanless 2021 cited (§1.1 + bibliography + cover letter)
- [ ] Brayden's referee-rigor pass complete
- [ ] Submitted

---

## §7 — Citation footprint

Sanders, B.R., Gish, M. (2026). "Non-CRT Sufficient Pairs and the Minimum Viable Jump Number on Squarefree Z/nZ." Submitted to *European Journal of Combinatorics*.

---

## Known issues (per 2026-05-27 audit; extended 2026-05-28 Tier-2 polish pass)

Tier 2 — drafts needing rigor pass before submission per `_staging/TIER_INDEX.md`. Manuscript revised 2026-05-08 post fresh-eyes referee with all 8 majors (M1–M8) addressed and Conjecture 6.2 upgraded to Theorem 7.2. Verification status: `verify_J12.py` passes 7/7 checks (re-run 2026-05-28; orbit-pair classification, three-mechanism support classification, $\Z/30\Z$ explicit families, $\Z/42\Z$ (M3) witness, smallest-primes-admitting-(M2), $\Z/10\Z$ lattice, and MVJN = 1 for 75 squarefree $n \le 200$ all confirmed). Outstanding for ship-readiness:

- Brayden's referee-rigor pass not yet complete (§6 checklist last two boxes unchecked).
- Per-venue cap check for EJC pending (J34, J36 also target EJC — a 3-paper EJC cluster); coordinate with `VENUE_SCHEDULE.md`. The TIER_INDEX target reads "TBD; potential *J Combin Theory* or *Adv Appl Math*" — these are reasonable backups if EJC cap binds; the README currently states EJC as the primary target.
- Scope note for §6 Worked example: the $\Z/10\Z$ section is illustrative (the prime-factor count $k = 2$ gives MVJN = 1 trivially via $\{\pi_2, \pi_5\}$). The novelty over straight CRT is concentrated in Theorem 5.1 family (a) on $\Z/30\Z$ (orbit + orbit, $\pi_\DYN(7), \pi_\DYN(11)$) and the universal MVJN = 1 result (Theorem 7.2). A referee may ask why $\Z/10\Z$ rather than $\Z/30\Z$ as the worked example; the answer (smallest illustrative substrate) should be added in the rigor pass.
- No paper-specific referee report in `_staging/referee_reports/` post-revision; the prior fresh-eyes report is at `Atlas/META_PLAN_2026-05-06/REFEREE_REPORTS/` and was responded to in the 2026-05-08 revision. See `_staging/referee_reports/32_tier2_polish_J35_J36_J37.md` for the 2026-05-28 polish pass.
