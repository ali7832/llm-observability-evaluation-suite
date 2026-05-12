import typer
from rich.console import Console

from llm_observability.evaluator import Evaluator
from llm_observability.schemas import EvaluationRequest

app = typer.Typer(help='LLM observability evaluation CLI')
console = Console()


@app.command()
def evaluate(
    prompt: str = 'Explain RAG evaluation.',
    response: str = 'RAG evaluation measures retrieval quality, answer quality, citations, latency, and cost.',
) -> None:
    request = EvaluationRequest(
        prompt=prompt,
        response=response,
        expected_keywords=['retrieval', 'quality', 'latency', 'cost'],
        latency_ms=850,
        cost_usd=0.01,
    )
    result = Evaluator().evaluate(request)
    console.print_json(data=result.model_dump())


@app.command()
def demo() -> None:
    evaluate()
