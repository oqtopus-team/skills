---
name: qdash-workflow-operator
description: Operate and inspect QDash workflows for users through qdash-client profiles. Use when a user asks about flows, flow templates, helper files, executions, schedules, execution status, workflow files, git status, run readiness, failed runs, cancellation, re-execution, or safe workflow operation in QDash.
---

# QDash Workflow Operator

Use this skill to help users understand and operate QDash workflows. Load `qdash-core` access rules first when credentials, profiles, or helper command syntax are not already clear.

## Workflow

1. Inspect before acting: list `flows`, `flow-templates`, `flow-helper-files`, `executions`, `files-tree`, and `git-status` as needed.
2. For a named flow, fetch `flow`, relevant helper files, template details, and recent executions before recommending action.
3. For failed or slow runs, inspect `execution`, task results, task notes, related issues, and provenance if the user asks why outputs changed.
4. For run readiness, report missing helper files, changed git state, required template parameters, current lock status if available, and recent failure patterns.
5. Before execute, re-execute, cancel, git push/pull, create/update/delete, or file writes, state the exact action and wait for explicit user confirmation.

## Helper Commands

```bash
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local flows
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local flow --flow-name calibration_demo
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local flow-templates
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local flow-helper-files
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local executions --limit 20
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local files-tree
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local git-status
```

## Output

- Separate current state, suspected cause, and recommended next action.
- Include flow names, execution IDs, file paths, schedule IDs, and timestamps.
- Treat operational actions as sensitive even when the API endpoint is available through a GET-like workflow.
