# version_manager/__main__.py
""" Cli programma voor de versie manager."""
import sys
import argparse

# Import modules
from version_manager.manager import VersionManager

def main():
    parser = argparse.ArgumentParser(description='Version Manager CLI')
    parser.add_argument("--level", choices=["patch", "minor", "major"], help="Bump level" )
    parser.add_argument("--module", help="Pad naar de modulemap, vb log_module")
    args = parser.parse_args()

    if args.level and args.module:
        module_path = f"python-modules/{args.module}"
        vm = VersionManager(module_path=module_path)
        if vm.is_git_dirty():
            print("⚠️ Git is niet clean. Eerst committen of auto-commit inschakelen.")
        else:
            vm.bump(args.level)
            print(f"✅ Nieuwe versie in {args.module}: {vm.get_current_version()}")

    else:
        # Interactief keuzemenu als geen CLI level meegegeven werd
        print("\n🔧 Version Manager\n")
        module = input("Pad naar de modulemap, vb log_module")
        print("1. Patch\n2. Minor\n3. Major\n4. Exit")
        choice = input("Maak een keuze (1/2/3/4):").strip()
        levels = {"1": "patch", "2": "minor", "3": "major"}

        if choice in levels:
            module_path = f"python-modules/{module}"
            vm = VersionManager(module_path=module_path)
            if vm.is_git_dirty():
                print("⚠️ Git is niet clean. Eerst committen of auto-commit inschakelen.")
                return
            vm.bump(levels[choice])
            print(f"✅ Nieuwe versie in {module}: {vm.get_current_version()}")

        else:
            print("❌ Ongeldige keuze.")
if __name__ == "__main__":
    main()
