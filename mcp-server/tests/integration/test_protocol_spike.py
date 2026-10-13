import asyncio
import hashlib
import json
import os
import signal
import socket
import subprocess
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import httpx
import jsonschema
import pytest
from mcp import Client
from mcp.shared.inbound import CLIENT_CAPABILITIES_META_KEY, PROTOCOL_VERSION_META_KEY
from mcp.types import HEADER_MISMATCH, INVALID_PARAMS, UNSUPPORTED_PROTOCOL_VERSION

ROOT = Path(__file__).resolve().parents[2]
PROVIDER_ENV_PREFIXES = ("OPENAI_", "ANTHROPIC_", "AZURE_OPENAI_", "GOOGLE_", "GEMINI_", "AWS_")


def original_hashes() -> dict[str, str]:
    root = ROOT.parent / "wiki-agentic-stock-analysis"
    return {
        p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted(root.rglob("*"))
        if p.is_file()
    }


@contextmanager
def live_server(artifacts: Path, name: str, *, probe: bool = True) -> Iterator[str]:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    env = {
        k: v
        for k, v in os.environ.items()
        if not k.startswith(PROVIDER_ENV_PREFIXES) and not k.startswith("LLM_WIKI_")
    }
    env["PYTHONUNBUFFERED"] = "1"
    factory = "create_dev_app" if probe else "create_app"
    log_path = artifacts / f"{name}-server.log"
    with log_path.open("w") as log:
        process = subprocess.Popen(
            [
                sys.executable,
                "-m",
                "uvicorn",
                f"llm_wiki_mcp.app:{factory}",
                "--factory",
                "--host",
                "127.0.0.1",
                "--port",
                str(port),
                "--no-access-log",
            ],
            cwd=ROOT,
            env=env,
            stdout=log,
            stderr=subprocess.STDOUT,
        )
        try:
            base = f"http://127.0.0.1:{port}"
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    pytest.fail(f"Server exited early: {log_path.read_text()}")
                try:
                    response = httpx.get(base + "/health/ready", timeout=0.3)
                    if response.status_code == 200 and response.json()["ready"]:
                        break
                except httpx.TransportError:
                    pass
                time.sleep(0.05)
            else:
                pytest.fail(f"Server never became ready: {log_path.read_text()}")
            yield base + "/mcp"
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
                pytest.fail("Uvicorn did not shut down cleanly")
    # Uvicorn re-raises the received signal after completing its graceful shutdown.
    assert process.returncode in (0, -signal.SIGTERM), log_path.read_text()
    assert "Application shutdown complete" in log_path.read_text()
    assert "Task group is not initialized" not in log_path.read_text()


@pytest.mark.parametrize("mode,version", [("auto", "2026-07-28"), ("legacy", "2025-11-25")])
def test_real_official_client_and_restart(mode: str, version: str, artifacts: Path) -> None:
    before = original_hashes()
    traces = []
    for restart in range(2):
        with live_server(artifacts, f"{mode}-{restart}") as url:

            async def exercise() -> None:
                async with Client(url, mode=mode) as client:
                    assert client.protocol_version == version
                    listed = await client.list_tools()
                    assert [t.name for t in listed.tools] == ["dev_protocol_probe"]
                    tool = listed.tools[0]
                    request = {"request": {"message": "P0 ✓", "repeat": 2}}
                    jsonschema.validate(request, tool.input_schema)
                    result = await client.call_tool(tool.name, request)
                    assert not result.is_error
                    assert result.structured_content == {
                        "schema_version": "1.0",
                        "echoes": ["P0 ✓", "P0 ✓"],
                        "provider_required": False,
                    }
                    jsonschema.validate(result.structured_content, tool.output_schema)
                    assert json.loads(result.content[0].text) == result.structured_content
                    bad = await client.call_tool(tool.name, {"request": {"repeat": 99}})
                    assert bad.is_error
                    assert not bad.structured_content
                    traces.append(
                        {
                            "mode": mode,
                            "protocol_version": client.protocol_version,
                            "request": request,
                            "tools": listed.model_dump(mode="json"),
                            "response": result.model_dump(mode="json"),
                            "malformed_input": bad.model_dump(mode="json"),
                        }
                    )

            asyncio.run(exercise())
    assert original_hashes() == before
    (artifacts / f"{mode}-client-trace.json").write_text(json.dumps(traces, indent=2) + "\n")
    (artifacts / "original-wiki-hashes.json").write_text(json.dumps(before, indent=2) + "\n")


def test_sdk_protocol_errors_and_endpoint_paths(artifacts: Path) -> None:
    traces = []
    with live_server(artifacts, "failures") as url, httpx.Client(follow_redirects=False) as http:
        meta = {PROTOCOL_VERSION_META_KEY: "2026-07-28", CLIENT_CAPABILITIES_META_KEY: {}}
        body = {"jsonrpc": "2.0", "id": 1, "method": "tools/list", "params": {"_meta": meta}}
        headers = {
            "accept": "application/json, text/event-stream",
            "mcp-protocol-version": "2026-07-28",
            "mcp-method": "tools/list",
        }
        response = http.post(url, json=body, headers=headers)
        assert response.status_code == 200 and response.json()["result"]["tools"]
        for path in (url + "/", url + "/mcp"):
            response = http.post(path, json=body, headers=headers)
            assert response.status_code == 404
            assert "location" not in response.headers
        tests = [
            (body, {**headers, "mcp-method": "tools/call"}, HEADER_MISMATCH),
            ({**body, "params": {}}, headers, INVALID_PARAMS),
            (
                {**body, "params": {"_meta": {**meta, PROTOCOL_VERSION_META_KEY: "2099-01-01"}}},
                {**headers, "mcp-protocol-version": "2099-01-01"},
                UNSUPPORTED_PROTOCOL_VERSION,
            ),
            (
                {
                    **body,
                    "method": "tools/call",
                    "params": {"_meta": meta, "name": "dev_protocol_probe", "arguments": {}},
                },
                {**headers, "mcp-method": "tools/call", "mcp-name": "different"},
                HEADER_MISMATCH,
            ),
            (
                {**body, "params": {"_meta": {**meta, PROTOCOL_VERSION_META_KEY: "2025-11-25"}}},
                headers,
                HEADER_MISMATCH,
            ),
        ]
        for request, sent_headers, code in tests:
            response = http.post(url, json=request, headers=sent_headers)
            assert response.status_code == 400, response.text
            assert response.json()["error"]["code"] == code, response.text
            traces.append(
                {
                    "request": request,
                    "headers": sent_headers,
                    "status": response.status_code,
                    "response": response.json(),
                }
            )
        response = http.post(
            url, content="{", headers={**headers, "content-type": "application/json"}
        )
        assert response.status_code == 400
        traces.append({"request": "{", "status": response.status_code, "response": response.json()})
    (artifacts / "protocol-failure-trace.json").write_text(json.dumps(traces, indent=2) + "\n")


def test_probe_is_explicitly_development_only(artifacts: Path) -> None:
    with live_server(artifacts, "probe-disabled", probe=False) as url:

        async def exercise() -> None:
            async with Client(url) as client:
                assert not (await client.list_tools()).tools

        asyncio.run(exercise())
