from pathlib import Path
from typing import Any, Callable, cast
from core.genai.AbstractGenai import AbstractGenai
from core.genai.register_ia import register_ia

from google import genai
from google.genai.types import Content, ContentListUnionDict

from core.gui.AbstractGUI import AbstractGUI

from .functions.transform_bytes_to_part import transform_bytes_to_part
from .functions.transform_to_content import transform_to_content
from .functions.execute_tool import execute_tool

from core.genai.input_types.AbstractInput import AbstractInput
from core.genai.input_types.transform_to_input import transform_to_input
from core.models.IAConfigs import IAConfigs
from core.models.adaptadores.config_gemini import config_gemini_adaptador
from core.tools.AbstractTool import AbstractTool

@register_ia("gemini")
class LLMGemini(AbstractGenai):
    def __init__(self, IAConfigs: IAConfigs, tool_getter: Callable[[str], type[AbstractTool[Any, Any]] | dict[str, type[AbstractTool[Any, Any]]]], user_interface: AbstractGUI):
        self.model = IAConfigs.model
        self.config = config_gemini_adaptador(IAConfigs)
        self.client = genai.Client(api_key=IAConfigs.api_key)
        self.tool_getter = tool_getter
        self.keep_history = IAConfigs.manter_historico
        self.user_interface = user_interface

        self.messages: list[Content] = []
    
    def enviar_prompt(self, prompt: str | tuple[str, bytes] | Path | AbstractInput[[str]], **kwargs: dict[str, Any]) -> str | None:
        input_data: AbstractInput[[str]] | None = None

        self.user_interface.set_main_text('Processando...')

        if type(prompt) is str:
            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt, 
                config=self.config
            )

            response_text = response.text

            if response_text is None:
                return None

            self.user_interface.set_main_text('Concluído!')
            self.user_interface.set_question_text(response_text)
            self.user_interface.show_question()

            if self.keep_history:
                self.messages = []

            return response.text
        
        else:
            input_data = transform_to_input(prompt)

            if input_data is None:
                return None
            
            part = input_data.process(transform_bytes_to_part)

            structured_content = transform_to_content(part)

            self.messages.append(structured_content)

            response = None
            loop_execution = True
            while loop_execution:
                self.user_interface.set_sub_text('Processando...')
                self.user_interface.set_main_text('Aguarde...')

                message_content_union = cast(ContentListUnionDict, self.messages)
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=message_content_union, 
                    config=self.config
                )

                self.user_interface.set_main_text('Resposta recebida!')

                if response.candidates is None or len(response.candidates) == 0:
                    return None
                
                if response.candidates[0].content is None:
                    return None

                self.messages.append(response.candidates[0].content)

                self.user_interface.set_main_text('Processando resposta...')
                loop_execution, response_parts, should_quit = execute_tool(response, self.tool_getter)

                if should_quit:
                    return '{{quit}}'

                if loop_execution:
                    structured_content = transform_to_content(response_parts)
                    self.messages.append(structured_content)

            if response is None or response.text is None:
                return None
            
            response_text = response.text

            self.user_interface.set_main_text('Concluído!')
            self.user_interface.set_question_text(response_text)
            self.user_interface.show_question()

            if self.keep_history:
                self.messages = []

            return response_text