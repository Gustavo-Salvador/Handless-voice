import os
import sys
import re
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

@register_tool('press_key')
class PressKeyPyautogui(AbstractTool[[list[str]], str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui
        
        self.user_interface = user_interface

        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return "Press the passed keys on order."

    @property
    def parameters(self) -> type[BaseModel]:
        return parameters

    def execute(self, keys: list[str]) -> str:
        self.user_interface.set_sub_text('Apertando teclas...')
        self.user_interface.set_main_text(f'Apertando teclas: {", ".join(keys)}')

        time.sleep(1)

        for key in keys:
            re_down = re.match('down_(.*)', key)
            re_up = re.match('up_(.*)', key)

            if re_down:
                pyautogui.keyDown(re_down.group(1))
            elif re_up:
                pyautogui.keyUp(re_up.group(1))
            else:
                pyautogui.press(key)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return 'Sucesso! teclas apertadas: ' + ', '.join(keys)
        

