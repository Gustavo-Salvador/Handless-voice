from typing import Any, Type

from core.models.tools.properties.BasicProperty import BasicProperty

from pydantic import BaseModel, Field

class ParameterDescriptions(BaseModel):
    prop_type: Type[dict[str, BasicProperty[Any]]] = dict
    properties: dict[str, BasicProperty[Any]]
    required: list[str] = Field(default_factory=list)