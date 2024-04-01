import os
import curses
from colorama import Fore, Back, Style, init

os.system("")
init()  # Initialize colorama

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

    def __init__(self, entity, length: int = 20, is_colored: bool = True, color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health
        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.hp

    def draw(self, stdscr) -> None:
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        stdscr.addstr(f"{self.entity.name}'s Health: {self.entity.health}/{self.entity.health_max}\n")
        stdscr.addstr(f"{self.barrier}"
                      f"{self.color if self.is_colored else ''}"
                      f"{self.symbol_remaining * remaining_bars}"
                      f"{self.symbol_lost * lost_bars}"
                      f"{self.colors['default'] if self.is_colored else ''}"
                      f"{self.barrier}\n")
