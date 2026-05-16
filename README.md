# LLM Observability Evaluation Suite

Deployable LLMOps evaluation service for monitoring prompt quality, safety, latency, cost, alerts, and traceability across LLM applications, with a premium multi-page React command center for AI platform teams.

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
- Multi-page React/Vite LLMOps observability frontend

## Quickstart

```bash
pip install .[dev]
llmobs demo
uvicorn llm_observability.api:app --reload
pytest -q
```

## Frontend LLMOps Control Center

The `frontend/` directory contains a premium React/Vite dashboard for LLM monitoring, evaluation, prompt regression, and release governance.

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

Frontend pages:

- Overview: evaluation volume, quality, latency, cost, and trend charts
- Live Traces: prompt trace stream with app, version, score, cost, and latency
- Evaluation Lab: interactive prompt/response quality and safety evaluation
- Regression Suite: prompt release regression runs and golden-test scorecards
- Model Compare: quality-vs-cost comparison across model choices
- Alerts: quality, latency, and cost alert center
- Release Gates: release decision panel with quality, safety, latency, and budget thresholds

The UI attempts to call `/evaluate` and falls back to demo LLMOps intelligence when the backend is offline.

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
