import pandas as pd
import os
from datetime import datetime

class Database:
    def __init__(self):
        self.pasta = "data_empresas"
        os.makedirs(self.pasta, exist_ok=True)
        
        self.empresas_file = f"{self.pasta}/empresas.csv"
        self.pratos_file = f"{self.pasta}/pratos.csv" 
        self.avaliacoes_file = f"{self.pasta}/avaliacoes.csv"
        
        self._criar_arquivos()
    
    def _criar_arquivos(self):
        # SEMPRE usar encoding='utf-8' e garantir que não sobrescreva arquivos existentes
        if not os.path.exists(self.empresas_file):
            df = pd.DataFrame(columns=['id','cnpj','razao_social','nome_fantasia','email','senha','telefone','endereco','segmento','data_cadastro'])
            df.to_csv(self.empresas_file, index=False, encoding='utf-8')
    
    # EMPRESAS - CORRIGIDO
    def salvar_empresa(self, empresa):
        try:
            # Ler arquivo existente com encoding correto
            if os.path.exists(self.empresas_file):
                df = pd.read_csv(self.empresas_file, encoding='utf-8')
            else:
                df = pd.DataFrame(columns=['id','cnpj','razao_social','nome_fantasia','email','senha','telefone','endereco','segmento','data_cadastro'])
            
            novo = pd.DataFrame([{
                'id': empresa.id,
                'cnpj': empresa.cnpj,
                'razao_social': empresa.razao_social,
                'nome_fantasia': empresa.nome_fantasia,
                'email': empresa.email,
                'senha': empresa.senha,
                'telefone': empresa.telefone,
                'endereco': empresa.endereco,
                'segmento': empresa.segmento,
                'data_cadastro': empresa.data_cadastro.isoformat()
            }])
            
            df = pd.concat([df, novo], ignore_index=True)
            # SALVAR SEMPRE COM UTF-8
            df.to_csv(self.empresas_file, index=False, encoding='utf-8')
            return True
            
        except Exception as e:
            print(f"Erro ao salvar empresa: {e}")
            return False
    
    def listar_empresas(self):
        try:
            # LER SEMPRE COM UTF-8
            df = pd.read_csv(self.empresas_file, encoding='utf-8')
            from models import Empresa
            empresas = []
            for _, row in df.iterrows():
                empresas.append(Empresa(
                    row['id'], row['cnpj'], row['razao_social'], row['nome_fantasia'],
                    row['email'], row['senha'], row['telefone'], row['endereco'],
                    row['segmento'], datetime.fromisoformat(row['data_cadastro'])
                ))
            return empresas
        except Exception as e:
            print(f"Erro ao listar empresas: {e}")
            return []