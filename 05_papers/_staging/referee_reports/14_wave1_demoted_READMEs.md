# Wave 1 — Demoted-paper README fixes (2026-05-27 audit)

**Operator:** Claude (Opus 4.7)
**Date applied:** 2026-05-27
**Repo:** `trinity-infinity-geometry` (the live arXiv-target repo; NOT `CK FINAL DEPLOYED`)

## Summary

After the 2026-05-27 referee rigor pass, four TIG papers were demoted Tier 1 → Tier 2, and one was merged into J24. Each paper's README was updated with the new Tier line and an appended Demotion notice section. J25 received a TOMBSTONE banner at the top instead, redirecting readers to J24.

## Files touched

| README | Edits applied | Verified by Grep |
|---|---|---|
| `05_papers/algebra/J08/README.md` | (1) Status line: SUBMISSION-READY → DRAFT with audit reason; (2) Tier line: 1 → 2 (demoted 2026-05-27 audit; was Tier 1); (3) appended **Demotion notice** documenting 3 math errors (power-associativity FAILS at e₂; L_{e₃} not a 4-cycle; ε₂ = 2e₃ + 3e₄ NOT idempotent over F_5). | YES (line 80) |
| `05_papers/algebra/J23/README.md` | (1) Tier line: 2 (draft, defensive-exposition) → 2 (demoted 2026-05-27 audit; was Tier 1); (2) appended **Demotion notice** flagging single-observation paper / reverse-engineered prime set / missing null-hypothesis. Recommended retargeting as *Mathematical Intelligencer*-class note. | YES (line 112) |
| `05_papers/algebra/J28/README.md` | (1) Tier line: 2 (draft, Path-B rewrite) → 2 (demoted 2026-05-27 audit; was Tier 1); (2) appended **Demotion notice** noting no characterization theorem; role partition labeled by fiat. | YES (line 112) |
| `05_papers/algebra/J29/README.md` | (1) Tier line: 2 (draft, verification PASS) → 2 (demoted 2026-05-27 audit; was Tier 1); (2) appended **Demotion notice** flagging pedagogical Math. Magazine-class content. Target venue (*Mathematics Magazine*) already on line 3 — no change required. | YES (line 92) |
| `05_papers/number_theory/J25/README.md` | TOMBSTONE banner inserted at line 1 (before the original title). Banner: `# [MERGED INTO J24 on 2026-05-27]` plus blockquote redirecting readers to J24 and the detailed merger plan in `_staging/referee_reports/15_J25_to_J24_merger_plan.md`. Rest of README left intact below banner (historical record). | YES (line 1) |

## Source audit files (cited in the demotion notices)

- `05_papers/_staging/referee_reports/08_J08_power_assoc_FIX.md` (J08 math errors)
- `05_papers/_staging/referee_reports/08_promotions_audit_J17_J23.md` (J23 single-observation)
- `05_papers/_staging/referee_reports/09_promotions_audit_J24_J25_J26.md` (J25 merger)
- `05_papers/_staging/referee_reports/10_promotions_audit_J27_J28_J29.md` (J28, J29)
- `05_papers/_staging/referee_reports/15_J25_to_J24_merger_plan.md` (J25 detailed merger plan, cited in the tombstone)

## Verification protocol followed

For every Edit, ran `Grep` against the new substring (e.g. "Demotion notice (2026-05-27 audit)" or "MERGED INTO J24 on 2026-05-27") on the exact target file path to confirm the new text appears at the expected line.

All five READMEs verified PASS at line numbers reported above.

## Repo-location confirmation

All five paths begin with `C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry\05_papers\...` — the live arXiv-target repo. The earlier mistaken writes to `CK FINAL DEPLOYED\Gen14\targets\journals\...` are NOT reflected in this run. Verification step before editing confirmed the J08 directory listing (`README.md`, `cover_letter.md`, `manuscript/`) matched the target repo's expected layout.
