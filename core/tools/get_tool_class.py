from typing import Any, Type

from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import tools
import core.tools.implementation # type: ignore

def get_tool_class(tool_name: str) -> Type[AbstractTool[Any, Any]] | dict[str, Type[AbstractTool[Any, Any]]]:
    if tool_name == '*':
        return tools
    
    key = tool_name.lower()
    
    if key not in tools:
        raise ValueError(
            f"Tool '{key}' not found. "
            f"Available tools: {list(tools.keys())}"
        )
        
    return tools[key]