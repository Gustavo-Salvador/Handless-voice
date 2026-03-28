from pathlib import Path
from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

def update_icon(icon_label: QLabel, icon_path: Path) -> None:
    if icon_path and Path(icon_path).exists():
        pixmap = QPixmap(str(icon_path))
        pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        icon_label.setPixmap(pixmap)
    else:
        icon_label.clear()