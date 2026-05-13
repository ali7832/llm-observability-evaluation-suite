from llm_observability.schemas import EvaluationRequest
from llm_observability.service import ObservabilityService


def test_observability_service_returns_run_metadata():
    request = EvaluationRequest(
        prompt='Explain RAG evaluation.',
        response='RAG evaluation tracks retrieval quality, latency, and cost.',
        expected_keywords=['retrieval', 'quality', 'latency'],
        app_name='rag-assistant',
        prompt_version='v2',
        latency_ms=700,
        cost_usd=0.02,
    )

    result = ObservabilityService().evaluate(request)

    assert result.run_id
    assert result.app_name == 'rag-assistant'
    assert result.prompt_version == 'v2'
    assert result.evaluator_version
    assert 0 <= result.overall_score <= 1


def test_observability_service_health_metadata():
    health = ObservabilityService().health()

    assert health.status == 'ok'
    assert health.service_name
    assert health.evaluator_version
