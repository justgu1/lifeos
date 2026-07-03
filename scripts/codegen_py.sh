#!/usr/bin/env bash
# Codegen: JSON Schema -> pydantic models (packages/shared/py).
# Single source of truth = packages/shared/schema/events/*.schema.json.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT="$ROOT/packages/shared/py/src/lifeos_shared/generated"
mkdir -p "$OUT"

uv run --with datamodel-code-generator datamodel-codegen \
  --input "$ROOT/packages/shared/schema/events" \
  --input-file-type jsonschema \
  --output "$OUT" \
  --output-model-type pydantic_v2.BaseModel \
  --formatters black isort

echo "[codegen-py] wrote pydantic models to $OUT"
