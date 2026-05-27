# ETP Profile Database

A queryable companion dataset to Tao et al.'s [Equational Theories Project (ETP)](https://github.com/teorth/equational_theories): for every magma we have classified, here is its **equational profile** — the set of ETP equation IDs it satisfies — together with structural metadata.

**Date of data freeze**: 2026-05-27.
**Companion papers**: J60 (linear-magma classification), J61 (taxonomy methodology).

---

## What is here

```
etp_database/
├── data/                   raw JSON datasets (~50K total)
├── scripts/                CLI query + verification harness
├── extensions/             test scripts for U-line investigations (crypto, Steiner, K_12)
├── verdicts/               written-up findings from U-line (mostly negatives + retractions)
├── lean/                   Lean 4 formalization scaffold of J61 Theorem 5
├── oeis_submissions/       4 draft OEIS sequences ready for submission
├── index.html              GitHub Pages-ready browse page
├── README.md               this file
└── VERIFICATION_LOG.md     5/5 PASS end-to-end audit
```

### `data/`

| Dataset | Rows | Description |
|---|---:|---|
| `order3_profile_distribution.json` | 19,683 | every order-3 magma, indexed by profile size and equation set |
| `order5_commutative_qg.json` | 720 | every order-5 commutative quasigroup (symmetric Latin square), with profile |
| `family_c.json` | 14 | the 14 equation IDs of Family C (closure of commutativity) |
| `profile14_families.json` | 23 | the 23 known equational profiles of size 14 in ETP, with anchor + smallest realizer |
| `sigma_magma.json` | 1 | the order-10 σ-magma: table, profile (size 14, Family C), structural certificate |
| `smallest_family_c_realizer.json` | 1 | the lex-first order-3 Family C realizer, verified by enumeration |

### `verdicts/` and `extensions/` (U-line findings)

Written-up answers to "is the σ-magma a crypto primitive / Steiner system / lattice subobject"
(spoiler: no, no, no — see `verdicts/README.md` for the mechanistic explanations). The
test scripts that generated each verdict live in `extensions/`.

### `lean/`

A Lean 4 scaffold of J61 Theorem 5 (the C5 fossil-variety theorem). Three substantive
lemmas fully proved; structural dichotomy and empirical profile bound documented as
`sorry`s pending Mathlib4 infrastructure. See `lean/README.md`.

All JSON files are reproducible from the scripts in `scripts/` and `extensions/`.

## Query interface

```bash
python scripts/query.py profile 14         # list all magmas / families with profile size 14
python scripts/query.py equation 43        # show closure of equation 43 + magmas realizing it
python scripts/query.py family C           # show Family C contents + smallest realizers
python scripts/query.py magma "[[0,1,2],[1,2,0],[2,0,1]]"   # compute profile of a given table
```

## OEIS submission drafts

The `oeis_submissions/` directory contains draft submissions for sequences we believe are novel:

| File | Sequence |
|---|---|
| `A_family_c_anchors.txt` | The 14 ETP IDs of Family C: 1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677 |
| `A_commutative_profile14_at_order_n.txt` | Number of commutative magmas with profile = Family C, at order n. n=3:120; n=5:480; ... |
| `A_distinct_profiles_order_n.txt` | Number of distinct ETP equational profiles realized by order-n magmas. n=3:158 |
| `A_profile14_count_order_n.txt` | Number of order-n magmas with |Eq_ETP| = 14 exactly. n=3:660; n=5:?; ... |
| `A_profile14_families_count.txt` | Number of distinct profile-14 equational classes (= 23 currently known) |

## Conventions

- **Magma tables** are 0-indexed lists of lists: `T[i][j] = i·j`.
- **Profile** = the set of ETP equation IDs satisfied; |Profile| is its size.
- **Family C** = the implication-closure of equation 43 (commutativity), exactly `{1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}`. (Proof: ETP implication graph; see J61 Appendix B.)
- **Family R** = the equational closure containing equation 4658 ((x·y)·y = (y·x)·x), realized at order 7 by the linear magma x·y = (5x+3y+6) mod 7.

## Reproducing

```bash
git clone https://github.com/teorth/equational_theories  # for explore_magma.py
git clone https://github.com/TiredofSleep/trinity-infinity-geometry
cd trinity-infinity-geometry/etp_database
python scripts/rebuild_all.py  # regenerates all data/ JSON from raw enumerations
```

Runtime: order-3 enumeration ~85 minutes on a single core; order-5 commutative ~3 minutes; linear magmas at orders 3–10 ~12 minutes total.

## Citation

```bibtex
@misc{tig_etp_database_2026,
  title  = {ETP Profile Database: Equational Profiles of Classified Magmas},
  author = {Trinity Infinity Geometry Project},
  year   = {2026},
  url    = {https://github.com/TiredofSleep/trinity-infinity-geometry/tree/main/etp_database},
  note   = {Companion to Tao et al., Equational Theories Project}
}
```

## License

Same as parent repository (see `../LICENSE`). Data files are CC-BY-SA-4.0; scripts are MIT.
