def separate_mimetype(mime_type: str) -> tuple[str, str]:
    if '/' not in mime_type:
        raise ValueError(f"Invalid MIME type: {mime_type}")

    type_part, subtype_part = mime_type.split('/', 1)
    return type_part, subtype_part