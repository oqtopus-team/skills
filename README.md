# OQTOPUS Skills

Agent skills for OQTOPUS products.

This repository collects reusable instructions, helper scripts, and reference material for coding agents. Each skill is kept self-contained so it can be installed independently.

## Skills

Skills are organized by product. Each product owns a set of user-facing capabilities, with a `*-core` skill for shared access, authentication, and safety rules.

| Product | Capabilities | Purpose |
| --- | --- | --- |
| [QDash](skills/qdash/) | [`core`](skills/qdash/qdash-core/SKILL.md), [`calibration-inspector`](skills/qdash/qdash-calibration-inspector/SKILL.md), [`workflow-operator`](skills/qdash/qdash-workflow-operator/SKILL.md), [`issue-triage`](skills/qdash/qdash-issue-triage/SKILL.md), [`provenance-analyst`](skills/qdash/qdash-provenance-analyst/SKILL.md), [`reporting`](skills/qdash/qdash-reporting/SKILL.md) | Connect agents to QDash and help users inspect calibration state, operate workflows, triage issues, analyze provenance, and create reports. |

### QDash

QDash skills let agents access QDash through `qdash-client` profiles and work with project-scoped calibration data without exposing credentials.

| Capability | Skill | Use when |
| --- | --- | --- |
| Core access | [`qdash-core`](skills/qdash/qdash-core/SKILL.md) | Connecting to QDash, discovering profiles, using read-only API helpers, or applying shared safety rules. |
| Calibration inspection | [`qdash-calibration-inspector`](skills/qdash/qdash-calibration-inspector/SKILL.md) | Inspecting chip health, qubit/coupling metrics, task results, trends, AI reviews, and calibration anomalies. |
| Workflow operation | [`qdash-workflow-operator`](skills/qdash/qdash-workflow-operator/SKILL.md) | Inspecting flows, templates, helper files, executions, schedules, file state, and run readiness. |
| Issue triage | [`qdash-issue-triage`](skills/qdash/qdash-issue-triage/SKILL.md) | Triage of issues, issue knowledge, task-result issues, AI review findings, notes, and support context. |
| Provenance analysis | [`qdash-provenance-analyst`](skills/qdash/qdash-provenance-analyst/SKILL.md) | Explaining parameter lineage, changes, impact, degradation trends, and provenance recommendations. |
| Reporting | [`qdash-reporting`](skills/qdash/qdash-reporting/SKILL.md) | Creating daily, weekly, incident, workflow, and experiment reports from QDash data. |

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

Install a product's skills directly from this repository:

```bash
scripts/install-product-skills.sh qdash --agent codex --scope user
```

While QDash is the only product in this repository, this also installs all skills:

```bash
gh skill install oqtopus-team/skills --all --agent codex --scope user
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
