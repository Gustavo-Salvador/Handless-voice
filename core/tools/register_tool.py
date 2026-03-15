from typing import Callable, Type, TypeVar, Dict

from core.tools.AbstractTool import AbstractTool

TTool = TypeVar("TTool", bound=AbstractTool)

tool: Dict[str, Type[AbstractTool]] = {}

def register_tool(tool_name: str) -> Callable[[Type[TTool]], Type[TTool]]:
    def decorator(tool_class: Type[TTool]) -> Type[TTool]:
        key = tool_name.lower()
        
        if key in tool:
            raise ValueError(f"An tool with the name '{key}' is already registered.")
            
        tool[key] = tool_class
        return tool_class
    
    return decorator