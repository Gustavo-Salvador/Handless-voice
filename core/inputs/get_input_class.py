from typing import Type

from core.inputs.AbstractInputSource import AbstractInputSource
from core.inputs.register_input import inputs

def get_input_class(input_name: str) -> Type[AbstractInputSource]:
    key = input_name.lower()
    
    if key not in inputs:
        raise ValueError(
            f"Input '{key}' not found. "
            f"Available inputs: {list(inputs.keys())}"
        )
        
    return inputs[key]