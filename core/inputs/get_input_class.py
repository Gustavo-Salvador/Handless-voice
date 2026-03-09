from typing import Type

from core.inputs.AbstractInputSource import AbstractInputSource
from core.inputs.register_input import inputs

def get_input_class(conf_name: str) -> Type[AbstractInputSource]:
    key = conf_name.lower()
    
    if key not in inputs:
        raise ValueError(
            f"Configuration '{key}' not found. "
            f"Available configs: {list(inputs.keys())}"
        )
        
    return inputs[key]