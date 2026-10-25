"""Validate the independent catalog rebuild against (a) laws whose ETP numbers are
well known, (b) equation texts that the archive copied out of the real ETP catalog
(read_equations_map of an ETP clone), (c) profile counts the archive computed with ETP tools."""
import json, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import etpcore as E

if len(sys.argv) < 2:
    sys.exit("usage: python check_catalog.py <archive>/etp_database   (<archive>: a checkout of the tag archive-2026-09-24; see ../README.md)")
ARCH = sys.argv[1]
t0 = time.time()
print("catalog size", E.NLAWS)
assert E.NLAWS == 4694

def norm(txt):
    txt = txt.replace("\u25c7", "*").replace("\u22c4", "*").replace("\u00b7", "*").replace("\u2218", "*")
    return " ".join(txt.replace("*", " * ").replace("(", "( ").replace(")", " )").split())

def mine(i):
    return norm(E.show(i))

def same_law(i, txt):
    # compare up to side swap (ETP lists each law in one orientation)
    a = norm(txt)
    if a == mine(i):
        return True
    l, r = a.split(" = ")
    return norm(r + " = " + l) == mine(i) or False

known = {1: "x = x", 2: "x = y", 3: "x = x * x", 4: "x = x * y", 5: "x = y * x",
         7: "x = y * z", 8: "x = x * (x * x)", 14: "x = y * (x * y)", 16: "x = y * (y * x)",
         23: "x = (x * x) * x", 38: "x * x = x * y", 40: "x * x = y * y", 42: "x * y = x * z",
         43: "x * y = y * x", 46: "x * y = z * w", 168: "x = (y * x) * (x * z)",
         4512: "x * (y * z) = (x * y) * z"}
bad = [i for i, s in known.items() if not same_law(i, s)]
print("well-known anchors checked:", len(known), "mismatches:", bad)

# texts that the archive took from the ETP's own equation list
fc = json.load(open(os.path.join(ARCH, "data", "family_c.json"), encoding="utf-8"))
sq = json.load(open(os.path.join(ARCH, "verdicts", "squag_variety_diff.json"), encoding="utf-8"))
p14 = json.load(open(os.path.join(ARCH, "data", "profile14_families.json"), encoding="utf-8"))
texts = {}
for e in fc["equations"]:
    texts[e["id"]] = e["expr"]
for k, v in sq["small_sts_extras"]["eq_texts"].items():
    texts[int(k)] = v
for f in p14["families"]:
    texts[f["anchor_id"]] = f["anchor_expr"]
j61 = {1312: "x = y * (((y * x) * x) * x)", 2241: "x = (x * (x * (x * y))) * y",
       4295: "x * (x * y) = y * (z * x)", 4303: "x * (x * y) = z * (y * x)",
       4610: "(x * x) * y = (y * z) * x", 4637: "(x * y) * x = (y * x) * z"}
texts.update(j61)
bad2 = [i for i, s in texts.items() if not same_law(i, s)]
print("archive/J61 texts checked:", len(texts), "mismatches:", bad2)
for i in bad2:
    print("   ", i, "archive:", texts[i], "| mine:", E.show(i))

# profile counts the archive computed with the ETP's explore_magma.py
cases = [("constant 3x3", np.zeros((3, 3), int), 1556),
         ("right projection 3x3", np.tile(np.arange(3), (3, 1)), 1214),
         ("Z/5", np.add.outer(np.arange(5), np.arange(5)) % 5, 32),
         ("-(x+y) mod 4", (-np.add.outer(np.arange(4), np.arange(4))) % 4, 294),
         ("x*y=f(y), f=(1,2,2)", np.tile(np.array([1, 2, 2]), (3, 1)), 261),
         ("Z/3", np.add.outer(np.arange(3), np.arange(3)) % 3, 60),
         ("Z/4", np.add.outer(np.arange(4), np.arange(4)) % 4, 116)]
for name, T, want in cases:
    got = len(E.profile(T))
    print(f"  {name}: {got} (archive: {want})", "OK" if got == want else "MISMATCH")
print("time %.1fs" % (time.time() - t0))
