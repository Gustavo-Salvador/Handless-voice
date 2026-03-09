# core/registry.py
from typing import Callable, Type, TypeVar, Dict

from core.inputs.AbstractInputSource import AbstractInputSource

TInput = TypeVar("TInput", bound=AbstractInputSource)

inputs: Dict[str, Type[AbstractInputSource]] = {}

def register_input(input_name: str) -> Callable[[Type[TInput]], Type[TInput]]:
    def decorator(input_class: Type[TInput]) -> Type[TInput]:
        key = input_name.lower()
        
        if key in inputs:
            raise ValueError(f"A input with the name '{key}' is already registered.")
            
        inputs[key] = input_class
        return input_class
    
    return decorator