# Commission Guidelines on Article 50 (Final, 20 July 2026) — Reference

The Commission's **Guidelines on the implementation of the Article 50 transparency obligations** are the
**broad** interpretive instrument: issued under **Art. 96(1)(d)** AI Act, they set out the Commission's
interpretation of Art. 50 for providers, deployers, and competent authorities across the **full scope of
all four duties** (the key difference from the Code, which only covers 50(2)/(4)/(5)).

**Status (checked 2026-08-04): FINAL.** The **51-page, 155-paragraph** text was adopted and published on
**20 July 2026**, together with the Communication approving it. It **supersedes** the 8 May 2026 draft
(consultation closed 3 Jun 2026) and the March 2026 first draft. **All paragraph numbers in this skill are
final-Guidelines numbers** — the draft numbering is superseded and must never be re-cited. A draft→final map
and the four substantive (non-cosmetic) changes are in [sources.md](sources.md).

**Legal weight:** explicitly **non-binding**. Only the **CJEU** can give an authoritative interpretation of
Art. 50, and it has not yet ruled. Treat the Guidelines as authoritative-in-practice interpretive guidance
that market-surveillance authorities and the AI Office are likely to follow, while flagging that the
Commission itself will **revise them** as experience accrues (para. 155).

---

## Interpretive moves practitioners should know

### 1. The "obvious" exemption (50(1)) → restrictively read, average-consumer benchmark
The Guidelines benchmark "obvious from the circumstances" against a **reasonably well-informed, observant and
circumspect** natural person (para. 43) and state the exception "**should be interpreted restrictively**"
because it deprives people of the right to be informed (para. 45). Critically: **general public awareness that
chatbots and agents exist does not mean people recognise them in a given interaction**. Factors (para. 45):
anticipated nature of the interaction (a genuine human-sounding voice or a human profile picture *decreases*
obviousness; visible mechanical components *increase* it), and audience composition — a professional-only
audience can support obviousness, but where **vulnerable persons** (children, elderly, cognitive/physical
disabilities, low AI literacy) may access the system, **the exception cannot be relied on at all**.
(Operationalised in [obviousness-and-exceptions.md](obviousness-and-exceptions.md) §1.)

### 2. AI agents → disclose the artificial nature *and the principal* (para. 31)
AI agents fall under 50(1) if they can interact with the people instructing them **or** with other natural
persons while executing tasks (bookings, correspondence, negotiating or concluding contracts, purchases).
They must disclose **both** their artificial nature **and the person on whose behalf they are acting** —
the Guidelines tie this to delegation of authority and accountability. This extends to **multi-agent
architectures** where another agent is the one facing the human. Where the provider **cannot reliably
determine in advance** whether the agent will meet a natural person, the agent must be designed *at the
architecture level* to self-disclose in **every reasonably likely** interaction. Agents must also disclose to
the **instructing** person at **key steps** (authorisation, reporting, validation — including when consuming
another AI system's output rather than a human's) and **at every new interaction**. This goes **further than
the Act itself**, which does not use the word "agent".

### 3. No retrospective marking — but the trigger is the date of **generation** (para. 154)
50(2) outputs and 50(4) first-subparagraph **deepfakes generated or manipulated before 2 August 2026** do
**not** need to be marked or labelled retroactively. **Public-interest text is different**: it escapes only if
it was **AI-generated *and* published** before 2 Aug 2026 — text generated before that date but **published on
or after** it **must be labelled**. Holders/disseminators of pre-existing unlabelled deepfakes are
**encouraged** to label voluntarily, but are **not expected to make disproportionate efforts** (no auditing of
pre-existing content databases, no reprinting of packaging).

> **v1.2 correction:** earlier versions of this skill keyed this rule on *publication*. That is wrong for
> images/audio/video and only accidentally right for text. Use the generation-date rule above.

### 4. Penalty band — correct the common error (para. 152)
Non-compliance with Art. 50 sits in the **second-highest** fine band: up to **EUR 15,000,000 or 3% of total
worldwide annual turnover, whichever is higher** (**EUR 750,000** for EU institutions/bodies; for **SMEs and
start-ups**, whichever is **lower**). The precise hook is **Art. 99(4)(g)**. If you see **€35M / 7%** cited
for Art. 50, that is **wrong** — that band is reserved for Art. 5 prohibited practices.

### 5. Horizontal findings
- **"Mere distribution" stays outside** (para. 16): hosting services, **online platforms** and **broadcasters**
  whose role is limited to disseminating or transmitting third-party AI content, or who lack authority over
  the AI's use, are **not deployers**. They are nonetheless *encouraged* to preserve existing marking and
  labelling. **But** a VLOP/VLOSE using an AI system under its own authority for its own professional
  purposes (e.g. creating marketing visuals) **is** a deployer (para. 126).
- **Personal-use carve-out is narrow** (para. 19): Art. **2(10)** requires the person to act in **both** a
  personal **and** a non-professional capacity. Regular economic benefit, or any professional/business/trade/
  freelance involvement, defeats it — as does acting under a professional deployer's authority.
- **FOSS does not help** (para. 24): open-source systems remain fully subject to Art. 50.
- **Art. 50/Art. 53 layering** (para. 27): Art. 50 attaches at the **AI-system** layer; Art. 50 does **not**
  apply to GPAI **models** as such. Where the system and model share a provider, the measures *may* be
  implemented at model level; other model providers are **encouraged** to do so to help downstream system
  providers. For models with systemic risk, model-level measures may form part of **Art. 55(1)(b)** mitigation.

### 6. Art. 50(2) scope — what the Guidelines pull IN and carve OUT
- **Not GPAI-specific** (paras. 57–58): **any** AI system generating synthetic audio/image/video/text is
  captured — narrow single-purpose generators, multi-purpose systems, **GPAI systems**, and **agentic systems**
  alike. Manipulation of existing content counts as well as generation (para. 59).
- **⚠ Machine translation is now OUT** (para. 92): "AI-generated translations of text" appears in the
  **standard-editing** example list. This **reverses the draft**, which had named a translation engine as an
  in-scope example. A translation that materially changes meaning, style or intent can still fall back in, but
  do **not** assert that translation engines owe 50(2) marking as a general rule.
- **Content outside scope** (paras. 64–68): simple data processing (e.g. a rendered frame); output that
  **merely reproduces, presents or arranges existing content** — music playlists, recommender systems,
  internal analytics that extract and structure data (para. 65); mere observations/recordings from physical or
  virtual environments and unaltered data transmissions (para. 66); and the para. 68 list —
  **short sequences** of numbers/symbols/letters (single words, image captions, alt-text, UI labels,
  icon-scale graphics); **source code**; **machine-to-machine-only** outputs; and **closed-loop industrial /
  product-development** outputs (e.g. film production) **unless they are the final output**.
- **Source code is exempt in the broad sense** (para. 68): content in a programming, scripting, markup, query
  or configuration language intended to be interpreted, compiled or executed — *regardless of whether it is
  composed of text characters* — plus natural-language **comments and contextual information integral to the
  code**, and expressly **SDKs, SQL, IaC, YAML, JSON configuration, schemas, scripts, machine-readable
  specifications, APIs and software libraries**. It is a **standalone** exclusion, **not** a subset of the
  machine-to-machine bullet. Standalone documentation generated separately (README prose, marketing copy) is
  ordinary text and **re-enters** 50(2).
- **Marking AND detection — both, or neither counts** (paras. 69–70): the duty has two "distinct but
  inherently interlinked" elements. For **every** marking solution deployed, corresponding **means for
  detection** must be available. Fulfilling only one "**will not suffice**". A marking-only compliance story
  is not partial compliance — it is non-compliance.
- **B2B/industrial is narrower than it sounds** (para. 87): **cumulative** conditions — output *strictly
  technical* (engineering designs, industrial workflows, technical instructions, predictive-maintenance
  output), excluding public- and consumer-facing systems, with safeguards against reasonably foreseeable
  misuse. "We only use it internally" is not enough on its own.
- **Ephemeral real-time generation** (para. 88): content generated and consumed immediately in video games or
  VR, **not recorded, stored or disseminated**, may be exempt **where marking is not technically feasible
  *and*** people exposed are made aware it is AI-generated (in-experience disclosure, session-level notice).
  Conditional, not a blanket gaming carve-out.

### 7. Art. 50(1) — the negative catalogue (para. 38)
The Guidelines give an unusually explicit list of what, **used alone**, does **not** satisfy 50(1)/50(5):
- disclosures only in **T&Cs, URLs or documentation** (these may *complement*, never *replace*, in-context
  disclosure);
- **machine-readable markings** not perceivable at the point of interaction (still fine for 50(2));
- **unclear or ambiguous signals** — generic references to an "**assistant**", or human-like representations
  that may mislead;
- **generalised, non-specific** disclosures — e.g. "Services on this website use AI" on a multi-service
  platform;
- **technical or capability-based descriptions** — "this system uses LLMs".

Several are common practice today, so 50(1) requires an *active redesign* of disclosures, not maintenance.

### 8. Art. 50(3) — broader than the high-risk lens
Two points: (a) unless the use is **prohibited under Art. 5(1)(g)**, 50(3) applies to **any** biometric
categorisation system — expressly **age or gender classification from biometric data** — **regardless of
whether it is high-risk** (para. 104); (b) the notice's **content** is narrow: deployers must say that people
are **exposed to** an operating emotion-recognition or biometric-categorisation system. The AI Act does **not**
require explaining the reasons for operating it or other processing purposes — those obligations come from
**Union data protection law** (para. 105). Inferring **race/ethnicity** is a *prohibited* Art. 5(1)(g)
categorisation, not a 50(3)-notice case.

### 9. Art. 50(4) — the four-criteria deepfake test
The Guidelines unfold Art. 3(60) into **four cumulative criteria** (para. 113): **(i) resemblance** —
"appreciable" per Recital 134, a high level of similarity assessed objectively case-by-case by the deployer;
**(ii) existing** — it suffices that the subject **exists, can plausibly exist, or could have plausibly
existed**, so photorealistic invented persons are in and physics-defying content (dragons, elephants driving
cars) is out; **(iii) persons/objects/places/entities/events** — including digital replicas, realistic
AI-generated avatars and personas, and personal characteristics such as voice, behaviour or performances;
**(iv) false appearance of authenticity or truthfulness** — assessed **as a whole and objectively**, against
the **intended and reasonably foreseeable audience** and deployment context, with **no requirement of intent
to deceive** (para. 114).

> **Do not "simplify" this to three criteria.** The Commission FAQ presents three by merging (ii) and (iii);
> the Guidelines themselves say four. Use four — the merged form loses the plausibly-could-exist test that
> decides invented-person cases.

Cosmetic or minor manipulation generally does **not** create a deepfake — background tidying, lighting, colour
correction, noise removal, compression, accessibility improvements, re-scaling in product ads and packaging —
but **substantial AI editing of journalistic images beyond standard editorial practice** can (para. 116).
The **"evidently" artistic/creative/satirical/fictional** limb excludes content whose nature is **exclusively
informative or commercial and recognisable as such** (para. 122); where it applies it **attenuates the form**
of disclosure only — the duty to disclose **survives** (para. 123) — and personality, IP and data-protection
rights continue in full (Recital 134; para. 124). Full operational test in
[obviousness-and-exceptions.md](obviousness-and-exceptions.md) §3.

---

## How the two instruments divide the work

| | Commission Guidelines | Code of Practice |
|---|----------------------|------------------|
| Legal basis | Art. 96(1)(d) | Art. 50(7) |
| Drafted by | The Commission | Independent experts (AI Office process) |
| Scope | **All** of 50(1)–(5) | **Only** 50(2), 50(4), 50(5) |
| Status (2026-08-04) | **Final** (20 Jul 2026, 155 paras.) | **Final** (10 Jun 2026), **assessed as adequate** by Commission + AI Board |
| Binding? | No (CJEU authoritative; but MSAs/AI Office likely to follow, divergence must be justified) | No (voluntary; adherence ≠ conclusive evidence, ≠ presumption of conformity) |
| Reach | Everyone in scope | Signatories (a compliance-demonstration vehicle); non-signatories bear the burden of showing an equally effective/interoperable/robust/reliable route |

Use the **Guidelines** for interpretation across the whole of Art. 50 (especially 50(1)/50(3), which the
Code does not touch); use the **Code** ([code-of-practice-final.md](code-of-practice-final.md)) for the
*how* of 50(2) marking and 50(4) labelling.

### Where they diverge — model-level marking
The clearest divergence is **upstream (GPAI model-level) marking**. The **Guidelines** merely *encourage*
GPAI model providers to implement marking at the model level, even where they fall outside Art. 50
(para. 27) — a "strongly suggested best practice". The **Code** treats model-level marking as a
**commitment for its signatories** (Measure 1.1.2). So a GPAI model provider that is **not** a Code signatory
can rely on the softer Guidelines wording — creating a dependency for downstream system providers, who still
owe 50(2) on their own outputs. Neither instrument makes this an **Art. 53** duty (Art. 53(1)(d) is the
training-data summary — a frequent mis-citation to correct).
