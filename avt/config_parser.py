from typing import Any
import yaml

from avt.dto.config import Config

def __read_config(filepath: str) -> Any:
    """Read the configuration file into memory"""
    with open(filepath, "r") as config_file:
        return yaml.safe_load(config_file)
    
def load_parse_config(filepath: str) -> Config:
    """"""
    config_dict = __read_config(filepath)
    config_obj = Config.from_yaml(config_dict)
    return config_obj
