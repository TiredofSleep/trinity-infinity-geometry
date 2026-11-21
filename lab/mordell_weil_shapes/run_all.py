"""run_all.py -- drive mw_shapes.py over Cremona's allgens tables, then merge the results.

  python -I run_all.py DATA_DIR OUT_DIR [W]

Reads every file named allgens.NNNNN-NNNNN below DATA_DIR, runs one mw_shapes.py process per table, at most W at a time
(default 4) and at below-normal priority, and writes OUT_DIR/parts/*.json and the merged OUT_DIR/all_rows.json (one
row per optimal curve of rank 2 or 3).
"""
import glob
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
BELOW_NORMAL = 0x00004000


def main(data_dir, out_dir, workers=4):
    files = sorted(f for f in glob.glob(os.path.join(data_dir, '**', 'allgens.*'), recursive=True)
                   if re.search(r'allgens\.\d+-\d+$', f))
    os.makedirs(os.path.join(out_dir, 'parts'), exist_ok=True)
    jobs = [(f, os.path.join(out_dir, 'parts', os.path.basename(f) + '.json')) for f in files]
    running, t0 = [], time.time()
    while jobs or running:
        while jobs and len(running) < workers:
            f, o = jobs.pop(0)
            running.append(subprocess.Popen([sys.executable, '-I', os.path.join(HERE, 'mw_shapes.py'), o, f],
                                            creationflags=BELOW_NORMAL if os.name == 'nt' else 0))
        time.sleep(1)
        running = [p for p in running if p.poll() is None]
    rows, bad = [], []
    for _, o in sorted((f, os.path.join(out_dir, 'parts', os.path.basename(f) + '.json')) for f in files):
        d = json.load(open(o))
        rows += d['rows']
        bad += d['bad']
    json.dump(rows, open(os.path.join(out_dir, 'all_rows.json'), 'w'))
    print(f"all {len(files)} tables done in {time.time() - t0:.0f} s: {len(rows)} curves "
          f"({sum(r['r'] == 2 for r in rows)} of rank 2, {sum(r['r'] == 3 for r in rows)} of rank 3), {len(bad)} failures")


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 4)
