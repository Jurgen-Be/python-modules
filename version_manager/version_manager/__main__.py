"""Cli programma voor de versie manager."""

import sys
import argparse
from pathlib import Path

from version_manager.manager import VersionManager

def main():
    parser = argparse.ArgumentParser(description='Version Manager CLI')
    parser.add_argument("--level", choices=["patch", "minor", "major"], help="Type versie bump")
    parser.add_argument("--module", help="Pad naar de modulemap, vb log_module")
    parser.add_argument("--version-file", help="Alternatief pad naar de version file, vb __init__.py")
    parser.add_argument("--dry-run", action="store_true", help="Voer bump uit zonder bestandswijziging")
    args = parser.parse_args()

    if args.level and args.module:
        module_path = str(Path(args.module).resolve())

        vm = VersionManager(
            module_path=module_path,
            version_file=args.version_file,
            dry_run=args.dry_run
        )

        if vm.is_git_dirty():
            print("⚠️ Git is niet clean. Eerst committen of auto-commit inschakelen.")
        else:
            if args.dry_run:
                print(f"[DRY-RUN] Simuleer bump ({args.level}) voor module: {args.module}")
            vm.bump(args.level)
            print(f"✅ Nieuwe versie in {args.module}: {vm.get_current_version()}")

    else:
        # Interactieve modus
        print("\n🔧 Version Manager\n")
        module_input = input("Pad naar de modulemap, vb log_module: ").strip()
        print("1. Patch\n2. Minor\n3. Major\n4. Exit")
        choice = input("Maak een keuze (1/2/3/4): ").strip()
        levels = {"1": "patch", "2": "minor", "3": "major"}

        if choice in levels:
            module_path = str(Path(module_input).resolve())

            vm = VersionManager(module_path=module_path)

            if vm.is_git_dirty():
                print("⚠️ Git is niet clean. Eerst committen of auto-commit inschakelen.")
                return

            vm.bump(levels[choice])
            print(f"✅ Nieuwe versie in {module_input}: {vm.get_current_version()}")

        else:
            print("❌ Ongeldige keuze.")

if __name__ == "__main__":
    main()