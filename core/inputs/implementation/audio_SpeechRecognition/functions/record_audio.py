from typing import Any

from speech_recognition import Microphone, Recognizer

def record_audio(recognizer: Recognizer, source: Microphone, pause_threshold: float) -> bytes:
    r = recognizer
    r.pause_threshold = pause_threshold
    
    with source as source:
        print(f"Pode falar! A gravação vai parar após {pause_threshold} segundos de silêncio.")
        
        audio = r.listen(source)

        print("Gravação finalizada. Salvando arquivo...")

    audio_bytes: Any = audio.get_wav_data()

    if isinstance(audio_bytes, bytes):
        return audio_bytes
    
    return b''