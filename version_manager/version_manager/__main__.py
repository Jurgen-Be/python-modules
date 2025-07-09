# version_manager/__main__.py
""" Cli programma voor de versie manager."""
import sys

# Import modules
from .manager import VersionManager

def main():
    print("\n🔧 Version Manager\n")
    print("1. Patch\n2. Minor\n3. Major\n4. Exit")
    choice = input("Maak een keuze (1/2/3/4):").strip()
    levels = {"1": "patch", "2": "minor", "3": "major"}

    if choice in levels:
        vm = VersionManager()
        if vm.is_git_dirty():
            print("⚠️ Git is niet clean. Eerst committen of auto-commit inschakelen.")
            return
        vm.bump(levels[choice])
        print(f"✅ Nieuwe versie: {vm.get_current_version()}")
if __name__ == "__main__":
    main()