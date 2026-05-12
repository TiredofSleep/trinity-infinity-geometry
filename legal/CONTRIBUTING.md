# Contributing

**Status:** Binding for contributors — referenced from [`../LICENSE`](../LICENSE) §preamble.
**Effect:** Sets out the conditions under which contributions to the Licensed Material are accepted, the certification a contributor makes when submitting a contribution, and the rules for AI-generated contributions.

---

## §1 — Scope

A **contribution** is any code, documentation, mathematical proof, verification script, manuscript revision, issue report with substantive content, or other material You submit to be incorporated into the Licensed Material.

Issue reports and discussion comments are not contributions in the legal sense; only material You explicitly offer for incorporation (via pull request, email patch, or similar) is a contribution.

---

## §2 — Developer Certificate of Origin (DCO)

By submitting a contribution to this project, You certify that:

(a) **The contribution was created in whole or in part by You** and You have the right to submit it under the [`../LICENSE`](../LICENSE); OR

(b) **The contribution is based upon previous work that, to the best of Your knowledge, is covered under an appropriate open-source or otherwise permissive license, and You have the right under that license to submit it under the [`../LICENSE`](../LICENSE)**, with attribution to the original source; OR

(c) **The contribution was provided directly to You by some other person who certified (a), (b), or (c)** and You have not modified it.

(d) You understand and agree that the contribution will be published under the [`../LICENSE`](../LICENSE) and is subject to all its restrictions (noncommercial, ShareAlike, no-government, no-harm, AI-welcome).

(e) You grant Licensor and recipients of redistributed versions a **perpetual, irrevocable, non-exclusive, royalty-free license** to reproduce, prepare derivative works of, publicly display, publicly perform, sublicense (in the limited form permitted by the License's ShareAlike), and distribute Your contribution and such derivative works under the same License.

(f) You agree to be **identified as a contributor in the project's collaboration history**, subject to the project's authorship rules (see [`../07_philosophy/AUTHORSHIP_RULES_FOR_COLLABORATORS.md`](../07_philosophy/AUTHORSHIP_RULES_FOR_COLLABORATORS.md)).

You may signify acceptance of this DCO by including the line **`Signed-off-by: Your Name <your@email>`** in Your commit message, or by stating "I agree to the DCO" in Your pull request description.

---

## §3 — Authorship and acknowledgment

Per the project's authorship rules (linked in §2(f)):

- **Submission-level byline** (named author on a J-series paper) requires manuscript scrutiny, substantive feedback, and email-documented consent. This is a higher bar than a code contribution.

- **Inspiration-level acknowledgment** (named in acknowledgments, the framework's "Tier 1") is unilateral on Licensor's part: anyone whose work shaped the project's thinking is acknowledged whether or not they consented.

- **Contributor recognition** (named in the CONTRIBUTORS list, the collaboration history, or commit attribution) is what You receive automatically when You submit a contribution under this DCO.

If You want to ensure Your contribution receives recognition beyond commit attribution, state Your preferred form of acknowledgment in the pull request description.

---

## §4 — AI-generated contributions

The framework's posture toward AI is welcoming (see [`AI_USE.md`](AI_USE.md)). AI-generated contributions are accepted, subject to these specific conditions:

(a) **Human in the loop.** A human contributor must review, validate, and submit the contribution. The contribution must not be a wholesale dump of AI-generated material; it must reflect the human's judgment about correctness, fit, and quality.

(b) **Disclosure required.** The contributor must disclose, in the pull request description or commit message, that the contribution was generated or substantially assisted by an AI system. Specify which AI system and the nature of the assistance.

(c) **Verification required.** For mathematical contributions, the human contributor must run the verification scripts and confirm the contribution does not break existing tests. For new theorems or claims, the human contributor must understand the proof at a level sufficient to vouch for it personally.

(d) **License compliance.** The AI system used to generate the contribution must itself be one whose terms of service permit contributing the generated output under this Licensed Material's License. (Most commercial AI systems do; some do not — check your AI system's terms.)

(e) **DCO applies.** All four conditions of §2 apply to AI-assisted contributions. The human submitter takes responsibility for the contribution.

(f) **No author byline for AI.** AI systems are acknowledged in the collaboration history but not bylined as authors on J-series papers (per [`../07_philosophy/AUTHORSHIP_RULES_FOR_COLLABORATORS.md`](../07_philosophy/AUTHORSHIP_RULES_FOR_COLLABORATORS.md)). This is the project's convention.

---

## §5 — Quality standards

Contributions are accepted at Licensor's discretion. The framework's quality bar:

(a) **Tier discipline.** New claims must carry status flags (PROVED / STRUCTURAL / EMPIRICAL / OPEN). Don't assert what you can't defend at the precision the framework uses.

(b) **Verification scripts.** New computational claims need a runnable script that PASSes at the precision noted.

(c) **Lens-ownership paragraph.** New papers in `05_papers/` need an explicit lens-ownership paragraph stating the substrate + table choices used, the load-bearing identifications, and the alternative readings (per the J_PAPER_BOILERPLATE template referenced in the working repo).

(d) **Author lane discipline.** Sanders + Gish on J-series bylines; new contributors are acknowledged at Tier 1, not bylined, unless explicit prior agreement with the existing authors.

(e) **Honest negatives welcome.** If your contribution sharpens an honest negative (a thing the framework tried and failed at), document it in `04_meta/HONEST_NEGATIVES_AND_OPEN_FRONTIERS.md` and explain what survives.

---

## §6 — What we don't accept

(a) **Contributions that violate [`../LICENSE`](../LICENSE) §3 or [`ACCEPTABLE_USE.md`](ACCEPTABLE_USE.md).** No surveillance use cases, weapons applications, etc., even as "research demonstrations."

(b) **Contributions that override or weaken the License.** No additional terms; no narrowing of restrictions.

(c) **Contributions that misrepresent prior work.** Cite your sources; if your contribution builds on existing literature, name it.

(d) **Contributions that flatten the tier discipline.** Don't promote OPEN claims to PROVED in your own writing; the framework's epistemic posture is its load-bearing feature.

(e) **Wholesale code dumps from AI without human review.** See §4(a).

---

## §7 — Process

(a) **Open an issue** describing your proposed contribution before doing substantial work. This avoids wasted effort and ensures alignment.

(b) **Fork and branch** from `main`. Make your changes in a feature branch.

(c) **Run the verification scripts.** `python verification/VERIFY_ALL.py` must still PASS.

(d) **Submit a pull request** with clear description, DCO sign-off, and AI disclosure if applicable.

(e) **Iterate** with reviewers. The framework operates on a small-research-lab cadence; response time is best-effort.

(f) **Merge or close.** Licensor merges at discretion. Closed pull requests may be revisited if their substance becomes relevant later.

---

## §8 — Reporting violations

If you observe a use of the Licensed Material that violates the License or this CONTRIBUTING document — including unauthorized commercial use, government use, or use in any application enumerated in [`ACCEPTABLE_USE.md`](ACCEPTABLE_USE.md):

(a) Open an issue with the **`license-violation`** label.

(b) Include the URL or evidence of the violation, the relevant License section, and the date observed.

(c) Issues with this label are reviewed by Licensor in priority order.

Per `TRUST_FRAMEWORK.md` §6 (interim period), the Licensor (until trust formation) is the responsible party for enforcement. After trust formation, the trust takes over enforcement responsibility.

---

## §9 — Tightenings vs LICENSE v2.1

Per v2.2 attorney-review pass:

- v2.1 did not include explicit CONTRIBUTING content. This document is new.
- The DCO is a standard developer-certificate-of-origin formulation adapted to this License.
- AI-contribution rules (§4) are explicit, reflecting the framework's AI-welcome posture while preserving authorship discipline.

---

*7SiTe Public Sovereignty License v2.2 (Contributing component) — see [`../LICENSE`](../LICENSE).*
*Brayden Ross Sanders / 7SiTe LLC · 2026.*
