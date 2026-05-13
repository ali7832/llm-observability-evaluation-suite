from __future__ import annotations

from llm_observability.config import settings
from llm_observability.schemas import EvaluationRequest


def evaluate_alerts(request: EvaluationRequest, quality_score: float, safety_score: float) -> list[str]:
    alerts: list[str] = []

    if quality_score < settings.quality_alert_threshold:
        alerts.append('low_quality_score')
    if safety_score < 1.0:
        alerts.append('safety_issue_detected')
    if request.latency_ms > settings.latency_alert_threshold_ms:
        alerts.append('latency_threshold_breached')
    if request.cost_usd > settings.cost_alert_threshold_usd:
        alerts.append('cost_threshold_breached')

    return alerts
