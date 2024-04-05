import curses
#import character
from curses import wrapper
#from character import Hero
import time

class Character:
        def __init__(self, name, health, points):
            self.name = name
            self.health = health
            self.points = points

player = Character("name", 5, 100)
tools = {"gun", "knife", "mystery item", "short bow", "torch"}

enter_temple = "???"
   
def display_text(stdscr, text, start_col, color_pair_id):
        global line_counter
        stdscr.refresh()
        time.sleep(0.2)  # Wait for a second before displaying each letter
        for i in range(len(text)):
            stdscr.addch(line_counter, start_col + i, text[i], curses.color_pair(color_pair_id))
            stdscr.refresh()
            time.sleep(0.05)
        line_counter += 1

def type(stdscr,message,i):
        for char in message:
         stdscr.addstr(char,curses.color_pair(i))
         stdscr.refresh()
         time.sleep(0.05)
         
   # line_counter = 0  # Initialize line counter

def aggressive(stdscr):
        global player
       # global enter_temple
        type(stdscr, "The guardians say:\n", 3)
        type(stdscr, "“We have been waiting for you after we received word of your father's death. However, we can see that you are not worthy of his treasure. You cannot proceed.”\n", 1)
        type(stdscr, "You have lost a life.\n", 1)
        player.health -= 1
        enter_temple = "no"
        type(stdscr,"choose again \n",3)
        approach_guardians(stdscr)
        

def polite(stdscr):
        type(stdscr, "The guardians say:\n", 3)
        type(stdscr, "”We have been waiting for you after we received word of your father's death. To acquire what your father left in our possession, you must first face the challenges that await behind this door and hand us the circle of life.”\n",1)
        
        
        
def approach_guardians(stdscr):
        type(stdscr, "How do you want your demeanor to be?\n", 3)
        type(stdscr,"1) Aggressive    2) Polite \n",5)
        choice2 = stdscr.getkey()
        if choice2 == '1':
            aggressive(stdscr)
        else:
            polite(stdscr)

def not_approach_guardians(stdscr):
        type(stdscr, "You sneaked past the temple's guards, making sure they didn't see you. As you explored around, you found an old door on the temple's wall. You tried to open it, but it was locked tight.\n", 3)
        if "mystery item" in tools:
            type(stdscr, "As you took hold of the mysterious item, you realized it was none other than the key to the door you faced. With the key in hand, you effortlessly unlocked the door and entered the temple without encountering any further obstacles.\n", 3)
        else:
            type(stdscr, "As you failed to retrieve the mystery item, you now realize its significance—it was the key to this very door. With a sinking feeling, you understand that without it, the door remains firmly locked. Accepting your fate, you prepare to confront the guardians standing before you, knowing that they are now your only path forward.\n", 3)
            approach_guardians(stdscr)


def left(stdscr):
    type(stdscr,"You are back at the crossroad.Where to look for the lamp? \n",3)
    type(stdscr,"       1) right            2)middle\n",1)
    choice = stdscr.getkey()
    if choice == '1' :
        type(stdscr," Found the lamp with no  oil. Worry not you already acquired it \n",3)
    elif choice == '2' :
        type(stdscr," it is a dead end \n",5)
        left(stdscr)
    else :
        type(stdscr," error \n",2)
        left(stdscr)


def right(stdscr):
    type(stdscr,"You are back at the crossroad.Where to look for the oil? \n",3)
    type(stdscr,"       1) left            2)middle\n",1)
    choice = stdscr.getkey()
    if choice == '1' :
        type(stdscr," good job , You found the oil \n",3)
    elif choice == '2' :
        type(stdscr," it is a dead end \n",5)
        right(stdscr)
    else :
        type(stdscr," error \n",2)
        right(stdscr)


def choix(stdscr):
    type(stdscr,"whitch way you want to go ?\n",2)
    type(stdscr,"    1) left         2) middle        3) right     \n",5)
    choice5 = stdscr.getkey()
    if choice5 == '1' :
        type(stdscr,"You acquired kerosene oil. It might help you later on. You need to find the lamp now\n",3)
        left(stdscr)
    elif choice5 == '2' :
        type(stdscr," it is a dead end \n",5)
        choix(stdscr)
    elif choice5 == '3' : 
        type(stdscr,"You find a kerosene lamp but it has no oil. You need to find the oil\n",3)
        right(stdscr)
    else :
        type(stdscr,"error try again !! \n",4)
        choix(stdscr)

           
def torch(stdscr): 
    type(stdscr,"You need to save the light's fuel.\n Quick use it to  look for something else to light the way \n",3)
    type(stdscr,"while searching for the fule , You find your self at a crossroad \n",3)
    type(stdscr,"whitch way you want to go ?\n",2)
    type(stdscr,"    1) left         2) middle        3) right     \n",5)
    choice4 = stdscr.getkey()
    if choice4 == '1' :
         type(stdscr,"You acquired kerosene oil. It might help you later on. You need to find the lamp now\n",3)
         left(stdscr)
    elif choice4 == '2' :
         type(stdscr," it is a dead end \n",5)
         choix(stdscr)
    elif choice4 == '3' :
        type(stdscr,"You find a kerosene lamp but it has no oil. You need to find the oil\n",3)
        right(stdscr)
    else :
        type(stdscr,"error try again !! \n",4)
        choix(stdscr)
        

def first_step(stdscr):
      global player
      
      type(stdscr,"As you step into the temple, you'll notice it's really dark inside. Hardly anything to see around here . \n use one of your tools to help you find your way \n",3)
      choice3 = stdscr.getstr().decode('utf-8')
      if choice3 == "torch" :
          if choice3 in tools :
              torch(stdscr)
          else :
              type(stdscr,"you do not have a torch in your inventory \n , do you want to bye one ? \n",2)
              choice = stdscr.getstr().decode('utf-8')
              if choice == "yes" :
                  player.points -= 5     # nbedlou la valeur
                  torch(stdscr)
              else :
                  type(stdscr,"one of the monsters have take of you guard \n ",3)
                  type(stdscr," you have lost a life \n",2)  
                  player.health -= 1
                  first_step(stdscr)       
      else :
          if "torch" in tools :
              type(stdscr," hint !! , you have a torch in your in inventory , you need to use it ",2)
              torch(stdscr)
          else :
              type(stdscr,"you can buy a torch that will help you , do you want to ?\n",3)
              choice = stdscr.getstr().decode('utf-8')
              if choice == "yes" :
                  player.points -= 5     # nbedlou la valeur
                  torch(stdscr)
              else :
                  type(stdscr,"one of the monsters have take of you guard \n ",3)
                  type(stdscr," you have lost a life \n",2)  
                  player.health -= 1
                  first_step(stdscr)  
     





def main(stdscr):
        
       
        stdscr.clear()
        stdscr.refresh()

        curses.start_color()
        curses.use_default_colors()

        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_RED, curses.COLOR_WHITE)

        height, width = stdscr.getmaxyx()
        footer_win = curses.newwin(1, width, height-1, 0)
         
         
         
        type(stdscr, "As you walk deeper along the path, you encounter a temple guarded by two formidable sentinels, their feline   features hinting at an otherworldly presence. These guardians, armored and armed, possess sleek fur, piercing eyes, and an aura of silent vigilance, their weapons poised for protection.\n", 3)
        type(stdscr, "What do you want to do?\n", 3)
        type(stdscr,"1) Approach the guardians    2) Look for another way in \n",5)
        choice1 = stdscr.getkey()

        if choice1 == '1':
            approach_guardians(stdscr)
            type(stdscr,"    \n",2)
        elif choice1 == '2':
            not_approach_guardians(stdscr)
            type(stdscr,"     \n",2)
       
        
        #type(stdscr,"As you step into the temple, you'll notice it's really dark inside. Hardly anything to see around here . \n use one of your tools to help you find your way \n",1)
        first_step(stdscr)
        type(stdscr,"As you continue walking  suddnely a magical cratures appears and says : \n",3)
        type(stdscr,"“ I’ve been waiting for your arrival and I’m sorry about your dad” it continues “I will lead you to the challenges. After you finish each challenges you find the pieces of the circle of life(wela haja wa5do5ra)”.",1)
       
        stdscr.getch()
       
       
wrapper(main)