import os
import time
import shutil 
from datetime import datetime
from ui.colors import Style
from ui.menus import menu_principal, efeito_digitacao, cabecalho_nexus
from core.storage import carregar_dados, salvar_dados
from core.engine import NexusEngine as Engine

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def registrar_log(acao):
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with open("nexus_audit.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] - GALAXY_CMD: {acao}\n")

def criar_backup():
    """Gera uma cópia de segurança do banco de dados antes de operações críticas."""
    try:
        if os.path.exists("data/pessoas.json"):
            shutil.copy("data/pessoas.json", "data/pessoas_backup.json")
            registrar_log("BACKUP PREVENTIVO GERADO")
    except Exception as e:
        registrar_log(f"FALHA NO BACKUP: {e}")

def obter_proximo_id(pessoas):
    """Calcula o próximo ID real, evitando buracos e duplicatas."""
    if not pessoas:
        return 1
    return max(p['id'] for p in pessoas) + 1

def animar_processamento(mensagem):
    print(f"{Style.YELLOW}{mensagem}", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print(f"{Style.RESET}")

def exibir_dashboard(pessoas):
    total = len(pessoas)
    stats = Engine.calcular_estatisticas(pessoas)
    data_hora = datetime.now().strftime("%H:%M:%S")
    print(f"{Style.CYAN} STATUS: {Style.GREEN}ATIVO{Style.CYAN} | REGISTROS: {Style.BOLD}{total}| MÉDIA IDADE: {Style.BOLD}{stats['media_idade']}{Style.RESET}{Style.RESET} | HORA: {Style.BOLD}{data_hora}{Style.RESET}")
    print(Style.LINE)

def rodar_sistema():
    global Engine
    pessoas = carregar_dados()
    limpar_tela()
    efeito_digitacao(f"{Style.CYAN}[SISTEMA]: Nexus Core Online. Bem-vindo.", 0.03)
    registrar_log("SISTEMA INICIALIZADO")
    
    while True:
        limpar_tela()
        menu_principal()
        exibir_dashboard(pessoas)
        
        opcao = input(f"{Style.BOLD}{Style.CYAN}Nexus@Comando >> {Style.RESET}")

        if opcao == "1":
            limpar_tela()
            cabecalho_nexus()
            print(f"{Style.PURPLE}{Style.BOLD}>>> PROTOCOLO DE CAPTURA BIOMÉTRICA <<<{Style.RESET}\n")
            
            nome = input(f"{Style.CYAN}NOME COMPLETO: {Style.RESET}").strip()
            
            # Validação de Idade Robusta
            while True:
                idade = input(f"{Style.CYAN}IDADE CRONOLÓGICA: {Style.RESET}")
                if idade.isdigit() and 0 < int(idade) < 150:
                    break
                print(f"{Style.RED}⚠ ENTRADA INVÁLIDA. INSIRA UMA IDADE REAL.{Style.RESET}")

            prof = input(f"{Style.CYAN}SETOR/ATUAÇÃO: {Style.RESET}").strip()
            print(f"{Style.YELLOW}Níveis: 1(Civil), 2(Operador), 3(Tático), 4(Elite), 5(Mestre){Style.RESET}")
            level = input(f"{Style.CYAN}NÍVEL DE ACESSO (1-5): {Style.RESET}") or "1"
            
            animar_processamento("\nSINCRO-DADOS EM CURSO")
            
            pessoas.append({
                "id": obter_proximo_id(pessoas),
                "nome": nome,
                "idade": idade,
                "profissao": prof,
                "acesso": level,
                "registro": datetime.now().strftime("%d/%m/%Y | %H:%M")
            })
            salvar_dados(pessoas)
            registrar_log(f"NOVO PERFIL: {nome}")
            print(f"{Style.GREEN}✔ BIO-PERFIL ARMAZENADO.{Style.RESET}")
            time.sleep(1.5)

        elif opcao == "2":
            limpar_tela()
            cabecalho_nexus()
            print(f"{Style.BOLD}{Style.CYAN}ID  | NOME {' ' * 13} | ACESSO | SETOR{Style.RESET}")
            print(Style.DIVIDER)
            
            for p in pessoas:
                status, cor = Style.get_level_color(p.get('acesso', '1'))
                n = p['nome'][:18].ljust(18)
                print(f"{str(p['id']).zfill(2)}  | {n} | {cor}{status.ljust(6)}{Style.RESET} | {p['profissao']}")
            
            print(Style.DIVIDER)
            input(f"\n{Style.YELLOW}[ENTER] VOLTAR AO TERMINAL...{Style.RESET}")

        elif opcao == "3":
            limpar_tela()
            cabecalho_nexus()
            
            # Pergunta direta e elegante
            print(f"{Style.CYAN}MODO SCANNER: [1] Nome/Setor | [2] Nível de Acesso{Style.RESET}")
            sub_op = input(f"{Style.BOLD}Nexus@Scanner >> {Style.RESET}")
            
            if sub_op == "2":
                # Mostramos os níveis em uma linha discreta
                termo = input(f"\n{Style.PURPLE}FILTRAR NÍVEL (1-Civil a 5-Mestre): {Style.RESET}")
                tipo = "acesso"
            else:
                # Pergunta limpa, sem blocos de texto de exemplo
                termo = input(f"\n{Style.PURPLE}SCANNER (Nome ou Setor): {Style.RESET}")
                tipo = "geral"
            
            # Aqui o erro vai sumir porque o Engine foi importado no topo do arquivo
            res = Engine.processar_busca(pessoas, termo, tipo)
            
            animar_processamento("RASTREANDO")
            
            if res:
                print(f"\n{Style.GREEN}✔ {len(res)} ASSINATURA(S) ENCONTRADA(S):{Style.RESET}")
                print(Style.DIVIDER)
                for r in res:
                    st, cor = Style.get_level_color(r.get('acesso', '1'))
                    print(f" {Style.CYAN}»{Style.RESET} {r['nome'].upper()} | {cor}{st}{Style.RESET}")
            else:
                print(f"\n{Style.RED}⚠ NENHUM RESULTADO PARA: '{termo}'{Style.RESET}")
            
            input(f"\n{Style.YELLOW}[ENTER] VOLTAR...{Style.RESET}")

        elif opcao == "4":
            registrar_log("SESSÃO ENCERRADA")
            break

        elif opcao == "5":
            limpar_tela()
            print(f"{Style.RED}{Style.BLINK}{'!'*20} ALERTA DE ACESSO CRÍTICO {'!'*20}{Style.RESET}")
            
            # Autenticação
            if input(f"{Style.BOLD}DIGITE A CHAVE MESTRA: {Style.RESET}") == "admin123":
                from ui.menus import menu_admin_estilizado  # Importando o novo menu tático
                
                criar_backup() # Proteção redundante ativa
                registrar_log("AUTENTICAÇÃO DE NÍVEL MESTRE CONCEDIDA")
                
                while True:
                    limpar_tela()
                    # Substituímos os prints manuais pela função de elite
                    menu_admin_estilizado()

                    op_adm = input(f"\n{Style.RED}ADM_CMD >> {Style.RESET}")

                    if op_adm == "1":
                        limpar_tela()
                        print(f"{Style.RED}--- LISTA DE ALVOS PARA EXPURGO ---{Style.RESET}\n")
                        for p in pessoas:
                            # Melhoria: ID formatado pela Engine (ex: 01, 02...)
                            id_viz = Engine.formatar_id(p['id'])
                            print(f" {Style.RED}»{Style.RESET} ID: {Style.YELLOW}{id_viz}{Style.RESET} | {p['nome']}")
                        
                        id_del = input(f"\n{Style.BOLD}ID para eliminar (ou Enter para cancelar): {Style.RESET}")
                        if id_del:
                            # Tratamos o ID para remover zeros à esquerda se o usuário digitar "01"
                            id_alvo = id_del.lstrip('0')
                            orig = len(pessoas)
                            pessoas = [p for p in pessoas if str(p['id']) != id_alvo]
                            
                            if len(pessoas) < orig:
                                salvar_dados(pessoas)
                                registrar_log(f"EXPURGO EXECUTADO: ID {id_alvo}")
                                animar_processamento("FRAGMENTANDO DADOS")
                                print(f"{Style.GREEN}✔ Registro apagado com sucesso.{Style.RESET}")
                            else: 
                                print(f"{Style.RED}⚠ ID não encontrado na database.{Style.RESET}")
                        time.sleep(1.5)

                    elif op_adm == "2":
                        limpar_tela()
                        print(f"{Style.CYAN}--- REESTRUTURAÇÃO DE PERFIL ---{Style.RESET}\n")
                        for p in pessoas: 
                            print(f" ID: {Style.YELLOW}{Engine.formatar_id(p['id'])}{Style.RESET} | {p['nome']}")
                        
                        id_edit = input(f"\n{Style.BOLD}ID para modificar: {Style.RESET}").lstrip('0')
                        alvo = next((p for p in pessoas if str(p['id']) == id_edit), None)
                        
                        if alvo:
                            print(f"\n{Style.PURPLE}Deixe em branco para manter o valor original.{Style.RESET}")
                            alvo['nome'] = input(f" {Style.CYAN}Nome{Style.RESET} [{alvo['nome']}]: ") or alvo['nome']
                            alvo['profissao'] = input(f" {Style.CYAN}Setor{Style.RESET} [{alvo['profissao']}]: ") or alvo['profissao']
                            alvo['acesso'] = input(f" {Style.CYAN}Nível{Style.RESET} [{alvo.get('acesso', '1')}]: ") or alvo.get('acesso', '1')
                            
                            salvar_dados(pessoas)
                            registrar_log(f"REESTRUTURAÇÃO: {alvo['nome']}")
                            animar_processamento("REESCREVENDO CÓDIGO FONTE")
                            print(f"{Style.GREEN}✔ Perfil atualizado.{Style.RESET}")
                        else: 
                            print(f"{Style.RED}⚠ Perfil não localizado.{Style.RESET}")
                        time.sleep(1.5)

                    elif op_adm == "3":
                        from core.storage import exportar_manifesto_txt
                        # Usando a nova função do storage para gerar o arquivo
                        caminho = exportar_manifesto_txt(pessoas)
                        animar_processamento("COMPILANDO MANIFESTO")
                        print(f"{Style.GREEN}✔ Relatório gerado em: {caminho}{Style.RESET}")
                        time.sleep(1.5)

                    elif op_adm == "4":
                        limpar_tela()
                        print(f"{Style.YELLOW}--- TRILHA DE AUDITORIA (LOGS) ---{Style.RESET}\n")
                        if os.path.exists("nexus_audit.log"):
                            with open("nexus_audit.log", "r", encoding="utf-8") as f:
                                logs = f.readlines()
                                # Aumentei para os últimos 15 logs para melhor visão
                                for log in logs[-15:]:
                                    print(f" {Style.WHITE}•{Style.RESET} {log.strip()}")
                        else: 
                            print("Nenhum log encontrado.")
                        input(f"\n{Style.YELLOW}Pressione Enter para fechar logs...{Style.RESET}")

                    elif op_adm == "5":
                        break
            else:
                registrar_log("CREDENCIAIS INVÁLIDAS")
                print(f"{Style.RED}{Style.BOLD}ACESSO NEGADO.{Style.RESET}")
                time.sleep(2)

if __name__ == "__main__":
    rodar_sistema()