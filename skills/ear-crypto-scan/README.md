Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# EAR Cryptographic Code Scanner

**A harness-agnostic skill for scanning codebases for export-controlled cryptographic
functionality under U.S. Export Administration Regulations (EAR).**

> ⚠ This tool produces investigative output only. Qualified export control counsel
> review is required before relying on output for any compliance purpose.

## What It Does

Scans Go, Python, JavaScript/TypeScript (and Java stub) source code to identify
explicit cryptographic API invocations and classifies each by its level of EAR control:

- **STRONG 5D002 INDICATOR** — "designed to use cryptography"
- **BORDERLINE** — requires human review
- **LIKELY EAR99** — "uses encryption without calling/invoking"

Produces a privileged consolidated report for legal counsel.

## Installation

### Claude Code

```bash
# Option 1: Clone directly
git clone https://github.com/[REPO_ORG]/ear-crypto-scan.git

# Option 2: Install via clawhub (if registered)
clawhub install ear-crypto-scan
```

Expose the `ear-crypto-scan/` folder to your Claude Code skills directory.

### Other Agent Skills-compatible harnesses

Any harness that supports the Agent Skills format (agentskills.io) can load this
skill by pointing to the `ear-crypto-scan/` directory.

## Quick Start

1. **Run setup once** — paste `assets/setup-template.md` into any Claude session.
   Answer 6 questions. Receive a configured scan prompt (`CONFIGURED.md`).
2. **Run the scan** — open a Claude Code session pointed at your repository root.
   Paste your `CONFIGURED.md` as your first message.
3. **Retrieve output** — scan results write to `./crypto-scan-results/FINAL-REPORT.md`.
4. **Deliver to counsel** — report is labeled with your privilege designation.
   Distribute only to authorized recipients.

## Supported Languages

| Language | Status |
|----------|--------|
| Go | ✅ Full |
| Python | ✅ Full |
| JavaScript / TypeScript | ✅ Full |
| Java | 🟡 Stub — contributions welcome |

## Harness Compatibility

Tested with:
- Claude Code (Anthropic)

Designed for compatibility with OpenClaw and other Agent Skills-compatible harnesses.

## Repository Structure

```
ear-crypto-scan/
├── SKILL.md                    # Core skill — start here
├── README.md                   # This file
├── LICENSE                     # Apache 2.0
├── references/
│   ├── appendix-go.md          # Go detection tables
│   ├── appendix-python.md      # Python detection tables
│   ├── appendix-js-ts.md       # JS/TS detection tables
│   ├── appendix-java-stub.md   # Java stub
│   ├── classification-examples.md
│   ├── output-format.md
│   └── access-modes.md
├── examples/
│   └── output.md               # Sample report output
└── assets/
    └── setup-template.md       # Cold start intake
```

## Contributing

New language appendices are the highest-value contribution. To add one:

1. Follow the format in `references/appendix-go.md` as the template
2. Include: Primary Detection Targets table, Secondary Detection Targets,
   Language-Specific Exclusions, and at least 2 Classification Examples
3. Test against at least 5 real-world code files in that language
4. Open a PR with your test results documented

## Disclaimer

This tool does not provide legal advice. Output requires review by qualified U.S.
export control counsel before use for any compliance purpose. See the disclaimer
in `SKILL.md` for full terms.

## License

Apache 2.0 — see `LICENSE`.
