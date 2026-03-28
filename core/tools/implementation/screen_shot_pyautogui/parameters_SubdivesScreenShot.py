from pydantic import BaseModel, Field


class SubPartParameters(BaseModel):
    x_index: int = Field(description="The horizontal index of the grid cell to capture.")
    y_index: int = Field(description="The vertical index of the grid cell to capture.")