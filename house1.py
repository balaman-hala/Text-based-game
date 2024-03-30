import curses
from curses import wrapper
#from character import Character
import time

key='a'
points=100
inventory=["gun","knife","sword","lighter","mystery item"]
#player = Character( name = "Idk", health = 100, damage = 5, points = 100 )
line_counter=0
run = True

def search(window, tool):
    for i in  range(len(inventory)):
        if inventory[i]== tool:
            return 1
        return -1
            
def add_item(window, line, item):
    global line_counter
    window.addstr(line,  20, "You found a %s!"%item)
    line_counter+=1
    window.refresh()
    
    
def display_text(stdscr, text,start_col,t):
    global line_counter
    stdscr.refresh()
    time.sleep(0.2)  # Wait for a second before displaying each letter
    for i in range(len(text)):
        stdscr.addch(line_counter, start_col + i, text[i],curses.color_pair(t))
        stdscr.refresh()
        time.sleep(0.05)
    line_counter += 1

def light(window):
    key = window.getkey()
    if key == '1':
        display_text(window,"The darkness seems to swallow you whole as you realize you forgot to pick up the lighter. Your hands fumble in the darkness, searching for something, anything, to guide you. Unfortunately, without a light source, you're unable to find your way forward. It looks like you'll need to rethink your strategy.\n",0,3)
        if search(window,"lighter") == -1:
            display_text(window,"Since you didn't pick up the lighter, you'll need to find another way to light your path. Maybe you can use your points to acquire one?\n",0,3)
            display_text(window, "1. Use 5 points to get the lighter               2. Don't use it\n")
            key1 = window.getkey()
            if key1 == '1':
                player.points  -= 5
            elif key1 == '2':
                display_text(window,"One of the monsters has caught you off guard, sealing your fate. Game over.",0,1)
                run = False
            else :
                display_text(window, "Invalid input! Try again.\n")
    elif key == '2':
        display_text(window,"As you flick the lighter, a small flame dances in the darkness, casting flickering shadows around you. A sense of caution washes over you as you remember that the lighter has limited fuel.\nYou decide to use it sparingly, illuminating your path only when necessary. Every second counts, and you know you must conserve its precious fuel to navigate through the darkness safely. You need to find a more reliable light source, like a torch, search for one as soon as possible",0,3)
        hallway(window)
            
def hallway(window):
        display_text(window,"You are in the hallway. Which way do you want to go?\n")
        display_text(window,"1.Left into the living room.               2.Right into the kitchen.\n")
        key1 = window.getkey()
        if key1 == '1':
            display_text(window,"As you enter the room, you realize it's just a plain, empty space with nothing of interest. Perhaps another area of the house holds the key to your adventure.")
            hallway(window)
        elif key1 == '2':
            display_text(window,"You're in the kitchen. Where would you like to look?\n")
            display_text(window,"1. Cabinet               2. Drawer\n",0,3)
        
        
def house_entery(window):
    display_text(window,"How do you want to enter the house?\n",0,3)
    display_text(window,"1. Through the door. \n2. Through the windows.\n",0,3)
    key = window.getkey()
    if key == '1':
        if search (window,'mystery item') != -1 :
            display_text(window,"The mystery item was a key. Congrats You were able to unlock the door !\n",0,3)
            display_text(window,"The house is dark use one of your tools to help you.\n",0,3)
            display_text(window,"Which tool do you want to use?\n",0,3)
            display_text(window,"1. Anything else\n2. Lighter\n",0,3)
            display_text(window,"",0,3)
        else:
            display_text(window,"The mystery item was a key. Since you didn’t choose it, you cannot unlock the door. You'll need to find another way in.\n",0,3)
            
    elif key == '2':
        display_text(window,"You managed to force the window open.\n",0,3)
        display_text(window,"The house is dark use one of your tools to help you.\n",0,3)
        display_text(window,"Which tool do you want to use?\n",0,3)
        display_text(window,"1. Anything else\n2. Lighter\n",0,3)

def main(stdscr):
    
    stdscr.clear()
    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    RED_BLACK = curses.color_pair(1)
    GREEN_BLACK = curses.color_pair(2)
    while run:
        display_text(stdscr,"As you walk deep in this path you encounter a house with an unwelcoming exterior.",0,3)
        house_entery(stdscr)
        stdscr.refresh()
        stdscr.getch()
    
    
wrapper(main)