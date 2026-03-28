from typing import Callable, Type, TypeVar, Dict

from core.genai.input_types.AbstractInput import AbstractInput

TInputType = TypeVar("TInputType", bound=AbstractInput[...])

input_types: Dict[str, Type[AbstractInput[...]]] = {}

def register_input_type(type_name: str) -> Callable[[Type[TInputType]], Type[TInputType]]:
    def decorator(input_class: Type[TInputType]) -> Type[TInputType]:
        key = type_name.lower()
        
        if key in input_types:
            raise ValueError(f"An input type with the name '{key}' is already registered.")
            
        input_types[key] = input_class
        return input_class
    
    return decorator