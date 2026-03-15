from pydantic import BaseModel, Field

class AudioSpeechRecognitionConfig(BaseModel):
    microphone_index: int | None = Field(default=None, description="Index do microfone a ser utilizado.")
    calib_duration: float = Field(default=1.0, description="Duração em segundos para calibração do ruído ambiente.")
    pause_threshold: float = Field(default=0.8, description="Segundos de áudio não falado antes de considerar uma frase completa.")
