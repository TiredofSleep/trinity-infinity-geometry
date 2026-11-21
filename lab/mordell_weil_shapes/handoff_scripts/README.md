# The handoff's scripts (20 November 2026)

These scripts computed every number in the eight `../registered/REGISTERED_2026-11-20_*.md` files. They were written and
run in the claude.ai session of 20 November, with PARI 2.19 through `cypari2`. They are copied here without change, as
evidence. They were not run in this repository: `cypari2` has no Windows build.

This repository's own reproduction, written from the definitions in the registered files, is in the folder above:
[`../mw_shapes.py`](../mw_shapes.py), [`../run_all.py`](../run_all.py) and [`../analyse.py`](../analyse.py). Its log,
[`../analyse.log`](../analyse.log), prints each recomputed number beside the handoff's.

`fetch_data.sh` rebuilds the data layout these scripts expect, from Cremona's `ecdata` repository on GitHub.
