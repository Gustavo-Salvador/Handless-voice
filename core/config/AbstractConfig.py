from abc import ABC, abstractmethod
from typing import Any

class AbstractConfig(ABC):
    @abstractmethod
    def __init__(self, category: str, file_path: str):
        pass

    @abstractmethod
    def get_config(self, name: str) -> Any:
        pass

    @abstractmethod
    def set_config(self, name: str, value: Any) -> None:
        pass
