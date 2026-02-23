from pydantic import BaseModel
from core.models.tipos.NivelSeguranca import NivelSeguranca
from core.models.tipos.CategoriaSeguranca import CategoriaSeguranca

class SegurancaConfigs(BaseModel):
    categoria: CategoriaSeguranca
    nivel: NivelSeguranca