from abc import ABC, abstractmethod
from typing import Generic, ParamSpec, TypeVar

from pydantic import BaseModel

P = ParamSpec("P")
R = TypeVar("R")

class AbstractTool(ABC, Generic[P, R]):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass
    
    @property
    @abstractmethod
    def parameters(self) -> type[BaseModel] | None:
        pass

    @abstractmethod
    def execute(self, *args: P.args, **kwargs: P.kwargs) -> R:
        pass