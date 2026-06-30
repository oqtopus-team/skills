#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage: scripts/install-product-skills.sh <product> [gh skill install flags...]

Examples:
  scripts/install-product-skills.sh qdash --agent codex --scope user
  scripts/install-product-skills.sh qdash --agent codex --scope user --force

Installs every skill under skills/<product>/ from this repository.
EOF
}

if [[ $# -lt 1 ]]; then
  usage
  exit 2
fi

product="$1"
shift

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
product_dir="$repo_root/skills/$product"

if [[ ! -d "$product_dir" ]]; then
  echo "error: product not found: $product" >&2
  exit 1
fi

mapfile -t skill_names < <(
  find "$product_dir" -mindepth 2 -maxdepth 2 -name SKILL.md -print \
    | while IFS= read -r skill_file; do
        sed -n 's/^name:[[:space:]]*//p' "$skill_file" | head -1
      done \
    | sort
)

if [[ ${#skill_names[@]} -eq 0 ]]; then
  echo "error: no skills found under $product_dir" >&2
  exit 1
fi

for skill_name in "${skill_names[@]}"; do
  echo "Installing $product/$skill_name"
  gh skill install "$repo_root" "$skill_name" --from-local "$@"
done
