from pathlib import Path
import time

from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from core.tools.implementation.screen_shot_pyautogui.functions.InfoContainer import InfoContainer
from .functions.draw_divisors import draw_divisors
from .functions.generate_file_name import generate_file_name
from .parameters_SubdivesScreenShot import SubPartParameters
from core.tools.register_tool import register_tool


@register_tool('subdivide_screen_shot')
class SubdivideScreenShot(AbstractTool[[int, int], Path | str]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        user_interface = conteiner.gui
        
        self.user_interface = user_interface
        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return (
            "Zooms into a specific grid cell (defined by x and y indexes) from the last screenshot "
            "and subdivides it with a new grid. Use this when the target element is too small or "
            "shares a cell with other elements. Requires 'screen_shot' to be executed first."
        )

    @property
    def parameters(self) -> type[BaseModel]:
        return SubPartParameters

    def execute(self, x_index: int, y_index: int) -> Path | str:
        self.user_interface.set_sub_text('melhorando captura...')
        self.user_interface.set_main_text('Aguarde...')

        time.sleep(1)

        info_container = InfoContainer()

        if info_container.last_screenshot is None:
            return 'None screenshot found to subdivide.'
        
        file_name = generate_file_name('SubRegion')
        file_path = Path(file_name)

        n_vertical_lines, n_horizontal_lines = info_container.grid_size
        
        left = x_index * (info_container.last_screenshot.width // n_vertical_lines)
        top = y_index * (info_container.last_screenshot.height // n_horizontal_lines)
        width = info_container.last_screenshot.width // n_vertical_lines
        height = info_container.last_screenshot.height // n_horizontal_lines

        original_size = info_container.last_screenshot.size
        screenshot = info_container.last_screenshot.crop((left, top, left + width, top + height))

        #Scale up screenshot to original size
        screenshot = screenshot.resize(original_size)
        screenshot.save(file_path)

        info_container.update(screenshot.copy(), file_path)
        info_container.append_subdivide(x_index, y_index)
        
        draw_divisors(screenshot)

        drawned_path_name = generate_file_name('sub_region_drawned')
        drawned_path = Path(drawned_path_name)
        screenshot.save(drawned_path)

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return drawned_path