import yaml
import json
from pathlib import Path

def parse_spec(spec_path: str) -> dict:
    """Parses an OpenAPI spec file and extracts relevant information."""
    path = Path(spec_path)
    with open(path) as f:
        if path.suffix in (".yaml", ".yml"):
            spec = yaml.safe_load(f)
        else:
            spec = json.load(f)

    parsed_spec = {"operations": []}
    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method in ["get", "post"]:
                op_data = {
                    "path": path,
                    "method": method.upper(),
                    "name": operation.get("operationId"),
                    "description": operation.get("description") or operation.get("summary"),
                    "params": [],
                    "requestBody": None,
                }

                for param in operation.get("parameters", []) :
                    if param.get("in") in ["path", "query"]:
                        op_data["params"].append(
                            {
                                "name": param["name"],
                                "in": param["in"],
                                "required": param.get("required", False),
                            }
                        )

                if "requestBody" in operation:
                    content = operation["requestBody"].get("content", {})
                    if "application/json" in content:
                        op_data["requestBody"] = {
                            "schema": content["application/json"].get("schema", {})
                        }

                parsed_spec["operations"].append(op_data)

    return parsed_spec
