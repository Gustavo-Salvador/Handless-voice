from abc import ABC, abstractmethod
from typing import Any, Callable, Concatenate, Generic, ParamSpec, TypeVar

processed_return = TypeVar("processed_return")
P = ParamSpec("P")

class AbstractInput(ABC, Generic[P]):
    @abstractmethod
    def __init__(self, dados: Any, mime_type: str, message: str | None):
        pass

    @abstractmethod
    def process(self, processor: Callable[Concatenate[bytes, P], processed_return]) -> list[str | processed_return]:
        pass