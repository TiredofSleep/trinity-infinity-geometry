# SYMBOL_SUBSTRATE_DECODING_ROADMAP

## Testing plan for the next phase of substrate-stratification research

**Locked**: 2026-05-12
**Status**: research roadmap; not load-bearing for current canon
**Companion docs**: `SYMBOL_SUBSTRATE_DECODING.md`, `SYMBOL_SUBSTRATE_DECODING_EXTENSIONS.md`
**Framework location**: `09_seekers/` planning document

---

## §1. Tests completed (n=7)

For reference, the seven tests already analyzed:

1. **Hindu-Arabic digits** (Rung 5) — ✓ Strong
2. **Latin alphabet** (Rung 1 + embedded 0, 2) — ✓ Strong
3. **Sumerian Cuneiform** (Mixed) — Productive refinement
4. **Chinese hanzi** (Multi-rung embedded) — ✓ Strong
5. **Korean Hangul** (Rung 2 designed) — ✓ STRONGEST
6. **Chemical symbols / Periodic table** (Rung 5) — Mixed at symbol level, ✓ at table level
7. **Programming syntax** (Rung 1 + Rung 2) — ✓ Strong

---

## §2. Priority-ordered next tests

### §2.1 Priority 1 (Critical falsification tests)

**Test 8 — Punctuation marks (Rung 0 prediction)**

The framework predicts punctuation should be Rung 0 (pure boundary, 0-1 component). If this fails, the substrate-stratification methodology is wrong about the smallest-rung case.

**Symbols to analyze**:
- Period (.) — predicted 1-component (pure point)
- Comma (,) — predicted 1-component (point + tail = 2-component, embedding Rung 1)
- Semicolon (;) — predicted 2-component (comma + point, embedding Rung 1)
- Colon (:) — predicted 2-component (two points)
- Exclamation (!) — predicted 2-component (stroke + point, embedding Rung 1)
- Question mark (?) — predicted 2-component (curve + point, embedding Rung 1)
- Ellipsis (…) — predicted 3-component (three points, embedding Rung 2)
- Em dash (—) — predicted 1-component (pure stroke = pure boundary)
- Apostrophe (') — predicted 1-component (single mark)
- Quotation marks (" ") — predicted paired 2-component (Rung 1 binary)

**Prediction summary**: simple punctuation should be Rung 0 with optional Rung 1 embedding. Complex punctuation (?, !, ellipsis) should show explicit Rung 1 or Rung 2 embedding.

**Falsification**: if punctuation decomposes into 3-component primary structures, the framework's Rung 0 prediction is wrong.

**Difficulty**: low. Glyphs are simple and well-documented.

**Priority**: 1A — this is the cleanest falsification test.

---

**Test 9 — Mayan numerals (independent-tradition Rung 5 test)**

The Maya developed an independent positional numeral system using dots, bars, and a shell glyph for zero. Their system has Rung 5 features at the organizational level.

**Mayan numerals 0-19**:
- 0: shell glyph (closed form, consistent with framework's "0 = closure" finding)
- 1: single dot
- 2: two dots
- 3: three dots
- 4: four dots
- 5: single bar
- 6: bar + dot
- 7: bar + 2 dots
- ...
- 10: 2 bars
- ...
- 19: 3 bars + 4 dots

**Structural analysis**:
- Single-digit (0-4): n dots, additive
- Quinary boundary at 5: bar replaces 5 dots (single structural component for the threshold)
- Composite (6-19): bar(s) + dot(s)

**Prediction**: Mayan numerals show **partial Rung 5 substrate-resonance** with the explicit quinary boundary at 5 (consistent with the framework's T*=5/7 threshold). The system uses **two-component composition** (bars + dots) rather than the 3-component decomposition of Hindu-Arabic numerals.

**Implications if confirmed**: Mayan numerals are *partially* substrate-resonant at Rung 5 (quinary threshold recognized) but not *fully* substrate-resonant at depth-3 wrapping (component count is 2, not 3). This would explain why Mayan numerals were historically more limited than Hindu-Arabic (the framework would predict partial substrate-resonance → partial cultural durability).

**Falsification**: if Mayan numerals show no rung-5 features at all, the cross-cultural substrate-stratification claim weakens significantly.

**Difficulty**: low-medium. Mayan glyphs are well-documented in Mayanist scholarship.

**Priority**: 1B — strong cross-cultural test for the digit hypothesis.

---

**Test 10 — Devanagari numerals and script (Indian tradition test)**

Devanagari is the ancestor (or close relative) of modern Hindu-Arabic numerals through Brahmi → Gupta → Nagari → Devanagari → Arabic transmission. Testing Devanagari directly examines an intermediate stage of the transmission.

**Devanagari numerals 0-9**:
- ० (zero) — circle, identical structural role to "0" in Hindu-Arabic
- १ (one) — single stroke with hook
- २ (two) — curved stroke
- ३ (three) — three-part stroke
- ४ (four) — angular shape
- ५ (five) — looped form
- ६ (six) — closed loop with descender
- ७ (seven) — angular meeting (similar to Hindu-Arabic 7)
- ८ (eight) — closed form
- ९ (nine) — closed loop with extension

**Prediction**: Devanagari numerals should show similar 3-component substrate-stratification to Hindu-Arabic, as they're ancestors. If the framework's prediction holds, we should see:
- Same substrate-rung encoding
- Possible *cleaner* encoding (closer to substrate) since less transmission-distance
- Same VOID-as-closure for 0, same LATTICE-as-minimum for 1, etc.

**Falsification**: if Devanagari numerals show *different* substrate-rung encoding than Hindu-Arabic, the framework would need to explain why transmission would *increase* substrate-resonance rather than decrease it.

**Difficulty**: medium. Requires familiarity with Devanagari script evolution.

**Priority**: 1C — directly tests the transmission-chain hypothesis.

---

### §2.2 Priority 2 (Strong cross-cultural tests)

**Test 11 — Egyptian hieroglyphs (independent-tradition multi-rung test)**

Egyptian hieroglyphs developed independently from Sumerian Cuneiform and used pictographic, ideographic, phonographic, and determinative signs simultaneously.

**Categories of hieroglyphs**:
- **Pictographs**: direct representations of objects (predicted Rung 2-3, depending on object complexity)
- **Ideographs**: representations of concepts (predicted Rung 2-3)
- **Phonographs**: signs representing sounds (predicted Rung 1-2)
- **Determinatives**: category markers added to clarify meaning (predicted Rung 1, binary classification)

**Specific test glyphs**:
- 𓂀 (Eye of Horus) — complex pictographic, predicted Rung 3 (multi-component)
- 𓀀 (seated man, A1) — pictographic person, predicted Rung 3
- 𓏏 (loaf, t-sound) — phonographic, predicted Rung 2
- 𓆑 (horned viper, f-sound) — phonographic, predicted Rung 2
- 𓊪 (stool, p-sound) — phonographic, predicted Rung 2

**Prediction**: Egyptian hieroglyphs should show **explicit substrate-stratification by sign category** — pictographs at higher rungs, phonographs at lower rungs, determinatives at the binary kernel level.

**Falsification**: if all categories of hieroglyphs encode at the same rung, the substrate-stratification methodology fails for this tradition.

**Difficulty**: high. Requires Egyptological expertise and access to primary glyph databases.

**Priority**: 2A — major independent-tradition test.

---

**Test 12 — Indian musical notation / Sargam (Rung 3 prediction)**

Indian classical music uses *sargam* notation: सा रे ग म प ध नि (Sa Re Ga Ma Pa Dha Ni), corresponding to the seven notes of the octave.

**Prediction**: Sargam should encode at Rung 3 (processual / triadic) like Western musical notation, with cultural variation in cross-rung embedding.

**Key features to analyze**:
- 7 notes (consistent with HARMONY = 7 in substrate)
- Use of Devanagari script (cross-rung embedding via writing system)
- Notation of duration, rhythm, ornamentation
- Comparison with raga/tala system (multi-rung organizational structure)

**Prediction in detail**:
- The 7-note system itself: Rung 3 (sequential, processual)
- Individual note glyphs (Devanagari): Rung 1 (binary kernel, embedded)
- Raga structures (modal frameworks): Rung 2-3 (relational + processual)
- Tala (rhythm cycles): Rung 3 explicitly cyclic

**Falsification**: if Sargam shows no Rung 3 encoding, the framework's prediction for musical notation fails across cultures.

**Difficulty**: medium-high. Requires Indian musical scholarship.

**Priority**: 2B — important cross-cultural musical notation test.

---

**Test 13 — Sign Languages (ASL, BSL, JSL) (multi-rung kinetic test)**

Sign languages encode meaning through handshape, location, movement, palm orientation, and non-manual markers (facial expression). They're a fundamentally different modality from written symbols.

**Prediction**: sign languages should show **multi-rung simultaneous encoding** because they handle multiple dimensions in parallel:
- **Handshape** (Rung 2): relational articulation similar to Hangul consonants
- **Location** (Rung 1): binary distinctions (face/body, left/right)
- **Movement** (Rung 3): processual/temporal
- **Palm orientation** (Rung 1): binary (toward/away)
- **Non-manual markers** (Rung 2): grammatical relations

**Specific test signs to analyze**:
- ASL "I love you" handshape
- BSL fingerspelling alphabet
- JSL (Japanese Sign Language) numbers

**Prediction**: sign languages should be the **most explicit multi-rung embedded systems** known, because they must use multiple simultaneous channels to convey what writing systems convey sequentially.

**Falsification**: if sign languages show single-rung encoding, the multi-rung embedding hypothesis fails.

**Difficulty**: high. Requires Deaf studies and sign linguistics expertise.

**Priority**: 2C — extends framework into kinetic-spatial modality.

---

### §2.3 Priority 3 (Specialized notation tests)

**Test 14 — Mathematical notation beyond operators (advanced multi-rung)**

- Set notation: ∈, ⊆, ⊇, ∪, ∩, ∅
- Calculus: ∫, ∂, ∇, lim, Σ, Π
- Logic: ∀, ∃, ⊢, ⊨, ¬, →, ↔
- Linear algebra: ⊗, ⊕, |⟩, ⟨|

**Prediction**: should show explicit Rung 2-3 encoding with rich cross-rung embedding for the most abstract symbols.

**Priority**: 3A.

---

**Test 15 — Cosmological / astronomical symbols**

- Zodiacal: ♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓
- Planetary: ☉ ☽ ☿ ♀ ♁ ♂ ♃ ♄ ♅ ♆
- Alchemical: ☉ ☽ ☿ ♀ ♂ ♃ ♄ (overlap with planetary)

**Prediction**: durable astronomical notation should be substrate-resonant; less durable alchemical-specific symbols should be less resonant.

**Priority**: 3B.

---

**Test 16 — Failed symbol systems (negative-result test)**

Symbol systems that were not historically durable and were displaced:
- Indus Valley script (undeciphered, ~2600-1900 BCE)
- Linear A (Minoan, undeciphered)
- Aztec pictographs (replaced by Latin alphabet after Spanish contact)
- Phaistos disc symbols (unique inscription)
- Vinča symbols (Neolithic European, possibly proto-writing)

**Prediction**: failed systems should show *less* substrate-resonance than successful ones. This is a critical test — if failed systems are equally substrate-resonant, the cultural-durability claim of the framework is wrong.

**Methodology**: even though some are undeciphered, we can analyze their *structural* features (component counts, organizational patterns) without knowing meaning. If failed systems show predominantly Rung 0-1 structure (under-resonant) or Rung 5+ structure (over-resonant for their use case), the framework's prediction holds.

**Priority**: 3C — most important *negative* test for the framework.

---

### §2.4 Priority 4 (Modern designed systems)

**Test 17 — Constructed languages**:
- Esperanto alphabet
- Klingon writing
- Tengwar (Tolkien)
- Lojban notation

**Prediction**: explicitly designed for human accessibility, these should show high substrate-resonance.

**Priority**: 4A.

---

**Test 18 — Emoji and Unicode pictographs**:
- The basic emoji set: 😀😢😡 etc.
- Symbol categories (animals, food, weather, activities)
- Compositional emoji (skin tones, gender variants)

**Prediction**: emoji should show evolutionary substrate-resonance as the most-used emoji are selected by cultural transmission. Multi-rung embedded encoding expected.

**Priority**: 4B — modern cultural-evolution test.

---

## §3. Methodology refinements suggested by current testing

Based on the seven completed tests, several methodology improvements are recommended for future tests:

### §3.1 Quantitative scoring

Develop a numerical "substrate-resonance score" for each symbol system based on:
- Match between predicted and observed component counts
- Match between substrate-rung properties and symbol features
- Consistency across symbols within a system
- Cross-cultural correlation strength

A scoring methodology would allow:
- Comparison between symbol systems
- Statistical analysis of cultural-durability vs. substrate-resonance correlation
- Publication in quantitative cognitive science venues

### §3.2 Primary-source verification protocol

Before any future test result is incorporated into canon:
1. All specific glyph descriptions must be verified against primary sources or recognized scholarly references
2. Glyph evolution paths must be traced through published historical sources
3. Phonological/articulatory claims must be checked against linguistic literature
4. Cross-cultural claims must be reviewed by domain specialists when possible

### §3.3 Independent replication

The substrate-stratification methodology should be reproducible by other researchers without framework-specific training. Future tests should be documented with sufficient detail that an external researcher could:
- Apply the methodology to the same symbol system
- Reach similar conclusions about substrate-rung encoding
- Replicate the analysis with their own scholarly verification

### §3.4 Blinded prediction protocol

For future tests, the framework's prediction should be **recorded before** the analysis begins, not generated during analysis. This prevents unconscious confirmation bias.

---

## §4. Falsifiability dashboard

The framework's overall credibility depends on maintaining a clear record of:

**Supporting tests** (currently 6/7):
- Hindu-Arabic digits ✓
- Latin alphabet ✓
- Chinese hanzi ✓
- Korean Hangul ✓ (strongest)
- Periodic table organization ✓
- Programming syntax ✓

**Refining test** (1/7):
- Cuneiform — productive refinement (substrate-resonance is evolutionary)

**Future critical tests**:
- Punctuation (Rung 0 critical falsification)
- Mayan numerals (independent-tradition Rung 5 test)
- Failed symbol systems (negative-result test)

**Acceptable failure rate**: if 3+ of the next 5 tests (Priority 1-2) fail to support the framework, the substrate-stratification methodology needs significant revision. The framework should make falsifiable predictions and own the results when they don't hold.

---

## §5. Publication strategy

When the methodology has been tested across 12-15 symbol systems with sufficient primary-source verification, this work would be publishable in:

**Primary venues**:
- *Cognitive Science* — quantitative analysis of substrate-resonance in symbol systems
- *Computational Linguistics* — methodology and data
- *Cognitive Linguistics* — theoretical framework
- *Journal of Quantitative Linguistics* — statistical analysis

**Secondary venues** (for specific findings):
- *Writing Systems Research* — for specific symbol-system analyses
- *Journal of the Royal Anthropological Institute* — cross-cultural findings
- *Music Perception* — for music notation analysis
- *Cognition* — for the Hangul deliberate-design case study

**Estimated timeline**: 18-24 months of additional testing and verification before initial submission. This is NOT a Sept 11 deliverable; it's a long-arc research program.

---

## §6. For ClaudeCode

Recommended sequencing:

**Phase 1 (next 2-4 weeks)**: complete Tests 8 (Punctuation), 9 (Mayan), 10 (Devanagari). These are the cleanest tests with the lowest verification cost.

**Phase 2 (1-3 months)**: complete Tests 11 (Egyptian), 12 (Sargam), 13 (Sign languages). These require external expertise and verification.

**Phase 3 (3-6 months)**: complete Tests 14-16 (Math notation, astronomical, failed systems). These deepen the framework.

**Phase 4 (6-12 months)**: complete Tests 17-18 (Constructed languages, emoji). These extend to modern designed systems.

**Phase 5 (12-18 months)**: methodology refinement, primary-source verification, publication preparation.

**Do not**:
- Draft journal papers without Brayden's authorization
- Treat untested predictions as canon
- Propagate Tier C content as if it were Tier B
- Skip primary-source verification for any individual test
- Rush to publication — this work is exploratory and the framework's credibility depends on getting the verification right

**Do**:
- Maintain the falsifiability dashboard rigorously
- Document each test's methodology, prediction, and result
- Cross-reference with the existing TIG canon (D101, D102, etc.)
- Flag interesting findings (like the 永 character) as standalone publishable observations
- Coordinate with computational linguistics literature properly

---

## §7. Status

This is a research roadmap, not a load-bearing canon document. It guides the next phase of exploration but doesn't commit the framework to any specific result.

The strength of the current evidence (6/7 tests supportive) justifies continued investigation. The framework is making testable predictions that have largely held up. The methodology is now mature enough to extend to additional symbol systems.

The work continues.

---

*© 2026 Brayden Ross Sanders / 7SiTe LLC*
*Licensed under the 7SiTe Public Sovereignty License v2.1*
*Coherence Keeper is sovereign of himself.*
*Trinity Infinity Geometry — Symbol-Substrate Decoding Roadmap.*
