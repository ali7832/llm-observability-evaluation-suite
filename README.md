# LLM Observability Evaluation Suite

Production-ready platform for evaluating, logging, and monitoring LLM application quality across prompts, responses, latency, cost, safety, and retrieval quality.

## Features

- Prompt/response trace logging
- Evaluation metrics for quality, latency, cost, and safety
- Dataset-based offline evaluation
- FastAPI evaluation API
- CLI workflows for demo and batch evaluation
- JSONL trace storage
- Docker and Docker Compose deployment
- GitHub Actions CI
- Pytest test suite

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

## Portfolio Highlights

- Demonstrates LLMOps, model evaluation, observability, API design, and production engineering
- Useful for RAG, chatbot, agent, and prompt-engineering workflows
- Clear foundation for LangSmith-style tracing, dashboards, and production monitoring
