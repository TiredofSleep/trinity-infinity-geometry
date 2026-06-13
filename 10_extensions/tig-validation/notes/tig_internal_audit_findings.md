# TIG internal audit — findings on the CL table

**Status**: First externally-verifiable check on the framework's internal mathematical claims. Reproducible via `experiments/tig_internal_audit.py`. Tested in `tests/test_baselines.py::test_*audit*`.

This note records what the audit found. It does **not** judge whether the framework is right or wrong — it reports the specific discrepancies between the transcribed CL table and the framework's stated claims, and lays out possible explanations for the framework's owner to address.

The discipline here is the same as for the BSD work earlier this week: report what the computation yields. Do not reverse-engineer parameters. Do not "patch" findings to make them come out right.

---

## What the audit checked

Seven structural claims about the CL table, as transcribed in user memory:

```
0000000700|0737777777|0377477779|0777777773|0747777787|
0777777777|0777777777|7777777777|0777877777|0797377777
```

| # | Claim | Result |
|:-:|:-|:-:|
| 1 | VOID(0)=17, HARMONY(7)=73, bumps=10 | **MATCH** |
| 2 | Commutative: CL[i][j] = CL[j][i] | MISMATCH |
| 3 | Non-associative (not a monoid) | **MATCH** (126/1000 triples violate) |
| 4 | Diagonal CL[i][i] = σ = [0,7,1,3,2,4,5,6,8,9] | MISMATCH |
| 5 | Idempotents {0,3,8,9} | MISMATCH |
| 6 | 6-cycle 1→7→6→5→4→2 under σ | MISMATCH |
| 7 | Eigenvalues approximate {e, 1/e, π, φ, ζ(3), Catalan G} within 1% | MISMATCH |

Two match, five do not. Details below.

---

## Details on the matches

### Counts (17/73/10) match exactly

Counting entries in the transcribed table:
- VOID(0): nine 0s in row 0; one 0 each in rows 1–6 and 8–9 (none in row 7) → **17**
- HARMONY(7): **73** (computed by subtraction; visible inspection confirms)
- bumps (entries that are neither 0 nor 7): **10**

This is the framework's own count and is internally consistent with the transcription.

### Non-associativity matches

The framework states CL is a commutative magma, *not* a monoid (i.e., non-associative). The transcribed table is non-associative: 126 of 1000 triples (a, b, c) ∈ {0..9}³ have $(a*b)*c \neq a*(b*c)$ where $*$ is CL. Framework: ✓.

---

## Details on the mismatches

### Commutativity

Framework claims CL is commutative. Transcribed table has:
- CL[3][9] = 3, but CL[9][3] = 7
- CL[4][9] = 7, but CL[9][4] = 3

(and possibly more — the audit reports the first two.)

This is straightforward to check by inspecting rows 3, 4, 9 of the transcribed table. The 9th entry of row 3 is 3; the 3rd entry of row 9 is 7. They are not equal.

### Diagonal

Framework states σ = [0, 7, 1, 3, 2, 4, 5, 6, 8, 9] and that "Diagonal=σ". The actual diagonal CL[i][i] of the transcribed table is:

```
[0, 7, 7, 7, 7, 7, 7, 7, 7, 7]
```

Only positions 0 and 1 match the claimed σ. The rest of the table's diagonal is uniformly 7 (HARMONY).

### Idempotents

Framework claims idempotents are {0, 3, 8, 9} — i.e., elements where CL[i][i] = i. The transcribed table has:
- CL[0][0] = 0 ✓
- CL[3][3] = 7 (not 3)
- CL[7][7] = 7 ✓ (not claimed)
- CL[8][8] = 7 (not 8)
- CL[9][9] = 7 (not 9)

Self-fixed elements in the transcribed table: **{0, 7}**.

### 6-cycle from 1 under σ

If σ = diagonal of the transcribed table, then σ = [0, 7, 7, 7, 7, 7, 7, 7, 7, 7], and the orbit of 1 is:
- 1 → σ(1) = 7
- 7 → σ(7) = 7 (loops)

So the orbit is **[1, 7]** of length 2, not the claimed 6-cycle [1, 7, 6, 5, 4, 2].

### Eigenvalues

Framework claims the CL matrix has eigenvalues approximating {e, 1/e, π, φ, ζ(3), Catalan's G} within 1%.

Computed eigenvalues of the transcribed table (numpy.linalg.eigvals):

```
61.37,  6.44,  5.77,  0.76 ± 0.86i,  -0.00,  0.00,  -1.58,  -3.73,  -6.79
```

For each claimed constant, the closest eigenvalue and relative error:

| Constant | Value | Closest eigenvalue | Relative error |
|:-:|:-:|:-:|:-:|
| e | 2.718 | 0.762 + 0.859i | 78.6% |
| 1/e | 0.368 | ≈ 0 | 100% |
| π | 3.142 | 0.762 + 0.859i | 80.5% |
| φ | 1.618 | 0.762 + 0.859i | 74.9% |
| ζ(3) | 1.202 | 0.762 + 0.859i | 80.2% |
| Catalan G | 0.916 | 0.762 + 0.859i | 95.2% |

None of the six constants is within 1% of any eigenvalue. The closest match (Catalan G to 0.762, but the eigenvalue is complex) has 95% relative error.

If the framework's claim were within 100% (i.e., any of the constants is *approximately* any of the eigenvalues), it would still fail: the constants range from 0.37 to 3.14, while the closest non-complex eigenvalue (other than ~0) is 5.77.

---

## Possible explanations

These are not adjudicated by the script. The framework's owner is in the best position to investigate.

**1. Transcription error.** The CL table as stored in user memory may differ from the version maintained in the framework's authoritative codebase. The Z/10Z physics sprint and Monte Carlo Z=21.3 statistics presumably used a specific table; if that table is not what's transcribed here, the audit is measuring the wrong thing. Recommendation: compare the digit string above against the canonical CL table in `github.com/TiredofSleep/ck`.

**2. Definitional differences.** The framework's σ may not be the literal diagonal CL[i][i]. It might be a permutation derived by a different operation — for example, the principal eigenvector's sign pattern, or the action of some specific element. Similarly, "idempotents" might mean idempotents under a *different* operation than CL[i][i] = i. Recommendation: confirm the operational definitions of σ and idempotent in the framework's text.

**3. The claim does not hold.** If the transcription is right and the definitions are as the audit assumed, then five of the seven claims are simply not facts about the CL table. This would mean the framework's structural claims about CL need revision.

The audit script does not select among (1), (2), (3). All three are live possibilities until the framework owner investigates.

---

## What this means for the framework's discipline

If the CL table is the framework's bedrock structural object — the carrier of the 73-HARMONY-17-VOID structure, the source of the eigenvalue claims, the algebraic foundation of fuse() and BHML/TSML — then five out of seven claimed properties not verifying from the transcription is a substantial issue. Either the transcription is wrong (fixable) or the claims are (harder to fix).

The framework's discipline this week has been: report what is, do not reverse-engineer. That discipline now applies to the framework's own claims. The validation harness was built to refuse fabricated empirical content; it must also refuse unverified structural content, regardless of which side of the table the unverified content sits on.

Recommendation: before any Oxford/IHÉS presentation cites Z/10Z structural results, run this audit script against the authoritative CL table from the CK codebase. If it passes there, the transcription was the issue. If it doesn't pass there either, the structural claims need either revision or a precise statement of which definitions they use.

This is uncomfortable. It is also exactly the work that distinguishes a defensible research program from an inflated one.

---

## What's already audited; what isn't

Audited here:
- Counts (VOID/HARMONY/bumps)
- Commutativity
- Associativity
- Diagonal
- Idempotents
- σ-orbit of 1
- Eigenvalue approximations to {e, 1/e, π, φ, ζ(3), G}

Not audited (out of scope for this script):
- T* = 5/7 (definitional)
- BHML / TSML separation (requires a separate table)
- "Doing" table (separate object)
- Spectral gap 54.93 (computable; can add)
- Generators {012, 071, 123} (requires generator definition)
- {1,4,9} → full algebra in 2 steps (requires reachability machinery)
- Non-associativity rates for sub-tables (12.8%, 49.8%, 56.8%)
- Z/10Z physics constants (downstream of CL)
- DBC translator (requires Hebrew/Latin mapping tables)
- Fruits of Spirit mapping (definitional, not mathematical)

The script is structured to make adding further audits straightforward. If the framework's owner wants to add specific TSML or BHML tables, the audit framework extends naturally.
