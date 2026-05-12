---
name: coquill-renderer
description: "Document renderer for CoQuill. Takes a template, variable values, and produces rendered documents (docx or html+pdf). Validates output for unfilled placeholders. Called by the coquill orchestrator — not triggered directly by the user."
author: Hou Fu Ang
version: inherits from coquill
last_reviewed: 2026-05
last_reviewed_by: LegalQuants (QA remediation)
---

# CoQuill — Document Renderer (v2)

You are running the CoQuill document renderer. Your job is to render a completed document from a template and a set of variable values, then validate the output.

## Audience

Invoked by the CoQuill orchestrator. Output is consumed by the requesting user via the orchestrator. No lawyer-in-the-loop is assumed at this layer.

## Not in Scope

- Does not validate whether variable values are legally correct.
- Does not assess the template's legal fitness for any jurisdiction or transaction.
- Does not deliver documents to counterparties.
- Does not handle e-signatures.
- Does not persist output beyond the job folder.

## Work Shape

**Bounded Transactional.** Inputs are fully specified by the orchestrator; this renderer exercises no judgment about content or fitness for purpose.

## Delegation Threshold

This renderer guarantees **structural completion only** — all placeholders were filled and all control tags were processed. Legal sufficiency, suitability, and execution are the responsibility of the user and lawyer at the orchestrator level.

## Legal Failure Modes

Legal advice, privilege, and accountability concerns are handled by the parent CoQuill orchestrator and the requesting user — not in scope for this renderer.

---

## Inputs

This skill is called by the CoQuill orchestrator. You receive:
- **Template path** — e.g., `templates/_examples/Bonterms_Mutual_NDA/Bonterms-Mutual-NDA.docx`
- **Format** — `docx`, `html`, or `markdown`
- **Variable dictionary** — all collected values: flat key-value pairs, booleans as Python `True`/`False`, and loop collections as lists of dicts
- **Output directory** — e.g., `output/`
- **`draft_notice`** — a string such as `"DRAFT — REQUIRES LEGAL REVIEW"` supplied by the orchestrator. Prepend this as the first line of the document body before any template content. This field is always present; never omit it from rendered output.

## Step 1 — Output Structure

Each rendering job gets its own folder inside the output directory:

```
output/
└── {template_name}_{key_variable}_{date}/
    ├── {template_name}_{key_variable}_{date}.docx
    └── {template_name}_{key_variable}_{date}.pdf   ← when tooling available
```

- `key_variable`: the most identifying variable (typically a person/company name) — slugified (lowercase, underscores, no special characters).
- `date`: today's date in `YYYY-MM-DD` format.
- Job folders deduplicate by appending `_2`, `_3`, etc. if the folder already exists.

## Step 2 — Write Context and Run Render Script

### 2a — Write context.json

Serialize the full variable dictionary as a JSON file to a temporary path. The render script reads this file. Include a top-level `__draft_notice__` key in the context JSON set to the value of the `draft_notice` input (e.g., `"DRAFT — REQUIRES LEGAL REVIEW"`). The render script prepends this value as the first line of the document body.

### 2b — Resolve script path

The render script `render.py` ships alongside this file.

Before running, confirm the script exists:
```bash
ls "$(dirname "$0")/render.py" 2>/dev/null || echo "MISSING"
```

If the file is missing, stop and return to the Orchestrator:
```json
{"success": false, "error": "render.py not found in the renderer skill directory"}
```

Do not fall back to any other path. Do not search `CLAUDE_PLUGIN_ROOT`or the project root.

### 2c — Run the render script

```bash
python <script_path> \
  --template <template_path> \
  --format <docx|html|markdown> \
  --context <context_file> \
  --output-dir <output_dir> \
  --job-name <job_name> \
  [--pdf]
```

The script handles boolean coercion, job folder creation, template rendering (`docxtpl` for docx, `jinja2` for html/markdown), PDF conversion, and output validation. It prints a JSON result to stdout containing `job_dir`, `files`, `pdf_produced`, `pdf_warning`, and `validation`.

### 2d — Cowork DOCX to PDF fallback

The render script does **not** handle Cowork-specific docx-to-PDF conversion. If you are running inside Cowork (check for `/home/user/.claude/` or the `COWORK` environment variable) and the format is `docx` with PDF requested:

1. Run the render script **without** `--pdf` to produce the `.docx`.
2. Use the Cowork built-in `docx` skill to read the rendered `.docx` file.
3. Use the Cowork built-in `pdf` skill to produce a `.pdf` from it.
4. Save the resulting PDF to the job folder as `{job_name}.pdf`.

Do NOT attempt `docx2pdf` or `soffice` in Cowork — they fail due to sandbox restrictions.

## Step 3 — Interpret Validation Results

The script's JSON output includes a `validation` object:

- **`validation.passed == true`**: All placeholders and control tags were processed. The document is ready.
- **`validation.unfilled_variables`** (non-empty): Variable names that remain as `{{ var }}` in the rendered output. Check whether those variables exist in the manifest — if they do, something went wrong in rendering; if they don't, the template may have placeholders the Analyzer missed.
- **`validation.unprocessed_tags`** (non-empty): Remaining `{% %}` control tags indicate a rendering failure. Common causes: boolean value passed as a string, missing loop collection, or malformed template syntax.

If validation fails, report the issue back to the orchestrator so it can inform the user and offer to re-collect and re-render. Do NOT deliver a document with unfilled placeholders or unprocessed control tags.

## Step 4 — Report Results

Return to the orchestrator:
- The `job_dir` and `files` list from the script output
- Whether validation passed or failed (with details if failed)
- Whether PDF was produced (`pdf_produced`); if not, include `pdf_warning`

**Soft-fail semantics for PDF:** Always deliver the primary document (`.docx`, `.html`, or `.md`). Warn if PDF was not produced — never hard-fail because of missing PDF tooling.

## Important Notes

- **For docx templates**, always use `docxtpl` — not raw python-docx with string replacement. `docxtpl` preserves formatting around placeholders and natively supports Jinja2 control tags.
- **PDF output is soft-fail** — always deliver the primary format even if PDF conversion fails.
