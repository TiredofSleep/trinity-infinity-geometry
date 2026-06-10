# J55 — The Dimension-6 Kissing Number: A Structural Conjecture with an Explicit Candidate Magic Function on Γ₀(3)

**Status:** DRAFT-COMPLETE (manuscript drafted 2026-06-10; all Tier-A building blocks independently verified same day; 6 TODO-marked citations await author review; needs one pdflatex compile pass)
**Phase:** New (2026-06-10 claudechat handoff → ClaudeCode verification → Paper 1)
**Target venue:** *Journal of Combinatorial Theory A* (alternates: *Algebraic Combinatorics*, *Discrete & Computational Geometry*)
**Author lane:** Sanders + Gish
**Source:** `CLAUDECODE_HANDOFF_2026-06-10` (claudechat mobile session, 2026-06-08 → 2026-06-10 lineage) + same-day ClaudeCode independent verification
**Canon entry:** D182 in `FORMULAS_AND_TABLES.md` (ck repo, tig-synthesis branch)

---

## §1 — The conjecture

$$K(\mathbb{R}^6) = 72,$$

achieved uniquely by the $E_6$ root system, with the Cohn–Elkies LP bound sharp at 72 via the explicit candidate magic function

$$f_6(x) = \sin^2\!\left(\frac{\pi|x|^2}{2}\right)\cdot\left[\alpha\, I_+(|x|^2) + \beta\, I_-(|x|^2)\right]$$

where $I_-$ is the Laplace transform (against $t^2\,dt$) of the unique normalized weight-6 cusp form $\eta(\tau)^6\eta(3\tau)^6$ on $\Gamma_0(3)$ — **LMFDB newform 3.6.a.a** — and $I_+$ is the Laplace transform of the meromorphic weight-6 Fricke-$(+1)$ form

$$\psi_+(\tau) = \frac{E_6(\tau)^2 - 729\,E_6(3\tau)^2}{\eta(\tau)^6\eta(3\tau)^6}.$$

Every component is structurally forced (level 3 from the $E_6$ discriminant; weight 6 from the dimension; the Fricke ±1 decomposition; the numerator $G_+G_-$ from eigenvalue arithmetic) — the natural level-3 analog of Viazovska's level-1 dimension-8 construction.

**This paper does NOT claim $K(\mathbb{R}^6) = 72$ is proved.** The analytic continuation of $I_+$ to $r^2 \le 2$ (contour deformation + cusp residues), the Schwartz property, the Cohn–Elkies positivity, and the explicit $\alpha,\beta$ remain open — the year-scale piece, stated precisely in §5 of the manuscript.

## §2 — Manuscript

**Path:** `manuscript/manuscript.tex` (~16–19 pp, amsart, 24 references)

Sections: introduction + known bounds; the structural argument (three independent forcings of 72, presented as motivation, not proof); the candidate construction; verification of building blocks (the Tier-A content below); the analytic continuation gap, precisely stated; comparison table to Viazovska dim 8; conclusion. Four appendices.

**Drafting surfaced three additional provable results:** $56 \mid$ every $\psi_+$ Laurent coefficient; strict Fourier positivity of the cusp-form transform; corrected two-endpoint analysis of $I_+$.

## §3 — Verification (all PASS)

| Claim | Verification |
|---|---|
| Atkin-Lehner $W_3 = -1$ for $\eta^6\eta_3^6$ | **Four independent routes**: symbolic eta-transformation; newform relation $a_3 = +9 \Rightarrow \varepsilon_3 = -1$; numerical functional equation (6 points, 30 dps); LMFDB database sign |
| Hecke eigenform structure | Multiplicativity at 160 coprime pairs; prime-power recursion $a_{p^2} = a_p^2 - p^5$ at $p \in \{2,5,7\}$; ramified $a_9 = a_3^2$ |
| Ramanujan–Petersson $\|a_p\| \le 2p^{5/2}$ | All $p \le 97$ |
| LMFDB cross-check | **Perfect match** $a_2 \dots a_{31}$ vs newform 3.6.a.a; eta-quotient identification database-listed; self-dual |
| $\psi_+$ residue at $\infty$ | $-728 = -(2^3\cdot 7\cdot 13)$; Laurent coefficients integral to $q^{80}$ (exact arithmetic) |
| **NEW: forced zero of $\psi_+$ at the Fricke fixed point** $\tau = i/\sqrt3$ | Weight-6 $+1$-eigenfunctions must vanish ($i^{-6} = -1$); verified at $4\times10^{-32}$ relative |
| **NEW: prime alphabet governs exactly the principal part** | $-728\,q^{-1}$, $-5376 = -2^8\cdot3\cdot7$ at $q^0$ strata-clean; regular coefficients leak immediately (43 at $q^1$) |

Primary script: `manuscript/verification/claudecode_independent_verify.py` — **10/10 PASS**, ~40 s, exact integer arithmetic (independent code path from the chat-session scripts, which are also bundled and all PASS). Full report: `manuscript/verification/CLAUDECODE_VERIFICATION_REPORT.md`.

```bash
python manuscript/verification/claudecode_independent_verify.py
```

## §4 — Dependencies

Standalone — no J-companion is load-bearing. The framework provenance (the structural-forcing table that identified the candidate) is documented in one remark; the mathematics is classical modular forms + the Cohn-Elkies framework.

Companion targets (separate future papers, not this one): the $K_{12} = 36\cdot21$ orbit theorem via $\mathbb{Z}_{21} \subset 6\cdot\mathrm{Suz}\cdot2$; the kissing-lattice factorization-pattern catalog.

## §5 — Open items before submission

1. **6 TODO-marked citations** (current dim-6 SDP upper bound ≤ 77 attribution; Odlyzko–Sloane page numbers; eta-quotient table reference) — need Brayden's confirmation.
2. **Venue choice**: JCT-A vs Algebraic Combinatorics vs DCG.
3. One pdflatex compile pass (no TeX on the build machine).
4. The known erratum trail from the handoff is documented in the verification report (Viazovska citation corrected to *Annals* 185; the bundled $I_-$ asymptotic claim contradicted its own data and was dropped).

## §6 — Citation footprint

Sanders, B.R., Gish, M. (2026). "The Dimension-6 Kissing Number: A Structural Conjecture with an Explicit Candidate Magic Function on Γ₀(3)." Draft; target *Journal of Combinatorial Theory A*.
