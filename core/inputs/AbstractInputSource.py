from abc import ABC, abstractmethod
from pathlib import Path

from core.config.AbstractConfig import AbstractConfig

class AbstractInputSource(ABC):
    @property
    @abstractmethod
    def config_source(self) -> AbstractConfig:
        pass
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def import_dependencies(self) -> None:
        pass

    @abstractmethod
    def generate_file(self) -> Path:
        pass