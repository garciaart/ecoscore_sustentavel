# habits.py
class HabitTrackerEmpresas:
    def __init__(self):
        pass
    
    def exibir_formulario(self, empresa_id):
        print("\n📝 QUESTIONÁRIO DE SUSTENTABILIDADE")
        print("=" * 40)
        print("Avalie sua empresa em cada categoria (1-5):")
        print("1 = Não implementado | 5 = Totalmente implementado")
        
        categorias = {
            "energia": "Uso de energia renovável",
            "agua": "Gestão eficiente de água", 
            "residuos": "Gestão de resíduos sólidos",
            "emissões": "Controle de emissões de carbono",
            "fornecedores": "Cadeia de fornecedores sustentáveis",
            "social": "Responsabilidade social",
            "governança": "Governança corporativa sustentável"
        }
        
        respostas = {}
        total_score = 0
        
        for categoria, descricao in categorias.items():
            while True:
                try:
                    nota = int(input(f"\n{descricao} (1-5): "))
                    if 1 <= nota <= 5:
                        respostas[categoria] = nota
                        total_score += nota * 3  # Peso 3 para cada categoria
                        break
                    else:
                        print("❌ Digite um número entre 1 e 5")
                except ValueError:
                    print("❌ Digite um número válido")
        
        # Calcular score final (máximo 105 pontos)
        score_final = min(100, int((total_score / 105) * 100))
        
        # Determinar nível
        if score_final >= 80:
            nivel = "EXCELENTE 🌟"
        elif score_final >= 60:
            nivel = "BOM ✅"
        elif score_final >= 40:
            nivel = "REGULAR ⚠️"
        else:
            nivel = "PRECISA MELHORAR 🚨"
        
        print(f"\n🎯 Score calculado: {score_final}/100")
        print(f"🏆 Nível de sustentabilidade: {nivel}")
        
        return {
            "empresa_id": empresa_id,
            "score_total": score_final,
            "nivel": nivel,
            "detalhes": respostas
        }