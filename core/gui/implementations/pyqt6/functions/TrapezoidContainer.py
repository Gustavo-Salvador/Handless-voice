from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtGui import QPaintEvent, QPainter, QPainterPath, QColor, QPolygonF

class TrapezoidContainer(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.internal_layout = QHBoxLayout(self)
        
        # --- 1. CORREÇÃO DO TEXTO VAZANDO ---
        # Definimos quantos pixels a parte de cima será menor que a base
        self.diagonal_width = 80 
        padding = 20
        
        # Setamos as margens: (Esquerda, Topo, Direita, Baixo)
        # A margem DIREITA recebe o 'diagonal_width' para criar uma barreira invisível
        self.internal_layout.setContentsMargins(padding, padding, self.diagonal_width + padding, padding)
        
        # --- 3. ALINHAMENTO VERTICAL (Container Geral) ---
        self.internal_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

    def paintEvent(self, a0: QPaintEvent | None) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # --- 2. TRANSPARÊNCIA ---
        # QColor(Red, Green, Blue, Alpha). O Alpha vai de 0 (transparente) a 255 (sólido)
        # Ajuste o último número (210) para deixar mais ou menos transparente
        background_color = QColor(40, 40, 40, 210) 
        painter.setBrush(background_color)
        painter.setPen(Qt.PenStyle.NoPen) 

        width = self.width()
        height = self.height()

        # O topo termina "diagonal_width" pixels antes da base
        points = QPolygonF([
            QPointF(0, 0),
            QPointF(width - self.diagonal_width, 0), # Topo recuado
            QPointF(width, height),                  # Base esticada até o final
            QPointF(0, height)
        ])
        
        path = QPainterPath()
        path.addPolygon(points)
        painter.drawPath(path)

    # Função auxiliar para adicionar widgets ao layout interno
    def add_widget(self, widget: QWidget, stretch: int = 0, alignment: Qt.AlignmentFlag = Qt.AlignmentFlag.AlignCenter):
        self.internal_layout.addWidget(widget, stretch, alignment)

    # Função auxiliar para adicionar layouts ao layout interno
    def add_layout(self, layout: QHBoxLayout | QVBoxLayout, stretch: int = 0):
        self.internal_layout.addLayout(layout, stretch)