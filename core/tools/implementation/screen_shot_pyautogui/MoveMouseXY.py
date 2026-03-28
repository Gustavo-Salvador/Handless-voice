import os
import sys
import time
from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool
from .functions.InfoContainer import InfoContainer
from .parameters_SubdivesScreenShot import SubPartParameters

try:
    import pyautogui
except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install pyautogui")
    print("Bibliotecas instaladas com sucesso.")
    import pyautogui

@register_tool('move_mouse')
class MoveMouseXY(AbstractTool[[int, int], str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui

        self.user_interface = user_interface
        
        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        info_container = InfoContainer()

        return (
            "Moves the mouse exactly to the center of the specified grid cell (x, y). "
            "You must use the coordinates observed from the most recent 'screen_shot' or "
            "'subdivide_screen_shot' execution. "
            f"The limit of the grid is x: {info_container.grid_size[0]} and y: {info_container.grid_size[1]}"
        )

    @property
    def parameters(self) -> type[BaseModel]:
        return SubPartParameters

    def execute(self, x_index: int, y_index: int) -> str:
        info_container = InfoContainer()
        
        if info_container.last_screenshot is None:
            return "Error: No screenshot found to calculate coordinates. Please take a screenshot first."

        self.user_interface.set_sub_text('Movendo mouse...')
        self.user_interface.set_main_text(f'x: {x_index}, y: {y_index}')

        time.sleep(1)

        n_vertical_cells, n_horizontal_cells = info_container.grid_size
        screen_w, screen_h = pyautogui.size()

        current_x, current_y = 0, 0
        current_w, current_h = screen_w, screen_h

        for sub_x, sub_y in info_container.sub_divided_list:
            cell_w = current_w / n_vertical_cells
            cell_h = current_h / n_horizontal_cells
            current_x += sub_x * cell_w
            current_y += sub_y * cell_h
            current_w, current_h = cell_w, cell_h

        final_cell_w = current_w / n_vertical_cells
        final_cell_h = current_h / n_horizontal_cells
        center_x = int(current_x + (x_index * final_cell_w) + (final_cell_w / 2))
        center_y = int(current_y + (y_index * final_cell_h) + (final_cell_h / 2))

        pyautogui.moveTo(center_x, center_y)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return f"Successfully moved mouse to grid coordinates ({x_index}, {y_index}) - Screen pixels: ({center_x}, {center_y})"