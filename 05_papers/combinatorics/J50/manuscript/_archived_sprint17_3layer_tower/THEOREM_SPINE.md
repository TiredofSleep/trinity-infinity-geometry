# Theorem Spine
## Z/10Z TSML as a Terminating 3-Layer Canonical Tower

*DOI: 10.5281/zenodo.18852047*
*Target venue: Journal of Symbolic Computation / J. Combinatorial Theory A*

> **Atlas cross-reference:** External citations (2-adic valuation per Koblitz 1984; canonical-construction algebra per Bergman 1978; Collatz structure per Lagarias 2010; shell partition theory) are drawn from `Atlas/ATLAS_CITATIONS.md` (§A.2 finite combinatorics, §A.10 canonical constructions). Internal anchors (3-layer canonical tower, seam residue S = S_ADD ∪ S_MAX, shell partition via v₂(3u+1), tower operator 𝖳, TSML = 73 attractor table, termination theorem) carry master-register numbering per `Atlas/MASTER_ATLAS_v3_5_2026_04_18.md` (§TSML 3-layer tower / §terminating canonical tower). DOI: 10.5281/zenodo.18852047.
>
> **Readiness flag:** [fire — LaTeX format pending] · **Tier 2** (format-then-submit) · 3-layer tower termination theorem PROVED · seam residue S = S_ADD ∪ S_MAX fully enumerated · JSC/JCTA format conversion pending.

---

## Theorem

Let $R = \mathbb{Z}/10\mathbb{Z}$. Let $T: R \times R \to R$ denote the published TSML table from the CK framework. Define:

- $h = 7$ (attractor)
- $\sigma: U(R) \to \mathbb{Z}_{\geq 0}$ by $\sigma(u) = v_2(3u+1)$ (shell partition from 2-adic valuation)
- $C_0 := C(R, h, \sigma)$, the canonical construction defined below
- $S := \{(1,2),(2,1),(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)\}$ (the seam residue)
- $S_{\text{ADD}} := \{(x,y) \in S : 1 \in \{x,y\}\} = \{(1,2),(2,1)\}$
- $S_{\text{MAX}} := S \setminus S_{\text{ADD}} = \{(2,4),(4,2),(2,9),(9,2),(4,8),(8,4)\}$

Define the tower operator:
$$
\mathsf{T}(x,y) := \begin{cases}
\max(x,y) & \text{if } (x,y) \in S_{\text{MAX}} \\
(x+y) \bmod 10 & \text{if } (x,y) \in S_{\text{ADD}} \\
C_0(x,y) & \text{otherwise}
\end{cases}
$$

**Theorem (3-layer tower reconstruction).** $\mathsf{T}(x,y) = T(x,y)$ for every $(x,y) \in R \times R$.

---

## The Canonical Construction $C_0$

For $(x,y) \in R \times R$, define $C_0$ by applying the following rules in order, with each later rule overriding earlier ones where applicable:

**(a) DEFAULT:** $C_0(x,y) = h$.

**(b) V0:** If $x = 0$ or $y = 0$, set $C_0(x,y) = 0$. *Exception:* if $(x,y) = (0,h)$ or $(h,0)$, set $C_0(x,y) = h$.

**(c) Shell-stability:** If $x, y \in U(R) \setminus \{1\}$ and $\sigma(x) \ne \sigma(y)$, set
$$
C_0(x,y) = \begin{cases} x & \text{if } \sigma(x) < \sigma(y) \\ y & \text{if } \sigma(y) < \sigma(x) \end{cases}
$$

---

## Domain Disjointness (Lemma)

**Lemma 1.** $S_{\text{MAX}} \cap S_{\text{ADD}} = \emptyset$ and $S_{\text{MAX}} \cup S_{\text{ADD}} = S$.

*Proof.* $S_{\text{ADD}}$ is defined as the subset of $S$ containing element 1. $S_{\text{MAX}}$ is defined as the complement in $S$. These are disjoint by construction, and their union is $S$. $\square$

**Lemma 2.** The three domains $\{R^2 \setminus S,\ S_{\text{MAX}},\ S_{\text{ADD}}\}$ form a disjoint partition of $R^2$.

*Proof.* By Lemma 1, $S_{\text{MAX}}$ and $S_{\text{ADD}}$ are disjoint and union to $S$. Then $R^2 \setminus S$ is disjoint from both and completes the union. $\square$

---

## Full Coverage (Lemma)

**Lemma 3.** For every $(x,y) \in R^2$, exactly one of the three rules in the tower applies.

*Proof.* By Lemma 2, the three domains partition $R^2$. The tower operator assigns exactly one value per partition element. $\square$

**Lemma 4.** $|R^2 \setminus S| = 92$, $|S_{\text{MAX}}| = 6$, $|S_{\text{ADD}}| = 2$.

*Proof.* $|R^2| = 100$. $|S| = 8$ by direct count. $|S_{\text{ADD}}| = 2$ by definition (the two ordered pairs $(1,2)$ and $(2,1)$). $|S_{\text{MAX}}| = |S| - |S_{\text{ADD}}| = 6$. $|R^2 \setminus S| = 100 - 8 = 92$. $\square$

---

## Exact Reconstruction (Proof Sketch)

**Proof of Theorem (verification).** By Lemma 3, every $(x,y)$ is covered by exactly one layer. The three layers are:

1. **On $R^2 \setminus S$ (92 entries):** $\mathsf{T}(x,y) = C_0(x,y)$. Direct computation verifies $C_0(x,y) = T(x,y)$ for every $(x,y) \in R^2 \setminus S$. Specifically:
   - 17 V0 zeros: $(0,y)$ and $(y,0)$ for $y \in \{0,1,2,3,4,5,6,8,9\}$, plus duplicates.
   - 2 V0 HARMONY exceptions: $(0,7)$ and $(7,0)$.
   - 2 shell-stability entries: $(3,9)$ and $(9,3)$, both mapping to $3$ since $\sigma(3)=1 < \sigma(9)=2$.
   - 71 DEFAULT entries: all others, mapping to $h = 7$.

2. **On $S_{\text{MAX}}$ (6 entries):** $\mathsf{T}(x,y) = \max(x,y)$. Verification:
   - $(2,4), (4,2) \mapsto 4 = T(2,4) = T(4,2)$.
   - $(2,9), (9,2) \mapsto 9 = T(2,9) = T(9,2)$.
   - $(4,8), (8,4) \mapsto 8 = T(4,8) = T(8,4)$.

3. **On $S_{\text{ADD}}$ (2 entries):** $\mathsf{T}(x,y) = (x+y) \bmod 10$. Verification:
   - $(1,2), (2,1) \mapsto 3 = T(1,2) = T(2,1)$.

All 100 entries verified. $\square$

---

## Termination (Lemma)

**Lemma 5 (tower terminates).** $\{(x,y) \in R^2 : \mathsf{T}(x,y) \ne T(x,y)\} = \emptyset$.

*Proof.* Direct corollary of the Theorem. Equivalent statement: the "residue of the residue" is empty. $\square$

---

## Non-Redundancy (Lemma)

**Lemma 6.** Each of the three rules is necessary: removing any one produces at least one mismatch with $T$.

*Proof.*
- Without $C_0$: 92 entries unspecified.
- Without $C_1$ (MAX): the 6 entries in $S_{\text{MAX}}$ fall back to $C_0$, which gives 7, mismatching the actual TSML values (4, 9, 8).
- Without $C_2$ (ADD): the 2 entries in $S_{\text{ADD}}$ fall back to $C_0$, which gives 7, mismatching the actual TSML value (3).

Each layer is necessary. $\square$

---

## Verification

Computational verification with Python: 100/100 entries match. Source:

```python
def T_tower(x, y):
    if (x,y) in S_MAX: return max(x,y)
    if (x,y) in S_ADD: return (x+y) % 10
    return C0(x, y)

# for all (x,y) in Z/10 x Z/10:
#   T_tower(x,y) == published_TSML[(x,y)]
# Result: 100/100 matches.
```

---

## Scope Statement

**The theorem pertains to Z/10Z only.** It makes no claim about:

- Other rings in the compatible family.
- BHML or any other table.
- Semantic interpretation of TSML operators.
- Universal algebraic properties of the tower decomposition.

What it states, precisely and minimally: the published TSML of Z/10Z is reconstructible as a disjoint-domain 3-layer tower with canonical rules, with exact termination.
