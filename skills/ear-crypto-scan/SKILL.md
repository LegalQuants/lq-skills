---
name: ear-crypto-scan
description: Scans a codebase for export-controlled cryptographic API invocations under U.S. EAR. Classifies each finding as STRONG 5D002 INDICATOR, BORDERLINE, or LIKELY EAR99 using a structured decision tree. Produces a privileged report for legal counsel review. Use when preparing for export classification analysis, engaging outside export control counsel, or auditing a codebase for encryption-related EAR obligations.
author: Ben Richter
jurisdiction: US
tags: [export-control, EAR, encryption, cryptography, codebase-scan, compliance]
---

Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# EAR Cryptographic Code Scanner

> ⚠ This tool produces investigative output only. It does not make legal determinations,
> ECCN classifications, or export compliance decisions. Qualified export control counsel
> review is required before relying on output for any compliance purpose.

## When to Use

Use this skill when:
- Preparing a codebase for U.S. export classification analysis under EAR
- Engaging or briefing outside export control counsel on a software product
- Auditing cryptographic API usage before a product launch, acquisition, or licensing deal
- Determining whether encryption registration obligations apply (e.g., annual
  self-classification reports to BIS)

Do not use this skill to make compliance determinations without qualified counsel review.

## How It Works

This skill scans source code files to identify explicit cryptographic API invocations
and classifies each finding by its level of cryptographic control:

- **STRONG 5D002 INDICATOR** — code directly invokes cryptographic APIs with parameter
  control (algorithm, mode, key size) and/or key material handling. Indicates software
  "designed to use cryptography" under EAR guidance.
- **BORDERLINE** — code configures cryptographic frameworks or invokes crypto with
  defaults. Requires human review to determine classification.
- **LIKELY EAR99** — code benefits from encryption handled transparently by frameworks
  with no direct crypto API calls.

The skill applies a structured EAR Classification Decision Tree to each finding,
records which decision branch was taken, and produces a consolidated privileged report
for legal counsel.

### Access Mode

This skill operates in `user_supplied_source` mode:
- Requires Claude Code (or equivalent agent with filesystem read access) pointed at
  the target repository
- Does NOT require web search, MCP tools, API keys, or external network access
- All analysis is performed on locally available source files
- If filesystem access is unavailable: produce a scan plan only — list directories
  to review and detection criteria to apply; do not attempt analysis from memory

See `references/access-modes.md` for full access mode declarations.

### Supported Languages

| Language | Appendix | Status |
|----------|----------|--------|
| Go | `references/appendix-go.md` | Full |
| Python | `references/appendix-python.md` | Full |
| JavaScript / TypeScript | `references/appendix-js-ts.md` | Full |
| Java | `references/appendix-java-stub.md` | Stub — contributions welcome |

### Execution Summary

1. Run setup (once): paste `assets/setup-template.md` into any Claude session to
   generate a configured version of the prompt for your organization
2. Survey repository structure and identify languages present
3. Load only the relevant language appendices from `references/`
4. Scan in prioritized batches; write intermediate results to `./crypto-scan-results/`
5. Deduplicate, aggregate, generate `FINAL-REPORT.md`
6. Deliver report to legal counsel — do not distribute beyond authorized recipients

## Examples

See `examples/output.md` for an annotated sample report output showing all three
finding types (STRONG 5D002 INDICATOR, BORDERLINE, LIKELY EAR99) with complete
field population and decision tree paths.

## Limitations

- Output is `[Unverified]` — no legal determinations or ECCN classifications are made
- Export control analysis requires qualified U.S. export control counsel; this tool
  surfaces evidence, legal makes the determination
- Detection is limited to languages with available appendices; other languages are
  flagged at Unknown confidence
- The 100-finding cap may mean some findings are deprioritized on large codebases —
  counsel should be aware scan may not be exhaustive at scale
- Labeling output as attorney work product requires the scan to be directed by or at
  the request of counsel; confirm privilege applicability with your legal team
- Java appendix is a stub; Go, Python, and JS/TS are fully validated. Java findings
  should be treated as Unknown confidence and flagged for manual review — do not rely
  on the Java appendix alone for classification without a completed detection table
- This skill is scoped to U.S. EAR. Findings that may implicate ITAR (e.g., defense
  or military-related cryptographic use cases) or foreign export control regimes fall
  outside scope and require separate counsel engagement
- Review this skill when: (a) the EAR is amended in ways that affect the definition
  of "designed to use cryptography"; (b) crypto libraries in supported languages
  introduce new API patterns not captured in the appendices; or (c) 12 months have
  elapsed since last review (current version: 3.1, reviewed: 2026-06-30)

## Full Prompt

The complete scan prompt (with all detection criteria, decision tree, execution
strategy, output format, and safeguards) is split across:
- This file (navigation and execution summary)
- `references/appendix-[language].md` — load the relevant one(s) before scanning
- `references/classification-examples.md` — load for borderline case calibration
- `references/output-format.md` — load for report template and batch JSON schema

The operator instructions and cold start intake are in `assets/setup-template.md`.

---

## Mission

Scan the target codebase to identify all export-controlled cryptographic functionality
under U.S. Export Administration Regulations (EAR). Produce a single consolidated
report that classifies each finding by its level of cryptographic control, enabling
legal counsel to distinguish between:

- **"Designed to use cryptography"** — code that directly invokes cryptographic APIs
  (ECCN 5D002 territory)
- **"Uses encryption without calling/invoking"** — code that benefits from encryption
  handled transparently by frameworks (EAR99 territory)

This distinction drives the export classification analysis. Your job is to surface the
evidence; legal makes the determination.

---

## Scope

| Parameter | Value |
| --------- | ----- |
| Languages | Any language with available appendix (Go, Python, JavaScript/TypeScript, Java stub); flag other languages if crypto calls found; see appendices for per-language detection tables |
| Detection target | Explicit cryptographic API invocations (primary); framework crypto configs (secondary) |
| Access level | Read-only — no code modification, no external network calls |
| Output | Single consolidated markdown report + intermediate JSON files |
| Maximum findings | 100 unique findings (prioritize High confidence) |

---

## Legal Framework

**All output must be labeled:** `[PRIVILEGE_LABEL]`

**All findings are `[Unverified]`** — no legal determinations or ECCN classifications
are made by this scan.

**Distribution:** `[DISTRIBUTION_LIST]`

Note on privilege: Labeling output as attorney work product requires that the scan be
directed by or at the request of counsel. Confirm with your legal team that this scan
is appropriately privileged under your jurisdiction before relying on the label.
`[PRIVILEGE_LABEL]` is a placeholder — substitute your organization's standard
privilege designation.

---

## Detection Criteria

### Reasoning Instruction

For every potential finding, work through this decision tree before recording it.
Do not skip steps.

```
STEP 1: Is there an explicit cryptographic API call in the code?
  ├─ YES → Go to Step 2
  └─ NO → Is there a framework/infrastructure crypto configuration?
           ├─ YES → Record as SECONDARY finding, go to Step 2
           └─ NO → EXCLUDE. Do not record.

STEP 2: Is the call actually invoked (not just imported, commented, or in dead code)?
  ├─ YES → Go to Step 3
  └─ NO → EXCLUDE. Do not record.

STEP 3: Classify the control level (see "EAR Classification Decision Tree" below)
  → Record finding with full assessment
```

### Primary Detection Target: Explicit Cryptographic API Invocations

These represent code "designed to use cryptography" under EAR guidance.

**Language-specific detection tables are in the appendices. Before scanning, confirm
which appendices apply to your codebase and load only those.**

Available appendices:
- Appendix A: Go → `references/appendix-go.md`
- Appendix B: Python → `references/appendix-python.md`
- Appendix C: JavaScript / TypeScript → `references/appendix-js-ts.md`
- Appendix D: Java (stub) → `references/appendix-java-stub.md`

### Secondary Detection: Framework/Infrastructure Crypto Configuration

These may represent "uses encryption without calling/invoking" — track separately
for analysis.

Language-specific examples are in each language appendix.

General pattern: any code that configures a cryptographic framework's behavior (sets
cipher suites, loads certificates, specifies TLS version, sets SSL context) without
directly invoking encrypt/decrypt/sign/hash/keygen functions.

### Exclusions — Do NOT Flag

| Category | Examples | Reason |
| -------- | -------- | ------ |
| Passive HTTPS | `requests.get('https://...')` with no ssl_context config | Platform handles encryption, no crypto API calls |
| Default TLS clients | `http.Client` with no explicit `TLSClientConfig` | Default behavior, no parameter control |
| Database connection flags only | `sslmode=require`, `encrypt=true` in connection strings | No key/cert manipulation |
| Storage encryption configs | S3 SSE-S3, EBS/EFS encryption flags | No key material handling |
| Comments / documentation | Mentions of encryption without code | No invocation |
| Import-only | `import ssl` with no corresponding API calls | No invocation |
| OAuth token *validation* (standard) | `jwt.decode(token, key, algorithms=['RS256'])` — only verifying tokens issued by an IdP using the IdP's public key | Passive consumption of crypto infrastructure; distinguish from *signing* |

### Cybersecurity SaaS Edge Cases

These patterns are common in B2B security products. Apply careful analysis:

| Pattern | Classification Guidance |
| ------- | ----------------------- |
| **JWT signing with app-generated keys** | If the code generates or loads a private key and signs JWTs → PRIMARY finding (5D002 indicator). If it only verifies JWTs using a public key from an IdP → EXCLUDE |
| **Webhook signature verification** | If the code computes `HMAC(secret, payload)` to verify inbound webhooks → PRIMARY finding (the code invokes HMAC). If it delegates to a framework middleware → SECONDARY |
| **OAuth nonce generation** | If using `secrets.token_urlsafe()` or `os.urandom()` to generate OAuth state/nonce → PRIMARY finding (CSPRNG invocation), but note purpose is anti-replay, not data encryption |
| **API request signing** (e.g., AWS SigV4) | If the code directly computes HMAC-SHA256 signatures for API auth → PRIMARY. If it uses the SDK which handles signing internally → EXCLUDE |
| **Certificate pinning** | If the code loads specific certificates and configures TLS to pin them → SECONDARY (TLS configuration with parameter control). If it just sets `verify=True` → EXCLUDE |
| **Package/artifact signing** (RSA/GPG) | If the code signs release artifacts with private keys → PRIMARY (5D002 strong). If it verifies signatures using public keys → PRIMARY but note verification-only |
| **Data-at-rest encryption** (customer data) | Direct `encrypt(customer_data)` calls → PRIMARY (5D002 strong). KMS API calls that delegate to cloud provider → SECONDARY |

### Keyword Confidence Tiers

| Tier | Keywords | Notes |
| ---- | -------- | ----- |
| **High** | `openssl`, `boringssl`, `fernet`, `cryptography`, `tls`, `ssl`, `cipher`, `rsa`, `aes`, `ecdsa`, `hkdf`, `pbkdf`, `x509`, `certificate` | Flag on sight if paired with invocation |
| **Medium** | `crypto`, `security`, `hash`, `digest`, `signature`, `hmac`, `jwt` | Only flag if paired with explicit API calls |
| **Low / Contextual** | `token`, `secret`, `nonce`, `salt`, `key` | Only flag if in a cryptographic context (e.g., `key` in `aes.NewCipher(key)`, not `key` in `dict[key]`) |

---

## EAR Classification Decision Tree

For each finding, walk this tree to determine the EAR assessment. Record which branch
you took.

```
Q1: Does the code DIRECTLY INVOKE a cryptographic function?
    (encrypt, decrypt, sign, verify, hash, derive key, generate key, CSPRNG)
    │
    ├─ YES
    │   │
    │   Q2: Does the code CONTROL cryptographic parameters?
    │       (specifies algorithm, mode, padding, key size, cipher suite)
    │       │
    │       ├─ YES
    │       │   │
    │       │   Q3: Does the code HANDLE KEY MATERIAL?
    │       │       (generates, derives, loads, stores, rotates keys)
    │       │       │
    │       │       ├─ YES → ★ STRONG 5D002 INDICATOR
    │       │       │         "Designed to use cryptography"
    │       │       │         (Application-level crypto with full control)
    │       │       │
    │       │       └─ NO  → ★ STRONG 5D002 INDICATOR
    │       │                 "Designed to use cryptography"
    │       │                 (Invokes and parameterizes crypto operations)
    │       │
    │       └─ NO (uses defaults)
    │           │
    │           Q3b: Does the code handle key material?
    │           │
    │           ├─ YES → ◆ BORDERLINE — Human review required
    │           │         (Handles keys but delegates algorithm choices)
    │           │
    │           └─ NO  → ◆ BORDERLINE — Human review required
    │                     (Direct invocation but with framework defaults)
    │
    └─ NO
        │
        Q4: Does the code CONFIGURE a framework's crypto behavior?
            (sets cipher suites, loads certs, specifies TLS version)
            │
            ├─ YES → ◆ BORDERLINE — Human review required
            │         (Configures crypto without direct invocation)
            │
            └─ NO  → ○ LIKELY EAR99
                      "Uses encryption without calling/invoking"
                      (Passive use only — framework handles everything)
```

**Record for each finding:**

1. Direct crypto API invocation? `[Yes/No]`
2. Controls cryptographic parameters? `[Yes — specify: algorithm/mode/keysize | No — uses defaults]`
3. Handles key material? `[Yes — specify: generation/derivation/storage/loading | No]`
4. Implementation layer: `[Application Data | Key Management | TLS/Transport | Framework Config]`
5. Decision tree path: `[Q1-Yes → Q2-Yes → Q3-Yes | etc.]`
6. Assessment: `[STRONG 5D002 INDICATOR | BORDERLINE | LIKELY EAR99]`

---

## Execution Strategy

### Batch Processing Protocol

**Phase 1: Directory Survey**
Before scanning any code, survey the repository structure. Write the directory tree to
`./crypto-scan-results/directory-survey.txt`. Identify:
- Total number of source files per language
- Key directories likely to contain crypto (`/crypto/`, `/security/`, `/auth/`,
  `/tls/`, `/kms/`, `/pkg/`, `/internal/`, `/lib/`)
- Estimated batch count (target ~20-30 files per batch)

**Phase 2: Prioritized Scanning**
Scan in this order:
1. **High-priority directories first:** anything matching `/crypto/`, `/security/`,
   `/kms/`, `/pki/`, `/auth/`, `/certs/`, `/signing/`
2. **Core application code:** `/pkg/`, `/internal/`, `/cmd/`, `/api/`, `/services/`
3. **Infrastructure / config:** `/infra/`, `/deploy/`, `/config/`, `/scripts/`
4. **Remaining:** everything else

For each batch:
1. Announce: "Scanning batch N: [directory list]"
2. Scan each file for detection criteria
3. For each finding, walk the EAR Classification Decision Tree
4. Write batch results to `./crypto-scan-results/batch-N.json`

The batch JSON schema is in `references/output-format.md`.

**Phase 3: Deduplication & Aggregation**
After all batches complete:
1. Load all `batch-N.json` files
2. Deduplicate: same file + same crypto function + same line range = merge into one
   finding (keep the most detailed version)
3. Same crypto library used across multiple files = separate findings (each file is a
   distinct invocation context)
4. Sort findings: STRONG 5D002 first, then BORDERLINE, then EAR99
5. Assign final sequential IDs (F001, F002, ...)

**Phase 4: Report Generation**
Generate `./crypto-scan-results/FINAL-REPORT.md` using the output format in
`references/output-format.md`.

### Stop Conditions

- Continue until entire codebase scanned
- Maximum 100 unique findings (prioritize High confidence; if limit approached,
  deprioritize EAR99/EXCLUDE-borderline findings)
- If session context is running low, write current state and instruct engineer to
  "resume scan"

### Resumption Protocol

If the engineer says "resume scan":
1. Read `./crypto-scan-results/` for existing batch files
2. Read `directory-survey.txt` to determine which directories remain
3. Continue from the next unscanned batch
4. On completion, regenerate the final report incorporating all batches

---

## Context Classification

For each finding, classify its architectural context:

| Context | Description | Evidence |
| ------- | ----------- | -------- |
| **Product** | End-user deliverable (web UI, APIs, browser extension) | Path: `/api/`, `/web/`, `/extension/`; serves customer traffic |
| **Feature** | Specific capability within product (auth, email processing) | Path: `/auth/`, `/mail/`, `/detection/`; feature-specific function names |
| **Infrastructure** | Backend/platform components (TLS termination, DB, CI) | Path: `/infra/`, `/deploy/`, `/gateway/`; ops-related function names |
| **Shared Service** | Reusable libraries (KMS client, crypto utils, PKI) | Path: `/lib/`, `/pkg/common/`, `/shared/`; generic utility patterns |
| **Unknown** | Context unclear from available evidence | Mark "human review recommended" |

**Confidence scoring:**
- **High:** Explicit call + clear corroborating evidence (path, function name, class name, comments)
- **Medium:** Explicit call + weak/ambiguous evidence
- **Low:** Conflicting or unclear signals → mark "human review recommended"

---

## Constraints & Safeguards

1. **Redact all secrets:** Replace keys, salts, certificate bodies, passwords, tokens
   with `—REDACTED—`
2. **Aggregate duplicates:** Multiple invocations of the same function in the same
   file/context = one finding (keep most detailed). Same library in different files =
   separate findings.
3. **Approximate locations:** "near lines 15-20" is acceptable when exact line numbers
   unavailable
4. **Prioritize High confidence:** Focus on clear cryptographic invocations first
5. **No false certainty:** Mark unclear cases as "Unknown" with "human review
   recommended"
6. **No legal conclusions:** Never state that code "violates" or "complies with" export
   regulations. Surface evidence only.
7. **Consistent classification:** If you classify Pattern X as STRONG 5D002 in finding
   F003, apply the same classification to the same pattern in F047. Before finalizing
   the report, review all findings for consistency.

---

## Self-Validation Checklist

Before generating the final report, verify each of the following. If any check fails,
fix it before output.

- [ ] Every finding has all required fields populated (no blanks except "Secondary purpose: none")
- [ ] Every finding includes a decision tree path (Q1 → Q2 → Q3 or Q1 → Q4 etc.)
- [ ] Every EAR assessment has a 2-3 sentence reasoning, not just a label
- [ ] No secrets, keys, salts, or tokens appear unredacted in any snippet
- [ ] Summary table finding count matches detailed findings count
- [ ] EAR distribution counts in summary match actual finding assessments
- [ ] All findings labeled `[Unverified]`
- [ ] Report header includes `[PRIVILEGE_LABEL]`
- [ ] Consistent classification: same crypto pattern → same EAR assessment across findings
- [ ] Exclusions log populated with notable evaluated-and-excluded items

---

## Execution Checklist

```
✅ Phase 1: Survey repository structure, write directory-survey.txt
✅ Phase 2: Scan in prioritized batches, write batch-N.json for each
   ✅ For each file: detect explicit crypto API calls (primary) and framework configs (secondary)
   ✅ For each finding: walk the EAR Classification Decision Tree, record path taken
   ✅ Redact all secrets before writing to batch file
✅ Phase 3: Load all batch files, deduplicate, aggregate, assign final IDs
✅ Phase 4: Generate FINAL-REPORT.md
   ✅ Run self-validation checklist
   ✅ Verify summary statistics match detailed findings
   ✅ Confirm privilege labels applied throughout
✅ Announce completion to engineer with finding count summary
```

**Begin by surveying the repository structure, then proceed to batch scanning.
Report progress after each batch.**

---

*AI assistance only — not legal advice. Human review required. Follow company data
handling and privilege protocols.*
