"""Maps dotted event_type -> generated pydantic model for payload validation.

Models come from the shared contract (lifeos_shared.generated, produced by
`scripts/codegen_py.sh`). If a model is unavailable, validation for that type is
skipped gracefully (the type must still be registered/known).
"""

from __future__ import annotations

import importlib
import json
import re
from functools import cache
from pathlib import Path
from typing import Any

from pydantic import BaseModel


def _snake(pascal: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", pascal).lower()


def _event_type_map() -> dict[str, str]:
    root = Path(__file__).resolve().parents[4]
    constants = root / "packages" / "shared" / "schema" / "constants.json"
    data = json.loads(constants.read_text(encoding="utf-8"))
    # dotted -> PascalCase
    return {dotted: pascal for pascal, dotted in data.get("eventTypes", {}).items()}


@cache
def _models() -> dict[str, type[BaseModel]]:
    mapping: dict[str, type[BaseModel]] = {}
    for dotted, pascal in _event_type_map().items():
        module_name = f"lifeos_shared.generated.{_snake(pascal)}_schema"
        try:
            module = importlib.import_module(module_name)
            mapping[dotted] = getattr(module, pascal)
        except (ModuleNotFoundError, AttributeError):
            continue
    return mapping


def known_event_types() -> set[str]:
    return set(_event_type_map().keys())


def validate_payload(event_type: str, payload: dict[str, Any]) -> None:
    """Raise pydantic ValidationError if the payload does not match the schema."""
    model = _models().get(event_type)
    if model is not None:
        model.model_validate(payload)
