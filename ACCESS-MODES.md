# Access Modes for Source-Dependent Skills

These skills are prompt/workflow packages. They do not grant Claude API keys, browser access, web search, MCP tools, or database credentials by themselves.

## How Claude Currently Gets Sources

Claude can work from sources in several ways, depending on the harness and configuration:

- **Uploaded or pasted material**: documents, judgment text, screenshots, exports, PDFs, CSVs, HTML, filing text, or URLs supplied by the user.
- **Built-in file tools**: where the harness gives Claude access to local files.
- **Web search / web fetch tools**: when enabled by the user's Claude environment or API request. Anthropic's web search tool is tool-provided, returns source citations, and may be unavailable or limited by max uses, domain filters, admin settings, model support, or provider environment.
- **MCP servers**: external tools/data sources configured separately. Claude Code and the Claude API can connect to MCP servers, but MCP tools require explicit configuration and permission/allowlisting. A skill cannot assume a Companies House, BAILII, Find Case Law, CourtListener, or document-management MCP exists.
- **Custom tools**: tools exposed by the app or SDK host. Tool availability varies by harness.

## Required Behaviour

For any source-dependent skill:

1. First identify what source access is actually available in the current Claude session.
2. Prefer authoritative public or user-supplied sources over search snippets or summaries.
3. Record source type, URL or document id, query/search path where relevant, access date, and pinpoint.
4. If live retrieval fails or is unavailable, ask for uploaded/pasted source material, URLs, screenshots, exports, or an enabled connector.
5. If no source is available, produce a verification queue, checklist, model specification, or research plan only.
6. Do not verify citations, propositions, judicial preferences, registry facts, procedural rules, or calculated outputs from model memory.

## Standard Access Modes

Use these terms consistently:

- `live_source` - source retrieved in-session through web, browser, MCP, API, or another configured tool.
- `user_supplied_source` - source supplied by the user as a file, pasted text, screenshot, export, URL, or copied content.
- `source_missing` - source needed for the requested check is unavailable.
- `unverified-source-unavailable` - the item cannot be verified because the source could not be retrieved or supplied.
- `verify_current_rule` - current procedural/statutory/rule source must be checked before relying on the point.
- `not_observed_not_excluded` - no evidence of a network path or behaviour was observed, but the review was not exhaustive.
- `model_memory_prohibited` - the skill must not rely on recalled knowledge for this finding.

## Claude-Specific Notes

- Claude Code skills are loaded when triggered; supporting files can provide examples, templates, scripts, or references.
- MCP servers can be configured in code or through project configuration, and tools must be explicitly allowed.
- Claude API web search is a server tool that must be enabled in the request and by the organization; it can return errors such as `max_uses_exceeded`, `too_many_requests`, or `unavailable`.
- Web search citations are useful for grounding, but a search result snippet is not always a verification-grade legal source. Prefer official pages, public judgment text, filings, or user-supplied primary material.
