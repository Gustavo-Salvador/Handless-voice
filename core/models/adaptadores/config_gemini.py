from google.genai import types

from core.models.IAConfigs import IAConfigs
from core.models.tipos.NivelPensamento import NivelPensamento

def config_gemini_adaptador(config: IAConfigs) -> types.GenerateContentConfig:
    dict_pensamento = {0: types.ThinkingLevel.THINKING_LEVEL_UNSPECIFIED, 1: types.ThinkingLevel.LOW, 2: types.ThinkingLevel.MEDIUM, 3: types.ThinkingLevel.HIGH}
    dict_categoria_seguranca = {0: types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, 1: types.HarmCategory.HARM_CATEGORY_HARASSMENT, 2: types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, 3: types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT}
    dict_nivel_seguranca = {0: types.HarmBlockThreshold.BLOCK_NONE, 1: types.HarmBlockThreshold.BLOCK_ONLY_HIGH, 2: types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE, 3: types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE}
    raw_tools_config = []
    tools_paresed: list[types.Tool] = []
    
    if len(config.ferramentas) > 0:
        raw_tools_config = config.ferramentas

    for tool_dict in raw_tools_config:
        func_declaration = types.FunctionDeclaration(name=tool_dict["name"], description=tool_dict["description"], parameters=tool_dict["parameters"])
        tools_paresed.append(types.Tool(function_declarations=[func_declaration]))

    if config.mecanismo_busca:
        tools_paresed.append(types.Tool(google_search=types.GoogleSearch()))

    if config.nivel_pensamento == NivelPensamento.NENHUM:
        config_pensamento = types.ThinkingConfig()
    else:
        config_pensamento = types.ThinkingConfig(
            thinking_level=dict_pensamento[config.nivel_pensamento.value]
        )

    if config.seguranca is not None:
        config_seguranca: list[types.SafetySetting] = []
        for conf in config.seguranca:
            if conf.nivel.value is -1:
                continue

            config_seguranca.append(types.SafetySetting(
                category=dict_categoria_seguranca[conf.categoria.value],
                threshold=dict_nivel_seguranca[conf.nivel.value]
            ))
    else:
        config_seguranca = [types.SafetySetting(category=k, threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE) for _, k in dict_categoria_seguranca.items()]

    return types.GenerateContentConfig(
        temperature=config.temperatura,
        top_k=config.top_k,
        top_p=config.top_p,
        max_output_tokens=config.max_tokens,
        seed=config.semente,
        system_instruction=config.instrucoes_sistema,
        tools=tools_paresed,
        thinking_config=config_pensamento,
        safety_settings=config_seguranca
    )