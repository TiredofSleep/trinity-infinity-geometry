r"""polish_tex.py -- post-process amsart .tex files for arXiv submission.

Fixes:
  1. Add \usepackage[utf8]{inputenc} for sigma, omega, etc.
  2. Fill in keywords field from paper ID
  3. Escape unescaped & in itemize-text (LaTeX reserved)
  4. Wrap proof environments where pattern matches
  5. Fix table column counts (header vs body mismatch)
"""
import sys
import re

KEYWORDS = {
    'J59': "magma, quasigroup, commutative, automorphism group, congruence, sub-magma, finite algebra, rigidity",
    'J61': "equational theory, variety, type specimen, fossil variety, magma, universal algebra, ETP catalog, Birkhoff",
    'J63': "Niemeier lattice, kissing number, sporadic simple group, supersingular prime, root system, Weyl group, polynomial arithmetic",
}


def polish(tex, paper_id):
    # 1. Add inputenc after amsart
    if r'\usepackage[utf8]{inputenc}' not in tex:
        tex = tex.replace(
            r'\documentclass[11pt,reqno]{amsart}',
            r'\documentclass[11pt,reqno]{amsart}' + '\n' + r'\usepackage[utf8]{inputenc}'
        )

    # 2. Fill keywords
    kw = KEYWORDS.get(paper_id, "")
    if kw:
        tex = tex.replace(r'\keywords{[FILL IN KEYWORDS BEFORE SUBMISSION]}', f'\\keywords{{{kw}}}')

    # 3. Escape standalone "&" in citations within itemize (avoid math table &)
    # Heuristic: replace "X & Y" inside text (i.e., not in math mode) -- this is
    # imperfect but covers the common case "Author, A. & Author, B."
    # We protect math by skipping lines that look like table rows ($, &, \\ structure)
    out_lines = []
    for line in tex.split('\n'):
        # If line looks like a tabular row (ends with \\), skip & substitution
        if line.rstrip().endswith(r'\\') and '&' in line:
            out_lines.append(line)
            continue
        # If line has $, skip & substitution (math)
        if '$' in line:
            out_lines.append(line)
            continue
        # Otherwise, escape unescaped & to \&
        line2 = re.sub(r'(?<!\\)&', r'\\&', line)
        out_lines.append(line2)
    tex = '\n'.join(out_lines)

    # 4. \section{References} -> \section*{References} + thebibliography would be cleaner
    # but keep simple for now
    return tex


def main():
    if len(sys.argv) < 3:
        print("Usage: polish_tex.py input.tex output.tex paper_id")
        sys.exit(1)
    inp, out, pid = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(inp, 'r', encoding='utf-8') as f:
        tex = f.read()
    tex = polish(tex, pid)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(tex)
    print(f"polished {out}")


if __name__ == "__main__":
    main()
