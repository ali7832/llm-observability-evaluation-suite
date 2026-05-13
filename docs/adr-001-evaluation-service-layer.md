# ADR-001: Evaluation Service Layer and Trace Metadata

## Status

Accepted

## Context

LLM applications need quality monitoring that is traceable by app, prompt version, user session, latency, cost, and evaluator version. A direct API-to-evaluator call is simple, but it does not provide enough operational metadata for demo or production review.

## Decision

Introduce an `ObservabilityService` that owns evaluator execution, health metadata, alert policy, trace persistence, and response metadata. Every evaluation receives a run ID and evaluator version.

## Consequences

Benefits:

- API routes remain thin and deployable.
- Every result can be traced by run ID.
- Alerts are generated consistently from configurable thresholds.
- App and prompt-version metadata support release comparisons.

Tradeoffs:

- JSONL trace storage is suitable for local demo mode, but production systems should use a database or observability backend.
- Heuristic metrics are fast and transparent, but production systems should add LLM-as-judge and task-specific evaluators.
