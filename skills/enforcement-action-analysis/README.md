# Enforcement Action Summary

A reusable LQ.AI skill that reads a single U.S. government enforcement document and produces a structured, citation-backed summary — parties, conduct, statutory basis, penalties, and resolution — in a consistent format for compliance and investigations work.

## What it does

Point it at one enforcement document (a DOJ DPA, an OFAC settlement, an SEC order, a BIS charging letter, a FinCEN consent order) and it extracts the substance into eight scannable sections, citing the source page for every item. It distinguishes what is *alleged* from what is *admitted* from what is *adjudicated*, and it flags what the document leaves unresolved rather than guessing.

It extracts and organizes only. It does not draw legal conclusions beyond the source, and it does not pull in outside facts.

## Who it's for

In-house compliance, ethics, and investigations professionals — and outside counsel — who read a steady stream of enforcement actions and want a consistent structured read instead of re-deriving the same summary by hand each time.

## Installation

Save the skill folder into your LQ.AI skills directory:

```
skills/
└── enforcement-action-analysis/
    ├── SKILL.md
    ├── README.md
    ├── LICENSE
    └── evals/
        └── evals.json
```

LQ.AI will surface the skill when your chat matches its trigger conditions (see `SKILL.md` → *When to Use*).

## Usage

Attach the skill and give it one enforcement document, then ask for a summary:

- "Summarize this enforcement action."
- "Pull the key facts, statutes, and penalty terms out of this DPA."
- "Give me a structured read of this OFAC settlement."

The output is a markdown summary with these sections: **At a Glance · Parties & Instrument · Conduct & Allegations · Statutory & Regulatory Basis · Penalties & Resolution · Compliance Observations · Aggravating / Mitigating Factors · Open Questions / Not Addressed.**

See `SKILL.md` for a hypothetical example.

## Scope and legal use

Designed for **public** enforcement documents; summaries of those are non-privileged and shareable. If applied to internal or matter-specific material, the output inherits the privilege of its inputs — label before sharing. Output is a **draft for attorney review**, not legal advice. See `SKILL.md` → *Scope and Legal Use*.

## Evals

`evals/evals.json` contains representative test prompts in the Anthropic `skill-creator` format. Each pairs a realistic request with a description of the expected extraction. Run the skill with and without it on the referenced document types and confirm the output matches.

## License

Apache 2.0 — see `LICENSE`.

## Author

Andrea Ren.
