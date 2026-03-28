from pathlib import Path
from typing import Optional
from PIL import Image

class InfoContainer:
    """
    A container to store and share screenshot data and metadata 
    between different screen processing functions.
    """
    _instance: Optional['InfoContainer'] = None
    
    # 1. Declare the attributes and their types at the class level
    last_screenshot: Optional[Image.Image]
    last_file_path: Optional[Path]
    grid_size: tuple[int, int]
    sub_divided_list: list[tuple[int, int]] = []
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InfoContainer, cls).__new__(cls)
            cls._instance.last_screenshot = None
            cls._instance.last_file_path = None
            cls._instance.grid_size = (15, 15)
        return cls._instance

    def update(self, screenshot: Image.Image, file_path: Path):
        self.last_screenshot = screenshot
        self.last_file_path = file_path

    def append_subdivide(self, x_index: int, y_index: int):
        self.sub_divided_list.append((x_index, y_index))

    def clear(self):
        self.last_screenshot = None
        self.last_file_path = None
        self.sub_divided_list = []

