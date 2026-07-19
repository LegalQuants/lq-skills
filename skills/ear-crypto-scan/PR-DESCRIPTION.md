Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

## Summary

Adds `ear-crypto-scan` — a harness-agnostic skill for scanning Go, Python, and
JavaScript/TypeScript codebases for export-controlled cryptographic API invocations
under U.S. EAR.

The skill classifies each finding as STRONG 5D002 INDICATOR, BORDERLINE, or LIKELY
EAR99 using a structured decision tree, and produces a privileged report for legal
counsel review.

## What it covers

- Explicit crypto API invocations (primary) and framework crypto configurations (secondary)
- Supported languages: Go, Python, JavaScript/TypeScript (full); Java (stub)
- EAR Classification Decision Tree with recorded decision paths per finding
- Batch processing protocol with intermediate JSON output and resumption support
- Cold start intake (assets/setup-template.md) for org-specific configuration

## Testing

- Validated against a 20-file synthetic Go/Python test suite: 20/20 (100%)
- Test suite covers STRONG 5D002, BORDERLINE, LIKELY EAR99, and EXCLUDE patterns
- Edge cases tested: JWT sign vs. verify, mixed files, SDK-mediated crypto, OAuth PKCE,
  TLS cipher control vs. defaults, non-security hash usage
- JavaScript/TypeScript appendix added for v3.0 multilanguage edition

## Harness compatibility

Tested with Claude Code and OpenClaw (AgentSkills spec — compatible via `openclaw skills install`). No harness-specific modifications required; skill uses standard SKILL.md frontmatter with no `metadata.openclaw` gating block.

## Author attestation

I am a licensed attorney (Ben Richter, Associate General Counsel). I built and used
this skill in the course of legal work related to export classification analysis.

## Quality Review

/legal-builder-hub:skills-qa verdict: **READY** (2026-07-18, confirmed 2026-07-18 post-fix)
- 13/13 design parameters fully addressed
- All three legal failure modes addressed
- Trust surface: minimal (local read/write only, no hooks, no MCP, no network)
- Injection scan: clean
- No conflicts with installed skills

## Notes

- Copyright holder is Abnormal AI, Inc. — approved by IP counsel 2026-06-30
- Java appendix is a stub — contributions welcome via follow-on PR
- skills-qa Top Fixes applied: review cadence trigger added to SKILL.md Limitations (versioning), ITAR/foreign export regime scope note added, Java stub runtime warning added
