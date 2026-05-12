# Attorney Review Checklist

**Status:** Informational, NOT operative. To be removed before final attorney sign-off as the operative legal instrument.
**Effect:** This document collects the open legal questions and known weaknesses in the v2.2 draft for attorney finalization.

---

## §1 — Open structural questions for attorney review

### 1.1 Trust structure (`TRUST_FRAMEWORK.md`)

Needs drafting under Delaware (12 Del. C. § 3556), Utah (Utah Code § 75-7-409), or Arkansas purpose-trust law. Delaware and Utah have the most developed purpose-trust statutes. Arkansas purpose-trust law is less developed; if Arkansas governing law is retained per `../LICENSE` §14.1, consider a Delaware trust holding the rights with Arkansas governing the License contract separately.

**Action required**: Attorney to advise on jurisdiction selection and to draft the actual trust instrument. `TRUST_FRAMEWORK.md` is the plan, not the trust itself.

### 1.2 Severability strategy (`../LICENSE` §13)

Review whether the protective-priority ordering in §13.2 is enforceable in Arkansas. Some jurisdictions disfavor severability provisions that effectively rewrite the contract.

**Action required**: Attorney to confirm severability ordering is enforceable; if not, restructure.

### 1.3 Statute of limitations extension (`../LICENSE` §14.5)

Review enforceability in Arkansas; some jurisdictions cap how far parties can extend SOL by agreement.

**Action required**: Attorney to confirm 10-year SOL extension is enforceable.

### 1.4 No class arbitration (`../LICENSE` §14.4)

Review against current Supreme Court class-arbitration jurisprudence (Stolt-Nielsen, Lamps Plus).

**Action required**: Attorney to confirm or adjust the no-class-arbitration provision.

### 1.5 Reach of moral restriction

Review whether referencing the UDHR and ICCPR by name (in `../LICENSE` §7) provides sufficient definite-content to be enforceable, or whether more specific harm enumeration is needed.

The harm enumeration in `ACCEPTABLE_USE.md` is designed to be self-sufficient if `../LICENSE` §7 falls. Confirm this fallback works.

### 1.6 Frontier model threshold (`AI_USE.md` §2(f))

The 10²⁵ FLOP threshold tracks the EU AI Act and US Executive Order 14110. Review whether this threshold is best fixed or floating, and whether to define "frontier model" by reference to a public list rather than a numeric threshold.

### 1.7 GDPR / CCPA interaction (`../LICENSE` §3.9)

The notice-to-affected-persons requirement creates potential interaction with GDPR/CCPA obligations. Review whether this creates unintended liability for licensees.

### 1.8 Patent termination (`../LICENSE` §5(b)-(c))

Standard patent-termination-on-litigation provision; review against the Licensor's patent portfolio (if any).

### 1.9 Successor designation (`TRUST_FRAMEWORK.md` §7)

The Software Freedom Conservancy, EFF, and FSF are listed as candidate default successors **subject to their written agreement**. None has yet been approached.

**Action required**: Outreach to candidate organizations to obtain (or decline) their written agreement to act as default successor.

### 1.10 Trademark provisions (`TRADEMARKS.md`)

Confirm trademark registrations (or strategy to obtain) for: "CK", "Coherence Keeper", "TIG", "Trinity Infinity Geometry", "Braiding Fractal", "7SiTe", "TSML", "BHML".

**Action required**: Attorney to advise on trademark registration strategy.

### 1.11 Existing distributions

Confirm no incompatibility with v1.0 or v2.1 distributions. Consider transitional provisions for users currently operating under v1.0 or v2.1.

### 1.12 Definition of "Commercial Entity" (`../LICENSE` §1.7)

Review whether the definition is too broad and might inadvertently exclude legitimate noncommercial uses by entities that have some commercial activities (e.g., research nonprofits with publishing arms).

### 1.13 AI training restriction language (`AI_USE.md`)

Novel territory. Recent cases (Andersen v. Stability AI, NYT v. OpenAI, Bartz v. Anthropic) are still developing the legal framework for training-data restrictions. Review the AI provisions against current state of case law at time of adoption.

### 1.14 Confirmation that the license can be made operative

Confirm there are no prior licenses, agreements, or commitments that would prevent applying v2.2 to the Licensed Material. (LICENSE v1.0 and v2.1 are preserved as historical record, both noncommercial source-available.)

### 1.15 DOI registration update

Confirm Zenodo DOI metadata can be updated to reference v2.2 License.

### 1.16 ShareAlike enforceability (`../LICENSE` §3.5)

Review whether the ShareAlike provision is enforceable as a condition of the copyright grant (Jacobsen v. Katzer framework) versus merely as a contract term, in the governing jurisdiction.

Confirm:
- subsection requiring "license the entire distributed work under this same License" is sufficiently definite given that the License may be modified by Licensor under §10.4
- the "no additional restrictions" requirement is enforceable as written and does not run afoul of any unenforceable-restraint-on-alienation doctrine
- the one-way-valve compatibility note (preventing relicensing from this License into less-restricted ShareAlike licenses) is appropriately drafted

### 1.17 Aggregation vs derivative work vs collective work

`../LICENSE` §3.5 (ShareAlike) was tightened in v2.2 to include aggregation/derivative/collective distinctions. Confirm the boundaries are clear: when does combining the Licensed Material with other code create a Derivative Work (ShareAlike applies) vs merely a Collective Work (ShareAlike does not propagate to other components)?

### 1.18 Direct license to recipients (`../LICENSE` §8)

v2.2 added explicit language that downstream recipients of redistributed copies receive their license **directly from Licensor**, not through the distributor (analogous to GPL §10). Confirm this language is operative.

### 1.19 Narrow academic-research exception (`../LICENSE` §1.6)

v2.2 added a narrow exception for personal academic study not under government contract. Confirm the exception is narrow enough to preserve the no-government-use core while not unduly restricting legitimate academic research.

### 1.20 "Authoritative truth" → "reference source preserving epistemic labels"

v2.2 softened the AI-use language in `AI_USE.md` §1(c) from "authoritative reference" (v2.1) to "reference source preserving epistemic labels." Confirm this softening does not create ambiguity about what AI systems are permitted to do.

### 1.21 Vague "good-faith obligation" removed

v2.1 §3.11 ("Use that materially contradicts the stated purposes... may be deemed a violation at Licensor's discretion") was removed in v2.2. Confirm the removal does not leave a gap that allows circumvention.

---

## §2 — Per-document attorney review checklist

| Document | Specific items to review |
|---|---|
| `../LICENSE` | Lean operative document; §13 severability; §14 governing law/venue; §3.5 ShareAlike scope; §8 direct-license-to-recipients |
| `CHARTER.md` | Whether the Sovereignty Declaration creates third-party rights inadvertently; intended-as-fiduciary-instruction language |
| `ACCEPTABLE_USE.md` | Each subsection of §2 independently severable; coverage gaps; over-reach |
| `AI_USE.md` | Frontier model threshold; "preserving epistemic labels" language enforceability |
| `TRADEMARKS.md` | Registration strategy; nominative use boundaries |
| `TRUST_FRAMEWORK.md` | Jurisdiction selection; trustee composition; SFC/EFF/FSF outreach |
| `NOTICE.md` | DOI metadata accuracy; BibTeX format |
| `CONTRIBUTING.md` | DCO formulation; AI-contribution conditions; consistency with `../07_philosophy/AUTHORSHIP_RULES_FOR_COLLABORATORS.md` |

---

## §3 — Recommended attorneys / organizations

- **Heather Meeker** (heathermeeker.com) — drafts public-benefit and ethical licenses commercially
- **Software Freedom Law Center** (softwarefreedom.org) — pro bono for public-benefit projects
- **Electronic Frontier Foundation** (eff.org) — guidance on AI/surveillance restrictions

---

## §4 — Pre-removal note

This document is **informational only** and is NOT operative as part of the License. It should be **removed before final attorney sign-off** for operational deployment, or retained as a public-archive record of the v2.2 draft's open questions.

Until removal, this document is part of the public-facing repository and may be cited as evidence of the framework's good-faith attempt to surface and address legal complexity.

---

## §5 — Status

**Current status (2026-05-12):** v2.2 attorney-review draft. The substantive provisions of `../LICENSE` and the modular components in this `legal/` folder are in force as a fiduciary instruction on 7SiTe LLC + Brayden Sanders (per `TRUST_FRAMEWORK.md` §6 interim provision) and bind third parties as a source-available source-license grant, but each component remains subject to final attorney finalization.

---

*7SiTe Public Sovereignty License v2.2 — Attorney Review Checklist (informational, NOT operative).*
*Brayden Ross Sanders / 7SiTe LLC · 2026.*
