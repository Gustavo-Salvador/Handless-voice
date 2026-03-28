from pydantic import BaseModel

from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool

@register_tool('quit')
class Quit(AbstractTool[[], str]):
    def __init__(self) -> None:
        pass

    @property
    def description(self) -> str:
        return "Stops and closes the application. Use this tool when the user asks to quit, exit, stop the program, or say goodbye."

    @property
    def parameters(self) -> type[BaseModel] | None:
        return None

    def execute(self) -> str:
        # Esta função não chegará a ser totalmente executada porque 
        # o 'execute_tool.py' intercepta a chamada 'quit' antes.
        return "Quitting..."