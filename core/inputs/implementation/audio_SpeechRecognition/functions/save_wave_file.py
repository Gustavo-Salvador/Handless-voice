from pathlib import Path

def save_wav_file(filename: str, data: bytes) -> Path:
    with open(filename, 'wb') as f:
        f.write(data)
        
    return Path(filename)