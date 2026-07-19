Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Appendix B: Python

**Use this appendix when scanning:** Python codebases
**Primary package ecosystem:** `cryptography`, `ssl`, `hashlib`, `hmac`, `secrets`,
`Fernet`, `pyjwt`
**Keyword confidence reference:** See Keyword Confidence Tiers in `SKILL.md`

## B1.1 Primary Detection Targets

| Category | Examples |
| -------- | -------- |
| Symmetric encryption | `Fernet.generate_key()`, `Fernet(...).encrypt(...)`, `Cipher(algorithms.AES(...), modes.GCM(...))` |
| Hashing / digests | `hashes.SHA256()`, `hashlib.sha256(...).update(...).digest()` |
| HMAC / MAC | `hmac.HMAC(...).update(...).finalize()` |
| TLS / SSL setup | `ssl.SSLContext(...)`, `.wrap_socket()`, `.load_cert_chain()` |
| CSPRNG | `secrets.token_bytes()`, `os.urandom()` |
| Asymmetric / signatures | `rsa.generate_private_key()`, `private_key.sign(...)`, `ecdsa.*` |
| KDF | `PBKDF2HMAC(...)`, `Scrypt(...)`, `HKDF(...)` |
| JWT signing (direct) | `jwt.encode(..., algorithm='RS256')`, `jwt.encode(..., key=private_key)` |
| Webhook/request signing | `hmac.new(secret, msg, hashlib.sha256).hexdigest()` |

## B1.2 Secondary Detection Targets

```
- requests.get('https://...', verify=True/False) — explicit ssl verification parameter
- app.run(ssl_context=context) — explicit SSL context (not 'adhoc' shorthand)
- psycopg2.connect(sslmode='require') — database TLS config with parameter
```

## B1.3 Language-Specific Exclusions

```
- requests.get('https://...') with no ssl_context → EXCLUDE
- import ssl / import hashlib / import cryptography without corresponding
  API calls → EXCLUDE
- ServerSideEncryption="AES256" as boto3/S3 parameter → EXCLUDE
- app.run(ssl_context='adhoc') → LIKELY EAR99 (not EXCLUDE — but document
  that framework handles all crypto with defaults)
```

## B1.4 Classification Examples

**Python Example B1 — Application Data Encryption:**

```py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(32)
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(user_data) + encryptor.finalize()
```

Decision path: Q1-Yes (direct encrypt call) → Q2-Yes (AES, GCM specified) → Q3-Yes (key generated) → **STRONG 5D002 INDICATOR**: Direct encryption of application data with full parameter control.

**Python Example B2 — JWT Verification Only:**

```py
import jwt
payload = jwt.decode(token, public_key, algorithms=["RS256"])
```

Decision path: Q1-Partially (verification invokes crypto, but verifier doesn't generate/control keys) → Q2-Yes (algorithm specified) → Q3-No (public key loaded, not generated) → **BORDERLINE**: Specifies algorithm for verification using externally-provided public key. Lower control level than signing, but algorithm selection is explicit. Flag for review.
