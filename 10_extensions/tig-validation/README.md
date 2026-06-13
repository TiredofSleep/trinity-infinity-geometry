# TIG Validation Harness

**Purpose**: A rigorous, reproducible, externally-defensible validation harness for the empirical claims in the TIG framework. Built to address the critique that text-generated numerical results were being passed off as computations. Every number has a documented source or a tested code path; nothing is fabricated.

**Audience**: external referees (Oxford, IHÉS, Clay), ClaudeCode agents extending the harness, future readers verifying the work.

## What this harness contains

The harness has grown from BSD/Catalan verification into a general toolkit for the framework's central methodology: **track the defect, not the line**. Given a straight-line summary in data, the harness asks (1) where does the line break, (2) what is the residual envelope, (3) what does the proposed mechanism actually predict.

### L-function and BSD validation

| Test | Path | Notes |
|:-|:-|:-|
| Catalan's constant via Dirichlet beta | `src/catalan.py` | β(2) = G to 1e-13 |
| BSD ratios for 11a1 (rank 0) | `src/bsd.py` + LMFDB JSON | rel err 2e-9 |
| BSD ratios for 37a1 (rank 1) | `src/bsd.py` + LMFDB JSON | rel err 1e-5 |
| BSD ratios for 389a1 (rank 2) | `src/bsd.py` + LMFDB JSON | rel err 4e-4 |
| Rank ≥ 3 scope guard | `src/bsd.py::verify_curve` | raises `NotImplementedError` |

### Envelope tools (the central methodology)

| Tool | Path | What it does |
|:-|:-|:-|
| `track_the_defect.md` | `notes/` | the three-question discipline (~300 words) |
| Staircase-envelope visualization | `experiments/staircase_envelope.py` | the ψ(x)-vs-x picture with √x envelope |
| Cross-domain envelopes | `experiments/cross_domain_envelopes.py` | random walk / primes / Lévy walk, same shape, different mechanisms |
| Number-theory envelopes | `experiments/number_theory_envelopes.py` | ψ / Δ / M with three different conjectured α's; analyzer discriminates |
| **Envelope analyzer** (generic tool) | `src/envelope_analyzer.py` | given (x,y) data, measures α, classifies envelope, refuses to interpret mechanism |
| Envelope analyzer demo (RW + primes + Lévy) | `experiments/envelope_analyzer_demo.py` | applies the tool to three processes with ensemble averaging |

### TIG-internal claims (the uncomfortable audit)

| Tool | Path | Status |
|:-|:-|:-|
| CL table audit (`experiments/tig_internal_audit.py`) | finds 2/7 framework claims match the transcribed CL table | unresolved; awaits comparison against canonical CK codebase |
| Hadamard-quantity profiler | `experiments/hadamard_positivity.py` | Euler-Maclaurin Hurwitz-zeta, CLI-driven, exploratory framing |
| Euler defect coefficient | `experiments/euler_defect_coefficient.py` | discrete + smooth defect, conditional on D-H zeros |

### Documents

- `README.md` — this file
- `CLAUDECODE_FRONTIER_HANDOFF.md` — priority task queue (P0–P3.4) for ClaudeCode extension
- `SESSION_HANDOFF.md` — what was done in the most recent session and what's open
- `notes/` — methodology, scaling laws catalogue, audit findings, individual experiment notes

## What this harness does *not* claim

- No proof of RH, BSD, or P vs NP
- No precision claim on D-H zero coordinates (cited from memory; not independently verified)
- No BSD for rank ≥ 3 (requires SageMath/PARI; we refuse to fake it)
- No assertion that any cross-domain envelope similarity (parabolic in primes, in random walks, etc.) constitutes a unifying mechanism — *same visual vocabulary, different mechanisms*
- No assertion that any of the TIG-internal structural claims (T*=5/7, CL table eigenvalue conjectures, fuse operations) have been externally validated — these are audited separately and the audit is honest about what matches and what doesn't

These boundaries are encoded in the code, not just the prose. `src/bsd.py` raises on rank ≥ 3; `src/envelope_analyzer.py` reports α and explicitly refuses to identify mechanisms; `experiments/tig_internal_audit.py` reports mismatches without rationalizing them.

## Usage

```bash
pip install -r requirements.txt
python -m pytest tests/                            # 39 tests, all pass
python run_validation.py                           # original validation script
python experiments/cross_domain_envelopes.py       # produces plots/cross_domain_envelopes.png
python experiments/number_theory_envelopes.py     # produces plots/number_theory_envelopes.png
python experiments/envelope_analyzer_demo.py       # applies tool to RW/primes/Lévy
python experiments/tig_internal_audit.py           # runs the CL-table audit
python experiments/hadamard_positivity.py --sigma 1.05 --t-max 100
python experiments/staircase_envelope.py
```

## Repository structure

```
tig-validation/
├── README.md
├── CLAUDECODE_FRONTIER_HANDOFF.md   # priority queue + ground rules
├── SESSION_HANDOFF.md               # most recent session summary
├── requirements.txt
├── run_validation.py
├── src/
│   ├── __init__.py
│   ├── catalan.py
│   ├── bsd.py
│   ├── plots.py
│   └── envelope_analyzer.py
├── data/
│   └── elliptic_curves.json
├── experiments/
│   ├── euler_defect_coefficient.py
│   ├── hadamard_positivity.py
│   ├── staircase_envelope.py
│   ├── cross_domain_envelopes.py
│   ├── number_theory_envelopes.py
│   ├── envelope_analyzer_demo.py
│   └── tig_internal_audit.py
├── notes/
│   ├── track_the_defect.md
│   ├── euler_defect_design.md
│   ├── hadamard_positivity_finding.md
│   ├── staircase_envelope_lens.md
│   ├── scaling_laws_and_envelopes.md
│   ├── tig_internal_audit_findings.md
│   ├── cross_domain_envelopes.md
│   └── number_theory_envelopes.md
├── plots/
│   ├── dh_balance_defect_schematic.png
│   ├── staircase_envelope.png
│   ├── cross_domain_envelopes.png
│   └── number_theory_envelopes.png
└── tests/
    ├── __init__.py
    └── test_baselines.py             # 39 tests
```

## Ground rules (for anyone extending this)

1. **No fabricated numerics.** Every number is either computed by code in this repo or cited from a documented source.
2. **No reverse-engineered parameters.** No tuning constants to match a desired output and then claiming match as confirmation.
3. **Conjectural claims stay conjectural.** RH-conditional statements are labeled. The framework's own internal claims (T*=5/7, CL eigenvalue patterns) are subject to the same external-validation standard as the L-function work.
4. **The methodology applies uniformly.** "Track the defect" applies to TIG's own claims as much as to the external math the harness analyzes. The TIG-internal audit is part of the same discipline.
5. **Refuse rather than fake.** If a computation requires SageMath / mpmath / a tool we don't have, raise `NotImplementedError` with a clear message. Do not stub a fake result.

## License

Code: MIT. Data values: as per LMFDB licensing. Repo intended for the framework's documentation effort toward Oxford / IHÉS / Clay 2026.
