from typing import Any

from pydantic import BaseModel, Field

class ParameterDescriptions(BaseModel):
    type: str
    properties: dict[str, Any]
    required: list[str] = Field(default_factory=list)