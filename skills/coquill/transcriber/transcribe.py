#!/usr/bin/env python3
"""Codraft transcript generator.

Reads an interview_log.json and manifest.yaml from a completed document
assembly session, then writes a human-readable transcript.md to the job
folder.

Usage:
    python scripts/transcribe.py \
        --interview-log output/job/interview_log.json \
        --manifest templates/example/manifest.yaml \
        --job-folder output/job/ \
        --output-files "agreement.docx, agreement.pdf" \
        --ended-at 2026-03-01T12:00:00Z
"""

import argparse
import json
import os
import sys
from datetime import datetime

import yaml


# ---------------------------------------------------------------------------
# Timestamp formatting
# ---------------------------------------------------------------------------


def format_time(iso_str: str | None) -> str | None:
    """Extract a human-readable time-of-day from an ISO 8601 timestamp.

    Returns e.g. '12:03 PM', or None if the input is missing/unparseable.
    """
    if not iso_str:
        return None
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%-I:%M %p")
    except (ValueError, AttributeError):
        return None


# ---------------------------------------------------------------------------
# Value formatting
# ---------------------------------------------------------------------------


def format_value(value) -> str:
    """Format a value for display in the transcript.

    True/true -> Yes, False/false -> No, empty/None/null -> em dash.
    """
    if value is True or (isinstance(value, str) and value.lower() == "true"):
        return "Yes"
    if value is False or (isinstance(value, str) and value.lower() == "false"):
        return "No"
    if value is None or value == "" or (isinstance(value, str) and value.lower() == "null"):
        return "\u2014"
    return str(value)


# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------


def get_variable_label(manifest: dict, var_name: str) -> str:
    """Get the display label for a variable from the manifest.

    Falls back to title-casing the variable name (underscores to spaces).
    """
    variables = manifest.get("variables", [])
    if isinstance(variables, list):
        for var in variables:
            if isinstance(var, dict) and var.get("name") == var_name:
                return var.get("label", var_name.replace("_", " ").title())
    return var_name.replace("_", " ").title()


def has_conditionals(manifest: dict) -> bool:
    """Check whether the manifest defines any conditional groups."""
    conditionals = manifest.get("conditionals")
    return bool(conditionals)


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------


def derive_ended_at(entries: list, cli_ended_at: str) -> str:
    """Derive the session end time from the last entry's timestamp or completed_at.

    Walks entries in reverse to find the most recent timestamp. Falls back to the
    CLI-provided ended_at value.
    """
    for entry in reversed(entries):
        ts = entry.get("completed_at") or entry.get("timestamp")
        if ts:
            return ts
    return cli_ended_at


def build_header(
    session_start: dict, ended_at: str, output_files: str
) -> str:
    """Build Section 1 -- Header."""
    lines = [
        "# Document Assembly Transcript",
        f"**Template:** {session_start.get('template', '')}",
        f"**Request:** {session_start.get('request', '')}",
        f"**Start date/time:** {session_start.get('started_at', '')}",
        f"**End date/time:** {ended_at}",
        f"**Output:** {output_files}",
        "",
        "---",
    ]
    return "\n".join(lines)


def build_interview(entries: list, manifest: dict) -> str:
    """Build Section 2 -- Interview.

    Walks through log entries in order and renders each type.
    """
    show_conditionals = has_conditionals(manifest)
    lines = ["## Interview", ""]
    corrections = []
    prev_type = None

    for entry in entries:
        entry_type = entry.get("type")

        if entry_type == "prefill":
            lines.append("> *The following values were provided by the user before the interview began:*")
            for item in entry.get("values", []):
                label = item.get("label", item.get("name", ""))
                value = format_value(item.get("value"))
                lines.append(f"> - **{label}:** {value}")
            lines.append("")

        elif entry_type == "group_start":
            name = entry.get("name", "")
            branch = entry.get("branch")
            if not show_conditionals or branch is None:
                heading = f"### {name}"
            elif branch == "if":
                heading = f"### {name} *(included)*"
            elif branch == "else":
                heading = f"### {name} *(alternative)*"
            elif branch == "skipped":
                heading = f"### {name} *(skipped)*"
            else:
                heading = f"### {name}"
            lines.append(heading)
            lines.append("")

        elif entry_type == "question":
            ts = format_time(entry.get("timestamp"))
            prefix = f"**Q** *({ts}):*" if ts else "**Q:**"
            lines.append(f"{prefix} {entry.get('text', '')}")
            lines.append("")

        elif entry_type == "clarification":
            lines.append(f"> **User:** {entry.get('user_question', '')}")
            lines.append(f"> **Codraft:** {entry.get('claude_response', '')}")
            lines.append("")

        elif entry_type == "validation_retry":
            reason = entry.get("reason", "")
            lines.append(f"**Q (retry \u2014 {reason}):** *(re-asked)*")
            lines.append("")

        elif entry_type == "answer":
            ts = format_time(entry.get("timestamp"))
            prefix = f"**A** *({ts}):*" if ts else "**A:**"
            lines.append(f"{prefix} {format_value(entry.get('text', entry.get('value', '')))}")
            lines.append("")

        elif entry_type == "tool_use":
            tool = entry.get("tool", "")
            action = entry.get("action", "")
            ts_start = format_time(entry.get("timestamp"))
            ts_end = format_time(entry.get("completed_at"))
            if ts_start and ts_end:
                time_range = f" ({ts_start} \u2192 {ts_end})"
            elif ts_start:
                time_range = f" ({ts_start})"
            else:
                time_range = ""
            lines.append(f"> *Tool: {tool} \u2014 {action}{time_range}*")
            lines.append("")

        elif entry_type == "skip":
            # If immediately after a group_start with branch "skipped", it's already
            # represented by the heading annotation -- don't duplicate.
            if prev_type == "group_start":
                pass
            else:
                reason = entry.get("reason", "")
                lines.append(f"*{reason}*")
                lines.append("")

        elif entry_type == "loop_item":
            index = entry.get("item_index", "")
            lines.append(f"**Item {index}**")
            lines.append("")
            # Loop items may contain inline Q/A pairs
            if entry.get("question"):
                lines.append(f"**Q:** {entry['question']}")
                lines.append("")
            if entry.get("answer"):
                lines.append(f"**A:** {format_value(entry['answer'])}")
                lines.append("")

        elif entry_type == "correction":
            corrections.append(entry)

        prev_type = entry_type

    # Corrections sub-section
    if corrections:
        lines.append("### Corrections")
        lines.append("")
        for c in corrections:
            label = c.get("label", "")
            old_val = c.get("old_value", "")
            new_val = c.get("new_value", "")
            line = f"- **{label}** changed from `{old_val}` to `{new_val}`"
            if c.get("note"):
                line += f" *(Note: {c['note']})*"
            lines.append(line)
        lines.append("")

    return "\n".join(lines)


def build_confirmed_values(entries: list, manifest: dict) -> str:
    """Build Section 3 -- Confirmed Values.

    Derives confirmed values from interview log entries, structured by group.
    """
    show_conditionals = has_conditionals(manifest)

    # Collect groups and their variables in order of appearance.
    groups = []  # list of dicts: {name, branch, variables: [{name, label, value}], is_loop, loop_items: [...]}
    current_group = None

    # Track corrections: label -> new_value
    correction_map = {}
    for entry in entries:
        if entry.get("type") == "correction":
            label = entry.get("label", "")
            correction_map[label] = entry.get("new_value", "")

    # Track prefilled values
    prefill_values = {}
    for entry in entries:
        if entry.get("type") == "prefill":
            for item in entry.get("values", []):
                name = item.get("name", "")
                prefill_values[name] = item.get("value")

    # Walk entries to build group structure
    pending_question_var = None
    for entry in entries:
        entry_type = entry.get("type")

        if entry_type == "group_start":
            current_group = {
                "name": entry.get("name", ""),
                "branch": entry.get("branch"),
                "variables": [],
                "is_loop": False,
                "loop_items": [],
            }
            groups.append(current_group)

        elif entry_type == "question":
            pending_question_var = entry.get("variable", entry.get("name", ""))

        elif entry_type == "answer":
            if current_group is not None and pending_question_var:
                label = get_variable_label(manifest, pending_question_var)
                value = entry.get("text", entry.get("value", ""))
                # Apply correction if one exists for this label
                if label in correction_map:
                    value = correction_map[label]
                current_group["variables"].append({"name": pending_question_var, "label": label, "value": value})
            pending_question_var = None

        elif entry_type == "loop_item":
            if current_group is not None:
                current_group["is_loop"] = True
                current_group["loop_items"].append(entry)

    # Also add prefilled variables that aren't already captured via Q/A
    captured_names = set()
    for g in groups:
        for v in g["variables"]:
            captured_names.add(v["name"])

    # Build markdown
    lines = ["## Confirmed Values", ""]

    for group in groups:
        name = group["name"]
        branch = group.get("branch")

        # Heading with conditional annotations
        if show_conditionals and branch == "skipped":
            lines.append(f"### {name} *(skipped \u2014 not applicable)*")
            lines.append("")
            continue
        elif show_conditionals and branch == "if":
            lines.append(f"### {name} *(included)*")
        elif show_conditionals and branch == "else":
            lines.append(f"### {name} *(alternative)*")
        else:
            lines.append(f"### {name}")
        lines.append("")

        if group["is_loop"] and group["loop_items"]:
            # Loop group: one sub-block per item
            for item in group["loop_items"]:
                index = item.get("item_index", "")
                lines.append(f"**Item {index}**")
                lines.append("")
                values = item.get("values", {})
                if values:
                    lines.append("| Field | Value |")
                    lines.append("|---|---|")
                    for var_name, var_value in values.items():
                        label = get_variable_label(manifest, var_name)
                        lines.append(f"| {label} | {format_value(var_value)} |")
                    lines.append("")
        elif group["variables"]:
            lines.append("| Field | Value |")
            lines.append("|---|---|")
            for var in group["variables"]:
                lines.append(f"| {var['label']} | {format_value(var['value'])} |")
            lines.append("")

    return "\n".join(lines)


def build_footer(ended_at: str) -> str:
    """Build Section 4 -- Footer.

    Uses the date from ended_at, falling back to today's date.
    """
    try:
        dt = datetime.fromisoformat(ended_at.replace("Z", "+00:00"))
        date_str = dt.strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        date_str = datetime.now().strftime("%Y-%m-%d")

    lines = [
        "---",
        "",
        f"*Generated by Codraft on {date_str}*",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Codraft transcript generator \u2014 builds a human-readable transcript.md from an interview log."
    )
    parser.add_argument(
        "--interview-log",
        required=True,
        help="Path to interview_log.json.",
    )
    parser.add_argument(
        "--manifest",
        required=True,
        help="Path to manifest.yaml.",
    )
    parser.add_argument(
        "--job-folder",
        required=True,
        help="Path to the job output folder.",
    )
    parser.add_argument(
        "--output-files",
        required=True,
        help="Comma-separated output file basenames (e.g. 'agreement.docx, agreement.pdf').",
    )
    parser.add_argument(
        "--ended-at",
        required=True,
        help="ISO 8601 timestamp for when the document was rendered.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)

    try:
        # Read inputs
        with open(args.interview_log, "r", encoding="utf-8") as f:
            log = json.load(f)

        with open(args.manifest, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f)

        entries = log.get("entries", [])

        # Extract session_start (first entry)
        session_start = {}
        remaining_entries = entries
        if entries and entries[0].get("type") == "session_start":
            session_start = entries[0]
            remaining_entries = entries[1:]

        # Derive ended_at from log entries, falling back to CLI arg
        ended_at = derive_ended_at(entries, args.ended_at)

        # Build all four sections
        header = build_header(session_start, ended_at, args.output_files)
        interview = build_interview(remaining_entries, manifest)
        confirmed = build_confirmed_values(remaining_entries, manifest)
        footer = build_footer(ended_at)

        transcript_content = "\n\n".join([header, interview, confirmed, footer]) + "\n"

        # Write transcript
        transcript_path = os.path.join(args.job_folder, "transcript.md")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript_content)

        print(json.dumps({"transcript_path": transcript_path, "success": True}))

    except Exception as exc:
        print(json.dumps({"transcript_path": None, "success": False, "error": str(exc)}))
        sys.exit(1)


if __name__ == "__main__":
    main()
