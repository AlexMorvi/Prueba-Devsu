import os
import subprocess
import sys
from pathlib import Path


def run_tests() -> int:
    """Run the E2E tests"""
    base_dir = Path(__file__).resolve().parent
    reports_dir = base_dir / "reports"
    reports_dir.mkdir(exist_ok=True)

    config_path = base_dir / "pytest.ini"
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-c",
        str(config_path),
        "--rootdir",
        str(base_dir),
    ]
    marker = os.getenv("PYTEST_MARKER")
    if marker:
        command.extend(["-m", marker])

    result = subprocess.run(command, cwd=base_dir)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(run_tests())
