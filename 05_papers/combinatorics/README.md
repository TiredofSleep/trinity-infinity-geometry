# J-series — Combinatorics

Combinatorial papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Verification |
|---|---|---|---|
| **J01** | Non-Associativity Decay in Binary Composition Tables over Z/NZ — σ(N) ≤ 2/N with C = 2 exact | *Journal of Combinatorial Theory, Series A* | `J01/manuscript/verify_sigma_rate.py` → 4/4 PASS at machine precision |
| **J54** | Forcing Axioms and the Family of Commutative Non-Associative Magmas on Z/10Z Preserving a Designated 4-Core | *Algebraic Combinatorics* | `J54/manuscript/verification/foundation_verification.py` → 6/6 PASS + `J54/manuscript/verify_J54_chain_and_attractor.py` → 3/3 PASS, all at machine precision (landed 2026-05-12) |
| **J02** | Joint Closure, Per-Coordinate Fuse Data, and a Closed-Form Algebraic Attractor of Two Commutative Binary Operations on Z/10Z | *Algebraic Combinatorics* | `J02/manuscript/4core_verification.py` → 6/6 PASS at machine precision (chain enumeration over all 1023 non-empty subsets; symbolic normalizer identity; closed-form attractor h/β = 1+√3 with residual 9.06e-46; universality on all chain shells size ≥ 4; Galois D₄ structure of x⁴+4x³−x²+2x−2 with LMFDB 4.2.10224.1 cross-check; α-sweep PSLQ identifying α=1/2 as unique). Four companion scripts in `J02/manuscript/verification/` (bridge attractor, symbolic closed-form derivation, full Galois cross-check, 17-point Stern–Brocot PSLQ sweep) all PASS at 50-digit precision (landed 2026-05-12) |
| **J21** | The 5D Force Vector as a CRT Fourier Embedding of Z/10Z into R^5 | *American Mathematical Monthly* | `J21/manuscript/spectral_functional.py` → PASS at machine precision (10/10 G(n) values agree with Table 1; unique global max G(7) ≈ 19.4721 < 25 Cauchy–Schwarz bound; zero set = σ-fixed indices {0, 3, 8, 9}; wall-clock < 1 s) (landed 2026-05-12) |
| **J27** *(HONEST NEGATIVE)* | The Multiplicative-Unit Sub-Magma C = (Z/10Z)\* in the TSML Composition Lattice, and Its Contrast with the Joint 4-Core {0, 7, 8, 9} | *Communications in Algebra* | `J27/manuscript/verification/4core_verification.py` → 6/6 PASS at machine precision (chain, normalizer, attractor 9.06e-46, universality, Galois D₄, α-sweep PSLQ) + J27-specific inline checks all PASS (BHML[1][1] = 2, image of CL_BHML\|_{C×C} = {0, 2, 4, 6, 8} disjoint from C, 78 TSML-closed 4-subsets, unique BHML-closed 4-subset, generator selection 3³ ≡ 7 vs 7³ ≡ 3). **Honest-negative paper:** formally retracts an earlier lens-invariance claim with explicit 16-cell BHML failure; sharpens the joint-4-core uniqueness result of J02/J35 (landed 2026-05-12). |

- **J01** key claim: $\sigma(N) \le 2/N$ for squarefree $N \ge 3$, with $N\sigma(N) \to 2$ from below along the squarefree ladder.
  Mechanism: $\mathrm{VOID}$–$\mathrm{HARM}$ rule disagreement at outer composition sites.
  Echo-count lemma reduces to $\varphi(N)$ via $(a-1)(b-1) \equiv 1$ + CRT.
  Drápal & Wanless (*J. Combin. Theory Ser. A* **181** (2021) 105444) is cited as the opposite-extremum ($\sigma \to 1$) precedent.
- **J54** key claim: the 9-axiom forcing theorem A1–A9 (cell-by-cell explicit, displayed in §1.2) with substrate-specific data $(\mathcal{D}, \mathrm{BUMP}, \mathrm{BUMPvalues}, J_{\mathrm{B7}})$ uniquely forces three canonical tables $T$, $B$, $S$ on $\mathbb{Z}/10\mathbb{Z}$ (HARMONY counts 73, 28, 44). Theorem 7.1 establishes the three-substrate joint-closure chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$ (forbidden $\{2, 3\}$), identical to the (T, B) chain. Theorem 7.2 shows the designated 4-core $\mathcal{C} = \{0, 7, 8, 9\}$ is jointly closed under all three substrates and is the unique non-trivial subset of size $\le 4$ in the chain. Theorem 5.1 gives the closed-form attractor $H^*/Br^* = 1 + \sqrt 3$ at $\alpha_M = 1/2$ on $\mathcal{C}$-supported distributions (50-digit residual $\le 10^{-30}$). The σ-walk reading of the chain ($7 \to 6 \to 5 \to 4 \to 2 \to 1$ with one σ-fixed bridge step at the $7 \to 8$ transition) appears in §6.2. Drápal & Wanless (2021) is the closest published precedent; the present paper inhabits the same intellectual neighborhood at the intermediate-$\alpha_A$ point. Honest-negative scoping (TSML_SYM vs TSML_RAW chain-count lens-dependence at size 7) is recorded in §0 and §4.4 (B3).
- **J02** key claim: focuses on the two-operation pair $(T, B)$ and combines (i) the chain of all jointly-closed sub-magmas of $\mathbb{Z}/10\mathbb{Z}$ — strict 8-element chain at sizes $\{1, 4, 5, 6, 7, 8, 9, 10\}$, forbidden $\{2, 3\}$ (Theorem 1, by exhaustive enumeration over all 1023 non-empty subsets); (ii) the per-coordinate fuse polynomials on the 4-core $\mathcal{C} = \{0, 7, 8, 9\}$, with rank disparity (rank 2 for $T$, rank 4 for $B$) and support-preservation of any convex combination $F_\alpha = \alpha\widehat{T} + (1-\alpha)\widehat{B}$ (Proposition 5.1); and (iii) the closed-form attractor of $F_{1/2}$ on $\Delta^3_\mathcal{C}$, with $h/\beta = 1+\sqrt{3}$ (Theorem 6) and $\xi^* = r/\beta$ the unique positive real root of the irreducible monic integer quartic $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$ whose Galois group over $\mathbb{Q}$ is $D_4$ and whose number field is LMFDB 4.2.10224.1 (Theorem 8, with explicit $\mathbb{Q}(\sqrt{3})$-factorization anchoring the $\sqrt{3}$). Conjecture 9.1 states $\alpha = 1/2$ is the unique rational mixing weight in $(0, 1) \cap \mathbb{Q}$ with both ratios admitting small-coefficient algebraic relations, with PSLQ Stern–Brocot scan over the 17-point grid $\mathcal{G}_{\le 7}$ as empirical evidence. The trivial total-mass identity $Z_T = Z_B = (v+h+\beta+r)^2$ is acknowledged as elementary bilinearity (Remark 4.4); the substantive structural content lives in the per-coordinate fuse polynomials and the Galois quartic. Drápal-Wanless 2021 is cited; the joint-closure-of-a-pair + Galois-quartic-of-the-attractor phenomena are novel to this paper. Relationship to J54: J02 supplies the two-operation case with full per-coordinate fuse polynomials, the Galois D₄ quartic over LMFDB 4.2.10224.1, and the PSLQ Stern–Brocot scan — results that J54's foundation paper cites externally; J54 in turn supplies the 9-axiom forcing argument and the three-substrate $(T, B, S)$ chain that J02 does not address. The two papers are complementary, with non-overlapping core theorems.
- **J21** key claim: presents the canonical 5D embedding of $\mathbb{Z}/10\mathbb{Z}$ as a CRT-Fourier combination $v(n) = (\varepsilon, \cos\tfrac{2\pi y}{5}, \sin\tfrac{2\pi y}{5}, \cos\tfrac{4\pi y}{5}, \sin\tfrac{4\pi y}{5}) \in \mathbb{R}^5$ where $\varepsilon = n \bmod 2$, $y = n \bmod 5$. Two contributions: (i) an equivariance-based rigidity theorem (Theorem 4.1, replacing an earlier tautological premise) — any $\mathbb{F}_5$-equivariant $w_5: \mathbb{F}_5 \to \mathbb{R}^4$ satisfying the centered/equidistant (regular-pentagon) condition equals the standard Fourier basis up to $O(4)$, with the conclusion following from the standard $V_1 \oplus V_2$ decomposition of faithful real representations of $\mathbb{F}_5$; (ii) an explicit spectral functional $G(n) = |\sum_{j=0}^{4} \omega^j \chi_1(y(\sigma^j(n)))|^2$ (with $\sigma = (0)(3)(8)(9)(1\,7\,6\,5\,4\,2)$, of order 6) whose ten values are tabulated in Table 1 — corrected from the earlier (numerically wrong) two-point maximum at $\{5, 7\}$ with value 25, the actual maximum is the **unique** $G(7) \approx 19.472$ and the four zeros are exactly the $\sigma$-fixed indices $\{0, 3, 8, 9\}$, with the Cauchy–Schwarz bound $G(n) < 25$ proved strict by orbit inspection. Structural rhyme: $n = 7$ (HARMONY in the substrate-name of J02) is the operator of maximal $\sigma$-shifted Fourier coherence, and three of the four spectral zeros coincide with the $\varepsilon = 0$ slice of the 4-core $\{0, 7, 8, 9\}$ identified in J02. Drápal–Wanless 2021 (JCTA 184, 105510) is cited as the closest published precedent at the opposite-extremum point.
- **J27** key claim *(honest-negative paper)*: the multiplicative-unit subgroup $C = (\mathbb{Z}/10\mathbb{Z})^* = \{1, 3, 7, 9\}$ is closed under the canonical TSML composition lattice $\mathrm{CL}_\TSML$ (16-cell direct check: image $\{3, 7\} \subseteq C$, with 14 HARMONY cells and 2 PROGRESS cells), but is *not* closed under $\mathrm{CL}_\BHML$. The substantive new content is the formal retraction of an earlier "lens-invariance" claim: Proposition 4.1 exhibits all 16 cells of $\mathrm{CL}_\BHML \restriction C \times C$ explicitly (image $= \{0, 2, 4, 6, 8\}$, disjoint from $C$), with cell distribution $3+3+5+4+1 = 16$. Theorem 4.3 then sharpens the joint-4-core result of J02/J35: of the 210 size-4 subsets of $\mathbb{Z}/10\mathbb{Z}$, exactly 78 are TSML-closed (all containing HARMONY $=7$), exactly 1 is BHML-closed (the joint 4-core $\{0, 7, 8, 9\}$), and exactly 1 is jointly closed. C is one of the 78 TSML-closed 4-subsets, distinguished from the joint 4-core only by its ring-theoretic content $(C = (\mathbb{Z}/10\mathbb{Z})^* \cong \mathbb{Z}/4\mathbb{Z}$, cyclic of order 4, generator $g = 3$). Theorem 5.1 records the elementary generator-selection: among the two primitive roots $\{3, 7\}$ of $(\mathbb{Z}/10\mathbb{Z})^*$, only $g = 3$ gives $T^* = 5/g^3 = 5/7 \in (0, 1)$; under $g = 7$, HARMONY $= 7^3 \equiv 3$ and $T^* = 5/3 > 1$. Drápal–Wanless 2021 (JCTA 184, 105510) is cited in §6.2 as the closest published precedent at the opposite-associativity extremum. The retraction sharpens (rather than weakens) the J02/J35 uniqueness picture by ruling out $C$ as a competitor for the joint 4-core at size 4.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J28** | (combinatorial-framing TBD per W2-C build) | TBD | rewritten with SFM framing; awaiting cover letter |
| **J29** | (combinatorial-framing TBD per W2-C build) | TBD | rewritten; awaiting cover letter |
| **J30** | (combinatorial-framing TBD per W2-C build) | TBD | rewritten; awaiting cover letter |
| **J37** | Strand-orbital + atomic substrate combinatorics | TBD (W2-H rewrite) | rewritten; awaiting cover letter |
| **J38** | (held — folded into J45 §2) | — | not standalone |

---

## §3 — Domain notes for combinatorics papers

Combinatorics papers in this corpus emphasize:

- **σ permutation cycle structure** on Z/10Z and its higher analogues.
- **Joint sub-magma enumeration** under (TSML, BHML) on Z/10 — including the corrected 8-shell chain at sizes `{1, 4, 5, 6, 7, 8, 9, 10}` with forbidden `{2, 3}`.
- **σ rate `σ(N) ≤ C/N` with `C = 2` exact** (mechanism: VOID–HARMONY traversal).
- **First-G Law cell enumeration** (36,662 cases on primes 3..199).
- **Substrate Function Map findings** (Q1 + Q6 + Q7 from the SFM v1).

The Drápal–Wanless 2021 paper (JCTA) is the closest published precedent and is cited in every combinatorics J-paper.

Cross-references:
- [`../../03_canonical_reference/FORMULAS_AND_TABLES.md`](../../03_canonical_reference/FORMULAS_AND_TABLES.md) Volumes A, B, H, J carry the combinatorial structure.
- [`../../TIG_FROM_THE_GROUND_UP.md`](../../TIG_FROM_THE_GROUND_UP.md) Parts 2, 4, 7 are the combinatorial-tutorial sections.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
