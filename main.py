import os
import sys
import subprocess 
import time
from pathlib import Path

from core.conteiners.global_conteiner import GlobalContainer
from core.functions.clear_input_files import clear_input_files
from core.functions.read_str_file import read_str_file
from core.genai.get_ia_class import get_ia_class

from core.inputs.get_input_class import get_input_class
from core.models.IAConfigs import IAConfigs

from core.config.implementations import *
from core.config.get_config_class import get_config_class
from core.functions.generate_tool_declaration import generate_tool_declaration

import core.genai.implementations # type: ignore

import core.tools.implementation # type: ignore
from core.tools.get_tool_class import get_tool_class

import core.gui.implementations # type: ignore
from core.gui.get_gui_class import get_gui_class 

from core.models.MainConfig import MainConfig

if __name__ == "__main__":
    try:
        import pydantic # type: ignore      

    except ImportError as e:
        print("\033[91mErro:\033[0m Algumas bibliotecas não estão instaladas, tentando instalar.")
        
        import os
        if not os.path.isfile("requiriments.txt"):
            # Erro: Printar em vermelho
            print("\033[91mArquivo 'requiriments.txt' não encontrado.\033[0m")
            print('Favor reinstalar o programa no github "https://github.com/Gustavo-Salvador/Handless-voice"')
            sys.exit(1)

        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requiriments.txt"])
        print("Bibliotecas instaladas com sucesso.")

    config = get_config_class('ini')('GENERAL', MainConfig, './configs/main_config.ini')

    system_instructions = read_str_file('./configs/system_instructions.md')

    api_key = config.get_config('api_key')
    ia_type = config.get_config('ia_type')
    ia_model = config.get_config('ia_model')
    input_type = config.get_config('input_type')
    gui_type = config.get_config('gui_type')

    ia_config = IAConfigs(
        api_key=api_key,
        model=ia_model,
        instrucoes_sistema=system_instructions
    )

    gui = get_gui_class(gui_type)()
    gui.set_sub_text("Handless Voice")
    gui.set_main_text('Iniciando...')
    default_icon_path = Path(r"./assets/default_icon.png")
    if default_icon_path.exists():
        gui.set_icon(default_icon_path)
    
    try:
        gui.start()

        input_generator = get_input_class(input_type)(get_config_class, './input_files', gui)

        global_conteiner = GlobalContainer()
        global_conteiner.gui = gui
        global_conteiner.input_source = input_generator

        all_tools = get_tool_class(tool_name='*')

        if not isinstance(all_tools, dict):
            raise ValueError("Esperado um dicionário de ferramentas, mas recebeu outro tipo.")
        
        tool_declaration = generate_tool_declaration(all_tools)

        ia_config.ferramentas = tool_declaration

        LLMGemini = get_ia_class(ia_type)

        llm = LLMGemini(IAConfigs=ia_config, tool_getter=get_tool_class, user_interface=gui)

        global_conteiner.config = config
        global_conteiner.genai = llm

        error_counter = 0

        while True:
            if error_counter >= 3:
                gui.set_main_text('Erro...')
                gui.set_question_text('Ocorreu uma série de erros inesperados, tente executar novamente o programa. Se isso persistir contate o desenvolvedor.')
                gui.show_question()
                time.sleep(7)
                break

            try:
                user_ask = input_generator.generate_file()

                ia_response = llm.enviar_prompt(user_ask)

                if ia_response == '{{quit}}':
                    gui.set_main_text('Encerrando...')
                    time.sleep(1)
                    break

                if ia_response is not None:
                    gui.set_question_text(ia_response)
                    gui.show_question()
                    print(ia_response)

                clear_input_files()

            except Exception as e:
                print(e)
                error_counter += 1

    finally:
        gui.stop()
        clear_input_files()