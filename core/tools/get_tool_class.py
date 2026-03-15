from typing import Type

from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import tool

def get_tool_class(tool_name: str) -> Type[AbstractTool]:
    key = tool_name.lower()
    
    if key not in tool:
        raise ValueError(
            f"Tool '{key}' not found. "
            f"Available tools: {list(tool.keys())}"
        )
        
    return tool[key]