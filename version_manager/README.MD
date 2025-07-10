Absoluut, Jurgen — je module verdient een README die niet enkel uitlegt wat ze doet, maar ook laat zien dat ze professioneel in elkaar zit. 📘✨ Hier is een kant-en-klare versie van je `README.md` die je direct in je repo kunt opnemen of aanpassen:

---

```markdown
# 📦 version_manager

Een Python CLI-tool voor het automatisch beheren van semantische versies van modules. Met ondersteuning voor `patch`, `minor` en `major` bumps, synchroniseert `version.py` en `pyproject.toml`, en voorkomt onbedoelde versiewijzigingen via Git-integratie.

---

## 🚀 Installatie

Via GitHub release:

```bash
uv add https://github.com/Jurgen-Be/python-modules/releases/download/version_manager-v0.2.2/version_manager-0.2.2-py3-none-any.whl
```

Of lokaal via build:

```bash
uv run python -m build
uv pip install dist/version_manager-0.2.2-py3-none-any.whl
```

---

## 🖥️ CLI Gebruik

### Interactieve modus

```bash
version-manager
```

➡️ Je krijgt een keuzemenu om de versie te bumpen (patch, minor, major).

### Directe aanroep

```bash
version-manager --module log_module --level minor
```

---

## 📚 Python API

```python
from version_manager.manager import VersionManager

vm = VersionManager(module_path="log_module")

if not vm.is_git_dirty():
    vm.bump("patch")
```

---

## 🔧 Functionaliteit

- 🔁 Semantische versiebeheer via `bump2version`
- 📂 Synchronisatie van `version.py` en `pyproject.toml`
- 🧠 Git-statuscontrole om bump bij unstaged wijzigingen te blokkeren
- ✅ Padafhankelijke werking → je kunt starten vanuit root of modulemap

---

## 🛠️ Vereisten

- Python 3.9 of hoger
- Git geïnstalleerd (voor dirty-check)
- Dependencies:
  - `bump2version`
  - `toml`

---

## 🔖 Changelog & releases

Bekijk [de releases](https://github.com/Jurgen-Be/python-modules/releases) voor changelogs en downloads van `.whl` builds per versie.

---

## 🧪 Testen lokaal

```bash
uv pip install -e .
version-manager
```

---

## 📄 Licentie

MIT – Vrij te gebruiken en aan te passen.

---

## 👤 Auteur

Gemaakt en onderhouden door [Jurgen Be](https://github.com/Jurgen-Be)

```

---

Wil je dat ik dit meteen verwerk als commitklare `README.md` met padding en headers zoals je andere modules? Of voeg je graag badges toe zoals PyPI-versie, GitHub downloads, of een linting-shield? 📦⚙️ Geef maar een seintje, dan tikken we het netjes af.
