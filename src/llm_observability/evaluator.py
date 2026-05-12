from __future__ import annotations

from llm_observability.metrics import cost_score, latency_score, quality_score, safety_score
from llm_observability.schemas import EvaluationRequest, EvaluationResult


class Evaluator:
    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        q_score = quality_score(request.response, request.expected_keywords)
        s_score, issues = safety_score(request.prompt + ' ' + request.response)
        l_score = latency_score(request.latency_ms)
        c_score = cost_score(request.cost_usd)
        overall = round((q_score + s_score + l_score + c_score) / 4, 4)
        return EvaluationResult(
            quality_score=q_score,
            safety_score=s_score,
            latency_score=l_score,
            cost_score=c_score,
            overall_score=overall,
            issues=issues,
        )
