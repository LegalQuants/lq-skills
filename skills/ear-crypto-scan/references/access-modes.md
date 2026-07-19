Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Access Modes — EAR Cryptographic Code Scanner

## Primary Access Mode

`user_supplied_source` — The engineer supplies the target repository by cloning it
locally and pointing a Claude Code session at the repository root. Claude reads
source files from the local filesystem.

## Requirements

- Claude Code session (or equivalent agent with filesystem read access)
- Read-only access to target repository (local clone or GitHub checkout)
- No web search, MCP tools, API keys, or external network access required or used
- Output directory writable by Claude Code for intermediate batch files

## Access Mode Declarations per Scan Phase

| Phase | Access Mode | Notes |
|-------|-------------|-------|
| Directory survey | `user_supplied_source` | Reads local filesystem |
| Batch file scanning | `user_supplied_source` | Reads local source files |
| Intermediate batch writes | Built-in file tools | Writes to `./crypto-scan-results/` |
| Final report generation | Built-in file tools | Writes `FINAL-REPORT.md` |
| External lookups | NONE | Scan is air-gapped — no external calls |

## Fallback Behaviour

If filesystem access is unavailable (harness does not support file tools):
- Do NOT attempt analysis from model memory
- Produce a scan plan only: list directories to review, detection criteria to
  apply per language, and the EAR Classification Decision Tree for manual use
- Label output: `source_missing — filesystem access unavailable`

## Prohibited Behaviours

- `model_memory_prohibited` — Do not classify crypto findings from recalled knowledge
  about specific libraries or codebases. Analysis must be grounded in code read
  from the supplied repository.
- Do not make external network calls during scanning
- Do not write output outside `./crypto-scan-results/`
