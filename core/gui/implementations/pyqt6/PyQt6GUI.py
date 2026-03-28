from __future__ import annotations

import os
import sys
import multiprocessing as mp
from typing import Any
from pathlib import Path

from core.gui.AbstractGUI import AbstractGUI
from core.gui.register_gui import register_gui

try:
    from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout # type: ignore
    from PyQt6.QtCore import Qt, QTimer # type: ignore
    from PyQt6.QtGui import QPixmap # type: ignore
except ImportError:
    print("\033[91mErro:\033[0m A biblioteca PyQt6 não está instalada, tentando instalar.")
    os.system(f"{sys.executable} -m pip install PyQt6")
    print("Biblioteca instalada com sucesso.")

from .functions.run_gui_process import run_gui_process

@register_gui('pyqt6')
class PyQt6GUI(AbstractGUI):
    def __init__(self) -> None:
        self._main_text = ""
        self._sub_text = ""
        self._question_text = ""
        self._question_visible = False
        self._icon = Path()
        
        self._process = None
        self._cmd_queue: mp.Queue[tuple[str, Any]] = mp.Queue()

    @property
    def main_text(self) -> str:
        return self._main_text

    @property
    def sub_text(self) -> str:
        return self._sub_text
    
    @property
    def question_text(self) -> str:
        return self._question_text
    
    @property
    def question_visible(self) -> bool:
        return self._question_visible

    @property
    def icon(self) -> Path:
        return self._icon

    def start(self) -> None:
        """Starts the GUI in a new Process (Non-Blocking)."""
        if self._process is None or not self._process.is_alive():
            self._process = mp.Process(
                target=run_gui_process,
                args=(self._cmd_queue, self._sub_text, self._main_text, self._icon),
                daemon=True
            )
            self._process.start()

    def stop(self) -> None:
        """Requests the GUI process to close via Queue."""
        if self._process and self._process.is_alive():
            self._cmd_queue.put(('stop', None))
            self._process.join(timeout=2)

    def set_main_text(self, text: str = "") -> None:
        self._main_text = text
        self._cmd_queue.put(('main_text', text))

    def set_sub_text(self, text: str = "") -> None:
        self._sub_text = text
        self._cmd_queue.put(('sub_text', text))

    def set_icon(self, icon_path: Path | None = None) -> None:
        if icon_path is not None:
            self._icon = icon_path
        self._cmd_queue.put(('icon', self._icon))

    def set_question_text(self, text: str = "") -> None:
        self._question_text = text
        self._cmd_queue.put(('question_text', text))

    def show_question(self) -> None:
        self._question_visible = True
        self._cmd_queue.put(('show_question', None))

    def hide_question(self) -> None:
        self._question_visible = False
        self._cmd_queue.put(('hide_question', None))