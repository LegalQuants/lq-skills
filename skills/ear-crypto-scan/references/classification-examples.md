Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Classification Examples

These examples calibrate the decision tree. Reference them when classifying ambiguous
findings.

## ★ STRONG 5D002 INDICATORS — "Designed to Use Cryptography"

**Example 1 — Application Data Encryption (Python):**

```py
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
key = os.urandom(32)
cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(user_data) + encryptor.finalize()
```

Decision path: Q1-Yes (direct encrypt call) → Q2-Yes (AES, GCM specified) → Q3-Yes (key generated) → **STRONG 5D002 INDICATOR**: Direct encryption of application data with full parameter control.

**Example 2 — Key Derivation (Go):**

```go
import "golang.org/x/crypto/argon2"
key := argon2.IDKey(password, salt, 1, 64*1024, 4, 32)
```

Decision path: Q1-Yes (KDF invocation) → Q2-Yes (iteration/memory/parallelism specified) → Q3-Yes (derives key material) → **STRONG 5D002 INDICATOR**: Derives cryptographic keys with specified parameters.

**Example 3 — Digital Signature / JWT Signing (Python):**

```py
from cryptography.hazmat.primitives.asymmetric import rsa, padding
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
signature = private_key.sign(message, padding.PSS(...), hashes.SHA256())
```

Decision path: Q1-Yes (sign call) → Q2-Yes (PSS padding, SHA256) → Q3-Yes (generates private key) → **STRONG 5D002 INDICATOR**: Key generation + digital signature with explicit algorithms.

**Example 4 — Webhook HMAC Signing (Python) (cybersecurity SaaS common pattern):**

```py
import hmac, hashlib
signature = hmac.new(
    webhook_secret.encode(),
    request_body,
    hashlib.sha256
).hexdigest()
```

Decision path: Q1-Yes (HMAC invocation) → Q2-Yes (SHA256 specified) → Q3-Yes (loads secret key) → **STRONG 5D002 INDICATOR**: Direct HMAC computation with specified algorithm and key material.

## ◆ BORDERLINE — Requires Human Review

**Example 5 — TLS with Cipher Suite Control (Python):**

```py
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.set_ciphers('ECDHE+AESGCM:ECDHE+CHACHA20:DHE+AESGCM')
context.load_cert_chain(certfile, keyfile)
server_socket = context.wrap_socket(sock)
```

Decision path: Q1-No (no encrypt/decrypt/sign call) → Q4-Yes (configures cipher suites, loads certs) → **BORDERLINE**: Substantive control over cryptographic parameters without direct data encryption. Human review needed to determine if cipher suite selection constitutes "designing to use."

**Example 6 — TLS with Defaults + Certificate Loading (Go):**

```go
import "crypto/tls"
config := &tls.Config{
    Certificates: []tls.Certificate{cert},
}
conn, _ := tls.Dial("tcp", "example.com:443", config)
```

Decision path: Q1-No → Q4-Yes (loads certificate into TLS config) → **BORDERLINE**: Certificate loading without algorithm selection. Review whether cert loading alone triggers classification.

**Example 7 — JWT Verification Only (Python):**

```py
import jwt
payload = jwt.decode(token, public_key, algorithms=["RS256"])
```

Decision path: Q1-Partially (verification invokes crypto, but verifier doesn't generate/control keys) → Q2-Yes (algorithm specified) → Q3-No (public key loaded, not generated) → **BORDERLINE**: Specifies algorithm for verification using externally-provided public key. Lower control level than signing, but algorithm selection is explicit. Flag for review.

## ○ LIKELY EAR99 — "Uses Encryption Without Calling/Invoking"

**Example 8 — Passive HTTPS (Python):**

```py
import requests
response = requests.get('https://api.example.com/data')
```

Decision path: Q1-No → Q4-No → **LIKELY EAR99**: HTTPS handled transparently by library.

**Example 9 — Database TLS Connection String (Go):**

```go
db, _ := sql.Open("postgres", "host=db.example.com sslmode=require")
```

Decision path: Q1-No → Q4-No (connection string flag only) → **LIKELY EAR99**: TLS negotiated by driver.

**Example 10 — Framework HTTPS Server with Defaults (Python):**

```py
from flask import Flask
app = Flask(__name__)
app.run(ssl_context='adhoc')
```

Decision path: Q1-No → Q4-Marginal (framework generates self-signed cert with defaults) → **LIKELY EAR99**: Framework handles TLS setup with default parameters. Verify framework doesn't expose substantive crypto control.

## ✕ EXCLUSIONS — Do Not Report

**Example 11 — Import Without Usage (Python):**

```py
import ssl  # Imported but never used in this file
```

→ **EXCLUDE**: No invocation.

**Example 12 — Comments Only (Python):**

```py
# TODO: Add AES encryption to user data
user_data = database.get(user_id)
```

→ **EXCLUDE**: Documentation only.
