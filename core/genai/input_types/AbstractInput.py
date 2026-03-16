from abc import ABC, abstractmethod
from typing import Any, Callable, Concatenate, Generic, ParamSpec, TypeVar

retorno_processamento = TypeVar("retorno_processamento")
P = ParamSpec("P")

class AbstractInput(ABC, Generic[P]):
    @abstractmethod
    def __init__(self, dados: Any, mime_type: str):
        pass

    @abstractmethod
    def process(self, retorno_lambda: Callable[Concatenate[bytes, P], retorno_processamento]) -> list[str | retorno_processamento]:
        pass