# Obviousness Test, Exceptions & Boundaries — Reference

Every Art. 50 trigger has a release valve — an obviousness exemption (50(1)), an assistive-function
exemption (50(2)), or a set of narrow exceptions (50(4)). This file collects them in one place, plus
the boundary analysis for "is my use case in scope at all?" and the interactions with other AI Act
provisions.

---

## 1. The 50(1) "obvious" exemption — average-consumer benchmark

50(1) does not apply where it is **obvious**, from the circumstances and context of use, that the
person is interacting with an AI system. The final Commission Guidelines benchmark "obvious" against
a **reasonably well-informed, observant and circumspect** person (para. 43) and instruct that the exception
"**should be interpreted restrictively**", because it deprives people of the right to be informed (para. 45).
Two framings to carry into every assessment: **general awareness that chatbots and agents exist does not mean
a person recognises one in the interaction in front of them**, and where **vulnerable persons may access the
system, the exception cannot be relied upon at all**. Applied through a **multi-factor test**:

| Factor | Effect on "obviousness" |
|--------|-------------------------|
| **Context of use** | A clearly labelled "AI assistant" widget is more obviously AI than an unbranded chat window |
| **Target audience** | Adjust for **vulnerable groups** (children, elderly, cognitively impaired) — what is obvious to an average adult may not be |
| **AI literacy** | Lower assumed literacy → higher disclosure burden |
| **Realism of the interaction** | A human-sounding voice agent that never self-identifies is *less* obviously AI, not more |

**Examples the Guidelines treat as plausibly "obvious" (disclosure may not be required):**
- developer-only code assistants used by professional engineers who know they are using an AI tool;
- non-player characters (NPCs) in a video game, where the fictional/game context makes AI nature obvious.

**Default when uncertain:** disclose. The exemption is narrow; the burden of showing obviousness sits
with the provider. For **AI agents** the default is stronger still (para. 31): disclose the artificial nature
**and the person on whose behalf the agent acts**, in every reasonably-likely human-interaction situation
where the provider cannot determine exposure in advance, to the **instructing** person at key steps
(authorisation, reporting, validation) and **at every new interaction** — including in multi-agent chains
where a *different* agent is the one facing the human.

---

## 2. The 50(2) assistive-function exemption

The provider marking duty does **not** apply where the AI system:

- performs an **assistive function for standard editing** (spell-check, grammar, basic formatting,
  noise reduction, colour correction); **and**
- does **not substantially alter** the input data provided by the **deployer** or its semantics.
  *(The statute says "input data provided by the deployer" — a defined term, not "the user".)*

**Boundary test:** does the output constitute a *new creative work* or merely an *improved version of
the user's own work*? Generation (new text/images from a prompt) always requires marking. Refinement
(correcting typos, adjusting brightness) does not.

### Boundary analysis (marking/labelling required vs. out of scope)

| WITHIN SCOPE (mark/label) | OUT OF SCOPE | Distinguishing factor |
|---------------------------|--------------|-----------------------|
| AI-generated image from a text prompt | AI brightness/contrast enhancement | Creation vs. enhancement |
| AI voice clone synthesising speech | AI noise reduction on a real recording | Synthetic generation vs. quality improvement |
| AI-generated article published as news | AI spell-checker fixing typos | Substantial alteration vs. assistive function |
| AI face-swap video (deepfake) | AI stabilisation of genuine footage | Identity manipulation vs. technical improvement |
| AI music generated from scratch | AI mastering of a recorded performance | Generation vs. post-processing |
| AI rewrite that changes meaning | AI spell/grammar correction that keeps meaning | Semantic alteration vs. assistive fix |
| AI text that materially changes meaning, style or intent under cover of "translation" | **AI translation of existing text (out of scope)** | See the caution below — the final Guidelines moved this |

> **⚠ Caution — machine translation is now OUT of 50(2) scope. This REVERSED between the draft and final
> Guidelines.** The **draft** (para. 54) named "a translation engine" as an in-scope example of a
> single-purpose generative tool. The **final Guidelines (20 Jul 2026) list "AI-generated translations of
> text" among the examples of standard editing and minor alterations benefiting from the Art. 50(2)
> exception** (para. 92). So a translation engine does **not** owe 50(2) marking on the strength of being a
> translation engine.
>
> **What survives the reversal.** The exception is framed around output that does **not** change "the
> substance, meaning, style or messaging" of the text (para. 92), and editing goes beyond standard editing
> where content is changed "in a material way … that affect[s] its meaning, style or intent" (para. 90). So a
> system marketed as translation that also **transcreates, summarises, restyles, expands or localises
> substantively** is doing more than translating and can fall back in. Assess the *actual* transformation,
> not the product label.
>
> **If you advised a user under v1.2 of this skill that their translation engine owed 50(2) marking, that
> advice is superseded.** Say so plainly rather than quietly changing the answer.

### Gray-zone scenarios

1. **AI-assisted creative collaboration** — designer generates AI logo variants, then heavily modifies
   one. Marking required if the AI's contribution is still recognisable as the creative origin; the
   assistive exemption only applies if the human rework is so extensive the AI contribution is no longer
   recognisable (a high threshold).
2. **AI-restored old photographs** — inpainting (filling missing regions) generates new content → mark;
   pure upscaling leans assistive. Mixed restoration workflows → marking is the safer default.
3. **AI background behind a real presenter** — a realistic synthetic location may be a deepfake of a
   *place* (50(4)); an abstract/fantastical background likely is not, but the synthetic background
   component still needs provider 50(2) marking.
4. **Corporate AI writing assistant** — the AI generates text → provider 50(2) marking applies. Whether
   the *deployer* must also label depends on whether the output is a deepfake (usually not for routine
   business communication); the 50(4) human-review exception may apply to published text, but 50(2)
   provider marking still applies.

---

## 3. The 50(4) deepfake analysis — two steps, not one categorical rule

**Step 1 — Is it even a deepfake? Apply Art. 3(60) properly.** A deepfake is AI-generated or manipulated
**image, audio or video** content that "resembles **existing** persons, objects, places, **entities** or
events" **and** "would falsely appear … to be authentic or truthful." The final Guidelines (para. 113)
unfold this into **four cumulative criteria** — use all four as the test:

1. **Appreciable resemblance** (Recital 134) — a high level of similarity to the simulated subject,
   including its recognisable elements; **not** required to be identical. Case-by-case, assessed objectively
   by the **deployer**, on how far characteristic or distinctive features are reproduced;
2. **Existing** — it is enough that the subject **exists, can plausibly exist, or could have plausibly
   existed**. *Stylised/impossible* content is **out** (dragons, elephants driving cars, humans flying
   unaided — content that defies nature or physics and has no potential to mislead); a **photorealistic
   invented person or synthetic celebrity is IN**, because such a person plausibly could exist — working with
   a *fictional* likeness does not by itself escape the regime;
3. **Persons / objects / places / entities / events** — "persons" expressly includes **digital replicas of
   real people, realistic AI-generated avatars and personas**, and personal characteristics such as **image,
   voice, behaviour and performances**; "objects" includes buildings, artworks, machinery and consumer goods;
4. **False appearance of authenticity or truthfulness** — assessed **as a whole and objectively** (para. 114)
   against the level of resemblance, the substantive message, the intended and foreseeable **deployment
   contexts**, the presentation environment, and the **intended and reasonably foreseeable audience** and its
   expectations. **No intent to deceive is required.** Note the inverse: where the foreseeable audience does
   **not** expect the content to be authentic, criterion (iv) may fail *even though the content is in fact
   non-authentic*.

> **Do not compress this to three criteria.** The Commission FAQ merges (ii) and (iii) into one bullet; the
> Guidelines say **four**. The merged form is where the plausibly-could-exist test — the one that decides
> invented-person cases — gets lost.

Minor or cosmetic manipulation typically does **not** make content a deepfake — background tidying (removing
a passer-by), lighting, colour correction, noise removal, accessibility improvements, compression, cosmetic
enhancement; the Guidelines add that aesthetic background replacement, product composition and re-scaling **in
advertisements and packaging** are likely to have only minor impact on perceived authenticity. But
**substantial AI editing of journalistic images beyond standard technical and editorial practice can** create
a deepfake (para. 116).
Heuristic: *"stylised/impossible" or "minor technical adjustment" → outside; "photorealistic/plausible" or
"substantive edit" → inside.*

**Step 2 — If it is a deepfake, does an exception apply, and how much disclosure survives?** Then run the
table below. The exceptions **soften or remove the disclosure**, they do not change Step 1.

## 3a. The 50(4) exceptions

| Exception | Scope | Conditions |
|-----------|-------|------------|
| **Law enforcement / national security** | 50(4) second subparagraph | Authorised by a competent authority for a specific investigation; never a blanket exemption |
| **Artistic / creative / satirical / fictional / analogous** | 50(4) third subparagraph | An **attenuated**, not removed, duty (para. 123): the deployer still discloses the AI origin, but "in an appropriate manner that does not hamper the display or enjoyment of the work" — Recital 134 frames this as not hampering normal exploitation while maintaining the work's utility and quality. Placement may be in credits/description, timing at the end, format textual — but "appropriate" ≠ "hidden", and Art. 50(5) still applies. The Guidelines define each category: **artistic** (created for the purpose of art — music, film, visual arts), **creative** (involving creative choices; work driven mainly by functional or technical considerations is not), **satirical** (criticising society, politics, business or public figures through humour, irony, sarcasm, pastiche), **fictional** (imaginary but verisimilitudinous), **analogous** (sharing core expressive traits). **Exception is lost** when the content leaves its original artistic context (a satirical clip reshared without its framing must be labelled) |
| **Public-interest text — human review** | 50(4) fourth subparagraph | A natural person reviewed the content and bears editorial responsibility; the publisher assumes legal accountability. Applies **only to text** — audio/image/video deepfakes must always be labelled |

**Marketing has no blanket pass — but "never" is too strong.** The test is *not* "is it an ad?" but the
two-step analysis above plus the "**evidently** artistic/creative/fictional" threshold. Per the final
Guidelines (para. 122), the word "evidently" **excludes** content whose nature is **exclusively informative or
commercial and recognisable as such** (the example given is news reporting) — so a persuasive product spot
using a photorealistic synthetic spokesperson (a Step-1 deepfake: an invented-but-plausible person) must be
labelled. The Guidelines are explicit that **advertisements or documentaries** containing deepfakes **might**
count as evidently creative or fictional **in certain specific situations but not others** — the assessment is
case-specific. Their own worked examples of deepfakes that do **not** qualify as artistic/creative work:
a teleshopping-style video of simulated consumers demonstrating a product; AI-generated images of celebrities
implying involvement in events that never happened; a realistic synthetic influencer demonstrating a sponsored
real product. So:

- **Default for marketing deepfakes: full labelling.** A synthetic brand spokesperson in a normal ad is IN
  and gets no artistic pass.
- **Do not tell the user marketing categorically qualifies** for the exception — but equally, don't assert
  it can *never* apply; apply the "evidently creative/fictional + primarily-informative-not-commercial" test.
- The artistic carve-out, where it does apply, **softens the *form* of disclosure only** — personality
  rights, IP and data-protection duties continue in full (Recital 134; Guidelines paras. 123–124).

---

## 4. Interactions with other AI Act provisions

### 4.1 Art. 50 ↔ Art. 53 (GPAI) — a value-chain dependency, **not** an Art. 53 duty
**Get the legal hook right.** Art. **50(2)** binds providers of **AI systems**, expressly "**including
general-purpose AI systems**", and is **not GPAI-specific** (final Guidelines paras. 57–58 — which also bring
**agentic** systems expressly within 50(2)). It attaches at the
**AI-system layer**. Art. **53** attaches at the **model layer** and is a *different* set of duties —
notably **Art. 53(1)(d)**, which is the **training-data content summary** obligation (a "sufficiently
detailed summary about the content used for training"). **Art. 53(1)(d) does not require marking capability,
and there is no Art. 53 duty to comply with 50(2).**

What actually happens across the chain:

- A generative AI **system** that uses a GPAI **model** must itself mark its outputs under **50(2)**; the
  model provider separately satisfies its **model-level documentation** duties under Art. 53.
- Marking is easiest when built upstream, so the model provider is **encouraged** to implement marking at
  the model level (final Guidelines para. 27 — a "strongly suggested best practice"; for models with systemic
  risk it may also form part of **Art. 55(1)(b)** mitigation), and the **Code**
  expects this of its **signatories** (Measure 1.1.2). This is a **value-chain dependency / best practice**,
  not a black-letter Art. 53 obligation.
- Note the **divergence**: the Guidelines merely *encourage* model-level marking, while the Code treats it
  as a signatory commitment — so a non-signatory model provider may lean on the softer Guidelines wording
  and leave downstream system providers dependent on it. Flag that dependency to the user.

### 4.2 Art. 50 ↔ Art. 13 (High-Risk Transparency)
Art. 50 applies **on top of** Art. 13. Art. 13 = detailed technical transparency to professional
deployers; Art. 50 = public-facing disclosure of AI nature / provenance. A high-risk system that also
interacts with persons or generates content owes **both**.

### 4.3 Art. 50 ↔ Art. 5 (Prohibited Practices)
- 50(3) ↔ 5(1)(f): emotion recognition in workplace/education is prohibited; 50(3) disclosure cannot
  cure a prohibition — the Art. 5 violation takes precedence.
- 50(3) ↔ 5(1)(g): biometric categorisation for sensitive characteristics is prohibited; 50(3) only
  covers non-sensitive categorisation (e.g. age estimation).
- 50(1) ↔ 5(1)(a): concealing AI involvement to manipulate behaviour can trigger both a 50(1) breach
  and the Art. 5(1)(a) deception prohibition.

### 4.4 Art. 50 ↔ Open-Source Exemption
Art. 2(12) exempts certain free-and-open-source AI systems from most AI Act requirements — but **Art. 50
is explicitly excluded from that exemption** (final Guidelines para. 24 confirms FOSS remains fully subject
to Art. 50). Open-source chatbots (50(1)), image generators (50(2)), and voice/deepfake tools (50(2)/(4))
must still comply.

### 4.5 Personal-use carve-out (Art. 2(10)) — narrower than it reads
The "purely personal non-professional activity" exclusion in **Art. 2(10)** is narrow (final Guidelines
para. 19): "purely personal" **qualifies** "non-professional", so the person must act in **both** capacities.
Any activity yielding **regular economic benefit**, or any professional, business, trade, occupational or
freelance involvement, is professional — and anyone acting **on behalf of or under the authority of** a
professional deployer falls within that deployer's 50(3)/(4) duties. Treat "it's just personal use" with
suspicion whenever the output reaches a public audience or touches public debate.

### 4.6 "Mere distribution" is not deployment
An actor whose role is limited to **disseminating or transmitting** third-party AI-generated content —
expressly **hosting services, online platforms and broadcasters** — is **not a deployer** within Art. 50
(final Guidelines para. 16); they are nonetheless **strongly encouraged** to preserve any marking and
labelling already applied. The 50(4) labelling duty stays with the deployer that has authority over the AI's
use. **Two traps:** (a) a **VLOP/VLOSE is a deployer** for AI systems it uses under its own authority for its
own professional purposes — e.g. producing its own marketing visuals (para. 126); (b) a company that
**merely commissions** an agency to make an ad, without deciding or controlling whether and how AI is used, is
**not** a deployer (para. 14). Where many actors feed one brand or marketplace, uniformity is a
**contractual** question, not a statutory one.

### 4.7 50(2) scope exclusions from the final Guidelines (quick reference)
Detailed in [commission-guidelines-art50.md](commission-guidelines-art50.md); the boundaries a practitioner
hits most often:
- **Source code is exempt, broadly** (para. 68) — programming, scripting, markup, query and configuration
  languages, plus **SDKs, SQL, IaC, YAML, JSON config, schemas, machine-readable specifications, APIs and
  libraries**, and natural-language comments integral to the code. This is a **standalone** exclusion, **not**
  a subset of the machine-to-machine bullet. But **standalone docs** (README prose, marketing copy,
  natural-language explanations generated separately) are ordinary text and **re-enter** 50(2).
- **Short sequences** (para. 68): single words, image captions, alt-text, UI labels, icon-scale graphics.
- **Machine-to-machine-only outputs** (para. 68): processed automatically, never exposed to humans.
- **Closed-loop industrial / product-development** output (para. 68), e.g. film production — **unless it is
  the final output**.
- **Mere reproduction or arrangement of existing content** (para. 65): recommender systems and playlists that
  only select or rank, internal analytics that extract and structure data.
- **B2B/industrial is narrow** (para. 87): *strictly technical* output, **excluding** public- and
  consumer-facing systems, with safeguards against foreseeable misuse — **cumulative** conditions.
- **Ephemeral in-game / VR generation** (para. 88): real-time content consumed immediately and **not
  recorded, stored or disseminated**, **where marking is not technically feasible *and*** exposed persons are
  told it is AI-generated. Conditional — not a blanket gaming carve-out.
