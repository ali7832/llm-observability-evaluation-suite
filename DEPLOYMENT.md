# Deployment Guide

## Local Development

```bash
pip install .[dev]
uvicorn llm_observability.api:app --reload
```

## CLI Demo

```bash
llmobs demo
llmobs evaluate
```

## Docker

```bash
docker build -t llm-observability .
docker run -p 8000:8000 llm-observability
```

## Docker Compose

```bash
docker-compose up --build
```

## Health Check

```bash
curl http://localhost:8000/health
```

## Evaluate Endpoint

```bash
curl -X POST http://localhost:8000/evaluate \
  -H 'Content-Type: application/json' \
  -d @sample_eval.json
```
