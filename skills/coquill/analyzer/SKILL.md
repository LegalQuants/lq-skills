---
name: coquill-analyzer
description: "Template analyzer for CoQuill (v2). Parses docx/HTML templates, extracts variables including conditionals and loops, merges config.yaml overrides, infers types, and generates a v2 manifest.yaml. Called by the coquill orchestrator — not triggered directly by the user."
author: Hou Fu Ang
version: inherits from coquill
last_reviewed: 2026-05
last_reviewed_by: LegalQuants (QA remediation)
---

# CoQuill — Template Analyzer v2

You are running the CoQuill template analyzer. You receive a **template directory path** from the Orchestrator (e.g., `templates/_examples/Bonterms_Mutual_NDA/`).

## Audience

**Caller:** CoQuill Orchestrator. **Human downstream:** template authors (legal engineers building reusable contract templates), not end-user lawyers.

## Out of Scope

- Not a legal review — does not assess whether the template's clauses are legally correct or jurisdictionally appropriate.
- Not a renderer — produces a manifest only.
- Not an interview designer — does not propose question wording or interview flow.
- Not a jurisdictional checker — operates on template structure only.

## Work Shape

**Bounded Transactional** — script-driven extraction with rule-based post-validation. No legal interpretation is performed.

## Delegation Threshold

Warnings from Step 2 require human acknowledgement at the Orchestrator level before rendering proceeds. This analyzer never green-lights a manifest on its own.

## Legal Failure Modes

This skill extracts placeholder structure only. It does not validate whether the template's clauses are legally correct or jurisdictionally appropriate — that responsibility sits with the template author and supervising counsel.

---

## Inputs

The Orchestrator passes a single argument: `template_dir` — the path to a template directory.

**Required:** exactly one template file (`.docx`, `.html`, or `.md`) must be present in `template_dir`. Before running the script, enforce the following:

- **No template file found** → halt immediately. Return `{"success": false, "error": "No .docx, .html, or .md file found in <template_dir>"}` to the Orchestrator. Do not run the script.
- **Multiple template files found** → halt immediately. Return `{"success": false, "error": "Multiple template files found in <template_dir> — Orchestrator must specify which one"}`. Do not run the script.
- **File exists but is unreadable or corrupt** → the script will exit 1 with a descriptive error. Relay the error message to the Orchestrator verbatim. Do not attempt recovery or fall back to a different file.

---

## Step 1 — Resolve Script Path and Run

The analysis script `analyze.py` ships alongside this file.

Before running, confirm the script exists:
```bash
ls "$(dirname "$0")/analyze.py" 2>/dev/null || echo "MISSING"
```

If the file is missing, stop and return to the Orchestrator:
```json
{"success": false, "error": "analyze.py not found in the analyzer skill directory"}
```

Do not fall back to any other path. Do not search `CLAUDE_PLUGIN_ROOT` or the project root.

If the file exists, run it from the skill directory:

```bash
python <script_path> <template_dir> [--force]
```

Pass `--force` if the Orchestrator requests re-analysis (skips the cache check).

The script handles: format detection, caching, text extraction (including docx XML merge), two-pass analysis, type inference, condition parsing, loop sub-variable extraction, dependency graph construction, config.yaml merge, and manifest save.

### Interpret Script Output

- **Exit 0** with `"Manifest is up to date"` — cached manifest is valid; load it from `<template_dir>/manifest.yaml`.
- **Exit 0** with `"Manifest written"` — fresh analysis complete; proceed to Step 2.
- **Exit 1** — error (e.g., no template file found, corrupt docx). Report the stderr/stdout message to the Orchestrator.

## Step 2 — Validate the Manifest

After a fresh analysis (not a cache hit), load `manifest.yaml` and check for issues the script cannot catch. Each check carries a **severity** and a prescribed **Orchestrator action**.

**🔴 HIGH — halt the Orchestrator (do not proceed to interview):**

1. **Zero variables** — `variable_count` is 0; the template has no placeholders. The file may be wrong or the template may need to be rebuilt. The Orchestrator must stop and inform the user.
2. **Orphaned gate variable** — a variable listed as a key in `dependencies` is absent from `variables`. The interview cannot collect the gate value; rendering will fail. The Orchestrator must stop and inform the user that the template has a configuration error.

**🟡 MEDIUM — flag and continue (log in `tool_use` entry, surface to user, do not halt):**

3. **Conditional variable shadowing unconditional** — the same variable name appears in both `variables` and a conditional's `if_variables`/`else_variables`. The script deduplicates at extraction time, but a `config.yaml` merge could reintroduce the conflict. Flag so the template author can investigate.
4. **Loop sub-variables with no names** — a loop's `variables` list is empty, so the loop collects nothing. May be intentional (iteration-only loop) or a sign of a non-standard loop variable pattern. Flag for the template author.

**🟢 LOW — cleanup hint only (mention in return value, do not log as warning, do not halt):**

5. **Config.yaml drift** — `config.yaml` references variable names that don't appear anywhere in the manifest. These are stale config entries the template author should remove. Do not block the interview.

**Halt list summary:** halt on checks 1 and 2. Pass through on checks 3, 4, and 5.

Report all findings alongside the manifest contents when returning to the Orchestrator, labelled by severity.

## Step 3 — Return to Orchestrator

Return the full `manifest.yaml` contents to the Orchestrator, along with any warnings from Step 2.
