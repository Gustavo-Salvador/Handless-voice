# core/registry.py
from typing import Callable, Type, TypeVar, Dict

from core.config.AbstractConfig import AbstractConfig

TConfig = TypeVar("TConfig", bound=AbstractConfig)

configs: Dict[str, Type[AbstractConfig]] = {}

def register_config(conf_name: str) -> Callable[[Type[TConfig]], Type[TConfig]]:
    def decorator(config_class: Type[TConfig]) -> Type[TConfig]:
        key = conf_name.lower()
        
        if key in configs:
            raise ValueError(f"A configuration with the name '{key}' is already registered.")
            
        configs[key] = config_class
        return config_class
    
    return decorator