# Operations Runbook

## Purpose

This service evaluates LLM application outputs and records structured traces for quality, safety, latency, and cost monitoring.

## Runtime Configuration

Configuration is controlled through `.env.example`:

- `LLMOBS_ENV`: deployment environment.
- `LLMOBS_SERVICE_NAME`: service identifier.
- `LLMOBS_EVALUATOR_VERSION`: evaluator version returned in every result.
- `LLMOBS_TRACE_STORE_PATH`: JSONL trace output path.
- `LLMOBS_QUALITY_ALERT_THRESHOLD`: minimum acceptable quality score.
- `LLMOBS_COST_ALERT_THRESHOLD_USD`: cost alert threshold.
- `LLMOBS_LATENCY_ALERT_THRESHOLD_MS`: latency alert threshold.

## Evaluation Lifecycle

1. An app submits prompt, response, expected keywords, latency, and cost to `/evaluate`.
2. The evaluator calculates quality, safety, latency, cost, and overall score.
3. Alert policy checks quality, safety, latency, and cost thresholds.
4. A run ID and evaluator version are attached to the result.
5. The request/result pair is written to the JSONL trace stream.

## Demo Readiness

For hosted demos, expose `/health` and `/evaluate`. The health endpoint returns service name, environment, and evaluator version.

## Production Roadmap

- Store traces in PostgreSQL or ClickHouse.
- Add dashboard views for prompt versions and app-level trends.
- Add LLM-as-judge evaluators.
- Add RAG-specific metrics for retrieval quality and citation faithfulness.
- Add alert integrations for Slack, PagerDuty, or email.
- Add scheduled regression test suites for prompt releases.
