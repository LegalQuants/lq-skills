Copyright 2026 Abnormal AI, Inc.
SPDX-License-Identifier: Apache-2.0

# Appendix C: JavaScript / TypeScript

**Use this appendix when scanning:** JavaScript or TypeScript codebases (Node.js,
browser, edge runtimes)
**Primary package ecosystem:** Node.js built-in `crypto` module, WebCrypto API
(`crypto.subtle`), `jsonwebtoken`, `jose`, `node-forge`, `tls`, `https`
**Keyword confidence reference:** See Keyword Confidence Tiers in `SKILL.md`

## C1.1 Primary Detection Targets

| Category | Examples |
| -------- | -------- |
| Symmetric encryption (Node.js crypto) | `crypto.createCipheriv('aes-256-gcm', key, iv)`, `cipher.update(data)`, `cipher.final()`, `crypto.createDecipheriv(...)` |
| Hashing / digests | `crypto.createHash('sha256').update(data).digest('hex')`, `crypto.createHmac('sha256', secret)` |
| HMAC / MAC | `crypto.createHmac('sha256', secret).update(data).digest('hex')` |
| CSPRNG | `crypto.randomBytes(32)`, `crypto.randomUUID()`, `crypto.getRandomValues(buffer)` (WebCrypto) |
| Asymmetric / signatures | `crypto.generateKeyPair('rsa', ...)`, `crypto.sign('sha256', data, privateKey)`, `crypto.verify(...)` |
| KDF | `crypto.pbkdf2(password, salt, iterations, keylen, digest, callback)`, `crypto.scrypt(password, salt, keylen, callback)`, `crypto.hkdfSync('sha256', ikm, salt, info, keylen)` |
| TLS / SSL setup (Node.js) | `tls.createServer({key, cert, ...})`, `tls.connect({...})`, `https.createServer({key, cert})` |
| WebCrypto API (browser/edge) | `crypto.subtle.encrypt(...)`, `crypto.subtle.decrypt(...)`, `crypto.subtle.sign(...)`, `crypto.subtle.verify(...)`, `crypto.subtle.deriveBits(...)`, `crypto.subtle.importKey(...)`, `crypto.subtle.generateKey(...)` |
| JWT signing (direct) | `jwt.sign(payload, privateKey, {algorithm: 'RS256'})` (jsonwebtoken), `new SignJWT(payload).setProtectedHeader({alg: 'RS256'}).sign(privateKey)` (jose) |
| Webhook/request signing | `crypto.createHmac('sha256', secret).update(body).digest('hex')` |
| Certificate / PKI | `tls.createSecureContext({cert, key, ca})`, `forge.pki.createCertificate()` (node-forge) |

## C1.2 Secondary Detection Targets

```
- https.get('https://...', options) with explicit agent or secureContext
- tls.connect({ rejectUnauthorized: false }) — TLS config with parameter
- axios.create({ httpsAgent: new https.Agent({...}) }) with explicit TLS options
- node-fetch / got with explicit https agent configuration
```

## C1.3 Language-Specific Exclusions

```
- fetch('https://...') with no explicit SSL/TLS configuration → EXCLUDE
- axios.get('https://...') with default config → EXCLUDE
- require('https').get('https://...') with no options → EXCLUDE
- import 'https://...' (ES module URL import) → EXCLUDE
- process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0' — configuration only, no invocation
  (but flag as a security note in reviewer actions)
- jwt.verify(token, publicKey, {algorithms: ['RS256']}) — verification only using
  externally-provided public key → BORDERLINE (same analysis as Python jwt_verifier)
- import * as crypto from 'crypto' without function calls → EXCLUDE
```

## C1.4 Classification Examples

**JavaScript Example C1 — Node.js AES-GCM Encryption (STRONG 5D002):**

```javascript
const crypto = require('crypto');
const key = crypto.randomBytes(32);
const iv = crypto.randomBytes(16);
const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
const encrypted = Buffer.concat([cipher.update(data), cipher.final()]);
const tag = cipher.getAuthTag();
```

Decision path: Q1-Yes (createCipheriv + update + final) → Q2-Yes (AES-256-GCM specified) → Q3-Yes (key generated via randomBytes) → **STRONG 5D002 INDICATOR**: Direct AES-GCM encryption with full algorithm, mode, and key control.

**JavaScript Example C2 — WebCrypto Subtle API (STRONG 5D002):**

```javascript
const keyMaterial = await crypto.subtle.importKey('raw', passwordBuffer, 'PBKDF2', false, ['deriveBits']);
const derivedBits = await crypto.subtle.deriveBits(
  { name: 'PBKDF2', hash: 'SHA-256', salt: saltBuffer, iterations: 100000 },
  keyMaterial, 256
);
```

Decision path: Q1-Yes (deriveBits) → Q2-Yes (PBKDF2, SHA-256, iterations specified) → Q3-Yes (derives key material) → **STRONG 5D002 INDICATOR**: KDF invocation with explicit parameters and key material output.

**JavaScript Example C3 — Passive fetch HTTPS (LIKELY EAR99):**

```javascript
const response = await fetch('https://api.example.com/data');
const data = await response.json();
```

Decision path: Q1-No → Q4-No → **LIKELY EAR99**: TLS handled transparently by runtime; no crypto API invocation.
