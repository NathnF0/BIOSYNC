import time
import sys
from ui.colors import Style

def efeito_digitacao(texto, delay=0.02):
    """Anima a saída de texto como um terminal antigo."""
    for char in texto:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def barra_carregamento(itinerario, total=20):
    """Exibe uma barra de progresso estilo terminal de hackers."""
    print(f"{Style.CYAN}{itinerario}{Style.RESET}")
    for i in range(total + 1):
        percent = int((i / total) * 100)
        barra = "█" * i + "░" * (total - i)
        sys.stdout.write(f"\r {Style.CYAN}[{barra}] {percent}%{Style.RESET}")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def cabecalho_nexus():
    """Desenha o logo ASCII do BioSync Nexus."""
    print(Style.LINE)
    print(f"{Style.BOLD}{Style.PURPLE}    ____  _     ______                 {Style.RESET}")
    print(f"{Style.BOLD}{Style.PURPLE}   / __ )(_)___/ / __ \_  ______  _____ {Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN}  / __  / / __  / / / / |/_/ __ \/ ___/ {Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN} / /_/ / / /_/ / /_/ />  </ / / (__  )  {Style.RESET}")
    print(f"{Style.BOLD}{Style.CYAN}/_____/_/\__,_/\____/_/|_/_/ /_/____/   {Style.RESET}")
    print(f"{Style.YELLOW}           >> CORE INTERFACE <<{Style.RESET}")
    print(Style.LINE)

def menu_principal():
    """Exibe o menu tático principal."""
    cabecalho_nexus()
    print(f" {Style.WHITE}❱{Style.RESET} {Style.CYAN}[1]{Style.RESET} Sincronizar Novo Bio-Perfil")
    print(f" {Style.WHITE}❱{Style.RESET} {Style.CYAN}[2]{Style.RESET} Acessar Database de Rede")
    print(f" {Style.WHITE}❱{Style.RESET} {Style.CYAN}[3]{Style.RESET} Scanner de Busca Global")
    print(f" {Style.WHITE}❱{Style.RESET} {Style.CYAN}[4]{Style.RESET} Finalizar Sessão")
    print(f" {Style.WHITE}❱{Style.RESET} {Style.CYAN}[5]{Style.RESET} {Style.BLINK}{Style.RED}ÁREA ADMINISTRATIVA (ADM){Style.RESET}")
    print(Style.DIVIDER)

def menu_admin_estilizado():
    """Interface exclusiva para o modo administrativo."""
    print(f"{Style.RED}{Style.LINE}")
    print(f"{Style.RED}{Style.BOLD}          Ω TERMINAL DO ADMINISTRADOR Ω          {Style.RESET}")
    print(f"{Style.RED}{Style.LINE}{Style.RESET}")
    opcoes = [
        ("1", "EXPURGAR", "Eliminar registro da existência", Style.RED),
        ("2", "MODIFICAR", "Reestruturar DNA de dados", Style.CYAN),
        ("3", "MANIFESTO", "Gerar relatório físico (.txt)", Style.GREEN),
        ("4", "AUDITORIA", "Visualizar logs de segurança", Style.YELLOW),
        ("5", "RETORNAR", "Sair do Nexus Root", Style.WHITE)
    ]
    for cmd, titulo, desc, cor in opcoes:
        print(f" {Style.WHITE}[{cmd}]{Style.RESET} {cor}{titulo.ljust(10)}{Style.RESET} | {desc}")
    print(f"{Style.RED}{Style.DIVIDER}{Style.RESET}")