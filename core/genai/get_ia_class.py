from typing import Type

from core.genai.AbstractGenai import AbstractGenai
from core.genai.register_ia import ias
import core.genai.implementations # type: ignore

def get_ia_class(ia_name: str) -> Type[AbstractGenai]:
    key = ia_name.lower()
    
    if key not in ias:
        raise ValueError(
            f"IA '{key}' not found. "
            f"Available IAs: {list(ias.keys())}"
        )
        
    return ias[key]