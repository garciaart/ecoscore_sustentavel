from auth import AuthSystem
from habits_empresas import HabitTrackerEmpresas
from scoring_empresas import ScoringSystemEmpresas
from tips_empresas import TipsSystemEmpresas
from dashboard_empresas import DashboardEmpresas
from database import Database


def main():
    auth = AuthSystem()
    habits = HabitTrackerEmpresas()
    scoring = ScoringSystemEmpresas()
    tips = TipsSystemEmpresas()
    dashboard = DashboardEmpresas()
    
    print("🏢 ECO SCORE EMPRESAS")
    print("=" * 40)
    print("Sistema de Sustentabilidade Empresarial")
    print("Avaliação e Melhoria Contínua para Empresas")
    
    while True:
        if not auth.get_empresa_logada():
            # Menu não logado
            print("\n📋 MENU PRINCIPAL:")
            print("1. 🏢 Cadastrar Empresa")
            print("2. 🔐 Login Empresa")
            print("3. 📊 Ranking Empresas")
            print("4. 🚪 Sair")
            
            opcao = input("\n👉 Escolha: ")
            
            if opcao == "1":
                auth.cadastrar_empresa()
            elif opcao == "2":
                if auth.login():
                    continue
            elif opcao == "3":
                exibir_ranking_empresas(auth.db)
            elif opcao == "4":
                print("\n🌱 Obrigado por usar o Eco Score Empresas!")
                break
            else:
                print("❌ Opção inválida!")
        else:
            # Menu logado
            empresa = auth.get_empresa_logada()
            print(f"\n👋 Bem-vindo(a), {empresa.nome_fantasia}!")
            print("📋 MENU DA EMPRESA:")
            print("1. 📝 Preencher Questionário Sustentabilidade")
            print("2. 📊 Ver Meu Dashboard")
            print("3. 💡 Receber Dicas Personalizadas")
            print("4. 📋 Gerar Relatório Completo")
            print("5. 🔐 Logout")
            
            opcao = input("\n👉 Escolha: ")
            
            if opcao == "1":
                if habits.exibir_formulario(empresa.id):
                    # Calcular pontuação automaticamente
                    resultado = scoring.calcular_pontuacao(empresa.id)
                    if resultado:
                        print(f"\n🎯 Score de Sustentabilidade: {resultado['total']}%")
                        print(f"🏆 Nível: {resultado['nivel']}")
            elif opcao == "2":
                dashboard.exibir_dashboard(empresa.id)
            elif opcao == "3":
                pontuacoes = scoring.db.listar_pontuacoes_empresa(empresa.id)
                if pontuacoes:
                    pontuacao_recente = max(pontuacoes, key=lambda p: p.data)
                    tips.gerar_dicas_personalizadas(pontuacao_recente.detalhes)
                else:
                    print("❌ Preencha o questionário de sustentabilidade primeiro!")
            elif opcao == "4":
                pontuacoes = scoring.db.listar_pontuacoes_empresa(empresa.id)
                if pontuacoes:
                    pontuacao_recente = max(pontuacoes, key=lambda p: p.data)
                    tips.gerar_relatorio_completo(
                        empresa,
                        pontuacao_recente.score_total,
                        pontuacao_recente.nivel_sustentabilidade
                    )
                else:
                    print("❌ Preencha o questionário primeiro!")
            elif opcao == "5":
                auth.logout()
            else:
                print("❌ Opção inválida!")


def exibir_ranking_empresas(db):
    print("\n🏆 RANKING DE EMPRESAS SUSTENTÁVEIS")
    print("=" * 40)
    
    empresas = db.listar_empresas()
    
    if not empresas:
        print("📭 Nenhuma empresa cadastrada")
        return
    
    ranking = []
    
    for empresa in empresas:
        pontuacoes = db.listar_pontuacoes_empresa(empresa.id)
        if pontuacoes:
            ultima_pontuacao = max(pontuacoes, key=lambda p: p.data)
            ranking.append((
                empresa,
                ultima_pontuacao.score_total,
                ultima_pontuacao.nivel_sustentabilidade
            ))
    
    if not ranking:
        print("📊 Nenhuma empresa com avaliação de sustentabilidade")
        return
    
    # Ordenar por score (melhores primeiro)
    ranking.sort(key=lambda x: x[1], reverse=True)
    
    print("\n🥇 TOP EMPRESAS SUSTENTÁVEIS:")
    for i, (empresa, score, nivel) in enumerate(ranking[:10], 1):
        medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
        print(f"   {medal} {empresa.nome_fantasia} - {score}% - {nivel}")


if __name__ == "__main__":
    main()
