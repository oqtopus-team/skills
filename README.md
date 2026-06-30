# OQTOPUS Skills

Agent skills for OQTOPUS products.

This repository collects reusable instructions, helper scripts, and reference material for coding agents. Each skill is kept self-contained so it can be installed independently.

## Skills

Skills are organized by product, then by user-facing capability.

| Product | Skill | Purpose |
| --- | --- | --- |
| QDash | [`qdash-core`](skills/qdash/qdash-core/SKILL.md) | Connect agents to QDash through `qdash-client` profiles, read-only helpers, and shared safety rules. |
| QDash | [`qdash-calibration-inspector`](skills/qdash/qdash-calibration-inspector/SKILL.md) | Inspect chip health, qubit/coupling metrics, task results, trends, AI reviews, and calibration anomalies. |
| QDash | [`qdash-workflow-operator`](skills/qdash/qdash-workflow-operator/SKILL.md) | Inspect flows, templates, helper files, executions, schedules, file state, and run readiness. |
| QDash | [`qdash-issue-triage`](skills/qdash/qdash-issue-triage/SKILL.md) | Triage issues, issue knowledge, task-result issues, AI review findings, notes, and support context. |
| QDash | [`qdash-provenance-analyst`](skills/qdash/qdash-provenance-analyst/SKILL.md) | Analyze parameter lineage, changes, impact, degradation trends, and provenance recommendations. |
| QDash | [`qdash-reporting`](skills/qdash/qdash-reporting/SKILL.md) | Create daily, weekly, incident, workflow, and experiment reports from QDash data. |

## Layout

```text
skills/
└── <product>/
    └── <product>-<capability>/
        ├── SKILL.md
        ├── agents/
        ├── references/
        └── scripts/
```

Use `skills/<product>/<product>-<capability>` so product families can grow independently. Keep shared access, authentication, and safety behavior in a `*-core` skill, then put task-specific judgment in capability skills.

## Install

Install skills directly from this repository:

```bash
gh skill install oqtopus-team/skills qdash-core --agent codex --scope user
gh skill install oqtopus-team/skills qdash-calibration-inspector --agent codex --scope user
```

For local development:

```bash
gh skill install . qdash-core --from-local --agent codex --scope user --force
```

## Validate

```bash
make validate
```

Validation checks skill frontmatter, required metadata, agent UI metadata, and Python helper syntax.
