from pathlib import Path
from typing import Any
from core.functions.read_file_to_bytes import read_file_to_bytes
from core.functions.separate_mimetype import separate_mimetype
from core.genai.input_types.AbstractInput import AbstractInput
from .get_input_type import get_input_type

def transform_to_input(data: Any, message: str | None = None) -> AbstractInput[[str]] | None:
    prompt_tuple: tuple[str, bytes] | None = None
    input_data: AbstractInput[[str]] | None = None

    if isinstance(data, Path):
        file_info = read_file_to_bytes(data)

        if file_info is None:
            return None
        
        if file_info[0] is None:
            return None
        
        mime_type, data_bytes = str(file_info[0]), file_info[1]

        prompt_tuple = (mime_type, data_bytes)
                
    if isinstance(data, tuple): 
        if isinstance(data[0], str) and isinstance(data[1], bytes):
            prompt_tuple = (data[0], data[1])
        else:
            return None
        
    if prompt_tuple is None:
        return None
        
    input_type, _ = separate_mimetype(prompt_tuple[0])

    input_data = get_input_type(input_type)(prompt_tuple[1], prompt_tuple[0], message)
    
    if isinstance(data, AbstractInput):
        input_data = data

    return input_data