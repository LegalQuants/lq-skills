# EU AI Act — Article 50 Transparency Assessor

A focused assessment of the **Article 50 transparency duties** of the EU AI Act (Regulation (EU)
2024/1689): which of the five duties (50(1)–(5)) bind a provider or deployer, what exactly must be
implemented, by when, and the penalty exposure — delivered as a lead-with-the-bottom-line answer plus,
on request, a formal mini-report and a per-obligation compliance checklist.

## When to use

Use this skill when the Art. 50 transparency questions are the ones that actually matter: an AI
**chatbot disclosure** (50(1)), **synthetic-content marking / watermarking** of AI-generated audio,
image, video or text (50(2)), an **emotion-recognition or biometric-categorisation notice** (50(3)),
**deepfake or public-interest-text labelling** (50(4)), or "what must we implement under Art. 50 and by
when?". It handles the German framing too — **Kennzeichnungspflicht / Transparenzpflichten**.

It assumes the AI-system / risk-tier and role questions are already settled (or takes them as given);
for breadth-first "does the AI Act apply and at what tier?" triage, that is a different, upstream job.

## How it works

1. **Pick a mode** — Quick triage (which duties bite + earliest deadline), Full assessment (mini-report
   + checklist + portable block), or Implementation plan (what to build per duty). It leads with the
   light answer, not a wall of report.
2. **Intake, one question at a time** — what the system does, which modalities it generates, whether it
   interacts with people, the provider/deployer role, and the **EU market-placement date** (which drives
   the 50(2) legacy-grace logic). It echoes the facts back before analysing.
3. **Role → trigger → exception** — splits the duties by role (provider owes 50(1)/(2); deployer owes
   50(3)/(4)), then for each duty applies the trigger test and the obviousness/exception test, gated by
   the Art. 5 prohibition where relevant.
4. **Implementation + dated roadmap** — the three marking tiers (statutory floor vs the Code's layered
   route), the official EU labelling icons, notice content, and the 22 Jul 2026 / 2 Aug 2026 / 2 Dec
   2026 / 2 Feb 2027 anchors.
5. **Output** — a bottom-line block, a readiness indicator, a "facts I'm relying on" echo, and a
   one-line source-status; then, on request, the mini-report, the per-obligation checklist, and a
   portable compliance block.

Every material statement is tagged **[Settled law] / [Official guidance] / [Best practice] / [Open issue]**
so you can see how firm it is. It prompts a quiet web-check on activation because the Art. 50 Guidelines
are still draft and the Digital Omnibus legacy-marking grace is awaiting Official Journal publication.

It is **self-contained**: where it points to a companion skill (a full role analysis, a consolidated
report), that is a pointer to the author's wider suite — not a dependency.

## Worked example

See [`examples/ai-act-transparency-worked-example.md`](examples/ai-act-transparency-worked-example.md)
for a full run: an EU SaaS **provider** launching a support chatbot plus a marketing-image generator
(intake → role → 50(1)+50(2) triggers → marking tiers → dated roadmap → bottom line + portable block).

## Reference material

In [`references/`](references/), loaded on demand: `art50-duties.md` (the five duties + penalty band),
`obviousness-and-exceptions.md` (the trigger/exception tests), `code-of-practice-final.md` (the June
2026 Code and the three marking tiers), `eu-labelling-icons.md` (the official EU icon set + the "AI"
acronym rules), `commission-guidelines-art50.md` (the final Guidelines paragraphs),
`timeline-and-grace.md` (dates + the Digital Omnibus as enacted), `implementation-checklists.md` (per-role
action items), `report-template-art50.md` (the mini-report / checklist / portable-block formats), and
`sources.md` (the live source manifest + uncertainty tiers).

## Installation

Copy the `ai-act-transparency/` folder into your skills directory (e.g.
`~/.claude/skills/ai-act-transparency/`). It auto-triggers on "Art. 50 transparency obligations", "do we
need to label AI content / deepfakes", "AI chatbot disclosure", "synthetic content marking /
watermarking", "Kennzeichnungspflicht", "Transparenzpflichten", and similar.

## Limitations

This is **structured analysis, not legal advice and not a compliance decision**. It does not run the
full risk-tier or role analysis (it takes them as given and flags Art. 5 / high-risk / Art. 25 edge
cases rather than deciding them), does not invent citations (thin inputs are marked `[UNCLEAR]` or
`[Open issue]`), does not certify compliance, and reports the Art. 99 statutory **maxima** (Tier 2 —
€15M / 3%) for context, not a prediction of actual fines. Because the Commission may revise the final Guidelines and
enforcement practice is only now developing, it prompts a live web-check on activation. See the
**"What this skill does not do"** section in `SKILL.md`.

## License

Apache-2.0 — see [LICENSE](LICENSE). Authored by Oliver Schmidt-Prietz.

---

*More EU regulatory skills (GDPR, EU AI Act, Data Act, NIS2, and more) →
[github.com/oliverschmidtprietz](https://github.com/oliverschmidtprietz)*

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
