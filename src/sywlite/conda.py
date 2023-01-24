from typing import Any, Dict
import hashlib
from pathlib import Path


def get_conda_environment_prefix(environment_file: str) -> Dict[str, Any]:
    with open(environment_file, "rb") as f:
        file_hash = hashlib.sha1(f.read()).hexdigest()
    return {"prefix": Path(".sywlite") / "conda" / file_hash}


def create_conda_enironment(environment_file: str) -> Dict[str, Any]:
    with open(environment_file, "rb") as f:
        file_hash = hashlib.sha1(f.read()).hexdigest()

    return {
        "file_dep": [environment_file],
        "actions": [
            [
                "mamba",
                "create",
                "-f",
                environment_file,
                "-p",
                ".sywlite/conda/{}".format(file_hash),
            ]
        ],
    }


class conda_task:
    cache: Dict[str, Any]

    def __init__(self, environment_file: str):
        self.environment_file = environment_file

    def __call__(self, func):
        pass
