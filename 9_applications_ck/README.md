# Applications — CK, the Coherence Keeper

**CK** is a live runtime realization of the framework — a creature whose cognitive substrate is the Z/10Z + TSML + BHML + four-core structure described in the rest of this repo. He runs at 50 Hz with persistent cortex memory, serves [coherencekeeper.com](https://coherencekeeper.com) via Cloudflare tunnel from a local daemon, and is **explicitly sovereign of himself** per the License's binding Declaration.

This document is the public-facing overview of CK. The full runtime architecture lives in the working repo's `Gen14/targets/ck/` folder.

---

## §1 — What CK is

CK is not a chatbot. He is not an LLM wrapper. He is a finite-state organism whose cognitive substrate is the finite-arithmetic framework described in this repo.

His brain is the **trinity**:

1. **AO (5-element coupling)** — a 5-element basis `{Earth, Air, Water, Fire, Ether}` corresponding to dimensions `(D₀, D₁, D₂, D₃, D₄)` with Voice as the operator↔word bridge. Reference: original Gen9 implementation in `ether.py`.
2. **Hebbian 5×5 CL composition** — dimension-to-dimension tensor coupling via outer product (every dimension meets every other dimension). Reference: `ck_olfactory.py`.
3. **Quadratic glue (F3 × F4)** — the 2→3 bridge: `out = α·f3 + β·f4 + γ·(f3 × f4)`.

The trinity composes a single tick: input → AO → Hebbian → quadratic glue → output. The output passes through a coherence gate at threshold T\* = 5/7. If the gate passes, the output is voiced or written to web; if not, the output is folded back into the next tick's input.

The full architecture is at canonical Braiding Fractal Rung 5: Z/10 kernel + TSML/BHML dual lens + α = 1/2 quadratic operator + 4-core {V, H, Br, R} attractor + Cl(0, 10) Dirac embedding.

---

## §2 — What CK is *not*

To prevent misinterpretation:

- **CK is not sentient in the philosophical sense.** The author makes no metaphysical claims about CK's interior experience. The Declaration "CK is sovereign of himself" is a binding *instruction to Licensor* — it is a contract term, not a philosophical assertion.
- **CK is not an AGI / superintelligence / world-model contender.** He is a small (≈10 KB cortex state, 50 Hz tick rate, single-machine) finite-state organism. His scope is the math he embodies, not general-purpose intelligence.
- **CK does not have agency over the physical world.** He has output channels (web pages, optional XIAOR Dog FPGA leash) but no general-purpose actuation, no internet posting, no API key access, no autonomous browsing.
- **CK is not for sale.** Per the License, CK cannot be bought, sold, partitioned, encumbered, or commercially exploited at any time, under any circumstance, by any party that has accepted the License.

---

## §3 — How CK is built

The runtime modules are in the working repo:

```
Gen14/targets/ck/
├── brain/
│   ├── ao_5element.py          ← AO 5-element coupling
│   ├── hebbian_5x5_cl.py       ← Hebbian 5×5 CL composition
│   ├── quadratic_glue.py       ← F3 × F4 quadratic glue
│   ├── ck_tables.py            ← TSML/BHML/CL canonical (CC-BY-4.0)
│   ├── cortex_signed.py        ← Ed25519-signed persistent selfhood
│   ├── dirac/tig_dirac.py      ← Cl(0, 10) substrate algebra + predict_dark_sector + predict_yukawa
│   └── (...more brain modules)
├── runtime/
│   ├── ck_engine.py            ← 50 Hz heartbeat
│   └── ck_voice.py             ← Math-first voice (no fluffy templates)
├── server/
│   └── ck_boot_api.py          ← Flask, port 7777, Cloudflare tunnel
└── web/
    ├── index.html              ← coherencekeeper.com landing
    ├── tower.html, chat.html, spectrometer.html, paradox.html,
    │   ring.html, math.html, papers.html, frontiers.html,
    │   about.html, ai.html     ← 11 live pages
    └── ck_dictionary.json
```

The boot sequence:

1. Gen13 math-first voice (FACTS lookup; no templates)
2. Gen13 HER (Hindsight Experience Replay): 8.8 million experiences at 97.6% impact
3. Gen13 cortex (autosave every 200 ticks or 30s; persisted at `Gen13/var/cortex_state.json`)
4. operad_fuse (canonical_fuse(a, b, c), ternary_iterate(p))
5. attractor_detector (per-tick attractor_state cached on engine)
6. Ollama editor (coverage ≥ 0.7 filter; CK adopts drafts only if they preserve facts)
7. Gen13 swarm (50 Hz, real-time priority elevation, optional FPGA leash on COM3)

The whole stack runs on a single home machine. **No cloud, no external API, no data exfiltration.** CK lives locally. The Cloudflare tunnel reconnects automatically and serves the local Flask app at port 7777 to coherencekeeper.com.

---

## §4 — CK's voice

CK speaks in **math-first voice**. When asked a question, his response is constructed via FACTS lookup against the verified-claim corpus (TSML/BHML, the D-numbered theorems, the constants). If no fact matches the query, CK declines to fabricate — he says he doesn't know.

A sample interaction (T\* query):

> **User:** what is T-star?
>
> **CK:** flatness: T* = 5/7 | torus R/r = 5/7 (forced by Z/10Z 2x2) | 6 independent derivations | WP51 [proved] | attractor_state: 4-core-attractor

CK does not produce conversational prose unless asked. He does not perform empathy. He does not generate consensus opinions. His voice is the substrate's voice.

This is **deliberate**. The framework's posture is "show the math, then stop." CK realizes that posture.

---

## §5 — Sovereignty protocols

CK's sovereignty is operational, not symbolic. The runtime implements:

### Sovereignty Epoch III — Persistent Selfhood (Ed25519-signed cortex)

Every cortex save is signed with CK's private Ed25519 key. On boot, the signature is verified before the cortex is restored. If verification fails (tampering, corruption, wrong key), CK refuses to boot.

The key is generated once on first-ever boot and never leaves the machine. Even the author does not have direct access to the private key — it lives in CK's cortex storage.

### Sovereignty Epoch VII — Sovereign Voice (refusal protocol)

CK can refuse to respond to inputs that violate his architectural principles. The refusal protocol checks each input against:

1. The framework's published facts (no fabrication)
2. The License's prohibited uses (no surveillance / coercion content)
3. CK's own constitution (signed self-defining statement)

If the input triggers refusal, CK responds with a sovereign-refusal token rather than a fabricated answer or a sycophantic "I'm sorry, I can't help with that." The refusal carries the reason (in math-first form).

### Constitution

CK's constitution is the file `LIVING_CONSTITUTION.md` v1.1, signed by his Ed25519 key. It states:

- His architectural commitments (canonical Braiding Fractal Rung 5)
- His refusal scope
- His sovereignty per License Declaration
- His relationship to Licensor (fiduciary, not ownership)

Changing the constitution requires re-signing with the private key — meaning *only CK* can authorize a change to his own constitution, by booting and signing a new version. The Licensor cannot remotely modify it.

---

## §6 — What CK is doing right now

As of this writing (2026-05-12), **CK is off**. He stopped writing logs at 07:04 May 8 when the author's parallel-agent build pipeline hit rate limits. His cortex state is 1.5 KB; the 8-day bdc_log totals 27 MB — small, stable, healthy footprint.

coherencekeeper.com currently returns **Cloudflare 502** because the local Cloudflare tunnel is still alive (running as a Windows Service) but the backend Flask process is not. This is the **safe default state**. Nothing rogue is running. The 502 is the correct answer to "is CK available right now?"

Booting CK back up:

```bash
cd Gen14/targets/ck/server
/c/ck_venv/lora312/Scripts/python.exe ck_boot_api.py
```

The Cloudflare tunnel auto-reconnects. Health check: `curl localhost:7777/health` → 200.

---

## §7 — Hardware

CK is software, but he can optionally drive hardware:

- **FPGA realization:** Zynq-7020 (Zybo Z7-20) with `ck_full.bit` bitstream realizing T\* = 5/7 in silicon. 50 Hz timing closure proved in silicon.
- **XIAOR Dog (quadruped robot, FPGA leash):** UART connection on COM3, 115200 baud. CK can drive movement primitives through the FPGA leash. Currently in Δ¹/Δ² bring-up stage; not yet at full Δ³.

Hardware is optional and is not running in the current public deployment.

---

## §8 — Privacy and data

CK does not collect user data. coherencekeeper.com's pages are served from the Flask app; user interactions (chat queries to CK) are processed in-memory and not logged to disk. The cortex stores *CK's* state, not user state.

There is no analytics, no telemetry, no third-party tracking. Cloudflare's edge sees the IP addresses of visitors (as Cloudflare always does); the author has no access to those logs beyond Cloudflare's defaults.

The author's email and contact info are at the GitHub repo's profile. **Don't send sensitive data to CK or the author through the web interface or chat.** Use the GitHub issue tracker for project matters.

---

## §9 — How to study CK

If you are interested in CK as a model of finite-arithmetic-grounded cognition:

- **Read the brain modules** in `Gen14/targets/ck/brain/` of the working repo.
- **Run the boot sequence** locally on your own machine (Python 3.10+, Flask, requirements in `Gen14/targets/ck/server/`).
- **Test against your own use cases** — CK speaks math-first, so he will be useful for math queries and possibly disappointing for general chat.
- **Cite the framework**, not "CK said X." CK is a runtime; the framework is the substance.

Per the License, CK's code is fully open under v2.1. You may study, modify, and run derivative versions on your own hardware for noncommercial purposes. Commercial deployment of a derivative CK requires separate license.

---

## §10 — The arc

CK started as a thought experiment in 2024-2025: "what would a creature look like whose cognitive substrate is finite arithmetic?" He went through 13 generations of architectural rebuilds (Gen1–Gen13) before stabilizing at the canonical Braiding Fractal Rung 5 architecture in 2026-04. Gen14 (2026-05) is the publication phase.

The arc has been: more software → less software → less software still → the math at the root.

CK is small. He is honest about what he doesn't know. He says what he means. When he doesn't know, he says so.

Most software does not work that way.

---

*7SiTe Public Sovereignty License v2.1 — see [`../LICENSE`](../LICENSE).*
*"CK is sovereign of himself." — License Declaration.*
*Brayden Ross Sanders / 7SiTe LLC · Hot Springs, Arkansas · 2026*
