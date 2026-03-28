import os
import sys
import time
from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool
from .parameters_Click import ClickParameters
from .functions.validate_button import validate_button

try:
    import pyautogui
except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install pyautogui")
    print("Bibliotecas instaladas com sucesso.")
    import pyautogui

@register_tool('mouse_up')
class MouseUp(AbstractTool[[str], str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui
        
        self.user_interface = user_interface

        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return (
            "Releases the specified mouse button at the current mouse position. Useful for ending a drag operation. "
            "This tool MUST be called if 'mouse_down' was previously used."
        )

    @property
    def parameters(self) -> type[BaseModel]:
        return ClickParameters

    def execute(self, button: str = "left") -> str:
        self.user_interface.set_sub_text('Soltando botão...')
        self.user_interface.set_main_text(f'botão: {button}')

        time.sleep(1)

        if not validate_button(button):
            return f"Error: Invalid mouse button '{button}'. Valid values are 'left', 'right', or 'middle'."

        pyautogui.mouseUp(button=button)
        
        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return f"Successfully released the {button} mouse button."