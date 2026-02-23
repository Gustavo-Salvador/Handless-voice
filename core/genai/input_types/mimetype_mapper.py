from typing import Type
from core.genai.input_types.AbstractInput import AbstractInput
from core.functions.separate_mimetype import separate_mimetype

def mimetype_mapper(mime_type: str) -> Type[AbstractInput[[str]]]:
    input_type, _ = separate_mimetype(mime_type)

    if input_type == 'audio':
        from core.genai.input_types.Genericos.AudioInput import AudioInput
        return AudioInput
    
    elif input_type == 'image':
        from core.genai.input_types.Genericos.ImagemInput import ImagemInput
        return ImagemInput
    
    raise ValueError(f"Unsupported input type: {input_type}")