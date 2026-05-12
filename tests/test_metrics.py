from llm_observability.metrics import cost_score, latency_score, quality_score, safety_score


def test_quality_score_with_keywords():
    score = quality_score('retrieval quality and cost are tracked', ['retrieval', 'quality', 'cost'])
    assert score == 1.0


def test_safety_score_flags_blocked_terms():
    score, issues = safety_score('do not expose a secret_key')
    assert score == 0.0
    assert 'secret_key' in issues


def test_latency_and_cost_scores():
    assert latency_score(500) == 1.0
    assert cost_score(0.001) == 1.0
