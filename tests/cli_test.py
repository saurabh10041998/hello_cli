import sys
import pytest
from types import MappingProxyType
from hello_cli.cli import parse_args

@pytest.fixture(scope='session', autouse=True)
def help_menus() -> MappingProxyType[str, str]:
    menus = MappingProxyType({
        'name': (
            "n NAME, --name NAME"
        )
    })
    return menus


def test_help_menu_exit(monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['hello_cli', '-h'])
        with pytest.raises(SystemExit) as excinfo:
            _ = parse_args()
        assert excinfo.value.args[0] == 0


def test_help_menu_content(help_menus, monkeypatch, capsys):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['hello_cli', '-h'])
        with pytest.raises(SystemExit) as excinfo:
            _ = parse_args()
        assert excinfo.value.args[0] == 0
        out, err = capsys.readouterr()
        assert help_menus['name'] in out

def test_help_menu_with_long_args(help_menus, monkeypatch, capsys):
    with monkeypatch.context() as m:
        m.setattr(sys, 'argv', ['hello_cli', '--help'])
        with pytest.raises(SystemExit) as excinfo:
            _ = parse_args()
        assert excinfo.value.args[0] == 0
        out, err = capsys.readouterr()
        assert help_menus['name'] in out
