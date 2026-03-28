from abc import ABC, abstractmethod
from pathlib import Path

class AbstractGUI(ABC):
    @property
    @abstractmethod
    def main_text(self) -> str:
        pass

    @property
    @abstractmethod
    def sub_text(self) -> str:
        pass

    @property
    @abstractmethod
    def question_text(self) -> str:
        pass

    @property
    @abstractmethod
    def question_visible(self) -> bool:
        pass

    @property
    @abstractmethod
    def icon(self) -> Path:
        pass

    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def set_main_text(self, text: str) -> None:
        pass

    @abstractmethod
    def set_sub_text(self, text: str) -> None:
        pass

    @abstractmethod
    def set_icon(self, icon_path: Path) -> None:
        pass

    @abstractmethod
    def set_question_text(self, text: str) -> None:
        pass

    @abstractmethod
    def show_question(self) -> None:
        pass

    @abstractmethod
    def hide_question(self) -> None:
        pass