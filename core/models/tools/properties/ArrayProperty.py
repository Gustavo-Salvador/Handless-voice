from typing import Type, TypeVar

from core.models.tools.properties.BasicProperty import BasicProperty

TItem = TypeVar("TItem")

class ArrayProperty(BasicProperty[list[TItem]]):
    prop_type: Type[list[TItem]] | None = list
    description: str
    items: TItem