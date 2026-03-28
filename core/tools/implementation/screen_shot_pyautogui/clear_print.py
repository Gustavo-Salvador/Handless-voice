from pydantic import BaseModel
from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool
from .functions.InfoContainer import InfoContainer

@register_tool('clear_screenshot_history')
class ClearScreenshotHistory(AbstractTool[[], str]):
    def __init__(self) -> None:
        pass

    @property
    def description(self) -> str:
        return (
            "Clears the current screenshot and subdivision history. Use this tool if you made a mistake "
            "in subdividing, or if you need to take a fresh 'screen_shot' to see new changes on the screen."
        )

    @property
    def parameters(self) -> type[BaseModel] | None:
        return None

    def execute(self) -> str:
        info_container = InfoContainer()
        info_container.last_screenshot = None
        info_container.last_file_path = None
        info_container.sub_divided_list = []
        
        return "Screenshot history and subdivisions have been cleared. If you need, take a new 'screen_shot'."
