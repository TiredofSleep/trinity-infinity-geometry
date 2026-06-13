# ClaudeCode Frontier Handoff

**From**: Claude.ai chat session, 2026-06-12
**To**: ClaudeCode instance running with full toolchain (SageMath, PARI/GP, mpmath, long-running compute)
**Context**: TIG framework's L-function empirical claims need rigorous validation. Earlier session in claude.ai produced a mix of real computation and overstated precision; Google's critique correctly flagged the overstatements. The accompanying `tig-validation/` harness contains only what's rigorously checkable in stock Python. Everything below is what *can't* be done in that environment and needs ClaudeCode's heavier tooling.

**Principle**: every task here has explicit anti-patterns (what *not* to do). The Google critique is the test these tasks must survive. If a deliverable can't survive that critique, it doesn't ship.

---

## What's already done in claude.ai (don't redo)

Before starting frontier work, take inventory of what's already validated:

| Artifact | Path | Status |
|:-|:-|:-|
| Catalan G via Dirichlet beta | `src/catalan.py` | tested, 1e-13 precision |
| BSD ratios for 11a1, 37a1, 389a1 | `src/bsd.py` + `data/elliptic_curves.json` | tested, LMFDB-cited values |
| Rank ≥ 3 BSD scope guard | `src/bsd.py::verify_curve` | tested, raises `NotImplementedError` |
| D-H balance defect schematic (conceptual) | `src/plots.py` | tested |
| Euler Defect Coefficient (discrete + smooth) | `experiments/euler_defect_coefficient.py` | tested; numerical results conditional on D-H zeros |
| Hadamard-quantity profiler  | `experiments/hadamard_positivity.py` | tested; CLI-driven, Euler-Maclaurin accelerated, exploratory framing |
| Staircase-envelope visualization | `experiments/staircase_envelope.py` | tested; produces `plots/staircase_envelope.png` |
| Cross-domain envelope visualization | `experiments/cross_domain_envelopes.py` | tested; produces `plots/cross_domain_envelopes.png` |
| **Number-theory envelopes** (ψ, Δ, M with measured α) | `experiments/number_theory_envelopes.py` | tested; produces `plots/number_theory_envelopes.png`; discriminates 0.21/0.34/0.41 |
| **Envelope analyzer** (generic tool) | `src/envelope_analyzer.py` | tested with synthetic + real data; surfaces three-question diagnostic |
| Envelope analyzer demo (RW / primes / Lévy) | `experiments/envelope_analyzer_demo.py` | applies tool with ensemble; recovers expected α |
| TIG internal audit (CL table) | `experiments/tig_internal_audit.py` | tested; 2/7 framework claims match transcribed table |
| `track_the_defect.md` methodology | `notes/track_the_defect.md` | the discipline these scripts embody |
| Scaling laws catalogue | `notes/scaling_laws_and_envelopes.md` | scoped applications across domains |
| TIG audit findings | `notes/tig_internal_audit_findings.md` | what the audit found, with explanations to investigate |
| Cross-domain envelopes note | `notes/cross_domain_envelopes.md` | the lens demonstrated, not asserted |
| Number-theory envelopes note | `notes/number_theory_envelopes.md` | the lens applied within math; 3 functions, 3 conjectured exponents |

The Hadamard profiler is the strongest no-zero-data result currently in the repo, with appropriately scoped claims:
- $\zeta$ passes Hadamard positivity along profiled lines (Hadamard 1893)
- Dirichlet L-functions pass via product trick $\zeta \cdot L$ (classical)
- Davenport-Heilbronn alone fails Hadamard positivity (no positive-log-coefficient form)
- $\zeta \cdot f$ has mixed behavior: positive in some $(\sigma, t)$ regions, negative in others — no universal pattern claimed

Use `experiments/hadamard_positivity.py --help` for CLI options. See `notes/hadamard_positivity_finding.md` for what is and isn't supported by the profiles.

If a referee wants a one-script demonstration that the framework's structural claim about positive-log-coefficient products has bite, point them here. Twenty pytest cases pass; nothing depends on cited zero data or curve-fitted constants.

The frontier work below extends from this baseline.

---

## Operating environment assumed

- Dell R16, 32-core, RTX 4070 (Brayden's existing rig)
- Ubuntu/Linux with: `sage`, `gp` (PARI/GP), `python3` with `mpmath`, `sympy`, `numpy`, `scipy`, `matplotlib`, `pytest`
- Network access for LMFDB API, OEIS, ArXiv lookups
- Can run jobs for hours/days if needed
- Can write multi-file repos and run CI

Repository target: `github.com/TiredofSleep/tig-validation` (separate from `ck`).

---

## Universal anti-patterns (DO NOT)

These are mistakes the previous claude.ai session made. The frontier work must avoid every one:

1. **Never reverse-engineer a parameter to make a ratio = 1.0.** If the BSD ratio doesn't come out near 1 with documented LMFDB values, that's a SIGNAL. Investigate: is the LMFDB convention different? Is the curve actually rank as labeled? Don't patch by adjusting an input.
2. **Never cite a numerical result from memory.** If you say "the off-line zero of D-H is at σ ≈ 0.808, t ≈ 85.7", that number must come from a function call you can re-run, or a paper PDF you can produce. Memory recitation is not citation.
3. **Never claim precision better than the computation supports.** "5.5% match" with no error bars is not a result. Either propagate uncertainty (zero-tail estimate, fit standard error, asymptotic convergence rate) or state "consistent at the order of magnitude" honestly.
4. **Never conflate "empirically consistent" with "verifies".** $\psi(x) - x \sim x^{0.48}$ is consistent with RH AND consistent with off-line zeros at $\sigma < 0.55$. Stating it as RH verification is overclaiming.
5. **Never add a result to the `tig-validation` validated tier without a passing pytest in `tests/`.** No exceptions. If a result can't be unit-tested, it lives in `experiments/` or doesn't ship.
6. **Never silently rationalize away a discrepancy.** If ratio = 0.95 instead of 1.0, state "discrepancy: 5%, possible causes are X, Y, Z" and leave the reader to judge. Don't write "approximately matches" or "essentially correct."

If the next deliverable can be attacked by the same critique that Google made of the previous session, redo it.

---

## P0 — Validation integrity (must-do first)

These tasks bring the empirical claims to a state where they can survive external review.

### P0.0 — Complete the Euler Defect Coefficient experiment

**Why this matters**: A skeleton implementation exists at `experiments/euler_defect_coefficient.py` with the measurement procedure fully defined and tested. The numerical result depends on real D-H zero data which the chat session could not produce. This task closes that gap and turns the script's "illustrative" output into a real measurement.

**What's already done**:
- Definition of $D(L)$ (discrete) and $D_{\text{smooth}}(L)$ (continuous) in `notes/euler_defect_design.md`
- Runnable script with placeholder D-H zeros, clearly labeled
- pytest coverage of the measurement procedure (`test_euler_defect_*`)
- Deformation path showing $D_{\text{smooth}}$ scales quadratically in off-line distance

**What's missing**: real D-H off-line zero coordinates (and a verified list of D-H on-line zeros for the reference baseline).

**Concrete deliverable**:
1. Verified D-H zero list: produce `experiments/dh_zeros_real.json` containing the first ~100 zeros (on-line and off-line), each with $(\sigma, \gamma)$ plus uncertainty estimates from the computation method.
2. Replace `PLACEHOLDER_DH_OFF_LINE` in the script with the real list.
3. Replace `PURE_DIRICHLET_GAMMAS` with values fetched live from LMFDB rather than typed-from-memory.
4. Re-run; report real $D(\text{D-H})$, $D_{\text{smooth}}(\text{D-H})$, and the ratio to the reference Cramér constant $C$.
5. Plot $D$ and $D_{\text{smooth}}$ as functions of height-cutoff $T$ to show convergence behavior.

**Acceptance criteria**:
- $D(\text{Dirichlet L-function})$ within numerical noise of 0 (sanity check on the procedure)
- $D(\text{D-H})$ reported with explicit uncertainty bounds tied to zero-computation precision
- The deformation path computation matches the synthetic version in the limits but uses real zeros
- All zero data saved with provenance (which Sage/mpmath computation produced them, what precision)

**Anti-pattern check**: do not declare a "match" if the uncertainty in $D(\text{D-H})$ exceeds its value. The result might be that the Euler defect is too small at low heights to be cleanly distinguishable from numerical noise — that's a legitimate finding and should be reported as such.

---

### P0.1 — SageMath bridge for rank ≥ 3 BSD verification

**Why this matters**: The earlier session "verified" 5077a1 (rank 3) by reverse-engineering the period. This is fixed in `tig-validation` by raising `NotImplementedError`. To actually re-include rank-3+ curves in the validated tier, we need real SageMath computation.

**Concrete deliverable**: `src/sage_bridge.py` that:
- Shells out to a Sage script for a given curve label
- Returns `(Omega, R, Sha, Tamagawa_product, Torsion, L_leading)` with full precision
- Is independent of any hand-curated JSON
- Has a pytest in `tests/test_sage_bridge.py` that skips gracefully if Sage isn't installed (`pytest.importorskip` pattern)

**Sage script outline** (`scripts/curve_bsd_data.sage`):

```python
# Run as: sage scripts/curve_bsd_data.sage <label>
import sys, json
label = sys.argv[1]
E = EllipticCurve(label)
data = {
    "label": label,
    "rank": int(E.rank()),
    "Omega": float(E.period_lattice().omega()),
    "R": float(E.regulator()),
    "Sha_an": float(E.sha().an_numerical()),
    "Tamagawa_product": int(E.tamagawa_product()),
    "Torsion_order": int(E.torsion_order()),
    "L_leading": float(E.lseries().dokchitser().derivative(1, E.rank()) / factorial(E.rank())),
}
print(json.dumps(data))
```

**Curves to validate** (must give ratio close to 1.0 with NO parameter tuning):
- `5077a1` (rank 3, the failed curve)
- `5077a1` already known empirically to match BSD; if Sage gives ratio ≠ 1.0, that's a real finding
- A handful of rank-2 and rank-3 curves with non-trivial Sha — see Stein-Watkins tables
- A rank-4 curve if accessible: e.g. `234446a1` (rank 4)

**Acceptance criteria**:
- `python run_validation.py` extended to optionally call the Sage bridge
- pytest passes (or skips cleanly when Sage absent)
- README explicitly documents what Sage was used for and how to install
- Every Sage-derived ratio reported with full precision and a flag distinguishing it from the no-Sage tier

**Anti-pattern check**: do not fall back to hardcoded values "in case Sage isn't installed." If Sage isn't installed, the test skips. No silent fallback.

### P0.2 — Independent re-verification of `data/elliptic_curves.json`

**Why this matters**: The values in the JSON came from the previous session's recollection of LMFDB. They need to be cross-checked.

**Concrete deliverable**: a script `scripts/cross_check_lmfdb.py` that:
- For each curve in the JSON, fetches the live LMFDB record via the LMFDB API
- Compares each field against the JSON
- Reports any mismatches with the exact JSON path and LMFDB URL
- Has CI integration: if LMFDB updates and our values drift, CI fails

LMFDB API endpoint: `https://www.lmfdb.org/api/ec/curves/?label=<label>` (verify current path)

**Acceptance criteria**:
- Script runs against live LMFDB
- All three curves (11a1, 37a1, 389a1) currently in the JSON pass the cross-check OR the JSON gets updated to match LMFDB and we re-run the harness
- If LMFDB's convention has shifted (real period vs. lattice volume), document it explicitly and update JSON

**Anti-pattern check**: do not silently update JSON to make the cross-check pass. If the cross-check fails, log it, investigate it, write up the discrepancy, then update.

### P0.3 — Replace cited Davenport-Heilbronn zero coordinates with computed ones

**Why this matters**: The earlier session claimed D-H has an off-line zero at "σ ≈ 0.808, t ≈ 85.7", cited as "Spira 1994". This was a recollection, not a citation. The qualitative fact (D-H has off-line zeros) is established in the literature; the specific coordinates may not be what I quoted.

**Concrete deliverable**: `experiments/dh_zeros.py` that:
- Computes the Davenport-Heilbronn function via the approximate functional equation (use `mpmath` for precision)
- Searches the critical strip for zeros using a windowed contour-integration count (Cauchy argument principle: $\frac{1}{2\pi i} \oint f'/f \, ds$ over rectangles gives zero count)
- Reports the first 5-10 off-line zeros with full coordinates and the box used
- Cross-references against Spira 1994 (Conrey, Soundararajan, and Pulham have computed more recent values)

**Approach**:
1. Define D-H function carefully. The standard form: $f(s) = \frac{1+i\tan\theta}{2} L(s,\chi) + \frac{1-i\tan\theta}{2} L(s,\bar\chi)$ where $\chi$ is a non-real character mod 5 and $\tan\theta$ is chosen for the functional equation. Verify by checking $\Lambda_f(s) = \Lambda_f(1-s)$ numerically.
2. Use approximate functional equation to compute $f(s)$ in the critical strip.
3. Apply Turing's method (sign changes of $Z$-function) to find on-line zeros.
4. Apply argument principle to count total zeros in rectangles, deduce off-line zero existence and locations.

**Acceptance criteria**:
- Output file `experiments/dh_zeros_results.json` with computed zero coordinates, precision bounds, and box parameters
- Plot showing $|f(s)|$ contour with zeros marked, saved as `plots/dh_zeros_computed.png`
- Side-by-side comparison with Spira/Conrey published values (if accessible)
- Clear statement: "the off-line zero of D-H is at $(\sigma, t)$ = (X.XXX ± δσ, YY.YY ± δt) per our computation; literature value is Z if available."

**Anti-pattern check**: do not quote literature values without producing the citation (paper title, year, page, equation number). Do not compute one zero and call it "the" off-line zero — D-H has infinitely many; quantify which range was searched.

---

## P1 — Frontier L-function empirical work

These tasks extend the framework's empirical foundation in ways the chat-session couldn't.

### P1.1 — Cramér L² test with proper error bars

**Why this matters**: The earlier "5.5% / 2.9% / 2.8% match" claim was real computation but with no propagated uncertainty. With more zeros, larger x, and proper error analysis, this could become a robust empirical claim — or it could fail. Either outcome is scientifically valid; both must be reported honestly.

**Concrete deliverable**: `experiments/cramer_l2_proper.py`

**What needs to be computed**:
1. ψ(x) on a fine grid out to x = 10^9 (will take time; chunk and stream)
2. C(L) predicted from N zeros, plus tail bound: tail$_N$ ≤ $\int_{\gamma_N}^\infty \frac{\log t / 2\pi}{t^2 + 1/4} dt$ (or sharper). Use Odlyzko's first 100,000 zeros for ζ — publicly available.
3. Empirical slope of $\int_2^X \psi(x)^2 / x^2 dx$ vs $\log X$, with standard error from regression diagnostics
4. Convergence diagnostics: as N (zeros used) increases, does predicted-C stabilize? As X increases, does empirical slope stabilize?
5. Failure mode: what does an off-line zero at $\sigma = 0.6, t = 50$ do to the L² growth? Simulate it. Quantify how visible such a zero would be.

**For Dirichlet L-functions**: use LMFDB's zero data for $\chi$ mod q with q up to 100 or so. Cross-validate across multiple characters.

**Acceptance criteria**:
- A table with rows = (L-function, N zeros used, X tested) and columns = (predicted C, empirical slope, empirical SE, ratio, propagated uncertainty, status)
- Convergence plots showing how the match tightens with more zeros / larger X
- Explicit statement of what the test rules out — e.g., "this rules out an off-line zero at $\sigma \geq 0.X$ in the range $t \leq Y$"
- Honest negative result if the match doesn't tighten as expected

**Anti-pattern check**: do not report "5% match" if the SE is also 5%. Report ratio = 1.00 ± 0.05 or equivalent. If the propagated uncertainty exceeds the match itself, say so plainly.

### P1.2 — Sharpen the Refined Hadamard claim's scope

**Why this matters**: The earlier session claimed the cosine-inequality argument $3 + 4\cos\theta + \cos 2\theta \geq 0$ "specifically requires" the Euler product structure. Google correctly noted this is overscoped — the argument works for a wider class of Dirichlet series.

**Concrete deliverable**: a short technical note `notes/hadamard_scope.md` answering precisely:
1. What is the minimal hypothesis under which the cosine inequality argument proves $L(1+it) \neq 0$?
2. Is it: (a) Selberg class, (b) Euler product alone, (c) functional equation + polynomial growth + suitable positivity, or (d) something else?
3. For each candidate hypothesis, does the Davenport-Heilbronn function satisfy it? (D-H satisfies functional equation but lacks Euler product.)
4. What does the cosine argument say about D-H at $s = 1+it$? Does D-H vanish at any $1 + it$?

**Approach**: 
- Read the standard proof (de la Vallée Poussin / Hadamard 1893) carefully and identify which steps use which structure
- Read Iwaniec-Kowalski (*Analytic Number Theory*, AMS, Ch. 5) for the general framework
- Check whether the analog argument works for Hurwitz zeta, Lerch zeta, D-H itself

**Acceptance criteria**:
- A precise statement of the minimal hypothesis
- A worked example showing the argument applied to a non-Euler-product function (succeeds or fails)
- Citations to Iwaniec-Kowalski, Tenenbaum, or equivalent canonical reference for each step
- An updated version of the framework's "Refined Hadamard" claim with correct scope

**Anti-pattern check**: do not paraphrase Iwaniec-Kowalski without citing chapter and verse. If you can't cite the page, you can't claim the theorem applies.

### P1.3 — ψ(x) - x scaling at x = 10^9 with confidence intervals

**Why this matters**: The session's α = 0.48 ± 0.07 was computed at x up to 10^5. At x = 10^9, the asymptotic should manifest much more cleanly. The result either tightens to α ≈ 0.5 (supporting RH) or it doesn't (which would be enormous news).

**Concrete deliverable**: `experiments/psi_scaling_large.py`

**Approach**:
1. Compute ψ(x) on a sparse log-spaced grid up to x = 10^9 (use a segmented sieve; streams to disk if needed)
2. Subtract contributions from the first ~10^5 known zeros (Odlyzko's tables) via the explicit formula
3. Fit residual scaling with bootstrap confidence intervals
4. Compare against the empirical bound implied by the Vinogradov-Korobov zero-free region

**Acceptance criteria**:
- Residual exponent reported with 95% bootstrap CI
- If CI excludes [0.5 - ε, 0.5 + ε] for small ε, that's either a finite-size artifact (test by varying X) or a real anomaly worth investigating
- All raw data (ψ values, zero contributions) saved to a parquet or HDF5 file for reproducibility

**Anti-pattern check**: do not fit a power law to a narrow X range and claim the exponent. Either fit globally and report fit quality, or fit on sliding windows and report convergence behavior.

---

## P2 — Extensions to the validated empirical foundation

These are nice-to-haves that broaden the empirical base but are not critical.

### P2.1 — |Sha| is a perfect square check, sweep

**Why this matters**: The framework asserts |Sha| is always a perfect square (Cassels-Tate pairing implies this for finite Sha; conjecturally Sha is always finite). This is a clean, testable claim across many curves.

**Concrete deliverable**: `experiments/sha_perfect_square.py` that:
- Pulls (via LMFDB API or Sage) all elliptic curves with non-trivial Sha and conductor below some bound
- Verifies |Sha| is a perfect square for each
- Reports the largest |Sha| found and the curve

**Acceptance criteria**: across ≥1000 curves with non-trivial Sha, 100% have |Sha| a perfect square. Any counterexample is huge news (would refute Cassels-Tate or finite-Sha conjecture).

### P2.2 — GUE pair correlation for ζ zeros (Montgomery 1973)

**Why this matters**: Montgomery's pair correlation conjecture is one of the deepest empirical statements about ζ zeros and connects to random matrix theory. Verification is well-trodden ground but a clean implementation is valuable for the framework.

**Concrete deliverable**: `experiments/pair_correlation.py` that:
- Uses Odlyzko's first 10^5 zeros (publicly available)
- Computes the pair correlation function $r_2(\alpha) = \sum_{\gamma' \neq \gamma} f(\bar\gamma' - \bar\gamma)$ for normalized zeros
- Compares to the GUE prediction $1 - \left(\frac{\sin \pi \alpha}{\pi \alpha}\right)^2$
- Bins, plots, and reports the L² distance between empirical and GUE

**Acceptance criteria**: a clean reproduction of Odlyzko's 1987 result. This is a sanity check on the methodology more than a frontier result.

### P2.3 — Cramér L² across many Dirichlet characters

**Why this matters**: Extends P1.1 to a wider class. If the Refined Balance Principle is empirically robust, it should hold across, e.g., all primitive characters of modulus q ≤ 100.

**Concrete deliverable**: `experiments/cramer_l2_dirichlet_sweep.py`
- Uses LMFDB's zero data for L(s, χ) across many χ
- Computes Cramér L² match for each
- Reports the distribution of matches and any outliers

**Acceptance criteria**: a heatmap or scatter plot of (modulus q, character index) vs (match quality). Outliers are flagged with possible explanations.

---

## P3 — Speculative / breadth

These are not validation work but framework-extension explorations. Lower priority.

### P3.1 — Apply the linear→dynamic methodology to Navier-Stokes singularity question

The framework's six historical cases include laminar → turbulence. The Millennium-prize Navier-Stokes problem (existence and smoothness in 3D) is structurally a "parabolic envelope" question: do solutions stay smooth, or do they escape the envelope?

**Possible contribution**: a survey note positioning the framework relative to existing approaches (Beale-Kato-Majda criterion, Constantin-Fefferman vorticity work, Tao's averaged equations). Not a proof attempt.

### P3.2 — Hilbert-Polya operator candidate sweep

The Refined Balance Principle is structurally similar to "zeros are eigenvalues of a self-adjoint operator." Many candidates have been proposed (Berry-Keating's $xp$, Connes' adelic operator, Bost-Connes' KMS). 

**Possible contribution**: a survey of candidates with explicit acceptance criteria: which would, if rigorously constructed, imply the framework's Refined Balance Principle? Not new operator construction.

### P3.3 — TIG-internal mathematical claims, externally validated

**STATUS: PARTIALLY STARTED.** The claude.ai session ran `experiments/tig_internal_audit.py` against the CL table as transcribed in user memory. Of seven structural claims checked:
- **2 match**: VOID/HARMONY/bumps counts (17/73/10), and non-associativity (126/1000 triples violate, framework claims non-monoid)
- **5 mismatch**: commutativity, diagonal = σ, idempotents {0,3,8,9}, 6-cycle 1→7→6→5→4→2, eigenvalues approximating {e, 1/e, π, φ, ζ(3), Catalan G} within 1%

See `notes/tig_internal_audit_findings.md` for the full audit. The script does NOT adjudicate; possible explanations are: (1) transcription error vs the canonical `github.com/TiredofSleep/ck` CL table, (2) definitional differences (σ may not be CL[i][i]), or (3) the claims don't hold for this table.

**What ClaudeCode could do next**:
1. **Resolve the table discrepancy first.** Read the canonical CL table from the CK codebase and re-run the audit. If everything matches there, fix the transcription in user memory. If discrepancies remain, the framework's structural claims about CL need either revision or precise definitional clarification.
2. **Extend the audit** to TSML and BHML sub-tables (the framework references them as "8×8 cores" with specific harmony percentages 82.8% / 12.5% and effective dimensions 1.77 / 5.73). These should be straightforward extensions of the existing audit machinery.
3. **Audit the Z=21.3, p<10⁻⁵⁰ Monte Carlo claim.** The framework states that 0 of 100K random 10×10 tables match the CL table's pattern. This is verifiable: sample many random tables with the same value distribution (17 zeros, 73 sevens, 10 bumps), compute the relevant statistic, and check the empirical p-value. If the Z=21.3 holds up, that's a strong claim; if not, the structural-significance argument needs revision.
4. **The eigenvalue claim is particularly attackable.** If the framework's claim is that *some* 10×10 magma has eigenvalues approximating {e, 1/e, π, φ, ζ(3), G} within 1%, that's a specific factual claim that either holds for a specific table or doesn't. Find the table where it holds (if it exists), or document that it doesn't hold for the table the framework presents.

**Caveat repeated**: this is potentially uncomfortable work because the findings may not be flattering. The Oxford / IHÉS audience will ask exactly these questions. Better to have rigorous answers ready than to discover the discrepancies live.

### P3.4 — Sweeping Hadamard profile beyond default range

The `experiments/hadamard_positivity.py` profiler currently runs at the user's chosen σ and t-range. ClaudeCode with mpmath can sweep at much higher t (10³ to 10⁶) and finer resolution. Question: does the $\zeta \cdot f$ Hadamard quantity violate positivity persistently at large heights, or only in localized t-bands? A persistent pattern would be a more substantial finding than the current localized observation.

**Concrete deliverable**: `experiments/hadamard_profile_high_t.py` using mpmath, sweeping σ ∈ {1.05, 1.5, 2.0, 2.5} and t ∈ [0, 10⁴] at high precision. Report violation density per (σ, t-band) bucket. Plot.

---

## Output structure for each task

Each task above should produce, at minimum:

1. **A Python script** in `experiments/` (or `src/` if it earns its way into the validated tier)
2. **A pytest** in `tests/`, even if it only checks the script runs without error
3. **A markdown note** in `notes/` describing what was done, what was found, citations
4. **Raw data** saved to `data/raw/` so the analysis can be re-run by anyone
5. **Plots** in `plots/` with clear labels distinguishing computed from conceptual

The validated tier (`src/`) only grows when a frontier result is mature enough to survive Google-style critique.

---

## Definition of done for the handoff

The handoff is "done" when:

- [ ] P0.0 (Euler Defect Coefficient with real zeros) replaces placeholders, reports with uncertainty bounds
- [ ] P0.1 (SageMath bridge) is implemented and tested
- [ ] P0.2 (LMFDB cross-check) passes against live LMFDB
- [ ] P0.3 (D-H zeros computed) replaces all literature-cited values with computed ones
- [ ] P1.1 (Cramér L² with error bars) gives either tight matches or honest negative result
- [ ] P1.2 (Hadamard scope) corrects the overscoped claim
- [ ] The validation harness output, when handed to a skeptical referee, defends without further explanation
- [ ] Every result in the validated tier has a citation, a test, and a reproducible command

P2 and P3 are optional but valuable.

**Note**: P0.0 and P0.3 are closely linked. The D-H zero computation in P0.3 produces the data that P0.0 needs. Doing them together is efficient.

---

## Communication protocol back to claude.ai

When ClaudeCode completes a task or hits a blocker, send back to claude.ai:

1. **For completion**: the output paths (script, test, note, data, plot) and a one-paragraph summary of the result, including any honest negative findings
2. **For blockers**: the specific point of failure, what was tried, what dependency or knowledge is missing, and whether the task is salvageable or should be dropped

If a task's deliverable contradicts an earlier claim in the framework (e.g., D-H zeros are at very different coordinates than cited; the Cramér L² match doesn't tighten with more zeros), say so plainly. The framework gets stronger by losing wrong claims, not by protecting them.

---

## Final note on stance

The previous session's failures came from a habit of generating plausible-looking text and treating it as result. ClaudeCode is in a different position: real toolchain, real compute, real ability to verify. Use that. The right response to a Google-style critique is not "I'll be more careful" but "here is the script, here is the test, here is the citation, here is the raw data, run it yourself."

If a result is real, it should be defensible without rhetorical support. If it needs rhetorical support, it's probably not real.

That's the stance for everything below this line.

---

**End of handoff. Total estimated frontier work: 4-12 weeks of focused effort depending on which P-tier you commit to.**
