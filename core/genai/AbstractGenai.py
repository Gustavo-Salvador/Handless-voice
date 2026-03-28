from typing import Any, Callable, Type

from abc import ABC, abstractmethod
from core.gui.AbstractGUI import AbstractGUI
from core.models.IAConfigs import IAConfigs
from core.tools.AbstractTool import AbstractTool

class AbstractGenai(ABC):
    @abstractmethod
    def __init__(self, IAConfigs: IAConfigs, tool_getter: Callable[[str], Type[AbstractTool[Any, Any]] | dict[str, Type[AbstractTool[Any, Any]]]], user_interface: AbstractGUI):
        pass

    @abstractmethod
    def enviar_prompt(self, prompt: Any, **kwargs: dict[str, Any]) -> str | None:
        pass