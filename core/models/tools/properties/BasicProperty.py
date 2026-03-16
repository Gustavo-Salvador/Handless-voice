from typing import Generic, Type, TypeVar

from pydantic import BaseModel, model_validator

TType = TypeVar("TType")

class BasicProperty(BaseModel, Generic[TType]):
    prop_type: Type[TType] | None = None
    description: str

    @model_validator(mode='after')
    def _set_prop_type(self) -> 'BasicProperty[TType]':
        if self.prop_type is None:
            # O Pydantic V2 guarda as informações do genérico instanciado (ex: [int]) nestes metadados
            metadata = getattr(self.__class__, '__pydantic_generic_metadata__', {})
            args = metadata.get('args')
            
            if args:
                self.prop_type = args[0]  # Extrai o primeiro argumento genérico (TType)
                
        return self