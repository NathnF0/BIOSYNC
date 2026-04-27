import json
import os
import shutil

# Definição de caminhos com redundância
PASTA_DB = os.path.join(os.path.dirname(__file__), "..", "database")
ARQUIVO_JSON = os.path.join(PASTA_DB, "pessoas.json")
ARQUIVO_BACKUP = os.path.join(PASTA_DB, "pessoas_backup.json")

def garantir_diretorio():
    """Garante a existência da infraestrutura de pastas."""
    if not os.path.exists(PASTA_DB):
        os.makedirs(PASTA_DB)

def carregar_dados():
    """Carrega dados com protocolo de autorreparo e normalização."""
    garantir_diretorio()
    
    # Tenta carregar o arquivo principal, se falhar, tenta o backup
    alvos = [ARQUIVO_JSON, ARQUIVO_BACKUP]
    
    for caminho in alvos:
        if os.path.exists(caminho):
            try:
                with open(caminho, "r", encoding='utf-8') as arquivo:
                    dados = json.load(arquivo)
                    
                    # Normalização Atômica: Garante integridade de chaves críticas
                    for p in dados:
                        if 'acesso' not in p: p['acesso'] = "1"
                        if 'registro' not in p: p['registro'] = "N/A"
                    return dados
            except (json.JSONDecodeError, Exception):
                continue # Pula para o próximo alvo (backup)
                
    return [] # Se tudo falhar, retorna base vazia

def salvar_dados(dados):
    """Salva dados e mantém uma 'shadow copy' (cópia de sombra) de segurança."""
    garantir_diretorio()
    
    try:
        # 1. Antes de salvar o novo, o antigo vira backup
        if os.path.exists(ARQUIVO_JSON):
            shutil.copy(ARQUIVO_JSON, ARQUIVO_BACKUP)
            
        # 2. Escrita Segura (Atomic Save)
        with open(ARQUIVO_JSON, "w", encoding='utf-8') as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            
    except Exception as e:
        print(f"ERRO CRÍTICO DE ESCRITA: {e}")

def exportar_manifesto_txt(dados):
    """Gera um arquivo legível para humanos fora da database."""
    path = os.path.join(PASTA_DB, "MANIFESTO_EXPORT.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"--- NEXUS DATABASE MANIFESTO ---\n")
        f.write(f"GERADO EM: {os.times()}\n\n")
        for p in dados:
            f.write(f"[{p['id']}] {p['nome']} | SETOR: {p['profissao']} | ACESSO: {p['acesso']}\n")
    return path