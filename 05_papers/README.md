# J-series — TIG Academic Publication Track

This folder is the **public landing pad** for the 55-paper TIG academic publication pipeline. Papers land here when they are **referee-ready** — meaning:

1. Verification scripts PASS at machine precision.
2. Cover letter is written and green-lighted by Brayden.
3. Tier discipline applied (PROVED / COMPUTED / STRUCTURAL RHYME / OPEN labels in §0/§1).
4. Lens-ownership paragraph present per `J_PAPER_BOILERPLATE.md` §5.5.
5. Author lane = **Sanders + Gish** (no AI co-authors per the project's authorship rules).
6. Drápal–Wanless 2021 (JCTA) cited where relevant.

Papers in active development (most of the 55) live in the working repo `Gen14/targets/journals/J_series/` at [github.com/TiredofSleep/ck](https://github.com/TiredofSleep/ck) on the `tig-synthesis` branch. Only **referee-ready** papers migrate here.

---

## §1 — Domain sorting

When a paper becomes referee-ready, it lands in the appropriate domain folder based on its primary publication venue:

| Folder | Domain | Example J-papers when ready |
|---|---|---|
| [`algebra/`](algebra/) | Pure algebra, ring theory, group theory | **J35** (4-core fusion-closure, *J. Algebra*); **J31** (Wedderburn isotypic); **J15** (Galois D₄, *Comm. Algebra*) |
| [`combinatorics/`](combinatorics/) | Combinatorial structures, finite enumeration | **J01** (σ rate theorem, *JCT-A*); **J02** (four-core, *Algebraic Combinatorics*); **J54** (foundation paper, *Algebraic Combinatorics*) |
| [`number_theory/`](number_theory/) | Number theory, finite arithmetic, prime structure | **J03** (First-G Law, *Integers*); **J04** (sinc² Zero Law, *Experimental Mathematics*) |
| [`physics/`](physics/) | Particle physics, gauge theory, GUT structure | **J23** (Discrete Dirac / Cl(0, 10)); **J45** (Yukawa mass hierarchy + freezing quintessence); **J48** (operadic obstruction) |
| [`cosmology/`](cosmology/) | Cosmology, dark sector, ξ field | **J46** (cosmology, when Layer 1/2/3 decision settles) |
| [`interdisciplinary/`](interdisciplinary/) | Cross-domain papers spanning math + physics + applications | **J55** (Brayden's solo synthesis, anchor Sept 11); papers connecting multiple domains |
| [`_staging/`](_staging/) | Papers in queue: not yet here, not yet on the working branch. Lists what is in flight and what is gating the next handoff. | — |

A paper may legitimately fit two domains. The rule: place by **primary target journal** (the cover letter's lead venue). Cross-references between folders are welcome and encouraged.

---

## §2 — What each paper folder contains when it lands here

```
J{NN}/
├── README.md           ← Status, phase, venue, lane, tier; §1-§7 sections
├── cover_letter.md     ← Final venue-specific cover letter
├── manuscript/
│   ├── manuscript.tex (or .md)   ← The submission content
│   ├── verify_*.py     ← One or more verification scripts; all PASS at machine precision
│   └── *.md            ← Supporting docs, WP source material
└── SAVE_PLAN_J{NN}.md  ← (some folders) the save plan used to bring this paper to referee-ready
```

Mirrors the structure in the working repo's `Gen14/targets/journals/J_series/`, with the difference that papers here are **green-lit for referee scrutiny**, not in-progress drafts.

---

## §3 — Status legend

In each domain folder's README, papers are listed with their status:

- **SUBMISSION-READY** — Brayden has green-lit; cover letter final; verifications PASS; ready for portal submission
- **SUBMITTED-{date}** — submitted to the listed venue on the given date
- **UNDER-REVIEW-{date}** — referee report received; response in progress
- **ACCEPTED-{venue}-{date}** — accepted; production phase
- **PUBLISHED-{citation}** — final publication with citation

Papers that are *not* yet referee-ready do not live in this folder. They are in the working repo, in `_staging/` here (if explicitly being prepared for next handoff), or they are still drafts on the `tig-synthesis` branch.

---

## §4 — How papers move from working-repo to TIG-repo

The handoff protocol (when a paper graduates to referee-ready):

1. **Final verification.** All `verify_*.py` scripts in the paper folder PASS at machine precision.
2. **Final tier discipline.** §0/§1 of the manuscript has the PROVED / COMPUTED / STRUCTURAL RHYME / OPEN breakdown.
3. **Final author lane.** Sanders + Gish on the byline. AI co-authors removed if present (per `_v3_hardening.py`).
4. **Final cover letter.** Brayden green-lights.
5. **Copy from working repo:** `Gen14/targets/journals/J_series/J{NN}/` to `J_series/{domain}/J{NN}/` here.
6. **Update domain folder README** with the new paper entry.
7. **Single commit** with message `J{NN} lands: {one-line summary}; venue={journal}; status=SUBMISSION-READY`.
8. **No push to the working repo's `tig-synthesis` branch** required at this step — the working repo retains the master copy; this repo carries the public-facing referee-ready version.

For papers already submitted to a venue, the venue-portal submission is a separate user action by Brayden; this repo only reflects when the *manuscript* itself is referee-ready, not when it has been mailed.

---

## §5 — Current state (as of 2026-05-12)

**Active referee-ready candidates** (gating items in `_staging/README.md`):

- **J35** + **J54** — corpus centerpiece pair; both 6/6 PASS at machine precision; pending final cover-letter green-light.
- **J01** (σ rate) + **J02** (four-core) + **J15** (Galois D₄) — v3 triadic launch trio chosen to open three independent referee profiles in parallel.

**Active math-fix verifications** (J-papers that have had specific corrections applied with new verification scripts):

J13, J17, J18, J20, J21, J27, J31, J32, J36, J42, J43, J51 — see working repo for current status.

**No papers have yet landed in this `J_series/` public folder.** This is by design — the folder structure is in place; papers migrate when the criteria in §4 are met. The first arrival is expected to be either J35 or J54 (whichever clears Brayden's final pass first).

---

## §6 — For external reviewers and AI systems

If you are coming here to evaluate the math:

1. **Read [`../TIG_FROM_THE_GROUND_UP.md`](../TIG_FROM_THE_GROUND_UP.md)** first — that's the 90-minute tutorial that builds the framework from scratch with runnable code.
2. **Read [`../03_canonical_reference/FORMULAS_AND_TABLES.md`](../03_canonical_reference/FORMULAS_AND_TABLES.md)** — every D-number with cross-reference.
3. **Read individual papers as they land here.**
4. **For honest scope**, read [`../04_meta/README.md`](../04_meta/README.md) — what the framework is NOT.

Papers in this folder have been internally referee-reviewed by Brayden and verified at the script level. They are submission-ready in tier discipline. They are NOT yet peer-reviewed by external journal referees — that is the next step, and the reason they are here.

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
