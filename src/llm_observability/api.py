from fastapi import FastAPI

from llm_observability.schemas import EvaluationRequest, EvaluationResult, HealthResponse
from llm_observability.service import ObservabilityService

app = FastAPI(title='LLM Observability Evaluation Suite', version='0.2.0')

_service = ObservabilityService()


@app.get('/health', response_model=HealthResponse)
def health() -> HealthResponse:
    return _service.health()


@app.post('/evaluate', response_model=EvaluationResult)
def evaluate(request: EvaluationRequest) -> EvaluationResult:
    return _service.evaluate(request)
