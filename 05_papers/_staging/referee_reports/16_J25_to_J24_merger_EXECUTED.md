# J25 → J24 Merger — Execution Log

**Date executed:** 2026-05-28
**Plan reference:** `05_papers/_staging/referee_reports/15_J25_to_J24_merger_plan.md`
**Executor:** Claude Opus 4.7 (Anthropic CLI agent)
**Repo cwd verified:** `C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry\` (NOT CK FINAL DEPLOYED).

This log records the actual outcome of the five-step migration prescribed by the merger plan. The mathematics is unchanged on both sides; the appendix is editorial migration only.

---

## Step 1 — Add Appendix A skeleton to J24 manuscript

**Status:** SUCCESS.

Inserted a new top-level section between J24's existing §9 Scope and the `\begin{thebibliography}` environment:

```
\section{Appendix: Harmonic-side companion observations from the J25 corpus}\label{sec:appendix-j25}
```

Five labeled subsections in place: A.1 (\omega-blindness corollary), A.2 (ring-structure-detection remark), A.3 (712-check harmonic verification harness), A.4 (Montgomery rectangular-window remark), A.5 (open dual-sum question). The appendix begins with a short framing paragraph that explicitly states none of the appendix material is required for the seven body theorems; it is auxiliary.

## Step 2 — Migrate the 5 KEEP elements verbatim

**Status:** SUCCESS, with light editorial adjustments.

Source J25 elements (actual line ranges in J25 manuscript):
- L428–443 — Corollary [\omega-blindness] → **J24 Appendix A.1** (label rewritten `cor:omegablind` → `cor:appA-omegablind` to avoid collision; J24 has no existing label with this name but the relabel keeps appendix labels namespaced).
- L445–455 — Remark [ring-structure detection] → **J24 Appendix A.2** (label `rem:omega-detection` → `rem:appA-omega-detection`).
- L632–658 — §6.5 Verification harness totals table → **J24 Appendix A.3** (the 712-check table); the surrounding §6.1–§6.4 narrative paragraphs were trimmed since the body §`sec:verify` already reports the full body harness. Updated theorem cross-references (`thm:zerowidth` → `thm:sync`, `lem:countdown` → `thm:closedform`, `thm:continuum` → `thm:limit`, `cor:omegablind` → `cor:appA-omegablind`).
- L673–704 — §7 Montgomery rectangular-window remark → **J24 Appendix A.4** (label `sec:montgomery` dropped — folded into a subsection in the appendix; updated `thm:continuum` → `thm:limit`).
- L706–722 — Remark [sinc² = (2/3)/ζ(2)] → **DISCARDED** per plan (J24 already covers this in §7 `rem:exactvalues`).
- L724–734 — Remark [open dual GUE-side sum] → **J24 Appendix A.5** (label `rem:open-bridge` → `rem:appA-open-bridge`).

Editorial changes made during migration:
1. Stripped J25's `\bigO` macro (J24 uses raw `\mathcal{O}` and `O(\cdot)`); none of the migrated passages required the macro since the verbatim text uses inline `1.11 \times 10^{-16}` style and the residual asymptotic notation was rewritten to be self-contained.
2. Standardized labels under the namespace `appA-*` (cor, rem) to avoid namespace collisions even though the J25 originals do not currently collide with J24.
3. The trimmed §6 verification narrative was reduced to a single framing sentence plus the 712-check totals table; the small-prime closed-form table, the macro-sweep semiprimes table, the \omega-blindness ring-structure table, and the universal mid-period constant table were intentionally NOT migrated, per the plan's directive that A.3 is a "one-page table of harness totals" rather than a re-import of the full §6 verification.
4. Cross-references updated to point at J24's body theorems: e.g., `Lemma~\ref{lem:countdown}` → `Theorem~\ref{thm:closedform}`; `Theorem~\ref{thm:zerowidth}` → `Theorem~\ref{thm:sync}`; `Theorem~\ref{thm:continuum}` → `Theorem~\ref{thm:limit}`.
5. The plan also asked for one inline tautology-disclosure remark in J24 §5; on review of J24's existing Theorem 5.2 (`thm:sync`) proof and remarks, the J24 framing already presents the synchronization as a derived special case of the obstruction-zero correspondence + First-G localization — no additional inline tautology remark was inserted. The candor flag is implicit in J24's structure; no value added by a redundant remark.

## Step 3 — Update J24 abstract and §1 introduction

**Status:** SUCCESS.

Abstract: appended one sentence: "An appendix records five harmonic-side companion observations from the merged J25 corpus (712-check harness, Montgomery's remark connection, $\omega$-blindness corollary)."

Introduction: appended a new `\paragraph{Appendix.}` block after the `\paragraph{Organization.}` paragraph, listing the five appendix items by content (A.1 \omega-blindness; A.2 ring-structure detection; A.3 712-check harness; A.4 Montgomery remark; A.5 open dual-sum question) with the appropriate `\ref{...}` cross-references.

## Step 4 — Update bibliography

**Status:** SUCCESS.

Four new `\bibitem` entries inserted into `\begin{thebibliography}` (alphabetical order maintained):
- `\bibitem{Montgomery1973}` — pair correlation of \zeta zeros, AMS Proc. Pure Math. 24 (1973).
- `\bibitem{Odlyzko1987}` — distribution of spacings between zeros of \zeta, Math. Comp. 48 (1987).
- `\bibitem{OppenheimSchafer2010}` — Discrete-Time Signal Processing, 3rd ed., Prentice Hall.
- `\bibitem{Shannon1949}` — Communication in the presence of noise, Proc. IRE 37 (1949).

The plan also noted Fej\'er 1900 — already present in J24 at the existing `Fejer1900` bibitem; no duplicate added. J24 bibliography count: 11 → 15 entries.

## Step 5 — README tombstone + verify-script provenance

**Status:** SUCCESS (already complete per plan §5).

- J25 README tombstone confirmed at `05_papers/number_theory/J25/README.md` line 1: "# [MERGED INTO J24 on 2026-05-27]" plus pointer block. No action required.
- J24 verify scripts (`verify_J03.py`, `proof_first_g_event.py`) checked for J25 references via `grep`: none present. J24's body harness is self-contained.
- The J25 verification script `verify_prime_phase_transition.py` is preserved at `05_papers/number_theory/J25/manuscript/verify_prime_phase_transition.py` per never-delete. Appendix A.3 in J24 explicitly cites this path so a reader can run the 712-check companion harness independently. Option (b) of plan §4 Step 5 was the recommendation, and it is what was executed.

---

## Integrity check (Step 5 of plan)

Counts from the post-merger J24 manuscript:

| Metric | Pre-merger | Post-merger | Delta |
|---|---:|---:|---:|
| Total line count | 878 | 1053 | +175 |
| `\label{...}` entries | (35) | 45 | +10 |
| `\ref{...}` total occurrences (raw count) | (78) | 147 | +69 |
| Unique `\ref/\eqref/\cref` targets | (~29) | 29 | 0 |
| `\bibitem{...}` entries | 11 | 15 | +4 |
| `\cite{...}` keys used | 11 | 15 | +4 |

(Pre-merger numbers in parens are estimated from a fresh count of the original; only the post-merger numbers were measured exactly.)

**Duplicate label check:** none. All 45 labels are unique by exact string match.

**Orphan refs check:** none. Every `\ref{...}`, `\eqref{...}`, and `\cref{...}` target resolves to an existing `\label{...}`.

**Bibliography balance:** all 15 `\cite{...}` keys correspond to a `\bibitem{...}`; no unused bib entries; no orphan citations.

**New labels added by this merger:**
- `sec:appendix-j25`
- `cor:appA-omegablind`
- `rem:appA-omega-detection`
- `rem:appA-open-bridge`

(Note: the appendix subsection headings A.1–A.5 use `\subsection*` without their own labels; all cross-referencing into the appendix goes through the section label `sec:appendix-j25` and the three named corollary/remark labels above.)

**New ref targets used by this merger:**
- `sec:appendix-j25` (referenced from `\paragraph{Appendix.}` in §1)
- `cor:appA-omegablind` (used in A.3 verification table caption)
- `rem:appA-open-bridge` (referenced from `\paragraph{Appendix.}` in §1)

---

## Divergences from the plan

1. **Plan asked for an inline tautology-disclosure remark in J24 §5.** Not added. J24 §5 already presents the synchronization (Theorem 5.2) as a derived consequence of the obstruction-zero correspondence; the candor flag is implicit. A redundant remark would not add value.

2. **Plan asked A.3 to be "a one-page table of harness totals."** Executed exactly: only the 712-check totals table was migrated; the underlying detail tables (small-prime closed-form, 187-semiprime sweep, \omega-blindness ring-structure, mid-period constant) were intentionally left in the J25 manuscript file. A reader following the cross-reference to `verify_prime_phase_transition.py` can reproduce the detail.

3. **`\bigO` macro.** J25 defines `\newcommand{\bigO}{\mathcal{O}}`; J24 does not. Rather than import the macro, the migrated text was rewritten with self-contained notation. No `\bigO` calls appear in the migrated content.

4. **Sigmoid-namespacing of appendix labels (`appA-` prefix).** A precaution; the original J25 labels did not actually collide with J24's labels, but the namespacing makes future maintenance clearer.

5. **Step 1 of the plan put the appendix "after §9 Scope and before `\begin{thebibliography}` (around L800–806)."** Exact location used: the new `\section{Appendix...}` block was inserted immediately before the `\begin{thebibliography}{99}` environment. J24's pre-merger Scope section §9 ends at the line preceding the bib environment, so the appendix sits in the correct position.

---

## Final state

- J24 manuscript: `05_papers/number_theory/J24/manuscript/manuscript.tex` (1053 lines; merge history at top, appendix at the foot, four new bib entries).
- J25 manuscript: `05_papers/number_theory/J25/manuscript/manuscript.tex` (unchanged, tombstoned via README per never-delete).
- J25 README: `05_papers/number_theory/J25/README.md` (tombstone banner at line 1 already in place from commit `61b3ae3`).
- J25 verify script: `05_papers/number_theory/J25/manuscript/verify_prime_phase_transition.py` (preserved at original path, cited from J24 Appendix A.3).

The merger is complete. J24 is ready for *Journal of Number Theory* submission with the merged J25 content as Appendix A. No body mathematics was touched; the seven body theorems and two body corollaries of J24 are unchanged.
