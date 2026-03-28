from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, Type

from core.config.AbstractConfig import AbstractConfig
from core.gui.AbstractGUI import AbstractGUI

class AbstractInputSource(ABC):
    @abstractmethod
    def __init__(self, get_config_class: Callable[[str], Type[AbstractConfig]], output_folder: str, user_interface: AbstractGUI) -> None:
        pass

    @property
    @abstractmethod
    def config_source(self) -> AbstractConfig:
        pass
    
    @abstractmethod
    def generate_file(self) -> Path:
        pass