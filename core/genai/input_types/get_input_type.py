from typing import Type

from core.genai.input_types.AbstractInput import AbstractInput
from core.genai.input_types.register_input_type import input_types
import core.genai.input_types.implementations # type: ignore

def get_input_type(type_name: str) -> Type[AbstractInput[...]]:
    key = type_name.lower()
    
    if key not in input_types:
        raise ValueError(
            f"Input type '{key}' not found. "
            f"Available input types: {list(input_types.keys())}"
        )
        
    return input_types[key]