# EUIPO Homoglyph / Look-alike Screening

Detects homoglyph and look-alike trademark conflicts that a standard register search misses — marks that look (and usually sound) identical to a human but are a different character string to a machine.

## What it does

A knowledge-security tool for brands. It closes the gap between *what a human sees* and *what a database matches on*:

1. Generates the **confusable variants** of a mark (Cyrillic/Greek homoglyphs, digit-for-letter like `0`→`O`, case/shape tricks like `rn`→`m`, diacritics, invisible characters), using a curated subset of the Unicode confusables standard (UTS #39).
2. Searches the **EUTM register** for each variant via a configured EUIPO connector.
3. Assesses any look-alike found under **Art. 8(1)(b)** (visual + phonetic confusion), **bad faith** (invalidity), and **Art. 8(5)** (reputation / unfair advantage).
4. Produces a draft conflict report with a **recommended action** for attorney review.

Two modes:
- **watch** — find look-alikes of an owned mark (squatting / free-riding).
- **clearance** — find earlier confusable marks before filing (the blind spot of a normal search).

## Requirements

**A configured EUIPO connector** exposing a `search_trademarks` tool against the EUTM register. The reference connector is [enxebre/euipo-mcp-server](https://github.com/enxebre/euipo-mcp-server) (MIT), built by [@enxebre](https://github.com/enxebre).

The EUIPO API uses OAuth2 client credentials (Client ID + Client Secret, not a single key). Register at the [EUIPO developer portal](https://dev.euipo.europa.eu/), create an App, and subscribe to the **Trademark Search** plan.

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

> **Match credentials to the environment.** Sandbox and production use separate credentials; a mismatch returns `401 Unauthorized`. Set `EUIPO_USE_SANDBOX="false"` for production App credentials.

> **Non-Latin search caveat.** The connector's handling of non-Latin characters in the query bounds what can be searched. The skill reports any variant it could not check rather than implying a clean result.

## Usage

```
Has anyone registered a Cyrillic or zero-for-O look-alike of AURORA in class 32?
```

```
Run a homoglyph blind-spot check on NOVARETTI before we file in classes 9 and 42
```

## Relationship to other skills

Complements [euipo-trademark-clearance](../euipo-trademark-clearance/): a standard clearance catches similar *strings*; this catches strings that are *different but look the same*. The full Art. 8(1)(b) analysis and CJEU corpus live in that skill.

## Jurisdiction

EU — EUTM register only. Does not cover national registers, domains, or unregistered use.

## Author & acknowledgements

Skill contributed by a practising EU trademark attorney and Agente de la Propiedad Industrial. Confusable data derived from the Unicode Consortium's UTS #39. EUIPO connector by [@enxebre](https://github.com/enxebre).

## License

Apache 2.0
