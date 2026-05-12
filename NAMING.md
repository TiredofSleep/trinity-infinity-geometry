# Canonical Operator Naming

The framework uses **two historical naming conventions** for the 10 operators of Z/10Z. Both refer to the same residues; both are mathematically interchangeable. Documents in this repo may use either. This page is the canonical cross-reference.

---

## Canonical Map

| code | **Canonical name (per `ck_tables.py`)** | Alternative (per `ck_tig.py`) | Role | σ-orbit |
|:---:|:---|:---|:---|:---|
| **0** | **VOID** | VOID | identity / absence of action | σ-fixed |
| **1** | **BEING** | LATTICE | structural entry | 4-cycle `(1 7 9 3)` |
| **2** | **DOING** | COUNTER | mirror of becoming | 4-cycle `(2 8 6 4)` |
| **3** | **BECOMING** | PROGRESS | forward step | σ³-fixed (in 4-cycle `(1 7 9 3)`) |
| **4** | **COLLAPSE** | COLLAPSE | oscillation | 4-cycle `(2 8 6 4)` |
| **5** | **CREATE** | BALANCE | midpoint | σ-fixed |
| **6** | **ASCEND** | CHAOS | reversed oscillation | 4-cycle `(2 8 6 4)` |
| **7** | **HARMONY** | HARMONY | stability attractor | σ³-fixed (in 4-cycle `(1 7 9 3)`) |
| **8** | **BREATH** | BREATH | rhythm | σ³-fixed (in 4-cycle `(2 8 6 4)`) |
| **9** | **RESET** | RESET | return | σ³-fixed (in 4-cycle `(1 7 9 3)`) |

**Stable across both conventions**: `VOID, COLLAPSE, HARMONY, BREATH, RESET` (codes 0, 4, 7, 8, 9). All five are σ-fixed or σ³-fixed.

**The four-core** `{V, H, Br, R} = {0, 7, 8, 9}` uses universally-stable names.

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

*7SiTe Public Sovereignty License v2.1 — see [`LICENSE`](LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026*
