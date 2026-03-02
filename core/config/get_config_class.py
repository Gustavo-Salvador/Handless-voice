from typing import Type

from core.config.AbstractConfig import AbstractConfig
from core.config.register_config import configs

def get_config_class(conf_name: str) -> Type[AbstractConfig]:
    key = conf_name.lower()
    
    if key not in configs:
        raise ValueError(
            f"Configuration '{key}' not found. "
            f"Available configs: {list(configs.keys())}"
        )
        
    return configs[key]