import curses
import time

class Character:
    def __init__(self, name, health, points):
        self.name = name
        self.health = health
        self.points = points

self = Character("name", 5, 100)

def display_text(stdscr, text, start_col, color_pair_id):
    global line_counter
    stdscr.refresh()
    time.sleep(0.2)  # Wait for a second before displaying each letter
    for i in range(len(text)):
        stdscr.addch(line_counter, start_col + i, text[i], curses.color_pair(color_pair_id))
        stdscr.refresh()
        time.sleep(0.05)
    line_counter += 1

line_counter = 0  # Initialize line counter

def aggressive(stdscr,self):
    display_text(stdscr, "The guardians say:\n", 0, 3)
    display_text(stdscr, "“We have been waiting for you after we received word of your father's death. However, we can see that you are not worthy of his treasure. You cannot proceed.”\n", 0, 5)
    display_text(stdscr, "You have lost a life.\n", 0, 1)
    self.health -= 1

def polite(stdscr):
    display_text(stdscr, "The guardians say:\n", 0, 3)
    display_text(stdscr, "”We have been waiting for you after we received word of your father's death. To acquire what your father left in our possession, you must first face the challenges that await behind this door and hand us the circle of life.”\n", 0, 5)

def approach_guardians(stdscr):
    display_text(stdscr, "How do you want your demeanor to be?\n", 0, 3)
    print("1) Aggressive    2) Polite")
    choice2 = int(input("> "))
    if choice2 == 1:
        aggressive(stdscr)
    else:
        polite(stdscr)

def not_approach_guardians(stdscr, tools):
    display_text(stdscr, "You sneaked past the temple's guards, making sure they didn't see you. As you explored around, you found an old door on the temple's wall. You tried to open it, but it was locked tight.\n", 0, 3)
    if "mystery item" in tools:
        display_text(stdscr, "As you took hold of the mysterious item, you realized it was none other than the key to the door you faced. With the key in hand, you effortlessly unlocked the door and entered the temple without encountering any further obstacles.\n", 0, 3)
    else:
        display_text(stdscr, "As you failed to retrieve the mystery item, you now realize its significance—it was the key to this very door. With a sinking feeling, you understand that without it, the door remains firmly locked. Accepting your fate, you prepare to confront the guardians standing before you, knowing that they are now your only path forward.\n", 0, 3)
        approach_guardians(stdscr)

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    stdscr.clear()

    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    tools = ["gun", "knife", "mystery item", "short bow", "torch"]

    display_text(stdscr, "As you walk deeper along the path, you encounter a temple guarded by two formidable sentinels, their feline features hinting at an otherworldly presence. These guardians, armored and armed, possess sleek fur, piercing eyes, and an aura of silent vigilance, their weapons poised for protection.\n", 0, 3)
    display_text(stdscr, "What do you want to do?\n", 0, 3)
    print("1) Approach the guardians    2) Look for another way in")
    choice1 = int(input("> "))

    if choice1 == 1:
        approach_guardians(stdscr, choice1)
    elif choice1 == 2:
        not_approach_guardians(stdscr, tools)

wrapper(main)