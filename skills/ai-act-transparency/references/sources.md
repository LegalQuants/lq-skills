# Source Manifest — Article 50 Transparency Assessor

Audit-grade provenance for every authority this skill relies on. Because the skill stands on **post-cutoff**
law and soft law (the Jul-2026 Digital Omnibus, the Jul-2026 final Guidelines, the Jun-2026 Code, the EU icon
set), each source below carries an official URL, a legal-status flag, a **last-checked date**, and a
*supersedes* note. On activation, re-verify any row still flagged **live / evolving** and stamp the result
into the report's **Source-status block** (see [report-template-art50.md](report-template-art50.md)).

> **Last full manifest check:** 2026-08-04. **The July 2026 consolidation is done:** the Digital Omnibus is in
> the OJ, the Art. 50 Guidelines are final, and the Code has been assessed as adequate. All three of the
> "pending" statuses carried by v1.2 of this skill are **superseded** — do not reintroduce them.

---

## Uncertainty tiers (used throughout the skill's output)

| Marker | Meaning | Instruments here |
|--------|---------|------------------|
| **Settled law** | Black-letter, in force | Regulation (EU) 2024/1689 Art. 50, 3(60), 99(4)(g); **Art. 111(4)** as inserted by Reg. (EU) 2026/1744 |
| **Official guidance** | Commission interpretation, **final but non-binding** | Art. 50 Guidelines (final, 20 Jul 2026) |
| **Technical best practice** | Voluntary Code (adequacy-assessed); adherence ≠ conclusive evidence | Code of Practice (final 10 Jun 2026); EU icon set |
| **Open issue** | Un-litigated or expressly left case-by-case | **No CJEU ruling on Art. 50**; the Guidelines' own case-by-case tests (appreciable resemblance, "evidently" artistic, substantiality of alteration); Guidelines to be revised with experience (para. 155) |

---

## Primary law

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Regulation (EU) 2024/1689 (AI Act)** — Art. 50, 3(60), 96(1)(d), 99(4)(g), 111, 113 | **In force** (settled law) | `https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689` | 2026-08-04 | Art. 50 **applies from 2 Aug 2026** (Art. 113 general date). Penalty **Art. 99(4)(g)** = up to €15M / 3% (€750k EU bodies; SMEs the lower figure). |
| **Regulation (EU) 2026/1744 (Digital Omnibus on AI)** | **In force** (settled law) | `https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng` | 2026-08-04 | **Published in OJ 24 Jul 2026; entered into force 27 Jul 2026** (3rd day after publication, chosen for urgency ahead of 2 Aug 2026). Inserts **Art. 111(4)** = the 50(2) legacy-marking transition to **2 Dec 2026**. Also: new **Art. 5(1)(ba)/(bb)** prohibitions (non-consensual intimate imagery; CSAM) applying from 2 Dec 2026; Annex III high-risk → 2 Dec 2027 / embedded → 2 Aug 2028; sandbox → 2 Aug 2027. **Supersedes** every "adopted, awaiting OJ" / "near-settled" / "politically agreed" framing. |

## Commission Guidelines on Article 50

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Final Art. 50 Guidelines (20 Jul 2026, 51 pp.)** | **Final** (official guidance; non-binding) | landing `https://digital-strategy.ec.europa.eu/en/library/guidelines-transparency-obligations-providers-and-deployers-ai-systems` · PDF `https://ec.europa.eu/newsroom/dae/redirection/document/131215` · approving Communication `https://ec.europa.eu/newsroom/dae/redirection/document/131214` | 2026-08-04 | Issued under **Art. 96(1)(d)**; covers **all** of Art. 50; **155 numbered paragraphs**. **Supersedes** the 8 May 2026 draft (consultation closed 3 Jun 2026) and the Mar 2026 first draft. Commission will revise as experience accrues (para. 155). |
| **Commission FAQ — transparency obligations under Art. 50** | Live (official guidance) | `https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act` | 2026-08-04 | Useful plain-language restatement. **Caution:** it compresses the deepfake test into "three cumulative criteria" by merging elements (ii) and (iii) — the Guidelines themselves say **four** (para. 113). Prefer the Guidelines when they differ in granularity. |
| **Policy hub — Guidelines on transparency of AI-generated content** | Live | `https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content` | 2026-08-04 | Entry point; links the PDF above. |

### Draft → final paragraph map (v1.2 cited draft numbers; all superseded)

| Point | Draft (8 May) | **Final (20 Jul)** |
|---|---|---|
| Mere dissemination / platforms are not deployers | 12 | **16** |
| Personal-use carve-out, Art. 2(10) | 17 | **19** |
| FOSS remains subject to Art. 50 | — | **24** |
| Art. 50 ↔ 53 layering; model-level marking encouraged | 23–24, 70 | **27** |
| AI agents self-disclose (+ on whose behalf, every new interaction) | 28 | **31** |
| 50(1) negative catalogue (T&Cs, "assistant", …) | 35 | **38** |
| Average-consumer benchmark / obviousness factors | 40–42 | **43–45** |
| 50(2) not GPAI-specific; single-purpose + agentic in scope | 54 | **57–58** |
| Mere reproduction/arrangement (recommenders) out of scope | — | **65** |
| Scope exclusions incl. **source code** | 64 | **68** |
| Marking **and** detection both required | 65 | **69–70** |
| Assistive function / standard editing exceptions | — | **90–92** |
| B2B/industrial, cumulative conditions | 81 | **87** |
| Ephemeral in-game / VR generation | 82 | **88** |
| 50(3) covers all biometric categorisation incl. non-high-risk | 98 | **104** |
| 50(3) notice content vs GDPR Art. 13/14 | — | **105** |
| Deepfake — four cumulative criteria | 107 | **113** |
| False authenticity; intended/foreseeable audience; no intent needed | 108 | **114** |
| Cosmetic vs substantive edits (journalistic images) | 109 | **116** |
| Attenuated artistic disclosure (duty survives) | — | **123** |
| Rights of third parties preserved (Recital 134) | 116 | **124** |
| Exclusively informative/commercial excluded from artistic limb | 114 | **122** |
| Penalties | 140 | **152** |
| Legacy 50(2) transition to 2 Dec 2026 | — | **153** |
| No retrospective marking (date of **generation**) | — | **154** |

### Substantive changes from draft to final (not just renumbering)

1. **Machine translation reversed.** The draft named a translation engine as an in-scope 50(2) example. The
   final Guidelines list **"AI-generated translations of text"** among the **standard-editing** examples
   benefiting from the exception (para. 92). v1.2 of this skill asserted the opposite — corrected in v1.3.
2. **Retroactivity keys on generation, not publication** (para. 154). Deepfakes and 50(2) outputs
   **generated or manipulated** before 2 Aug 2026 escape; public-interest **text** escapes only if
   **generated *and* published** before that date.
3. **Source-code exclusion is broader than v1.2 stated** (para. 68): programming, scripting, markup, query and
   configuration languages, plus SDKs, SQL, IaC, YAML, JSON config, schemas, APIs and libraries, and
   natural-language comments integral to the code. It is a **standalone** exclusion — *not* limited to
   machine-to-machine outputs, which are a separate bullet in the same list.
4. **AI-agent disclosure expanded** (para. 31): agents disclose their artificial nature **and the person on
   whose behalf they act**, at key steps and at every new interaction.

## Code of Practice on Transparency of AI-Generated Content

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **Code of Practice — policy page** | **Final (10 Jun 2026); voluntary; ASSESSED AS ADEQUATE** by the Commission and the AI Board | `https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content` | 2026-08-04 | Covers only **50(2), 50(4), 50(5)**. **Supersedes** the "adequacy assessment pending / signatures conditional" framing. Adequacy makes it a recognised means to *demonstrate* compliance (Art. 50(7); Guidelines §8.1) — **not** a presumption of conformity, **not** conclusive evidence. ~190 signatories by end-Jul 2026; the **initial**-signatory deadline of 22 Jul 2026 has **passed**, but signing remains open. |
| **Code of Practice — full text (PDF)** | Final text | `https://ec.europa.eu/newsroom/dae/redirection/document/129555` | 2026-08-04 | Authoritative wording for the two-layer marking rule, the 200-token text threshold, detection, and Section 2 labelling. All of these are the **Code route**, never the statutory floor. |
| **Signing the Code — FAQ + signature form** | Live | `https://digital-strategy.ec.europa.eu/en/faqs/signing-code-practice-transparency-ai-generated-content` · form DOCX `https://ec.europa.eu/newsroom/dae/redirection/document/129548` | 2026-08-04 | Sign Section 1 (providers) and/or Section 2 (deployers) — whole sections, not individual commitments. Check the **published signatory list** rather than quoting a deadline. |

## EU labelling icon set (Code Section 2, Annex 1)

| Source | Status | Official URL | Last checked | Notes |
|--------|--------|--------------|--------------|-------|
| **EU Icons for labelling AI-generated content** | Published (technical best practice; **optional**) | `https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content` | 2026-08-04 | **Three icons** — *Basic*, *Fully AI-Generated*, *Partially AI-Modified* — each in **4 variations**. Icons are optional and **do not establish compliance by themselves**. A task force will add an **audio** version + interactive second layer. |
| **Icon assets** | Downloadable | SVG `https://ec.europa.eu/newsroom/dae/redirection/document/129546` · PNG `https://ec.europa.eu/newsroom/dae/redirection/document/129547` | 2026-08-04 | Freely usable without attribution; non-signatory use is not a signal of adherence. |

## Secondary commentary (persuasive, not authoritative)

| Source | Status | URL | Last checked | Notes |
|--------|--------|-----|--------------|-------|
| Bird & Bird — "Commission adopts final Art. 50 Guidelines: first impressions" (Jul 2026) | Law-firm insight | `https://www.twobirds.com/en/insights/2026/european-commission-adopts-final-guidelines-on-ai-act-article-50-transparency-obligations-first-impr` | 2026-08-04 | Flags the generation-date shift as a deliberate departure from the draft. |
| Bird & Bird — "The Final Transparency Code of Practice" (22 Jun 2026) | Law-firm insight | `https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-the-final-transparency-code-of-practice` | 2026-08-04 | Source for the 200-token rule, single-layer exceptions, detection-fee nuance, third-icon reading, GENERATED/MODIFIED copyright sensitivity. |
| Bird & Bird — "Reading the Commission's **draft** Art. 50 Guidelines" (15 May 2026) | Law-firm insight (**superseded**) | `https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-reading-the-commissions-draft-article-50-guidelines` | 2026-08-04 | **Historical only.** Its machine-translation and paragraph-numbering points no longer hold — see the map above. |

---

## What still needs a live check on activation

1. **Any revision of the Guidelines** — the Commission committed to updating them with practical experience
   (para. 155). Check for a version later than 20 Jul 2026.
2. **First enforcement / national practice** — market-surveillance activity and any national guidance;
   Art. 50 is now applicable law, so enforcement, not legislation, is the live variable.
3. **CJEU** — still zero rulings on Art. 50; the first reference would move several case-by-case tests.
4. **Signatory list growth** — as major providers converge, the Code becomes the de-facto standard.
5. **Icon task-force additions** — audio icon + interactive second layer.
6. **50(2) standardisation** — any harmonised standard or implementing act on machine-readable marking.
