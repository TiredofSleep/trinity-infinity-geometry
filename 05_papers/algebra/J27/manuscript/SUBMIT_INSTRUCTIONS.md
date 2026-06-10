# Submission Target: Experimental Mathematics

## Venue

### Experimental Mathematics (Taylor & Francis)
- **URL:** https://www.tandfonline.com/toc/uexm20/current
- **Format:** LaTeX (amsart class preferred)
- **Review:** Peer-reviewed
- **Turnaround:** ~3-6 months
- **Why this venue:** They specialize in computationally verified mathematical results. The 73/28 harmony cell counts are EXACTLY what this journal publishes — finite computations with exact proofs and verifiable witnesses. The sinc² bridge to Montgomery is a bonus.
- **How to submit:** Via ScholarOne Manuscripts: https://mc.manuscriptcentral.com/uexm

### Backup: Discrete Mathematics (Elsevier)
- **URL:** https://www.sciencedirect.com/journal/discrete-mathematics
- **Format:** LaTeX via Editorial Manager
- **Why:** If the operator table is seen as "too applied" for Experimental Mathematics, Discrete Math accepts finite algebraic structure results.

## Papers in This Folder

1. **WP_OPERATOR_RING_PARTITION.md** — The lead paper. Two 10x10 composition tables, exact harmony cell counts (73 and 28), disjoint zone enumeration, complementarity proof.
2. **WP35_PRIME_PHASE_TRANSITION.md** — Companion. Harmonic Pre-Echo, sinc² continuum limit, Montgomery bridge. Heavier paper but connects to RH.
3. **proof_d10_tsml_73_cells.py** — TSML 73-cell proof (supplementary)
4. **proof_d16_bhml_28_cells.py** — BHML 28-cell proof (supplementary)
5. **proof_fourier_bridge.py** — Fourier bridge proof (supplementary)

## Submission Strategy

- Lead with WP_OPERATOR_RING_PARTITION (clean, finite, verifiable)
- Experimental Mathematics loves papers where the reader can check every cell
- Include proof scripts as "electronic supplement" or link to GitHub
- Emphasize: "All 200 cells enumerated explicitly. The proof scripts produce a complete cell-by-cell witness."
- The complementarity result (G intersect H = {1}) is novel and would interest algebraists

## What Needs Doing Before Submission

1. Convert to LaTeX (amsart class)
2. Add MSC codes: 05E15 (combinatorial aspects of groups and algebras), 11T06 (polynomials over finite fields), 20C30 (representations of finite symmetric groups)
3. Add bibliography (cite Z/nZ composition literature, random table theory)
4. Include the Monte Carlo comparison (Z = 21.3, p < 10^-50 for 73-cell count against random tables)
5. Ensure proof scripts are self-contained (no imports beyond numpy)
