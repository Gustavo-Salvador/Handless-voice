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

@register_tool('mouse_down')
class MouseDown(AbstractTool[[str], str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui

        self.user_interface = user_interface

        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return (
            "Holds the specified mouse button down at the current mouse position. Useful for starting a drag operation. "
            "IMPORTANT: If 'mouse_down' is called, 'mouse_up' must be called afterwards to release the button."
        )

    @property
    def parameters(self) -> type[BaseModel]:
        return ClickParameters

    def execute(self, button: str = "left") -> str:
        self.user_interface.set_sub_text('Segurando botão...')
        self.user_interface.set_main_text(f'botão: {button}')

        time.sleep(1)

        if not validate_button(button):
            return f"Error: Invalid mouse button '{button}'. Valid values are 'left', 'right', or 'middle'."

        pyautogui.mouseDown(button=button)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return f"Successfully pressed and held the {button} mouse button down."