from typing import Any

from core.tools.AbstractTool import AbstractTool

def generate_tool_declaration(tools: dict[str, type[AbstractTool[Any, Any]]]) -> list[dict[str, Any]]:
    tool_declarations: list[dict[str, Any]]= []
    for tool_name, tool_class in tools.items():
        tool_instance = tool_class()
        tool_declaration: dict[str, Any] = {
            "name": tool_name,
            "description": tool_instance.description,
            "parameters": tool_instance.parameters.model_json_schema() if tool_instance.parameters else {}
        }
        tool_declarations.append(tool_declaration)
    
    return tool_declarations
    