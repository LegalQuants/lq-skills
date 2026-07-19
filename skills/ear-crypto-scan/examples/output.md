Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Example Output — EAR Cryptographic Code Scanner

This is an annotated sample of FINAL-REPORT.md output. File paths, organization
details, and privilege labels are illustrative placeholders. Actual scan output
will reflect your configured values from the setup step.

---

# EXPORT CONTROL CRYPTOGRAPHIC SCAN REPORT

Attorney-Client Privileged / Attorney Work Product / Confidential
All findings [Unverified] — No compliance determinations made.

Scan Date: 2026-06-19
Repository: example-repo
Organization: [YOUR_ORG]
Languages Scanned: Go, Python, TypeScript
Total Files Scanned: 31
Total Findings: 3 (excerpt — full scan produced 33)
  - STRONG 5D002 INDICATOR: 1 (shown)
  - BORDERLINE: 1 (shown)
  - LIKELY EAR99: 1 (shown)

Scan Model: [MODEL_USED]

---

## === SUMMARY TABLE (excerpt) ===

| # | File Path | Lang | Primary Evidence | Purpose | Context | EAR Assessment | Confidence |
|---|-----------|------|-----------------|---------|---------|----------------|------------|
| F001 | lib/signing/artifact_signer.go | Go | rsa.SignPKCS1v15, x509.ParsePKCS1PrivateKey | Artifact integrity signing | Loads+uses priv key | STRONG 5D002 INDICATOR | High |
| F010 | infra/tls/server_config.py | Py | ssl.SSLContext, .set_ciphers(), .load_cert_chain() | TLS cipher config | Framework crypto config | BORDERLINE | High |
| F014 | infra/tls/adhoc_server.py | Py | app.run(ssl_context='adhoc') | Dev TLS server | Framework default | LIKELY EAR99 | High |

---

## === EAR DISTRIBUTION ANALYSIS ===

This repository shows clear bifurcation between active cryptographic engineering and
passive infrastructure usage. The majority of findings qualify as STRONG 5D002
INDICATORs, concentrated in the pkg/crypto, pkg/auth, pkg/kms, pkg/webhook, and
lib/signing packages — representing deliberate, parameterized invocations of symmetric
encryption (AES-GCM), asymmetric operations (RSA, ECDSA), key derivation (HKDF,
Scrypt, PBKDF2), HMAC signing, and CSPRNG, all with explicit algorithm selection and
key material handling. Borderline findings cover TLS infrastructure configuration with
explicit cipher suite selection and JWT verification using externally-provided IdP
public keys. LIKELY EAR99 findings are limited to development server configurations
using framework-default TLS parameters. Legal review should prioritize the pkg/crypto,
pkg/kms, lib/signing, and pkg/auth/jwt_signer files as presenting the strongest ECCN
5D002 indicators.

---

## === DETAILED FINDINGS (three representative examples) ===

---

### --- CRYPTO FINDING #F001 ---

> **[ANNOTATION: This is a STRONG 5D002 INDICATOR. It shows all three decision tree
> branches firing: Q1-Yes (direct invocation), Q2-Yes (algorithm + padding specified),
> Q3-Yes (private key loaded and used). This is the clearest 5D002 pattern.]**

Attorney-Client Privileged / Attorney Work Product / Confidential
[Unverified]

File: lib/signing/artifact_signer.go
Location: Lines 33, 43
Language: Go
Finding Type: PRIMARY — explicit asymmetric crypto invocation

Primary Evidence Line:
> x509.ParsePKCS1PrivateKey(block.Bytes) (line 33); rsa.SignPKCS1v15(rand.Reader, s.privateKey, crypto.SHA256, hashed[:]) (line 43)

Matched Keyword: rsa, x509, pkcs1, sha256
Keyword Confidence: High

Context Snippet:
```
key, err := x509.ParsePKCS1PrivateKey(block.Bytes)
signature, err := rsa.SignPKCS1v15(rand.Reader, s.privateKey, crypto.SHA256, hashed[:])
```

Purpose Inference:
  Primary: Digital Signature/Verify — Signs release artifacts with an RSA private key
           loaded from PEM file for integrity verification
  Secondary: none

EAR Classification Assessment:
  Decision Tree Path: Q1-Yes → Q2-Yes → Q3-Yes → STRONG 5D002 INDICATOR
  Direct Crypto API Invocation: Yes
  Controls Cryptographic Parameters: Yes — PKCS1v15 padding, SHA-256 hash specified
  Handles Key Material: Yes — loads RSA private key from PEM file
  Implementation Layer: Application Data

  Control Level Detail:
  - Algorithm selection: Explicit in code: RSA
  - Mode/padding: Explicit in code: PKCS1v15
  - Key size: Framework default (key size set at key generation time)
  - Key source: Loaded from config/env (PEM file on disk)

  ★ EAR Assessment: STRONG 5D002 INDICATOR
  Reasoning: The code directly invokes rsa.SignPKCS1v15 with explicit algorithm and
  padding parameters, and loads an RSA private key from a PEM file. All three decision
  tree indicators fire: direct invocation, parameter control, and key material handling.
  This is the canonical "designed to use cryptography" pattern under EAR guidance.

Context Classification:
  Type: Shared Service
  Confidence: High
  Likely Area: Artifact signing / release integrity
  Evidence: File path lib/signing/artifact_signer.go; function name and PEM load
            pattern confirm release artifact signing use case.

Reviewer Actions Recommended:
  - Confirm private key is application-controlled (loaded from file vs. injected by
    a KMS at runtime)
  - Both signing and verification functions present; signing is the primary indicator
  - Verify whether this code is compiled into customer-shipped binaries or runs
    only in the build pipeline

---

### --- CRYPTO FINDING #F010 ---

> **[ANNOTATION: This is a BORDERLINE finding. The code configures TLS cipher suites
> (Q4-Yes) but does not directly encrypt/decrypt application data (Q1-No). The
> combination of explicit cipher suite selection + certificate loading + socket wrapping
> makes this more than passive HTTPS, but less than direct crypto invocation. Legal
> determines whether cipher suite control = "designed to use."]**

Attorney-Client Privileged / Attorney Work Product / Confidential
[Unverified]

File: infra/tls/server_config.py
Location: Lines 22-27
Language: Python
Finding Type: SECONDARY — TLS server configuration with explicit cipher suite selection

Primary Evidence Line:
> ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER), .set_ciphers(ALLOWED_CIPHERS), .load_cert_chain(certfile, keyfile), .wrap_socket(sock, server_side=True)

Matched Keyword: ssl, tls, cipher, certificate
Keyword Confidence: High

Context Snippet:
```
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.minimum_version = self.MIN_TLS_VERSION
context.set_ciphers(self.ALLOWED_CIPHERS)
context.load_cert_chain(certfile=self.certfile, keyfile=self.keyfile)
context.options |= ssl.OP_NO_SSLv2 | ssl.OP_NO_SSLv3
return context.wrap_socket(sock, server_side=True)
```

Purpose Inference:
  Primary: Encrypt/Decrypt Data (in transit/TLS) — Configures hardened TLS server with
           explicit cipher suite list (ECDHE+AESGCM, ECDHE+CHACHA20), TLSv1.2 minimum,
           and server certificate loading
  Secondary: none

EAR Classification Assessment:
  Decision Tree Path: Q1-No → Q4-Yes → BORDERLINE
  Direct Crypto API Invocation: No
  Controls Cryptographic Parameters: Yes — set_ciphers specifies named cipher suites;
    minimum_version specifies TLS floor
  Handles Key Material: Yes — load_cert_chain loads certificate and private key
  Implementation Layer: TLS/Transport

  Control Level Detail:
  - Algorithm selection: Explicit in code: ECDHE+AESGCM, ECDHE+CHACHA20, DHE+AESGCM
  - Mode/padding: Framework default (TLS negotiation)
  - Key size: Framework default
  - Key source: Loaded from config/env (certfile, keyfile paths)

  ★ EAR Assessment: BORDERLINE
  Reasoning: The code does not directly encrypt or decrypt application data, placing
  it at Q1-No. However, it explicitly configures the TLS cipher suite list, sets a
  minimum TLS version, loads a certificate/key chain, and wraps the socket — all of
  which represent substantive parameter control over the cryptographic framework.
  Legal should assess whether cipher suite selection combined with certificate loading
  constitutes "designed to use cryptography" under 5D002 scope.

Context Classification:
  Type: Infrastructure
  Confidence: High
  Likely Area: TLS infrastructure / API gateway hardening
  Evidence: File path infra/tls/server_config.py; function and variable names confirm
            hardened TLS server configuration role.

Reviewer Actions Recommended:
  - Assess whether explicit cipher suite selection (set_ciphers) + cert loading
    triggers 5D002 classification
  - Companion finding in infra/tls/server.ts shows the same pattern in TypeScript
  - Note: ALLOWED_CIPHERS constant value should be confirmed — explicit named AES-GCM
    and ChaCha20-Poly1305 suite strings strengthen the finding

---

### --- CRYPTO FINDING #F014 ---

> **[ANNOTATION: This is a LIKELY EAR99 finding. The flask 'adhoc' ssl_context is
> a framework shorthand that generates a temporary self-signed certificate with default
> parameters. No cipher suite selection, no key material handling, no algorithm control.
> Decision tree exits at Q4-Marginal → LIKELY EAR99. This is a development-only
> pattern that should not appear in production.]**

Attorney-Client Privileged / Attorney Work Product / Confidential
[Unverified]

File: infra/tls/adhoc_server.py
Location: Line 12
Language: Python
Finding Type: SECONDARY — Framework HTTPS server with default parameters

Primary Evidence Line:
> app.run(ssl_context='adhoc')

Matched Keyword: ssl
Keyword Confidence: High

Context Snippet:
```
from flask import Flask
app = Flask(__name__)
app.run(host='0.0.0.0', port=8443, ssl_context='adhoc')
```

Purpose Inference:
  Primary: Encrypt/Decrypt Data (in transit/TLS) — Development TLS server using Flask's
           'adhoc' self-signed certificate shorthand; framework generates certificate
           with default parameters
  Secondary: none

EAR Classification Assessment:
  Decision Tree Path: Q1-No → Q4-Marginal → LIKELY EAR99
  Direct Crypto API Invocation: No
  Controls Cryptographic Parameters: No — 'adhoc' is a Flask shorthand; framework
    generates self-signed cert with all default parameters
  Handles Key Material: No — framework handles all key generation internally
  Implementation Layer: Framework Config

  Control Level Detail:
  - Algorithm selection: Framework default
  - Mode/padding: Framework default
  - Key size: Framework default
  - Key source: Framework-generated (ephemeral, not application-controlled)

  ★ EAR Assessment: LIKELY EAR99
  Reasoning: The ssl_context='adhoc' parameter delegates all cryptographic decisions
  to Flask/Werkzeug, which generates a temporary self-signed certificate with default
  parameters. There is no algorithm selection, no cipher suite control, and no
  application-managed key material — the framework handles everything transparently.
  Per classification example 10 in references/classification-examples.md, this is
  the canonical LIKELY EAR99 framework-default TLS pattern.

Context Classification:
  Type: Infrastructure
  Confidence: High
  Likely Area: Development server — should not be present in production builds
  Evidence: File path infra/tls/adhoc_server.py; 'adhoc' ssl_context is documented
            Flask shorthand for development-only use.

Reviewer Actions Recommended:
  - Confirm this file is not included in production deployments
  - 'adhoc' is a development convenience; production should use a hardened TLS
    configuration (cf. server_config.py Finding #F010)
  - No compliance action expected for this finding, but confirm with counsel

---

## === EXCLUSIONS LOG (excerpt) ===

| File | Pattern Found | Reason for Exclusion |
|------|--------------|---------------------|
| pkg/api/notification_client.go | http.Client{} with Timeout only | Default TLS client — no TLSClientConfig |
| pkg/api/s3_client.py | ServerSideEncryption="AES256" | S3 API parameter — SDK-mediated encryption; no direct crypto calls |
| pkg/api/storage_client.ts | S3 ServerSideEncryption: 'AES256' | Same as s3_client.py |
| pkg/api/threat_intel_client.py | requests.Session().get(https://...) | Passive HTTPS — no ssl_context |
| pkg/api/threat_intel_client.ts | fetch('https://...') | Passive HTTPS — no SSL config options |
| services/detection/db.go | sql.Open("postgres", "sslmode=require") | DB connection string SSL flag only |
| services/detection/threat_scorer.go | Comments mentioning AES, STARTTLS | Comments only — zero crypto API calls |
| services/email/parser.py | import ssl, import hashlib | Dead imports — neither module called |
| services/notifications/emailer.ts | import * as crypto | Import-only — no crypto functions called |

---

## === SCAN METADATA ===

Scan Execution Date: 2026-06-19
Scan Prompt Version: 3.1
Repository Path: example-repo/
Total Files in Repository: 31
Files Fully Read: 31 of 31
Files With Findings: 21
Files Excluded (no findings): 10

Language Breakdown (full scan, 33 findings):
- Go: 11 findings
- Python: 12 findings
- TypeScript: 10 findings

Scan Limitations:
- This scan identifies cryptographic API invocations as evidence; it does not make
  legal determinations.
- Dynamic invocations, obfuscated calls, or crypto invoked through runtime reflection
  may not be captured.
- All findings are [Unverified] pending legal review.
- ECCN classification, license determination, and EAR compliance assessment require
  human legal counsel.
- The decision tree paths recorded are analytical tools, not legal conclusions.

---

AI assistance only — not legal advice. Human review required. Follow company data
handling and privilege protocols.
