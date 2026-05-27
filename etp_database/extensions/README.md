# Extensions

Python test harnesses used to generate the `verdicts/` writeups. Each
script is self-contained, reproduces a specific finding, and depends only
on the ETP `explore_magma.py` interface (set `ETP_PATH` env var).

## Scripts

| Script | What it does | Verdict |
|---|---|---|
| `sigma_magma_crypto.py` | Differential uniformity, linear bias, avalanche, MD collisions for σ-magma vs addition / affine / random | `verdicts/sigma_magma_crypto_verdict.md` |
| `steiner_vs_family_c.py` | Profile of Steiner quasigroups (orders 3, 7), linear commutative quasigroups, profile-15 order-5 SLQs | `verdicts/steiner_family_c_verdict.md` |
| `confirm_squag_profile.py` | Builds STS(3), STS(7), STS(9), cyclic STS(13) squags and computes profiles | (data for above) |
| `squag_variety_diff.py` | Identifies the 40 equation IDs that hold in STS(3,7,9) but fail in cyclic STS(13) | (data for above) |
| `sts_15_classification.py` | PG(3,2) STS(15) profile — the refuting case for the geometric-vs-combinatorial hypothesis | `verdicts/sts_classification_corrected.md` |
| `sigma_k12_embedding.py` | Tests σ-magma embedding into Aut(K₁₂) (Coxeter-Todd lattice) | `verdicts/sigma_k12_verdict.md` |

## Running

```bash
ETP_PATH=/path/to/equational_theories/scripts python sigma_magma_crypto.py
```

Most scripts complete in seconds; `sigma_magma_crypto.py 1000000 1000000`
runs in ~10s. None require >1GB RAM.

## Output format

Scripts print human-readable summaries to stdout and (where applicable)
save raw JSON data alongside in `../verdicts/`. The verdict markdown files
in `../verdicts/` are the curated written-up findings.
