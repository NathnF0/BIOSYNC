import time
from ui.colors import Style

class NexusEngine:
    """O cérebro tático do BioSync Nexus."""
    
    @staticmethod
    def validar_nivel_acesso(nivel_usuario, nivel_exigido):
        """Verifica se o operador tem autoridade para executar a ação."""
        return int(nivel_usuario) >= int(nivel_exigido)

    @staticmethod
    def processar_busca(pessoas, termo, tipo_busca="geral"):
        """Scanner avançado de banco de dados."""
        if not termo:
            return []
            
        if tipo_busca == "acesso":
            # Filtra exatamente pelo nível de segurança
            return [p for p in pessoas if str(p.get('acesso')) == str(termo)]
        
        # Busca geral (Nome ou Profissão)
        termo = termo.lower()
        return [
            p for p in pessoas 
            if termo in p['nome'].lower() or termo in p['profissao'].lower()
        ]

    @staticmethod
    def calcular_estatisticas(pessoas):
        """Gera dados analíticos para o Dashboard."""
        if not pessoas:
            return {"total": 0, "media_idade": 0, "niveis": {}}
            
        idades = [int(p['idade']) for p in pessoas if str(p['idade']).isdigit()]
        media = sum(idades) / len(idades) if idades else 0
        
        contagem_niveis = {}
        for p in pessoas:
            lvl = p.get('acesso', '1')
            contagem_niveis[lvl] = contagem_niveis.get(lvl, 0) + 1
            
        return {
            "total": len(pessoas),
            "media_idade": round(media, 1),
            "niveis": contagem_niveis
        }

    @staticmethod
    def formatar_id(id_num):
        """Gera a estética de ID do sistema (ex: 001, 002)."""
        return str(id_num).zfill(3)