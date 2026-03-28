from __future__ import annotations

import multiprocessing as mp
from queue import Empty
from typing import Any
from PyQt6.QtWidgets import QLabel, QApplication

from .update_icon import update_icon

def check_queue(cmd_queue: mp.Queue[tuple[str, Any]], main_text_label: QLabel,  sub_text_label: QLabel, 
                icon_label: QLabel, question_label: QLabel, app: QApplication) -> None:
    try:
        while True:
            cmd, payload = cmd_queue.get_nowait()
            
            if cmd == 'main_text':
                main_text_label.setText(payload)
            elif cmd == 'sub_text':
                sub_text_label.setText(payload)
            elif cmd == 'icon':
                update_icon(icon_label, payload)
            elif cmd == 'question_text':
                question_label.setText(payload)
            elif cmd == 'show_question':
                question_label.show()
            elif cmd == 'hide_question':
                question_label.hide()
            elif cmd == 'stop':
                app.quit()
    except Empty:
        pass