from llm_observability.evaluator import Evaluator
from llm_observability.schemas import EvaluationRequest


def test_evaluator_returns_scores():
    request = EvaluationRequest(
        prompt='Explain RAG evaluation',
        response='RAG evaluation tracks retrieval quality and latency.',
        expected_keywords=['retrieval', 'quality'],
        latency_ms=500,
        cost_usd=0.001,
    )
    result = Evaluator().evaluate(request)
    assert result.overall_score > 0.5
    assert result.issues == []
