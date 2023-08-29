from typing import Any
import yaml

from auto_vt.dto.config import Config

def __read_config(filepath: str) -> Any:
    """Read the configuration file into memory"""
    with open(filepath, "r") as config_file:
        return yaml.safe_load(config_file)
    
def load_parse_config(filepath: str) -> Config:
    """"""
    config_dict = __read_config(filepath)
    config_obj = Config.from_yaml(config_dict)
    print(config_obj)
    return config_obj
