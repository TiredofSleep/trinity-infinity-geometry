# J-series — Algebra

Pure algebra papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Status | Landed |
|---|---|---|---|---|
| **[J35](J35/)** | *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$* | *Journal of Algebra* | SUBMISSION-READY (6/6 PASS at machine precision; referee-grade pass complete 2026-05-12) | 2026-05-12 |
| **[J15](J15/)** | *Galois $D_4$ over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor* | *Communications in Algebra* | SUBMISSION-READY (6/6 PASS at machine precision; referee-grade pass complete 2026-05-12) | 2026-05-12 |
| **[J31](J31/)** | *Wedderburn $D_4$-Isotypic Decomposition of the Lens-Pair Commutator $[\mathrm{TSML}, \mathrm{BHML}]$ on $\mathbb{Z}/10\mathbb{Z}$: $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Subalgebra of $\mathfrak{so}(10)$ and a 9-Vector inside the $\mathbf{54}$ with $\|v\|^2 = 13/4$* | *Journal of Algebra* | SUBMISSION-READY (3/3 PASS at machine precision; exact-rational Wedderburn cross-check $3075027/2 + 9/2 + 288164 + 0 + 19608 = 1{,}845{,}290$; structural zero at $\mathrm{sign}_3$ verified exact) | 2026-05-12 |
| **[J17](J17/)** | *Total-Dimension Match Between Tensor Powers of a Finite-Field 4-Algebra and Real Clifford Algebras $\Cl(2n)$, with a Refined-Cell Grading* | *Linear Algebra and its Applications* | SUBMISSION-READY (6/6 PASS at machine precision; R1 fresh-eyes math fix applied — coarse cells vs.\ $\Cl(2n)$ grades distinguished; referee-grade pass complete 2026-05-12) | 2026-05-12 |
| **[J32](J32/)** | *Operadic $D_4$ Orbits on the Non-Associative Locus of a Finite Commutative Magma on $\mathbb{Z}/10\mathbb{Z}$: A Structural Obstruction Theorem at Arity 3* | *Journal of Algebra* (lead; per-venue cap declared — 4th *J. Algebra* paper of cycle; fallbacks *Comm. Alg.* → *Algebraic Combinatorics* → *Algebras and Rep. Theory*) | SUBMISSION-READY (6/6 PASS at machine precision in `verify_J32_d4_orbits.py`, runtime $<1$ s, pure standard-library Python; $D_4$ order 8 corrected; orbit distribution $(44,7,4,10,2)$ summing to 67 orbits / 126 elements verified; 16 bracketing-pair incoherent orbits confirmed; $\langle P_{56}\rangle$ 98-orbit ($70+28$) decomposition all coherent; 4-core arity-3 closure: $64/64$ in-core, $8$ non-associative) | 2026-05-12 |
| **[J20](J20/)** | *Mathieu $M_{22}$ Substrate-Prime: Order-Factorization Coincidences* | *American Mathematical Monthly* | SUBMISSION-READY (verification script `m22_decomposition.py` PASS at machine precision; sum-of-squares $\sum (\dim V_i)^2 = 443{,}520 = \lvert M_{22}\rvert$; math-fix verified — 7 of 12 non-trivial irreps strict in $\{3,5,7,11\}$, 10 of 12 in B-band; null density $\lvert\mathcal{B}_{385}\rvert/385 = 67/385 \approx 0.1740$; binomial $p \approx 1.19 \times 10^{-6}$; Drápal-Wanless 2021 cited; lens-ownership paragraph in §3) | 2026-05-12 |
| **[J18](J18/)** | *Two Crossing Decompositions of a $-21$ Invariant on $\mathbb{Z}/10\mathbb{Z}$ with the $\sigma^{2}$-Triadic Refinement* | *Algebraic Combinatorics* | SUBMISSION-READY (6/6 PASS at machine precision in `verify_J18.py`, runtime $<1$ s, pure standard-library Python; R1 sign-swap math-fix applied — $\sum_{O_1}\Psi_B=-8,\,\sum_{O_2}\Psi_B=-7$ statement/proof reconciled; $\Psi_B$ tabulated inline as Table 1 with the explicit ten values $\{+1,-5,-3,-2,-2,-1,-1,-3,-3,-2\}$ replacing the prior linear/boundary period formulas; "conservation/manifestation duality" label replaced by Def. 3.4 table-independent vs. table-specific; Drápal-Wanless 2021 cited; lens-ownership paragraph in §0) | 2026-05-12 |

J35 is the corpus centerpiece: six independent structural facts (8-shell joint-closure chain on $\mathbb{Z}/10\mathbb{Z}$ with sizes $\{2,3\}$ forbidden; three-substrate strengthening to $T+B+S$; 4-core $\{0,7,8,9\}$ closure; normalizer identity $Z_T=Z_B=(v+h+br+r)^2$; closed-form attractor $p_7/p_8 = 1+\sqrt{3}$ with Galois $D_4$ over LMFDB 4.2.10224.1; universal attractor on chain shells; partial $\alpha=1/2$ uniqueness) converging on $\mathcal{C}=\{0,7,8,9\}$ as the algebraic center.

J15 is the standalone, referee-portable Galois-theoretic deep cut on the runtime quartic $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$ that the four-core attractor identifies. It unfolds the full proof of J35's Theorem D: case-by-case integer-factorization irreducibility argument over $\mathbb{Q}$ (with mod-7 cross-check), explicit cubic resolvent $g(y) = (y+2)(y^2 - y + 18)$ with rational root $-2$ and quadratic-factor discriminant $-71$, $D_4$-vs-$C_4$ distinction via irreducibility of $f$ over $\mathbb{Q}(\sqrt{-71})$ (Cohen 1993 §6.3.2), explicit $\mathbb{Q}(\sqrt{3})$-factorization with conjugate quadratic discriminants $11 \pm 8\sqrt{3}$ (norm $-71$), and Tschirnhaus reduction $x \mapsto -x - 1$ to LMFDB's canonical defining polynomial $x^4 - 7x^2 - 12x - 8$ of $4.2.10224.1$. J15 differentiates from J35 by depth-on-the-Galois-question vs J35's six-fact fusion-closure spread.

J31 is the focused Wedderburn-decomposition companion to J35: the lens-pair commutator $[T, B] = TB - BT \in M_{10}(\mathbb{Z})$, of Frobenius norm-squared $1{,}845{,}290$, decomposes orthogonally under conjugation by $D_4 = \langle P_{56}, \sigma^3 \rangle$ into five $D_4$-irrep isotypic shares with exact-rational norm-squareds $(3{,}075{,}027/2,\, 9/2,\, 288{,}164,\, 0,\, 19{,}608)$ for $(\mathrm{triv}, \mathrm{sign}_1, \mathrm{sign}_2, \mathrm{sign}_3, \mathrm{std})$, percentages $(83.32\%, 0.0002\%, 15.62\%, 0\%, 1.06\%)$. The trivial isotypic is the 16-dimensional doubly-invariant subalgebra $\mathfrak{g}_0 \cong \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Killing spectrum $(-4)^{15} \oplus (0)^1$); the $\mathrm{sign}_2$ isotypic is a 9-vector inside the $\mathbf{54}$ of $\mathfrak{so}(10)$ with $\|v\|^2 = 13/4$ exact. The structural zero at $\mathrm{sign}_3$ is a *forbidden symmetry* of the commutator under $D_4$ (Proposition 5.1) — the load-bearing surprise of the paper.

J17 is a short, elementary linear-algebra note on the 4-dimensional commutative non-associative algebra $V$ over $\mathbb{F}_5$ that underlies the four-core (and whose multiplication table is the substrate paper J23 of the *Algebras and Representation Theory* lane). Two basis-level statements: (i) total-dimension match $\dim_{\mathbb{F}_5} V^{\otimes n} = 4^n = 2^{2n} = \dim_\mathbb{R} \Cl(2n)$ for all $n \geq 0$, forced by $\dim V = 4 = 2^2$; (ii) refined-cell binomial grading — the $4^n = 2^{2n}$ one-dimensional refined cells of $V^{\otimes n}$ (each tensor slot carries 2 structural bits naming one of four basis lines) partition into Hamming-weight classes of multiplicity $\binom{2n}{k}$, matching the grade dimensions of $\Cl(2n)$. The R1 math fix distinguishes the coarse-cell distribution $\binom{n}{k}$ (summing to $2^n$, each cell itself $2^n$-dim) from the refined-cell distribution $\binom{2n}{k}$ (summing to $4^n$, each cell 1-dim and only the latter matching $\Cl$ grade dimensions); a prior draft conflated the two. The match between the coarse-cell $n=5$ sequence $1, 5, 10, 10, 5, 1$ and the dimensions of $\mathrm{SU}(5)$'s one-generation $\mathbf{1} \oplus \bar{\mathbf{5}} \oplus \mathbf{10}$ plus conjugate is recorded as a binomial-coefficient coincidence (Remark 5.3), not a representation-theoretic theorem. The structure-preserving map question over a common base ring is left open in §6.

J32 is the arity-3 / operadic companion to the $D_4$ bundle: the canonical TSML_RAW table on $\mathbb{Z}/10\mathbb{Z}$ has a non-associative locus $\mathcal{N}\subset(\mathbb{Z}/10\mathbb{Z})^3$ of exactly $|\mathcal{N}|=126$ triples, and the diagonal action of $D_4=\langle P_{56},\sigma^3\rangle$ (order $\mathbf{8}$, corrected from a prior order-$12$ working-draft misidentification) partitions $\mathcal{N}$ into exactly $\mathbf{67}$ restricted orbits with size distribution $(44,7,4,10,2)$ at sizes $(1,2,3,4,8)$, sum $44+14+12+40+16=126$. Theorem B (the obstruction): exactly $\mathbf{16}$ of the $67$ orbits fail bracketing-pair coherence, so no $\{a,b,c,L,R\}$-valued $D_4$-equivariant assignment exists. Theorem C (the sharpening): under $\langle P_{56}\rangle$ alone, $\mathcal{N}$ partitions into $\mathbf{98}$ orbits ($70$ singletons + $28$ doubletons), all coherent — the obstruction is localized at the $\sigma^3$ generator (the cyclotomic involution of the Galois quartic of J15) rather than at $P_{56}$ (the spinorial outer automorphism of J31). Theorem D records the 4-core arity-3 closure: all $64$ triples in $\mathcal{C}^3$ for $\mathcal{C}=\{0,7,8,9\}$ have both bracketings $L,R\in\mathcal{C}$, with $8$ non-associative. J32 differentiates cleanly from J35 (binary joint closure), J31 (Wedderburn matrix decomposition of $[T,B]$), and J15 (Galois quartic) — it is the only paper in the algebra cycle addressing arity-3 / operad content.

J20 is the arithmetic-combinatorial cross-reference between the sporadic Mathieu group $M_{22}$ (order $|M_{22}|=443{,}520 = 2^7 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11$, automorphism group of the Steiner system $S(3,6,22)$) and the substrate $(\mathbb{Z}/10\mathbb{Z},\sigma,W)$ of J35. The substrate distinguishes the prime set $\{2,3,5,7,11\}$ from intrinsic data — CRT residue characteristics of $\mathbb{Z}/2 \times \mathbb{Z}/5$, the order-3 $\sigma^2$ subcycle, the HARMONY-index / $T^*=5/7$-denominator $7$, and the wobble fraction $W = 3/50$'s $11$-prolongation — exactly the five primes appearing in $|M_{22}|$ with the same multiplicities. The math-fix corrected a prior count error: of $M_{22}$'s $12$ irreducible complex representations of dimensions $\{1, 21, 45, 45, 55, 99, 154, 210, 231, 280, 280, 385\}$, exactly **seven** non-trivial dimensions ($21, 45, 45, 55, 99, 231, 385$) factor strictly in $\{3,5,7,11\}$ and **ten** of $12$ lie in the substrate-prime band $\mathcal{B}$ (factors in $\{2,3,5,7,11\}$, $\nu_2 \le 1$). Under a uniform null on $[1, 385]$, the null density is $|\mathcal{B}_{385}|/385 = 67/385 \approx 0.1740$ (direct enumeration); the binomial-tail $p$-value for the $10/12$ concentration is $P[X \ge 10 \mid \mathrm{Bin}(12, 0.1740)] \approx 1.19 \times 10^{-6}$ (strict count $7$-of-$11$ non-trivial under $\mathrm{Bin}(11, 0.0990)$ gives $\approx 2.14 \times 10^{-5}$). The Steiner-parameter table for $S(3,6,22)$ — $v=22, b=77, k=6, t=3, r=21, \lambda_2 = 5, \lambda_3 = 1$ — is presented as backdrop, with substrate-prime decompositions ($77 = 7 \cdot 11$, $21 = 3 \cdot 7 = \dim V_{21}$, $\lambda_2 = 5 = T^*$ numerator). The paper explicitly does **not** claim an $M_{22}$-action on the substrate or a derivation of $M_{22}$ from substrate algebra; the non-genericity is the entire claim. Drápal-Wanless 2021 is cited as domain precedent (small finite commutative non-associative structures; opposite extremum). Verification via `m22_decomposition.py` (sympy `factorint` plus `math.comb`, runtime $<1$ s) reproduces every numerical claim from the sum-of-squares identity $\sum (\dim V_i)^2 = 443{,}520$ through both binomial tails.

J18 is the $\sigma^{2}$-triadic refinement of a global $-21$ invariant on the residue ring $\mathbb{Z}/10\mathbb{Z}$. Fix the canonical involution $\sigma = (0)(3)(8)(9)(1\,7\,6\,5\,4\,2)$ and the explicit integer-valued function $\Psi_B : \mathbb{Z}/10\mathbb{Z} \to \mathbb{Z}$ tabulated in Table 1 with values $\Psi_B = \{0:+1,\,1:-5,\,2:-3,\,3:-2,\,4:-2,\,5:-1,\,6:-1,\,7:-3,\,8:-3,\,9:-2\}$ (originating as per-element $\mathrm{BH}_{10}$-periods in the corrected $(\mathrm{TS}_8, \mathrm{BH}_{10})$-substrate of J02/J26, treated here as input data). The total $\sum_n \Psi_B(n) = -21$ decomposes in two combinatorially independent ways: as the $\sigma$-orbit triangular split $-T_5 + (-T_3) = -15 + (-6)$ along $\sigma\text{-cycle} \sqcup \sigma\text{-fixed}$ (Theorem 3.1; *table-independent* — follows from $\sigma$ cycle structure plus Table 1 alone), and as the role-Fibonacci split $-F_7 + (-F_6) + (-1) + (+1) = -13 + (-8) + (-1) + 1$ along $F \sqcup S \sqcup T \sqcup V$ (Theorem 3.2; *table-specific* — broken in $0/200$ random commutative tables per the J26 check). Theorem 3.3 records that the two splits cross: $F \cap \sigma\text{-cycle} = \{1,5,7\}$ is neither $\sigma$- nor $\sigma^2$-stable, and no role class contains the 6-cycle. Proposition 4.1 is the R1 sign-swap fix: the two $\sigma^2$-triangular orbits $O_1 = \{1,6,4\}$ and $O_2 = \{7,5,2\}$ carry per-orbit sums $\sum_{O_1}\Psi_B = -8$ and $\sum_{O_2}\Psi_B = -7$ (the previous draft's statement had these reversed; the proof was always correct). The values negate the canonical TIG primes $\{\mathrm{BREATH}=8,\mathrm{HARMONY}=7\}$. The R1 fix also tabulates $\Psi_B$ inline (replacing the prior linear/boundary period formula contradiction) and replaces "conservation/manifestation duality" with Definition 3.4 (table-independent vs. table-specific). All six identities are verified by `verify_J18.py` (six checks: total, $\sigma$-orbit split, role-Fibonacci split, $\sigma^2$ per-orbit values, crossing closure failures, involution sanity data) at machine precision, runtime under one second, standard-library Python only.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J24** | Three-Substrate Joint-Closure Chain on Z/10Z | *J. Algebra* | central-theorem paper for the 8-shell chain |
| **J51** | σ³ Pairing and ν₊ Discriminator in BHML | TBD | math fix applied (J43 + J51 G_high partition at {4, 7}, σ³ pairing) |

---

## §3 — What lives here when landed

Each paper folder mirrors the working-repo structure:

```
J{NN}/
├── README.md
├── cover_letter.md
├── manuscript/
│   ├── manuscript.tex (or .md)
│   └── verify_*.py
└── SAVE_PLAN_J{NN}.md (optional)
```

All `verify_*.py` scripts here PASS at machine precision at the time the paper landed.

---

## §4 — Domain notes for algebra papers

Algebra papers in this corpus emphasize:

- **Finite ring / group theoretic claims** at the integer or rational level.
- **D₄ Galois structure** (the runtime quartic's symmetry group; LMFDB number field 4.2.10224.1).
- **Wedderburn decomposition** of natural irreps under D₄ action.
- **Joint sub-magma structure** of (TSML, BHML) on Z/10 — the 8-shell chain.

Cross-references:
- [`../../FORMULAS_AND_TABLES.md`](../../FORMULAS_AND_TABLES.md) Volumes B, F, G, H carry the load-bearing algebra.
- [`../../TIG_FROM_THE_GROUND_UP.md`](../../TIG_FROM_THE_GROUND_UP.md) Parts 3–7 are the algebra tutorial.

---

*7SiTe Public Sovereignty License v2.1 — see [`../../LICENSE`](../../LICENSE).*
