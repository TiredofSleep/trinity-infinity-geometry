# Integration checklist for ClaudeCode

The claude.ai session that built this package didn't have access to:
- The canonical CK codebase at `github.com/TiredofSleep/ck`
- The journal-paper series this gets integrated into
- The actual notation, definition, and citation conventions used across the existing work

Treat this package as a *proposal* that needs to be reconciled with the live repo. The work below is what to verify before merging.

---

## A. Reconcile against the canonical CK codebase

### A.1 The CL table — highest priority

`experiments/tig_internal_audit.py` parses the CL table from the digit-string in the claude.ai session's user-memory:

```
0000000700|0737777777|0377477779|0777777773|0747777787|
0777777777|0777777777|7777777777|0777877777|0797377777
```

**Before doing any further audit work**:
1. Find the canonical CL table in the CK codebase (likely `ck_core.py`, or in one of the lattice modules).
2. Compare digit-by-digit against the transcription above.
3. If they match → the 5 mismatched claims in `notes/tig_internal_audit_findings.md` need to be either reformulated or retired.
4. If they don't match → fix the audit script's `parse_cl_table()`, re-run the audit, and update `notes/tig_internal_audit_findings.md` with the corrected findings.

Either outcome is honest. Do not avoid this step.

### A.2 Definitions used in the audit

The audit makes specific assumptions about what σ, "idempotent," and "orbit" mean for the CL table:

| Concept | Audit's assumption | Verify against canonical |
|:-|:-|:-|
| σ | `σ[i] = CL[i][i]` (diagonal) | Read the framework's actual definition |
| idempotent | `i` such that `CL[i][i] = i` | Check whether framework uses fuse-based definition |
| orbit of 1 | iterated `CL[x][x]` starting from 1 | Check whether framework means orbit under fuse(·,·,1) or different ternary op |
| 6-cycle | sequence of distinct values in orbit | Check if framework defines cycle differently |

Each of these has multiple reasonable definitions. The mismatches in the audit could entirely be resolved by adjusting these definitions to match the framework's canonical usage. Read the framework's own definitions FIRST, then re-audit.

### A.3 The fuse operation

`fuse(a, b, c) = CL[CL[a][b]][c]` is the audit's definition. Verify this matches the canonical CK definition. There are at least two natural variants (`CL[CL[a][b]][c]` vs `CL[a][CL[b][c]]`); the framework's choice should be documented.

---

## B. Reconcile against the journal-paper series

### B.1 Hadamard quantity definition

`experiments/hadamard_positivity.py` defines:

```
Hadamard(s) = real_part(zeta(s) * f(s))
```

where `f(s)` is the smooth normalization the paper specifies. The claude.ai session's session refactored this with Euler-Maclaurin Hurwitz-zeta. **Verify**:
1. The `f(s)` in the script matches the paper's definition exactly.
2. The Euler-Maclaurin truncation depth is sufficient at the σ values the paper claims (default σ=1.05).
3. The "positivity" framing in the paper's claim matches the script's `min(H) > 0` test.

Likely friction points: sign conventions, complex-vs-real conventions, where the gamma factor goes.

### B.2 Euler defect coefficient definition

`experiments/euler_defect_coefficient.py` has both a "discrete" and "smooth" defect:

- Discrete: `D_K = log(K) - sum_{p ≤ K} log(p)/p^σ`
- Smooth: `D_K^smooth = log(K) - integral version`

The journal paper may use one of these, or a third version. Pick the canonical one; archive the others or relegate to a comparison appendix.

### B.3 BSD verification scope

`src/bsd.py::verify_curve` currently raises `NotImplementedError` for rank ≥ 3.

**Decide**:
- Keep the guard as-is (defensible, refuses to fake what we can't verify); OR
- Implement the SageMath bridge (P0.1 in the frontier handoff) and remove the guard

The first is safer for an external referee. The second is more useful research output. Brayden's call.

### B.4 The "track the defect" methodology

`notes/track_the_defect.md` is ~300 words of methodology. **Decide**:
- Does this become a methods section in one of the journal papers?
- Does it stay as developer-notes only?
- Does it get a standalone short methodology paper?

The discipline is the spine of the harness; the question is how visible to make it.

### B.5 Citation conventions

The data file `data/elliptic_curves.json` cites LMFDB URLs inline. The journal series likely has a stricter convention (BibTeX, author-year, persistent identifiers). Reconcile.

### B.6 Notation

The notation used throughout the harness:
- `ψ(x)` for von Mangoldt summatory
- `Δ(x)` for divisor problem residual
- `M(x)` for Mertens
- `S_n` for random walks

If the journal series uses different symbols (e.g., `R(x)` for the divisor residual, capital Psi vs lowercase), normalize.

---

## C. Code-level review pointers

### C.1 `src/envelope_analyzer.py`

The most-likely-to-be-extended file. Key design choices to verify:

- **90th percentile statistic.** The analyzer uses 90th percentile of |residual| per bin, not max or L². For the divisor problem this gave α = 0.21 vs conjectured 0.25 — possibly because 90th percentile is anti-conservative relative to sup-norm. ClaudeCode could compare multiple statistics (P90, P95, P99, max, L²) on the same data and report which best matches the conjectured exponent for known cases.
- **Quantile bins, not geomspaced.** Geomspaced bins biased alpha upward when sample density was non-uniform; switching to quantile bins fixed this for the synthetic tests. Verify this choice for the journal data formats.
- **`skip_line_fit=True` for already-residual data.** When y is e.g. ψ(x) - x or a random walk S_n, the analyzer should not refit a line. The cross-domain demo uses this flag; the journal-paper version may or may not.

### C.2 `experiments/number_theory_envelopes.py`

Verify:
- The main terms subtracted from D(x) match the paper's convention. The script uses `x log(x) + (2γ - 1)·x`. Voronoi adds `1/4`; some references absorb it into a single constant. The paper's choice matters for the residual's measured α.
- The divisor sieve `divisor_count_sieve` is O(N log N) and exact. Tested against d(1)..d(12) in `tests/test_baselines.py`.
- The Möbius sieve `mobius_sieve` is exact via smallest-prime-factor. Tested against μ(1)..μ(12).
- The Mertens cumsum uses int64 to avoid overflow at N = 200,000+.

### C.3 Tests

39 tests pass. Verify:
- Each test's expected value is either a known closed form (Catalan G, μ small values, d small values, π²/6, etc.) or a documented LMFDB value, NOT a value that was reverse-engineered from the script's output.
- No test uses `assert math.isnan(x) or x > 0` style escape hatches.
- No test catches generic `Exception` to hide failures.

### C.4 What's NOT tested but should be

- Real D-H zeros (currently placeholder)
- The Hadamard quantity at high t (>1000)
- The envelope analyzer with bootstrap CIs
- The number-theory envelopes at N > 10^6

These are explicitly P0/P1 priorities in `CLAUDECODE_FRONTIER_HANDOFF.md`. The TODOs in those files are real; they should not be silently dropped on integration.

---

## D. After verification: completing the frontiers

`CLAUDECODE_FRONTIER_HANDOFF.md` has the priority queue. After A, B, and C are clean, work through P0 → P3.4 in order.

The two most-likely-to-be-immediately-rewarding:

- **P3.3.1** (resolve CL table against canonical) — clears the audit overhang.
- **P0.0 + P0.3** (real D-H zeros via approximate functional equation) — promotes `euler_defect_coefficient.py` from "conditional on placeholder zeros" to "actually computing."

These two unlock most of the rest.

---

## E. What not to do during integration

These are the failure modes the harness was built to prevent. They apply on integration too.

1. **Don't accept claims into the paper series that lose their tests on the way in.** If a number isn't tested in `tests/test_baselines.py` or directly cited from data, it doesn't go into the paper.
2. **Don't restore rank-3 BSD "verification" without SageMath.** The guard is there because the earlier numbers were unreliable.
3. **Don't reformulate the 5 audit mismatches as features.** If they're real, they're real. If they're transcription errors, fix the transcription. If they're definitional, fix the definition. Don't paper over them.
4. **Don't absorb the cross-domain envelopes work into a unification claim.** The note `notes/cross_domain_envelopes.md` is explicit: same visual vocabulary, different mechanisms. The paper version should preserve this scoping.
5. **Don't upgrade the Mertens-α-low-at-finite-scale observation into a "framework prediction."** It's a known finite-scale phenomenon that long predates the framework. The framework's contribution is the consistent measurement, not the phenomenon.

---

## F. Sanity checks before submission anywhere

Before any of this gets into a paper that goes to a referee:

```bash
pytest tests/ -v                                 # all green
python experiments/tig_internal_audit.py        # report matches the audit note
python experiments/number_theory_envelopes.py   # alphas reproduce
python experiments/envelope_analyzer_demo.py    # RW/Lévy alphas reproduce
python experiments/cross_domain_envelopes.py    # figure regenerates
diff <(python run_validation.py) expected_output.txt   # if it exists
```

If any of these fail or produce changed numbers after integration, something has drifted. Fix it before submitting.

---

The package is provisional. The repo is authoritative. The journal series defines the conventions. Make the package match.
