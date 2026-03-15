from typing import Callable, Type, TypeVar, Dict

from core.tools.AbstractAction import AbstractAction

TAction = TypeVar("TAction", bound=AbstractAction)

actions: Dict[str, Type[AbstractAction]] = {}

def register_action(action_name: str) -> Callable[[Type[TAction]], Type[TAction]]:
    def decorator(action_class: Type[TAction]) -> Type[TAction]:
        key = action_name.lower()
        
        if key in actions:
            raise ValueError(f"An action with the name '{key}' is already registered.")
            
        actions[key] = action_class
        return action_class
    
    return decorator