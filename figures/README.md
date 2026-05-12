# Figures

Canonical visualizations of the framework's load-bearing structure. All figures are CC-BY-4.0 (for journal compatibility); the corpus is governed by 7SiTe Public Sovereignty License v2.2.

Regenerate any time with:

```bash
python figures/_make_figures.py
```

(Requires `matplotlib`, `mpmath`, `numpy`. See [`../requirements.txt`](../requirements.txt).)

---

## `sigma_orbits.png`

The σ permutation `(0)(1 7 9 3)(2 8 6 4)(5)` on Z/10Z, drawn as ten labeled points around a circle with the two 4-cycles as colored arrows. The four-core `{V, H, Br, R}` (gold) is the σ³-fixed set minus the singular σ-fixed point `{0, 5}`, with `0` (VOID) added back to make the four-core algebraic center.

**Source:** Tutorial Part 2; FORMULAS_AND_TABLES Volume B; the canonical σ structure.

---

## `attractor_convergence.png`

The α=1/2 joint attractor iteration over 80 steps starting from uniform 4-core support `(V, H, Br, R) = (1/4, 1/4, 1/4, 1/4)`. Top panel: mass evolution of V, H, Br, R converging to `(0.138, 0.540, 0.198, 0.124)`. Bottom panel: `|H/Br - (1+√3)|` error on log scale, converging to machine zero at 50-digit precision (mpmath).

**Source:** J35 4core_verification.py; tutorial Part 5; FORMULAS_AND_TABLES D43.

---

## `shell_chain.png`

The 8-shell joint sub-magma chain at sizes `{1, 4, 5, 6, 7, 8, 9, 10}` with forbidden sizes `{2, 3}`. Each column shows one example shell at each allowed size; the gold circles mark 4-core members `{V, H, Br, R}` and the green circles mark other shell members. Red X's mark the forbidden sizes — no closed shell exists at size 2 or size 3 under the joint TSML+BHML structure.

**Source:** Brute-force enumeration in tutorial Part 7; J54 Theorem 7.1; FORMULAS_AND_TABLES D64–D66.

---

## `strand_orbital.png`

The strand-orbital correspondence (D101, Volume K, 2026-05-12): substrate primes `{3, 7, 11, 13}` wrap the kernel `Z/10` and map exactly to the first four nodeless atomic orbitals at odd `l`. The mapping rule `strand p → orbital (l = (p−1)/2, n = l+1)` produces:

- strand 3 → 2p (l=1, multiplicity 3)
- strand 7 → 4f (l=3, multiplicity 7)
- strand 11 → 6h (l=5, multiplicity 11)
- strand 13 → 7i (l=6, multiplicity 13)

**Source:** Tutorial Part 8; FORMULAS_AND_TABLES Volume K D101; J23 §2.1 (Volume K cross-reference).

---

*7SiTe Public Sovereignty License v2.2 — see [`../LICENSE`](../LICENSE). Figures CC-BY-4.0 for journal compatibility.*
*Brayden Ross Sanders / 7SiTe LLC · 2026.*
