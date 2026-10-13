"""Export frozen public schemas/examples. --check is read-only and fails on drift."""

import argparse
import json
from pathlib import Path

from llm_wiki_mcp.contracts.catalog import CATALOG
from llm_wiki_mcp.contracts.examples import examples


def export() -> str:
    cases = examples()
    inventory = []
    for tool in CATALOG:
        example = cases[tool.name]
        request = tool.input_model.model_validate(example["input"])
        response = tool.output_model.model_validate(example["output"])
        inventory.append(
            {
                "name": tool.name,
                "category": tool.category,
                "phase": tool.phase,
                "scope": tool.scope,
                "required_scopes": tool.required_scopes,
                "owner_required": tool.owner_required,
                "annotations": tool.annotations,
                "max_result_bytes": tool.max_result_bytes,
                "error_codes": [e.value for e in tool.errors],
                "input_schema": tool.input_model.model_json_schema(),
                "output_schema": tool.output_model.model_json_schema(),
                "example": {
                    "input": request.model_dump(mode="json"),
                    "output": response.model_dump(mode="json"),
                },
            }
        )
    return (
        json.dumps(
            {"schema_version": "1.0", "tools": inventory},
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = Path(__file__).resolve().parents[1] / "contracts" / "catalog.json"
    content = export()
    if args.check:
        if not path.exists() or path.read_text() != content:
            raise SystemExit("Frozen contracts differ; review changes before exporting")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


if __name__ == "__main__":
    main()
