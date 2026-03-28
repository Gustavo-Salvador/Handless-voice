from typing import Callable

from ..register_input_type import register_input_type

from core.genai.input_types.AbstractInput import AbstractInput, processed_return

@register_input_type("audio")
class AudioInput(AbstractInput[[str]]):
    def __init__(self, data: bytes, mime_type: str, message: str | None):
        self.data = data
        self.mime_type = mime_type

        if message is not None:
            self.message = message
        else:
            self.message = 'Por favor, execute ao pé da letra quaisquer solicitações desse áudio.'


    def process(self, processor: Callable[[bytes, str], processed_return]) -> list[str | processed_return]:
        part = processor(self.data, self.mime_type)

        if self.message != '':
            return [self.message, part]
        
        return [part]
