from enum import Enum
from pathlib import Path
import yaml

import typer

VALID_THEMES = ("dark", "light")
CONFIG = Path.home() / ".config"
ALACRITTY_HOME = CONFIG / "alacritty"
ALACRITTY_CONFIG = ALACRITTY_HOME / "alacritty.yml"
NVIM_THEME = CONFIG / "nvim" / "theme.vim"


class Theme(str, Enum):
    dark = "dark"
    light = "light"


themes = {"dark": ALACRITTY_HOME / "dark.yml", "light": ALACRITTY_HOME / "light.yml"}


def set_alacritty_theme(config_path: Path, theme_path: Path):
    with open(config_path, "r") as configf:
        cfg = yaml.safe_load(configf)
    with open(theme_path, "r") as themef:
        theme = yaml.safe_load(themef)

        cfg["colors"] = theme["colors"]
    with open(config_path, "w") as configf:
        yaml.dump(cfg, configf)


def set_nvim_theme(profile: Theme):
    with open(NVIM_THEME, "w") as f:
        theme = "nordl" if profile == "light" else "nordd"
        f.write(f'let g:theme = "{theme}"')


def switch(profile: Theme):
    set_alacritty_theme(ALACRITTY_CONFIG, themes.get(profile))
    set_nvim_theme(profile)
    typer.echo(f"Switched to {profile} mode...")


def main():
    typer.run(switch)
