from typing import Optional

from core.config.AbstractConfig import AbstractConfig
from core.genai.AbstractGenai import AbstractGenai
from core.inputs.AbstractInputSource import AbstractInputSource
from core.gui.AbstractGUI import AbstractGUI

class GlobalContainer:
    """
    A singleton container to share core components across the application.
    """
    _instance: Optional['GlobalContainer'] = None
    _config: Optional[AbstractConfig] = None
    _genai: Optional[AbstractGenai] = None
    _input_source: Optional[AbstractInputSource] = None
    _gui: Optional[AbstractGUI] = None

    def __new__(cls) -> 'GlobalContainer':
        if cls._instance is None:
            cls._instance = super(GlobalContainer, cls).__new__(cls)
            cls._instance._config = None
            cls._instance._genai = None
            cls._instance._input_source = None
            cls._instance._gui = None
        return cls._instance

    @property
    def config(self) -> AbstractConfig:
        if self._config is None:
            raise RuntimeError("GlobalContainer: Config has not been initialized.")
        return self._config

    @config.setter
    def config(self, value: AbstractConfig) -> None:
        self._config = value

    @property
    def genai(self) -> AbstractGenai:
        if self._genai is None:
            raise RuntimeError("GlobalContainer: GenAI has not been initialized.")
        return self._genai

    @genai.setter
    def genai(self, value: AbstractGenai) -> None:
        self._genai = value

    @property
    def input_source(self) -> AbstractInputSource:
        if self._input_source is None:
            raise RuntimeError("GlobalContainer: InputSource has not been initialized.")
        return self._input_source

    @input_source.setter
    def input_source(self, value: AbstractInputSource) -> None:
        self._input_source = value

    @property
    def gui(self) -> AbstractGUI:
        if self._gui is None:
            raise RuntimeError("GlobalContainer: GUI has not been initialized.")
        return self._gui

    @gui.setter
    def gui(self, value: AbstractGUI) -> None:
        self._gui = value
