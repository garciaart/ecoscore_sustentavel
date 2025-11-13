# scoring.py
from auth import Pontuacao
import datetime

class ScoringSystemEmpresas:
    def __init__(self):
        from auth import Database
        self.db = Database()
    
    def calcular_pontuacao(self, empresa_id):
        # Na implementação real, isso viria do habits
        from habits import HabitTrackerEmpresas
        habits = HabitTrackerEmpresas()
        resultado = habits.exibir_formulario(empresa_id)
        
        if resultado:
            pontuacao = Pontuacao(
                empresa_id=empresa_id,
                score_total=resultado["score_total"],
                nivel_sustentabilidade=resultado["nivel"],
                detalhes=resultado["detalhes"],
                data=datetime.datetime.now()
            )
            self.db.salvar_pontuacao(pontuacao)
            return resultado
        
        return None