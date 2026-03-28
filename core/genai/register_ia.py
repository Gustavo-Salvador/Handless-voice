from typing import Callable, Type, TypeVar, Dict

from core.genai.AbstractGenai import AbstractGenai

TIA = TypeVar("TIA", bound=AbstractGenai)

ias: Dict[str, Type[AbstractGenai]] = {}

def register_ia(ia_name: str) -> Callable[[Type[TIA]], Type[TIA]]:
    def decorator(ia_class: Type[TIA]) -> Type[TIA]:
        key = ia_name.lower()
        
        if key in ias:
            raise ValueError(f"An IA with the name '{key}' is already registered.")
            
        ias[key] = ia_class
        return ia_class
    
    return decorator