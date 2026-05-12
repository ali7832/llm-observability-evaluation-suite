from __future__ import annotations

from pydantic import BaseModel


class EvaluationRequest(BaseModel):
    prompt: str
    response: str
    expected_keywords: list[str] = []
    latency_ms: float = 0.0
    cost_usd: float = 0.0


class EvaluationResult(BaseModel):
    quality_score: float
    safety_score: float
    latency_score: float
    cost_score: float
    overall_score: float
    issues: list[str]
