import curses
from curses import wrapper
from curses.textpad import Textbox
import time

key='a'
points=100
inventory={"gun","knife","sword","lighter"}
line_counter=0

def display_text(stdscr, text,start_col,color_pair_id):
    global line_counter
    stdscr.refresh()
    time.sleep(0.2)  # Wait for a second before displaying each letter
    for i in range(len(text)):
        stdscr.addch(line_counter, start_col + i, text[i],curses.color_pair(color_pair_id))
        stdscr.refresh()
        time.sleep(0.05)
    line_counter += 1
    

#def find(inventory,key):
 #   i=0
  #  while(i<3):
   #     if(inventory[i]== key):
    #        return i
        
    #return -1


def house_entry(stdscr,key):
    display_text(stdscr,"How you want to enter the house?\n",0,1)
    display_text(stdscr,"Please press:\n",0,4)
    display_text(stdscr,"w:for window\n",2,4)
    display_text(stdscr,"d: for door\n",2,4)
    key = stdscr.getkey()
    if key == 'w':
        display_text(stdscr,"you managed to force the window open\n",0,3)
    elif key == 'd':
        display_text(stdscr,"The door is locked. you can't force it open. find another way in\n",0,2)
        house_entry(stdscr,key)
    else:
        display_text(stdscr,"Invalide choice. try again\n",0,2)
        house_entry(stdscr,key)

def door2_entery(stdscr,key):
    global points
    display_text(stdscr,"It's attacking you act quick!\n",0,4)
    display_text(stdscr,"what do you want to do?\n",0,1)
    display_text(stdscr,"Please press:\n",0,0)
    display_text(stdscr,"b: for block\n",3,4)
    display_text(stdscr,"d: for dodge\n",3,4)
    key=stdscr.getkey()
    if key == 'd':
        display_text(stdscr,"You successfully dodged.\n",0,3)
    elif key =='b':
        display_text(stdscr,"Its attack was too strong. you didn't have enough time to get into the right stance\n",0,2)
        points -= 10
        door2_entery(stdscr,key)
    else:
        display_text(stdscr,"Invalide choice. try again\n",0,2)
        door2_entery(stdscr,key)

#def door2_attack(stdscr,key,points):
 #   display_text(stdscr,"Its time for you to attack now.\n",line_counter,0,0)
  #  display_text(stdscr,"What tools do you want to use during the fight.\n",line_counter,0,1)
   # key=stdscr.getstr().decode(encoding="utf-8")
    #if key != "gun" and key != "knife":



def main (stdscr):
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    stdscr.clear()
    display_text(stdscr,"As you walk deep in this path. you encounter a house with an unwelcoming exterior\n",0,4)
    house_entry(stdscr,key)
    stdscr.refresh()
    time.sleep(1)
    stdscr.clear()
    global line_counter
    line_counter=0
    display_text(stdscr,"You used the key to open the other door. As you enter you find a giant spider.\n",0,4)
    door2_entery(stdscr,key)
    stdscr.refresh()
    time.sleep(1)
    stdscr.getch()



wrapper(main)
