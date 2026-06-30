---
name: qdash-calibration-inspector
description: Inspect QDash calibration state for users through qdash-client profiles. Use when a user asks about chip health, qubit or coupling metrics, task results, time-series trends, degraded parameters, calibration anomalies, AI review findings, notes, figures, or experiment quality in QDash.
---

# QDash Calibration Inspector

Use this skill to answer calibration-health questions from QDash data. Load `qdash-core` access rules first when credentials, profiles, or helper command syntax are not already clear.

## Workflow

1. Establish context: profile, project, chip, date or time range, target qid/coupling, and parameter names. If missing, use `default-chip`, `metrics-config`, and focused list commands before asking the user.
2. Gather current state before history: `chip-metrics`, `chip-qubits`, `chip-couplings`, `qubit-latest`, `coupling-latest`, and `task-results`.
3. For anomalies or drift, fetch history with `timeseries`, `qubit-history`, `coupling-history`, and recent `task-result` details.
4. Cross-check interpretation with `task-knowledge`, `task-knowledge-markdown`, `task-note`, `task-result-issues`, and `ai-reviews` when available.
5. Summarize as a calibration finding: affected targets, metric values, thresholds if known, trend direction, evidence IDs, and practical next steps.

## Helper Commands

Use the shared helper from `qdash-core`:

```bash
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local default-chip
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local metrics-config
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local chip-metrics --chip-id chip-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local qubit-latest --task t1 --chip-id chip-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local coupling-latest --task cz_error_rate --chip-id chip-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local timeseries --parameter t1 --qid Q00 --start-at 2026-06-01T00:00:00Z --end-at 2026-06-08T00:00:00Z
```

## Output

- Lead with the answer, not raw JSON.
- Include enough IDs to let the user inspect the same records: chip ID, qid/coupling ID, task ID, run date, review run ID, or issue ID.
- Distinguish measured facts from inferred diagnosis.
- Do not recommend excluding, re-executing, or editing task results without explicit user confirmation.
