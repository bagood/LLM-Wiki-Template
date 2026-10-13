import ast
import importlib.util
from pathlib import Path

PACKAGE = Path(__file__).resolve().parents[2] / "src/llm_wiki_mcp"
FORBIDDEN: dict[str, set[str]] = {
    "domain": {
        "controllers",
        "services",
        "repositories",
        "contracts",
        "container",
        "app",
        "config",
    },
    "contracts": {"controllers", "services", "repositories", "container", "app", "config"},
    "services": {"controllers", "container", "app", "config"},
    "repositories": {"controllers", "services", "contracts", "container", "app", "config"},
}
TRANSPORT = {"mcp", "mcp_types", "fastapi", "starlette", "uvicorn", "httpx", "httpx2"}
PROVIDERS = {"openai", "anthropic", "google.genai", "azure.ai"}


def imported_modules(source: str, package: str) -> set[str]:
    modules: set[str] = set()
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            modules.update(a.name for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if node.level:
                module = importlib.util.resolve_name("." * node.level + module, package)
            modules.add(module)
            modules.update(f"{module}.{a.name}" for a in node.names)
        elif isinstance(node, ast.Call):
            if (isinstance(node.func, ast.Name) and node.func.id == "__import__") or (
                isinstance(node.func, ast.Attribute) and node.func.attr == "import_module"
            ):
                if not node.args or not isinstance(node.args[0], ast.Constant):
                    raise AssertionError("Uninspectable dynamic package import")
                modules.add(str(node.args[0].value))
    return modules


def violations(layer: str, imports: set[str]) -> set[str]:
    blocked = FORBIDDEN.get(layer, set())
    return {
        m
        for m in imports
        if (
            (m.startswith("llm_wiki_mcp.") and m.split(".")[1] in blocked)
            or (layer in FORBIDDEN and m.split(".")[0] in TRANSPORT)
            or any(m == p or m.startswith(p + ".") for p in PROVIDERS)
        )
    }


def test_real_package_import_boundaries() -> None:
    inspected = 0
    for path in PACKAGE.rglob("*.py"):
        rel = path.relative_to(PACKAGE)
        layer = rel.parts[0]
        package = ".".join(("llm_wiki_mcp", *rel.parts[:-1]))
        bad = violations(layer, imported_modules(path.read_text(), package))
        assert not bad, f"{rel}: forbidden imports {bad}"
        inspected += 1
    assert inspected >= 20


def test_boundary_checker_detects_absolute_relative_and_dynamic_imports() -> None:
    for source in (
        "from llm_wiki_mcp.controllers.mcp import probe",
        "from ..controllers import mcp",
        "from .. import controllers",
        "import fastapi",
        'importlib.import_module("llm_wiki_mcp.controllers.mcp")',
    ):
        assert violations("services", imported_modules(source, "llm_wiki_mcp.services"))
