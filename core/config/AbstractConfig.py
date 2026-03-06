from abc import ABC, abstractmethod
from typing import Any, Type

from pydantic import BaseModel

class AbstractConfig(ABC):
    @property
    @abstractmethod
    def file_path(self) -> str:
        pass

    @property
    @abstractmethod
    def category(self) -> str:
        pass

    @property
    @abstractmethod
    def pydantic_model(self) -> Type[BaseModel]:
        pass

    @abstractmethod
    def __init__(self, category: str, pydantic_model: Type[BaseModel], file_path: str):
        pass

    @abstractmethod
    def to_pydantic(self) -> BaseModel:
        pass

    @abstractmethod
    def get_config(self, name: str) -> Any:
        pass

    @abstractmethod
    def set_config(self, name: str, value: Any) -> None:
        pass
