from pydantic import BaseModel, Field

class ClickParameters(BaseModel):
    button: str = Field(default="left", description="The mouse button to click. Valid values are 'left', 'right', or 'middle'.")