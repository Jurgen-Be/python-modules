## 📝 Bestand: `README.md`

# 📦 version_manager

Een Python CLI-tool voor semantische versiebumping van modules. Synchroniseert `pyproject.toml` en een versiebestand (`version.py` of `__init__.py`) en controleert of de Git-status clean is voor uitvoering.


## 🚀 Installatie

Via GitHub-release:

```bash
uv add https://github.com/Jurgen-Be/python-modules/releases/download/version_manager-v0.2.3/version_manager-0.2.3-py3-none-any.whl
```

Of lokaal via build:

```bash
uv run python -m build
uv pip install dist/version_manager-0.2.3-py3-none-any.whl
```

---

## ⚙️ Functionaliteit

- 🔁 Bump van `patch`, `minor`, of `major` via CLI of interactief menu
- 📂 Synchronisatie van `pyproject.toml` + versiebestand (`version.py`, `__init__.py`, ...)
- 🧠 Git-integratie voorkomt bump bij uncommitted changes
- ✳️ Nieuwe CLI-flags:
  - `--dry-run`: simuleer bump zonder wijzigingen
  - `--version-file`: geef een alternatief pad op voor versiebestand

---

## 🖥️ CLI Gebruik

Interactief:

```bash
version-manager
```

Of direct:

```bash
version-manager --module log_module --level patch
```

Met extra flags:

```bash
version-manager --module log_module --level minor --version-file __init__.py --dry-run
```

---

## 📚 Python API

```python
from version_manager.manager import VersionManager

vm = VersionManager(module_path="log_module", version_file="__init__.py", dry_run=True)

if not vm.is_git_dirty():
    vm.bump("minor")
```

---

## 🛠️ Vereisten

- Python 3.9 of hoger
- Git geïnstalleerd (voor statuscontrole)
- Dependencies:
  - `bump2version`
  - `toml`

---

## 🧪 Lokale tests

```bash
uv pip install -e .
version-manager
```

---

## 📜 Changelog

Zie [CHANGELOG.md](./CHANGELOG.md) voor alle versies en updates.

---

## 👤 Auteur

Gemaakt en onderhouden door [Jurgen Be](https://github.com/Jurgen-Be)

---

## 📄 Licentie

MIT – Vrij te gebruiken, aan te passen en te delen.
```

---
