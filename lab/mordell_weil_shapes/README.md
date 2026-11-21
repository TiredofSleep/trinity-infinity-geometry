# Shapes of Mordell–Weil lattices

This folder holds Part F of the lens handoff of 20 November 2026: the shapes and packing densities of the rank-2
Mordell–Weil lattices of elliptic curves over ℚ. The author chose `lab/` as its place on 21 November 2026. The full
page follows in the next commit: the reproduction of the 20 November numbers, the prior art (Watkins 2006, §6.4) and
the ledger.

- [`registered/`](registered/) holds the eight rounds registered and scored on 20 November, copied without change
  from the handoff. It also holds the round registered on 21 November, "every loop fails a little".
- [`every_loop.py`](every_loop.py) is that round's script, committed before its run. Its self-test, on synthetic
  lattices and on one pair of curves outside Cremona's tables, is in
  [`every_loop_selftest.log`](every_loop_selftest.log).
