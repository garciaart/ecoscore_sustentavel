from database import Database
from models import HabitoEmpresa
from datetime import datetime

class HabitTrackerEmpresas:
    def __init__(self):
        self.db = Database()
    
    def exibir_formulario(self, empresa_id):
        print("\n📊 FORMULÁRIO DE SUSTENTABILIDADE EMPRESARIAL")
        print("=" * 50)
        print("Avalie as práticas sustentáveis da sua empresa:")
        
        # GESTÃO DE RESÍDUOS
        print("\n🗑️ GESTÃO DE RESÍDUOS")
        coleta_seletiva = self._obter_opcao_sim_nao("Implementa coleta seletiva?")
        compostagem = self._obter_opcao_sim_nao("Faz compostagem de resíduos orgânicos?")
        reducao_plasticos = self._obter_opcao_sim_nao("Reduziu uso de plásticos descartáveis?")
        
        # ENERGIA
        print("\n💡 ENERGIA")
        energia_renovavel = self._obter_opcao_sim_nao("Usa energia renovável?")
        eficiencia_energetica = self._obter_opcao_sim_nao("Tem programa de eficiência energética?")
        
        # ÁGUA
        print("\n💧 ÁGUA")
        reuso_agua = self._obter_opcao_sim_nao("Possui sistema de reuso de água?")
        consumo_agua = self._obter_opcao_nivel("Nível de controle do consumo de água (1-5): ")
        
        # FORNECEDORES
        print("\n🏭 FORNECEDORES")
        fornecedores_locais = self._obter_opcao_nivel("Percentual de fornecedores locais (1-5): ")
        produtos_organicos = self._obter_opcao_nivel("Uso de produtos orgânicos (1-5): ")
        
        # TRANSPORTE
        print("\n🚗 TRANSPORTE")
        frota_sustentavel = self._obter_opcao_sim_nao("Possui frota sustentável?")
        logistica_eficiente = self._obter_opcao_nivel("Eficiência da logística (1-5): ")
        
        # Salvar hábito
        habitos = self.db.listar_habitos_empresa(empresa_id)
        novo_id = max([h.id for h in habitos]) + 1 if habitos else 1
        
        habito = HabitoEmpresa(
            novo_id, empresa_id, datetime.now(),
            coleta_seletiva, compostagem, reducao_plasticos,
            energia_renovavel, eficiencia_energetica,
            reuso_agua, consumo_agua,
            fornecedores_locais, produtos_organicos,
            frota_sustentavel, logistica_eficiente
        )
        
        if self.db.salvar_habito_empresa(habito):
            print("\n✅ Dados de sustentabilidade registrados com sucesso!")
            return True
        return False
    
    def _obter_opcao_sim_nao(self, pergunta):
        while True:
            resposta = input(f"{pergunta} (s/n): ").lower()
            if resposta in ['s', 'sim']:
                return 'sim'
            elif resposta in ['n', 'nao', 'não']:
                return 'nao'
            else:
                print("❌ Digite 's' para sim ou 'n' para não")
    
    def _obter_opcao_nivel(self, pergunta):
        while True:
            try:
                nivel = int(input(pergunta))
                if 1 <= nivel <= 5:
                    return str(nivel)
                else:
                    print("❌ Digite um número entre 1 e 5")
            except ValueError:
                print("❌ Digite um número válido!")