---
name: qdash-provenance-analyst
description: Analyze QDash provenance and parameter lineage for users through qdash-client profiles. Use when a user asks why a calibration value changed, what affected a parameter, lineage of qubit or coupling results, degradation trends, execution comparisons, downstream impact, or recalibration recommendations in QDash.
---

# QDash Provenance Analyst

Use this skill to explain where QDash values came from and what changed. Load `qdash-core` access rules first when credentials, profiles, or helper command syntax are not already clear.

## Workflow

1. Establish the entity: parameter name, qid or coupling ID, chip, date range, execution ID, or task ID.
2. Start broad with `provenance-stats` and `provenance-changes`, then narrow with `provenance-history` or `raw-get` for read-only provenance endpoints not yet exposed by the helper.
3. Compare provenance with metric history and task results when the user asks whether a change is meaningful.
4. For impact analysis, report upstream task inputs, downstream affected values, execution IDs, and recommendation records where available.
5. Keep causal language disciplined: use "correlates with" unless lineage data directly supports "caused by".

## Helper Commands

```bash
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local provenance-stats
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local provenance-changes --within-hours 24 --parameter-name t1
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local provenance-history --parameter-name t1 --qid Q00 --limit 20
uv run --with qdash-client python skills/qdash/qdash-core/scripts/qdash_query.py --profile local raw-get --path /provenance/compare --params '{"limit": 20}'
```

## Output

- Present a concise timeline when explaining changes.
- Include parameter, target, old/new values if available, execution IDs, and timestamps.
- Separate provenance facts, metric observations, and operational recommendations.
- Ask before triggering recalibration, re-execution, exclusion, or file changes.
