"""apply_tier_marks.py -- add Tier markers to each paper's README.

Adds a line `**Tier:** N (description)` immediately after the `**Status:**`
line in each paper README. Skip if the tier line already exists.

Run from the repo root or from anywhere; uses absolute paths via REPO_ROOT.
"""
import os, sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]  # 05_papers/_staging/.. = repo root no wait
# Actually: 05_papers/_staging/portfolio_review_2026-05-27/apply_tier_marks.py
# parents[0] = portfolio_review_2026-05-27
# parents[1] = _staging
# parents[2] = 05_papers
# parents[3] = trinity-infinity-geometry (repo root)
REPO_ROOT = Path(__file__).resolve().parents[3]
PAPERS = REPO_ROOT / "05_papers"

# Tier assignments:
TIER = {
    # TIER 1: ship-ready
    "combinatorics/J01": (1, "ship-ready (JCT-A, SUBMISSION-READY, 6/6 PASS)"),
    "combinatorics/J02": (1, "ship-ready (Algebraic Combinatorics, SUBMISSION-READY)"),
    "algebra/J13":      (1, "ship-ready (Acta Arithmetica, SUBMISSION-READY)"),
    "algebra/J15":      (1, "ship-ready (Communications in Algebra, SUBMISSION-READY)"),
    "algebra/J17":      (1, "ship-ready (LinAlgApps, SUBMISSION-READY)"),
    "algebra/J18":      (1, "ship-ready (Algebraic Combinatorics, SUBMISSION-READY)"),
    "algebra/J22":      (1, "ship-ready (JCT-A, SUBMISSION-READY)"),
    "algebra/J25":      (1, "ship-ready (Algebraic Combinatorics, READY, cover letter finalized)"),
    "algebra/J26":      (1, "ship-ready (Communications in Algebra, READY)"),
    "combinatorics/J27":(1, "ship-ready (HONEST NEGATIVE, important for credibility)"),
    "algebra/J31":      (1, "ship-ready (Journal of Algebra, READY)"),
    "interdisciplinary/J34": (1, "ship-ready (HONEST NEGATIVE on detector specificity, REVISED)"),
    "algebra/J35":      (1, "ship-ready (Journal of Algebra, SUBMISSION-READY -- corpus centerpiece)"),

    # TIER 2: drafts needing referee-rigor pass
    "number_theory/J03": (2, "draft (Integers; J03 absorbed J04, needs final consolidation pass)"),
    "algebra/J05":      (2, "draft (REVISED 2026-05-08; SFM framing applied)"),
    "algebra/J06":      (2, "draft (DRAFT-FINALIZED; rigor pass pending)"),
    "combinatorics/J07":(2, "draft (SAVE-PLAN APPLIED; restructured)"),
    "number_theory/J08":(2, "draft (REVISED; major referee fixes applied)"),
    "algebra/J09":      (2, "draft (REVISED; Path-B rewrite per fresh-eyes referee)"),
    "combinatorics/J10":(2, "draft (SAVE-PLAN APPLIED; coverage criteria restructured)"),
    "combinatorics/J12":(2, "draft (REVISED post fresh-eyes referee)"),
    "combinatorics/J19":(2, "draft (SAVE-PLAN APPLIED; Path-C role-quotient)"),
    "algebra/J20":      (2, "draft (defensive-exposition pass complete)"),
    "physics/J23":      (2, "draft (manuscript stable; Volume K cross-reference added)"),
    "algebra/J30":      (2, "draft (REWRITTEN per SAVE_PLAN; D2-D5 corollary diagnostic)"),
    "algebra/J32":      (2, "draft (REWRITE 2026-05-12; operadic D4 obstruction)"),
    "algebra/J37":      (2, "draft (RETARGETED to LAA; LinAlgApps target)"),
    "physics/J40":      (2, "draft (R1 revised; could submit to JMP standalone)"),
    "number_theory/J42":(2, "draft (with venue fallback flagged)"),
    "combinatorics/J52":(2, "draft (REWRITTEN per SAVE PLAN; pedagogical exposition)"),
    "interdisciplinary/J53": (2, "draft (REWRITTEN per SAVE PLAN; scope-narrowed to algebra)"),
    "combinatorics/J54":(2, "draft (foundation paper; SFM Q6 + FAMILY_STRUCTURE_v1 applied)"),
    "algebra/J58":      (2, "draft (verification PASS; awaiting referee-rigor pass)"),
    "algebra/J59":      (1, "ship-ready (Semigroup Forum; 4/4 PASS in ~3s; PROMOTED 2026-05-27)"),
    "algebra/J60":      (1, "ship-ready (Experimental Mathematics; 4/4 PASS in ~7s; PROMOTED 2026-05-27)"),
    "algebra/J61":      (1, "ship-ready (Journal of Symbolic Computation; 5/5 PASS in ~13s; PROMOTED 2026-05-27, **most novel**)"),
    "number_theory/J62_RH_short_note": (1, "ship-ready (Mathematical Intelligencer short note; 2 theorems + Conjecture Z.5; 5-line numpy verifier PASS; 2026-05-27)"),
    "algebra/J_qseries_merged": (1, "ship-ready (European J Combin; 5 theorems verified at machine precision incl. G_low=1.871644, G_high=9.389185; PROMOTED 2026-05-27)"),
    "algebra/J_Fp_merged":       (1, "ship-ready (Algebra Universalis; idempotent counts verified at 6 primes; chain-shell dets match exactly; PROMOTED 2026-05-27)"),

    # TIER 3: hold / retire / speculation
    "number_theory/J04": (3, "MERGED into J03 (formal tombstone)"),
    "physics/J36":      (3, "HOLD pending particle-physics collaborator OR reframe as observation"),
    "physics/J39":      (3, "HOLD pending NV-center experimentalist"),
    "physics/J45":      (3, "RETIRE candidate -- Tier-C structural rhyme without theorem"),
    "physics/J48":      (3, "RETIRE candidate -- duplicates J32 operadic obstruction"),
    "interdisciplinary/J49": (3, "HOLD pending terahertz microtubule experimentalist"),
    "interdisciplinary/J56_DRAFT": (3, "RETIRE candidate to 04_meta -- Tier-C atomic-substrate"),

    # MERGED (absorbed into mergers)
    "combinatorics/J21": (None, "MERGED 2026-05-27 into J_qseries_merged"),
    "algebra/J43":      (None, "MERGED 2026-05-27 into J_qseries_merged"),
    "algebra/J51":      (None, "MERGED 2026-05-27 into J_qseries_merged"),
    "algebra/J14":      (None, "MERGED 2026-05-27 into J_Fp_merged"),
    "algebra/J16":      (None, "MERGED 2026-05-27 into J_Fp_merged"),
}


def apply_tier(paper_path, tier, desc):
    """Insert a Tier line after the Status line in the paper's README."""
    readme = PAPERS / paper_path / "README.md"
    if not readme.exists():
        return f"SKIP {paper_path}: no README.md"
    content = readme.read_text(encoding="utf-8")
    if "**Tier:**" in content or "**Tier**:" in content:
        # Update existing tier line
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if line.startswith("**Tier:**") or line.startswith("**Tier**:"):
                if tier is None:
                    lines[i] = f"**Tier:** -- ({desc})"
                else:
                    lines[i] = f"**Tier:** {tier} ({desc})"
                break
        readme.write_text("\n".join(lines) + ("\n" if content.endswith("\n") else ""),
                          encoding="utf-8")
        return f"UPDATED {paper_path}: Tier {tier if tier else '--'} ({desc})"
    # Insert after Status line
    lines = content.splitlines()
    out = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and (line.startswith("**Status:**") or line.startswith("**Status**:")):
            if tier is None:
                out.append(f"**Tier:** -- ({desc})")
            else:
                out.append(f"**Tier:** {tier} ({desc})")
            inserted = True
    if not inserted:
        # Insert near the top instead (after title)
        for i, line in enumerate(out[:5]):
            if line.startswith("#"):
                if tier is None:
                    out.insert(i + 2, f"**Tier:** -- ({desc})")
                else:
                    out.insert(i + 2, f"**Tier:** {tier} ({desc})")
                inserted = True
                break
    readme.write_text("\n".join(out) + ("\n" if content.endswith("\n") else ""),
                      encoding="utf-8")
    return f"ADDED {paper_path}: Tier {tier if tier else '--'} ({desc})"


def main():
    results = []
    for paper_path, (tier, desc) in TIER.items():
        results.append(apply_tier(paper_path, tier, desc))
    for r in results:
        print(r)
    print(f"\nTotal papers tagged: {len(results)}")


if __name__ == "__main__":
    main()
