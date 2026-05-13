"""
_rewrite_formula_links.py — surgical link rewrite for FORMULAS_AND_TABLES.md.

The FORMULAS file references many `Gen12/...`, `Gen13/...`, `Atlas/...`,
and `papers/...` paths from the original working repo. Those paths
DON'T EXIST in the public trinity-infinity-geometry repo, which uses
the new `05_papers/<category>/J##/` layout.

This script applies the mapping table below, in-place. It also:
  - Wraps any path that DOES exist in the new layout as a [text](path)
    markdown link, so the click actually works.
  - For paths with no direct public equivalent, rewrites them to point
    at the canonical working-repo GitHub URL on the tig-synthesis
    branch so the click still resolves to the real file.
  - Leaves WP## doc-name backtick refs in place (they're contextual,
    not navigation targets).

Run once after editing FORMULAS_AND_TABLES.md. Idempotent.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).parent.resolve()
TARGET = HERE / "FORMULAS_AND_TABLES.md"

# Public-repo paths that exist for sure (relative to repo root, where
# this script's parent's parent lives).
REPO_ROOT = HERE.parent

# GitHub URL prefix for paths that don't have a public-repo equivalent.
# The working repo (with Gen12/Gen13/Atlas/) lives at:
WORKING_REPO_GH = (
    "https://github.com/TiredofSleep/ck/blob/tig-synthesis"
)


# ─── Mapping table ──────────────────────────────────────────────────────
# old_path_pattern -> new_path_or_github_url
#
# Order matters: more specific (longer) keys first so a sed pass doesn't
# clobber a sub-string. We use literal string replacement, NOT regex.

MAP_TO_NEW_REPO = {
    # First-G Law proof
    "Gen12/targets/clay/papers/sprint35_first_g_event_2026_04_19/proof_first_g_event.py":
        "../05_papers/number_theory/J03/manuscript/proof_first_g_event.py",
    # Crossing Lemma
    "Gen12/targets/clay/papers/sprint10_flatness_2026_04_06/CROSSING_LEMMA.md":
        "../05_papers/algebra/J06/manuscript/WP57_CROSSING_LEMMA.md",
    # TSML tower theorem spine (J05 has the canonical TSML manuscript)
    "Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/THEOREM_SPINE.md":
        "../05_papers/algebra/J05/manuscript/manuscript.tex",
    # Bare sprint17 directory pointer (used in the §19 sprint trail table)
    "Gen12/targets/clay/papers/sprint17_tsml_tower_2026_04_17/":
        "../05_papers/algebra/J05/",
    # WP51 Flatness — no canonical doc in 05_papers; the J01 manuscript
    # carries the proof. Best target: J01 manuscript.
    "Gen12/targets/journal_attempts/05_journal_pure_applied_algebra/WP51_FLATNESS_THEOREM.md":
        "../05_papers/combinatorics/J01/manuscript/manuscript.tex",
    # Sigma rate theorem
    "Gen12/targets/journal_attempts/08_sigma_rate_combinatorics/WP101_SIGMA_RATE_THEOREM.md":
        "../05_papers/combinatorics/J01/manuscript/WP101_SIGMA_RATE_THEOREM.md",
    # NS separability bridge
    "Gen12/targets/journal_attempts/09_jmp_bb_bridge/WP91_NS_SEPARABILITY_BRIDGE.md":
        "../05_papers/algebra/J32/manuscript/WP91_NS_SEPARABILITY_BRIDGE.md",
    # BHML 28-cell proof
    "Gen12/targets/journal_attempts/02_experimental_mathematics/proof_d16_bhml_28_cells.py":
        "../05_papers/algebra/J05/manuscript/proof_d16_bhml_28_cells.py",
    # Wobble check
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/wobble_check.py":
        "../05_papers/algebra/J37/manuscript/verification/wobble_check.py",
    # Alpha-uniqueness
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/alpha_uniqueness/alpha_uniqueness_general.py":
        "../05_papers/algebra/J25/manuscript/verification/f3_galois_alpha_uniqueness.py",
    # Operad obstruction
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/operad/":
        "../05_papers/physics/J48/",
    # Corridor closure
    "Gen12/targets/clay/papers/sprint25_corridor_closure_proof_2026_04_17/impl/prove_corridor_closure.py":
        "../05_papers/combinatorics/J19/manuscript/verify_J19.py",
    "Gen12/targets/clay/papers/sprint25_corridor_closure_proof_2026_04_17/README.md":
        "../05_papers/combinatorics/J19/",
}

# Paths with no direct public equivalent -> point at working-repo GH URL
MAP_TO_GITHUB = {
    "Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/desi_xi_mcmc.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/desi_xi_mcmc.py",
    "Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint14_prism_xi_2026_04_10/",
    "Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/impl/generator/generate_nscg.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/impl/generator/generate_nscg.py",
    "Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/impl/discovery_fitter.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/impl/discovery_fitter.py",
    "Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/impl/nstress.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/impl/nstress.py",
    "Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/impl/ari_scaling.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/impl/ari_scaling.py",
    "Gen12/targets/clay/papers/sprint16_":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint16_",
    # Shorthand .../sprintN_*/ references in the §19 sprint trail table.
    # All point at the working repo since these are research-stage sprints
    # without direct 05_papers/J## equivalents.
    ".../sprint18_b1_nscg_benchmark_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint18_b1_nscg_benchmark_2026_04_17/",
    ".../sprint19_b2_wrg_benchmark_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint19_b2_wrg_benchmark_2026_04_17/",
    ".../sprint20_b3_lbtp_benchmark_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint20_b3_lbtp_benchmark_2026_04_17/",
    ".../sprint21_structural_discovery_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint21_structural_discovery_2026_04_17/",
    ".../sprint22_collapse_point_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint22_collapse_point_2026_04_17/",
    ".../sprint23_curve_recovery_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint23_curve_recovery_2026_04_17/",
    ".../sprint24_collapse_synthesis_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint24_collapse_synthesis_2026_04_17/",
    ".../sprint25_corridor_closure_proof_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint25_corridor_closure_proof_2026_04_17/",
    ".../sprint26_ari_scaling_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint26_ari_scaling_2026_04_17/",
    ".../sprint27_b3_spec_revision_memo_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint27_b3_spec_revision_memo_2026_04_17/",
    ".../sprint28_curve_recovery_prereg_2026_04_17/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint28_curve_recovery_prereg_2026_04_17/",
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/",
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/SIGMA_OUTER_FINDING.md":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/SIGMA_OUTER_FINDING.md",
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/first_g_crossing_tie.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/first_g_crossing_tie.py",
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/verify_truth.py",
    "Gen12/.../sprint_unmistakable_truth_2026_04_25/scripts/xi_cosmology_tie.py":
        f"{WORKING_REPO_GH}/Gen12/targets/clay/papers/sprint_unmistakable_truth_2026_04_25/scripts/xi_cosmology_tie.py",
    "Gen12/targets/ck_desktop/bhml_eigenvalue_analysis.py":
        f"{WORKING_REPO_GH}/Gen12/targets/ck_desktop/bhml_eigenvalue_analysis.py",
    # Gen13/foundations -> working repo (the source of truth lives there)
    "Gen13/targets/foundations/cl.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/cl.py",
    "Gen13/targets/foundations/cl_std.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/cl_std.py",
    "Gen13/targets/foundations/invariants.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/invariants.py",
    "Gen13/targets/foundations/lenses.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/lenses.py",
    "Gen13/targets/foundations/bhml_variants.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/bhml_variants.py",
    "Gen13/targets/foundations/tables/harmony_ladder.py":
        f"{WORKING_REPO_GH}/Gen13/targets/foundations/tables/harmony_ladder.py",
    # Atlas -> working repo
    "Atlas/META_PLAN_2026-05-06/":
        f"{WORKING_REPO_GH}/Atlas/META_PLAN_2026-05-06/",
    "Atlas/META_PLAN_2026-05-06/RELEASE_PLAN_SEPT11.md":
        f"{WORKING_REPO_GH}/Atlas/META_PLAN_2026-05-06/RELEASE_PLAN_SEPT11.md",
    "Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md":
        f"{WORKING_REPO_GH}/Atlas/META_PLAN_2026-05-06/TSML_RECONCILIATION.md",
    "Atlas/META_PLAN_2026-05-10/":
        f"{WORKING_REPO_GH}/Atlas/META_PLAN_2026-05-10/",
    "Atlas/PLAN_RIGOROUS_EXECUTION_2026_04_21.md":
        f"{WORKING_REPO_GH}/Atlas/PLAN_RIGOROUS_EXECUTION_2026_04_21.md",
    "Atlas/applications_pass_2026_04_27/SPECULATIONS_FIELD9_DIRAC_INSIDE.md":
        f"{WORKING_REPO_GH}/Atlas/applications_pass_2026_04_27/SPECULATIONS_FIELD9_DIRAC_INSIDE.md",
    "Atlas/applications_pass_2026_04_27/WP104_DEEP_AUDIT_2026_04_27.md":
        f"{WORKING_REPO_GH}/Atlas/applications_pass_2026_04_27/WP104_DEEP_AUDIT_2026_04_27.md",
    "Atlas/applications_pass_2026_04_27/code/item1c_corrected_bound_v2.py":
        f"{WORKING_REPO_GH}/Atlas/applications_pass_2026_04_27/code/item1c_corrected_bound_v2.py",
    "Atlas/applications_pass_2026_04_27/code/item5_6_frw.py":
        f"{WORKING_REPO_GH}/Atlas/applications_pass_2026_04_27/code/item5_6_frw.py",
    "Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py":
        f"{WORKING_REPO_GH}/Atlas/applications_pass_2026_04_27/code/markov_binary_cl.py",
}

# Combined map; longer keys first for safe sed-style replacement
COMBINED = {**MAP_TO_NEW_REPO, **MAP_TO_GITHUB}


def rewrite(text: str) -> tuple[str, int]:
    """Return (new_text, n_replacements).

    Single-pass regex with longest-key-first alternation. Each match
    region is replaced atomically; no key can match within an already-
    rewritten region (which is what caused the double-prefix bug in the
    cascading two-pass version).
    """
    # Sort longest keys first so multi-segment paths take precedence over
    # their own prefixes.
    keys = sorted(COMBINED.keys(), key=len, reverse=True)
    # Build a single alternation pattern; escape each key literally.
    pattern = re.compile("|".join(re.escape(k) for k in keys))
    counter = {"n": 0}

    def _sub(m: re.Match) -> str:
        counter["n"] += 1
        return COMBINED[m.group(0)]

    new_text = pattern.sub(_sub, text)
    return new_text, counter["n"]


# ─── Pass 2: wrap backticked URLs / relative paths as clickable links ───

# Matches `<url-or-relative-path>` (path inside single backticks).
# The URL must start with http(s) or ../ (relative); only those are
# converted to clickable [text](url) markdown. Other backticked code
# remains unchanged.
_LINK_BACKTICK_RE = re.compile(
    r"`(https?://[^`\s]+|\.\./[^`\s]+)`"
)


def _display_text(url: str) -> str:
    """Derive a short display text for the [text](url) form."""
    # For GitHub URLs, show the trailing path
    if url.startswith("https://github.com/"):
        # Show the part after blob/<branch>/
        parts = url.split("/blob/", 1)
        if len(parts) == 2:
            after_branch = parts[1].split("/", 1)[1] if "/" in parts[1] else parts[1]
            return after_branch
        return url
    # Other absolute URL: show host + last path segment
    if url.startswith("http"):
        return url
    # Relative path: strip leading ../
    return url.lstrip("./") if url.startswith("../") else url


def wrap_clickable(text: str) -> tuple[str, int]:
    """Convert `<url>` -> [<display>](<url>) so GitHub renders clickable."""
    counter = {"n": 0}

    def _sub(m: re.Match) -> str:
        url = m.group(1)
        # Skip URLs that are already inside a [text](url) link form
        # (re won't see those because of the surrounding parentheses;
        # they'd be matched only if naked `...` — which is what we want).
        counter["n"] += 1
        return f"[{_display_text(url)}]({url})"

    new_text = _LINK_BACKTICK_RE.sub(_sub, text)
    return new_text, counter["n"]


def main():
    src = TARGET.read_text(encoding="utf-8")
    new, n1 = rewrite(src)
    new, n2 = wrap_clickable(new)
    if new == src:
        print("FORMULAS_AND_TABLES.md: no changes needed (already rewritten?)")
        return 0
    TARGET.write_text(new, encoding="utf-8")
    print(f"Rewrote {n1} path references + wrapped {n2} backtick-URLs "
          f"as clickable links in {TARGET}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
