# Canonical Operator Naming

The framework uses **two historical naming conventions** for the 10 operators of Z/10Z. Both refer to the same residues; both are mathematically interchangeable. Documents in this repo may use either. This page is the canonical cross-reference.

---

## Canonical Map

| code | **Canonical name (per `ck_tables.py`)** | Alternative (per `ck_tig.py`) | Role | σ-orbit |
|:---:|:---|:---|:---|:---|
| **0** | **VOID** | VOID | identity / absence of action | σ-fixed |
| **1** | **BEING** | LATTICE | structural entry | 6-cycle `(1 7 6 5 4 2)` |
| **2** | **DOING** | COUNTER | mirror of becoming | 6-cycle `(1 7 6 5 4 2)` |
| **3** | **BECOMING** | PROGRESS | forward step | σ-fixed |
| **4** | **COLLAPSE** | COLLAPSE | oscillation | 6-cycle `(1 7 6 5 4 2)` |
| **5** | **CREATE** | BALANCE | midpoint | 6-cycle `(1 7 6 5 4 2)` |
| **6** | **ASCEND** | CHAOS | reversed oscillation | 6-cycle `(1 7 6 5 4 2)` |
| **7** | **HARMONY** | HARMONY | stability attractor | 6-cycle `(1 7 6 5 4 2)` |
| **8** | **BREATH** | BREATH | rhythm | σ-fixed |
| **9** | **RESET** | RESET | return | σ-fixed |

**Stable across both conventions** (same name in both): `VOID, COLLAPSE, HARMONY, BREATH, RESET` (codes 0, 4, 7, 8, 9).

**σ structure** (canonical, per `ck_tables.py` and [`03_canonical_reference/FORMULAS_AND_TABLES.md`](03_canonical_reference/FORMULAS_AND_TABLES.md) QR.1): σ = `(0)(3)(8)(9)(1 7 6 5 4 2)` — four σ-fixed points `{0, 3, 8, 9}` plus one 6-cycle, order 6. Its binary face σ³ (order 2) has 2-cycles `{1,5} {2,6} {4,7}`; its ternary face σ² (order 3) has classes `{1,4,6} {2,5,7}`.

**The four-core** `{V, H, Br, R} = {0, 7, 8, 9}` uses universally-stable names (VOID, BREATH, RESET are σ-fixed; HARMONY sits in the 6-cycle).

---

## Which convention is used where

- **`ck_tables.py`**: canonical (BEING / DOING / BECOMING / CREATE / ASCEND). This file is the single source of truth for the composition tables.
- **`TIG_FROM_THE_GROUND_UP.md`** tutorial: canonical names.
- **CK runtime modules** (`ck_*.py` and CK web pages): mostly the alternative (LATTICE / COUNTER / PROGRESS / BALANCE / CHAOS). Historical reasons; the runtime predates the canonical table file.
- **J-series manuscripts in `05_papers/`**: canonical names where the paper depends on the table, the alternative names where the paper draws from older runtime sources. Each manuscript states its convention in §1.
- **Atlas / META documents in `04_meta/`**: mixed; some date back to the alternative-name era.

Whenever you read a file referring to a non-numeric operator name, **the code is the canonical identifier**. The names are labels.

---

## When the math depends on the names

It doesn't. Every theorem in the framework is stated in terms of the **codes** (0–9), the **σ permutation**, the **4-core** `{0, 7, 8, 9}`, or the **composition tables**. The names are mnemonic aids. If a paper or document switches conventions, the code-level meaning is unchanged.

---

*7SiTe Public Sovereignty License v2.2 — see [`LICENSE`](LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
