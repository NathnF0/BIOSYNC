class Style:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    
    LINE = f"{CYAN}=" * 55 + f"{RESET}"
    DIVIDER = f"{CYAN}-" * 55 + f"{RESET}"

    @staticmethod
    def get_level_color(level):
        levels = {
            "1": ('VERDE', '\033[92m'),
            "2": ('AZUL', '\033[94m'),
            "3": ('AMARELO', '\033[93m'),
            "4": ('LARANJA', '\033[33m'),
            "5": ('CRÍTICO', '\033[91m')
        }
        return levels.get(str(level), ('DESCONHECIDO', '\033[97m')) 