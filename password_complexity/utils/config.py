"""Configuration operations."""

from pathlib import Path

import box
import yaml


def load_config(config_path: Path) -> box.ConfigBox:
    """Loads yaml config in instance of box.ConfigBox.

    Args:
        config_path (Path): path to config

    Returns:
        box.ConfigBox
    """
    with open(config_path) as config_file:
        config = yaml.safe_load(config_file)
        config = box.ConfigBox(config)
        return config
