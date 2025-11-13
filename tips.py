# tips.py
class TipsSystemEmpresas:
    def __init__(self):
        pass
    
    def gerar_dicas_personalizadas(self, detalhes_pontuacao):
        print("\n💡 DICAS PERSONALIZADAS")
        print("=" * 35)
        
        dicas_por_categoria = {
            "energia": [
                "Instale painéis solares para reduzir custos com energia",
                "Substitua lâmpadas por LED de baixo consumo",
                "Implemente sistema de gestão de energia inteligente"
            ],
            "agua": [
                "Instale sistemas de captação de água da chuva",
                "Use redutores de vazão em torneiras e chuveiros",
                "Implemente reuso de água em processos industriais"
            ],
            "residuos": [
                "Crie programa de reciclagem interna",
                "Reduza uso de descartáveis e embalagens",
                "Estabeleça parceria com cooperativas de reciclagem"
            ]
        }
        
        for categoria, nota in detalhes_pontuacao.items():
            if nota <= 3 and categoria in dicas_por_categoria:
                print(f"\n📌 Para melhorar em {categoria.upper()}:")
                for dica in dicas_por_categoria[categoria][:2]:
                    print(f"   • {dica}")
    
    def gerar_relatorio_completo(self, empresa, score, nivel):
        print("\n📊 RELATÓRIO COMPLETO")
        print("=" * 30)
        print(f"Empresa: {empresa.nome_fantasia}")
        print(f"Setor: {empresa.setor}")
        print(f"Tamanho: {empresa.tamanho}")
        print(f"Score de Sustentabilidade: {score}/100")
        print(f"Nível: {nivel}")
        print("\n📈 RECOMENDAÇÕES:")
        print("• Continuar monitorando métricas mensalmente")
        print("• Estabelecer metas de melhoria contínua")
        print("• Compartilhar resultados com stakeholders")
        print("• Buscar certificações sustentáveis")