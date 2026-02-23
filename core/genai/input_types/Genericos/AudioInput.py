from core.genai.input_types.AbstractInput import AbstractInput, retorno_processamento
from typing import Callable

class AudioInput(AbstractInput[[str]]):
    def __init__(self, dados: bytes, mime_type: str):
        self.dados = dados
        self.mime_type = mime_type

    def process(self, retorno_lambda: Callable[[bytes, str], retorno_processamento]) -> list[str | retorno_processamento]:
        part = retorno_lambda(self.dados, self.mime_type)

        return ['Por favor, interprete e execure quaisquer solicitações desse áudio?', part]