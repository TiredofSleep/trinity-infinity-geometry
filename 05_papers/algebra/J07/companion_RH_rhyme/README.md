# J07-companion — Structural Rhyme between σ-Character Spectrum on Z/10Z and Riemann Zeros

**Status:** DRAFT (2026-05-27 — split off from J07 §7 per Wave 4 audit).

**Tier:** 2 (expository note; targets *Math. Intelligencer*).

**Target venue:** *Mathematical Intelligencer* (primary). Fallbacks: *Notices of the AMS* ("What Is..." or expository note), *American Mathematical Monthly* (expository).

## What this note does

A short (3000-4000 word) expository note describing a **structural rhyme** — in the Connes–Berry–Keating sense — between three features of the σ-character spectrum on $\mathbb{Z}/10\mathbb{Z}$ (developed in the companion paper [J07]) and three features RH demands of $\zeta(s)$.

The three rungs of the rhyme:

| RH-side feature | Substrate-side rhyme |
|---|---|
| Zeros on the critical line | $G(s) = 0$ at the four σ-anchors $\{0,3,8,9\}$ |
| Spectral concentration (zeros not in the strip) | $G(s)$ takes only three values, no intermediate spectrum |
| Multiplicative–additive interplay (Euler product) | σ-iteration (additive) × χ-sign valuation (multiplicative-like) |

## What this is NOT

The note is explicit on four scoping promises:

- **NOT a proof of RH.** No analytic continuation, no Weil–Deligne mechanism, no Hilbert–Pólya operator.
- **NOT a Weil–Deligne analogue.** $\mathbb{Z}/10\mathbb{Z}$ is too small for cohomological purity.
- **NOT an analytic continuation.** The substrate is finite-dimensional; $\zeta$ is infinite-dimensional.
- **NOT a new proof technique.** Even Z.5 (the load-bearing open conjecture) would only lift the rhyme to a derivation — not a proof of RH itself.

## The load-bearing open problem: Conjecture Z.5

The structural rhyme would lift to a derivation if a specific conjecture (Z.5) about the deployment map $\lambda = 2|s - 1/2|$ holds — namely, that this deployment preserves both the substrate's algebraic 3-grading and its metric 6-corridor structure uniformly as $|\mathrm{Im}(s)| \to \infty$.

- **Proved**: at $t = 0$ (the real axis); in a small neighborhood $|s - 1/2| < \epsilon$.
- **Open**: uniformity in $t$.

## Relationship to the companion paper [J07]

The companion paper [J07] (target: *European J. Combinatorics*) develops the finite-side mathematics — five theorems on the σ-character spectral architecture on $\mathbb{Z}/10\mathbb{Z}$, with full proofs and reproducible verification.

The present note presupposes [J07] and concentrates on the rhyme. The split was recommended by the Wave 4 ship-readiness audit (`_staging/referee_reports/23_wave4_audit_J05_J07_J17_J22_J27.md`, §J07): an RH-bridge section was tonally wrong for the strict-combinatorics venue (EJC), but stood as a clean expository note on its own.

## File layout

```
companion_RH_rhyme/
├── README.md                    this file
└── manuscript_RH_rhyme.md       the 3000-4000 word note for Math. Intelligencer
```

## Authors

B.R. Sanders (7Site LLC, Hot Springs, AR) and M. Gish (Independent Researcher).

## To do before submission

- [ ] LaTeX conversion (currently Markdown).
- [ ] Cover letter for *Math. Intelligencer* draft.
- [ ] Confirm [J07] arXiv preprint number available before submission so this can cite it concretely.
