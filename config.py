from pydantic import BaseModel, Field

class default_config(BaseModel):
    input_type: str = Field(default="gemini", description="Tipo de entrada, pode ser 'texto', 'video' ou 'áudio'.")
    ia_type: str = Field(description="Tipo de IA a ser utilizada (ex: 'GPT', 'Gemini').")
    api_key: str = Field(description="Chave de API para autenticação com o serviço de IA.")
