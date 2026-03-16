from abc import ABC, abstractmethod
from typing import Generic, ParamSpec
from core.models.tools.ParameterDescriptions import ParameterDescriptions

P = ParamSpec("P")

class AbstractTool(ABC, Generic[P]):
    @property
    @abstractmethod
    def description(self) -> str:
        pass
    
    @property
    @abstractmethod
    def parameters(self) -> ParameterDescriptions:
        pass

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def execute(self, *args: P.args, **kwargs: P.kwargs) -> None:
        pass