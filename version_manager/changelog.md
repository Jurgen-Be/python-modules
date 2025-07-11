# 📦 version_manager – Changelog

Versieoverzicht voor de CLI-tool `version_manager`. Hier worden alle veranderingen per release bijgehouden. Voeg bij nieuwe versies telkens een blok toe bovenaan.

## v0.2.4 – Exit-fix en padvalidatie

### ✳️ Debug & validatie
- Extra logging van versiebestandpad in `bump()` toegevoegd
- Nieuwe helper `write_version_py()` verwerkt correct versienummer
- Voorkomt mismatch van pad bij bump zonder argumenten


---

## v0.2.3 – CLI-uitbreiding

### ✳️ Toegevoegde functionaliteit
- `--version-file`: versiebestand is nu configureerbaar via CLI
- `--dry-run`: bumpoperatie wordt gesimuleerd zonder bestandswijziging

### 🛠️ Intern
- `__main__.py`: argparse uitgebreid met flags
- `manager.py`: constructor en bump-logica aangepast
- Verbeterde logging bij simulaties

---

## v0.2.2 – Padfix & CLI stabilisatie

### 🩹 Fixes
- CLI input wordt correct vertaald naar absolute padcontext
- Padopbouw via `Path.resolve()` voorkomt instabiliteit
- Git-check via rootmap (rev-parse) is nu stabiel
- Debug toegevoegd voor padcontrole tijdens bump

---