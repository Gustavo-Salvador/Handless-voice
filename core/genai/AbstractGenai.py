from typing import Any

from abc import ABC, abstractmethod
from core.models.IAConfigs import IAConfigs, ferramenta

class AbstractGenai(ABC):
    @abstractmethod
    def __init__(self, IAConfigs: IAConfigs[ferramenta]):
        pass

    @abstractmethod
    def enviar_prompt(self, prompt: Any, **kwargs: dict[str, Any]) -> str | None:
        pass