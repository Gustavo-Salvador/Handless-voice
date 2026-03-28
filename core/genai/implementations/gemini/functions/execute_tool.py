from pathlib import Path
from typing import Any, Callable, Type

from google.genai.types import GenerateContentResponse, Part, FunctionResponseBlob, FunctionResponsePart, FunctionResponse
from core.functions.read_file_to_bytes import read_file_to_bytes
from core.tools.AbstractTool import AbstractTool


def execute_tool(ia_response: GenerateContentResponse, tool_getter: Callable[[str], Type[AbstractTool[Any, Any]] | dict[str, Type[AbstractTool[Any, Any]]]]) -> tuple[bool, list[Part | str], bool]:
    should_quit = False
    
    if ia_response.function_calls is None:
        return False, [], should_quit
    
    if len(ia_response.function_calls) == 0 or ia_response.candidates is None:
        return False, [], should_quit
    
    response_parts: list[Part | str] = []

    candidate = ia_response.candidates[0]

    if candidate.content is None or candidate.content.parts is None:
        return False, [], should_quit
    
    for resp_part in candidate.content.parts:
        if resp_part.function_call is None:
            continue
        
        function_call = resp_part.function_call
        if function_call.name is None:
            continue
        
        tool_name = function_call.name

        if tool_name == 'quit':
            should_quit = True
            return False, response_parts, should_quit

        print(f'calling tool: {tool_name} with args: {function_call.args}')

        tool_class = tool_getter(tool_name)

        args = function_call.args or {}

        if isinstance(tool_class, dict):
            if tool_name not in tool_class:
                continue
            
            tool_class = tool_class[tool_name]

        result = tool_class().execute(**args)

        if result is not None:
            if isinstance(result, Path):
                input_from_result = read_file_to_bytes(result)

                if input_from_result is None:
                    continue
                
                mime_type, data_bytes = str(input_from_result[0]), input_from_result[1]
                
                # 1. Cria a resposta da função (Apenas metadados simples em JSON)
                function_response_part = Part.from_function_response(
                    name=tool_name,
                    response={"status": "success", "message": "File generated and attached as media."},
                )
                response_parts.append(function_response_part)

                # 2. Cria a mídia de forma independente, utilizando a mesma lógica padrão do áudio inicial
                media_part = Part.from_bytes(
                    data=data_bytes,
                    mime_type=mime_type
                )
                response_parts.append(media_part)
                
                # Use 'continue' para pular a adição no final do loop, 
                # já que as duas partes necessárias já foram incluídas.
                continue

                # input_from_result = read_file_to_bytes(result)

                # if input_from_result is None:
                #     continue
                
                # mime_type, data_bytes = str(input_from_result[0]), input_from_result[1]
                
                # function_response_part = Part(
                #     function_response=FunctionResponse(
                #         name=tool_name,
                #         id=function_call.id, 
                #         response={"status": "success", "message": "File read successfully"}, 
                #         parts=[
                #             FunctionResponsePart(
                #                 inline_data=FunctionResponseBlob(
                #                     data=data_bytes,
                #                     mime_type=mime_type
                #                 )
                #             )
                #         ]
                #     )
                # )

            else:
                function_response_part = Part.from_function_response(
                    name=tool_name,
                    response={"result": result},
                )

            response_parts.append(function_response_part)
                
    return True, response_parts, should_quit