from typing import TypeVar

from core.models.tools.properties.BasicProperty import BasicProperty

TItem = TypeVar("TItem")

class ArrayProperty(BasicProperty[list[TItem]]):
    type: list[TItem]
    description: str
    items: TItem