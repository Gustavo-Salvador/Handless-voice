from typing import Type

from core.gui.AbstractGUI import AbstractGUI
from core.gui.register_gui import guis
import core.gui.implementations # type: ignore

def get_gui_class(gui_name: str) -> Type[AbstractGUI]:
    key = gui_name.lower()
    
    if key not in guis:
        raise ValueError(
            f"GUI '{key}' not found. "
            f"Available GUIs: {list(guis.keys())}"
        )
        
    return guis[key]