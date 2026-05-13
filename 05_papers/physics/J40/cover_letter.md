# Cover letter — J40: Logarithmic Nonlinearity as a Forcing Principle: A Bialynicki-Birula Reading and Its Limits for Navier-Stokes

**To:** Editors, *Journal of Mathematical Physics*

**From:**
- B.R. Sanders (corresponding), 7Site LLC, Hot Springs, AR — brayden@7site.co
- M. Gish, Independent Researcher

**Date:** [DATE OF SUBMISSION]

**Manuscript title:** *Logarithmic Nonlinearity as a Forcing Principle: A Bialynicki-Birula Reading and Its Limits for Navier-Stokes*

**Status:** R1 (Revised after fresh-eyes referee report; revisions itemized in manuscript §7.)

---

## Summary

We exploit the Bialynicki-Birula--Mycielski uniqueness theorem (1976) — that logarithmic nonlinearity is the unique self-interaction preserving separability of composite quantum systems on the non-relativistic Schrödinger side — as a *forcing principle*: any continuum lift of a discrete composition algebra that respects partition independence is forced to take the logarithmic form on that side. We then study a specific scalar-field model $\Box \Xi = \kappa(1 + \log \Xi)$ whose potential $V(\Xi) = \kappa \Xi \log \Xi$ is BB-forced via the cosmological-quintessence side [J46], and prove a **conditional regularity theorem** (Theorem 4.1): assuming positivity preservation $\Xi(t, x) > 0$ and a uniform lower bound $\inf_x \Xi(t, x) \ge \delta > 0$ on $[0, T]$, the Brezis-Gallouet log-Sobolev embedding plus a Bihari-type Grönwall inequality yields a single-exponential-in-$t$ Sobolev bound at fixed initial data. The positivity preservation hypothesis is itself elevated to **Open Problem 0**; in its absence, we cannot upgrade Theorem 4.1 to unconditional regularity. We then compare to Navier-Stokes, define a separability defect $\sigma(u; \mathcal P)$ over a tractable polyhedral-divergence-free partition class $\mathcal P_K$, state the Separability Regularity Criterion as a precise conjecture, and identify three further open problems. **The paper claims a new framework, not a proof of NS regularity, and not unconditional regularity of $\Xi$.**

## R1 revisions

This is a revised submission addressing fresh-eyes referee comments [J40_JMP_FreshEyes, 2026-05-07]. The substantive revision is **Theorem 4.1 has been recast as a conditional regularity theorem with explicit hypotheses (H1) positivity preservation and (H2) uniform lower bound, with a complete proof from Brezis-Gallouet log-Sobolev + Bihari-type Grönwall**. The earlier draft's invocation of Cazenave-Haraux 1980 was incorrect (their result is for $u \log |u|^k$, vanishing at $u = 0$; our nonlinearity $1 + \log \Xi$ is genuinely singular at $\Xi = 0$); we replace it with the appropriate log-Sobolev tool. The previously implicit "BB theorem extended to wave equations" claim is removed; we state explicitly (§2.3) that we work with a specific scalar-field model whose potential is BB-forced via the Schrödinger / cosmological side, not a wave-equation extension of BB. Definition 5.1 of the separability defect is rewritten over an explicit class $\mathcal P_K$ of polyhedral divergence-free partitions, making Conjecture 5.2 a precise mathematical statement (in contrast to R0's underspecified version). §5.4's "logarithmic gap" comparison is downgraded to interpretive heuristic. The full itemized list is in manuscript §7 (13 items).

## Why JMP

- The paper sits at the intersection of nonlinear PDE, constructive QFT, and discrete-to-continuum transport — the natural JMP audience.
- The BB-forced log nonlinearity reading is, to our knowledge, novel: previous work has used BB as a constraint on admissible nonlinear QM, not as a forcing principle for continuum lifts.
- Theorem 4.1 (R1, conditional version) is fully proved by elementary log-Sobolev + Bihari machinery; the BB result it relies on is the classical 1976 paper; only the Open Problems 0–3 are conjectural, and that conjectural status is stated explicitly. The paper is intellectually honest about its scope.
- The Open Problems are **precisely formulated** with explicit functional spaces and partition classes; they are concrete attack surfaces, not slogans.

## PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** Theorem 2.1 (BB uniqueness, 1976; cited, not re-proved). Theorem 4.1 (conditional regularity of $\Xi$ under H1+H2). NS quadratic nonlinearity breaks separability (immediate from Definition 5.1).
- **COMPUTED.** Companion script `proof_separability_bridge.py` verifies elementary numerical claims on the potential's algebra: vacuum at $\Xi_0 = e^{-1}$, fluctuation curvature $V''(\Xi_0) = \kappa e$, asymptotic $\log \rho \ll \rho^\alpha$ at large $\rho$. Sanity check on the potential, not on the load-bearing PDE results.
- **STRUCTURAL RHYME.** §5.4's "logarithmic gap" comparison between BB log and Kozono-Taniuchi BMO log improvements: these are different functional senses of "log" that we do not unify rigorously; framing is interpretive heuristic, not derivational.
- **OPEN.** Open Problem 0 (positivity preservation of $\Xi$ — the hypothesis of Theorem 4.1). Open Problem 1 ($\Phi_N$ continuum lift). Open Problem 2 ($\delta^*$ nonlinearity gap). Open Problem 3 (separability bound on NS).

## Companion submissions

The TIG/CK research program is shipping a coordinated J-series. The papers most relevant as already-submitted companions:

- [J01] Sanders, B.R., Gish, M. (2026). "Non-Associativity Decay in Binary Composition Tables over $\mathbb{Z}/N\mathbb{Z}$." Submitted to *JCT-A*. (Provides the discrete-side $\sigma(N) \to 0$ rate, motivational for §3 only — not load-bearing.)
- [J46] Sanders, B.R., Gish, M. (2026). "Logarithmic Quintessence." Submitted to *JCAP*. (Cosmological realization of the same $V(\Xi) = \Lambda^4 \Xi \log \Xi$.)
- [J05] Sanders, B.R., Mayes, B. (2026). "Crossing Lemma." Submitted. (Discrete partition-independence reading of information generation.)
- [J41] Sanders, B.R., Gish, M. (2026). "The Yang-Mills Mass Gap Bridge." Companion JMP submission.

## Reproducibility

`proof_separability_bridge.py` (43/43 PASS; rebranded in R1 as elementary numerical sanity check, **not** verification of Theorem 4.1, Definition 5.1, or Conjecture 5.2 — those are not directly testable by the script). Runs in `python` with `math` only on a standard laptop in seconds. DOI: 10.5281/zenodo.18852047.

## Suggested reviewers

- T. Tao (UCLA) — NS regularity, log-improvements.
- C. Fefferman (Princeton) — Clay NS problem.
- I. Bialynicki-Birula (Polish Academy of Sciences) — original 1976 author, if available.
- J. Maas (IST Austria) — discrete-to-continuum transport, log-Sobolev.
- N. Gigli (SISSA) — Maas / JKO framework.
- K.G. Zloshchastiev — logarithmic Schrödinger applications.

## Conflict of interest

The authors declare no competing interests. No funding was received for this work.

## Tier and scope

Central claim is **Tier 4** (framework paper, structural). The BB theorem (Schrödinger, 1976) and Theorem 4.1 (conditional regularity under H1+H2) are proved; the bridge premise relies on a discrete-to-continuum lift $\Phi_N$ whose explicit construction is left open (Open Problem 1); positivity preservation is itself open (Open Problem 0); NS regularity is *not* claimed proved. The Status Table in §6 of the manuscript makes this explicit.

## Per-venue cap note

This is the **first** JMP submission in the J-series; the second (J41, YM bridge) follows as the companion. Both papers cite each other; the 2/quarter cap is approached, not exceeded.

---

Sincerely,
B.R. Sanders
