"""md_to_amsart.py -- convert J-series manuscript.md to amsart .tex skeleton.

Reads a manuscript.md formatted in the J-series house style and produces an
amsart .tex file suitable for arXiv submission (after a manual polish pass).

Conversion rules:
  Headers:        # / ## / ### -> \title{} / \section{} / \subsection{}
  Inline emph:    **X** -> \textbf{X}, *X* -> \textit{X}
  Math:           $...$ and $$...$$ pass through unchanged (already LaTeX)
  Bullets:        - X -> itemize/item
  Code fences:    ``` -> verbatim
  Pipe tables:    | a | b | -> tabular (booktabs style)
  Theorem-style:  **Theorem N.** -> noindent paragraph (no theorem env wrapping)
                  Keeps the load-bearing bold prefix; manual env conversion later.

Usage:
  python md_to_amsart.py input.md output.tex
"""
import sys
import re


PREAMBLE = r"""\documentclass[11pt,reqno]{amsart}
\usepackage{amsmath, amssymb, amsthm, mathtools}
\usepackage[margin=1in]{geometry}
\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue]{hyperref}
\usepackage{microtype}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{listings}

\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}

\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{conjecture}[theorem]{Conjecture}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}

% Common abbreviations
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Aut}{\mathrm{Aut}}
\newcommand{\End}{\mathrm{End}}
"""


def emit_header(title, authors, address, email, address2, email2, venue, msc):
    return f"""\\title[{title[:40]}]{{{title}}}

\\author{{{authors[0]}}}
\\address{{{address}}}
\\email{{{email}}}

\\author{{{authors[1]}}}
\\address{{{address2}}}
\\email{{{email2}}}

\\subjclass[2020]{{{msc}}}
\\keywords{{[FILL IN KEYWORDS BEFORE SUBMISSION]}}

\\begin{{document}}

\\maketitle

% Target venue: {venue}
"""


def convert_inline(line):
    """Inline conversions: emph, bold, code, em-dashes, etc."""
    # Code spans `x` -> \texttt{x}
    line = re.sub(r'`([^`\n]+)`', r'\\texttt{\1}', line)
    # Bold **x** -> \textbf{x} (must come before italic *x*)
    line = re.sub(r'\*\*([^*\n]+)\*\*', r'\\textbf{\1}', line)
    # Italic *x* -> \textit{x} (avoid matching $math$ via heuristic: no $ in span)
    line = re.sub(r'(?<!\*)\*([^*\n$]+)\*(?!\*)', r'\\textit{\1}', line)
    # Em-dash safety
    line = line.replace('—', '---')
    # & in math is fine; in text it should be escaped
    # (skip for simplicity; tables handle this themselves)
    return line


def convert_table(lines, start):
    """Convert a pipe-style markdown table to tabular env. Returns (latex, next_i)."""
    # find table lines (start with |)
    end = start
    while end < len(lines) and lines[end].strip().startswith('|'):
        end += 1
    table_lines = [l.strip() for l in lines[start:end]]
    if len(table_lines) < 2:
        return None, start
    header_cells = [c.strip() for c in table_lines[0].strip('|').split('|')]
    n = len(header_cells)
    # second line is separator (--|--|--)
    body = table_lines[2:]
    body_rows = [[c.strip() for c in r.strip('|').split('|')] for r in body]

    align = 'l' * n  # default left-align; could parse ---: for right
    out = []
    out.append('\\begin{center}')
    out.append('\\begin{tabular}{' + align + '}')
    out.append('\\toprule')
    out.append(' & '.join(convert_inline(c) for c in header_cells) + ' \\\\')
    out.append('\\midrule')
    for row in body_rows:
        # pad if short
        while len(row) < n:
            row.append('')
        out.append(' & '.join(convert_inline(c) for c in row[:n]) + ' \\\\')
    out.append('\\bottomrule')
    out.append('\\end{tabular}')
    out.append('\\end{center}')
    return '\n'.join(out), end


def convert(md_text, header_info=None):
    """Top-level Markdown -> LaTeX conversion."""
    lines = md_text.split('\n')
    out = [PREAMBLE]
    if header_info:
        out.append(emit_header(**header_info))

    i = 0
    in_code = False
    code_buffer = []
    in_abstract = False
    abstract_buffer = []
    started_body = False
    in_itemize = False
    while i < len(lines):
        line = lines[i]
        # Code fence
        if line.strip().startswith('```'):
            if in_code:
                out.append('\\begin{verbatim}')
                out.extend(code_buffer)
                out.append('\\end{verbatim}')
                code_buffer = []
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_buffer.append(line)
            i += 1
            continue

        # Top-level h1 -> title (already in header)
        if line.startswith('# ') and not started_body:
            i += 1
            continue

        # Frontmatter (authors, venue, MSC) — skip until first ##
        if not started_body:
            if line.startswith('## '):
                started_body = True
            else:
                i += 1
                continue

        # Headers
        if line.startswith('### '):
            if in_itemize:
                out.append('\\end{itemize}')
                in_itemize = False
            title = line[4:].strip()
            # strip leading §N.M
            title_clean = re.sub(r'^§[\d.]+\s*', '', title)
            out.append(f'\\subsection{{{convert_inline(title_clean)}}}')
            i += 1
            continue
        if line.startswith('## '):
            if in_itemize:
                out.append('\\end{itemize}')
                in_itemize = False
            title = line[3:].strip()
            title_clean = re.sub(r'^§\d+\s*', '', title)
            if title_clean.lower() in ('abstract',):
                in_abstract = True
                out.append('\\begin{abstract}')
                i += 1
                continue
            elif in_abstract:
                # Close previous abstract
                out.append('\\end{abstract}')
                in_abstract = False
            out.append(f'\\section{{{convert_inline(title_clean)}}}')
            i += 1
            continue

        # Tables
        if line.strip().startswith('|') and i + 1 < len(lines) and lines[i+1].strip().startswith('|'):
            tab, next_i = convert_table(lines, i)
            if tab:
                if in_itemize:
                    out.append('\\end{itemize}')
                    in_itemize = False
                out.append(tab)
                i = next_i
                continue

        # Itemize
        if line.strip().startswith('- '):
            if not in_itemize:
                out.append('\\begin{itemize}')
                in_itemize = True
            content = line.strip()[2:]
            out.append(f'\\item {convert_inline(content)}')
            i += 1
            continue
        elif in_itemize and line.strip() == '':
            # blank line ends itemize
            out.append('\\end{itemize}')
            in_itemize = False
            out.append('')
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ('---', '----', '_____'):
            out.append('\\medskip\\hrule\\medskip')
            i += 1
            continue

        # Normal paragraph
        if line.strip() == '':
            out.append('')
        else:
            out.append(convert_inline(line))
        i += 1

    if in_itemize:
        out.append('\\end{itemize}')
    if in_abstract:
        out.append('\\end{abstract}')
    out.append('\\end{document}')
    return '\n'.join(out)


def main():
    if len(sys.argv) < 3:
        print("Usage: md_to_amsart.py input.md output.tex [paper_id]")
        sys.exit(1)
    inp, out = sys.argv[1], sys.argv[2]
    paper = sys.argv[3] if len(sys.argv) > 3 else 'generic'

    # Paper-specific header information
    HEADERS = {
        'J59': dict(
            title="Algebraic Rigidity of the sigma-Magma on Z/10Z: Simplicity, Trivial Automorphism Group, and Unique Sub-Magma",
            authors=["Brayden R.\\ Sanders", "M.\\ Gish"],
            address="7Site LLC, Hot Springs, Arkansas, USA",
            email="brayden@7site.co",
            address2="Independent Researcher, Hot Springs, Arkansas, USA",
            email2="monica.gish1992@gmail.com",
            venue="Semigroup Forum",
            msc="20N02, 08A05, 08A30, 20N05",
        ),
        'J61': dict(
            title="Type Specimens in the ETP-Restricted Variety Lattice: a Magma-by-Equational-Theory Taxonomy",
            authors=["Brayden R.\\ Sanders", "M.\\ Gish"],
            address="7Site LLC, Hot Springs, Arkansas, USA",
            email="brayden@7site.co",
            address2="Independent Researcher, Hot Springs, Arkansas, USA",
            email2="monica.gish1992@gmail.com",
            venue="Journal of Symbolic Computation",
            msc="08A05, 08B05, 20N02, 20N05, 68W30",
        ),
        'J63': dict(
            title="The Strata-Prime Fingerprint: Polynomial vs Factorial Invariants in Niemeier Lattices and Sporadic Simple Groups",
            authors=["Brayden R.\\ Sanders", "M.\\ Gish"],
            address="7Site LLC, Hot Springs, Arkansas, USA",
            email="brayden@7site.co",
            address2="Independent Researcher, Hot Springs, Arkansas, USA",
            email2="monica.gish1992@gmail.com",
            venue="Journal of Number Theory",
            msc="11H06, 11R52, 20D08, 17B22, 11N05, 20B25",
        ),
    }
    header_info = HEADERS.get(paper)

    with open(inp, 'r', encoding='utf-8') as f:
        md = f.read()
    tex = convert(md, header_info)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(tex)
    print(f"wrote {out} ({len(tex):,} bytes)")


if __name__ == "__main__":
    main()
