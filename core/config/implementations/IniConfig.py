import os
import sys
from typing import Any, Type

try:
    from configparser import ConfigParser
    
except ImportError:
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install configparser")
    print("Bibliotecas instaladas com sucesso.")
    from configparser import ConfigParser

from pydantic import BaseModel

from core.config.AbstractConfig import AbstractConfig
from core.config.register_config import register_config

@register_config('ini')
class IniConfig(AbstractConfig):
    @property
    def file_path(self):
        return self._file_path

    @property
    def category(self) -> str:
        return self._category
    
    @property
    def pydantic_model(self) -> Type[BaseModel]:
        return self._base_model

    def __init__(self, category: str, pydantic_model: Type[BaseModel], file_path: str = './config.ini'):
        self._file_path = file_path
        self._category = category
        self._base_model = pydantic_model

        self.config_parser = ConfigParser()
        self.config_parser.read(self._file_path)

        if not self.config_parser.has_section(category):
            self.config_parser.add_section(category)
            with open(self._file_path, 'w') as configfile:
                self.config_parser.write(configfile)

        self.config = self.config_parser[category]

    def get_config(self, name: str) -> Any | None:
        if name in self.config:
            return self.config[name]
        return None

    def set_config(self, name: str, value: Any) -> None:      
        self.config_parser[self._category][name] = value
                
        with open(self._file_path, 'w') as configfile:
            self.config_parser.write(configfile)
            
    def to_pydantic(self) -> BaseModel:
        return self._base_model.model_validate(self.config)