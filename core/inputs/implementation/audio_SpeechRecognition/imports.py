import os, sys

def imports():
    try:
        import pyaudio # type: ignore
        import speech_recognition # type: ignore
    
    except ImportError:
        # Informa o usuário sobre a falta de bibliotecas
        print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
        os.system(f"{sys.executable} -m pip install SpeechRecognition pyaudio")
        print("Bibliotecas instaladas com sucesso.")