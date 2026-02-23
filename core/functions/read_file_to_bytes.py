from mimetypes import guess_type
from pathlib import Path

def read_file_to_bytes(file_path: Path | str) -> tuple[str | None, bytes] | None:
    try:
        if isinstance(file_path, str):
            file_path = Path(file_path)
        
        tipo = guess_type(file_path)
        
        with open(file_path, 'rb') as file:
            dados = file.read()

        return tipo[0], dados
        
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None
    
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None