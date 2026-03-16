from typing import Type, TypeVar

from core.models.tools.properties.BasicProperty import BasicProperty

TItem = TypeVar("TItem")

class ArrayProperty(BasicProperty[list[TItem]]):
    type: Type[list[TItem]] = list
    description: str
    items: TItem