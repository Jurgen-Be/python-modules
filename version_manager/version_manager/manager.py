# version_manager/manager.py

# Import van de nodige modules
import toml
import subprocess
import os
from pathlib import Path

# Classes met functies
class VersionManager:
    def __init__(self, module_path=".", version_file=None, dry_run=False):
        self.module_path = Path(module_path).resolve()
        self.toml_path = self.module_path/"pyproject.toml"
        self.version_py = self.module_path/version_file if version_file else self.module_path/"version.py"
        self.dry_run = dry_run

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
        if self.dry_run:
            print(f"[DRY-RUN] Zou bump uitvoeren naar {level} vanaf {current}")
        else:
            subprocess.run([
                "bump2version", level,
                "--current-version", current,
                "--commit", "--tag",
                self.toml_path
            ])
            bumped_version = self.get_current_version()
            self.write_version_py(bumped_version)
            print(f"[DEBUG] Vresie geschreven naar: {self.version_py}")

    def write_version_py(self, version):
        with open(self.version_py, "w") as f:
            f.write(f'__version__ = "{version}"\n')