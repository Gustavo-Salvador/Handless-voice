from abc import ABC, abstractmethod
from core.models.tools.ParameterDescriptions import ParameterDescriptions

class AbstractAction(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        pass
    
    @property
    @abstractmethod
    def parameters(self) -> ParameterDescriptions:
        pass

    @abstractmethod
    def execute(self) -> None:
        pass