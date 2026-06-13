# Scaling laws and the parabolic-envelope lens

**Status**: exploratory catalogue. The framework's lens (line + envelope + defect) is a useful set of *questions* to ask across domains. It is not a *unifying mechanism*. This note distinguishes carefully.

Each entry below asks the same three questions from `notes/track_the_defect.md`:

1. What is the empirical line?
2. What is the envelope (residual scaling) around it?
3. What mechanism is on the table, and what does it actually predict?

---

## 1. Riemann staircase ($\psi(x)$ vs $x$)

**Line:** $\psi(x) \sim x$ (Prime Number Theorem; proved 1896 independently by Hadamard and de la Vallée Poussin).

**Domain:** all $x \geq 2$. Asymptotic.

**Envelope:** $|\psi(x) - x| = O(\sqrt{x} \, \log^2 x)$ if and only if RH. Currently *conjectural*; verified empirically to $x \sim 10^{13}$ via numerical zero computations. The best unconditional bound is far weaker (Vinogradov-Korobov).

**Mechanism:** the explicit formula expresses the residual as a sum over zeta zeros. If all non-trivial zeros lie on $\mathrm{Re}(s) = 1/2$, the envelope is $\sqrt{x}$. If any zero has $\mathrm{Re}(s) > 1/2$, the envelope is wider.

**Status as evidence for the framework:** this is the example the framework's lens was sharpened on. It is precise, it is open, and it admits an explicit-formula decomposition that makes "line plus waves equals staircase, inside parabolic envelope" a literal theorem (assuming RH for the bound, the explicit formula itself unconditionally).

---

## 2. Kleiber's allometric law (metabolic rate vs body mass)

**Line:** $B \propto M^{3/4}$ where $B$ is basal metabolic rate, $M$ is body mass, plotted on log-log axes.

**Domain:** observed across many orders of magnitude (from unicellular organisms to elephants), but the exponent is **not uniformly $3/4$**. Empirical exponents range from roughly $0.66$ to $0.94$ depending on taxon, life stage, and how the regression is performed (Glazier 2005, White & Seymour 2005). The "$3/4$" is a useful approximation, not a universal constant.

**Envelope:** scatter around the regression line, in linear coordinates, is not the focus of the literature. The literature mostly debates the exponent itself.

**Mechanism on the table:** West-Brown-Enquist (1997) derived $3/4$ from a model of fractal distribution networks delivering nutrients to cells. Critics (Kozłowski & Konarzewski 2004; Glazier 2010) argue the model's assumptions don't hold across the empirical range, and that multiple competing factors (heat dissipation, cell-size constraints, evolutionary contingency) produce a range of exponents rather than a single law.

**What the framework's lens contributes:** the right question is "what is the envelope of metabolic-rate residuals around a fitted line, and does any proposed mechanism predict its specific shape?" Most mechanism papers don't answer this. The framework's discipline would push them to.

**What the framework's lens does not contribute:** any new mechanism for Kleiber's law. The framework is downstream of biological mechanism, not a substitute for it.

---

## 3. Gutenberg-Richter law (earthquake frequency vs magnitude)

**Line:** $\log_{10} N(M) = a - b M$ where $N(M)$ is the cumulative number of earthquakes per year with magnitude $\geq M$, and $b \approx 1$.

**Domain:** typically valid for magnitudes between catalog completeness and tectonic-size limit. $b$ varies regionally (oceanic vs. continental, volcanic vs. fault systems).

**Envelope:** scatter in $\log N$ around the regression line is the focus of much of the literature, because it bears on hazard estimation. Specific deviations (curvature at high magnitudes, "characteristic earthquake" peaks) are domain-specific.

**Mechanism on the table:** self-organized criticality (Bak-Tang-Wiesenfeld 1987; Sornette et al.) interprets G-R as a critical-point power law. Other models (asperity, stick-slip dynamics) give G-R-like behavior from different microphysics.

**What the framework's lens contributes:** the same three questions. SOC explanations predict a *specific* envelope around the line (universality classes); other explanations predict different envelopes. The framework's discipline says: pick a mechanism, derive its envelope prediction, compare to data.

**What the framework's lens does not contribute:** a derivation of $b \approx 1$ or a unified theory of earthquakes. G-R is a robust *statistical* pattern, not a predictive equation.

---

## 4. Kolmogorov $-5/3$ (turbulence energy spectrum)

**Line:** in the inertial range of fully developed 3D turbulence, the energy spectrum $E(k) \propto k^{-5/3}$.

**Domain:** scales between the energy-injection scale and the Kolmogorov dissipation scale. The inertial range can span several decades in well-developed turbulence.

**Envelope:** intermittency corrections — multifractal scaling exponents that deviate from the Kolmogorov 1941 prediction at high moments. The line is leading order; the actual structure functions $\langle |\delta v|^p \rangle \sim r^{\zeta_p}$ have $\zeta_p$ deviating from $p/3$ in a way that quantifies intermittency.

**Mechanism on the table:** Kolmogorov 1941 dimensional analysis gives $-5/3$ assuming homogeneous isotropic turbulence and energy cascading at a constant rate. Intermittency corrections (K62, multifractal models, She-Lévêque) modify this in measurable ways.

**What the framework's lens contributes:** explicit framing of "line plus envelope" as the actual content. The framework would push: don't just verify $-5/3$, characterize $\zeta_p - p/3$ across moments, compare to model predictions.

**What the framework's lens does not contribute:** new mechanisms for turbulence. K41 and its multifractal refinements are mature physics.

---

## 5. Zipf's law (rank-frequency in language and elsewhere)

**Line:** $f(r) \propto r^{-\alpha}$ where $f$ is frequency, $r$ is rank, $\alpha \approx 1$.

**Domain:** roughly the top 10,000 most common words in many languages; departures at both ends (top few common words; long tail).

**Envelope:** the deviation pattern at the tails is informative (and often the most-studied aspect).

**Mechanism on the table:** Mandelbrot's information-theoretic derivation; preferential attachment models; Simon's stochastic model. None is universally accepted; the linguistic and information-theoretic mechanisms make different envelope predictions.

**What the framework's lens contributes:** consistent envelope-first analysis across linguistics, network science, and population biology where Zipf-like patterns appear. Discourages "Zipf is universal" handwaves; encourages mechanism comparison via envelope shape.

**What the framework's lens does not contribute:** resolution of which Zipf mechanism is right in any particular domain.

---

## Summary

| Domain | Line | Envelope | Mechanism | Framework adds? |
|:-|:-|:-|:-|:-|
| Primes | $\psi(x) \sim x$ | $\sqrt{x} \log^2 x$ (under RH) | explicit formula + zeros | Vocabulary for the conjecture |
| Kleiber | $B \sim M^{3/4}$ | unspecified in most literature | WBE fractal network (contested) | Three-question discipline |
| Gutenberg-Richter | $\log N \sim -bM$ | regional, model-dependent | SOC (one candidate) | Three-question discipline |
| Kolmogorov | $E(k) \sim k^{-5/3}$ | intermittency corrections | K41 + multifractal | Reframing as line + envelope |
| Zipf | $f(r) \sim r^{-1}$ | tail-dependent | Mandelbrot / Simon / others | Three-question discipline |

## What this catalogue is not

This is **not** a unified theory of scaling laws. Each entry has its own mechanism, its own envelope, its own contested questions. The framework's contribution is the *consistency of questions* asked across them. The framework would be falsified if it claimed to derive any of these from its own first principles; it does not.

## What this catalogue is

A reading list for the three-question discipline. Each example shows what "track the defect, not the line" looks like in a different domain. The lens is real because the questions are real. The questions don't presuppose any answer.

## What this catalogue is not yet

Filled with framework-internal claims about how these scaling laws "manifest" the parabolic envelope. They might, in some loose sense. Without a mechanism that predicts envelope shape from the framework's own ingredients, the loose sense is the only sense available — and it doesn't earn the right to be called a unification.
