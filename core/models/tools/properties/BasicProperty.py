from typing import Generic, TypeVar

from pydantic import BaseModel

TType = TypeVar("TType")

class BasicProperty(BaseModel, Generic[TType]):
    type: TType
    description: str