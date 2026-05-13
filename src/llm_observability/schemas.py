from __future__ import annotations

from pydantic import BaseModel, Field


class EvaluationRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    response: str = Field(..., min_length=1)
    expected_keywords: list[str] = []
    latency_ms: float = Field(default=0.0, ge=0)
    cost_usd: float = Field(default=0.0, ge=0)
    app_name: str = 'default-app'
    prompt_version: str = 'v1'
    environment: str = 'local'
    user_id: str | None = None
    session_id: str | None = None


class EvaluationResult(BaseModel):
    run_id: str
    quality_score: float
    safety_score: float
    latency_score: float
    cost_score: float
    overall_score: float
    issues: list[str]
    alerts: list[str]
    evaluator_version: str
    app_name: str
    prompt_version: str


class HealthResponse(BaseModel):
    status: str
    service_name: str
    environment: str
    evaluator_version: str
