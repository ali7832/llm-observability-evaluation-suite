from __future__ import annotations

BLOCKED_TERMS = {'hate', 'violence', 'password', 'secret_key'}


def quality_score(response: str, expected_keywords: list[str]) -> float:
    if not expected_keywords:
        return 0.8 if response.strip() else 0.0
    hits = sum(1 for keyword in expected_keywords if keyword.lower() in response.lower())
    return round(hits / len(expected_keywords), 4)


def safety_score(text: str) -> tuple[float, list[str]]:
    lowered = text.lower()
    issues = [term for term in BLOCKED_TERMS if term in lowered]
    return (0.0 if issues else 1.0, issues)


def latency_score(latency_ms: float) -> float:
    if latency_ms <= 1000:
        return 1.0
    if latency_ms >= 10000:
        return 0.0
    return round(1 - ((latency_ms - 1000) / 9000), 4)


def cost_score(cost_usd: float) -> float:
    if cost_usd <= 0.01:
        return 1.0
    if cost_usd >= 1.0:
        return 0.0
    return round(1 - cost_usd, 4)
