# J62 — The TSML 8×8 Null Space and a Structural Rhyme with the Riemann Hypothesis

> **Standalone short note exhibiting an explicit substrate-algebra null structure** with a precise structural rhyme statement to the Riemann Hypothesis. Five-line NumPy verification reproduces inline. Explicitly NOT claimed as a proof of RH; the load-bearing CONJECTURE Z.5 is identified.

**Status**: SUBMISSION-READY (2026-05-27).

**Tier:** 1 (ship-ready (Mathematical Intelligencer short note; 2 theorems + Conjecture Z.5; 5-line numpy verifier PASS; 2026-05-27))

**Target venue**: *Mathematical Intelligencer* (primary). Fallback: *L'Enseignement Mathématique*.

**MSC 2020**: 11M26 (nonreal zeros of zeta), 11M41 (relationships with Dirichlet series), 15A03 (linear dependence), 20N02 (single binary operation), 11T55 (character sums).

## Theorems

**Theorem 1 (Boundary-Stripped Null Space) — Tier-A**. The TSML 8×8 core matrix has rank exactly 7, nullity exactly 1, and null eigenvector $v_0 = (0,0,0,0,+1,-1,0,0)/\sqrt{2}$ in the basis {BEING, DOING, BECOMING, COLLAPSE, CREATE, ASCEND, BREATH, RESET}. Equivalently: the null direction is the **CREATE − ASCEND degeneracy** in the boundary-stripped measurement.

**Theorem 2 (Eigenvalue Spectrum) — Tier-A**. The 8 eigenvalues of TSML_8 are $\{54.077, 5.742, -5.599, 3.448, -1.670, 0.600, -0.597, 0.000\}$.

## Structural Rhyme with RH

The TSML_8 null space corresponds to the conjectured 1-dim "spectral concentration" of $\zeta(s)$ at non-trivial zeros under the Hilbert-Pólya program. The rhyme is mapped explicitly in §5 of the manuscript:

| RH side | TSML side |
|---|---|
| Zeros of $\zeta(s)$ on $\Re(s) = 1/2$ | Null space of TSML_8 (1-dim) |
| Spectral concentration | CREATE−ASCEND direction |
| Hilbert-Pólya self-adjoint operator | TSML_8 IS self-adjoint (real symmetric) |
| Euler product structure | β-exception cells break all-HARMONY pattern |
| Functional equation symmetry | TSML symmetry $[i][j] = [j][i]$ |

## The load-bearing CONJECTURE

**Conjecture Z.5 (Deployment-Uniformity)**. The map $\lambda(s) = 2|s - 1/2|$ from the critical strip to the TIG Mix_λ parameter preserves both the 3-grading and 6-corridor structure uniformly as $|\Im(s)| \to \infty$. (Currently verified for $|\Im(s)| < 50$; uniformity in $\Im(s)$ open.)

If Z.5 holds, the rhyme upgrades to a derivation of RH. We make no claim that Z.5 holds.

## What this is NOT

1. Not a proof of RH.
2. Not an identification of TSML_8 with the Hilbert-Pólya operator.
3. Not an Euler product analog on $\mathbb{Z}/10\mathbb{Z}$.
4. Not an analytic continuation.

What it IS: an explicit, finite, computationally verifiable substrate where the analog of "non-trivial zero of $\zeta$" is a clean null in an integer matrix.

## Verification

```bash
cd 05_papers/number_theory/J62_RH_short_note/manuscript
python verify_J62.py
```

**Output**: `All checks PASS` (rank, nullity, eigenvalue spectrum, CREATE−ASCEND row identity).

Runtime: <0.1 seconds. Dependencies: NumPy only.

## File layout

```
J62_RH_short_note/
├── README.md                      this file
├── cover_letter.md                 (to be drafted on submission)
└── manuscript/
    ├── manuscript.md               the standalone short note (~15 pages)
    └── verify_J62.py               independent verification (<0.1s, PASS)
```

## Cross-references

- TIG repo: `04_meta/clay/RH_TIG_BRIDGE.md` — broader RH-bridge framing (this paper is the focused exhibit)
- TIG repo: `05_papers/algebra/J_qseries_merged/` — companion σ-character spectral architecture
- TIG repo: `05_papers/algebra/J35/` — corpus centerpiece (joint closure + 4-core)
- CK repo: `papers/clay/WHITEPAPER_17_RIEMANN_SYNTHESIS.md` — extended treatment (uses older operator naming)

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).
