r"""recover_from_transcripts.py -- replay lost Write/Edit operations from
Claude Code session transcripts to restore the deleted working copy's
file artifacts.

The 2026-05-27/30 session's 24 commits were lost when the local working
copy was deleted before pushing. But every Write and Edit tool call --
with full file contents -- is logged in the session transcript and its
subagent transcripts:

  C:\Users\brayd\.claude\projects\C--Users-brayd-OneDrive-Desktop-CK-FINAL-DEPLOYED\
    4d3410e6-aff7-445d-aa8c-10c94bea4cc0.jsonl          (main, 263 MB)
    4d3410e6-aff7-445d-aa8c-10c94bea4cc0/subagents/agent-*.jsonl

This script:
  1. Streams every transcript line, extracting tool_use blocks with
     name in {Write, Edit} whose input.file_path targets the
     trinity-infinity-geometry tree.
  2. Filters to ops at/after the renumbering cutoff (the Write of
     renumber_all_v2.py) so pre-renumber artifacts (already on GitHub
     at a24f44f) are not duplicated at stale paths.
  3. Replays chronologically: Write -> write file; Edit -> exact
     old_string -> new_string replacement (honoring replace_all).
  4. Logs every op + outcome; failures collected for manual follow-up.

Usage:
  python recover_from_transcripts.py            # dry run (inventory)
  python recover_from_transcripts.py --apply    # replay onto the repo
"""
import io
import json
import os
import sys

TRANSCRIPT_DIR = (r"C:\Users\brayd\.claude\projects"
                  r"\C--Users-brayd-OneDrive-Desktop-CK-FINAL-DEPLOYED")
MAIN = os.path.join(TRANSCRIPT_DIR, "4d3410e6-aff7-445d-aa8c-10c94bea4cc0.jsonl")
SUBDIR = os.path.join(TRANSCRIPT_DIR, "4d3410e6-aff7-445d-aa8c-10c94bea4cc0",
                      "subagents")

REPO_MARKER = "trinity-infinity-geometry"
REPO_ROOT = r"C:\Users\brayd\OneDrive\Desktop\trinity-infinity-geometry"
CUTOFF_BASENAME = "renumber_all_v2.py"   # first Write of this = cutoff


def iter_ops(path):
    """Yield (timestamp, toolname, input) from one .jsonl transcript."""
    with io.open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            if '"tool_use"' not in line or REPO_MARKER not in line:
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            ts = obj.get("timestamp") or ""
            msg = obj.get("message") or {}
            content = msg.get("content") or []
            if not isinstance(content, list):
                continue
            for block in content:
                if not isinstance(block, dict):
                    continue
                if block.get("type") != "tool_use":
                    continue
                name = block.get("name")
                if name not in ("Write", "Edit"):
                    continue
                inp = block.get("input") or {}
                fp = inp.get("file_path", "")
                if REPO_MARKER not in fp:
                    continue
                yield (ts, name, inp)


def collect_all():
    ops = []
    files = [MAIN]
    if os.path.isdir(SUBDIR):
        files += [os.path.join(SUBDIR, fn) for fn in sorted(os.listdir(SUBDIR))
                  if fn.endswith(".jsonl")]
    print(f"Scanning {len(files)} transcript files...")
    for p in files:
        n_before = len(ops)
        for op in iter_ops(p):
            ops.append(op)
        n = len(ops) - n_before
        if n:
            print(f"  {os.path.basename(p)}: {n} ops")
    ops.sort(key=lambda t: t[0])
    return ops


def normalize_path(fp):
    """Map any historical absolute path onto the current repo root."""
    fp = fp.replace("/", "\\")
    idx = fp.lower().find(REPO_MARKER)
    if idx == -1:
        return None
    rel = fp[idx + len(REPO_MARKER):].lstrip("\\")
    if rel.startswith("tmp_renumber"):
        return None
    return os.path.join(REPO_ROOT, rel)


def main():
    apply = "--apply" in sys.argv
    ops = collect_all()
    print(f"\nTotal trinity ops found: {len(ops)}")

    # cutoff = first Write of renumber_all_v2.py
    cutoff = None
    for ts, name, inp in ops:
        if name == "Write" and inp.get("file_path", "").endswith(CUTOFF_BASENAME):
            cutoff = ts
            break
    if cutoff is None:
        print("WARNING: cutoff marker not found; replaying ALL ops")
        cutoff = ""
    else:
        print(f"Cutoff timestamp (first {CUTOFF_BASENAME} Write): {cutoff}")

    before = next((a.split("=", 1)[1] for a in sys.argv
                   if a.startswith("--before=")), None)
    after = next((a.split("=", 1)[1] for a in sys.argv
                  if a.startswith("--after=")), None)
    replay = [(ts, name, inp) for ts, name, inp in ops
              if ts >= cutoff
              and (before is None or ts < before)
              and (after is None or ts >= after)]
    print(f"Ops at/after cutoff: {len(replay)}")

    writes = sum(1 for _, n, _ in replay if n == "Write")
    edits = len(replay) - writes
    print(f"  Write: {writes}   Edit: {edits}\n")

    results = {"write_ok": 0, "edit_ok": 0, "edit_fail": [],
               "skipped": 0, "write_paths": set()}

    for ts, name, inp in replay:
        target = normalize_path(inp.get("file_path", ""))
        if target is None:
            results["skipped"] += 1
            continue
        rel = os.path.relpath(target, REPO_ROOT)
        if name == "Write":
            content = inp.get("content", "")
            if apply:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with io.open(target, "w", encoding="utf-8", newline="\n") as f:
                    f.write(content)
            results["write_ok"] += 1
            results["write_paths"].add(rel)
        else:  # Edit
            old = inp.get("old_string", "")
            new = inp.get("new_string", "")
            rall = inp.get("replace_all", False)
            if not apply:
                results["edit_ok"] += 1
                continue
            try:
                with io.open(target, "r", encoding="utf-8") as f:
                    s = f.read()
            except OSError:
                results["edit_fail"].append((ts, rel, "missing file"))
                continue
            if old not in s:
                # Tolerate already-applied edits (idempotent replay)
                if new and new in s:
                    results["edit_ok"] += 1
                else:
                    results["edit_fail"].append((ts, rel, "old_string not found"))
                continue
            s2 = s.replace(old, new) if rall else s.replace(old, new, 1)
            with io.open(target, "w", encoding="utf-8", newline="\n") as f:
                f.write(s2)
            results["edit_ok"] += 1

    print("=" * 64)
    print(f"Write replayed : {results['write_ok']}  "
          f"({len(results['write_paths'])} unique paths)")
    print(f"Edit  replayed : {results['edit_ok']}")
    print(f"Edit  failed   : {len(results['edit_fail'])}")
    print(f"Skipped (tmp/unmappable): {results['skipped']}")
    print(f"Mode: {'APPLIED' if apply else 'DRY RUN'}")

    if results["edit_fail"]:
        print("\nFailed edits (need manual follow-up):")
        for ts, rel, why in results["edit_fail"][:60]:
            print(f"  [{ts[:19]}] {rel}: {why}")

    # write a manifest of recovered paths
    if apply:
        man = os.path.join(REPO_ROOT, "05_papers", "_staging",
                           "RECOVERY_MANIFEST.txt")
        with io.open(man, "w", encoding="utf-8", newline="\n") as f:
            f.write("# Files restored from session transcripts 2026-06-10\n")
            for p in sorted(results["write_paths"]):
                f.write(p + "\n")
            f.write(f"\n# Edit failures: {len(results['edit_fail'])}\n")
            for ts, rel, why in results["edit_fail"]:
                f.write(f"# FAIL {rel}: {why}\n")
        print(f"\nManifest: {man}")


if __name__ == "__main__":
    main()
