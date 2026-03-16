from typing import Type

from pydantic import Field

from core.models.tools.properties.BasicProperty import BasicProperty

class EnumProperty(BasicProperty[str]):
    prop_type: Type[str] | None = str
    description: str
    enum: list[str] = Field(default_factory=list)