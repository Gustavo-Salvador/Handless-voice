from google.genai.types import Part

def transform_bytes_to_part(dados: bytes, mime_type: str) -> Part:
    part = Part.from_bytes(
        data=dados,
        mime_type=mime_type
    )

    return part