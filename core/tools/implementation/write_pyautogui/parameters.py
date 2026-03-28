from pydantic import BaseModel, Field

class parameters(BaseModel):
    text: str = Field(description='The text to be written.')
