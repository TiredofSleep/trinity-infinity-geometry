# 30 — Retirements executed: J44, J45, J47

**Date**: 2026-05-27
**Action**: Three Tier-3 RETIRE-candidate papers moved from `05_papers/` to `04_meta/retired_J_papers/` per the 2026-05-27 TIER_INDEX audit. Original paths now contain single-file tombstone READMEs redirecting to the new location.

---

## Move commands run (git mv preserves history)

```bash
git mv 05_papers/physics/J44              04_meta/retired_J_papers/J44_FN_Pattern
git mv 05_papers/physics/J45              04_meta/retired_J_papers/J45_Operadic_Obstruction
git mv 05_papers/interdisciplinary/J47    04_meta/retired_J_papers/J47_Atomic_Substrate
```

All three were registered by git as pure renames (status `R`), preserving full commit history on every file (manuscript, cover letter, verification scripts).

### git status excerpt — confirms rename, not copy+delete

```
R  05_papers/physics/J44/README.md                    -> 04_meta/retired_J_papers/J44_FN_Pattern/README.md
R  05_papers/physics/J44/cover_letter.md              -> 04_meta/retired_J_papers/J44_FN_Pattern/cover_letter.md
R  05_papers/physics/J44/manuscript/manuscript.tex    -> 04_meta/retired_J_papers/J44_FN_Pattern/manuscript/manuscript.tex
R  05_papers/physics/J44/manuscript/verify_J45_yukawa.py -> 04_meta/retired_J_papers/J44_FN_Pattern/manuscript/verify_J45_yukawa.py

R  05_papers/physics/J45/README.md                    -> 04_meta/retired_J_papers/J45_Operadic_Obstruction/README.md
R  05_papers/physics/J45/cover_letter.md              -> 04_meta/retired_J_papers/J45_Operadic_Obstruction/cover_letter.md
R  05_papers/physics/J45/manuscript/manuscript.md     -> 04_meta/retired_J_papers/J45_Operadic_Obstruction/manuscript/manuscript.md
R  05_papers/physics/J45/manuscript/verify_J48_operadic_obstruction.py -> 04_meta/retired_J_papers/J45_Operadic_Obstruction/manuscript/verify_J48_operadic_obstruction.py

R  05_papers/interdisciplinary/J47/README.md          -> 04_meta/retired_J_papers/J47_Atomic_Substrate/README.md
R  05_papers/interdisciplinary/J47/manuscript/manuscript.md -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/manuscript.md
R  05_papers/interdisciplinary/J47/manuscript/verification/clifford_substrate_shell.py -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/clifford_substrate_shell.py
R  05_papers/interdisciplinary/J47/manuscript/verification/meta_extension.py -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/meta_extension.py
R  05_papers/interdisciplinary/J47/manuscript/verification/pauli_divisor_bijection.py -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/pauli_divisor_bijection.py
R  05_papers/interdisciplinary/J47/manuscript/verification/strand_orbital_map.py -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/strand_orbital_map.py
R  05_papers/interdisciplinary/J47/manuscript/verification/verify_d2d1_closed_form.py -> 04_meta/retired_J_papers/J47_Atomic_Substrate/manuscript/verification/verify_d2d1_closed_form.py
```

---

## Tombstone redirect stubs in place

After `git mv` removed the source folders, three new single-file tombstone READMEs were written at the original locations so any stale link reaches a redirect rather than a 404.

| Tombstone path | Target |
|---|---|
| `05_papers/physics/J44/README.md` | `../../../04_meta/retired_J_papers/J44_FN_Pattern/` |
| `05_papers/physics/J45/README.md` | `../../../04_meta/retired_J_papers/J45_Operadic_Obstruction/` |
| `05_papers/interdisciplinary/J47/README.md` | `../../../04_meta/retired_J_papers/J47_Atomic_Substrate/` |

Each tombstone states the retirement reason and the date (2026-05-27). Verified by `ls`:

```
05_papers/physics/J44/               -> README.md (tombstone only)
05_papers/physics/J45/               -> README.md (tombstone only)
05_papers/interdisciplinary/J47/     -> README.md (tombstone only)
```

### Retirement reasons recorded in tombstones

| Paper | Reason |
|---|---|
| **J44** (FN Pattern λ=10/49 with SU(5) Indexing) | Tier-C structural rhyme; the FN pattern λ=10/49 + SU(5) indexing is a numerical coincidence rather than a derivation. Not ship-worthy for a refereed venue. |
| **J45** (Operadic Obstruction Synthesis) | Duplicates J10's operadic D₄ obstruction content. The Tier 1 spine already contains the operadic-obstruction analysis at J10; this draft is a redundant earlier formulation. |
| **J47** (Atomic-Substrate D100-D104) | Tier-C atomic-substrate correspondence; D100-D104 are integer/rational identities not theorems; per status hygiene the retirement question supersedes the venue question. |

---

## TIER_INDEX.md updates

1. **Tier 3 table**: J44, J45, J47 rows now strike-through with "RETIRED to `04_meta/retired_J_papers/...` (2026-05-27)" and the retirement reason. Header retitled "Tier 3 — hold / retire candidates (4 papers after 2026-05-27 retirements; 3 RETIRED)" and active set noted as J41-J43 + J46.

2. **Numbers summary table**: Tier 3 count revised from **7 → 4**. New "Retired to `04_meta/retired_J_papers/`" row added with count **3**. Total-row note updated to "48 active ship-targets; J25 + J44 + J45 + J47 now tombstones".

3. **Quick legend**: Tier 3 bullet now notes that J44/J45/J47 have been retired with tombstone redirects.

4. **Numbering scheme range table**: J41-J47 entry annotated "(J44, J45, J47 retired to `04_meta/` 2026-05-27)".

## RELEASE_ORDER.md

Grep of `J4[4-7]` against `RELEASE_ORDER.md` returns **no matches** — none of J44/J45/J47 appear in any Wave 1-4 ship plan, so no edits are needed there. (J46 is also absent — it is HOLD-not-ship for terahertz-experimentalist reasons, matching the Tier 3 hold classification.)

---

## Verification checklist

- [x] Source folders `05_papers/physics/J44`, `05_papers/physics/J45`, `05_papers/interdisciplinary/J47` no longer contain manuscript content.
- [x] Each source path contains a single `README.md` tombstone with retirement reason + date.
- [x] Each retired tree lives at `04_meta/retired_J_papers/<NewName>/` with full manuscript + cover letter + verification scripts intact.
- [x] All moves registered as git renames (`R`), preserving file history.
- [x] TIER_INDEX.md Tier 3 table updated with strike-through entries + retirement notes.
- [x] TIER_INDEX.md Numbers summary updated (Tier 3: 7→4; Retired: 3).
- [x] TIER_INDEX.md legend + range table annotated with retirement note.
- [x] RELEASE_ORDER.md confirmed clean (no Wave references to J44/J45/J47).

## Aftermath / portfolio impact

- **Tier 1 spine**: unchanged at 26 papers (J01-J07, J09-J22, J24, J26-J27, J30-J31).
- **Tier 2 active drafts**: unchanged at 13 papers.
- **Tier 3 hold**: now 4 papers (J41 merger-tombstone, J42 needs collaborator, J43 needs NV experimentalist, J46 needs terahertz experimentalist).
- **Retired to `04_meta/`**: 3 papers (J44, J45, J47) with full history preserved.
- **MERGED tombstones**: unchanged at 6 papers.
- **Net active ship-targets**: 48 (down from 51 in the post-audit numbering).

The retirement closes out the "RETIRE candidate" entries in the 2026-05-27 TIER_INDEX. The remaining Tier 3 set (J41-J43, J46) is HOLD-not-retire — each waits on an experimental collaborator or a venue decision rather than being structurally unship-worthy.
