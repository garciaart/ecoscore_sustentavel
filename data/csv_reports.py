import pandas as pd
import os
from datetime import datetime

class CSVReportGenerator:
    def __init__(self):
        self.pasta_relatorios = "relatorios_csv"
        os.makedirs(self.pasta_relatorios, exist_ok=True)
    
    def exportar_relatorio_empresa(self, empresa, pontuacao, habitos_recentes):
        # Dados principais - CORRIGIDO ENCODING
        dados_empresa = {
            'cnpj': [empresa.cnpj],
            'razao_social': [empresa.razao_social],
            'nome_fantasia': [empresa.nome_fantasia],
            'segmento': [empresa.segmento],
            'score_total_porcentagem': [pontuacao.score_total],
            'nivel_sustentabilidade': [pontuacao.nivel_sustentabilidade],
            'data_avaliacao': [pontuacao.data.strftime('%d/%m/%Y')],
            'data_geracao_relatorio': [datetime.now().strftime('%d/%m/%Y %H:%M:%S')],
            'certificacoes_recomendadas': [self._sugerir_certificacoes_texto(pontuacao.score_total)]
        }
        
        df_empresa = pd.DataFrame(dados_empresa)
        
        # Detalhes do score
        detalhes_score = {}
        for categoria, score in pontuacao.detalhes.items():
            max_score = 15 if categoria in ['energia_renovavel', 'reuso_agua'] else 10 if categoria in ['coleta_seletiva', 'compostagem', 'reducao_plasticos', 'frota_sustentavel'] else 5
            percentual = (score / max_score) * 100
            detalhes_score[categoria] = score
            detalhes_score[f'{categoria}_percentual'] = percentual
        
        detalhes_score['empresa_id'] = empresa.id
        detalhes_score['nome_empresa'] = empresa.nome_fantasia
        
        df_detalhes = pd.DataFrame([detalhes_score])
        
        # Salvar arquivos - CORRIGIDO ENCODING
        nome_base = f"relatorio_{empresa.nome_fantasia}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        arquivo_principal = f"{self.pasta_relatorios}/{nome_base}_principal.csv"
        df_empresa.to_csv(arquivo_principal, index=False, encoding='utf-8')
        
        arquivo_detalhes = f"{self.pasta_relatorios}/{nome_base}_detalhes.csv"
        df_detalhes.to_csv(arquivo_detalhes, index=False, encoding='utf-8')
        
        print(f"✅ Relatórios exportados com encoding correto:")
        print(f"   📄 {arquivo_principal}")
        print(f"   📄 {arquivo_detalhes}")
        
        return [arquivo_principal, arquivo_detalhes]