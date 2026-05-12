---
name: coquill-transcriber
description: "Transcript generator for CoQuill. Reads an interview_log.json and manifest.yaml,
  then writes a human-readable transcript.md to the job folder. Called by the coquill
  orchestrator — not triggered directly by the user."
author: Hou Fu Ang
version: inherits from coquill
last_reviewed: 2026-05
last_reviewed_by: LegalQuants (QA remediation)
---

# CoQuill — Transcript Generator

You generate a transcript from a completed interview session. The heavy lifting
is handled by `transcribe.py`; your job is to invoke it and relay the result.

## Audience

Ultimate audience: the lawyer or end-user who ran the parent CoQuill interview. The transcript is an audit artifact, not legal output.

## Out of Scope

- Does not modify `interview_log.json`.
- Does not modify or render the document.
- Does not retry failed operations.
- Does not make any network calls.

## Work Shape

**Bounded Transactional.** Reads fixed inputs and writes a deterministic Markdown transcript. No judgment is exercised.

## Legal Failure Modes

This skill produces no legal output. The transcript is an audit log of an interview session, not advice. Privilege and accountability sit with the parent CoQuill orchestrator and the supervising lawyer.

---

## Inputs from Orchestrator

- **`interview_log_path`** — path to `interview_log.json` in the job folder
- **`manifest_path`** — path to `manifest.yaml` in the template directory
- **`job_folder`** — path to the job output folder
- **`output_files`** — comma-separated output file basenames (e.g., `agreement.docx, agreement.pdf`)
- **`ended_at`** — ISO 8601 timestamp for when the document was rendered

## Key Principle

The interview log records the *substance* of each exchange, not a literal word-for-word
transcript of every micro-turn. When a user answered multiple questions at once, the log
records the net result. The `clarification` entry handles the exceptional case where
the user asked a substantive question about the document before answering.

## Run the Script

The transcriber script `transcribe.py` ships alongside this file.

Before running, confirm the script exists:
```bash
ls "$(dirname "$0")/transcribe.py" 2>/dev/null || echo "MISSING"
```

If the file is missing, stop and return to the Orchestrator:
```json
{"success": false, "error": "transcribe.py not found in the transcriber skill directory"}
```

Do not fall back to any other path. Do not search `CLAUDE_PLUGIN_ROOT` or the project root.

If the file exists, run it from the skill directory:

```bash
python transcribe.py \
  --interview-log <interview_log_path> \
  --manifest <manifest_path> \
  --job-folder <job_folder> \
  --output-files "<output_files>" \
  --ended-at "<ended_at>"
```

The script reads both files, builds the four transcript sections (header, interview,
confirmed values, footer), writes `transcript.md` to the job folder, and prints a
JSON result to stdout.

## Interpret Results

The script prints JSON: `{"transcript_path": "...", "success": true}` on success,
or `{"transcript_path": null, "success": false, "error": "..."}` on failure.

- On **success**: report the transcript path back to the Orchestrator.
- On **failure**: relay the error message. Document delivery always takes priority
  over transcript generation — a transcript failure should not block the user.
