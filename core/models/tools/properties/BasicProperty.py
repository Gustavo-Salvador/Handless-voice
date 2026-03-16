from typing import Generic, Type, TypeVar

from pydantic import BaseModel

TType = TypeVar("TType")

class BasicProperty(BaseModel, Generic[TType]):
    type: Type[TType]
    description: str