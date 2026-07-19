Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Appendix D: Java

**Status: STUB — Community contributions welcome**

**Use this appendix when scanning:** Java / Kotlin codebases
**Primary package ecosystem:** JCA (Java Cryptography Architecture), Bouncy Castle,
Spring Security Crypto, Google Tink

## D1.1 Primary Detection Targets (Stub)

Key Java crypto patterns to detect (expand with specific method signatures):

| Category | Libraries / Patterns to Detect |
| -------- | ------------------------------ |
| Symmetric encryption | `javax.crypto.Cipher.getInstance("AES/GCM/NoPadding")`, `.init()`, `.doFinal()` |
| Hashing | `MessageDigest.getInstance("SHA-256")`, `.digest()` |
| HMAC | `Mac.getInstance("HmacSHA256")`, `.doFinal()` |
| CSPRNG | `new SecureRandom()`, `.nextBytes()` |
| Asymmetric / signatures | `KeyPairGenerator.getInstance("RSA")`, `Signature.getInstance("SHA256withRSA")` |
| KDF | `SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256")`, Bouncy Castle `SCrypt` |
| TLS setup | `SSLContext.getInstance("TLS")`, `.init()`, `SSLSocketFactory` |
| JWT signing | `io.jsonwebtoken.Jwts.builder().signWith(key, alg)` (JJWT library) |
| Certificate / PKI | `CertificateFactory.getInstance("X.509")`, `KeyStore`, `TrustManagerFactory` |

**Note:** This stub covers JCA standard library patterns. Bouncy Castle, Spring
Security Crypto, and Google Tink require separate expansion. Contributions welcome
via pull request.

## D1.2 – D1.4: To Be Completed

Community contributions welcome. Follow the Appendix C (`references/appendix-js-ts.md`)
template for format. Include:
- Secondary Detection Targets
- Language-Specific Exclusions
- At least 2 Classification Examples tested against real code
