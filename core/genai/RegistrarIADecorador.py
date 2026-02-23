# core/registry.py
from typing import Callable, Type, TypeVar, Dict

from core.genai.AbstractGenai import AbstractGenai

construtor_ia = TypeVar("construtor_ia", bound=AbstractGenai)

LLMs: Dict[str, Type[AbstractGenai]] = {}

def RegistrarIA(nome_ia: str) -> Callable[[Type[construtor_ia]], Type[construtor_ia]]:
    """
    Decorador para registrar uma classe de IA no dicionário LLMs.
    """
    
    def decorator(classe_ia: Type[construtor_ia]) -> Type[construtor_ia]:
        LLMs[nome_ia.lower()] = classe_ia
        return classe_ia
    
    return decorator