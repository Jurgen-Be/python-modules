# version_manager/manager.py

# Import van de nodige modules
import toml
import subprocess
import os
from pathlib import Path

# Classes met functies
class VersionManager:
    def __init__(self, module_path="."):
        self.toml_path = os.path.join(module_path, "pyproject.toml")
        self.version_py = os.path.join(module_path, "version_manager", "version.py")
        self.module_path = Path(module_path)

    def get_current_version(self):
        return toml.load(self.toml_path)["project"]["version"]

    def is_git_dirty(self):
        result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        return  bool(result.stdout.strip())

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