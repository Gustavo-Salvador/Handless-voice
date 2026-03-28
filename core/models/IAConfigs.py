from typing import Any

from pydantic import BaseModel

from core.models.SegurarançaConfigs import SegurancaConfigs
from core.models.tipos.NivelSeguranca import NivelSeguranca
from core.models.tipos.CategoriaSeguranca import CategoriaSeguranca
from core.models.tipos.NivelPensamento import NivelPensamento

class IAConfigs(BaseModel):
    api_key: str
    model: str
    instrucoes_sistema: str | None = None
    mecanismo_busca: bool = False
    ferramentas: list[dict[str, Any]] = []
    manter_historico: bool = False
    nivel_pensamento: NivelPensamento = NivelPensamento.MEDIO
    verbose: bool = False

    max_tokens: int | None = 65536
    top_p: float = 0.85
    top_k: float = 40
    temperatura: float = 1
    semente: int | None = None

    seguranca: list[SegurancaConfigs] | None = [
        SegurancaConfigs(categoria=CategoriaSeguranca.CONTEUDO_SEXUAL, nivel=NivelSeguranca.MEDIO_E_ACIMA),
        SegurancaConfigs(categoria=CategoriaSeguranca.ASSEDIO, nivel=NivelSeguranca.MEDIO_E_ACIMA),
        SegurancaConfigs(categoria=CategoriaSeguranca.ODIO, nivel=NivelSeguranca.MEDIO_E_ACIMA),
        SegurancaConfigs(categoria=CategoriaSeguranca.CONTEUDO_PERIGOSO, nivel=NivelSeguranca.MEDIO_E_ACIMA)
    ]