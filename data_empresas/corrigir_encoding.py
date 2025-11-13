import pandas as pd
import os

def corrigir_arquivos_csv():
    """Corrige o encoding de todos os arquivos CSV existentes"""
    
    arquivos = [
        'data_empresas/empresas.csv',
        'data_empresas/habitos_empresas.csv', 
        'data_empresas/pontuacoes_empresas.csv'
    ]
    
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            try:
                print(f"Corrigindo {arquivo}...")
                
                # Tentar ler com diferentes encodings
                try:
                    df = pd.read_csv(arquivo, encoding='utf-8')
                except:
                    df = pd.read_csv(arquivo, encoding='latin-1')
                
                # Salvar com UTF-8
                df.to_csv(arquivo, index=False, encoding='utf-8')
                print(f"✅ {arquivo} corrigido!")
                
            except Exception as e:
                print(f"❌ Erro em {arquivo}: {e}")

if __name__ == "__main__":
    corrigir_arquivos_csv()
    print("🎉 Correção de encoding concluída!")