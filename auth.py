# auth.py
import json
import os

class Empresa:
    def __init__(self, id, nome_fantasia, email, setor, tamanho):
        self.id = id
        self.nome_fantasia = nome_fantasia
        self.email = email
        self.setor = setor
        self.tamanho = tamanho

class Database:
    def __init__(self):
        self.empresas = []
        self.pontuacoes = []
    
    def salvar_empresa(self, empresa):
        self.empresas.append(empresa)
    
    def buscar_empresa_por_email(self, email):
        for empresa in self.empresas:
            if empresa.email == email:
                return empresa
        return None
    
    def listar_empresas(self):
        return self.empresas.copy()
    
    def salvar_pontuacao(self, pontuacao):
        self.pontuacoes.append(pontuacao)
    
    def listar_pontuacoes_empresa(self, empresa_id):
        return [p for p in self.pontuacoes if p.empresa_id == empresa_id]

class Pontuacao:
    def __init__(self, empresa_id, score_total, nivel_sustentabilidade, detalhes, data):
        self.empresa_id = empresa_id
        self.score_total = score_total
        self.nivel_sustentabilidade = nivel_sustentabilidade
        self.detalhes = detalhes
        self.data = data

class AuthSystem:
    def __init__(self):
        self.db = Database()
        self.empresa_logada = None
    
    def cadastrar_empresa(self):
        print("\n🏢 CADASTRO DE EMPRESA")
        print("=" * 30)
        
        nome_fantasia = input("Nome fantasia: ")
        email = input("Email: ")
        setor = input("Setor de atuação: ")
        tamanho = input("Tamanho (PEQUENA/MÉDIA/GRANDE): ")
        
        # Verificar se email já existe
        if self.db.buscar_empresa_por_email(email):
            print("❌ Email já cadastrado!")
            return
        
        nova_empresa = Empresa(
            id=len(self.db.empresas) + 1,
            nome_fantasia=nome_fantasia,
            email=email,
            setor=setor,
            tamanho=tamanho.upper()
        )
        
        self.db.salvar_empresa(nova_empresa)
        print("✅ Empresa cadastrada com sucesso!")
    
    def login(self):
        print("\n🔐 LOGIN DA EMPRESA")
        print("=" * 25)
        
        email = input("Email: ")
        
        empresa = self.db.buscar_empresa_por_email(email)
        if empresa:
            self.empresa_logada = empresa
            print(f"✅ Login realizado! Bem-vindo(a), {empresa.nome_fantasia}!")
            return True
        else:
            print("❌ Empresa não encontrada!")
            return False
    
    def logout(self):
        if self.empresa_logada:
            print(f"👋 Até logo, {self.empresa_logada.nome_fantasia}!")
            self.empresa_logada = None
        else:
            print("❌ Nenhuma empresa logada!")
    
    def get_empresa_logada(self):
        return self.empresa_logada