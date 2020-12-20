from pathlib import Path
import shutil
import tempfile

from nose.tools import assert_equals

from theme.theme import set_alacritty_theme

TEST_DIR = Path(tempfile.mkdtemp())
TEST_CONFIG = TEST_DIR / "alacritty.yml"
TEST_THEME = TEST_DIR / "theme.yml"


def setup():
    TEST_CONFIG.write_text(
        """
some:
  random:
    key: foo
bar: baz
colors:
  not: set
"""
    )
    TEST_THEME.write_text(
        """
colors:
  primary:
    background: '#2e3440'
    foreground: '#d8dee9'
    dim_foreground: '#a5abb6'
"""
    )


def teardown():
    shutil.rmtree(TEST_DIR)


def test_switch_alacritty_theme():
    expectation = """bar: baz
colors:
  primary:
    background: '#2e3440'
    dim_foreground: '#a5abb6'
    foreground: '#d8dee9'
some:
  random:
    key: foo
"""
    set_alacritty_theme(TEST_CONFIG, TEST_THEME)
    assert_equals(expectation, TEST_CONFIG.read_text())
