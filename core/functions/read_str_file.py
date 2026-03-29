def read_str_file(file_path: str, encoding: str = 'utf-8') -> str:
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return ""
    
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return ""