from typing import Any, Dict


def task_run_in_conda() -> Dict[str, Any]:
    return {
        "actions": [["conda", "run", "-n", "sywlite", "python", "--version"]],
        "verbosity": 2,
    }
