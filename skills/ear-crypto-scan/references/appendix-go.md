Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Appendix A: Go

**Use this appendix when scanning:** Go codebases
**Primary package ecosystem:** Go standard library (`crypto/*`, `golang.org/x/crypto`),
cgo bindings
**Keyword confidence reference:** See Keyword Confidence Tiers in `SKILL.md`

## A1.1 Primary Detection Targets

| Category | Examples |
| -------- | -------- |
| Symmetric encryption | `aes.NewCipher`, `cipher.NewGCM`, `cipher.NewCBCEncrypter/Decrypter` |
| TLS / SSL setup | `tls.Config{...}`, `tls.Dial`, `tls.Listen` |
| Asymmetric / signatures | `ecdsa.GenerateKey`, `ecdsa.Sign/Verify`, `rsa.GenerateKey`, `rsa.Encrypt*/Decrypt*` |
| Certificate / PKI | `x509.CreateCertificate`, `x509.ParseCertificate` |
| Extended crypto | `golang.org/x/crypto/*` (e.g., `argon2.IDKey`, `scrypt.Key`, `hkdf`) |
| Hashing / HMAC | `sha256.New()`, `hmac.New()` |
| JWT signing (direct) | `jwt.SignedString()`, `jwt.NewWithClaims(..., jwt.SigningMethodRS256)` |
| C interop via cgo | `EVP_EncryptInit_ex`, `EVP_EncryptUpdate`, `EVP_Decrypt*`, `SSL_new`, `SSL_set_fd`, `SSL_connect`, `SSL_accept` (OpenSSL / BoringSSL via cgo wrappers) |

## A1.2 Secondary Detection Targets

```
- http.Client{Transport: &http.Transport{TLSClientConfig: ...}} — TLS config with parameter
- sql.Open with connection string containing tls=true AND a TLSClientConfig (not connection string flag only)
```

## A1.3 Language-Specific Exclusions

```
- sql.Open with connection string containing tls=true or sslmode=require only
  (no TLSClientConfig) → EXCLUDE
- http.Client{} with no TLSClientConfig field set → EXCLUDE
- import "crypto/..." without corresponding function calls → EXCLUDE
```

## A1.4 Classification Examples

**Go Example A1 — Key Derivation (argon2):**

```go
import "golang.org/x/crypto/argon2"
key := argon2.IDKey(password, salt, 1, 64*1024, 4, 32)
```

Decision path: Q1-Yes (KDF invocation) → Q2-Yes (iteration/memory/parallelism specified) → Q3-Yes (derives key material) → **STRONG 5D002 INDICATOR**: Derives cryptographic keys with specified parameters.

**Go Example A2 — TLS with Defaults + Certificate Loading:**

```go
import "crypto/tls"
config := &tls.Config{
    Certificates: []tls.Certificate{cert},
}
conn, _ := tls.Dial("tcp", "example.com:443", config)
```

Decision path: Q1-No → Q4-Yes (loads certificate into TLS config) → **BORDERLINE**: Certificate loading without algorithm selection. Review whether cert loading alone triggers classification.
