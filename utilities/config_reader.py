from configparser import ConfigParser
from pathlib import Path


def load_config(path="config.ini"):
    config = ConfigParser()
    config.read(Path(path))
    return config
