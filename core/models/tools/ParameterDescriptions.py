from typing import Any

from core.models.tools.properties.BasicProperty import BasicProperty

from pydantic import BaseModel, Field

class ParameterDescriptions(BaseModel):
    type: str
    properties: dict[str, BasicProperty[Any]]
    required: list[str] = Field(default_factory=list)