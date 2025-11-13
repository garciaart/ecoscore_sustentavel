# dashboard.py
class DashboardEmpresas:
    def __init__(self):
        from auth import Database
        self.db = Database()
    
    def exibir_dashboard(self, empresa_id):
        print("\n📊 DASHBOARD DA EMPRESA")
        print("=" * 30)
        
        pontuacoes = self.db.listar_pontuacoes_empresa(empresa_id)
        
        if not pontuacoes:
            print("📭 Nenhuma avaliação de sustentabilidade encontrada")
            print("💡 Complete o questionário para ver seu dashboard!")
            return
        
        ultima_pontuacao = max(pontuacoes, key=lambda p: p.data)
        
        print(f"🎯 Score Atual: {ultima_pontuacao.score_total}/100")
        print(f"🏆 Nível: {ultima_pontuacao.nivel_sustentabilidade}")
        print(f"📅 Última avaliação: {ultima_pontuacao.data.strftime('%d/%m/%Y')}")
        
        # Evolução histórica
        if len(pontuacoes) > 1:
            primeira_pontuacao = min(pontuacoes, key=lambda p: p.data)
            evolucao = ultima_pontuacao.score_total - primeira_pontuacao.score_total
            print(f"📈 Evolução: {evolucao:+d} pontos")
        
        print("\n📋 DETALHES POR CATEGORIA:")
        for categoria, nota in ultima_pontuacao.detalhes.items():
            barras = "█" * nota + "░" * (5 - nota)
            print(f"   {categoria.upper()}: {barras} ({nota}/5)")