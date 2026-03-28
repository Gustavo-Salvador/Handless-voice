import os
import sys
import time

from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool

from .parameters import parameters

try:
    import pyautogui

except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install pyautogui")
    print("Bibliotecas instaladas com sucesso.")

    import pyautogui

@register_tool('write')
class WritePyautogui(AbstractTool[[str], str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui
        
        self.user_interface = user_interface
        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return "Writes text on actual cursor position."

    @property
    def parameters(self) -> type[BaseModel]:
        return parameters

    def execute(self, text: str) -> str:
        self.user_interface.set_sub_text('Escrevendo...')
        self.user_interface.set_main_text('Aguarde...')

        time.sleep(1)

        pyautogui.write(text)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return f"Escreveu com sucesso: {text}"
