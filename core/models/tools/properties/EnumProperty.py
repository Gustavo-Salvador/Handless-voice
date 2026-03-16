from typing import Type

from pydantic import Field

from core.models.tools.properties.BasicProperty import BasicProperty

class EnumProperty(BasicProperty[str]):
    type: Type[str] = str
    description: str
    enum: list[str] = Field(default_factory=list)