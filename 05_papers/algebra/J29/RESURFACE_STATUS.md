# J29 — RESURFACE STATUS (2026-09-22)

**Determination: RESURFACE.** The verified core is intact; the paper is resurfaced to
submission-ready for *Mathematics Magazine* (MAA). It was only ever *demoted* (Tier 1 → Tier 2,
2026-05-27 audit) as **pedagogical**, never as wrong — the mathematics is correct and complete.

This follows the project taxonomy: a resurface candidate = retired/held **for packaging**
with a surviving **verified core**. Here the core survives (the verifier passes 10/10), so
the paper comes back up.

## Verifier result

Command:

```
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe \
  "05_papers/algebra/J29/manuscript/verification/verify_J29.py"
```

Outcome: **PASS — exit code 0**, final line `Overall: PASS (10/10)`.

The 10 checks all PASS:
1. Theorem A — Lo Shu $D_4$ orbit has 8 distinct elements.
2. Theorem B — mod-3 reduction yields 4 distinct tables, each appearing twice.
3. Theorem F — $\mathbb{Z}/3$ is one of the tables.
4. Theorem D — all 4 tables are quasigroups.
5. Theorem E — cumulant $\kappa=\pm48$ separates commutativity ($-48$ commutative, $+48$ non-commutative).
6. Theorem C — the two non-commutative tables are opposite magmas.
7. Theorem E.1 — $V_4'$ preserves $\kappa$ for any $3\times3$ matrix (100 random trials).
8. Theorem G — Dürer $4\times4$ mod-3 shows the same pattern with $\kappa=\pm128$.
9. Diagonal Lemma — no $3\times3$ commutative quasigroup has a repeated diagonal
   (6 comm-quasigroups found by exhaustive $3^9$ enumeration, 0 violations).
10. Corollary — Lo Shu diagonal mod 3 $=\{2,2,2\}$ (constant), anti-diagonal mod 3 $=\{0,1,2\}$.

## What survives (the verified core)

The full result set of the note:
- the 4-magma exact count for the $D_4$ orbit (Theorems A, B, D),
- the opposite-magma / $\mathbb{Z}/3$ identifications (Theorems C, F),
- the cumulant witness $\kappa=\pm48$ (Theorem E) with the coset-invariance lemma
  (Theorem E.1) and the diagonal-lemma half-proof of the commutativity correlation,
- the Dürer $4\times4$ extension at $\kappa=\pm128$ (Theorem G).

All ten are machine-verified. The paper is honest about its own tier discipline: Theorem E's
commutativity correlation is half-proved (diagonal lemma) and half-observed, and the note says so.

## What was pruned / held for packaging

- **Nothing was pruned from the content.** The demotion (Tier 1 → Tier 2) was a *retarget*,
  not a cut: the material is *Mathematics Magazine*-class pedagogy rather than Tier-1 research.
  The four distinct magmas + cumulant spectrum are correct and complete.
- The only genuinely open step is a final author green-light before submission; the
  cover letter already exists (`cover_letter.md`).

## Remaining packaging work (honest; does not affect the verified core)

- **Stale pass-count in the manuscript and cover letter.** The current `verify_J29.py`
  emits **10/10** (it grew to include Theorem E.1, Theorem G, the Diagonal Lemma, and the
  Corollary). But `manuscript/manuscript.md` §5 shows a sample-output block reading
  "Overall: PASS (6/6)" with only checks 1–6, and `cover_letter.md` likewise says
  "6/6 PASS" and "~140 lines". The README §5 is already correct ("10 OK lines +
  Overall: PASS (10/10)"). The manuscript/cover-letter counts should be updated to 10/10
  before submission. (Left unchanged here to avoid rewriting manuscript prose; flagged for
  the packaging pass.)
- **Internal naming:** the script and its checks are labeled `J58` (file `verify_J29.py`,
  header "J29 verification"), while the paper is J29. Same content; harmonize the label
  before submission if desired.
- **`SAVE_PLAN_J29.md` is not in this folder.** A file of that name exists under
  `Gen13/targets/journals/J_series/J29/` (outside `05_papers/algebra/J29/`, i.e. outside
  this paper folder). Nothing in this folder depends on it.


## Update 2026-09-22 — packaging flags resolved

The stale pass-count is fixed: manuscript §5 sample block and the prose/cover references now read **10/10** (matching the script), and the sample block lists all ten checks. The verifier is renamed folder-consistent to `verify_J29.py` (was `verify_J58.py`), its internal label and all references repointed. Script re-run: PASS (10/10).
