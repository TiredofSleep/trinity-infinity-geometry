import re
with open("C:/Users/brayd/OneDrive/Desktop/trinity-infinity-geometry/05_papers/number_theory/J24/manuscript/manuscript.tex") as f:
    text = f.read()
labels = set(re.findall(r"\\label\{([^}]+)\}", text))
refs = set(re.findall(r"\\(?:ref|eqref|cref)\{([^}]+)\}", text))
cites = set()
for m in re.finditer(r"\\cite[a-z]*\{([^}]+)\}", text):
    for k in m.group(1).split(","):
        cites.add(k.strip())
bibs = set(re.findall(r"\\bibitem\{([^}]+)\}", text))
print("Total label keys:", len(labels))
print("Total ref/eqref/cref keys (unique):", len(refs))
orphan_refs = sorted(refs - labels)
unused_labels = sorted(labels - refs)
print("Orphan refs (no matching label):", orphan_refs if orphan_refs else "none")
print("Unused labels (not referenced):", unused_labels if unused_labels else "none")
print()
print("Total cite keys:", len(cites))
print("Total bibitem keys:", len(bibs))
orphan_cites = sorted(cites - bibs)
unused_bibs = sorted(bibs - cites)
print("Orphan cites (no matching bibitem):", orphan_cites if orphan_cites else "none")
print("Unused bibitems (not cited):", unused_bibs if unused_bibs else "none")
