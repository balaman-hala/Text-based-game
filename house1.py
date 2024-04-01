import curses
import character
from curses import wrapper
from character import Hero
import time

key='a'
points=100
inventory=["gun","knife","sword","lighter","mystery item"]
player = Hero( name = "Idk", health = 100, points = 100 )
line_counter=0
run = True
keyy = '0'

def hb(stdscr):
    player.health_bar.draw(stdscr)
    


def clr(window):
    global line_counter
    global keyy
    window.addstr(line_counter+2,0,"PRESS ANY KEY TO CONTINUE!",curses.A_BOLD)
    keyy = window.getkey()
    window.clear()
    time.sleep(2)
    line_counter = 0
    window.refresh()

def search(window, tool):
    for i in  range(len(inventory)):
        if inventory[i]== tool:
            return 1
        
        
    return -1
            
def add_item(window, item):
    display_text(window,"You found a %s !\n"%item,0,2)
    display_text(window,"Do you want to pick it up? y/n \n",0,3)
    key = window.getkey()
    if key == 'y' or  key == 'Y':
        global inventory
        inventory.append(item)
        display_text(window,"You picked up the %s.\n"%item,0,2)
    elif key == 'n' or  key == 'N':
        display_text(window,"You left the %s behind.\n"%item,0,1)
    else :
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
        add_item(window,item)
    window.refresh()
    

def display_text(stdscr, text,start_col,t):
    global line_counter
    stdscr.refresh()
    time.sleep(0.2)  # Wait for a second before displaying each letter
    for i in range(len(text)):
        stdscr.addch(line_counter, start_col + i, text[i],curses.color_pair(t) | curses.A_ITALIC)
        stdscr.refresh()
        time.sleep(0.05)
    line_counter += 2
    
    
def savingLightsfuel(window):
    display_text(window,"As you flick the lighter, a small flame dances in the darkness, casting flickering shadows around you.\n",0,3)
    display_text(window,"But remember The lighter has limited fuel. Please use it sparingly, illuminating your path only when necessary.\n",0,3)
    display_text(window,"Every second counts, and you know you must conserve its precious fuel to navigate through the darkness safely.\n",0,3)
    display_text(window,"I think you need to find a more reliable light source, like a torch, search for one as soon as possible\n",0,3)
    clr(window)
    hallway(window)
    
    
def light(window):
    key1 = '0'
    display_text(window,"The house is dark use one of your tools to help you.\n",0,3)
    display_text(window,"Which tool do you want to use?\n",0,3)
    display_text(window,"1. Anything else.",0,4)
    display_text(window,"2. Lighter\n",0,4)
    key = window.getkey()
    if key == '1':
        display_text(window,"The darkness seems to swallow you whole as you realize you didn't choose to use the lighter.\n",0,3)
        display_text(window,"Your hands fumble in the darkness, searching for something, anything, to guide you.\n",0,3)
        display_text(window,"Unfortunately, without a light source, you're unable to find your way forward.\n",0,3)
        display_text(window,"It looks like you'll need to rethink your strategy.\n",0,3)
        if search(window,"lighter") == -1:
            while key1 != '1'  and key1 != '2':
                display_text(window,"We've checked your inventory, but unfortunately, the lighter isn't there. You'll need to find another way to light your path.\n",0,3)
                display_text(window,"Maybe you can use your points to acquire one?\n",0,3)
                display_text(window,"1. Use 5 points to get the lighter\n",0,4)
                display_text(window,"2. Don't use it\n",0,4)
                key1 = window.getkey()
                if key1 == '1':
                    player.points  -= 5
                    inventory.append('lighter')
                    display_text(window,"You got the lighter!\n",0,7)
                    clr(window)
                    savingLightsfuel(window)
                elif key1 == '2':
                    display_text(window,"One of the monsters has caught you off guard, sealing your fate. Game over.",0,1)
                    run = False
                else :
                    display_text(window, "Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
                    clr(window)
        else:
            display_text(window,"You were well-prepared, as the trusty lighter was already in your inventory.\n",0,2)
            savingLightsfuel(window)
    elif key == '2':
        savingLightsfuel(window)
         
def drawer(window):
    key1 = '0'
    display_text(window,"Where else to look?\n",0,3)
    display_text(window,"1. Cabinet\n",0,4)
    display_text(window,"2. Frigde\n",0,4)
    key = window.getkey()
    if key == '1':
        display_text(window,"You found the torch! But unfortunately, it has no batteries.\n",0,3)
        if search(window,'Batteries') == 1:
            display_text(window, "But don't worry, you've already picked up the batteries.\n",0,3)
            clr(window)
        else:
            while key1 !=  'y' and key1 != 'Y':
                display_text(window,"Regrettably, you left the batteries behind. Would you like to redeem points to retrieve them? y/n \n",0,3)
                key1 = window.getkey()
                if key1 == 'y' or key1 == 'Y':
                    player.points -= 5
                    add_item(window,'Batteries')
                    display_text(window,"Congratulations! You have gotten a set of Batteries.",0,8)
                    clr(window)
                elif  key1 == 'n' or key1 == 'N':
                    display_text(window,"You'll need the torch later on. It's essential to pick up the batteries now.\n",0,1)
                    clr(window)
                else:
                    display_text(window, "Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
                    clr(window)
    elif key == '2':
        display_text(window,"Oops, it looks like there's nothing here.\n",0,3)
        clr(window)
        drawer(window)
    else:
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n")
        clr(window)
        drawer(window)        
   
def cabinet(window):
    display_text(window,"Where do you think you could find batteries?\n",0,3)
    display_text(window,"1. Fridge\n",0,4)
    display_text(window,"2. Drawer\n",0,4)
    key1 = window.getkey()
    if key1 == '1':
        display_text(window,"Oops, it looks like there's nothing here.\n",0,1)
        clr(window)
        cabinet(window)
    elif key1 == '2':
        add_item(window, 'Bug Spray')
        add_item(window, 'Batteries')
    else:
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.",0,1)
        clr(window)
        cabinet(window) 
    
    
def hallway(window):
        key2 ='0'
        display_text(window,"You are in the hallway. Which way do you want to go?\n",0,3)
        display_text(window,"1.Left into the living room\n",0,4)
        display_text(window,"2.Right into the kitchen\n",0,4)
        key1 = window.getkey()
        if key1 == '1':
            display_text(window,"As you enter the room, you realize it's just a plain, empty space with nothing of interest.\n",0,3)
            display_text(window,"Perhaps another area of the house holds the key to your adventure.So you decide to go back to the hallway.\n",0,3)
            clr(window)
            hallway(window)
        elif key1 == '2':
            while key2 != '1' and key2 != '2':
                clr(window)
                display_text(window,"You're in the kitchen. Where would you like to look?\n",0,3)
                display_text(window,"1. Cabinet",0,4)
                display_text(window,"2. Drawer",0,4)
                key2 = window.getkey()
                if key2 == '1':
                    display_text(window,"You found the torch, but unfortunately, it has no batteries.\n",0,1)
                    display_text(window,"It seems you'll need to search for batteries elsewhere to make it useful.\n",0,3)
                    clr(window)
                    cabinet(window)
                elif key2 == '2':
                    add_item(window,"Batteries")
                    add_item(window,"Bug Spray")
                    clr(window)
                    drawer(window)
                else:
                    display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
                    clr(window)
        else:
            display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)  
            clr(window)
            hallway(window)
        
def house_entery(window):
    display_text(window,"How do you want to enter the house?\n",0,3)
    display_text(window,"1. Through the door.\n",0,4)
    display_text(window,"2. Through the windows.\n",0,4)
    key = window.getkey()
    if key == '1':
        if search (window,"mystery item") == 1 :
            display_text(window,"The mystery item was a key. Congrats You were able to unlock the door !\n",0,7)
            clr(window)
            light(window)
        else:
            display_text(window,"The mystery item was a key. Since you didn’t choose it, you cannot unlock the door. You'll need to find another way in.\n",0,1)
            player.points -= 5
            clr(window)
            house_entery(window)
            
    elif key == '2':
        display_text(window,"You managed to force the window open.\n",0,7)
        clr(window)
        light(window)
    else:
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
        clr(window)
        house_entery(window)
  
def creating_bigger_flame(window):
    display_text(window,"You have to create a bigger flame!",0,8)
    display_text(window,"1. Use bug spray\n",0,3)
    display_text(window,"2. Ask Jeremy for disinfectant spray.\n",0,3)
    key = window.getkey()
    if key == '1':
        display_text(window,"The bug spray ran out, leaving you defenseless against the relentless swarm. It simply wasn't enough to fend them off.\n",0,1)
        player.health -= 10
        clr(window)
        creating_bigger_flame(window)
    elif key == '2':
        display_text(window,"With sheer determination, you battled through the swarm, emerging victorious and claiming the key as your prize.\n",0,7)
    else:
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
  
        
def spiders(window):
    display_text(window,"What tool do you want to use?\n")
    display_text(window,"1. Lighter\n",0,8)
    display_text(window,"2. Bug Spray\n",0,8)
    display_text(window,"3. Anything else\n",0,8)
    key = window.key()
    if key == '2':
        display_text(window,"The horde of spiders was overwhelming, and unfortunately, the bug spray ran out.\n",0,1)
        clr(window)
        spiders(window)
    elif key == '3':
        display_text(window,"That's not helpful. The spiders have swarmed around you and started sucking your blood.",0,1)
        player.health -= 10
        clr(window)
        spiders()
    elif key == '1':
        display_text(window,"The spiders slightly back away.\n",0,8)
        creating_bigger_flame(window)
    else:
       display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1) 
       clr(window)
       spiders(window)

  
def door(window):
    display_text(window,"Which door to choose?\n",0,3)
    display_text(window,"1. Left\n",0,3)
    display_text(window,"2. Right\n",0,3)
    key = window.getkey()
    if key == '1':
        display_text(window,"This door is locked. To proceed, you'll need to find a key. You should return to the other door for now.\n",0,3)
        door(window)
    elif key == '2':
        display_text(window,"You find a key hidden behind a swarm of baby blood-sucking spiders.\n",0,1)
        display_text(window,"You must find a way to get rid of them! \n",0,1)
        spiders(window)
    else:
        display_text(window,"Oops! That key doesn't seem to have an effect here. Please try a different key.\n",0,1)
        clr(window)
        door(window)


def main(stdscr):
    
    stdscr.clear()
    
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    while run:
        display_text(stdscr,"As you walk deep in this path you encounter a house with an unwelcoming exterior.\n\n",0,3)
        house_entery(stdscr)
        clr(stdscr)
        display_text(stdscr,"As you explore the house, you come across an elderly man in one of the rooms.\n",0,3)
        display_text(stdscr,"With a warm smile, he introduces himself as the master of the house.\n",0,3)
        display_text(stdscr,"Expressing sorrow for your loss, he reveals that he was a close friend of your father's.\n",0,3)
        display_text(stdscr,"He shows you a picture to validate his claim and explains that he has been anticipating your arrival to help you complete your mission.\n",0,3)
        display_text(stdscr,"Guiding you to a point between two doors, he gestures for you to make a choice.\n",0,3)
        
        
        
        stdscr.getch()
        
    
    
wrapper(main)