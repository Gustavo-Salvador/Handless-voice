from typing import Any
from configparser import ConfigParser

from core.config.AbstractConfig import AbstractConfig
from core.config.register_config import register_config

@register_config('ini')
class IniConfig(AbstractConfig):
    def __init__(self, category: str, file_path: str = './config.ini'):
        self.file_path = file_path
        self.category = category
        self.config_parser = ConfigParser()
        self.config_parser.read(self.file_path)

        if not self.config_parser.has_section(category):
            self.config_parser.add_section(category)
            with open(self.file_path, 'w') as configfile:
                self.config_parser.write(configfile)

        self.config = self.config_parser[category]

    def get_config(self, name: str) -> Any | None:
        if name in self.config:
            return self.config[name]
        return None

    def set_config(self, name: str, value: Any) -> None:      
        self.config_parser[self.category][name] = value
                
        with open(self.file_path, 'w') as configfile:
            self.config_parser.write(configfile)
            