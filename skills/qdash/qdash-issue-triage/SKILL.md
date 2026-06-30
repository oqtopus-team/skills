---
name: qdash-issue-triage
description: Triage QDash issues and support knowledge for users through qdash-client profiles. Use when a user asks about open issues, known calibration problems, issue knowledge, task-result issues, AI review notes, forum posts, incident summaries, root-cause clues, or recommended follow-up in QDash.
---

# QDash Issue Triage

Use this skill to turn QDash issue and knowledge data into an actionable triage summary. Load `qdash-core` access rules first when credentials, profiles, or helper command syntax are not already clear.

## Workflow

1. Identify the scope: chip, qid/coupling, task name, date range, open/closed status, severity, or user-reported symptom.
2. Start with `issues`, `issue-knowledge`, `task-result-issues`, and `ai-reviews`.
3. Pull supporting evidence from `task-result`, `task-note`, `task-knowledge`, `qubit-latest`, `coupling-latest`, and recent history when needed.
4. Group related findings by symptom, target, task, or likely cause.
5. Recommend concrete next steps: inspect records, compare history, run a workflow, create/update an issue, or approve/reject knowledge. Ask before any write action.

## Helper Commands

```bash
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local issues --limit 20 --is-closed false
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local issue-knowledge --status approved --limit 20
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local task-result-issues --task-id task-001
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local ai-reviews --chip-id chip-001 --limit 20
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local task-note --task-id task-001
```

## Output

- Start with priority: urgent, needs follow-up, informational, or resolved.
- Include issue IDs, task IDs, review IDs, affected targets, and dates.
- Call out uncertainty when evidence is circumstantial.
- Do not close, reopen, extract knowledge, approve, reject, or post replies without explicit user confirmation.
