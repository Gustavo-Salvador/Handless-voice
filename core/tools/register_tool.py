from typing import Callable, Type, TypeVar, Dict, Any

from core.tools.AbstractTool import AbstractTool

TTool = TypeVar("TTool", bound=AbstractTool[Any, Any])

tools: Dict[str, Type[AbstractTool[Any, Any]]] = {}

def register_tool(tool_name: str) -> Callable[[Type[TTool]], Type[TTool]]:
    def decorator(tool_class: Type[TTool]) -> Type[TTool]:
        key = tool_name.lower()

        if key == '*':
            raise ValueError("The tool name '*' is reserved and cannot be used.")
        
        if key in tools:
            raise ValueError(f"An tool with the name '{key}' is already registered.")
            
        tools[key] = tool_class
        return tool_class
    
    return decorator