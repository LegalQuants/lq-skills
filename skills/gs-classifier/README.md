# EUIPO Goods & Services Classifier

Maps goods and services to the correct Nice classes and to the harmonised terms accepted by the EUIPO, to prepare a trademark specification before filing.

## What it does

Queries the EUIPO Goods & Services (TMclass / harmonised database, "HDB") via a configured EUIPO connector and returns Nice class numbers with accepted term wording. Two modes:

- **Detailed** — classifies a concrete product/service list into Nice classes with validated HDB wording.
- **General** — maps a plain-language business description to candidate classes, grouped by priority.

Bilingual (ES / EN), cost-aware (flags the fee impact of extra classes), and HDB-only (never invents wording — unconfirmed terms are flagged `[?]` for counsel).

## Requirements

**A configured EUIPO connector** — this skill requires an MCP connector exposing the EUIPO Goods & Services tools (`suggest_goods_and_services`, `search_goods_and_services`, `validate_classification`, `get_nice_class_headings`, `get_nice_taxonomy`, `translate_classification`). The reference connector is [enxebre/euipo-mcp-server](https://github.com/enxebre/euipo-mcp-server) (MIT), built by [@enxebre](https://github.com/enxebre); this skill was developed against it.

The EUIPO API uses OAuth2 client credentials, so the connector takes a **Client ID and Client Secret** (not a single API key). Register for free at the [EUIPO developer portal](https://dev.euipo.europa.eu/), create an App to obtain your credentials, and subscribe to the **Goods and Services** API plan.

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

> **Important — match your credentials to the environment.** The EUIPO portal issues separate credentials for sandbox and production, and the token endpoint rejects a mismatch with a `401 Unauthorized`. Set `EUIPO_USE_SANDBOX="true"` only with sandbox credentials; set it to `"false"` to use your production App credentials. If you get a 401 on the token request, this toggle is the first thing to check.

## Usage

```
Classify these goods for a trademark: moisturizing creams, shampoo, shower gel, perfumes
```

```
We're an online language academy — which Nice classes should we file in?
```

The skill asks whether you want **detailed** mode (a concrete list) or **general** mode (explore by business type) if you don't say.

## Jurisdiction

EU — EUIPO harmonised database practice. National offices may classify differently; the skill flags this where the filing target is a national office.

## Author & acknowledgements

Skill contributed by a practising EU trademark attorney and Agente de la Propiedad Industrial.

The EUIPO MCP connector this skill runs against was built by [@enxebre](https://github.com/enxebre) ([euipo-mcp-server](https://github.com/enxebre/euipo-mcp-server), MIT).

## License

Apache 2.0
