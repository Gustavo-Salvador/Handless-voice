import os
from pathlib import Path
import sys
import time

from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from .functions.draw_divisors import draw_divisors
from .functions.generate_file_name import generate_file_name
from .functions.InfoContainer import InfoContainer
from core.tools.register_tool import register_tool

try:
    import pyautogui

except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install pyautogui")
    print("Bibliotecas instaladas com sucesso.")

    import pyautogui

@register_tool('screen_shot')
class ScreenShotPyautogui(AbstractTool[[], Path]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui

        self.user_interface = user_interface
        
        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return (
            "Captures a screenshot of the entire screen and overlays a numbered grid. "
            "Use this tool FIRST to see the current state of the screen and identify "
            "the grid coordinates (x, y) of the UI elements you want to interact with."
        )

    @property
    def parameters(self) -> type[BaseModel] | None:
        return None

    def execute(self) -> Path:
        self.user_interface.set_sub_text('Capturando tela...')
        self.user_interface.set_main_text('Aguarde...')

        time.sleep(1)

        file_name = generate_file_name()
        file_path = Path(file_name)

        screenshot = pyautogui.screenshot(file_path)

        info_container = InfoContainer()
        info_container.update(screenshot.copy(), file_path)

        n_vertical_lines, n_horizontal_lines = info_container.grid_size

        draw_divisors(screenshot, n_vertical_lines, n_horizontal_lines)

        screenshot = screenshot.resize((int(screenshot.width // 2), int(screenshot.height // 2)))

        drawned_path_name = generate_file_name('drawned')
        drawned_path = Path(drawned_path_name)
        screenshot.save(drawned_path)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return drawned_path