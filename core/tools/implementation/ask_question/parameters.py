from pydantic import BaseModel, Field

class parameters(BaseModel):
    question: str = Field(description="The text of the question to ask the user.")