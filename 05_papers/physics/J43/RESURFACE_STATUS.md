# J43 — RESURFACE STATUS (2026-09-22)

**Determination: RESURFACE.** The verified core is intact; the paper is resurfaced from
"HOLD pending NV-center experimentalist" to an active standalone quantum-control /
NV-proposal paper (target: PRA).

This follows the project taxonomy: a resurface candidate = retired/held **for packaging**
with a surviving **verified core**. Here the core survives (the verifier passes), so the
paper comes back up.

## Verifier result

Command:

```
PYTHONIOENCODING=utf-8 /c/ck_venv/lora312/Scripts/python.exe \
  "05_papers/physics/J43/manuscript/verify_J43_S4_closure.py"
```

Outcome: **PASS — exit code 0**, final line `All verifications passed.`

Reproduced quantities (script output):
- `|S_4| = 24` group elements built from generators $(12)$ and $(1234)$; character
  $(3,1,0,-1,-1)$ on the conjugacy classes confirmed.
- $U_4$ symbolic (sympy) properties exact: $\mathrm{tr}=-1$, $\det=-1$,
  eigenvalues $\{-1,i,-i\}$, $U_4^4=\mathbb{1}$.
- Change-of-basis $V$: $VV^\dagger=\mathbb{1}$, $\det V = i$.
- $U_{4,\mathrm{NV}}=VU_4V^{-1}$: $\mathrm{tr}=-1$, $\det=-1$, $U_{4,\mathrm{NV}}^4=\mathbb{1}$
  (residual $1.55\times10^{-16}$).
- Deterministic Cartan/Reck–Zeilinger six-pulse decomposition: closure residual
  $3.48\times10^{-16}$; pulse angles G_02 $(\theta{=}{+}1.1071,\phi{=}{-}4.1888)$,
  G_01 $(\theta{=}{+}0.7297,\phi{=}0)$, G_12 $(\theta{=}{+}0.4636,\phi{=}{-}1.5708)$,
  trailing Z-phases $\approx 0$.
- **Max residual over the 24-element closure: $1.84\times10^{-16}$** — matches the
  headline claim in the README, cover letter, and manuscript.

## What survives (the verified core)

The entire mathematical content of the paper:
- exact $S_3$-skeleton character match (Theorem 2.1),
- the explicit 4-cycle matrix $U_4$ with its symbolic properties (Theorem 3.1),
- the analytic change-of-basis $V$,
- the deterministic six-pulse decomposition of $U_{4,\mathrm{SU(3)}}$,
- machine-precision closure of all 24 $S_4$ elements (Theorem 6.1).

The core is **lens-invariant**: finite-group representation theory and quantum control on
$\mathbb{C}^3$, with no TIG / TSML / BHML / $\mathbb{Z}/10\mathbb{Z}$ dependence. A PRA referee can
read it cold.

## What was pruned / held for packaging

- **Nothing was pruned from the manuscript.** The paper was *held* (not shrunk) pending a
  lab partner for the experimental falsification ladder.
- On resurfacing, the **experimental Test E (projector covariance)** is reframed as a
  *proposed* measurement that invites lab-partner collaboration, rather than a blocker on
  publishing the theory. This is exactly the framing the 2026-09-21 resurface note in the
  README recommended. The theory paper is complete with or without the lab partner; the
  experimental result would be a follow-up paper.

## Remaining packaging work (honest, does not affect the verified core)

These were already tracked in the README §6 checklist and "Known issues"; none of them
touches the correctness of the verified core:
- LaTeX (REVTeX 4.2) conversion still pending.
- Lab-partner outreach is the gating step for the *experimental follow-up*, not for the
  theory paper.
- **Naming inconsistency to reconcile before submission:** the actual verifier file is
  `verify_J43_S4_closure.py` (its own docstring also opens with the stale name
  `verify_J43_S4_closure.py` and says "for J39"), but the README, cover letter, and
  manuscript refer to it throughout as `verify_J43_S4_closure.py`. Same script, correct
  content — only the filename references need harmonizing. (Left as-is here to avoid
  touching the manuscript's math; flagged for the packaging pass.)
- README §7 previously listed a "Mayes" byline; the manuscript byline is Sanders + Gish —
  cross-check before submission (already noted in "Known issues").


## Update 2026-09-22 — packaging flags resolved

The verifier filename mismatch is fixed: the script is now `verify_J43_S4_closure.py` (folder-consistent), its docstring and every reference (README, cover letter, manuscript) repointed to it. Previously the references pointed to `verify_J11_S4_closure.py`, which did not exist. Script re-run: PASS.
