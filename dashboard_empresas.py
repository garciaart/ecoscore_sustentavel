from database import Database
# REMOVER: from scoring_empresas import ScoringSystemEmpresas

class DashboardEmpresas:
    def __init__(self):
        self.db = Database()
        # REMOVER: self.scoring = ScoringSystemEmpresas()
    
    def exibir_dashboard(self, empresa_id):
        pontuacoes = self.db.listar_pontuacoes_empresa(empresa_id)
        empresa = self._buscar_empresa_por_id(empresa_id)
        
        if not pontuacoes:
            print("\n📊 Ainda não há dados de sustentabilidade.")
            print("   Preencha o formulário primeiro!")
            return
        
        # Pontuação mais recente
        pontuacao_recente = max(pontuacoes, key=lambda p: p.data)
        
        print("\n📊 DASHBOARD EMPRESARIAL - SUSTENTABILIDADE")
        print("=" * 50)
        print(f"🏢 EMPRESA: {empresa.nome_fantasia}")
        print(f"📋 SEGMENTO: {empresa.segmento}")
        print(f"🎯 SCORE: {pontuacao_recente.score_total}%")
        print(f"🏆 NÍVEL: {pontuacao_recente.nivel_sustentabilidade}")
        
        # Barra de progresso visual CORRIGIDA
        self._exibir_barra_progresso(pontuacao_recente.score_total)
        
        print(f"\n📈 DETALHES POR CATEGORIA:")
        categorias = {
            'coleta_seletiva': 'Coleta Seletiva',
            'compostagem': 'Compostagem',
            'reducao_plasticos': 'Redução Plásticos',
            'energia_renovavel': 'Energia Renovável',
            'eficiencia_energetica': 'Eficiência Energética',
            'reuso_agua': 'Reuso Água',
            'consumo_agua': 'Consumo Água',
            'fornecedores_locais': 'Fornecedores Locais',
            'produtos_organicos': 'Produtos Orgânicos',
            'frota_sustentavel': 'Frota Sustentável',
            'logistica_eficiente': 'Logística Eficiente'
        }
        
        for cat_key, cat_nome in categorias.items():
            score = pontuacao_recente.detalhes.get(cat_key, 0)
            # USAR VALOR FIXO TEMPORARIAMENTE - será corrigido depois
            max_score = 10  # Temporário até vermos o scoring_empresas.py
            percentual_categoria = (score / max_score) * 100 if max_score > 0 else 0
            
            barra = "█" * int(percentual_categoria / 4) + "░" * (25 - int(percentual_categoria / 4))
            print(f"   {cat_nome:20} {barra} {score:2d}/{max_score} ({percentual_categoria:.0f}%)")
        
        # Certificações sugeridas
        self._sugerir_certificacoes(pontuacao_recente.score_total)
        
        # Evolução temporal
        if len(pontuacoes) > 1:
            print(f"\n📅 EVOLUÇÃO:")
            for p in sorted(pontuacoes, key=lambda x: x.data)[-5:]:
                data_str = p.data.strftime("%d/%m")
                print(f"   {data_str}: {p.score_total}% - {p.nivel_sustentabilidade}")
    
    def _exibir_barra_progresso(self, porcentagem):
        """Exibe barra de progresso visual CORRIGIDA"""
        barras_preenchidas = int(porcentagem / 2)  # 50 caracteres = 100%
        barras_vazias = 50 - barras_preenchidas
        barra = "█" * barras_preenchidas + "░" * barras_vazias
        print(f"   [{barra}] {porcentagem}%")
        print(f"   📊 Progresso: {porcentagem}% de 100%")
    
    def _sugerir_certificacoes(self, score):
        """Sugere certificações baseadas no score"""
        print(f"\n🏅 CERTIFICAÇÕES RECOMENDADAS:")
        
        if score >= 85:
            print("   ✅ LEED - Prédios Sustentáveis")
            print("   ✅ ISO 14001 - Gestão Ambiental")
            print("   🌟 Você está pronto para certificações avançadas!")
        
        elif score >= 70:
            print("   ✅ Selo Verde - Produtos Sustentáveis")
            print("   📋 ISO 14001 - Em 3-6 meses de preparação")
            print("   💡 Foque em energia e gestão de resíduos")
        
        elif score >= 55:
            print("   📋 Programa de Sustentabilidade Empresarial")
            print("   🌿 Selo de Empresa Verde Local")
            print("   🎯 Melhore em 15 pontos para Selo Verde")
        
        elif score >= 40:
            print("   📚 Curso de Gestão Ambiental Básica")
            print("   🔧 Consultoria para diagnóstico inicial")
            print("   🎓 Capacitação da equipe em sustentabilidade")
        
        else:
            print("   🎓 Capacitação em Práticas Básicas")
            print("   📊 Diagnóstico Ambiental Completo")
            print("   🚨 Priorize ações críticas primeiro")
    
    def _buscar_empresa_por_id(self, empresa_id):
        empresas = self.db.listar_empresas()
        for emp in empresas:
            if emp.id == empresa_id:
                return emp
        return None