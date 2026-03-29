from pydantic import BaseModel, Field

class MainConfig(BaseModel):
    input_type: str = Field(default="audio", description="Tipo de entrada, pode ser 'texto', 'video' ou 'áudio'.")
    ia_type: str = Field(default="gemini", description="Tipo de IA a ser utilizada (ex: 'GPT', 'Gemini').")
    ia_model: str = Field(default="gemini-3-pro-preview", description="Modelo de IA a ser utilizado.")
    api_key: str = Field(description="Chave de API para autenticação com o serviço de IA.")
    gui_type: str = Field(default="pyqt6", description="Tipo de interface gráfica a ser utilizada (ex: 'pyqt6', 'tkinter').")