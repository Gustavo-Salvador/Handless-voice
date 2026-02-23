from enum import Enum

class NivelSeguranca(Enum):
    DESLIGADO = -1
    NAO_BLOQUEAR = 0
    ALTO_APENAS = 1
    MEDIO_E_ACIMA = 2
    BAIXO_E_ACIMA = 3