from typing import Callable, Type, TypeVar, Dict

from core.gui.AbstractGUI import AbstractGUI

TGUI = TypeVar("TGUI", bound=AbstractGUI)

guis: Dict[str, Type[AbstractGUI]] = {}

def register_gui(gui_name: str) -> Callable[[Type[TGUI]], Type[TGUI]]:
    def decorator(gui_class: Type[TGUI]) -> Type[TGUI]:
        key = gui_name.lower()
        
        if key in guis:
            raise ValueError(f"A GUI with the name '{key}' is already registered.")
            
        guis[key] = gui_class
        return gui_class
    
    return decorator