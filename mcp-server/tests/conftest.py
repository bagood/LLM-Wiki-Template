import json
import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = Path(os.environ.get("P0_ARTIFACT_DIR", ROOT / "artifacts/validation/p0"))


@pytest.fixture
def artifacts() -> Path:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    return ARTIFACTS


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    (ARTIFACTS / "test-execution.json").write_text(
        json.dumps(
            {
                "exit_status": exitstatus,
                "collected": session.testscollected,
                "failed": session.testsfailed,
            },
            indent=2,
        )
        + "\n"
    )
