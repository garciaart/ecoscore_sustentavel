class TipsSystemEmpresas:
    def __init__(self):
        self.dicas = {
            'coleta_seletiva': [
                "🗑️ Implemente coleta seletiva com parceiros de reciclagem locais",
                "♻️ Treine funcionários sobre separação correta de resíduos",
                "📊 Monitore métricas de reciclagem mensalmente"
            ],
            'compostagem': [
                "🥕 Implemente compostagem para resíduos orgânicos da cozinha",
                "🌱 Use composto produzido em jardins ou doe para agricultura local",
                "📚 Ofereça treinamento sobre compostagem para a equipe"
            ],
            'reducao_plasticos': [
                "🚫 Substitua plásticos descartáveis por alternativas reutilizáveis",
                "🛍️ Ofereça desconto para clientes que trazem próprios recipientes",
                "📦 Use embalagens biodegradáveis ou recicladas"
            ],
            'energia_renovavel': [
                "☀️ Instale painéis solares para reduzir custos com energia",
                "💡 Mude para fornecedor de energia renovável",
                "🌬️ Considere energia eólica se viável na região"
            ],
            'eficiencia_energetica': [
                "💡 Substitua lâmpadas por LED em toda empresa",
                "❌ Implemente sistema de desligamento automático de equipamentos",
                "🏢 Faça auditoria energética para identificar melhorias"
            ],
            'reuso_agua': [
                "💧 Capture água da chuva para limpeza e jardins",
                "🔄 Instale sistema de reuso de água cinza",
                "🚰 Use redutores de vazão em torneiras e chuveiros"
            ],
            'consumo_agua': [
                "📊 Instale hidrômetros para monitorar consumo por setor",
                "🔧 Corrija vazamentos imediatamente",
                "🌿 Use plantas nativas que requerem menos irrigação"
            ],
            'fornecedores_locais': [
                "🏭 Priorize fornecedores dentro de 100km de distância",
                "🤝 Crie parcerias com produtores locais",
                "📈 Estabeleça programa de desenvolvimento de fornecedores locais"
            ],
            'produtos_organicos': [
                "🥦 Aumente gradualmente percentual de ingredientes orgânicos",
                "🏷️ Destaque produtos orgânicos no cardápio/estoque",
                "👨‍🌾 Participe de feiras de produtores orgânicos"
            ],
            'frota_sustentavel': [
                "🚗 Substitua veículos antigos por modelos elétricos ou híbridos",
                "⛽ Use biocombustíveis quando possível",
                "🛵 Considere veículos elétricos para entregas locais"
            ],
            'logistica_eficiente': [
                "🗺️ Otimize rotas de entrega para reduzir quilometragem",
                "📦 Consolide entregas para reduzir viagens",
                "🚲 Use bicicletas para entregas em curta distância"
            ]
        }
    
    def gerar_dicas_personalizadas(self, scores):
        print("\n💡 DICAS DE SUSTENTABILIDADE EMPRESARIAL")
        print("=" * 50)
        
        # Ordenar categorias por pior score
        categorias_ordenadas = sorted(scores.items(), key=lambda x: x[1])
        
        print("\n🎯 ÁREAS PARA MELHORIA:")
        for categoria, score in categorias_ordenadas[:4]:  # Top 4 piores
            if score == 0 or score < 5:  # Se score for muito baixo
                print(f"\n📌 {categoria.replace('_', ' ').upper()}:")
                for dica in self.dicas[categoria][:2]:
                    print(f"   • {dica}")
        
        print(f"\n🌟 ÁREAS DE DESTAQUE:")
        for categoria, score in categorias_ordenadas[-3:]:  # Top 3 melhores
            if score > 0:
                print(f"   ✅ {categoria.replace('_', ' ').upper()} - Score: {score}")
    
    def gerar_relatorio_completo(self, empresa, score_total, nivel):
        print("\n📋 RELATÓRIO DE SUSTENTABILIDADE")
        print("=" * 40)
        print(f"🏢 Empresa: {empresa.nome_fantasia}")
        print(f"📊 CNPJ: {empresa.cnpj}")
        print(f"🎯 Score Total: {score_total}/100")
        print(f"🏆 Nível: {nivel}")
        print(f"📅 Data: {empresa.data_cadastro.strftime('%d/%m/%Y')}")