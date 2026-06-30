---
name: qdash-reporting
description: Create user-facing QDash reports from qdash-client data. Use when a user asks for daily or weekly calibration summaries, chip health reports, experiment reports, incident reports, workflow execution summaries, issue summaries, trend reports, or concise status updates from QDash.
---

# QDash Reporting

Use this skill to produce concise reports from QDash data. Load `qdash-core` access rules first when credentials, profiles, or helper command syntax are not already clear.

## Workflow

1. Clarify report scope only if it cannot be inferred: chip, project, date range, audience, and desired report type.
2. Gather high-signal data first: `default-chip`, `metrics-config`, `chip-metrics`, `task-results`, `issues`, `executions`, `ai-reviews`, and `provenance-changes`.
3. Pull details only for outliers, failed executions, open issues, or changed parameters.
4. Summarize in a report format suited to the user: executive status, calibration engineer handoff, incident update, or experiment log.
5. Include a short evidence appendix when useful: IDs and timestamps, not raw JSON.

## Helper Commands

```bash
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local default-chip
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local chip-metrics --chip-id chip-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local task-results --limit 50 --chip-id chip-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local issues --limit 20 --is-closed false
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local executions --limit 20
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local provenance-changes --within-hours 24
```

## Output

- Use concrete dates and UTC timestamps from QDash where available.
- Lead with status and changes since the last relevant period.
- Keep recommendations tied to evidence.
- Avoid dumping tables unless the user asks for a table.
