from __future__ import annotations

from llm_observability.config import settings
from llm_observability.evaluator import Evaluator
from llm_observability.schemas import EvaluationRequest, EvaluationResult, HealthResponse
from llm_observability.tracing import append_trace


class ObservabilityService:
    def __init__(self) -> None:
        self.evaluator = Evaluator()

    def health(self) -> HealthResponse:
        return HealthResponse(
            status='ok',
            service_name=settings.service_name,
            environment=settings.environment,
            evaluator_version=settings.evaluator_version,
        )

    def evaluate(self, request: EvaluationRequest) -> EvaluationResult:
        result = self.evaluator.evaluate(request)
        append_trace(
            {
                'run_id': result.run_id,
                'app_name': request.app_name,
                'prompt_version': request.prompt_version,
                'environment': request.environment,
                'user_id': request.user_id,
                'session_id': request.session_id,
                'request': request.model_dump(),
                'result': result.model_dump(),
            },
            path=settings.trace_store_path,
        )
        return result
