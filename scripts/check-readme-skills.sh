#!/usr/bin/env bash
# Verify the README "Skills" table lists exactly the skills present on disk.
# Fails (exit 1) if any skills/<name>/SKILL.md has no matching README row,
# or any README row points at a skills/<name>/ directory that doesn't exist.
set -euo pipefail

cd "$(dirname "$0")/.."

# Skills that actually exist (any dir under skills/ containing a SKILL.md).
fs_slugs=$(find skills -mindepth 2 -maxdepth 2 -name SKILL.md \
  | sed -E 's#^skills/([^/]+)/SKILL\.md$#\1#' | sort -u)

# Skills referenced by the README table (links of the form skills/<slug>/).
readme_slugs=$(grep -oE '\(skills/[a-z0-9-]+/\)' README.md \
  | sed -E 's#\(skills/([a-z0-9-]+)/\)#\1#' | sort -u)

missing=$(comm -23 <(echo "$fs_slugs") <(echo "$readme_slugs") || true)
phantom=$(comm -13 <(echo "$fs_slugs") <(echo "$readme_slugs") || true)

status=0
if [ -n "$missing" ]; then
  echo "❌ Skills on disk but NOT listed in README:"
  echo "$missing" | sed 's/^/   - /'
  status=1
fi
if [ -n "$phantom" ]; then
  echo "❌ README rows with NO matching skills/<name>/ directory:"
  echo "$phantom" | sed 's/^/   - /'
  status=1
fi

if [ "$status" -eq 0 ]; then
  echo "✅ README skill list matches disk ($(echo "$fs_slugs" | wc -l | tr -d ' ') skills)."
fi
exit "$status"

# CI verification: no-op trigger (revert before merge)
