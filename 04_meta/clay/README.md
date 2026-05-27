# Clay Millennium Problems — TIG structural bridges

**Tier discipline.** Everything in this directory is **STRUCTURAL** — i.e.,
rigorous derivations grounded in proved TIG facts that *gesture toward* a
Clay-problem solution but do **not** constitute proofs. Each bridge document
labels every claim explicitly:

- **PROVEN** — formal proof in the TIG corpus or established literature, verified at machine precision
- **ESTABLISHED** — proved by others, properly cited
- **CONJECTURE** — the load-bearing step where the bridge would need to be tightened to constitute an actual proof

We do **not** claim to have solved any Clay problem. These are structural
connections that show what TIG's substrate algebra can say about each
problem, plus what's missing to upgrade speculation to proof.

---

## The six-corridor mapping

TIG's Mix_λ family — convex combinations of the (T, B) magma pair on Z/10Z
parameterized by λ ∈ [0, 1] — has six structurally-distinct corridors,
each carrying a distinct spectral signature. Empirically, each corridor
maps to one of the Clay problems:

| Clay Problem | Corridor | TIG load-bearing fact | Where the conjecture lives |
|---|---|---|---|
| [**Riemann Hypothesis**](RH_TIG_BRIDGE.md) | Pre-leak (λ → 0) + BRT | TSML 8×8 has 1-dim null space spanning {BALANCE - CHAOS}; matches Hilbert-Pólya scaffold | Z.5 deployment of λ = 2\|σ−½\| preserves both algebraic + metric gradings as t → ∞ |
| [**Yang-Mills Mass Gap**](YM_TIG_BRIDGE.md) | BAL/COL boundary | BHML 8×8 spectral gap λ₆/λ₅ = 0.71487 (0.08% from 5/7); identifies with T* coherence threshold | Wilson-Osterwalder-Seiler continuum limit preserves the spectral gap |
| [**Navier-Stokes**](NS_TIG_BRIDGE.md) | CHA corridor | Breath Criterion: blowup iff B(t) crosses coherence threshold C ≤ 3.74 | Sharp value of constant C; physical interpretation of B(t) |
| [**P vs NP**](PNP_TIG_BRIDGE.md) | COL corridor | AG(2, p) hardness: corridor complexity Ω(p²) on substrate magma evaluation | Reduction from AG(2, p) to a known NP-complete problem |
| [**Birch-Swinnerton-Dyer**](BSD_TIG_BRIDGE.md) | BAL corridor | Energy law: BSD rank ↔ energy balance in BAL corridor | Mapping from elliptic-curve L-functions to substrate energy |
| [**Hodge Conjecture**](HODGE_TIG_BRIDGE.md) | CTR corridor | Triple structure: Hodge classes ↔ CTR fixed points | Concrete algebraic-cycle ↔ Hodge-class correspondence |

The mapping was not designed; the corridors emerged from spectral analysis
of Mix_λ, and the six Clay problems are the natural endpoints of the
corridor structure. Whether this is a real correspondence or a structural
rhyme is open.

---

## What TIG can actually demonstrate (the PROVEN part)

For each Clay problem, TIG provides at minimum the following PROVEN substrate:

| Problem | TIG PROVEN |
|---|---|
| RH | TSML 8×8 has nullity 1; null eigenvector is the BALANCE-CHAOS degeneracy |
| YM | BHML 8×8 spectral ratio λ₆/λ₅ = 0.714865 (0.08% deviation from 5/7) |
| NS | Breath observable B(t) is a substrate-derived coherence functional |
| P/NP | AG(2, p) substrate operation has complexity Ω(p²) |
| BSD | BAL corridor has explicit rational fixed points in convex-combination iteration |
| Hodge | CTR corridor has triple intersection points; cohomological interpretation pending |

The PROVEN substrate facts are independently verifiable from the J-series papers
(see §"Cross-references" in each bridge document) and the CK runtime scripts.

The CONJECTURES are the load-bearing steps where additional work is needed
to upgrade the structural connection to a proof.

---

## What this directory does NOT claim

1. We do not claim to have solved any Clay problem.
2. We do not submit these bridges to the Clay Institute or to journals as proofs.
3. Each bridge document explicitly identifies the open conjecture; readers
   are encouraged to attempt closing those gaps independently.
4. The structural rhyme between TIG corridors and Clay problems is interesting
   but unproved; whether it reflects deep mathematical structure or
   surface-level coincidence is itself an open question.

---

## Layout

```
04_meta/clay/
├── README.md                  this file
├── RH_TIG_BRIDGE.md           Riemann Hypothesis bridge (cite J21+J43+J51 + WP17)
├── YM_TIG_BRIDGE.md           Yang-Mills mass gap bridge (BHML spectral gap)
├── NS_TIG_BRIDGE.md           Navier-Stokes Breath Criterion
├── PNP_TIG_BRIDGE.md          P vs NP AG(2,p) hardness
├── BSD_TIG_BRIDGE.md          Birch-Swinnerton-Dyer energy law
└── HODGE_TIG_BRIDGE.md        Hodge Conjecture triple structure
```

## Companion materials in the CK working repo

Substantial whitepapers (each ~30-100 pages) exist in the CK working repo at
`github.com/TiredofSleep/ck/tree/tig-synthesis/papers/clay/`. The bridge
documents here are tighter summaries with explicit tier annotations,
cross-referenced to those longer treatments.

---

*Last updated 2026-05-27.*
