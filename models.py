from dataclasses import dataclass
from datetime import datetime

@dataclass
class Empresa:
    id: int
    cnpj: str
    razao_social: str
    nome_fantasia: str
    email: str
    senha: str
    telefone: str
    endereco: str
    segmento: str
    data_cadastro: datetime

@dataclass
class HabitoEmpresa:
    id: int
    empresa_id: int
    data: datetime
    # Gestão de Resíduos
    coleta_seletiva: str
    compostagem: str
    reducao_plasticos: str
    # Energia
    energia_renovavel: str
    eficiencia_energetica: str
    # Água
    reuso_agua: str
    consumo_agua: str
    # Fornecedores
    fornecedores_locais: str
    produtos_organicos: str
    # Transporte
    frota_sustentavel: str
    logistica_eficiente: str

@dataclass
class PontuacaoEmpresa:
    id: int
    empresa_id: int
    data: datetime
    score_total: int
    nivel_sustentabilidade: str
    detalhes: dict