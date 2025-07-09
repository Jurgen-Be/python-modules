# version_manager/tests/test_manager.py
from version_manager.version_manager.manager import VersionManager

def test_version():
    vm = VersionManager()
    assert isinstance(vm.get_current_version(), str)
