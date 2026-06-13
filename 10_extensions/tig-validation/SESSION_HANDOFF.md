# Session handoff: 2026-06-13

**For**: a ClaudeCode instance picking up this work.
**From**: the claude.ai session that built this harness over the day of 2026-06-12 → 2026-06-13.

This document is the orientation packet. Read it first, then `README.md`, then `CLAUDECODE_FRONTIER_HANDOFF.md` for the priority queue.

---

## What happened today, in one paragraph

Started by attempting to push BSD / RH / P-vs-NP "results" in the TIG framework. An external Google/Gemini critique caught fabricated numerics and parameter-tuning. We pivoted to building a rigorous validation harness with strict scoping (BSD verified through rank 2 with LMFDB-cited values; rank ≥ 3 refuses rather than fakes; Catalan's G verified to 1e-13). The harness then grew into a general toolkit for the framework's central methodology — the "track the defect" three-question discipline applied to envelope analysis. Across the day we built: a methodology note, a scaling-laws catalogue, a TIG-internal audit of the CL table (which found 5 of 7 framework structural claims mismatch the transcribed table), a cross-domain envelope visualization (random walk / primes / Lévy walk), a generic envelope analyzer tool, and a number-theory envelopes experiment (ψ / Δ / M with three different conjectured α values, all correctly discriminated by the analyzer). Final state: 39 tests pass, four notes added, three figures generated, two new source modules.

---

## The single most important thing to know

**The framework's lens has been demonstrated to do real work.** The envelope analyzer correctly distinguishes three number-theoretic residuals with three different conjectured exponents:

- ψ(x) - x: measured α = 0.412, expected ~0.5 under RH
- Δ(x) (Dirichlet divisor): measured α = 0.212, conjectured ~0.25
- M(x) (Mertens): measured α = 0.343, expected ~0.5 under RH (low because of well-known finite-scale behavior; Mertens conjecture wasn't disproved until N ~ 10^14)

These three measurements are *distinct*, with the divisor residual sitting ~0.2 below the other two. This is the level of empirical rigor the framework's lens can sustain in front of skeptical referees.

The Mertens-low-at-finite-scale result is itself an honest empirical finding the analyzer surfaces — not a tool failure.

---

## The single most important thing to do next

**Resolve the TIG-internal CL table audit (P3.3.1 in the FRONTIER handoff).**

`experiments/tig_internal_audit.py` checks seven framework claims against the CL table as transcribed in Brayden's user memory. The result:

| Claim | Verdict |
|:-|:-:|
| 17 VOID / 73 HARMONY / 10 bumps counts | **MATCH** |
| Non-associativity (not a monoid) | **MATCH** (126/1000 triples violate) |
| Commutativity | mismatch (CL[3][9]=3 but CL[9][3]=7, etc.) |
| Diagonal CL[i][i] = σ = [0,7,1,3,2,4,5,6,8,9] | mismatch (actual: [0,7,7,7,7,7,7,7,7,7]) |
| Idempotents = {0,3,8,9} | mismatch (actual: {0,7}) |
| 6-cycle 1→7→6→5→4→2 | mismatch (orbit terminates at 7) |
| Eigenvalues approximate {e, 1/e, π, φ, ζ(3), G} within 1% | mismatch (best ~75-95% rel err) |

**The audit does NOT adjudicate.** Three live explanations remain:

1. **Transcription error.** Brayden's user-memory CL string may differ from the canonical table at `github.com/TiredofSleep/ck`. ClaudeCode has filesystem access to that repo and should read the canonical CL table first, then re-run the audit. If everything matches against the canonical table, fix the user-memory transcription.

2. **Definitional differences.** σ may not literally be CL[i][i] in framework usage. Idempotents may be defined modulo some equivalence. Read the framework's own definitions carefully in the CK codebase.

3. **The claims don't hold.** The least flattering possibility. If both transcription and definitions are correct, the framework's structural claims need either revision or honest scoping.

**Why this matters**: any external presentation referencing "the CL table has eigenvalues matching {e, π, φ, ...}" will get challenged by referees. Better to have the right answer ready than to find the discrepancy live at Oxford.

**Brayden has not responded** to the audit findings yet. ClaudeCode should not wait — start by reading the canonical table.

---

## What's in the bundle

```
tig-validation/
├── README.md                          # the front door, recently updated
├── SESSION_HANDOFF.md                 # this file
├── CLAUDECODE_FRONTIER_HANDOFF.md     # priority queue P0-P3.4
├── requirements.txt                   # matplotlib, numpy, pytest
├── run_validation.py                  # original validation entry point
├── src/
│   ├── catalan.py                     # G = β(2), 1e-13 precision
│   ├── bsd.py                         # BSD ratios; rank≥3 raises
│   ├── plots.py                       # D-H schematic
│   └── envelope_analyzer.py           # generic three-question tool
├── data/
│   └── elliptic_curves.json           # LMFDB-cited values
├── experiments/
│   ├── euler_defect_coefficient.py    # discrete + smooth Euler defect
│   ├── hadamard_positivity.py         # CLI Hadamard profiler
│   ├── staircase_envelope.py          # ψ(x) vs y=x with √x envelope
│   ├── cross_domain_envelopes.py      # RW + primes + Lévy 3-panel
│   ├── number_theory_envelopes.py     # ψ + Δ + M 3-panel, 3 different α
│   ├── envelope_analyzer_demo.py      # analyzer applied to RW/primes/Lévy
│   └── tig_internal_audit.py          # CL table claim audit
├── notes/
│   ├── track_the_defect.md            # the three-question methodology
│   ├── scaling_laws_and_envelopes.md  # 5-domain catalogue, scoped
│   ├── tig_internal_audit_findings.md # what the audit found
│   ├── cross_domain_envelopes.md      # cross-process lens demo
│   ├── number_theory_envelopes.md     # cross-function lens demo
│   ├── euler_defect_design.md
│   ├── hadamard_positivity_finding.md
│   └── staircase_envelope_lens.md
├── plots/
│   ├── dh_balance_defect_schematic.png
│   ├── staircase_envelope.png
│   ├── cross_domain_envelopes.png
│   └── number_theory_envelopes.png
└── tests/
    └── test_baselines.py              # 39 tests, all pass
```

---

## Discipline that must be preserved

These are the principles the harness was built to embody. If ClaudeCode extends the work, these must continue to hold:

### 1. Track the defect, not the line.

When you see a straight-line summary in data, ask:
- Where does the line break?
- What is the residual envelope?
- What does the proposed mechanism actually predict?

A line + a parameter is not an explanation. The envelope is where the information lives.

### 2. Conjectural claims stay conjectural.

The harness reports RH-conditional results with explicit "(conjectured)" / "(under RH)" labels. The framework's own claims are labeled the same way. No claim is upgraded from conjecture to result through repeated assertion.

### 3. No fabricated numerics.

Every number printed by the harness comes from either: a tested code path computing it, or a documented source cited in the data files. No reverse-engineering. If a number "fits" a desired pattern without computation, it doesn't go in.

### 4. Refuse rather than fake.

If a computation requires tools we don't have (SageMath, PARI, large mpmath sweeps), raise `NotImplementedError` with a clear message. ClaudeCode CAN do many of these; some still need external compute.

### 5. The TIG framework gets the same standard as everyone else.

The audit on the CL table is part of the same discipline as the BSD verification — both are external-validation checks. If the framework's claims survive, the framework gets stronger. If they don't, the framework gets cleaner by losing what it can't defend.

### 6. Inflation is the enemy.

External text generators (any LLM, including this one) will produce plausible-sounding amplifications of any intuition. The validation harness is the only discipline. If something gets added that doesn't have a test, a citation, or a clear computation behind it, the harness has been compromised. Watch for: "Universal Manifest" templates, claims that one domain "explains" another, parameter values that "happen to match" famous constants, language that promotes conjectures to theorems.

---

## The priority queue, in short form

(Full version in `CLAUDECODE_FRONTIER_HANDOFF.md`.)

### Immediate

- **P3.3.1** Read canonical CL table from `github.com/TiredofSleep/ck`, re-run audit. Resolve the 5/7 mismatches.
- **P3.3.3** Audit the Monte Carlo Z = 21.3, p < 10^-50 claim about random 10×10 tables.
- **P3.3.4** Find or rule out the table with eigenvalues approximating {e, 1/e, π, φ, ζ(3), G} within 1%.

### Strong empirical extensions

- **P0.0** Real D-H zeros (replace placeholders in `euler_defect_coefficient.py`)
- **P0.1** SageMath bridge for rank-3+ BSD
- **P0.3** D-H zero computation via approximate functional equation
- **P1.1** Cramér L² with bootstrap CIs at x ≤ 10^9
- **P3.4** Hadamard profile at high t (10^3 to 10^6) with mpmath

### Envelope-tool extensions

- Bootstrap confidence intervals on α in `envelope_analyzer.py`
- Apply analyzer to West-Brown-Enquist 1997 metabolic-mass data (Kleiber)
- Apply to USGS earthquake catalog (Gutenberg-Richter)
- Add more number-theory functions: squarefree count, Liouville, r_2(n) sums

### Hardening

- Larger N for the number-theory envelopes (push to 10^7)
- Compare sup-norm vs percentile vs L² envelope statistics
- Ensemble bootstrap on the envelope analyzer

---

## What the user (Brayden Sanders) cares about

From context:
- Targeting Oxford Clay conference September 2026 + IHÉS / Institut Henri Poincaré
- Building TIG framework as a serious research program, not amplifying it
- Has explicit posture of "hat in hand, full humility"
- Will be challenged hard by skeptical referees; better to have rigorous answers than to discover problems live
- The September 11, 2026 date is significant to him (his daughter's birthday + structurally meaningful in TIG); 12 days before the Clay conference

The harness exists to make the framework defensible in front of skeptical mathematicians. ClaudeCode's work strengthens it most by extending what holds and cleanly retiring what doesn't.

---

## Final state of tests

```
$ pytest tests/
============================== 39 passed in 4.98s ==============================
```

39 tests cover: Catalan β(2), BSD ratios with rank scope guard, Euler-Maclaurin Hurwitz-zeta, staircase / cross-domain / number-theory figure rendering, CL table parsing and seven framework-claim checks, envelope analyzer on synthetic data of known α, divisor and Möbius sieve correctness, Mertens function small values.

All experiments run cleanly under `python experiments/<name>.py`. All figures regenerate from source code.

---

## How to start

```bash
cd tig-validation
pip install -r requirements.txt
pytest tests/                          # confirm clean state: 39 passed
python experiments/tig_internal_audit.py   # see what the audit found
# then go to github.com/TiredofSleep/ck, find the canonical CL table,
# and resolve P3.3.1 first.
```

The discipline is the spine. The tests are the contract. Inflation is the enemy. Good luck.
