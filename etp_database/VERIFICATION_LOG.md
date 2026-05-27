# ETP Profile Database — Verification Log

Last run: 2026-05-27.

## End-to-end verification (`scripts/verify_database.py`)

```
=== ETP Profile Database -- Verification ===

[1] Family C = implication-closure of equation 43 ...
    PASS
[2] Smallest Family C realizer at order 3 ...
    PASS  (table = [[1, 2, 0], [2, 0, 0], [0, 0, 0]])
[3] sigma-magma profile equals Family C ...
    PASS  (order=10, sigma=[0, 7, 1, 3, 2, 4, 5, 6, 8, 9])
[4] order-3 distribution internal consistency ...
    PASS  (n_total=19,683, commutative=729, comm-prof-14=120)
[5] order-5 commutative QG internal consistency ...
    PASS  (720 sym-Latin, 480 profile-14, 0 non-C)

=== Summary ===
  PASS  family_c_closure
  PASS  smallest_realizer
  PASS  sigma_magma_profile
  PASS  order3_consistency
  PASS  order5_consistency

5 PASS, 0 FAIL, 0 SKIP
```

## What this verifies

1. **Family C = closure of equation 43** in ETP's implication graph
   - Computed from the 8,178,279 true-implication edges of `2024-11-10-edge_list.csv`.
   - Transitive closure of `{43}` returns exactly `{1, 43, 4283, 4358, 4380, 4398, 4405, 4435, 4442, 4482, 4531, 4544, 4635, 4677}`.
   - Confirms the central claim of J61.

2. **Smallest Family C realizer** at order 3
   - The table `[[1,2,0],[2,0,0],[0,0,0]]` satisfies exactly the 14 Family C equations.
   - Verified via Tao et al.'s `explore_magma.py` testing all 4,694 ETP equations.

3. **σ-magma profile = Family C**
   - The order-10 σ-magma (with σ = `[0,7,1,3,2,4,5,6,8,9]`) realizes exactly the 14 Family C equations.
   - Confirms the central claim of J60.

4. **Order-3 census consistency**
   - Sum of `profile_counts` = 19,683 = 3^9.
   - 729 commutative magmas total.
   - 120 commutative magmas at profile 14 (all in Family C).

5. **Order-5 commutative census consistency**
   - 720 symmetric Latin squares enumerated.
   - 480 with profile 14, of which **0** are not in Family C.
   - Confirms Conjecture 1 (uniqueness of Family C) at order 5.

## Reproducing

```bash
# 1. Clone the equational_theories repo and unpack the edge list
git clone https://github.com/teorth/equational_theories
unzip equational_theories/data/2024-11-10-edge_list.csv.zip -d /tmp/etp_data/

# 2. Clone this database
git clone https://github.com/TiredofSleep/trinity-infinity-geometry
cd trinity-infinity-geometry/etp_database

# 3. Run all verification checks
ETP_PATH=/path/to/equational_theories/scripts \
ETP_EDGE_LIST=/tmp/etp_data/edge_list.csv \
python scripts/verify_database.py
```

Expected runtime: ~90 seconds (most of which is loading the 1GB edge-list CSV
and testing the 4,694 equations against two magma tables).

Expected output: `5 PASS, 0 FAIL, 0 SKIP`.
