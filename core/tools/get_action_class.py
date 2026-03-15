from typing import Type

from core.tools.AbstractAction import AbstractAction
from core.tools.register_action import actions

def get_action_class(action_name: str) -> Type[AbstractAction]:
    key = action_name.lower()
    
    if key not in actions:
        raise ValueError(
            f"Action '{key}' not found. "
            f"Available actions: {list(actions.keys())}"
        )
        
    return actions[key]