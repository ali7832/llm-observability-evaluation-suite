from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class ObservabilitySettings:
    environment: str = os.getenv('LLMOBS_ENV', 'local')
    service_name: str = os.getenv('LLMOBS_SERVICE_NAME', 'llm-observability-evaluation-suite')
    evaluator_version: str = os.getenv('LLMOBS_EVALUATOR_VERSION', 'heuristic-evaluator-v1')
    trace_store_path: str = os.getenv('LLMOBS_TRACE_STORE_PATH', 'traces.jsonl')
    quality_alert_threshold: float = float(os.getenv('LLMOBS_QUALITY_ALERT_THRESHOLD', '0.60'))
    cost_alert_threshold_usd: float = float(os.getenv('LLMOBS_COST_ALERT_THRESHOLD_USD', '0.25'))
    latency_alert_threshold_ms: float = float(os.getenv('LLMOBS_LATENCY_ALERT_THRESHOLD_MS', '5000'))


settings = ObservabilitySettings()
