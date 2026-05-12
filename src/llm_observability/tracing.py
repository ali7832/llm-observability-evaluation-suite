from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


def append_trace(payload: dict, path: str | Path = 'traces.jsonl') -> None:
    record = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    with Path(path).open('a', encoding='utf-8') as handle:
        handle.write(json.dumps(record) + '\n')
