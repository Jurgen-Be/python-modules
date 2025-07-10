# version_manager/manager.py

# Import van de nodige modules
import toml
import subprocess
import os
from pathlib import Path

# Classes met functies
class VersionManager:
    def __init__(self, module_path="."):
        self.module_path = Path(module_path)
        self.toml_path = self.module_path/"pyproject.toml"
        self.version_py = self.module_path/"version.py"
        print(f"[DEBUG] module_path argument: {module_path}")
        print(f"[DEBUG] resolved module_path: {self.module_path}")
        print(f"[DEBUG] expected pyproject.toml: {self.toml_path}")


    def get_current_version(self):
        return toml.load(self.toml_path)["project"]["version"]

    def is_git_dirty(self):
        git_root = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=git_root,
            capture_output=True,
            text=True,
        )
        return  any(line.startswith(" M") or line.startswith("A ") or line.startswith("D ") for line in result.stdout.splitlines())

    def bump(self, level="patch"):
        current = self.get_current_version()
        subprocess.run([
            "bump2version", level,
            "--current-version", current,
            "--commit", "--tag",
            self.toml_path
        ])
        self.update_version_py()

    def update_version_py(self):
        version = self.get_current_version()
        with open(self.version_py, "w") as f:
            f.write(f'__version__ = "{version}"\n')