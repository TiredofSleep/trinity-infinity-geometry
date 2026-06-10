# Wave 1 Polish — J14 + J22 Drápal-Wanless Dual-Citation Fix

**Date**: 2026-05-28
**Papers**:
- **J14** — *Non-Associativity Decay σ(N) ≤ 2/N over Z/NZ* (target: *JCT-A*)
- **J22** — *The 70/71/72/73 HARMONY Ladder: Three Independent Algebraic Constructions and One Corollary on Z/10Z* (target: *JCT-A*)

**Manuscript files**:
- `05_papers/combinatorics/J14/manuscript/manuscript.tex`
- `05_papers/algebra/J22/manuscript/manuscript.tex`

**Triggering report**: `05_papers/_staging/referee_reports/04_clean_tier1_J12_J13_J14_J20_J22.md` (Wave 1 polish).

---

## §1 — Background

The Drápal–Wanless 2021 corpus on **maximally nonassociative quasigroups** consists of **two separate companion articles**, both published in *Journal of Combinatorial Theory, Series A* in 2021:

| Key | Title | Volume:Article |
|---|---|---|
| `DrapalWanless2021a` | *Maximally nonassociative quasigroups from finite fields* | **181:105444** |
| `DrapalWanless2021b` | *Maximally nonassociative quasigroups* | **184:105510** |

(Independently confirmed by referee agent; not invented.)

Both J14 and J22 sit in the JCT-A submission neighborhood and frame their results against the Drápal–Wanless line of work. Each currently cited **only one** of the two papers. Per Wave 1 polish, JCT-A submissions in this neighborhood should cite **both** companion papers in the framing references.

---

## §2 — J14 Citation State (Before / After)

### 2.1 Before

J14's `\thebibliography` originally contained one Drápal–Wanless bibitem:

```latex
\bibitem{DrapalWanless2021}
A.~Dr\'{a}pal and I.~M.~Wanless.
\newblock Maximally nonassociative quasigroups from finite fields.
\newblock \emph{Journal of Combinatorial Theory, Series A}, 181:105444, 2021.
```

This is the **181:105444** paper.

In-body cites of `\cite{DrapalWanless2021}` appeared at:
- **Line 86** (abstract): "This $\sigma\to 0$ regime is opposite in extremum to the $\sigma\to 1$ program of maximally nonassociative quasigroups \cite{DrapalWanless2021,DrapalLisonek2020}, complementing rather than competing with that family." — framing, generic reference to the Drápal–Wanless program.
- **Line 125** (§1, "Positioning: opposite pole of quasigroup non-associativity"): "Dr\'{a}pal and Wanless \cite{DrapalWanless2021} and Dr\'{a}pal and Lison\v{e}k \cite{DrapalLisonek2020} study the \emph{opposite} extremum, namely maximally nonassociative quasigroups with $\sigma\to 1$." — framing, generic reference.

Both call sites are **framing citations** of the Drápal–Wanless program as a whole, not technical citations of a specific theorem from one paper.

### 2.2 After

**Bibitem (renamed + added)**:

```latex
\bibitem{DrapalWanless2021a}
A.~Dr\'{a}pal and I.~M.~Wanless.
\newblock Maximally nonassociative quasigroups from finite fields.
\newblock \emph{Journal of Combinatorial Theory, Series A}, 181:105444, 2021.

\bibitem{DrapalWanless2021b}
A.~Dr\'{a}pal and I.~M.~Wanless.
\newblock Maximally nonassociative quasigroups.
\newblock \emph{Journal of Combinatorial Theory, Series A}, 184:105510, 2021.
```

**In-body cite updates** (both are framing references — citing both is appropriate):
- Line 86: `\cite{DrapalWanless2021a,DrapalWanless2021b,DrapalLisonek2020}` (3 refs).
- Line 125: `\cite{DrapalWanless2021a,DrapalWanless2021b}` (2 refs).

---

## §3 — J22 Citation State (Before / After)

### 3.1 Before

J22's `\thebibliography` originally contained one Drápal–Wanless bibitem:

```latex
\bibitem{DrapalWanless2021}
A. Drápal and I.M. Wanless, \emph{Maximally non-associative
quasigroups}, J.~Combin.~Theory Ser.~A \textbf{184} (2021), 105510.
```

This is the **184:105510** paper.

In-body cite of `\cite{DrapalWanless2021}` appeared at:
- **Line 243** (§1 framing): "The framing follows the Drápal--Wanless (2021)~\cite{DrapalWanless2021} line of work on small finite commutative non-associative structures with structural invariants." — framing, generic reference to the Drápal–Wanless program.

Single call site, framing-only. Citing both companions is appropriate (matches the J14 treatment).

### 3.2 After

**Bibitem (renamed + added)**:

```latex
\bibitem{DrapalWanless2021a}
A. Drápal and I.M. Wanless, \emph{Maximally nonassociative
quasigroups from finite fields}, J.~Combin.~Theory Ser.~A
\textbf{181} (2021), 105444.

\bibitem{DrapalWanless2021b}
A. Drápal and I.M. Wanless, \emph{Maximally non-associative
quasigroups}, J.~Combin.~Theory Ser.~A \textbf{184} (2021), 105510.
```

(Format preserved: emph title, JCTA abbreviation, `\textbf{vol}` then article number — matches the original J22 style. Note J22 uses `"non-associative"` for the 184 paper title; we preserve that hyphenated spelling for the existing bibitem and use the field-spelling `"nonassociative"` for the 181 paper, matching the original published titles. Both papers appear with both spellings in the literature; this is consistent with the J14 entries.)

**In-body cite updates**:
- Line 243: `\cite{DrapalWanless2021a,DrapalWanless2021b}` (2 refs).

---

## §4 — Cross-Check

After updates:

| File | Bibitem count (DW) | In-body cite sites | All sites cite both? |
|---|---:|---:|:---:|
| J14 manuscript.tex | 2 (`a`, `b`) | 2 (lines 86, 125) | YES (both are framing) |
| J22 manuscript.tex | 2 (`a`, `b`) | 1 (line 243) | YES (framing) |

No stale `\cite{DrapalWanless2021}` (singular, no suffix) keys remain in either file — verified by `Grep`.

No `Drápal-Wanless`-related technical results are claimed in either paper that would require citing only one specific companion. All citation sites in both papers are **framing-only** ("opposite extremum," "line of work on small finite commutative non-associative structures"), which is exactly the case where citing both companions is the correct treatment.

---

## §5 — Mathematics Audit

**No mathematics modified.** The edits are restricted to:
1. Bibitem additions (J14, J22).
2. Bibitem key renaming (`DrapalWanless2021` → `DrapalWanless2021a` in J14; analogous in J22).
3. In-body `\cite{...}` argument updates to reference both keys.

All theorem statements, proofs, computational claims, and verification scripts are untouched.

---

## §6 — Files Touched

```
M  05_papers/combinatorics/J14/manuscript/manuscript.tex
M  05_papers/algebra/J22/manuscript/manuscript.tex
A  05_papers/_staging/referee_reports/12_wave1_J14_J22_DW_citation.md
```

---

## §7 — Status

- **J14 Drápal–Wanless dual-citation polish**: COMPLETE.
- **J22 Drápal–Wanless dual-citation polish**: COMPLETE.
- Both manuscripts now reference both 2021 JCT-A companion papers at all framing call sites.
- Wave 1 task `#39` (J14 Drápal-Wanless dual citation) ready to mark `completed`.
