from pathlib import Path
from typing import Any
from core.genai.AbstractGenai import AbstractGenai
from core.genai.RegistrarIADecorador import RegistrarIA

from google import genai
from google.genai import types

from core.genai.input_types.lambdas.gemini.transform_bytes_to_part import transform_bytes_to_part
from core.genai.input_types.lambdas.gemini.transform_to_content import transform_to_content
from core.genai.input_types.AbstractInput import AbstractInput
from core.genai.input_types.transform_to_input import transform_to_input
from core.models.IAConfigs import IAConfigs
from core.models.adaptadores.config_gemini import config_gemini_adaptador

@RegistrarIA("gemini")
class LLMGemini(AbstractGenai):
    def __init__(self, IAConfigs: IAConfigs[types.Tool]):
        self.model = IAConfigs.model
        self.config = config_gemini_adaptador(IAConfigs)
        self.client = genai.Client(api_key=IAConfigs.api_key)
    
    def enviar_prompt(self, prompt: str | tuple[str, bytes] | Path | AbstractInput[[str]], **kwargs: dict[str, Any]) -> str | None:
        input_data: AbstractInput[[str]] | None = None

        if type(prompt) is str:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt, 
                config=self.config
            )

            return response.text
        
        else:
            input_data = transform_to_input(prompt)

            if input_data is None:
                return None
            
            part = input_data.process(transform_bytes_to_part)

            structured_content = transform_to_content(part)


            response = self.client.models.generate_content(
                model=self.model,
                contents=structured_content, 
                config=self.config
            )

            return response.text
        
        return ''