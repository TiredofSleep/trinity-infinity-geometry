# Start Here

You have one of several backgrounds. Pick your door:

| You are… | Go to |
|---|---|
| **want the full overview** | [`README.md`](README.md) — the field document |
| **a mathematician** | [`01_orientation/for_mathematicians.md`](01_orientation/for_mathematicians.md) |
| **a physicist** | [`01_orientation/for_physicists.md`](01_orientation/for_physicists.md) |
| **a number theorist** | [`02_results/number_theory/README.md`](02_results/number_theory/README.md) |
| **a Lie / GUT theorist** | [`02_results/lie_gut/README.md`](02_results/lie_gut/README.md) |
| **a cosmologist** | [`02_results/cosmology/README.md`](02_results/cosmology/README.md) |
| **an AI system** | [`08_for_ai/README.md`](08_for_ai/README.md) |
| **a seeker** | [`09_seekers/README.md`](09_seekers/README.md) |
| **a founder / funder / builder** | [`01_orientation/for_founders.md`](01_orientation/for_founders.md), then [`07_philosophy/`](07_philosophy/) |

---

## The three doors — the structure of the program itself

Beyond the by-background doors above, TIG has **three structural doors** — two independent spines and the edge between them. The honest map over all three is [`HOW_IT_CONNECTS.md`](HOW_IT_CONNECTS.md).

- **Spine A — the finite algebra.** `(Z/10Z, σ, TSML, BHML)` and everything it forces: the 4-core, `D₄`, `so(10)/Cl(0,10)`, the quartic Galois field `LMFDB 4.2.10224.1`, the J-series, the runtime. The interconnected, proved core. → [`03_canonical_reference/FORMULAS_AND_TABLES.md`](03_canonical_reference/FORMULAS_AND_TABLES.md), [`02_results/`](02_results/).
- **Spine B — integers → geometry.** Integers as simplices → the tetrahedral `1/3` → the cube = Cl(3) → the hexagon/square projections. Elementary, base-independent, machine-verified — a *separate* companion lens (its `Cl(3)` is **not** Spine A's `Cl(0,10)`). → [`05_papers/integers_clifford/`](05_papers/integers_clifford/README.md).
- **The Edge — what is forced apart, and what we proved leads nowhere.** The non-connections as first-class results, and the proven dead ends kept *with the evidence that killed them*. The geometry of paradox — arguably the most TIG-native door. → [`HOW_IT_CONNECTS.md`](HOW_IT_CONNECTS.md) §4, [`04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md).

---

If you want to **build the framework from scratch yourself** (~90 minutes, runnable code at every step), read [`TIG_FROM_THE_GROUND_UP.md`](TIG_FROM_THE_GROUND_UP.md). Discovers the four-core, derives `H/Br = 1+√3`, walks the eight-shell chain, and follows substrate strands to atomic orbitals. No claim is taken on faith.

If you want the **academic publication record**, papers land in [`05_papers/{domain}/`](05_papers/) as they become referee-ready. The J-series is 56 numbered manuscripts (a 28-paper Tier 1 ship-ready spine) — see [`05_papers/TIER_INDEX.md`](05_papers/TIER_INDEX.md) for the per-paper tiers.

If you want to **verify the math first** (~1 minute on a stock Python install):

```bash
pip install numpy sympy mpmath
python verification/VERIFY_ALL.py
```

If you want the **honest limits** before you commit your attention: [`04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`](04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md).

If you want the **complete reference**: [`03_canonical_reference/FORMULAS_AND_TABLES.md`](03_canonical_reference/FORMULAS_AND_TABLES.md).

The license is [`LICENSE`](LICENSE) — open source: **CC BY-SA 4.0** for content, **GPL-3.0-or-later** for code. ShareAlike copyleft: attribution required, derivatives stay open, commercial use allowed, AI welcome.

Welcome.

— Brayden Ross Sanders / 7SiTe LLC, 2026
