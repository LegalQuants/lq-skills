# PR Readiness Checklist

Use this before opening a pull request to a public skills repository.

## Content Checks

- [ ] Repo contains only AnonLQ-authored contribution materials.
- [ ] No private app, firm, client, project, or personal-name references.
- [ ] Each skill has:
  - `SKILL.md`
  - `README.md`
  - `LICENSE`
  - `examples/output.md`
  - at least one `references/*.md`
- [ ] Each `SKILL.md` links to its local example and reference file.
- [ ] Each skill has explicit access modes and no-source fallback behaviour.
- [ ] Externally sourced examples cite public sources or clearly mark source absence.
- [ ] No skill verifies from model memory.

## Behaviour Checks

Run each relevant skill's local `evals.yaml` manually in the target harness. For each eval:

- [ ] Claude selects or can be directed to the right skill.
- [ ] Response includes source/access state.
- [ ] Response uses the local example shape where appropriate.
- [ ] Response preserves uncertainty when sources are absent.
- [ ] Response avoids prohibited outputs.

## Install Checks

Test at least one clean installation route:

- [ ] Clone repo into a fresh directory.
- [ ] Expose `skills/` to Claude Code or another Agent Skills-compatible harness.
- [ ] Invoke one skill directly or by trigger phrase.
- [ ] Confirm supporting files in `examples/` and `references/` are loadable.

## Suggested PR Summary

```markdown
## Summary

- Adds 11 AnonLQ legal workflow skills covering UK litigation review, citation/proposition checking, reviewer markup collation, claim economics, local-first legal AI audit, and Companies House investigation.
- Each skill is self-contained with local examples, reference models, access-mode fallbacks, and source-status guardrails.
- Adds shared access-mode guidance and prompt evals for live-source, user-supplied-source, and no-source scenarios.

## Testing

- Validated clean repo structure and AnonLQ-only content.
- Checked every skill has SKILL.md, README.md, LICENSE, examples/output.md, and references/*.md.
- Ran forbidden-reference scans for private app/project/identity labels.
- Fresh-cloned public repo and verified only AnonLQ skill directories were present.
```
