from fastapi import FastAPI

from llm_observability.evaluator import Evaluator
from llm_observability.schemas import EvaluationRequest, EvaluationResult
from llm_observability.tracing import append_trace

app = FastAPI(title='LLM Observability Evaluation Suite')
_evaluator = Evaluator()


@app.get('/health')
def health() -> dict:
    return {'status': 'ok'}


@app.post('/evaluate', response_model=EvaluationResult)
def evaluate(request: EvaluationRequest) -> EvaluationResult:
    result = _evaluator.evaluate(request)
    append_trace({'request': request.model_dump(), 'result': result.model_dump()})
    return result
