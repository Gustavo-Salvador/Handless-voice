from typing import Callable, Type, TypeVar, Dict, Any

from core.tools.AbstractTool import AbstractTool

TTool = TypeVar("TTool", bound=AbstractTool[Any])

tool: Dict[str, Type[AbstractTool[Any]]] = {}

def register_tool(tool_name: str) -> Callable[[Type[TTool]], Type[TTool]]:
    def decorator(tool_class: Type[TTool]) -> Type[TTool]:
        key = tool_name.lower()
        
        if key in tool:
            raise ValueError(f"An tool with the name '{key}' is already registered.")
            
        tool[key] = tool_class
        return tool_class
    
    return decorator