# LLM Observability Evaluation Suite

Deployable LLMOps evaluation service for monitoring prompt quality, safety, latency, cost, alerts, and traceability across LLM applications.

## Core Capabilities

- Prompt and response evaluation API
- Quality, safety, latency, and cost scoring
- Run IDs for evaluation traceability
- App name, prompt version, user, and session metadata
- Configurable alert thresholds for quality, cost, and latency
- Evaluator version returned with every result
- JSONL trace stream for local demo and audit workflows
- FastAPI `/evaluate` endpoint
- CLI workflows for demo and one-off evaluation
- Runtime configuration through environment variables
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest coverage
- Operations runbook and architecture decision record

## Quickstart

```bash
pip install .[dev]
llmobs demo
uvicorn llm_observability.api:app --reload
pytest -q
```

## API

```bash
curl http://localhost:8000/health
curl -X POST http://localhost:8000/evaluate \
  -H 'Content-Type: application/json' \
  -d @sample_eval.json
```

## Docker

```bash
docker-compose up --build
```

## Runtime Configuration

See `.env.example` for environment, evaluator version, trace store, and alert threshold settings.

## Documentation

- `ARCHITECTURE.md`
- `DEPLOYMENT.md`
- `OPERATIONS.md`
- `docs/adr-001-evaluation-service-layer.md`
- `sample_eval.json`

## Production Roadmap

- Database-backed trace storage
- Prompt/version dashboards
- LLM-as-judge evaluators
- RAG faithfulness and retrieval metrics
- Alert integrations
- Scheduled regression suites for prompt releases
