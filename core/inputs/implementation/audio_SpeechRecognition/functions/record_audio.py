from pathlib import Path
from typing import Any

from speech_recognition import Microphone, Recognizer

from core.gui.AbstractGUI import AbstractGUI

def record_audio(recognizer: Recognizer, source: Microphone, pause_threshold: float, user_interface: AbstractGUI) -> bytes:
    r = recognizer
    r.pause_threshold = pause_threshold
    
    old_icon_path = user_interface.icon
    record_icon_path = Path(r"./assets/mic_recording.png")

    with source as source:

        user_interface.set_icon(record_icon_path)
        user_interface.set_main_text("Gravando...")
        print(f"Pode falar! A gravação vai parar após {pause_threshold} segundos de silêncio.")
        
        audio = r.listen(source)

        print("Gravação finalizada. Salvando arquivo...")

    audio_bytes: Any = audio.get_wav_data()

    if isinstance(audio_bytes, bytes):
        user_interface.hide_question()
        user_interface.set_icon(old_icon_path)
        user_interface.set_main_text("Gravação finalizada!")

        return audio_bytes
    
    return b''