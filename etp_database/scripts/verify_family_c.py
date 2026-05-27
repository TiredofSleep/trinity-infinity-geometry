"""verify_family_c.py — verify that Family C = implication-closure of eq 43.

This is the core citable claim of the database. We read ETP's edge-list CSV
(filtered to proved-true edges), compute the transitive closure of {43},
and confirm the result equals the 14-element Family C set.

ETP's edge list format (CSV):
    Source,Target,Outcome
    Equation43,Equation4283,implicit_proof_true
    ...

Outcome values include:
    implicit_proof_true / explicit_proof_true   (proved implications)
    implicit_proof_false / explicit_proof_false / explicit_conjecture_false (non-implications)
    explicit_conjecture_true   (conjectured but not yet proved)

We use only the *true* outcomes. The default edge-list path is the unpacked
2024-11-10-edge_list.csv from ETP's data/ directory.

Usage:
    python verify_family_c.py [--edge-list /path/to/edge_list.csv] [--seed 43]
"""
import argparse
import csv
import os
import re
import sys
from collections import defaultdict

EXPECTED_FAMILY_C = frozenset({1, 43, 4283, 4358, 4380, 4398, 4405, 4435,
                                4442, 4482, 4531, 4544, 4635, 4677})

DEFAULT_EDGE_LIST = os.environ.get("ETP_EDGE_LIST", "/tmp/edge_list.csv")
TRUE_OUTCOMES = {"implicit_proof_true", "explicit_proof_true"}
EQ_RE = re.compile(r"Equation(\d+)")


def load_true_implications(path):
    """Return adjacency dict {premise_id: set of consequence_ids}."""
    adj = defaultdict(set)
    with open(path, "r", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        src_idx = header.index("Source")
        tgt_idx = header.index("Target")
        out_idx = header.index("Outcome")
        for row in reader:
            outcome = row[out_idx]
            if outcome not in TRUE_OUTCOMES:
                continue
            ms = EQ_RE.fullmatch(row[src_idx])
            mt = EQ_RE.fullmatch(row[tgt_idx])
            if ms and mt:
                adj[int(ms.group(1))].add(int(mt.group(1)))
    return adj


def closure(seeds, adj):
    out = set(seeds)
    frontier = set(seeds)
    while frontier:
        nxt = set()
        for p in frontier:
            for q in adj.get(p, ()):
                if q not in out:
                    nxt.add(q)
        out |= nxt
        frontier = nxt
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--edge-list", default=DEFAULT_EDGE_LIST)
    ap.add_argument("--seed", type=int, default=43)
    args = ap.parse_args()

    if not os.path.exists(args.edge_list):
        print(f"ERROR: edge list not found at {args.edge_list}")
        print("Unpack ETP's data/2024-11-10-edge_list.csv.zip, or set ETP_EDGE_LIST.")
        sys.exit(2)

    print(f"Loading ETP edge list from {args.edge_list} ...")
    print(f"  (this may take 30-60s; file is ~1GB)")
    adj = load_true_implications(args.edge_list)
    n_edges = sum(len(v) for v in adj.values())
    print(f"  {len(adj)} premise nodes, {n_edges} true implication edges.")

    print(f"\nComputing transitive closure of seed = {{{args.seed}}} ...")
    cl = closure({args.seed}, adj)
    print(f"  closure size: {len(cl)}")
    print(f"  closure:      {sorted(cl)}")

    print(f"\nExpected Family C: {sorted(EXPECTED_FAMILY_C)}")
    print(f"Expected size:     {len(EXPECTED_FAMILY_C)}")

    if cl == EXPECTED_FAMILY_C:
        print("\n  PASS: implication-closure of {43} equals Family C exactly.")
        sys.exit(0)
    else:
        missing = EXPECTED_FAMILY_C - cl
        extra = cl - EXPECTED_FAMILY_C
        print("\n  FAIL: implication-closure of {43} differs from Family C.")
        if missing:
            print(f"    missing (in Family C, not in closure): {sorted(missing)}")
        if extra:
            print(f"    extra   (in closure, not in Family C): {sorted(extra)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
