import os
import sys
from typing import Callable, Type
from pathlib import Path

from datetime import datetime

from core.gui.AbstractGUI import AbstractGUI
from core.inputs.implementation.audio_SpeechRecognition.config_pydantic import AudioSpeechRecognitionConfig
from core.inputs.implementation.audio_SpeechRecognition.functions.record_audio import record_audio
from core.inputs.implementation.audio_SpeechRecognition.functions.save_wave_file import save_wav_file
from core.inputs.register_input import register_input
from core.config.AbstractConfig import AbstractConfig
from core.inputs.AbstractInputSource import AbstractInputSource

try:
    import pyaudio # type: ignore
    import speech_recognition as sr # type: ignore

except ImportError:
    # Informa o usuário sobre a falta de bibliotecas
    print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
    os.system(f"{sys.executable} -m pip install SpeechRecognition pyaudio")
    print("Bibliotecas instaladas com sucesso.")

    import pyaudio # type: ignore
    import speech_recognition as sr # type: ignore

@register_input("audio")
class audio_SpeechRecognition(AbstractInputSource):
    def __init__(self, get_config_class: Callable[[str], Type[AbstractConfig]], output_folder: str, user_interface: AbstractGUI) -> None:
        self.get_config = get_config_class
        self.user_interface = user_interface

        self.icon = Path(r"./assets/mic_idle.png")
        self.user_interface.set_icon(self.icon)
        
        self.dir = Path(__file__).parent.resolve()
        self.config_path = os.path.join(self.dir, 'config.ini')
        self._config_source = get_config_class('ini')(category='AUDIO', pydantic_model=AudioSpeechRecognitionConfig, file_path=self.config_path)

        self.recognizer = sr.Recognizer()
        self.microphone_index = int(self.config_source.get_config('microphone'))
        self.microphone = sr.Microphone(device_index=self.microphone_index)

        self.calibrate_microphone()

        self.output_folder = output_folder

    @property
    def config_source(self) -> AbstractConfig:
        return self._config_source

    def calibrate_microphone(self) -> None:
        print("Calibrando o ruído ambiente... Aguarde um segundo.")

        r = self.recognizer

        calib_duration = float(self.config_source.get_config('calib_duration'))

        old_sub_text = self.user_interface.sub_text

        self.user_interface.set_main_text("Calibrando o ruído ambiente.")
        self.user_interface.set_sub_text("é necessario silêncio.")

        with self.microphone as source:
            r.adjust_for_ambient_noise(source, duration=calib_duration)

        self.user_interface.set_main_text("Calibração concluída!")
        self.user_interface.set_sub_text(old_sub_text)

        print("Calibração concluída.")

    def generate_file_name(self) -> str:
        return f"{self.output_folder}/{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.wav"

    def generate_file(self) -> Path:

        pause_threshold = float(self.config_source.get_config('pause_threshold'))

        r = self.recognizer

        file_name = self.generate_file_name()

        audio_bytes = record_audio(r, self.microphone, pause_threshold, self.user_interface)

        file_path = save_wav_file(file_name, audio_bytes)

        return file_path