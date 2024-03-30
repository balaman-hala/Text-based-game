import os
from colorama import Fore, Back, Style, init
os.system("")


class HealthBar:
    symbol_remaining: str = "▮"
    symbol_lost = "_"
    barrier: str = "|"
    colors: dict = {"red": Fore.RED,
                    "green": Fore.GREEN,
                    "blue": Fore.BLUE,
                    "white": Fore.WHITE,
                    "black": Fore.BLACK,
                    "yellow": Fore.YELLOW,
                    "purple": Fore.MAGENTA,
                    "orange": Fore.LIGHTRED_EX,
                    "pink": Fore.LIGHTMAGENTA_EX,
                    "brown": Fore.LIGHTRED_EX,
                    "gray": Fore.LIGHTBLACK_EX,
                    "cyan": Fore.CYAN,
                    "magenta": Fore.MAGENTA,
                    "turquoise": Fore.CYAN,
                    "gold": Fore.YELLOW,
                    "default": Fore.RESET}

    def __init__(self, entity, length, current_value, is_colored, color) -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        self.is_colored = is_colored
        self.color = color
        