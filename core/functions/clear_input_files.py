import os
import shutil
from pathlib import Path

def clear_input_files() -> None:
    path = Path('./input_files')
    if not path.exists():
        return

    for item in os.listdir(path):
        item_path = path / item
        try:
            if item_path.is_file() or item_path.is_symlink():
                item_path.unlink()
            elif item_path.is_dir():
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")
