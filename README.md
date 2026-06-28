# OQTOPUS Skills

Agent skills for OQTOPUS products.

This repository collects reusable instructions, helper scripts, and reference material for coding agents. Each skill is kept self-contained so it can be installed independently.

## Skills

| Product | Skill | Purpose |
| --- | --- | --- |
| QDash | [`qdash`](skills/qdash/SKILL.md) | Inspect a running QDash instance through `qdash-client` profiles and read-only API helpers. |

## Layout

```text
skills/
└── <product>/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── scripts/
```

Use `skills/<product>/<skill>` if one product grows multiple independent skills. Keep a single product-level skill at `skills/<product>` while there is only one obvious entry point.

## Install

Install a skill directly from this repository:

```bash
gh skill install oqtopus-team/skills qdash --agent codex --scope user
```

For local development:

```bash
gh skill install . qdash --from-local --agent codex --scope user --force
```

## Validate

```bash
make validate
```

Validation checks skill frontmatter, required metadata, agent UI metadata, and Python helper syntax.
