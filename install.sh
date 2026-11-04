#!/usr/bin/env sh
# Links every bstack skill in this repo into an agent's skills folder, so edits in the repo apply at once.
set -e

repo_dir="$(cd "$(dirname "$0")" && pwd)"
skills_dir="${1:-$HOME/.claude/skills}"
mkdir -p "$skills_dir"

for skill in "$repo_dir"/*/; do
    [ -f "$skill/SKILL.md" ] || continue
    name="$(basename "$skill")"
    link="$skills_dir/$name"

    if [ -e "$link" ] && [ ! -L "$link" ]; then
        echo "Skipped $name: $link is a real folder. Move it away and run again." >&2
        continue
    fi

    ln -sfn "${skill%/}" "$link"
    echo "Linked $name into $skills_dir"
done
