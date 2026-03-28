from google.genai.types import Part, Content

def transform_to_content(parts: list[Part | str], role: str = "user") -> Content:
    formatted_parts = [
        Part.from_text(text=p) if isinstance(p, str) else p 
        for p in parts
    ]

    structured_content = Content(
        role=role, 
        parts=formatted_parts
    )

    return structured_content