from pathlib import Path
from pydantic import BaseModel

from core.conteiners.global_conteiner import GlobalContainer
from core.tools.AbstractTool import AbstractTool
from core.tools.register_tool import register_tool

from .parameters import parameters

@register_tool('ask_question')
class AskQuestion(AbstractTool[[str], Path]):
    def __init__(self) -> None:
        conteiner = GlobalContainer()
        self.user_interface = conteiner.gui
        self.input_source = conteiner.input_source
        
        # Save previous UI state
        self.old_main_text = self.user_interface.main_text
        self.old_sub_text = self.user_interface.sub_text

    @property
    def description(self) -> str:
        return ("Asks a question to the user and waits for their response."
                "This should be used if you not sure about the user intention, "
                "or if the user didn't ask anything.")

    @property
    def parameters(self) -> type[BaseModel]:
        return parameters

    def execute(self, question: str) -> Path:
        self.user_interface.set_question_text(question)
        self.user_interface.show_question()

        self.user_interface.set_sub_text('Aguardando resposta...')

        generated_file_path = self.input_source.generate_file()

        self.user_interface.set_main_text(self.old_main_text)
        self.user_interface.set_sub_text(self.old_sub_text)

        return generated_file_path