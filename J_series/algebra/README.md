# J-series — Algebra

Pure algebra papers from the TIG corpus. Papers in this folder are referee-ready (per `J_series/README.md` §4 criteria).

---

## §1 — Currently landed

| J# | Title | Target venue | Status | Landed |
|---|---|---|---|---|
| **[J35](J35/)** | *Joint Closure, a Universal Attractor, and an Algebraic Mixing Point for a Pair of Binary Operations on $\mathbb{Z}/10\mathbb{Z}$* | *Journal of Algebra* | SUBMISSION-READY (6/6 PASS at machine precision; referee-grade pass complete 2026-05-12) | 2026-05-12 |
| **[J15](J15/)** | *Galois $D_4$ over LMFDB 4.2.10224.1: Number-Field Identification of the Four-Core Attractor* | *Communications in Algebra* | SUBMISSION-READY (6/6 PASS at machine precision; referee-grade pass complete 2026-05-12) | 2026-05-12 |
| **[J31](J31/)** | *Wedderburn $D_4$-Isotypic Decomposition of the Lens-Pair Commutator $[\mathrm{TSML}, \mathrm{BHML}]$ on $\mathbb{Z}/10\mathbb{Z}$: $\mathfrak{su}(4) \oplus \mathfrak{u}(1)$ Subalgebra of $\mathfrak{so}(10)$ and a 9-Vector inside the $\mathbf{54}$ with $\|v\|^2 = 13/4$* | *Journal of Algebra* | SUBMISSION-READY (3/3 PASS at machine precision; exact-rational Wedderburn cross-check $3075027/2 + 9/2 + 288164 + 0 + 19608 = 1{,}845{,}290$; structural zero at $\mathrm{sign}_3$ verified exact) | 2026-05-12 |

J35 is the corpus centerpiece: six independent structural facts (8-shell joint-closure chain on $\mathbb{Z}/10\mathbb{Z}$ with sizes $\{2,3\}$ forbidden; three-substrate strengthening to $T+B+S$; 4-core $\{0,7,8,9\}$ closure; normalizer identity $Z_T=Z_B=(v+h+br+r)^2$; closed-form attractor $p_7/p_8 = 1+\sqrt{3}$ with Galois $D_4$ over LMFDB 4.2.10224.1; universal attractor on chain shells; partial $\alpha=1/2$ uniqueness) converging on $\mathcal{C}=\{0,7,8,9\}$ as the algebraic center.

J15 is the standalone, referee-portable Galois-theoretic deep cut on the runtime quartic $f(x) = x^4 + 4x^3 - x^2 + 2x - 2$ that the four-core attractor identifies. It unfolds the full proof of J35's Theorem D: case-by-case integer-factorization irreducibility argument over $\mathbb{Q}$ (with mod-7 cross-check), explicit cubic resolvent $g(y) = (y+2)(y^2 - y + 18)$ with rational root $-2$ and quadratic-factor discriminant $-71$, $D_4$-vs-$C_4$ distinction via irreducibility of $f$ over $\mathbb{Q}(\sqrt{-71})$ (Cohen 1993 §6.3.2), explicit $\mathbb{Q}(\sqrt{3})$-factorization with conjugate quadratic discriminants $11 \pm 8\sqrt{3}$ (norm $-71$), and Tschirnhaus reduction $x \mapsto -x - 1$ to LMFDB's canonical defining polynomial $x^4 - 7x^2 - 12x - 8$ of $4.2.10224.1$. J15 differentiates from J35 by depth-on-the-Galois-question vs J35's six-fact fusion-closure spread.

J31 is the focused Wedderburn-decomposition companion to J35: the lens-pair commutator $[T, B] = TB - BT \in M_{10}(\mathbb{Z})$, of Frobenius norm-squared $1{,}845{,}290$, decomposes orthogonally under conjugation by $D_4 = \langle P_{56}, \sigma^3 \rangle$ into five $D_4$-irrep isotypic shares with exact-rational norm-squareds $(3{,}075{,}027/2,\, 9/2,\, 288{,}164,\, 0,\, 19{,}608)$ for $(\mathrm{triv}, \mathrm{sign}_1, \mathrm{sign}_2, \mathrm{sign}_3, \mathrm{std})$, percentages $(83.32\%, 0.0002\%, 15.62\%, 0\%, 1.06\%)$. The trivial isotypic is the 16-dimensional doubly-invariant subalgebra $\mathfrak{g}_0 \cong \mathfrak{su}(4) \oplus \mathfrak{u}(1)$ (Killing spectrum $(-4)^{15} \oplus (0)^1$); the $\mathrm{sign}_2$ isotypic is a 9-vector inside the $\mathbf{54}$ of $\mathfrak{so}(10)$ with $\|v\|^2 = 13/4$ exact. The structural zero at $\mathrm{sign}_3$ is a *forbidden symmetry* of the commutator under $D_4$ (Proposition 5.1) — the load-bearing surprise of the paper.

---

## §2 — Expected papers when ready

| J# | Title | Target venue | Status |
|---|---|---|---|
| **J32** | Three-Substrate Architecture and D₄ Orbits | *J. Algebra* (lead) | math fix applied (orbit recount: 44, 7, 4, 10, 2 → 67 orbits / 126 elements) |
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
