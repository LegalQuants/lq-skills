# EUIPO Trademark Clearance

Pre-filing trademark clearance against the EUTM register, with likelihood-of-confusion analysis under Art. 8.1.b EUTMR and CJEU case law.

## What it does

Queries the EUTM register via a configured EUIPO connector, identifies potentially conflicting earlier marks, and produces a structured risk report with a traffic-light rating (🔴 High / 🟡 Medium / 🟢 Low). Coverage and freshness depend entirely on the connector configured by the user.

The analysis applies the multi-factor test from CJEU case law:
- **Sign similarity** — visual, phonetic, and conceptual comparison (SABEL v Puma, C-251/95)
- **Goods/services similarity** — Canon factors (C-39/97)
- **Distinctiveness** — inherent and enhanced (Lloyd Schuhfabrik, C-342/97)
- **Global assessment** — interdependence of all factors

## Requirements

**A configured EUIPO connector** — this skill requires an MCP connector exposing a `search_trademarks` tool against the EUTM register. The reference connector is [enxebre/euipo-mcp-server](https://github.com/enxebre/euipo-mcp-server) (MIT), built by [@enxebre](https://github.com/enxebre); this skill was developed against it.

The EUIPO API uses OAuth2 client credentials, so the connector takes a **Client ID and Client Secret** (not a single API key). Register for free at the [EUIPO developer portal](https://dev.euipo.europa.eu/), create an App to obtain your credentials, and subscribe to the **Trademark Search** API plan (sandbox approval ~1 day).

Clone and pin to a specific commit for reproducibility, then point your MCP client at it:

```json
{
  "mcpServers": {
    "euipo": {
      "command": "uv",
      "args": ["--directory", "/path/to/euipo-mcp-server", "run", "euipo-mcp-server"],
      "env": {
        "EUIPO_CLIENT_ID": "your-client-id",
        "EUIPO_CLIENT_SECRET": "your-client-secret",
        "EUIPO_USE_SANDBOX": "true"
      }
    }
  }
}
```

```bash
git clone https://github.com/enxebre/euipo-mcp-server.git
cd euipo-mcp-server && git checkout d07eabdccf2160869d42b12857fe9d67d379e208
```

> **Important — match your credentials to the environment.** The EUIPO portal issues separate credentials for sandbox and production, and the token endpoint rejects a mismatch with a `401 Unauthorized`. Set `EUIPO_USE_SANDBOX="true"` only with sandbox credentials; set it to `"false"` to use your production App credentials. If you get a 401 on the token request, this toggle is the first thing to check. (Verified working end-to-end against the production Trademark Search API.)

Coverage and freshness of the search results depend entirely on this connector and the EUIPO APIs it calls; the skill itself does not guarantee live or complete register access.

## Usage

 ```
Check if AURORA is available in class 32 (beverages) before we file at the EUIPO
 ``` 

 ```
Run a clearance search for NOVATECH in classes 9 and 42
 ``` 

The skill will ask for Nice classes if not provided. It produces either an **internal** report (full legal analysis, all conflicts, CJEU citations) or a **client** report (plain language, top conflicts only).

## Jurisdiction

EU — EUTM register only. Does not cover national registers (OEPM Spain, UKIPO, INPI France, etc.). For comprehensive clearance, complement with national searches.

## Author & acknowledgements

Skill contributed by a practising EU trademark attorney and Agente de la Propiedad Industrial.

The EUIPO MCP connector this skill runs against was built by [@enxebre](https://github.com/enxebre) ([euipo-mcp-server](https://github.com/enxebre/euipo-mcp-server), MIT).

## License

Apache 2.0
