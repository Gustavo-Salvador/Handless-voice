from __future__ import annotations

import sys
import multiprocessing as mp
from pathlib import Path
from typing import Any
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt, QTimer

from core.gui.implementations.pyqt6.functions.TrapezoidContainer import TrapezoidContainer

from .update_icon import update_icon
from .check_queue import check_queue

def run_gui_process(cmd_queue: mp.Queue[tuple[str, Any]], initial_sub: str, initial_main: str, initial_icon: Path) -> None:
    app = QApplication(sys.argv)
    
    window = QWidget()
    window.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
    window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
    
    main_layout = QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0) 
    main_layout.addStretch()
    
    question_label = QLabel("Texto de pergunta")
    question_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    question_label.setStyleSheet("background-color: rgba(128, 128, 128, 200); padding: 20px; font-size: 24px; color: black;")
    main_layout.addWidget(question_label)
    
    trapezoid_container = TrapezoidContainer()
    
    icon_label = QLabel()
    icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    icon_label.setStyleSheet("border: none; min-width: 80px; min-height: 80px;") 
    
    texts_layout = QVBoxLayout()
    # Adicionando uma margem à esquerda de 15px para afastar o texto do ícone
    texts_layout.setContentsMargins(15, 0, 0, 0)
    # --- 3. ALINHAMENTO VERTICAL (Textos) ---
    texts_layout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    
    sub_text_label = QLabel(initial_sub)
    sub_text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    sub_text_label.setStyleSheet("color: #CCCCCC; font-size: 18px;")
    
    main_text_label = QLabel(initial_main)
    main_text_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    main_text_label.setStyleSheet("color: #FFFFFF; font-size: 32px; font-weight: bold;")
    
    texts_layout.addWidget(sub_text_label)
    texts_layout.addWidget(main_text_label)
    
    # Adiciona os componentes ao layout interno da nossa classe TrapezoidContainer
    trapezoid_container.internal_layout.addWidget(icon_label)
    trapezoid_container.internal_layout.addLayout(texts_layout)
    
    main_layout.addWidget(trapezoid_container, alignment=Qt.AlignmentFlag.AlignLeft)
    window.setLayout(main_layout)

    question_label.hide()

    update_icon(icon_label, initial_icon)
    screen_geometry = app.primaryScreen().availableGeometry()
    
    # Define o tamanho e a posição da janela para ocupar apenas a área útil
    window.setGeometry(screen_geometry)
    
    # Mostra a janela normalmente (sem forçar o FullScreen)
    window.show()

    timer = QTimer()
    timer.timeout.connect(lambda: check_queue(cmd_queue, main_text_label, sub_text_label, icon_label, question_label, app))
    timer.start(50)

    app.exec()