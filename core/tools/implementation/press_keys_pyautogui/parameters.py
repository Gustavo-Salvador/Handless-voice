from pydantic import BaseModel, Field

class parameters(BaseModel):
    keys: list[str] = Field(description="A list of keys to be pressed. It must be one key per string. Special keys like 'enter', 'esc', 'win', or 'ctrl' can be used. To hold a key down use 'down_{key}' and to release use 'up{key}. ex: ['down_ctrl', 'a', 'up_ctrl']")
