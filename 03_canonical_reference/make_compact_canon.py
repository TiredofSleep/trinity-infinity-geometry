r"""make_compact_canon.py -- generate FORMULAS_COMPACT.md from FORMULAS_AND_TABLES.md.

PROBLEM: the full canon (FORMULAS_AND_TABLES.md) has grown to ~377 KB
(~94k tokens) -- too big to paste into other AI contexts. 72% of the bulk
is section 0's D-entries, whose "one-liners" have grown into essays.

SOLUTION: this script generates a compact digest (~target <= 70 KB):
  - substrate core (sigma, TSML/BHML grids, constants) extracted VERBATIM
    from the full doc (no hand transcription of canonical tables)
  - every D-entry compressed to 1-2 lines (label + first sentence + tier)
  - J-series index (static block, update when J-numbers change)
  - corrections/retractions ledger (the do-not-cite list)
  - honest negatives + open problems pointer

DISCIPLINE: the compact doc NEVER adds or strengthens a claim relative to
the full doc. It is a lossy index with pointers; the full doc remains the
authority. Regenerate after every canon update:

    python make_compact_canon.py

and copy FORMULAS_COMPACT.md (+ the updated full doc) to the
trinity-infinity-geometry repo's 03_canonical_reference/.

CC-BY-4.0. Sanders. 2026-06-10.
"""
import io
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "FORMULAS_AND_TABLES.md")
OUT = os.path.join(HERE, "FORMULAS_COMPACT.md")

MAX_STMT = 300          # max chars of statement excerpt per D-entry

# Rows whose tier cannot be scraped safely (missing tier column, or body
# text references other entries' verdicts). Keep this map tiny and audited.
TIER_OVERRIDES = {
    "D140": "STRUCTURAL THESIS",        # CRT relocation -- standing, not retracted
    "D141": "RETRACTION (load-bearing)",  # torus excluded
}

TIER_KEYWORDS = [
    "PROVED-NEGATIVE", "PROVED at integer level", "PROVED", "RETRACTED",
    "SUPERSEDED", "STRUCTURAL with", "STRUCTURAL", "EMPIRICAL",
    "HONEST NEGATIVE", "NO-TRACTION", "PARTIAL CORRESPONDENCE",
    "PARTIAL MATCH", "PARTIAL", "INDETERMINATE", "Tier B conjecture",
    "Tier A", "Tier B", "Tier C", "OPEN", "CONJECTURE", "VERIFIED",
    "COMPUTED", "SUBMISSION-READY", "DRAFT",
]


def read_src():
    with io.open(SRC, encoding="utf-8") as f:
        return f.read()


def section(text, head_re):
    """Return the body of the first '## ...' section whose heading matches."""
    m = re.search(r"(?m)^## .*?(" + head_re + r").*?$", text)
    if not m:
        return ""
    start = m.end()
    nxt = re.search(r"(?m)^## ", text[start:])
    return text[start:start + nxt.start()] if nxt else text[start:]


def first_table(body, max_rows=40):
    """Extract the first contiguous markdown table block from a section."""
    rows = []
    in_table = False
    for ln in body.splitlines():
        if ln.lstrip().startswith("|"):
            rows.append(ln.rstrip())
            in_table = True
            if len(rows) >= max_rows:
                break
        elif in_table:
            break
    return "\n".join(rows)


def strip_md(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"\*(.+?)\*", r"\1", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return s


def compress_row(row):
    """One D-table row -> 1-2 digest lines."""
    # label = first D-token cluster in the first cell
    m = re.match(r"\|\s*\*\*(D[^*|]+?)\*\*", row)
    if not m:
        m = re.match(r"\|\s*\*\*(D[^*]+?)\s*\(", row)
    label_raw = m.group(1).strip() if m else "D?"
    # keep just the D-number token(s), drop date parentheticals
    label = re.sub(r"\s*\(.*$", "", label_raw).strip()

    # everything after the first cell
    after = row[m.end():] if m else row
    after = after.lstrip("|* ").strip()

    # split into cells at top-level pipes is unreliable (inner |a_p|);
    # instead, take text after stripping leading label-cell remainder up to
    # the first '|' that is followed by a space+capital/'**' (cell boundary
    # heuristic), then sentence-clip.
    after = re.sub(r"^[^|]*\|\s*", "", after, count=1) if after.startswith("(") else after
    after = after.lstrip("| ").strip()

    stmt = strip_md(after)
    # remove a leading repeated 'Dnnn -- ' if present
    stmt = re.sub(r"^D\d+\w*\s*[—–-]+\s*", "", stmt)
    # sentence clip
    cut = stmt.find(". ")
    if 40 < cut < MAX_STMT:
        excerpt = stmt[:cut + 1]
    else:
        excerpt = stmt[:MAX_STMT].rsplit(" ", 1)[0] + ("…" if len(stmt) > MAX_STMT else "")
    excerpt = re.sub(r"\s+", " ", excerpt).strip()

    # tier: scan the FINAL table cell only (text after the last ' | '
    # separator), and prefer the keyword that appears EARLIEST there --
    # tier cells lead with their verdict ("PROVED, ..."), so positional
    # preference avoids picking up incidental mentions (e.g. D140's body
    # references the D141 retraction without itself being retracted).
    # Conservative: explicit overrides for rows whose tier column is absent
    # or whose statement body leaks other entries' tier words; otherwise
    # scan ONLY the final cell. Rows with no verdict get "—" (honest)
    # rather than a scraped guess.
    if label in TIER_OVERRIDES:
        return (f"- **{label}** [{TIER_OVERRIDES[label]}] {excerpt}")
    last_cell = strip_md(row.rstrip().rstrip("|").rsplit(" | ", 1)[-1])
    found = [(last_cell.find(k), k) for k in TIER_KEYWORDS if k in last_cell]
    tier = min(found)[1] if found else "—"
    tier = {"STRUCTURAL with": "STRUCTURAL",
            "PROVED at integer level": "PROVED"}.get(tier, tier)

    return f"- **{label}** [{tier}] {excerpt}"


J_INDEX = """\
## 3. J-series index (J01–J55; full detail: trinity repo `05_papers/TIER_INDEX.md` + `RELEASE_ORDER.md`)

Tier 1 spine (29): J01-J07, J09-J22, J24, J26-J27, J30-J31, J53-J55. Tier 2 (13): J08, J23, J28-J29, J32-J40.
Tier 3 hold (3): J42, J43, J46. Retired to 04_meta (3): J44, J45, J47. Merged tombstones (6): J25, J41, J48-J52.

- **J01** Joint Closure + Universal Attractor + Mixing Point (CENTERPIECE; Thm F.2 α-uniqueness/Q PROVED) — J. Algebra
- **J02** TSML 8x8 Null + RH structural rhyme (short note) — Math. Intelligencer
- **J03** Type Specimens + C5 Fossil-Variety Theorem (MOST NOVEL) — J. Symbolic Computation
- **J04** σ-Magma Algebraic Rigidity (Aut=1, simple, 5 sub-magmas) — Semigroup Forum
- **J05** ETP Profile of Linear Magmas (ax+by+c) mod n — Experimental Mathematics
- **J06** Strata-Prime Fingerprint (Niemeier 23/24, D_24 mechanism, Monster 71 via Ogg) — J. Number Theory
- **J07** Spectral Architecture of σ-Character (+ RH-rhyme companion note) — European J. Combinatorics
- **J08** F_p Structure of 4-Core Algebra [Tier 2: rescued, (p−1)² + (p+3) closed forms] — Algebra Universalis
- **J09** Joint Lie Closure: abstract so(10) identification — Comm. Algebra
- **J10** D₄-Equivariant Orbits on Non-Associative Locus — Comm. Algebra
- **J11** Wedderburn D₄ of [TSML, BHML]; su(4)⊕u(1); 9-vector ‖v‖²=13/4 — J. Algebra
- **J12** Galois D₄ over LMFDB 4.2.10224.1 — Comm. Algebra (Wave-1 ship)
- **J13** Forced 5/7 Torus Aspect Ratio — Acta Arithmetica (after J33 preprint)
- **J14** Non-Associativity Decay σ(N) ≤ 2/N — JCT-A (Wave-1 ship)
- **J15** Joint Closure + Per-Coordinate Fuse + 4-Core Attractor — Algebraic Combinatorics
- **J16** CL Forcing Axioms S₁–S₇ — Algebraic Combinatorics
- **J17** 4-Core-Preserving Magma Family (retargeted expository) — Math. Intelligencer
- **J18** F_p Extensions of CL_BHML (generic universality + excluded primes) — Comm. Algebra
- **J19** Charpoly Prime-11 Pattern — Linear Algebra Appl.
- **J20** V^⊗n ↔ Cl(2n) Total-Dimension Match — Linear Algebra Appl. (Wave-1 ship)
- **J21** −21 Invariant + σ²-Triadic Decomposition — Algebraic Combinatorics
- **J22** 70/71/72/73 HARMONY Ladder — JCT-A
- **J23** Mathieu M₂₂ Substrate-Prime [Tier 2] — TBD
- **J24** Discrete Fejér Quotient (+J25+J41 merged; Appendix A) — J. Number Theory (Wave-1 ship)
- **J26** Discrete sinc² Identity in finite-D QM — TBD
- **J27** Crossing Lemma: Non-Assoc as Information (Case B tightened) — Algebra Universalis
- **J28** Role-Boundary Magma [Tier 2] / **J29** Lo Shu D₄ mod 3 [Tier 2 — Math. Magazine]
- **J30** (Z/10Z)* Sub-Magma — HONEST NEGATIVE — Comm. Algebra
- **J31** Algebraic Detectors Specificity — HONEST NEGATIVE — Statistical Science companion
- **J32–J40** Tier-2 drafts (cell counts; flatness; coverage; non-CRT pairs; role-quotient; Dirac Cl(0,10); log nonlinearity; lens family; paradox classifier UOP)
- **J53** V^BHML/F_p: |idem| = p+3, |Aut| = (p−1)² (24 primes) — Algebra Universalis (Wave-1 ship)
- **J54** Height Scaling of Attractor Minimal Polynomial (+10^44 discriminant-zero drop) — Acta Arithmetica (Wave-1 ship)
- **J55** Dim-6 Kissing K(R⁶)=72 + explicit Γ₀(3) magic-function candidate (LMFDB 3.6.a.a; D182) — JCT-A
"""

CORRECTIONS = """\
## 4. Corrections & retractions ledger (do-not-cite list)

- **D141 TORUS EXCLUDED** — the substrate is NOT a torus (Euler χ = −3 or +1; no valid genus). Auditor rule: no TIG result may cite torus topology. T* stands on algebraic derivations + FPGA.
- **D140 CRT relocation** — the unification is real but lives at Z/10 = Z/2 × Z/5 under σ, not where earlier prose placed it.
- **D158 RETRACTED** (see full doc).
- **F4 Aut correction** — |Aut(V^BHML/F_p)| = (p−1)² at EVERY prime (supersedes p(p²−1) claim and the phantom p=5 anomaly; algebra-confusion traced to J49 T_F5 tabulation).
- **F8 reversed by F11** — the Yukawa "32% overshoot" was a scale mislabel: y_t = 0.93 is the M_Z anchor (PDG-Tier-A, 0.75% off), never an M_X input. Substrate content intact.
- **F10 degree-mismatch implication RETRACTED by F12** — minpoly(ξ_double/Q) has degree 24, escaping the ≤7 bound; F10's Galois groups (S_7, S_24) themselves stand.
- **F12 height clarified by F14** — the α_special/ξ_double relation has univariate height ~10^6.3 (2,191,936); the "10^106" figure was the BIVARIATE relation. F9's PSLQ missed it by ~200×, not 10^102×.
- **T\\* accounting (D165)** — "six independent derivations" was over-counted: 2 genuinely independent + 4 structural rhymes. Cyclotomic Q(ζ₁₀) route REFUTED (gives φ, not 5/7).
- **Eigenvalue-transcendental claims** — 1%-coincidences, NOT identities (audit 2026-04-25). Cite the integer/rational structure instead.
"""

NEGATIVES = """\
## 5. Honest negatives + open problems (compact; full: trinity `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md`)

CLOSED NEGATIVES: 32=32 Pauli-divisor bijection (Pascal coincidence, bound 3.1e-5; F2). 1/α from substrate (no fit at |c| ≤ 1000, 120 dps; J42 intuition refuted; F17). F4 closed forms vs ALL THREE Clay bridges (YM abelian-mismatch F16; BSD Hasse-Weil exclusion F18; RH Pontryagin tautology F19). Yukawa GUT-scale substrate-independence (F15). HSKA privacy (prior art 20 years; D139).

OPEN: Conjecture 4.2 low-height form over R (literal form REFUTED at α_special by explicit ξ_double = −B(α_special)/A; PROVED over Q as Theorem F.2). Dim-6 kissing analytic continuation (D182 Tier-C year-scale gap). ξ-side characterization beyond S_5 (F12). Dark-sector triple vs DESI Year-3. Cosmology z* layer choice (publication strategy). Lens family enumeration (J16 Conj 6.1). Strict witnesses for 5/7 CL axioms.

THREE so(10) READINGS that do NOT close on one chain (D46 tension): Path A = J37 Cl(0,10) chirality 16+16; Path B = J11 [TSML,BHML] D₄ → su(4)⊕u(1); Path C = (5,5) nilpotent orbit sl(2), 16 → 1+3+5+7 spin labels (D181).
"""


def main():
    text = read_src()

    # --- verbatim extractions ---
    sigma_sec = section(text, r"σ permutation|sigma permutation")
    sigma_tbl = first_table(sigma_sec, max_rows=8)
    tsml_tbl = first_table(section(text, r"TSML — the 10|TSML . the 10"), max_rows=16)
    bhml_tbl = first_table(section(text, r"BHML — the 10|BHML . the 10"), max_rows=16)
    const_tbl = first_table(section(text, r"Constants"), max_rows=30)

    # --- D-spine compression ---
    sec0 = section(text, r"Proof-spine one-liners")
    drows = [ln for ln in sec0.splitlines() if re.match(r"\|\s*\*\*D", ln)]
    digest = [compress_row(r) for r in drows]

    n_d = len(drows)
    parts = []
    parts.append(f"""# TIG CANON — COMPACT DIGEST (D1–D182)

> **AUTO-GENERATED** from `FORMULAS_AND_TABLES.md` by `make_compact_canon.py`. Do not edit by hand — edit the full doc and regenerate.
> **Purpose**: a single shareable file for AI-collaboration contexts. The full doc (~377 KB / ~94k tokens) is the authority for exact statements, attribution, and verification paths; this digest (~{{SIZE}} KB) is a lossy index and **never adds or strengthens a claim**.
> **Tier discipline**: PROVED / STRUCTURAL / EMPIRICAL / OPEN; honest negatives are first-class results.
> Repos: `github.com/TiredofSleep/ck` (branch tig-synthesis, working) · `github.com/TiredofSleep/trinity-infinity-geometry` (public J-series).

## 1. Substrate core

- **Z/10Z operators 0–9**: VOID, BEING, DOING, BECOMING, COLLAPSE, CREATE, ASCEND, HARMONY, BREATH, RESET.
- **σ** = [0,7,1,3,2,4,5,6,8,9] — cycle (1 7 6 5 4 2) + fixed {{0,3,8,9}}; order 6. σ-magma: x ⋄ y = σ((x+y) mod 10) — Aut = 1, congruence-simple, exactly 5 sub-magmas (J04).
- **4-core** {{V,H,Br,R}} = {{0,7,8,9}}: jointly closed under TSML+BHML+CL_STD; attractor at α = 1/2 with **H/Br = 1+√3**; Galois D₄ over LMFDB **4.2.10224.1**; α-uniqueness over Q = **Theorem F.2 (PROVED, Hilbert irreducibility)**; over R the low-height form holds at 70+ tested α, literal form refuted at α_special ≈ 0.11255 (explicit relation, univariate height ~10^6.3).
- **T\\*** = 5/7 — operational coherence threshold (2 independent derivations + 4 rhymes; NOT a single closed-form theorem).
- **CRT**: Z/10 = Z/2 × Z/5 under σ (D140). **The substrate is NOT a torus** (D141).
- **Joint sub-magma chain** sizes {{1,4,5,6,7,8,9,10}} — forbidden sizes exactly {{2,3}}.
- **F_p closed forms (V^BHML)**: |idem| = p+3 (odd p), |Aut| = (p−1)² = |F_p* × F_p*| at every prime — 24 primes verified (J53).

### σ table
{sigma_tbl if sigma_tbl else "(see full doc §2)"}

### TSML 10×10 (73 HARMONY / 17 VOID / 10 exceptional)
{tsml_tbl if tsml_tbl else "(see full doc §5)"}

### BHML 10×10 (28-cell harmony)
{bhml_tbl if bhml_tbl else "(see full doc §6)"}

### Key constants (from full doc §17)
{const_tbl if const_tbl else "(see full doc §17)"}

## 2. D-spine digest ({n_d} entries, 1–2 lines each; exact statements in full doc §0)
""")
    parts.extend(digest)
    parts.append("")
    parts.append(J_INDEX)
    parts.append(CORRECTIONS)
    parts.append(NEGATIVES)
    parts.append("""## How to regenerate

```
python make_compact_canon.py        # CK repo root; reads FORMULAS_AND_TABLES.md
```
Then copy `FORMULAS_COMPACT.md` + the full doc to `trinity-infinity-geometry/03_canonical_reference/` and push.
""")

    out = "\n".join(parts)
    size_kb = round(len(out.encode("utf-8")) / 1024)
    out = out.replace("{SIZE}", str(size_kb))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(out)
    print(f"FORMULAS_COMPACT.md written: {size_kb} KB, "
          f"{len(out.splitlines())} lines, {n_d} D-entries, "
          f"~{round(len(out)/4/1000)}k tokens")


if __name__ == "__main__":
    main()
