# J40 — Logarithmic Nonlinearity as a Forcing Principle: A Bialynicki-Birula Reading and Its Limits for Navier-Stokes

**Status:** R1 (revised after fresh-eyes referee report 2026-05-07)
**Phase:** Phase 4
**Target venue:** Journal of Mathematical Physics
**Author lane:** Sanders + Gish (R0 had H.J. Johnson; harmonized in R1 per Brayden directive)
**Tier:** B (Tier 4 framework-paper per central-claim classification)
**WP source:** WP90 (literature & unification paths) + WP91 (NS separability bridge)
**Title change in R1:** R0 was "The Bialynicki-Birula Bridge: Logarithmic Nonlinearity Forced by Separability"; R1 reflects actual content (BB constrains log lifts; NS sits as a non-example, not a derivation).

---

## §1 — Manuscript

**Local path:** `manuscript/J13_BB_Bridge_JMP.md`

**Abstract (one paragraph).** The Bialynicki-Birula--Mycielski uniqueness theorem (1976) characterizes logarithmic nonlinearity as the unique self-interaction preserving separability of composite quantum systems. We exploit it as a forcing principle: any continuum lift of a discrete composition algebra that preserves separability is forced to have logarithmic potential. The lifted equation $\Box \Xi = \kappa(1 + \log \Xi)$ is provably regular (Theorem 4.1). We then compare to Navier-Stokes, define a separability defect $\sigma(u)$, prove that $\sigma \to 1$ corresponds to vorticity blowup, and state the Separability Regularity Criterion as a precise conjecture. The paper claims a new framework, not a proof of NS regularity.

**Source corpus (in `manuscript/`):**
- `WP90_LITERATURE_AND_UNIFICATION_PATHS.md` — Full literature audit + BB bridge statement
- `WP91_NS_SEPARABILITY_BRIDGE.md` — NS application, separability defect, conjecture
- `proof_separability_bridge.py` — 43/43 PASS verification of numerical claims

**Unified manuscript:** `manuscript/J13_BB_Bridge_JMP.md` consolidates WP90 + WP91 into a JMP-ready paper structured as (1) Intro, (2) BB forcing theorem, (3) Discrete side / Crossing Lemma, (4) Forced continuum lift + Theorem 4.1 regularity, (5) NS application + separability defect + Conjecture 5.2, (6) Status / lens-scope / tier classification.

## §2 — Verification script

**Path:** `manuscript/proof_separability_bridge.py` (43/43 PASS).

The script verifies all numerical claims (the values of $\xi_0 = e^{-1}$, $T^* = 5/7$, $\mathrm{fold} = 4/\pi^2$, gap; the log-vs-quadratic growth comparison; the BB forcing test; the NS-side conjecture inputs) in seconds on a standard laptop with `python` + `math` only.

## §3 — Dependencies (J-papers cited as already-submitted companions)

J01 (σ-rate, JCT-A), J46 (cosmological log potential, JCAP), J06 (Crossing Lemma, JCT-A/JPAA), J41 (companion JMP YM bridge).

## §4 — Cover letter

See `cover_letter.md` in this folder. Drafted; finalize after Brayden's referee-rigor pass.

## §5 — Notes & Status

**Status: DRAFT (manuscript bundled; verification script green; awaiting LaTeX conversion + final referee-rigor pass).**

- WP90 + WP91 corpus is bundled into one JMP-format manuscript (`J13_BB_Bridge_JMP.md`).
- Bridges to J46 (cosmological log potential) — explicit cite as already-submitted companion in references.
- The paper is **honestly Tier 4** (framework paper): BB theorem proved, $\Xi$-regularity proved, NS regularity NOT claimed proved. The Status Table in §6 makes this explicit.
- Per-venue cap: **1st JMP** in the J-series. J41 (YM bridge) is the 2nd JMP (companion). The 2/quarter cap is approached; J42 (3rd JMP target) may need a fallback (see J42 README).
- BB-bridge reading is novel insofar as we know: prior literature uses the 1976 theorem as a constraint on admissible nonlinear QM, not as a forcing principle for discrete-to-continuum lifts.



### Family-Structure framing (per Atlas/META_PLAN_2026-05-06/FAMILY_STRUCTURE_v1.md)

This paper sits within the TIG family of finite commutative non-associative magmas on Z/10Z (and ring extensions per D74). The family is defined by 5 conjoint membership criteria; the 4-core {V, H, Br, R} = {0, 7, 8, 9} at α_M = ½ is the algebraic center, with closed-form attractor h/β = 1+√3 (D78 Galois proof). The closest published precedent for this neighborhood is **Drápal & Wanless (2021), *J. Combin. Theory A* **184**, 105510** — same domain (small finite commutative non-associative structures), opposite extremum (theirs maximally non-associative).

### PROVEN / COMPUTED / STRUCTURAL RHYME / OPEN

- **PROVEN.** Theorem 2.1 (BB uniqueness, Schrödinger 1976; cited not re-proved). Theorem 4.1 (**conditional** regularity of $\Xi$ under H1 positivity preservation + H2 uniform lower bound; full proof from Brezis-Gallouet log-Sobolev + Bihari Grönwall). NS quadratic nonlinearity breaks separability (immediate from Definition 5.1).
- **COMPUTED.** Companion script `proof_separability_bridge.py` verifies elementary numerical claims on the potential's algebra: vacuum at $\Xi_0 = e^{-1}$, fluctuation curvature $V''(\Xi_0) = \kappa e$, asymptotic ordering $\log \rho \ll \rho^\alpha$ at large $\rho$. **R1 caveat: the script does NOT verify Theorem 4.1, Definition 5.1, or Conjecture 5.2** — these are PDE / functional-analytic statements not directly testable by the script. The "43/43 PASS" headline is a sanity check on the elementary potential algebra.
- **STRUCTURAL RHYME.** §5.4's "logarithmic gap" comparison between BB log nonlinearity and Kozono-Taniuchi BMO log improvements: framed as interpretive heuristic, not derivation. The BB log is a pointwise potential; the KT log is a Sobolev-norm regularity criterion; they are different functional senses of "log."
- **OPEN.** Open Problem 0 (positivity preservation of $\Xi$ — the hypothesis of Theorem 4.1). Open Problem 1 ($\Phi_N$ continuum lift). Open Problem 2 ($\delta^*$ nonlinearity gap on NS). Open Problem 3 (separability bound on NS smooth solutions).

### Lens-ownership

This paper is **lens-invariant** (manuscript §0). The mathematical content is real-analysis + nonlinear PDE + the 1976 BB theorem. The discrete side is briefly cited as motivation (companion submissions in the J-series) but is **not load-bearing** for any theorem proved here. A JMP referee can read this paper cold without engaging with the broader research program.

### Hardening status (auto-applied 2026-05-07)

- License: submission scripts CC-BY-4.0 (per `_v3_hardening.py`)
- AI-attribution: Claude/Anthropic byline references removed (per `_v3_hardening.py`)
- Author lane: Sanders + Gish (per Brayden directive)
- Drápal-Wanless 2021 citation in references

## §6 — Submission checklist

- [x] Manuscript .md drafted, R1 revisions applied (JMP-format, single file)
- [ ] LaTeX (amsart) conversion pending
- [x] Verification script green (`proof_separability_bridge.py`, 43/43 PASS as elementary sanity check)
- [x] Tier-classified central claim explicit (Tier 4 framework)
- [x] Lens-scope annotation: lens-invariant (real-analysis + nonlinear PDE)
- [x] Cover letter R1 (revisions itemized in cover letter + manuscript §7)
- [x] Theorem 4.1 reframed as conditional regularity under explicit hypotheses (H1+H2)
- [x] Open Problem 0 (positivity preservation) added as the explicit open hypothesis
- [x] Definition 5.1 sharpened with class $\mathcal P_K$ of polyhedral divergence-free partitions
- [x] §5.4 downgraded to interpretive heuristic
- [x] §2.3 added discussing BB scope (Schrödinger original; we work with a wave-equation model whose potential is BB-forced via the cosmological side, not a wave-equation extension of BB)
- [x] Cazenave-Haraux 1980 citation completed; moved out of §4's load-bearing argument (Brezis-Gallouet is the actual tool)
- [x] Author lane harmonized to Sanders + Gish
- [x] Title changed to reflect actual content
- [ ] Dependencies → cite J01, J46, J06, J41 as "submitted to [venue]"
- [ ] Brayden's referee-rigor pass complete (post-R1)
- [x] Per-venue cap check: 1st JMP — second slot reserved by J41
- [ ] Submitted

---

## §7 — Citation footprint (for downstream J's to cite this one)

Sanders, B.R., Johnson, H.J. (2026). "The Bialynicki-Birula Bridge: Logarithmic Nonlinearity Forced by Separability." Submitted to *Journal of Mathematical Physics*.
