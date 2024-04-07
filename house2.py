import curses
from curses import wrapper
from curses.textpad import Textbox
import time
from tools2 import Sword
from tools2 import Knife
from tools2 import Lighter
from tools2 import Mystery
from tools2 import Fangs
from tools2 import Spray
from tools2 import Fist

def clr(window):
    global line_counter
    global keyy
    window.addstr(line_counter+2,0,"PRESS ANY KEY TO CONTINUE!",curses.A_BOLD)
    keyy = window.getkey()
    window.clear()
    time.sleep(1)
    line_counter = 1
    window.refresh()



def display_text(stdscr, text,start_col,color_pair_id):
    global line_counter
    mrows, mcols = stdscr.getmaxyx()
    stdscr.refresh()
    time.sleep(0.2) 
    j=0
    if line_counter >= mrows-5:
        line_counter = 1
        stdscr.clear()
        time.sleep(1)
        line_counter = 0
        stdscr.refresh()
    
    for i in range(len(text)):
        col= start_col +j 
        stdscr.addch(line_counter, col , text[i],curses.color_pair(color_pair_id))
        stdscr.refresh()
        time.sleep(0.05)
        j += 1 
        if col>= mcols - 10 and text[i]== ' ':
            j=0
            line_counter += 1 
        

    line_counter += 1



line_counter=1

def health_bar (stdscr,character):
    global line_counter
   
    remaining_symbol = chr(0x2588)
    lost_symbol='_'
    barrier_symbol='|'
    max_bars=30
    remaining_bars=round(character.health*max_bars/character.health_max)
    lost_bars=max_bars-remaining_bars
    display_text(stdscr,f"{character.name}'s health : {character.health}/{character.health_max}",3,4)
    display_text(stdscr,f"{barrier_symbol}{remaining_symbol*remaining_bars}{lost_symbol*lost_bars}{barrier_symbol}",5,character.health_bar_color)



class Character:
    def __init__(self,name: str,health: int,tool,health_bar_color :int ) -> None:
        self.name = name
        self.health = health
        self.health_max = 100
        self.tool=tool
        self.health_bar_color = health_bar_color


    def attack(self,stdscr,target, power: int =1):
        global line_counter
        self.power=power
        target.health -= self.tool.damage*self.power
        target.health = max(target.health, 0)
        display_text(stdscr,f"{self.name} dealt a {self.tool.damage*self.power} damage to {target.name} with {self.tool.name}",0,4)
        health_bar(stdscr,target)
        health_bar(stdscr,self)
        
        
        line_counter += 2


   
key='a'
points=100
inventory=[Mystery,Knife,Sword,Lighter]



def find (inventory,key):
    for i in range(len(inventory)):
        if(key == inventory[i].name):
            return i
        return -1



def fight_show(stdscr, enemy_name : str , enemy_health : int , enemy_weapon  ,hero_health : int , hero_weapon ,hero_power: int):
    global line_counter
    hero =Character(name="Charlotte",health=hero_health,tool=hero_weapon,health_bar_color=3)
    enemy=Character(name=enemy_name,health=enemy_health,tool=enemy_weapon,health_bar_color=2)
    
    while(hero.health!=0 and enemy.health!=0 ):
            hero.attack(stdscr,enemy,hero_power)


            if enemy.health!=0:
                enemy.attack(stdscr,hero,1)

    if(hero.health==0):
        display_text(stdscr,"You lost game over\n",0,2)
        clr(stdscr)
    else:
        display_text(stdscr,f"The {enemy_name} has been defeated",0,3)
        clr(stdscr)
    
    

def help (stdscr,key,enemy_name:str,enemy_weapon,hero_health: int, enemy_health: int,hero_weapon,power):
    global line_counter
    display_text(stdscr,"Whose assistance will you seek in this dire moment?",1,1)
    display_text(stdscr,"Please press:",3,4)
    display_text(stdscr,"j: for jeremy\n",5,4)
    display_text(stdscr,"m: for the master\n",5,4)
    key=stdscr.getkey()
    line_counter +=1
    if key == 'j':
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter +=3
        jeremy=Character("jeremy",100,Spray,1)
        enemy=Character(enemy_name,enemy_health,enemy_weapon,2)
        jeremy.attack(stdscr,enemy,1)
        display_text(stdscr,"Jeremy's attack provides a crucial distraction, momentarily drawing the spider's attention away from you.",1,3)
        clr(stdscr)
        display_text(stdscr,f"Jeremy's distraction grants you the precious seconds needed to pick up your weapon and resume your assault.",1,4)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,hero_weapon,power)
        
    elif key== 'm':
        display_text(stdscr,"The master remains unable to intervene, bound by an oath sworn not to interfere with the mission.",0,2)
        display_text(stdscr,f"You're left to confront the {enemy_name} on your own, relying solely on your fists",1,2)
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        enemy=Character(enemy_name,enemy_health,enemy_weapon,2)
        hero=Character("charlotte",hero_health,Fist,3)
        enemy.attack(stdscr,hero,1)
        
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,Fist,1)
        
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        help(stdscr,key,enemy_name,enemy_weapon,hero_health,enemy_health,hero_weapon,power)
        
    

def tool_drop(stdscr,key,enemy_name :str,enemy_health: int,enemy_weapon, hero_health: int,hero_weapon,power):
    global line_counter
    display_text(stdscr,f"The {enemy_name}'s ferocious attack forces you to relinquish your weapon, the force of the blow knocking it from your grasp.\n",1,4)
    time.sleep(1)
    display_text(stdscr,"What is your next step?",1,1)
    display_text(stdscr,"Please press\n",3,4)
    display_text(stdscr,"h: to ask for help",5,4)
    display_text(stdscr,"p: to try and pick up the weapon",5,4)
    key=stdscr.getkey()
    line_counter += 1
    if key == 'p':
        clr(stdscr)
        display_text(stdscr,"Your reflexes faltered, leaving you unable to retrieve your weapon in time. Now, you must rely on your bare fists to finish the fight.",1,2)
        line_counter += 2
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        enemy=Character(enemy_name,enemy_health,enemy_weapon,2)
        hero=Character("charlotte",hero_health,Fist,3)
        enemy.attack(stdscr,hero,1)
        fight_show(stdscr,enemy_name,enemy_health,enemy_weapon,hero_health,Fist,1)
        clr(stdscr)
        
    elif key == 'h':
        help(stdscr,key,enemy_name,enemy_weapon,hero_health,enemy_health,hero_weapon,power)
       
        
          
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        tool_drop(stdscr,key,enemy_name,enemy_health,enemy_weapon,hero_health,hero_weapon,power)



def attack_area (stdscr,key,hero_weapon,hero_health:int ,enemy_name: str, enemy_weapon):
    global line_counter
    line_counter += 2
    display_text(stdscr,"Choose your target wisely. Where will you aim your strike?\n",1,1)
    display_text(stdscr,"Please press\n",3,4)
    display_text(stdscr,"o: for over the head\n",5,4)
    display_text(stdscr,"s: for sliding under\n",5,4)
    key= stdscr.getkey()
    line_counter += 1
    if key == 'o':
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,hero_weapon,1)
        clr(stdscr)
    elif key == 's':
        clr(stdscr)
        hero=Character("Charlotte",100,hero_weapon,3)
        enemy=Character(enemy_name,100,enemy_weapon,2)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        hero.attack(stdscr,enemy,2)
        enemy.attack(stdscr,hero,1)
        clr(stdscr)
        tool_drop(stdscr,key,enemy_name,enemy.health,enemy_weapon,hero.health,hero_weapon,2)
        
    else:
        display_text(stdscr,"Invalid choice. Try again",0,3)
        clr(stdscr)
        attack_area(stdscr,key,hero_weapon,hero_health,enemy_name,enemy_weapon)
        


def fight(stdscr,key,enemy_name: str,enemy_weapon,hero_health):
    global line_counter
    display_text(stdscr,"Now is your chance to strike back! Seize the moment and unleash your counterattack!\n",1,4)
    time.sleep(1)
    display_text(stdscr,"Pick your tool:",1,1)
    display_text(stdscr,f"Your options are:{inventory[0].name} ,{inventory[1].name} ,{inventory[2].name}\n",2,4)
    curses.echo()
    key= stdscr.getstr().decode('utf-8')
    curses.noecho()
    line_counter += 1
    if key == Mystery.name:
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,Mystery,1)
        clr(stdscr)
    elif key == Lighter.name:
        clr(stdscr)
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        fight_show(stdscr,enemy_name,100,enemy_weapon,hero_health,Lighter,1)
        clr(stdscr)
    elif key == Sword.name:
        attack_area(stdscr,key,Sword,hero_health,enemy_name,enemy_weapon)
        clr(stdscr)
    elif key == Knife.name:
        attack_area(stdscr,key,Knife,hero_health,enemy_name,enemy_weapon)
        clr(stdscr)
    else:
        display_text(stdscr,"Invalide choice.try again.",0,3)
        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,hero_health)
        


def door2_entery(stdscr,key,enemy_name: str,enemy_weapon):

    global line_counter
    display_text(stdscr,"As you insert the key into the lock, the mechanism clicks softly, allowing the door to swing open with a creak. Your senses are immediately assaulted by a musty odor, and as you step cautiously into the room, you're met with a chilling sight.",1,4)
    display_text(stdscr,f"Before you stands a colossal {enemy_name}, its body poised menacingly. This isn't just any {enemy_name}; it's the matriarch, the mother of all the smaller {enemy_name}s you've encountered thus far.",1,4)
    line_counter += 1
    time.sleep(1)
    display_text(stdscr,f"With a primal hiss, it lunges at you, venom dripping from its {enemy_weapon.name}. There's no time to hesitate - you must act swiftly to fend off this formidable adversary!",1,4)
    line_counter += 1
    time.sleep(1)
    display_text(stdscr,"what do you want to do?\n",1,1)
    display_text(stdscr,"Please press:\n",2,0)
    display_text(stdscr,"b: for block\n",5,4)
    display_text(stdscr,"d: for dodge\n",5,4)
    key=stdscr.getkey()
    line_counter += 1
    if key == 'd':
        display_text(stdscr,f"With lightning reflexes, you manage to sidestep the {enemy_name}'s attack just in time, narrowly avoiding its deadly strike",1,3)
        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,100)
    
    elif key =='b':
        display_text(stdscr,f"The force of its attack overwhelms you, leaving you scrambling to find your footing. Before you can even assume the proper defensive stance, the {enemy_name}'s strike lands true, catching you off guard.",1,2)
        clr(stdscr)
        line_counter += 3
        stdscr.addstr(line_counter,4,"******Fight******",curses.color_pair(5) | curses.A_BOLD)
        line_counter += 3
        hero=Character(name="charlotte",health=100,tool=Fist,health_bar_color=3)
        enemy=Character(name= enemy_name,health=100,tool=enemy_weapon,health_bar_color=2)
        enemy.attack(stdscr,hero,1)
        line_counter += 1
        stdscr.addstr(line_counter,4,"******Fight\E******",curses.color_pair(5) | curses.A_BOLD)

        clr(stdscr)
        fight(stdscr,key,enemy_name,enemy_weapon,hero.health)
        
    else:
        display_text(stdscr,"Invalide choice. try again\n",0,2)
        clr(stdscr)
        door2_entery(stdscr,key,enemy_name,enemy_weapon)



def main (stdscr):
    curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    stdscr.clear()
    global line_counter
    door2_entery(stdscr,key,"Spider",Fangs)
    stdscr.clear()
    stdscr.refresh()



wrapper(main)
